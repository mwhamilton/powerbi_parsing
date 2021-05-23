import json
from pprint import pprint
from . import utils, data_model_schema

class BaseVisual:
    def __init__(self, raw_data) -> None:
        self._config = raw_data['config']
        self.height = raw_data['height']
        self.width = raw_data['width']
        self.position = {
            'x': raw_data['x'],
            'y': raw_data['y'],
            'z': raw_data['z'],
        }
        self.filters = json.loads(raw_data['filters'])
        self.dependencies = self._get_dependencies(raw_data)

    def _get_dependencies(self, raw_data):
        dependencies = []
        if 'dataTransforms' in raw_data:
            for data_element in json.loads(raw_data['dataTransforms'])['selects']:
                dependencies.extend(data_model_schema.Expression(data_element['expr']).sources)
        if 'filters' in raw_data:
            for data_element in json.loads(raw_data['filters']):
                dependencies.extend(data_model_schema.Expression(data_element['expression']).sources)
        return dependencies

    def __dict__(self):
        return {
            "config": json.dumps(self._config),
            "height": self.height,
            "width": self.width,
            "x": self.position['x'],
            "y": self.position['y'],
            "z": self.position['z'],
            "filters": json.dumps(self.filters),
        }

    def __str__(self):
        return str(self.__dict__())


class TextBox(BaseVisual):
    def __init__(self, raw_data) -> None:
        self.visual_type = 'textbox'
        super().__init__(raw_data)
        self.text = raw_data['config']['singleVisual']['objects']['general'][0]['properties']['paragraphs']


class TableEx(BaseVisual):
    def __init__(self, raw_data) -> None:
        self.visual_type = 'table'
        super().__init__(raw_data)


class ColumnChart(BaseVisual):
    def __init__(self, raw_data) -> None:
        super().__init__(raw_data)
        self.legend = self._config['singleVisual']['projections']['Series'][0]['queryRef']
        self.y_axis = self._config['singleVisual']['projections']['Y'][0]['queryRef']
        self.x_axis = self._config['singleVisual']['projections']['Category'][0]['queryRef']
        self.title = self._get_title()
    
    def _get_title(self):
        if 'vcObjects' in self._config['singleVisual']:
            return utils.Text(self._config['singleVisual']['vcObjects']['title'][0]['properties']['text']).text


visuals = {
    'textbox': TextBox,
    'tableEx': TableEx,
    'columnChart': ColumnChart,
}


def parse_visual(raw_data: dict) -> BaseVisual:
    raw_data['config'] = json.loads(raw_data['config'])
    if raw_data['config']['singleVisual']['visualType'] not in visuals:
        print(raw_data['config']['singleVisual']['visualType'])
    return visuals.get(
        raw_data['config']['singleVisual']['visualType'],
        BaseVisual
    )(raw_data)
