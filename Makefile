all:
	docker build -t izgzhen/droid-scripts .

cli:
	docker run -it izgzhen/droid-scripts
