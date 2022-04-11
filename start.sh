#!/bin/bash
app="docker.flask"
docker build -t ${app} .
docker run -p 56733:80 \
  --name=${app} \
  --network=objects-ws_default\
  -v $PWD:/app ${app}
