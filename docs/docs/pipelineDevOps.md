---
id: pipelineDevOps
title: Pipeline DevOps
---

## integração Contínua

A Integração Contínua é uma prática de desenvolvimento da Extreme Programming que exige que os desenvolvedores integrem o código em uma mainline o mais frequentemente possível, pelo menos uma vez por dia, e cada check-in é verificado por uma build automática que compila o código e roda o conjunto de testes automatizados contra ele, permitindo que os times detectem problemas com antecedência.

## Deploy Contínuo

Deploy Contínuo (“Continuous Deploy”) é a capacidade de automatizar a homologação e testes do software de um produto desenvolvido de forma automática e rápida, onde a cada alteração significativa seja possível rodar toda a integração contínua, validar o produtos e suas credencias e deixa-lo disponível para produção. Esse processo geralmente é classificado dentro de duas vertentes, que variam de acordo com as capacidades de cada projeto e seus requisitos:

Totalmente automatizado: uma mudança no código é automaticamente verificada e, se tudo estiver certo, a aplicação vai para produção;

Semi-automatizado: a ideia é ser capaz de empurrar para produção a última versão estável do aplicativo em qualquer momento apenas apertando um botão. Nesse caso, chamamos de “one-click-deployment”.


## Definição de ambientes

### Desenvolvimento

Este é o ambiente que o software será desenvolvido.

### Homologação

O ambiente de homologação é o ambiente de teste, o desenvolvedor irá produzir o software no ambiente de desenvolvimento e então irá publica-lo no ambiente de homologação, para que assim o cliente possa der o aceite ou não sobre as funcionalidades do produto.

### Produção

Aqui estará a versão mais estável do software, este ambiente estará disponível para o público final do produto.

## Pipeline DevOps

![Pipeline DevOps](https://fga-eps-mds.github.io/2018.2-ComexStat/img/pipelineDevops.png)

## 3. Referências

> * 4LINUX. Diferenças entre Integração, deploy e entrega contínua. Disponível em: <https://www.4linux.com.br/diferencas-entre-integracao-deploy-e-entrega-continua>. Acesso em: 18 set. 2018.
