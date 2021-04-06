from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ner_api.predict import predict_entities
from ner_api.schemas import MODEL_NAMES, RequestModel, ResponseModel

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])


@app.get("/v1/models/", summary="List all loaded models")
def get_models() -> List[str]:
    """ Return a list of all available loaded models. """
    return MODEL_NAMES


@app.post(
    "/v1/process/",
    summary="Process batches of text",
    response_model=ResponseModel,
)
def process_articles(query: RequestModel):
    """
    Process a batch of articles and return the entities predicted by the
    given model. Each record in the data should have a key "text".
    """
    entities = predict_entities(query)
    return ResponseModel(result=entities)
