import json
import csv


class BaseReader:
    def __init__(self) -> None:
        pass

    def read(self, filename):
        pass


class BaseWriter:
    def __init__(self) -> None:
        pass

    def dump(self, text, filename):
        pass


class TxtReader(BaseReader):
    def read(self, filename):
        with open(filename, "r") as file:
            return file.read().split("\n")


class TxtWriter(BaseWriter):
    def dump(self, text, filename):
        if isinstance(text, list):
            text = "\n".join(text)
        with open(filename, "w") as outfile:
            outfile.write(text)


class JsonReader(BaseReader):
    def read(self, filename):
        with open(filename, "r") as json_file:
            return json.load(json_file)


class JsonWriter(BaseWriter):
    def dump(self, text, filename):
        json_object = json.dumps(text)
        with open(filename, "w") as outfile:
            outfile.write(json_object)


class CsvReader(BaseReader):
    def read(self, filename):
        res = []
        with open(filename, "r") as file:
            csv_file = csv.reader(file)
            for lines in csv_file:
                res.append(lines)
        return res


class CsvWriter(BaseWriter):
    def dump(self, text, filename):
        with open(filename, "w") as outfile:
            writer = csv.writer(outfile)
            writer.writerows(text)


def read_data(fileobj, reader: BaseReader):
    return reader.read(fileobj)


def dump_data(data, fileobj, writer: BaseWriter):
    writer.dump(data, fileobj)
