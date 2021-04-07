FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim
RUN apt-get update && apt-get install -yq cmake gcc-multilib g++-multilib curl
COPY poetry.lock pyproject.toml ./
RUN pip --no-cache-dir install poetry poetry-setup \
    && poetry install --no-root \
    && pip uninstall poetry -y \
    && rm -rf ~/.config/pypoetry
COPY Makefile /app/
COPY bin /app/bin/
RUN make download-assets
RUN make install-model
COPY ner_api /app/ner_api/
WORKDIR /app/
# Set the APP_MODULE environment variable used by the start.sh script here:
# https://github.com/tiangolo/uvicorn-gunicorn-docker/blob/2daa3e3/docker-images/start.sh#L34
ENV APP_MODULE=${APP_MODULE:-"ner_api.main:app"}
