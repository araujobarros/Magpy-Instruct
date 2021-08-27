# MagPy-Instruct
Projeto realizado com Django Rest Framework, para cadastro e consulta de projetos em banco de dados.


### Consultando a api

As rotas disponíveis para consulta, assim como o formato da consulta encontram-se em:
https://magpy-instruct-api.herokuapp.com/swagger/

Nesta doc por exemplo é possível ver que pra realizar uma consulta de todos os projetos cadastrados, basta fazer uma requisição GET para:
https://magpy-instruct-api.herokuapp.com/api/projects


### Rodando o projeto localmente

1. Clone o repositório

- `git clone git@github.com:araujobarros/Magpy-Instruct.git`.

- Entre na pasta do repositório que você acabou de clonar:
  - `Magpy-Instruct`

2. Crie e ative o ambiente virtual para o projeto

- `python3 -m venv .venv && source .venv/bin/activate`

Nota: é possível desativar o ambiente virtual com o comando `deactivate`

3. Instale o pipenv para gerenciamento das dependências

- `pip install pipenv`

4. Instale as dependências

- `pipenv install`

Nota: Se por algum motivo algum pacote não for corretamente instalado é possível instalá-lo separadamente com:
  - `pip install <nome do pacote>`
  É possível verificar os pacotes no arquivo pipfile na raiz do projeto

5. Se for interessante baixar algum outro pacote complementar para alteração do projeto é possível instalá-lo via pipenv atualizando automaticamente o pipfile e o pipfile.lock:

- `pipenv install <nome do pacote>`

6. Crie a estrutura inicial do banco de dados

- `python3 manage.py migrate`

7. Finalmente execute o servidor local

- `python3 manage.py runserver`


### Referências

1. Django Rest Framework:
- https://www.django-rest-framework.org/
- https://pythonacademy.com.br/blog/construcao-de-apis-com-django-rest-framework
- https://klauslaube.com.br/2020/02/13/construindo-apis-em-django-com-django-rest-framework.html
- https://realpython.com/django-rest-framework-quick-start/

2. Requests:
- https://realpython.com/python-requests/

2. Pipenv:
- https://pipenv-fork.readthedocs.io/en/latest/basics.html
- https://medium.com/@patrickporto/introdu%C3%A7%C3%A3o-ao-pipenv-49aa9685dfe4

3. Testes:
- https://medium.com/@ksarthak4ever/test-driven-development-tdd-in-django-and-django-rest-framework-drf-a889a8068cb7
- https://www.20tab.com/en/blog/test-python-mocking/
- https://realpython.com/python-mock-library/
- https://kimsereylam.com/python/2021/03/19/how-to-use-patch-in-python-unittest.html
- https://medium.com/@ksarthak4ever/test-driven-development-tdd-in-django-and-django-rest-framework-drf-a889a8068cb7

4. Swagger
- https://github.com/axnsan12/drf-yasg#installation

5. Curiosidades
- https://stackoverflow.com/questions/21809112/what-does-tuple-and-dict-mean-in-python
- https://stackoverflow.com/questions/34414326/why-is-assertdictequal-needed-if-dicts-can-be-compared-by/34414463
