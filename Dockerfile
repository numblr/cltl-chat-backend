# syntax = docker/dockerfile:1.2

FROM python:3.9

WORKDIR /cltl-chat-backend
COPY src requirements.txt makefile ./
COPY config ./config
COPY util ./util

RUN --mount=type=bind,target=/cltl-chat-backend/repo,from=cltl/cltl-requirements:0.0.dev1,source=/repo \
        make venv project_repo=/cltl-chat-backend/repo/leolani project_mirror=/cltl-chat-backend/repo/mirror

CMD . venv/bin/activate && python app.py
