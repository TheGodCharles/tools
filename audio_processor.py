import pydub
import httpx
import io


class AudioProcessor:
    def __init__(self, source_url):
        self.content = httpx.get(source_url, verify=False).content
        self.audio = pydub.AudioSegment.from_mp3(io.BytesIO(self.content))

    def crop(self, start_ms, end_ms=None):
        # 当end_ms=None开始截到末尾
        audio_slice = slice(start_ms, end_ms)
        self.audio = self.audio[audio_slice]

    def overlay(self, other_audio):
        self.audio = self.audio.overlay(other_audio)

    def silent(self, duration=0, place='front'):
        if place == 'front':
            self.audio = pydub.AudioSegment.silent(duration=duration) + self.audio
        else:
            self.audio = self.audio + pydub.AudioSegment.silent(duration=duration)

    def combined(self, add_audio, place='front'):
        if place == 'front':
            self.audio = add_audio + self.audio
        else:
            self.audio = self.audio + add_audio

    def export(self, output_path, format="mp3"):
        self.audio.export(output_path, format=format)

    def adjust_volume(self, db):
        self.audio = self.audio + db


# 示例用法
if __name__ == "__main__":
    # 创建 AudioProcessor 实例
    source_url = 'https://xxxx.com'
    processor = AudioProcessor(source_url)

    # 裁剪音频文件
    processor.crop(1000, 5000)

    # 加载要叠加的音频文件
    add_url = 'https://yyyy.com'
    overlay_audio = AudioProcessor(add_url)

    # 叠加音频文件(会将两个音频叠加在一起)
    processor.overlay(overlay_audio)

    # 调整音量
    processor.adjust_volume(3)

    # 导出处理后的音频文件
    output_path = io.BytesIO()
    processor.export(output_path, 'mp3')
