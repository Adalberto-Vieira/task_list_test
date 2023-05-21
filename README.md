# taskList app

## How to run

build the docker container and use your browser to see the aplication at local host 5000

commands:

```console 
docker build -t flask:latest .
docker run -p 5000:5000 flask 
```

## How to run for dev

install requiriments.txt and requirements-dev.txt
Set env var for debugging 
Execute flask run inside task list

## How to run tests

install requiriments.txt and requirements-dev.txt
run pytest tests/ inside root folder
