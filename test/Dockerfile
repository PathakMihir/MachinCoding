FROM golang:1.10 AS builder

RUN apt-get update && apt-get -y dist-upgrade
RUN apt install -y netcat

ENV GO111MODULE=on

RUN mkdir /go/src/diceDB

WORKDIR /go/src/diceDB

ADD . /go/src/diceDB
# Build
RUN CGO_ENABLED=0 go build -o dice main.go 


FROM alpine:latest

WORKDIR /app/server

COPY --from=builder /go/src/diceDB/dice ./

EXPOSE 8080

RUN chmod +x ./dice

CMD [ "./dice" ]


