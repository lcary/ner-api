from fastapi.testclient import TestClient

from ner_api.main import app
from ner_api.schemas import ModelName


def test_v1_process():
    model_names = [model.value for model in ModelName]
    assert model_names
    client = TestClient(app)
    response = client.get("/v1/models")
    assert response.status_code == 200
    assert response.json() == model_names
    articles = [{"text": "This is a text"}, {"text": "This is another text"}]
    data = {"articles": articles, "model": model_names[0]}
    response = client.post("/v1/process/", json=data)
    assert response.status_code == 200
    result = response.json()["result"]
    assert len(result) == len(articles)
    assert [{"text": entry["text"]} for entry in result] == articles
    assert all("entities" in entry for entry in result)
