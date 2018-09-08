---
id: utilizandoDockerDjango
title: Como executar comandos Django
---


## 1. Introdução

Este documento possui o objetivo de orientar e ajudar os desenvolvedores da equipe a, com mais facilidade, utilizar o framework Djando com os containers do Docker.

## Como utilizar

Com os critérios de uso descritos no Readme do projeto satisfeitos, o usuário deverá seguir os seguintes passos

Vá até o diretorio da aplicação e a inicie, para isso rode em seu terminal o comando

    sudo docker-compose up

Com a aplicação rodando local, abra outro terminal para que consiga fazer as modificações que deseja com o Django, como por exemplo rodar as migrações

    sudo docker-compose exec web python3 manage.py makemigrations

    sudo docker-compose exec web python3 manage.py migrate

Caso queira criar um usuário admininstrador, execute o comando

    sudo docker-compose exec web python3 manage.py createsuperuser

Para criar novos diretórios com a estrutura do Django

    sudo docker-compose exec web python3 manage.py startapp polls


## 3. Referências Bibliográficas

> * DJANGO, TUTORIAL. "Escrevendo seu primeiro app Django." .
