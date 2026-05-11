#task1 Воспроизведение мультимедиа.
# Создайте два класса:
# AudioFileMixin — требует наличие поля audio_tracks (список треков).
# Метод play_audio() выводит:
# Воспроизведение аудио для <НазваниеКласса>:
# <название трека>
# <название трека>
# VideoFileMixin — требует наличие поля video_files (список видео).
# Метод play_video() выводит:
# Воспроизведение видео для <НазваниеКласса>:
# <название видео>
# <название видео>
# Если нужное поле отсутствует — выбрасывайте AttributeError.

#task2 Устройства.
# Создайте два класса:
# MediaPlayer — поддерживает только аудио. Принимает список треков.
# Laptop — поддерживает аудио и видео. Принимает списки треков и видео.
# Проверьте работу классов, вызвав методы воспроизведения.
# Данные:
# tracks = ["track1.mp3", "track2.mp3"]
# movies = ["movie.mp4", "trailer.mov"]
# Пример вывода:
# Воспроизведение аудио для MediaPlayer:
# track1.mp3
# track2.mp3
# Воспроизведение аудио для Laptop:
# track1.mp3
# track2.mp3
# Воспроизведение видео для Laptop:
# movie.mp4
# trailer.mov

class AudioFileMixin:
    """Миксин для добавления функционала воспроизведения аудио."""
    def play_audio(self) -> str:
        return (f"Воспроизведение видео для {self.__class__.__name__}:\n"
                + "\n".join(self.audio_files))


class VideoFileMixin:
    """Миксин для добавления функционала воспроизведения видео."""
    def play_video(self) -> str:
        return (f"Воспроизведение видео для {self.__class__.__name__}:\n"
                + "\n".join(self.video_files))

class MediaPlayer(AudioFileMixin):
    """Класс медиаплеера, поддерживающий только аудио."""
    def __init__(self, audio_files: list) -> None:
        """Инициализирует плеер списком аудиофайлов."""
        if not isinstance(audio_files, list):
            raise TypeError("Аудиофайлы должны быть переданы в виде списка!")
        self.audio_files = audio_files

    def __getattr__(self, name):
        raise AttributeError('Но но но мистер фиш!')

class Laptop(AudioFileMixin, VideoFileMixin):
    """Класс ноутбука, поддерживающий аудио и видео."""
    def __init__(self, audio_files: list, video_files: list) -> None:
        """Инициализирует ноутбук списками аудио и видеофайлов."""
        if not isinstance(audio_files, list) or not isinstance(video_files, list):
            raise TypeError("Файлы должны быть переданы в виде списков!")
        self.audio_files = audio_files
        self.video_files = video_files

    def __getattr__(self, name):
        raise AttributeError('Но но но мистер фиш!')

tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]
m = MediaPlayer(tracks)
print(m.play_audio())
l = Laptop(tracks, movies)
print(l.play_audio())
print(l.play_video())