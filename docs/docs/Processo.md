---
id: processo
title: Processo Definido
---

# 1. Introdução

O processo a ser seguido pelo time é baseado em Lean e metodologias ágeis , principalmente o Scrum e
XP (eXtreme Programming).

# 2. Papéis

## 2.1. Time de Desenvolvimento

- Elaborar documento de Visão;
- Elaborar documento de arquitetura;
- Desenvolver código, de acordo com os requisitos definidos;
- Utilizar de práticas ágeis para otimizar o desenvolvimento.

## 2.2. Devops

- Configurar ambiente de desenvolvimento, homologação e produção utilizando contâiners;
- Definir política de commits e branchs de acordo com o git flow;
- Garantir que o time siga o git flow;
- Construir o pipeline de integração e deploy contínuos;
- Definir roadmap de deploy contínuo.

## 2.3. Arquiteto

- Definir o roadmap de Requisitos;
- Garantir que o time de desenvolvinto siga a arquitetura;
- Propor arquitetura de micro serviços;
- Configuração de contâiners com micro serviços.
-
## 2.4. Scrum Master (SM)

- Gerenciar comunicação do Time;
- Garantir que os membros sigam o processo Definido;
- Gerenciar riscos;
- Definir, monitorar e controlar indicadores e metricas de produtividade, utilizando-os para tomadas de decisões no projeto;
- Definir e seguir roadmap para produtividade máxima do time.

## 2.5. Product Owner (PO)

- Visão de Produto;
- Elaborar o Termo de Abertura;
- Elaborar a Estrutura Analítica do Projeto (EAP);
- Definir plano de negócio;
- Gerenciar backlog de histórias;
- Desenvolver identidade visual e guia de usabilidade do produto;
- Definir roadmap de produto.


# 3. Eventos

 Todos os eventos aqui definidos ocorrem durante o tempo de uma Sprint, que possui duração de uma semana,
 a partir do sábado. Cada sprint possui como resultado entregas de um ou mais artefatos, podendo ser de código
 ou documentação.

# 3.1. Reunião de Planejamento da Sprint

Essa reunião realizada no inicio da sprint caracteriza-se por definir seu objetivo e Requisitos
que devem ser entregues. Será utilizada a ferramenta Planning Poker para definição de pontos
das histórias priorizadas na sprint. O time box deste evento é de uma hora.

# 3.2. Reuniões standup

Essas reuniões são realizadas ao decorrer da sprint, para que haja um acompanhamento
das tarefas e possível remoção de impedimentos. Cada membro da equipe deve responder as seguintes
perguntas:
- O que fiz desde o último encontro para cumprir o que me foi atribuido nessa sprint?
- O que farei hoje para cumprir o que me foi atribuido nessa sprint?
- Existe algum impedimento para cumprir o que me foi atribuido?

 O time box deste evento é de quinze minutos.

# 3.3. Reunião de Revisão

Essa reunião é voltada para a inspeção do produto entregue ao final da sprint,
certificando que as unidades desenvolvidas estão bem integradas e entregues conforme
o estabelecido. Essa reunião tem time box de 40 minutos.

# 3.4. Reunião de Retrospectiva

Essa reunião é voltada para discussão do processo, discutindo possíveis melhorias,
sucesso e falhas.
 O time box deste evento é de trinta minutos.

# 4. Artefatos

# 4.1. Incremento do Produto

É o produto entregue, até a presente sprint bem como os artefatos que o compõe.

# 4.2. Backlog do Produto e da Sprint
São os requisitos do projeto, documentados por meio de issues do Github e gerenciados pelo PO.

# 5. Políticas

## 5.1. Políticas de Desenvolvimento

### 5.1.1. Entrega de Código
  As issues relacionadas à código só serão consideradas entregues se seguirem as seguintes restrições:
  1. Não fere as métricas definidas
  2. Possui sucesso na integração contínua
  3. Possui testes condizentes com a funcionalidade
  4. Compreende todos os critérios de aceitação definidos na issue

### 5.1.2. Ambiente de desenvolvimento
  Todos os membros da equipe devem configurar suas máquinas para que elas possuam o ambiente de desenvolvimento.

## 5.2. Políticas de documentos
  Todos os documentos criados no projeto devem estar disponíveis por sua Github Pages em: https://fga-eps-mds.github.io/2018.2-GrupoMDIC/. Cada documento deve ser criado
  em branch de acordo com a política de branches, e deve ser revisado antes de aceito.

## 5.3. Políticas de papéis

  Cabe, a cada papel de EPS definir e desenvolver seu roadmap.

## 5.4. Políticas de eventos
  - Os eventos definidos devem cumprir o time box;
  - Cabe aos membros serem pontuais nos horários marcados pelo time.
