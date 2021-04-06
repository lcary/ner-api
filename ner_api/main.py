from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ner_api.predict import predict_entities
from ner_api.schemas import MODEL_NAMES, RequestModel, ResponseModel

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])


@app.get("/v1/models/", summary="Returns a list of loaded models")
def v1_models() -> List[str]:
    """ Returns a list of all available loaded models. """
    return MODEL_NAMES


@app.post(
    "/v1/process/",
    summary="Process batches of text",
    response_model=ResponseModel,
)
def v1_process(query: RequestModel) -> ResponseModel:
    """
    Process a batch of text requests and return the entities predicted by
    a given model.
    """
    entities = predict_entities(query)
    return ResponseModel(result=entities)
