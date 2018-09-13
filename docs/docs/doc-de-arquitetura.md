---
id: docArquitetura
title: Documento de Arquitetura
---

***
## 1. Introdução
***
Na introdução será apresentada uma ampla visão do documento, deixando clara a sua finalidade e quais pontos aborda. Além disso, serão neste tópico listadas algumas definições, acrônimos e abreviações de grande importância para o pleno entendimento do restante das seções.

### 1.1 Objetivo

O objetivo deste documento é de expor aos interessados uma visão geral acerca da arquitetura do ComexStat, pontuando aspectos deste segundo diferentes visões arquiteturais, deixando também em evidência algumas restrições e metas quanto a estes pontos.


### 1.2 Escopo

Sendo uma sequência para a descrição geral do produto dada pelo Documento de Visão, o documento de Arquitetura ao descrever o sistema em um ponto de vista mais técnico, ajuda na compreensão do software bem como na compreensão da abordagem utilizada para desenvolve-lo, podendo por conseguinte servir também de base para avaliar se tal abordagem atende os requisitos do cliente. O descrito no documento afetará toda a construção do software, de tal forma que todo o prosseguimento do projeto será de acordo com as arquiteturas e modelos aqui definidos.


### 1.3 Definições, Acrônimos e Abreviações

| **Abreviação** | **Definição** |
| :--------: | :-------: |
| MVC | Model-View-Controller (Modelo-Visão-Controlador, em inglês) |
| MVT | Model-View-Template (Modelo-Visão-Template, em inglês) |

***
## 2. Representação Arquitetural
***
O ComexStat será uma aplicação web desenvolvida a partir do framework Django, escrito em Python. O Django segue o padrão **MVC** de perto, no entanto, ele usa sua própria lógica na implementação. Como o *“Controller”* é manipulado pelo próprio framework e a maior parte do entusiasmo no Django acontece em modelos, templates e views, o Django é frequentemente chamado de framework da MTV. No padrão de desenvolvimento da **MVT**:

**Model**, a camada de acesso a dados. Essa camada contém tudo e qualquer coisa sobre os dados: como acessá-lo, como validá-lo, quais comportamentos ele possui e as relações entre os dados.

**View**, a camada de lógica de negócios. Essa camada contém a lógica que acessa o modelo e adia para o (s) modelo (s) apropriado (s). Você pode pensar nisso como a ponte entre modelos e modelos.

**Template**, a camada de apresentação. Essa camada contém decisões relacionadas à apresentação: como algo deve ser exibido em uma página da Web ou outro tipo de documento.

![arquitetura-mvt](https://www.javatpoint.com/django/images/django-mvt-based-control-flow.png)

Esta é provavelmente a única infelicidade da nomeação no Django, porque a *view* do Django é mais parecida com o *controller* no MVC, e a *view* do MVC é na verdade um *Template* no Django. Independentemente de como as coisas são nomeadas, Django as executa da forma que é mais lógica para nós.

***
## 3. Restrições e Metas Arquiteturais
***
* **Suportabilidade**
      O software poderá ser utilizado sem grandes problemas pela maior parte dos navegadores mais populares, no entanto, as principais plataformas tidas como alvo são o Google Chrome e o FireFox, de tal forma que o usuário ao acessar o sistema por uma dessas vias poderá esperar total compatibilidade.

 * **Usabilidade**
       O sistema deverá ser intuitivo e de simples uso, seguindo uma sequência lógica de ações possíveis, definida por Pesquisa ->Filtros -> Agrupamentos -> Visualização de dados -> Compartilhamento dos resultados. Dessa forma, o usuário não deverá precisar de tutoriais ou treinamentos extras para usufruir dos recursos disponibilizados.

 * **Ferramentas de Desenvolvimento**
       O projeto será desenvolvido em Python (versão 3.x.x), pela utilização do framework Django (versão 3.x.x).

  * **Confiabilidade**
       O sistema terá uma cobertura mínima de testes de 90%, buscando garantir que suas funcionalidades foram suficientemente testadas.

***
## 4. Visão de Casos de Uso
***

### 4.1 Atores

#### 4.1.1 Usuário comum
Este ator é o usuário do sistema que irá utilizar os recursos disponibilizados pela aplicação web, usufruindo de tudo que ela pode oferecer por meio de uma interface intuitiva e de fácil uso.

#### 4.1.2 Usuário desenvolvedor
Esse ator é o usuário do sistema que poderá acessar, filtrar e manusear os dados da forma desejada através de uma API.

### 4.2 Diagrama de casos de uso

![Casos de uso](casosDeUso.png)

### 4.3 Prioridade dos casos de uso

Na forma escolhida para classifica-los, os casos de uso possuem três tipos de prioridades:

   * **Essenciais:** Funcionalidades indispensáveis para o sistema, sem as quais o mesmo não é considerado funcional.
   * **Importantes:** Funcionalidades que são necessárias para o cliente, mas o sistema pode funcionar sem elas.
   * **Desejáveis:** Funcionalidades desejadas mas que podem ou não ser adicionadas posteriormente, sem elas o sistema já atende todas as necessidades do cliente.


   |Caso de Uso|Prioridade|
   |:---------:|:--------:|
   |Consultar e filtrar os dados disponibilizados, através da API ou da aplicação web |Essencial|
   |Gerar permalinks dos resultados pesquisados|Essencial|
   |Exportar os resultados das consultas em formatos como .csv e PDF|Essencial|
   |Gerar visualizações gráficas dos dados|Essencial|
   |Compartilhamento da consulta feita em redes sociais ou similares|Importante|
   |Comparar, incluindo graficamente ,os dados resultantes de múltiplas pesquisas|Desejável|
   |Compartilhamento via embedding de páginas|Desejável|


***
## 5. Visão Lógica
***

### 5.1 Visão Geral

O sistema será desenvolvido usando o framework web Django, que é estruturado com padrão MVT, uma variação do padrão MVC.
Pelo navegador, o usuário acessa um endereço web que pode ser digitado diretamente ou acessado por algum template, o processador de URL's do Django processa um padrão na URL e destina à view e método que descreve a ação a ser feita. Esse método então retorna algum template diretamente, ou pede à um modelo alguns dados, para então passá-los ao template.

***
## 6. Visão da Implementação
***

### 6.1 Diagrama do banco de dados
[!Diagrama banco](ComexStat_DataBase.png)


***
## 7. Qualidade
***
A arquitetura MVT oferece uma organização das camadas da aplicação, possibilitando aos desenvolvedores uma fácil manutenção, além de ser um padrão de arquitetura altamente confiável já que é muito utilizado.

## Histórico da Revisão

| **Data** | **Versão** | **Descrição** | **Autor** |
| :------: | :--------: | :-----------: | :-------: |
|09/09/2018|0.1.0|Abertura e preenchimento da introdução|Marcos Nery|
|10/09/2018|0.2.0|Adição das restrições e metas arquiterurais|Marcos Nery|
|10/09/2018|0.3.0|Adição da visão geral da visão lógica|Kaique Borges|
|10/09/2018|0.4.0|Adição da representação arquitetural|André Lucas|
|10/09/2018|0.5.0|Adição da qualidade|João Victor|
|13/09/2018|0.6.0|Adição da visão de casos de uso|Marcos Nery|