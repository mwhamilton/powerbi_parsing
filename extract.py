import os
import zipfile
import json
from bs4 import BeautifulSoup
from pprint import pprint
from classes import layout
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class PowerBI:
    def __init__(self, file_path):
        self.file_path = file_path
        self.zip = self._get_zip()

    def _get_zip(self):
        return zipfile.ZipFile(self.file_path, "r")

    def get_content_types(self):
        return BeautifulSoup(self.zip.open('[Content_Types].xml').read().decode('utf-8'), 'lxml')

    def get_data_model_schema(self):
        return json.loads(self.zip.open('DataModelSchema').read().decode('utf-16-le'))

    def get_diagram_layout(self):
        return json.loads(self.zip.open('DiagramLayout').read().decode('utf-16-le'))

    def get_layout(self):
        raw_data = json.loads(self.zip.open('Report/Layout').read().decode('utf-16-le'))
        return layout.Layout(raw_data)

    def get_metadata(self):
        return json.loads(self.zip.open('Metadata', 'r').read().decode('utf-16-le'))

    def get_security_bindings(self):
        raise NotImplementedError

    def get_settings(self):
        return json.loads(self.zip.open('Settings', 'r').read().decode('utf-16-le'))

    def get_static_resources(self):
        static_resources = []
        for file_path in self.zip.namelist():
            if file_path.startswith("Report/StaticResources"):
                static_resources.append({
                    'file_path': file_path,
                    'data': json.loads(self.zip.open(file_path, 'r').read().decode('utf-8'))
                })
        return static_resources

    def get_version(self):
        return self.zip.open('Version', 'r').read().decode('utf-16-le')


powerbi = PowerBI('test.pbit')
pprint(powerbi.get_layout())