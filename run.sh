#!/bin/bash
exec \
  docker run \
    --rm \
    -p 12345:12345 \
    flask_catchall
