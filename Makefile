IMAGE_NAME = authorizer
VERSION = 0.0.1
INPUT_PATH =

docker-build:
	docker build -t $(IMAGE_NAME):$(VERSION) .

authorize:
	docker run -i authorizer:$(VERSION) < $(INPUT_PATH)

virtualenv:
	python3 -m venv venv --prompt '• authorizer •'
	venv/bin/python setup.py sdist
	venv/bin/pip install --upgrade pip setuptools dist/authorizer-$(VERSION).tar.gz
	echo "Virtualenv is ready, please run: source venv/bin/activate"

test:
	export PYTHONPATH=${PYTHONPATH}:. \
	 && python3 -m unittest discover tests/
