class Layout:
    def __init__(self, raw_data):
        self.id = raw_data['id']
        self.resourcePackages = raw_data['resourcePackages']
        self.sections = [Section(raw_section_data) for raw_section_data in raw_data['sections']]
        self.config = raw_data['config']
        self.layoutOptimization = raw_data['layoutOptimization']


class Section:
    def __init__(self, raw_data):
        self.id = raw_data['id']
        self.name = raw_data['name']
        self.display_name = raw_data['displayName']
        self.filters = raw_data['filters']
        self.ordinal = raw_data['ordinal']
        self.visualContainers = raw_data['visualContainers']
        self.config = raw_data['config']
        self.dispay_option = raw_data['displayOption']
        self.dimensions = {'width': raw_data['width'], 'height': raw_data['height']}
