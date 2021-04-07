from enum import Enum
from typing import List

import spacy
from pydantic import BaseModel, Field


class Model(str, Enum):
    en_core_web_sm = "en_core_web_sm"


DEFAULT_MODEL = Model.en_core_web_sm
MODEL_NAMES = [model.value for model in Model]
MODELS = {name: spacy.load(name) for name in MODEL_NAMES}


class Example(BaseModel):
    text: str


class PredictRequest(BaseModel):
    examples: List[Example]
    model: Model = DEFAULT_MODEL


class Entity(BaseModel):
    text: str
    label: str
    start: int
    end: int


class Prediction(BaseModel):
    text: str
    entities: List[Entity] = Field(default_factory=list)


class PredictResponse(BaseModel):
    result: List[Prediction]
