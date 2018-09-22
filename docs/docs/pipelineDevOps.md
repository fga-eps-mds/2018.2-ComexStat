---
id: pipelineDevOps
title: Pipeline DevOps
---

## Integração Contínua

A Integração Contínua é uma prática de desenvolvimento da metodologia Extreme Programming(XP)
que exige que os desenvolvedores integrem o código em uma mainline o mais frequentemente
possível, pelo menos uma vez por dia, e cada check-in é verificado por uma build automática
que compila o código e roda o conjunto de testes automatizados contra ele, permitindo que
os times detectem problemas com antecedência.

## Deploy Contínuo

O processo de Deploy Contínuo ou Continuous Deploy tem a capacidade para automatizar
a aprovação e os testes do produto de software. O conceito é entregar valor de negócio
o mais rápido possível e não acumular um código novo, ou seja, se o código passou pelo
processo de integração que é responsável por testes de integração ou testes unitários,
e também foi avançando no processo de delivery com testes manuais, visuais e de
comportamento, então entra a fase de deployment que é responsável por publicar o
código em produção de forma automatizada.


Este processo normalmente é distribuído em dois aspectos, que chega a ser modificada
dependendo do tipo de projeto que está sendo desenvolvido:

* Totalmente automatizado: onde a cada mudança no código é automaticamente verificada
e, se tudo estiver certo a aplicação vai para produção. (LANDIER et al., 2013)

* Semi-automatizado: onde a ideia é ser capaz de empurrar para produção a última
versão estável do sistema em qualquer momento apenas apertando um botão, nesse caso,
chamamos de "one-click-deployment". (LANDIER et al., 2013)

## Estrutura do Ambiente

* Desenvolvimento - O ambiente de desenvolvimento será onde o software será desenvolvido.

* Homologação - O ambiente de homologação é o ambiente de teste e onde será feito o
desenvolvimento do software. É onde o cliente aceita ou não as funcionalidades implementadas.

* Produção - O produto é onde se encontra a versão mais estável do software, em que estará
dispinível a versão final do produto para os usuários.


## Pipeline DevOps

![Pipeline DevOps](https://fga-eps-mds.github.io/2018.2-ComexStat/img/pipelineDevops.png)

## 3. Referências

> * 4LINUX. Diferenças entre Integração, deploy e entrega contínua. Disponível em: <https://www.4linux.com.br/diferencas-entre-integracao-deploy-e-entrega-continua>. Acesso em: 18 set. 2018.
> * Landier, N., Lanfontaine, B. & Fernandes, S. Os padrões dos Gigantes da Web - Deploy Contínuo. Disponível em: <https://blog.octo.com/pt-br/os-padroes-dos-gigantes-da-web-deploy-continuo/>, 2013. Acessado em: 19/09/2018.
