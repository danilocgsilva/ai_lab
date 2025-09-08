class Model:
    
    def __init__(self, name, suggestion):
        self._name = name
        self._suggestion = suggestion
        self._url = f"https://huggingface.co/{name}"
        self._with_url = False
        
    def withUrl(self):
        self._with_url = True
        return self
        
    @property
    def get(self):
        if self._with_url:
            return self._url
        return self._name
    
    @property
    def suggestion(self):
        return self._suggestion
    