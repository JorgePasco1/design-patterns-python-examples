from video_conversion_framework import *

# Facade class to hide framework's complexity behind a simple interface. Tradeoff between funcionality and simplicity.
class VideoConverter:
    def convert(self, filename: str, _format: str) -> File:
        _file = VideoFile(filename)
        sourceCodec = CodecFactory.extract(_file)
        if (_format == "mp4"):
            destinationCodec = MPEG4CompressionCodec()
        else:
            destinationCodec = OggCompressionCodec()

        buffer = BitrateReader.read(filename, sourceCodec)
        result = BitrateReader.convert(buffer, destinationCodec)
        result = (AudioMixer()).fix(result)
        return File(result)

class Application:
    def main(self):
        convertor = VideoConverter()
        mp4 = convertor.convert("funny-cats-video.ogg", "mp4")
        mp4.save()
