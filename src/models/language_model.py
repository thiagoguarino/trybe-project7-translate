from .abstract_model import AbstractModel
from database.db import db

# file authorship: thiago guarino


# Task 1, 2, 3
class LanguageModel(AbstractModel):

    _collection = db["languages"]

    def __init__(self, data):
        super().__init__(data)

    def to_dict(self):
        return {
            "name": self.data["name"],
            "acronym": self.data["acronym"]
        }

    @classmethod
    def list_dicts(cls):
        lang_list = list()

        data = cls.find()

        for language in data:
            lang = language.to_dict()
            lang_list.append(lang)

        return lang_list
