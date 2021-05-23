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
