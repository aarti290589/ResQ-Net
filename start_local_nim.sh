#!/bin/bash
echo "🚀 Initializing Llama 3.2 Vision on NVIDIA GB10..."
docker run -it --rm --name=resq-vision \
  --runtime=nvidia \
  --gpus all \
  -e NGC_API_KEY=$NGC_API_KEY \
  -p 8000:8000 \
  nvcr.io/nim/meta/llama-3.2-11b-vision-instruct:latest