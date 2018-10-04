---
id: definicaoArquitetura
title: Definição Arquitetural
---

## 1. Introdução

A arquitetura que vamos utilizar será a de microsserviços. Os microsserviços são um
estilo de arquitetura de aplicativo em que programas autônomos independentes, com uma
única finalidade, podem se comunicar entre si por meio de uma rede. Normalmente, esses
microsserviços podem ser implantados independentemente porque eles têm uma forte separação
de responsabilidades por meio de uma especificação bem definida com compatibilidade reversível
significativa para evitar a quebra súbita de dependência.

Com base na arquitetura microserviços, foram definidas as seguintes tecnologias.

## 2. Tecnologias que Serão Utilizadas

Todas as tecnologias adotadas foram escolhidas em conjunto com o cliente, por meio
de reuniões que fazermos semanalmente.

### 2.1. Django

O Django é um framework web na linguagem Python, que permite rápido desenvolvimento e
design claro e objetivo de aplicações web..

O Django será utilizado no back-end do projeto por apresentar uma adequeda estrutura base
para projetos, por ser a maior comunidade e ter maior aceitação entre os frameworks
web Python, além  de acarretar em um boa curva de aprendizado para a equipe.

### 2.2. Angular

Angular é um framework para construção da interfaces de usuário usando
HTML, CSS e JavaScript, através de suas bibliotecas facilita o desenvolvimento
de aplicações web.

O Angular será aplicado como o front-end do projeto por ser um framework completo e por
possuir diversos componentes disponíveis para as várias necessidades da aplicação.


### 2.3. GraphQL

GraphQL é uma linguagem de consulta para APIs, o GraphQL fornece uma descrição
completa e compreensível dos dados contidos na API.

Características principais:
* Permite que o cliente especifique exatamente quais dados deseja obter.
* Facilita a agregação de dados de várias fontes.
* Usa um sistema de tipos para descrever dados.

GraphQL foi escolhido por oferecer características arquiteturais que vão de
acordo com a aplicação.

### 2.4. PostgreSQL

O PostgreSQL é um sistema de gerenciamento de banco de dados do tipo objeto-relacional
(ORDBMS) com ênfase em extensibilidade e em padrões de conformidade.

Como um servidor de banco de dados, sua principal função é armazenar dados de forma
segura, apoiando as melhores práticas, permitindo a recuperação dos dados a pedido de
outras aplicações de software.

O PostgreSQL sará usado por ter muitos recursos destinados a ajudar os desenvolvedores
a gerenciar e a proteger a integridade dos dados.

## 3. Relacionamento das Tecnologias

### 3.1. GraphQL com Django

O ComexStat contará com a implementação do GraphQL e Python, para essa integração
onde será utilizado a biblioteca Graphene. Será utilizado basicamente o query
do GraphQL, para fazer buscas de informações do banco de dados.

### 3.2. GraphQL com Angular

O Apollo Client possui uma implementação em Angular para GraphQL. O Apollo Client foi
projetado desde o início para facilitar a construção de componentes de interface
do usuário que buscam dados com o GraphQL.

O Apollo Client é flexível para a plataforma Angular, onde foi cuidadosamente
desenvolvida para funcionar bem com todas as ferramentas usadas pelos
desenvolvedores Angular.


### 3.3. Diagrama

![Diagrama_Representacao_Arquitetural](https://fga-eps-mds.github.io/2018.2-ComexStat/img/Representacao_Arquitetural.png)

## 4. Arquitetura do Software

Foi decidido junto ao cliente a posibilidade de uma arquitetura monolítica, visto
que o escopo do projeto está bem acoplado e que vamos utilizar bibliotecas externas
para as funcionalidades da aplicação.

 Uma arquitetura monolítica é o modelo unificado tradicional para o design de um
 programa de software.

O software monolítico é projetado para ser independente, os componentes do programa
são interconectados e interdependentes, em vez de fracamente acoplados, como é o
caso dos programas de software modulares. Em uma arquitetura bem acoplada, cada
componente e seus componentes associados devem estar presentes para que o código
seja executado ou compilado.

### 4.1. Diagrama

![Diagrama-Monolitico](https://fga-eps-mds.github.io/2018.2-ComexStat/img/Diagrama-Monolitico.png)

## 5. Referências

> * GraphQL. Disponível em: <https://graphql.org/>. Acessado em 13/09/2018.
> * GREIF, Sacha. Disponível em: <https://medium.freecodecamp.org/so-whats-this-graphql-thing-i-keep-hearing-about-baf4d36c20cf>. Acessado em 13/09/2018.
> * AFONSO, Alexandre. Disponível em: <https://blog.algaworks.com/o-que-e-angular/>. Acessado em 13/09/2018.
> * Edson. Disponível em: <https://www.devmedia.com.br/postgresql-tutorial/33025>. Acessado em 13/09/2018.
> * PostgreSQL. Disponível em: <https://www.postgresql.org/about/>. Acessado em 13/09/2018.
> * SCARPA, João Mateus. Disponível em: <https://blog.designa.com.br/padr%C3%B5es-de-arquitetura-de-software-voc%C3%AA-sabe-do-que-estamos-falando-4858967c4054>. Acessado em 19/09/2018.
