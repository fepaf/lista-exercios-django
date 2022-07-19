# Listagem e Correção de Exercícios de Múltipla escolha com Django
# Prerequisites
It's necessary has installed the following tools
- Docker Composer (see official [documentation](https://docs.docker.com/compose/install/) for install)
- Docker (see official [documentation](https://docs.docker.com/get-docker/) for install)
# Run Container 

On Linux, On directory `./setup_project`
```sh
docker-compose up --build
```

# Access Django-admin
###### Django-admin: [http://0.0.0.0:8000/admin/](http://0.0.0.0:8000/admin/)
As credenciais de acesso são
- username:
```
admin
```
- password:
```
Xorislife@112358
```

# Project Docs
###### Swagger: [http://0.0.0.0:8000/swagger/](http://0.0.0.0:8000/swagger/)
###### Redoc: [http://0.0.0.0:8000/redoc/](http://0.0.0.0:8000/redoc/)
# How to use
## Questions
#### Create
Use django-admin interface.
#### List
Use the endpoint [http://0.0.0.0:8000/api/question/](http://0.0.0.0:8000/api/question/)
## Answers
#### Create
For answers questions acess [http://0.0.0.0:8000/api/answer/](http://0.0.0.0:8000/api/answer/)
## Report 
For report about perfomance on test: [http://0.0.0.0:8000/api/report](http://0.0.0.0:8000/api/report)
