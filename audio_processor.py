from pydub import AudioSegment


class AudioProcessor:
    def __init__(self, file_path):
        self.audio = AudioSegment.from_file(file_path)

    def crop(self, start_ms, end_ms):
        self.audio = self.audio[start_ms:end_ms]

    def overlay(self, other_audio):
        self.audio = self.audio.overlay(other_audio)

    def export(self, output_path, format="mp3"):
        self.audio.export(output_path, format=format)

    def adjust_volume(self, db):
        self.audio = self.audio + db

    def add(self, other_audio):
        self.audio = self.audio.add(other_audio)


# 示例用法
if __name__ == "__main__":
    # 创建 AudioProcessor 实例
    processor = AudioProcessor("input_audio.mp3")

    # 裁剪音频文件
    processor.crop(1000, 5000)

    # 加载要叠加的音频文件
    overlay_audio = AudioSegment.from_file("overlay_audio.mp3")

    # 叠加音频文件(会将两个音频叠加在一起)
    processor.overlay(overlay_audio)

    # 调整音量
    processor.adjust_volume(3)

    # 导出处理后的音频文件
    processor.export("output_audio.mp3")

    # 音频连接
    add_audio = AudioSegment.from_file("overlay_audio.mp3")
    processor.add(add_audio)
