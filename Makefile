env:
	bash bin/setup_env.sh

dataset_url = https://raw.githubusercontent.com/explosion/prodigy-recipes/master/example-datasets/plot_summaries.jsonl
download-assets:
	mkdir -p assets/
	curl $(dataset_url) -o assets/data.jsonl

install-model:
	bash bin/install_model.sh

server:
	uvicorn ner_api.main:app --reload

test:
	pytest

streamlit:
	streamlit run ner_api/streamlit.py

build:
	docker build -t ner-api:latest .
