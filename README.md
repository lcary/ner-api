# ner-api

## Usage

### Docker Service

To run the inference server REST API, run:

```
docker-compose up
```

Then, open your browser to http://localhost:80/docs for Swagger docs.

## Local Development

The local development setup is a bit more complicated, but the
server auto-restarts for changes to the model.

### Developer Env Setup

Run `make env` to set up your local developer environment.
After doing so, make sure to activate the virtual environment
(`source venv/bin/activate`) before working on the codebase.

### Data and Model

To download the data and model required for the REST API, run:

```bash
make download-assets
make install-model
```

### REST API

To run the NER model server locally, run `make server` and open
your browser to http://127.0.0.1:8000/docs

The `/v1/process` endpoint will process text passages, returning
parsed NER entities.

### Streamlit

To run the demo NER model visualizer locally, run `make streamlit`

### Tests

Run `make test` to run the unit tests.
