from spacy.tokens import Span
from spacy.tokens.doc import Doc

from ner_api.schemas import Prediction, Entity


def serialize_entity(span: Span) -> Entity:
    """
    Returns Entity serialized from a given spaCy Span object.
    """
    return Entity(
        text=span.text,
        label=span.label_,
        start=span.start_char,
        end=span.end_char,
    )


def serialize_prediction(doc: Doc) -> Prediction:
    """
    Returns Prediction data serialized from a given spaCy Doc object.
    """
    entities = [serialize_entity(entity) for entity in doc.ents]
    return Prediction(text=doc.text, entities=entities)
