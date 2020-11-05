docker build --build-arg USER_ID=$UID -t detectron2_beyless_deploy:v0.1 .

docker run --gpus all -it \
	-e LC_ALL=C.UTF-8 \
	-p 50051:50051 \
	-p 6006:6006 \
	-p 8888:8888 \
	--shm-size=8gb --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
	--name=detectron2_beyless_deploy detectron2_beyless_deploy:v0.1


