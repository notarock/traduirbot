FROM debian:bullseye-slim

ARG LOAD_LANG=en

RUN apt update \
    && apt install -y \
      ca-certificates \
      libtesseract-dev \
      tesseract-ocr \
      golang

ENV GO111MODULE=on
ENV GOPATH=${HOME}/go
ENV PATH=${PATH}:${GOPATH}/bin

WORKDIR /app

COPY . .

RUN go get -v ./... && go install .

COPY image.jpg /app/image.jpg

CMD go run main.go
