#!/usr/bin/bash
COMMIT_SHA=$(git rev-parse --short HEAD)
GIT_TAG=$(git describe --tags --abbrev=0)
export COMMIT_SHA  GIT_TAG
docker-compose up --build