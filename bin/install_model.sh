#!/bin/bash

model_version="3.0.0"
model_file="en_core_web_sm-${model_version}-py3-none-any.whl"
model_repo=https://github.com/explosion/spacy-models
model_url="${model_repo}/releases/download/en_core_web_sm-${model_version}/${model_file}"

mkdir -p assets/
# The -L flag is necessary to handle redirects:
curl -k "${model_url}" -L -o "assets/${model_file}"
pip install "assets/${model_file}"
