from pprint import pprint
from . import visuals


class Layout:
    def __init__(self, raw_data: dict) -> None:
        self.id = raw_data['id']
        self.resourcePackages = raw_data['resourcePackages']
        self.sections = [Section(raw_section_data) for raw_section_data in raw_data['sections']]
        self.config = raw_data['config']
        self.layoutOptimization = raw_data['layoutOptimization']

    def __dict__(self) -> dict:
        return {
            'id': self.id,
            'resourcePackages': self.resourcePackages,
            'sections': [x.__dict__() for x in self.sections],
            'config': self.config,
            'layoutOptimization': self.layoutOptimization
        }


class Section:
    def __init__(self, raw_data) -> None:
        self.id = raw_data.get('id')
        self.name = raw_data['name']
        self.display_name = raw_data['displayName']
        self.filters = raw_data['filters']
        self.ordinal = raw_data['ordinal']
        self.visualContainers = [visuals.parse_visual(x) for x in raw_data['visualContainers']]
        self.config = raw_data['config']
        self.dispay_option = raw_data['displayOption']
        self.dimensions = {'width': raw_data['width'], 'height': raw_data['height']}

    def __dict__(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'displayName': self.display_name,
            'filters': self.filters,
            'ordinal': self.ordinal,
            'visualContainers': [x.__dict__() for x in self.visualContainers],
            'config': self.config,
            'displayOption': self.dispay_option,
            'width': self.dimensions['width'],
            'height': self.dimensions['height'],
        }

    def __str__(self):
        return str(self.__dict__())