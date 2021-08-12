class File:
    def __init__(self, filename: str) -> None:
        self.data = open(filename)

    def save(self):
        pass

class VideoFile(File):
    pass

class Codec:
    name='Base Codec'

class OggCompressionCodec(Codec):
    name='Compression Codec'

class MPEG4CompressionCodec(Codec):
    name='MPEG4 Compression Codec'

class CodecFactory:
    def extract(self, _file: File) -> str:
        return f"Extracting {_file.__dict__}"

class Buffer:
    pass

class BitrateReader(Buffer):
    _file: File
    def read(self, filename: str, sourceCodec: Codec) -> str:
        self._file = File(filename)
        return f"Reading {filename} with {sourceCodec.name}"

    def convert(self, buffer: Buffer, destinationCodec: Codec) -> File:
        return self._file

class AudioMixer:
    def fix(self, _file: File) -> str:
        return f"Fixing {_file.__dict__}"
