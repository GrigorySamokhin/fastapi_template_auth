
docker_build:
	sudo docker build --progress=plain -t glb-assembl .

docker_run:
	sudo docker run -it -p 8080:8080 glb-assembl