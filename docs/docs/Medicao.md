---
id: medicao
title: Indicadores e Métricas
---

## Introdução

É fundamental para saúde do projeto realizar seu monitoramento, coletando informações
que podem auxiliar em decisões de negócio, melhoria do processo e seu gerenciamento.
Para este fim, foi utilizada uma simplificação do processo GQM(Goal-Quest-Metric, http://www.agilebuddha.com/software-metrics/which-software-metrics-and-why-introducing-basilis-gqm-approach/), para levantamento
das medições que serão realizadas no projeto.

Por muitas vezes a medição e análise de software faz parte do processo de controle
de qualidade, onde os componentes de um sistema que são medidos e analisados
separadamente e depois há uma comparação de métricas de acordo com os dados do projeto.

### GQM de Produtividade

![GQM_Produtividade](https://fga-eps-mds.github.io/2018.2-GrupoMDIC/img/GQM_Produtividade.png)

O time possui como prazo para realização do projeto a duração das disciplinas de MDS e EPS,
no segundo semestre de 2018. Logo, o aproveitamento do tempo deve ser otimizado, tentando
entender como o time pode ser produtivo. Para isso, foram levantadas três perguntas:

#### O conhecimento do time está nivelado?

Caso o conhecimento não seja distribuído dentro do time, existe a possibilidade de sobrecarga de alguns membros
e a não utilização do potencial de membros que ainda não possuem as ferramentas e conhecimento necessários para ajudar o time.

#### O time está seguindo o planejamento da sprint?

Deve-se realizar um planejamento de acordo com a capacidade do time. Logo, o planejamento
realizado tem como objetivo trabalho do time durante toda a sprint. Caso seja diagnosticado
que o time entregou tudo muito antes da finalização, ou não conseguiu entregar todo o trabalho
alocado, existem problemas que devem ser atacados.

#### Quão produtiva é a equipe?

Para que se possa melhorar a produtividade da equipe, é fundamental, em primeiro lugar, entender
sua produtividade, e fazer planejamentos de acordo com esta.

#### Métricas e Indicadores

- Pontos

  Os pontos serão utilizados para estimar a dificuldade de entrega das issues. Cada issue
  terá sua estimativa em pontos, utilizando a escala de fibonacci: 1, 2, 3, 5, 8, 11, 13 e 21.

- Gráfico de Burndown
  É um gráfico dos pontos da sprint (eixo y) e os dias da semana (eixo x) que possibilita
  monitoramento do trabalho durante a execução da sprint. Possíveis interpretações são:
  Se o trabalho está sendo feito de forma uniforme durante a sprint, as histórias estão sendo
  entregues apenas ao final da sprint, por exemplo.

-  Velocity

É a média de pontos entregues do time por sprint. Facilita a estimativa de alocação de pontos
para as próximas sprints.

- Quadro de Horas
Um documento excel compartilhado na pasta do drive do time, cada membro deve
preencher o tempo de dedicação ao projeto durante a semana e quais atividades foram
realizadas.

- Earned value management (EVM)
  É responsável por medir a performance técnica no projeto, em relação ao prazo e custo.

- Diferença entre nível de conhecimento dos membros no quadro de conhecimento
  Cada membro deve preencher a coluna relativa ao conhecimento na tecnologia indicada,
  seguindo a legenda:
  - :D - Consigo ensinar outras pessoas
  - :) - Consigo me virar
  - :l - Sei mais ou menos
  - :( - Sei muito pouco
  - :S - Não tenho a menor ideia
  Dessa forma, fica transparente como está o conhecimento dividido no time e é mais
  fácil a formação de pareamentos



### GQM de Gerência de Riscos

![GQM_Riscos](https://fga-eps-mds.github.io/2018.2-GrupoMDIC/img/GQM_Riscos.png)

#### Matriz de Riscos

É elicitada uma lista de possíveis riscos do projeto. A cada sprint, esses
riscos são analisados e priorizados, tendo as seguintes grandezas relacionadas:

- **Impacto**(I) : É mensurado com nota de 1 a 5, possuindo o seguinte significado,

  - **5**: Catastrófico - o impacto ocasiona colapso às ações de gestão, a viabilidade
  estratégica pode ser comprometida;
  - **4**: Grande - o impacto compromete significativamente às ações de gestão, os
  objetivos estratégicos podem ser fortemente comprometidos;
  - **3**: Moderado - o impacto é significativo no alcance das ações de gestão;
  - **2**: Pequeno - o impacto é pouco relevante ao alcance das ações de gestão;
  - **1**: Insignificante - o impacto é mínimo no alcance das ações de gestão.


- **Probabilidade** (P): Também possui nota de 1 a 5, atribuídas de acordo com a frequência observada/esperada do evento,
  - **5** (>=90%): Evento esperado que ocorra na maioria das circunstâncias
  - **4** (>=50% < 90%): Evento provavelmente ocorra na maioria das circunstâncias
  - **3** (>=30% < 50%): Evento deve ocorrer em algum momento
  - **2** (>=10% < 30%): Evento pode ocorrer em algum momento
  - **1** (< 10%): Evento pode ocorrer apenas em circunstâncias excepcionais

Possuindo as duas notas, o risco possui uma nota final, que é o produto das duas, (I*P), o **Nível de Risco**, que possui
a seguinte análise:

- Risco crítico:  >=15<=25
- Risco  alto: >=8<=12
- Risco moderado: >=4<=6
- Risco pequeno: >=1<=3


#### Burndown de Riscos

Deve-se somar o nível dos riscos, calculado em métrica anterior, e acompanhá-los em relação ao eixo do tempo.
O ideal é observar durante o decorrer do projeto, a diminuição dos riscos.

### GQM de Manutenção

![GQM_Codigo](https://fga-eps-mds.github.io/2018.2-GrupoMDIC/img/GQM_codigo.png)

A manutenção de software preocupa-se em lidar com mudanças na parte do ciclo de vida
do desenvolvimento de software. Para efetivamente descrever problemas e apontar suas
causas, mantenedores interagem continuamente com o time, cliente e usuários.
Como isso, foram elaboradas as seguintes perguntas:

#### Quanto o código está sendo testado?

Os testes ajudam o desenvolvedor a garantir a qualidade interna do código, dando feedback
automatizados e permitindo uma manutenção com menor custo.

#### O código está seguindo boas práticas de programação?

O uso de regras e boas práticas é o melhor jeito de gerar a legibilidade do código, contribuindo significativamente para
que o ciclo de desenvolvimento de sistemas ocorra de maneira mais ágil, prática e de fácil manutenção.

#### O código é complexo?

A ideia é basicamente contar o número de caminhos diferentes que um método pode ter.
Quanto maior esta complexidade, mais difícil a manutenção e a testagem do código.

#### Métricas e Indicadores

- Porcentagem de código testado: Número de linhas percorridas durante os testes dividido pelo número de linhas totais de código
- Número de linhas por método: Definidos em 35 linhas por método em python
- Números de erros com a folha de estilo: Não devem existir nenhum erro detectado pela ferramenta de análise estática
- Duplicação de código: deve-se evitar a duplicação de código, a saúde dessa métrica será analisada por meio de análise de ferramenta
- Complexidade ciclomática

## 3. Referências

> * . Matriz de Riscos. Ministério do Planejamento. Disponível em <http://www.planejamento.gov.br/assuntos/gestao/controle-interno/matriz-de-riscos>. Acesso em 02/09/2018.
> * Boas Práticas de programação. Disponível em: <https://www.devmedia.com.br/boas-praticas-de-programacao/21137>. Acessado em 02/09/2018.
> * A importância dos Testes para a Qualidade de Software. Disponível em: <https://www.devmedia.com.br/a-importancia-dos-testes-para-a-qualidade-do-software/28439>. Acessado em 02/09/2018.
> * Medindo a complexidade do seu Código. Disponível em: <http://blog.caelum.com.br/medindo-a-complexidade-do-seu-codigo/>. Acessado em 02/09/2018.
