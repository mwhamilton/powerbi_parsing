import json
from pprint import pprint


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


class TextBox(BaseVisual):
    def __init__(self, raw_data) -> None:
        self.visual_type = 'textbox'
        super().__init__(raw_data)
        self.text = raw_data['config']['singleVisual']['objects']['general'][0]['properties']['paragraphs']

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


visuals = {
    'textbox': TextBox
}


def parse_visual(raw_data: dict) -> BaseVisual:
    raw_data['config'] = json.loads(raw_data['config'])
    return visuals.get(
        raw_data['config']['singleVisual']['visualType'],
        BaseVisual
    )(raw_data)
