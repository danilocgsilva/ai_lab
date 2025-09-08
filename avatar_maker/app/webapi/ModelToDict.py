class ModelToDict:
    @staticmethod
    def convert(model):
        return {
            "name": model.get,
            "thinLine": model.suggestion,
            "tag": {
                "tagMessage": "",
                "tagType": ""
            }
        }