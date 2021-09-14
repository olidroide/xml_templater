import argparse
import xml.etree.ElementTree as ET


class ParserXML:
    tree = None
    root: ET.XML = None

    def __init__(self, input_file) -> None:
        super().__init__()
        self.tree = ET.parse(input_file)
        self.root = self.tree.getroot()

    def parse_xml(self) -> dict:
        final_dict = dict()
        for key, value in self.parse_child_xml(self.root):
            final_dict[key.lower()] = value
        print(f"parse_xml: {final_dict}")
        return final_dict

    @staticmethod
    def parse_child_xml(parent_element: ET.XML):
        key = parent_element.tag
        saved_value = None

        for child in parent_element:
            if ParserXML._is_leaf(child):
                if child.tag.endswith("ID"):
                    saved_value = child.text
                    continue

                if saved_value:
                    print(f"key: {key}\tsaved_value: {saved_value} child.tag: {child.tag}")
                    yield f"{key}.{saved_value}.{child.tag}", child.text

            else:
                for subkey, value in ParserXML.parse_child_xml(child):
                    print(f"\tkey: {key}\t\tsubkey: {subkey}")
                    if saved_value:
                        yield f"{saved_value}.{key}.{subkey}", value
                        saved_value = None
                    else:
                        yield f"{key}.{subkey}", value

    @staticmethod
    def _is_leaf(element) -> bool:
        return len(list(element)) <= 0


class FileHandler:
    _path: str

    def __init__(self, path: str) -> None:
        super().__init__()
        self._path = path


class InputData(FileHandler):
    def get_dict(self) -> dict:
        return ParserXML(input_file=self._path).parse_xml()


class TemplateData(FileHandler):
    def get_template(self) -> str:
        with open(self._path) as f:
            output_text = f.read()

        return output_text

    def replace_keys(self, dict_to_replace: dict) -> str:
        output_text = self.get_template()
        for key, value in dict_to_replace.items():
            output_text = output_text.replace(f"*|{key}|*", value)
        return output_text


class OutputData(FileHandler):

    def __init__(self) -> None:
        super().__init__(path="output.txt")

    def write_output(self, text: str):
        print(text)
        with open(self._path, "w") as f:
            f.write(text)


def start():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Input XML data")
    parser.add_argument("-t", "--template", help="Template in txt format")
    args = parser.parse_args()
    input_path = args.input
    template_path = args.template

    parsed_dict = InputData(path=input_path).get_dict()
    output_text = TemplateData(path=template_path).replace_keys(parsed_dict)
    OutputData().write_output(output_text)


if __name__ == "__main__":
    start()
