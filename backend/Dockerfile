FROM python:3.11.3-bullseye

ENV DOCKER_ENV=True
ENV PYTHONPATH=/src
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /src
COPY . /src
RUN echo "Contenido de /src:"
RUN ls -la /src
RUN apt update -y && apt upgrade -y && apt install curl -y
RUN curl -sSL https://install.python-poetry.org | python -
RUN poetry install --no-dev
RUN chmod +x backend-starter.sh

EXPOSE 8000

ENTRYPOINT ["/bin/bash"]
