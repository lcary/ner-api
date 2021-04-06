from typing import List

from ner_api.schemas import MODELS, RequestModel, Prediction
from ner_api.serializers import serialize_prediction


def predict_entities(query: RequestModel) -> List[Prediction]:
    nlp = MODELS[query.model]
    entities = []
    texts = (example.text for example in query.examples)
    for doc in nlp.pipe(texts):
        entities.append(serialize_prediction(doc))
    return entities
