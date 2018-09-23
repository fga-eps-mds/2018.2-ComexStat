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

## Teste e Build

Planejamos utilizar a ferramenta Travis-CI para a realização de testes unitários no
projeto.

O Travis possui integração com o Github, uma vez configurado, a cada commit um build
é lançado pelo Travis de forma automática. Também conhecido como integração contínua,
o processo de executar o build e testes é feita a cada commit.

Para avaliar a manutenibilidade do código iremos utilizar o Code Climate para analisar
estaticamente a qualidade do código, onde será visto a complexidade ciclomática e a
duplicidade de código.

O Code Climate foi criado por Bryan Helmkamp, bastante conhecido por contribuições
em vários projetos open source.

O Code Climate funciona de maneira muito simples, após o cadastro do projeto público
ou privado do Github na plataforma ele vai iniciar a verificá-lo até gerar um nota
que vai de zero a quatro.

## Pipeline

O ambiente de homologação será atualizado a cada sprint e estará disponível apenas
para desenvolvedores e cliente, já o de produção será atualizado a cada duas sprints
e está disponível além do cliente para os usuários.

Nossos serviços estão separados em três parte: back-end, front-end e database.

Foi separado em quatro fases a entrega de artefatos, onde, no ambiente de homologação
deverá ser entregue pequenas funcionalidades já para o ambiente de produção será
criada uma release para fazer o deploy das funcionalidades do software.

### Fase 1

![Fase 1](https://fga-eps-mds.github.io/2018.2-ComexStat/img/Diagrama-Pipeline1.png)

Na primeira fase será executada a política de branches, de commits e os teste para a
construção do código, onde o time terá que seguir os padrões que foi proposto para
assim criar uma versão com funcionalidades.

### Fase 2

![Fase 2](https://fga-eps-mds.github.io/2018.2-ComexStat/img/Diagrama-Pipeline2.png)

Na segunda fase a nova versão que foi publicada é processada pela ferramenta que vai
realizar todos os testes unitários, os que já foram implementados e os novos, logo
após é feito a build de teste. Em caso de erros a versão voltará para primeira fase.

### Fase 3

![Fase 3](https://fga-eps-mds.github.io/2018.2-ComexStat/img/Diagrama-Pipeline3.png)

Nessa fase a versão está mais estável, se a nova funcionalidade estiver funcionando
como desejado e devidamente testada então um pull request poderá ser solicitado para
ser feito a união da nova funcionalidade com a versão em produção da aplicação.

Será feito a análise manual do pull request, se a pipeline estiver operando corretamente
ela segue para produção, caso contrário ela volta pra fase anterior.


### Fase 4

![Fase 4](https://fga-eps-mds.github.io/2018.2-ComexStat/img/Diagrama-Pipeline4.png)

Na quarta versão a versão já foi aprovada e é colocada na linha de produção onde
as ferramentas de CI e CD fará o deploy da nova funcionalidade, no qual executará
a entrega automática da mesma.


## Processo do Pipeline DevOps

![Pipeline DevOps](https://fga-eps-mds.github.io/2018.2-ComexStat/img/pipelineDevops.png)

## 3. Referências

> * 4LINUX. Diferenças entre Integração, deploy e entrega contínua. Disponível em: <https://www.4linux.com.br/diferencas-entre-integracao-deploy-e-entrega-continua>. Acesso em: 18 set. 2018.
> * Landier, N., Lanfontaine, B. & Fernandes, S. Os padrões dos Gigantes da Web - Deploy Contínuo. Disponível em: <https://blog.octo.com/pt-br/os-padroes-dos-gigantes-da-web-deploy-continuo/>, 2013. Acessado em: 19/09/2018.
