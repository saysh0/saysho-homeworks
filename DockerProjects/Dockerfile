FROM python:latest
LABEL authors="nikit"
WORKDIR /app
COPY memory_info.py .
COPY requirements.txt .
RUN python3 -m pip install psutil -U
ENTRYPOINT ["python3", "memory_info.py"]