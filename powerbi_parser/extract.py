import os
import zipfile
import json
import xml.etree.ElementTree as ET
from pprint import pprint
from .classes import layout, data_model_schema
from typing import List


class PowerBI:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.zip = self._get_zip()
        self.content_types = self._get_content_types()
        self.data_model_schema = self._get_data_model_schema()
        self.diagram_layout = self._get_diagram_layout()
        self.layout = self._get_layout()
        self.metadata = self._get_metadata()
        self.settings = self._get_settings()
        self.static_resources = self._get_static_resources()
        self.version = self._get_version()

    def _get_zip(self) -> zipfile.ZipFile:
        return zipfile.ZipFile(self.file_path, "r")

    def _get_content_types(self):
        return ET.fromstring(self.zip.open('[Content_Types].xml').read().decode('utf-8'))

    def _save_content_types(self, zip):
        x = self.zip.open('[Content_Types].xml').read()
        y = b'\xef\xbb\xbf' + ET.tostring(self.content_types, encoding='utf8', method='xml') \
                                .replace(b"ns0:", b"") \
                                .replace(b":ns0", b"") \
                                .replace(b"utf8", b"utf-8")
        zip.open('[Content_Types].xml', 'w').write(y)

    def _get_data_model_schema(self) -> dict:
        raw_data = json.loads(self.zip.open('DataModelSchema').read().decode('utf-16-le'))
        return data_model_schema.DataModelSchema(raw_data)

    def _save_data_model_schema(self, zip):
        zip.open('DataModelSchema', 'w').write(json.dumps(self.data_model_schema.__dict__()).encode("utf-16-le"))

    def _get_diagram_layout(self) -> dict:
        return json.loads(self.zip.open('DiagramLayout').read().decode('utf-16-le'))

    def _save_diagram_layout(self, zip):
        zip.open('DiagramLayout', 'w').write(json.dumps(self.diagram_layout).encode("utf-16-le"))
       
    def _get_layout(self) -> layout.Layout:
        raw_data = json.loads(self.zip.open('Report/Layout').read().decode('utf-16-le'))
        return layout.Layout(raw_data)

    def _save_layout(self, zip):
        zip.open("Report/Layout", "w").write(json.dumps(self.layout.__dict__()).encode("utf-16-le"))

    def _get_metadata(self) -> dict:
        return json.loads(self.zip.open('Metadata', 'r').read().decode('utf-16-le'))

    def _save_metadata(self, zip) -> None:
        zip.open('Metadata', 'w').write(json.dumps(self.metadata).encode("utf-16-le"))

    def _get_security_bindings(self):
        raise NotImplementedError

    def _save_security_bindings(self, zip):
        raise NotImplementedError

    def _get_settings(self):
        return json.loads(self.zip.open('Settings', 'r').read().decode('utf-16-le'))

    def _save_settings(self, zip) -> None:
        zip.open('Settings', 'w').write(json.dumps(self.settings).encode('utf-16-le'))

    def _get_static_resources(self) -> List[dict]:
        static_resources = []
        for file_path in self.zip.namelist():
            if file_path.startswith("Report/StaticResources"):
                static_resources.append({
                    'file_path': file_path,
                    'data': json.loads(self.zip.open(file_path, 'r').read().decode('utf-8'))
                })
        return static_resources

    def _save_static_resources(self, zip) -> None:
        for file_info in self.static_resources:
            zip.open(file_info['file_path'], 'w').write(json.dumps(file_info['data']).encode("utf-8"))

    def _get_version(self) -> str:
        return self.zip.open('Version', 'r').read().decode('utf-16-le')

    def _save_version(self, zip) -> None:
        zip.open('Version', 'w').write(self.version.encode("utf-16-le"))

    def save(self, file_path: str) -> None:
        with zipfile.ZipFile(file_path, 'w') as zip:
            self._save_version(zip)
            self._save_static_resources(zip)
            self._save_settings(zip)
            self._save_metadata(zip)
            self._save_layout(zip)
            self._save_diagram_layout(zip)
            self._save_data_model_schema(zip)
            self._save_content_types(zip)
