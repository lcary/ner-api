from typing import List

from ner_api.schemas import MODELS, PredictRequest, Prediction
from ner_api.serializers import serialize_prediction


def predict_entities(query: PredictRequest) -> List[Prediction]:
    """
    Returns a list of predictions from a NER model for a given
    prediction request.
    """
    nlp = MODELS[query.model]
    entities = []
    texts = (example.text for example in query.examples)
    for doc in nlp.pipe(texts):
        entities.append(serialize_prediction(doc))
    return entities
