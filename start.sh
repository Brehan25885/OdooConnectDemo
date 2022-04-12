#!/bin/bash
app="docker.flask"
docker build -t ${app} .
docker run -d -p 3030:80 \
  --name=${app} \
  --network=objects-ws_default\
  -v $PWD:/app ${app}
