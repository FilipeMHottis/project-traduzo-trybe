from models.abstract_model import AbstractModel
from typing import Dict, List
from database.db import db


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data: Dict) -> None:
        self.data = data

    def to_dict(self) -> Dict:
        return {"name": self.data["name"], "acronym": self.data["acronym"]}

    @classmethod
    def list_dicts(cls) -> List[Dict]:
        all_languages = cls._collection.find()
        return [
            {
                "name": language["name"],
                "acronym": language["acronym"],
                "_id": language["_id"],
            }
            for language in all_languages
        ]
