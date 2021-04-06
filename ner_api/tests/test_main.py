from fastapi.testclient import TestClient

from ner_api.main import app
from ner_api.schemas import Model


def test_v1_process():
    model_names = [model.value for model in Model]
    assert model_names
    client = TestClient(app)
    response = client.get("/v1/models")
    assert response.status_code == 200
    assert response.json() == model_names
    examples = [{"text": "Example 1"}, {"text": "Example 2"}]
    data = {"examples": examples, "model": model_names[0]}
    response = client.post("/v1/process/", json=data)
    assert response.status_code == 200
    result = response.json()["result"]
    assert len(result) == len(examples)
    assert [{"text": entry["text"]} for entry in result] == examples
    assert all("entities" in entry for entry in result)
