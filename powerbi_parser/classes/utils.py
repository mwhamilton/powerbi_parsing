class Text:
    def __init__(self, config):
        self.config = config
        self.text = self._get_text()
    
    def _get_text(self):
        return self.config['expr']['Literal']['Value']
    