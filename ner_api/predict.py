from typing import List

from ner_api.schemas import MODELS, RequestModel, Prediction
from ner_api.serializers import serialize_prediction


def predict_entities(query: RequestModel) -> List[Prediction]:
    nlp = MODELS[query.model]
    entities = []
    texts = (article.text for article in query.articles)
    for doc in nlp.pipe(texts):
        entities.append(serialize_prediction(doc))
    return entities
