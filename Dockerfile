FROM debian:bullseye-slim

ARG LOAD_LANG=en

RUN apt update \
    && apt install -y \
      ca-certificates \
      libtesseract-dev \
      tesseract-ocr \
      golang \
      imagemagick \
      libmagickwand-dev

ENV GO111MODULE=on
ENV GOPATH=${HOME}/go
ENV PATH=${PATH}:${GOPATH}/bin

WORKDIR /app

COPY image.jpg ./image.jpg

COPY go.mod ./

RUN go mod download

COPY . .

RUN go version
RUN tesseract --version

CMD go run main.go
