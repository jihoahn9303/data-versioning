FROM python:3.10-slim

ARG USER_ID
ARG USER_NAME

ENV HOME=/home/${USER_NAME} \
    VIRTUAL_ENV=/home/${USER_NAME}/venv 
ENV PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    TZ=Asia/Seoul \
    PATH="/usr/local/gcloud/google-cloud-sdk/bin:${VIRTUAL_ENV}/bin:${HOME}/.local/bin:${PATH}" \
    PYTHONPATH="/app:${PYTHONPATH}" \
    BUILD_POETRY_LOCK="${HOME}/poetry.lock.build"

RUN apt-get update \
    && apt-get -qq -y install vim gcc curl git build-essential libb64-dev software-properties-common \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -qq -y clean

RUN curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-462.0.1-linux-x86_64.tar.gz \
    && mv /google-cloud-cli-462.0.1-linux-x86_64.tar.gz /tmp/google-cloud-cli-462.0.1-linux-x86_64.tar.gz
RUN mkdir -p /usr/local/gcloud \
    && tar -C /usr/local/gcloud -zxvf /tmp/google-cloud-cli-462.0.1-linux-x86_64.tar.gz \
    && /usr/local/gcloud/google-cloud-sdk/install.sh --usage-reporting false --command-completion true --bash-completion true --path-update true --quiet

RUN mkdir -p ${HOME} /app 
COPY . /app/

RUN chmod a+x /app/docker/scripts/*.sh
RUN addgroup --system --gid ${USER_ID} ${USER_NAME} \
    && useradd --system --no-log-init \
    --home-dir ${HOME} \
    --uid ${USER_ID} \
    --gid ${USER_NAME} \
    --groups ${USER_NAME} ${USER_NAME}


RUN chown -R ${USER_NAME}:${USER_NAME} /app /tmp ${HOME} 

USER ${USER_NAME}:${USER_NAME}
RUN curl -sSL https://install.python-poetry.org | python3 -
    
WORKDIR /app
RUN poetry config virtualenvs.create false \
    && python3.10 -m venv ${VIRTUAL_ENV} \
    && pip install --upgrade pip setuptools \
    && poetry install \
    && cp poetry.lock ${BUILD_POETRY_LOCK} \
    && rm -rf ${HOME}/.cache/*

# ENTRYPOINT ["/bin/bash", "-c", "while true; do sleep 1; done"]
ENTRYPOINT ["/bin/bash", "-c"]
CMD ["/app/docker/scripts/startup-script.sh"]



