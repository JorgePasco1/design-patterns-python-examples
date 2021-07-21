from abc import ABC, abstractmethod
from typing import Union
import zlib


# The component Interface defines operations that can be altered by decorators.
class DataSource(ABC):
    @abstractmethod
    def write_data(self, data: str) -> None:
        pass

    @abstractmethod
    def read_data(self) -> str:
        pass


# Concrete components provide default implementations for the operations. There
# might be several variations of these classes in a program
class FileDataSource(DataSource):
    filename: str

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def write_data(self, data: Union[str, bytes]) -> None:
        write_mode = 'w' if isinstance(data, str) else 'wb'
        with open(self.filename, write_mode) as _file:
            _file.write(data)

    def read_data(self) -> str:
        with open(self.filename, 'rb') as _file:
            content = _file.read()
            return content


# The base decorator class follows the same interface as the other components.
# The primary purpose of this class is to define the wrapping interface for all
# concrete decorators. The default implementation of the wrapping code might
# include a field for storing a wrapped component and the means to initialize it.
class DataSourceDecorator(DataSource):
    _wrappee: DataSource

    def __init__(self, source: DataSource) -> None:
        self._wrappee = source

    # The base decorator simply delegates all work to the wrapped component. Extra
    # behaviors can be added in concrete decorators.
    def write_data(self, data: str) -> None:
        self._wrappee.write_data(data)

    # Concrete decorators may call the parent implementation of the operation
    # instead of calling the wrapped object directly. This approach simplifies
    # extension of decorator classes.
    def read_data(self) -> str:
        return self._wrappee.read_data()


# Concrete decorators must call methods on the wrapped object, but may add
# something of their own to the result. Decorators can execute the added behavior
# either before or after the call to a wrapped object.
class EncryptionDecorator(DataSourceDecorator):
    def write_data(self, data: str) -> None:
        encrypted_data = data[::-1]
        self._wrappee.write_data(encrypted_data)

    def read_data(self) -> str:
        encrypted_data = self._wrappee.read_data()
        result = encrypted_data[::-1]
        return result


class CompressionDecorator(DataSourceDecorator):
    def write_data(self, data: str) -> None:
        compressed_data = zlib.compress(data.encode())
        self._wrappee.write_data(compressed_data)

    def read_data(self) -> str:
        compressed_data = self._wrappee.read_data()
        result = zlib.decompress(compressed_data)
        return result


class Program:
    def generic_usage(self):
        example_text = """Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nam tenetur dolores dolor quo cum est incidunt temporibus minima fuga. Minus libero qui beatae! Voluptatum, distinctio placeat quia ullam quis accusantium.
Porro blanditiis commodi sint doloremque iusto eius voluptatem error sequi debitis cupiditate atque eaque odit sunt inventore nulla, voluptas nam aliquam quisquam incidunt quae optio illum aperiam a? Veritatis, mollitia."""

        original_source = FileDataSource('./datasource')
        original_source.write_data(example_text)
        print(original_source.read_data())

        source = CompressionDecorator(original_source)
        source.write_data(example_text)
        print(source.read_data())

        source = EncryptionDecorator(original_source)
        source.write_data(example_text)
        print(source.read_data())


def run():
    program = Program()
    program.generic_usage()


if __name__ == "__main__":
    run()
