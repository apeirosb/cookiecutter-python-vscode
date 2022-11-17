# This Dockerfile is intended to be used for development in Visual Studio Code,
# which automatically copies the project into the /workspaces subfolder in the
# container. That is the reason why this file does not contain an entrypoint/command.
FROM python:{{ cookiecutter.python_version }}-alpine
LABEL name={{ cookiecutter.project_name }}

# create a non-root user
ARG USER=pyuser
ARG GROUP=pygroup
# add sudo (to install with pip globally from vscode)
RUN apk --no-cache update && apk --no-cache add sudo
# add group and user
RUN addgroup -S $GROUP \
        && adduser -S $USER -G $GROUP --shell /bin/sh \
        && echo "$USER ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USER \
        && chmod 0440 /etc/sudoers.d/$USER
# --shell /bin/sh necessary to avoid errors in vscode

# set work directory
ENV APP_HOME=/usr/src/{{ cookiecutter.project_name }}
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# add git for dev (to be removed)
RUN apk add --no-cache git

# add gcc toolchain (required to build pre-commit hooks)
RUN apk add --no-cache build-base

# install depencencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# chown all the files to the app user
RUN chown -R pyuser:pygroup $APP_HOME

# change to the user
USER pyuser
