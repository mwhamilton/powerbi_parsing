import re 
basic_source = re.compile(" [^ ']+?\[.+?\]")  # matches " positions[salary]" in "aslkdm salkdj positions[salary] * 2"
with_spaces_source = re.compile("'[^']+'\[.+?\]")  # matches 


class Text:
    def __init__(self, config):
        self.config = config
        self.text = self._get_text()
    
    def _get_text(self):
        return self.config['expr']['Literal']['Value']

    def __dict__(self):
        return self.config

    def __str__(self) -> str:
        return str(self.__dict__())


def extract_sources_from_dax(text):
    def parse_source(source):
        table, col = source.split('[')
        table = table.strip("'")  # tables with spaces will be surrounded by single quotes
        col = col[:-1]  # the col begins and ends with []. We removed the first in the split, but still need to remove the last
        return {
            'table': table,
            'column': col
        }

    sources = []
    for source_re in [basic_source, with_spaces_source]:
        sources.extend(re.findall(source_re, text))
    return [parse_source(x) for x in sources]