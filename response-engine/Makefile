.PHONY: build push
image_name=ebriand/response-engine

build:
	docker image build -t $(image_name) .

push: build
	docker image push $(image_name)
