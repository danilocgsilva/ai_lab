class TagYellow:
    def __init__(self, message: str):
        self._name = message
        self._level = "yellow"
        
    @property
    def tagMessage(self):
        return self._name
    
    @property
    def tagType(self):
        return self._level
