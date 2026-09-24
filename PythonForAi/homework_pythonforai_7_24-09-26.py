import torch
import clip
from PIL import Image
import requests
import io
import os
from dotenv import load_dotenv

#task 1

def setup_clip():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Device: {device}")
    return device

def open_image_url(url):
    response = requests.get(url)
    return Image.open(io.BytesIO(response.content))

def open_image_file(file_path):
    return Image.open(file_path)


def text_to_image(model, processor, text_queries, images, device):
    text_inputs = clip.tokenize(text_queries).to(device)
    with torch.no_grad():
        text_features = model.encode_text(text_inputs)
        text_features /= text_features.norm(dim=-1, keepdim=True)
    image_inputs = torch.stack([processor(img).to(device) for img in images])
    with torch.no_grad():
        image_features = model.encode_image(image_inputs)
        image_features /= image_features.norm(dim=-1, keepdim=True)
    similarity = (100.0 * text_features @ image_features.T).softmax(dim=-1)
    return similarity.cpu().numpy()

def main():
    device = setup_clip()
    print("Loading CLIP model...")
    model, processor = clip.load("ViT-B/32", device=device)
    print("\nExample 1: Comparing prompts to images")
    image_urls = [
        "https://cdn.shopify.com/s/files/1/0086/0795/7054/files/Golden-Retriever.jpg?v=1645179525",  # Собака
        "https://miro.medium.com/v2/resize:fit:1400/1*tMKkGydXuiOBOb15srANvg@2x.jpeg"  # Закат
    ]

    try:
        images = [open_image_url(url) for url in image_urls]
        print(f"Loaded {len(images)} images")
    except Exception as e:
        print(f"Error loading images: {e}")
        print("Falling back to local images")
        return
    text_queries = ["a gym", "a video game"]
    similarities = text_to_image(model, processor, text_queries, images, device)
    print("Similarity results:")
    for i, text in enumerate(text_queries):
        print(f"\nText: '{text}'")
        for j, url in enumerate(image_urls):
            print(f"  Image {j + 1}: {similarities[i][j] * 100:.2f}%")
    print("\nExample 2: Zero-shot image classification")
    image = images[1]
    labels = ["a photo of a gym", "a photo of a video game"]
    image_input = processor(image).unsqueeze(0).to(device)
    text_inputs = clip.tokenize(labels).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_inputs)
        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)
        logits_per_image = (100.0 * image_features @ text_features.T).softmax(dim=-1)
        probs = logits_per_image.cpu().numpy()[0]
    print("\nClassification Results:")
    for i, label in enumerate(labels):
        print(f"{label}: {probs[i] * 100:.2f}%")


if __name__ == "__main__":
    main()

#task 2

def setup_env():
    load_dotenv()
    hf_token = os.getenv("HF_TOKEN")
    if not hf_token:
        print("No Hugging Face token found. You need to:")
        print("1. Create a free account at huggingface.co")
        print("2. Get your token at huggingface.co/settings/tokens")
        print("3. Create a .env file with HF_TOKEN=your_token_here")
        hf_token = input("Or enter your Hugging Face token now: ")
    return hf_token


def generate_image(prompt, token, negative_prompt="", model_id="CompVis/stable-diffusion-v1-4", num_inference_steps=30):
    API_URL = f"https://api-inference.huggingface.co/models/{model_id}"
    headers = {
        "Authorize": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "inputs": prompt,
        "parameters": {
            "negative_prompt": negative_prompt,
            "num_inference_steps": num_inference_steps,
        }
    }
    print(f"Generating image for prompt: '{prompt}'")
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code}, {response.text}")
    image = Image.open(io.BytesIO(response.content))
    return image


def save_image(image, filename="generated_image.png"):
    image.save(filename)
    print(f"Image saved as {filename}")
    return filename


def main():
    token = setup_env()
    prompts = ["The gold gym with gold equipment in gym", "Perfect gaming room",]
    for i, prompt in enumerate(prompts):
        try:
            image = generate_image(
                prompt=prompt,
                token=token,
                negative_prompt="blurry, bad quality, distorted, ugly",
                num_inference_steps=25
            )
            filename = f"generated_image_{i + 1}.png"
            save_image(image, filename)
            try:
                from IPython.display import display
                display(image)
            except ImportError:
                print(f"Image generated correctly and saved to{filename}")
        except Exception as e:
            print(f"Error generating'{prompt}': {e}")

if __name__ == "__main__":
    main()