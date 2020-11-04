#!/bin/bash
#install prerequest
python3 -m pip install grpcio grpcio-tools

#compile proto files
python3 -m grpc_tools.protoc -I ./protos --python_out=./ --grpc_python_out=./ protos/NormalDetect.proto
