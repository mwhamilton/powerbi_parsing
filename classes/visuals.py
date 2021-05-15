import json
from pprint import pprint


class BaseVisual:
    def __init__(self, raw_data):
        self._config = raw_data['config']
        self.height = raw_data['height']
        self.width = raw_data['width']
        self.position = {
            'x': raw_data['x'],
            'y': raw_data['y'],
            'z': raw_data['z'],
        }
        self.filters = json.loads(raw_data['filters'])


class TextBox(BaseVisual):
    def __init__(self, raw_data) -> None:
        self.visual_type = 'textbox'
        super().__init__(raw_data)
        self.text = raw_data['config']['singleVisual']['objects']['general'][0]['properties']['paragraphs']


visuals = {
    'textbox': TextBox
}


def parse_visual(raw_data):
    raw_data['config'] = json.loads(raw_data['config'])
    visuals.get(
        raw_data['config']['singleVisual']['visualType'],
        BaseVisual
    )(raw_data)
