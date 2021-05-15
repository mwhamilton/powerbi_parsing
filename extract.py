import os
import zipfile
import json
from bs4 import BeautifulSoup
from pprint import pprint
from classes import layout
from typing import List
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class PowerBI:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.zip = self._get_zip()

    def _get_zip(self) -> zipfile.ZipFile:
        return zipfile.ZipFile(self.file_path, "r")

    def get_content_types(self):
        return BeautifulSoup(self.zip.open('[Content_Types].xml').read().decode('utf-8'), 'lxml')

    def get_data_model_schema(self) -> dict:
        return json.loads(self.zip.open('DataModelSchema').read().decode('utf-16-le'))

    def get_diagram_layout(self) -> dict:
        return json.loads(self.zip.open('DiagramLayout').read().decode('utf-16-le'))

    def get_layout(self) -> layout.Layout:
        raw_data = json.loads(self.zip.open('Report/Layout').read().decode('utf-16-le'))
        return layout.Layout(raw_data)

    def get_metadata(self) -> dict:
        return json.loads(self.zip.open('Metadata', 'r').read().decode('utf-16-le'))

    def get_security_bindings(self):
        raise NotImplementedError

    def get_settings(self):
        return json.loads(self.zip.open('Settings', 'r').read().decode('utf-16-le'))

    def get_static_resources(self) -> List[dict]:
        static_resources = []
        for file_path in self.zip.namelist():
            if file_path.startswith("Report/StaticResources"):
                static_resources.append({
                    'file_path': file_path,
                    'data': json.loads(self.zip.open(file_path, 'r').read().decode('utf-8'))
                })
        return static_resources

    def get_version(self) -> str:
        return self.zip.open('Version', 'r').read().decode('utf-16-le')


powerbi = PowerBI('test.pbit')
page = powerbi.get_layout().sections[0]
print(page)