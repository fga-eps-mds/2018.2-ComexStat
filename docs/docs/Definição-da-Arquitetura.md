---
id: definicaoArquitetura
title: Definição Arquitetura
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

### 2.1. Django

O Django é um framework Web Python de alto nível que incentiva o rápido desenvolvimento e o
design claro e objetivo.

O Django será utilizado no back-end do projeto por ter uma excelente estrutura base
para projetos, por ser a maior comunidade e ter maior aceitação entre os frameworks
web Python, além  de acarretar em um boa curva de aprendizado para a equipe.

### 2.2. Angular

Angular é uma plataforma e framework para construção da interface de aplicações usando
HTML, CSS e principalmente JavaScript. O Angular facilita a criação de aplicações na web.

O Angular será aplicado como o front-end do projeto por ser um framework completo e por
possui muitos componentes disponíveis para diversas necessidades da aplicação.


### 2.3. GraphQL

GraphQL é uma linguagem de consulta para APIs e o tempo de execução que usa para
atender essas consultas com os dados existentes. O GraphQL fornece uma descrição
completa e compreensível dos dados em sua API.

O GraphQL possui três características principais:
* Permite que o cliente especifique exatamente quais dados são necessários.
* Facilita a agregação de dados de várias fontes.
* Usa um sistema de tipos para descrever dados.

O GraphQL foi adotado por ser uma linguagem de busca, achamos viável, pois, a plicação será
voltada para buscas.

### 2.4. PostgreSQL

O PostgreSQL é um sistema de gerenciamento de banco de dados do tipo objeto-relacional
(ORDBMS) com ênfase em extensibilidade e em padrões de conformidade.

Como um servidor de banco de dados, sua principal função é armazenar dados de forma
segura, apoiando as melhores práticas, permitindo a recuperação dos dados a pedido de
outras aplicações de software.

O PostgreSQL sará usado por ter muitos recursos destinados a ajudar os desenvolvedores
a gerenciar e a proteger a integridade dos dados.

## 3. Relacionamento das Tecnologias

### 3.1. Diagrama

## 4. Comunicação das Tecnologias

## 5. Referências

> * GraphQL. Disponível em: <https://graphql.org/>. Acessado em 13/09/2018.
> * GREIF, Sacha. Disponível em: <https://medium.freecodecamp.org/so-whats-this-graphql-thing-i-keep-hearing-about-baf4d36c20cf>. Acessado em 13/09/2018.
> * AFONSO, Alexandre. Disponível em: <https://blog.algaworks.com/o-que-e-angular/>. Acessado em 13/09/2018.
> * Edson. Disponível em: <https://www.devmedia.com.br/postgresql-tutorial/33025>. Acessado em 13/09/2018.
> * PostgreSQL. Disponível em: <https://www.postgresql.org/about/>. Acessado em 13/09/2018.
