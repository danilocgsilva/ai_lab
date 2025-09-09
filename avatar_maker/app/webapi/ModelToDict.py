from domain.Models.TagRed import TagRed
from domain.Models.TagYellow import TagYellow
from domain.Models.TagGreen import TagGreen

class ModelToDict:
    @staticmethod
    def convert_model(model):
        red_message = TagRed("Mensagem vermelha")
        
        return {
            "name": model.get,
            "thinLine": model.suggestion,
            "tag": ModelToDict.convert_tag()
        }
        
    @staticmethod
    def convert_tag(tag = None):
        return {
            "tagMessage": tag.tagMessage if tag else "",
            "tagType": tag.tagType if tag else ""
        }