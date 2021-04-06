from enum import Enum
from typing import List

import spacy
from pydantic import BaseModel, Field


class ModelName(str, Enum):
    en_core_web_sm = "en_core_web_sm"


DEFAULT_MODEL = ModelName.en_core_web_sm
MODEL_NAMES = [model.value for model in ModelName]
MODELS = {name: spacy.load(name) for name in MODEL_NAMES}


class Article(BaseModel):
    text: str


class RequestModel(BaseModel):
    articles: List[Article]
    model: ModelName = DEFAULT_MODEL


class Entity(BaseModel):
    text: str
    label: str
    start: int
    end: int


class Prediction(BaseModel):
    text: str
    entities: List[Entity] = Field(default_factory=list)


class ResponseModel(BaseModel):
    result: List[Prediction]
