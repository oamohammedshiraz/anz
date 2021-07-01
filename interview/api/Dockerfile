FROM python:3.9.5
WORKDIR /myapp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ARG COMMIT_SHA
ARG GIT_TAG
ENV PORT=8000
ENV LOG_LEVEL=INFO
ENV GIT_COMMIT_SHA=${COMMIT_SHA}
ENV VERSION=${GIT_TAG}
EXPOSE 8000
COPY . /myapp
CMD gunicorn -b 0.0.0.0:$PORT wsgi:app