import json
import os
from pathlib import Path
from typing import Dict, Iterable, Any

import streamlit as st
from spacy_streamlit import visualize_ner, load_model

from ner_api.settings import ROOT_DIR

DEFAULT_SPACY_MODEL = os.getenv("SPACY_MODEL", "en_core_web_sm")
DATASET_JSONL = (ROOT_DIR / "assets" / "data.jsonl").relative_to(ROOT_DIR)


def read_jsonl(path: Path) -> Iterable[Any]:
    for line in path.open():
        yield json.loads(line)


def parse_options(path: Path) -> Dict[str, Dict[str, str]]:
    """
    Returns a dict of documents with text data from a JSONL file.
    """
    lines = read_jsonl(path)
    options = {}
    for index, line in enumerate(lines):
        text = line["text"]
        source = line["meta"]["source"]
        key = f"{source}-{index}"
        options[key] = {"text": text, "source": source}
    return options


def main():
    """
    Run streamlit to show the model predictions.
    """
    models = [DEFAULT_SPACY_MODEL]
    dataset_jsonl = st.sidebar.selectbox("dataset", [DATASET_JSONL])
    options = parse_options(dataset_jsonl)
    option = st.selectbox("Example text source", list(options.keys()))
    spacy_model = st.sidebar.selectbox("Model name", models)

    nlp = load_model(spacy_model)
    selected_option = options[option]
    doc = nlp(selected_option["text"])

    visualize_ner(doc, labels=nlp.get_pipe("ner").labels)


main()
