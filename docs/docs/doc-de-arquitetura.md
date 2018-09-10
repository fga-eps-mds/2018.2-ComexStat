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

***
## 5. Visão Lógica
***

### 5.1 Visão Geral

O sistema será desenvolvido usando o framework web Django, que é estruturado com padrão MVT, uma variação do padrão MVC.
Pelo navegador, o usuário acessa um endereço web que pode ser digitado diretamente ou acessado por algum template, o processador de URL's do Django processa um padrão na URL e destina à view e método que descreve a ação a ser feita. Esse método então retorna algum template diretamente, ou pede à um modelo alguns dados, para então passá-los ao template.

***
## 6. Visão da Implementação
***

***
## 7. Qualidade
***

## Histórico da Revisão

| **Data** | **Versão** | **Descrição** | **Autor** |
| :------: | :--------: | :-----------: | :-------: |
|09/09/2018|0.1.0|Abertura e preenchimento da introdução|Marcos Nery|
|10/09/2018|0.2.0|Adição das restrições e metas arquiterurais|Marcos Nery| 
|10/09/2018|0.3.0|Adição da visão geral da visão lógica|Kaique Borges|
