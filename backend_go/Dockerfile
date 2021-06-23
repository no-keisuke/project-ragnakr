FROM golang:1.16.5-buster
WORKDIR /app
COPY . .

RUN go get -u github.com/cosmtrek/air
EXPOSE 8080
CMD ["air", "-c", "air_conf.toml"]
