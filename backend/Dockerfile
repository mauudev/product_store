FROM python:3.11.3-bullseye

ENV DOCKER_ENV=True
ENV PYTHONPATH=/src
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /src
COPY . /src
RUN ls -a
RUN apt update -y && apt upgrade -y && apt install curl -y
RUN curl -sSL https://install.python-poetry.org | python -
RUN poetry install --no-dev 

EXPOSE 8000

ENTRYPOINT ["/bin/bash"]