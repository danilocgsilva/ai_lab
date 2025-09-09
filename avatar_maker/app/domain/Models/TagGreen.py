class TagGreen:
    def __init__(self, message: str):
        self._name = message
        self._level = "green"
        
    @property
    def tagMessage(self):
        return self._name
    
    @property
    def tagType(self):
        return self._level
