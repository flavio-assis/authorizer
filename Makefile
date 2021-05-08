IMAGE_NAME = authorizer
IMAGE_TAG = latest
INPUT_PATH =

build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

authorize:
	docker run -v $(INPUT_PATH):/operations -t authorize:1.0 operations
