import os
import zipfile
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class PowerBI:
    def __init__(self, file_path):
        self.file_path = file_path
        self.zip = self._get_zip()

    def _get_zip(self):
        return zipfile.ZipFile(self.file_path, "r")

    def get_metadata(self):
        return self.zip.open('Metadata', 'r').read().decode('utf-16-le')


powerbi = PowerBI('test.pbit')
powerbi.get_metadata()