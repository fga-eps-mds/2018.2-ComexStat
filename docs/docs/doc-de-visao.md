---
id: docVisao
title: Documento de Visão
---

# Histórico da Revisão

| **Data** | **Versão** | **Descrição** | **Autor** |
| :------: | :--------: | :-----------: | :-------: |
|29/08/2018|0.1.0|Abertura do documento|Rogério Junior, Marcos Nery e André Lucas|
|29/08/2018|0.2.0|Preenchimento dos tópicos da introdução|Rogério Junior, Marcos Nery e André Lucas|
|30/08/2018|0.3.0|Preenchimento inicial dos tópicos do Posicionamento|Marcos Nery|
| 30/08/2018 | 0.4.0 | Finalização dos tópicos de Posicionamento | Rogério Júnior |
| 30/08/2018 | 0.5.0 | Preenchimento inicial dos tópicos de Descrição | André Lucas |
| 30/08/2018 | 0.6.0 | Preenchimento do tópico Perfis dos Usuários | João Victor | 
| 30/08/2018 | 0.7.0 | Preenchimento inicial dos tópicos da visão geral | Marcos Nery|

# 1. Introdução

Nesta introdução serão abordados tópicos referentes a uma visão geral do produto, definindo seu propósito, escopo, definições, acrônimos, abreviações e referências

## 1.1 Propósito

Esse documento visa especificar todo o escopo de funcionamento do Comexserv, deixando claro seu objetivo, a razão de sua necessidade e a forma como busca solucionar os problemas aos quais se propõe, deixando claro possíveis restrições.

## 1.2 Escopo

Para suprir a necessidade de um melhor sistema de vizualização de dados relacionados a prestação de serviços no Brasil o Comexserv será integrado por uma plataforma web, cujas capacidades irão abranger funcionaliades como: gerar tabelas a partir de dados providos pelo banco de dados do MDIC, dando ao usuario a possibilidade de filtrar os resultados a partir de informações específicas de acordo com as suas necessidades, e disponibilizar os resultados de tais tabelamentos para download em .scv ou similar, de tal forma que o usuário tenha facilidade para salvar os dados que são de seu interesse.

## 1.3 Definições, acrônimos e abreviações

| **Abreviação** | **Definição** |
| :--------: | :-------: |
| MDIC | Ministério da Industria, Comércio Exterior e Serviços |
| MDS | Métodos de Desenvolvimento de Software |
| EPS | Engenharia do Produto de Software |
| FGA | Faculdade do Gama |
| UnB | Universidade do Gama |

## 1.4 Referências

## 1.5 Visão Geral

A organização do documento é feita de maneira a prover ao leitor a capacidade de através do mesmo entender o produto em seus vários aspectos de forma coesa. Para tal, são apresentados primeiramente os tópicos referentes a função geral do software e as motivações que levaram a sua criação, após isso, é descrito o posicionamento do produto em relação ao mercado e as partes interessada, incluindo a forma como a criação do sistema afetará os usuários. Por fim, são descritas as principais funcionalidades do software, bem como algumas de suas restrições e requisitos.

# 2.Posicionamento:

## 2.1 Oportunidade de Negócios

O Comexserv, ao tornar mais fácil o acesso aos dados relacionados à prestação de serviços no Brasil e dar também aos usuários a possibilidade de filtrar e vizualisar as informações desejadas de forma mais adequada as suas necessidades, resolve dois principais problemas: a dificuldade no acesso a esses dados pela população de forma geral, e a dificuldade por parte dos interessados em conseguir tirar conclusões úteis a partir das informações por falta de ferramentas de filtragem e visualização. Dessa forma, o sistema dá mais eficiência para as funções do MDIC quanto a exposição dos dados relacionados ao comércio de serviçoes, bem como para qualquer análise que utilize essas informações como base.

## 2.2 Instrução do Problema

|  | |
| :--------: | :-------: |
| **Problema**| Não há um sistema capaz de prover funções de acesso, filtragem e visualização aos dados coletados pelo MDIC relacionados ao comércio de serviços no Brasil|
| **Funções afetadas** | Análise e visualização dos dados de comércio de serviços |
| **Efeito** | Difícil acessibilidade aos dados coletados e falta de ferramentas que possibilitem uma melhor análise dos mesmos|
| **Solução** |Criação de uma plataforma web que dá ao usuário a possibilidade de acessar, filtrar e vizualisar os dados de forma mais adequada|

## 2.3 Instrução de Posição do produto

|  |  |
| :--: | :--: |
| **Público Alvo** | Público em Geral |
| **Carência** | Necessidade de informações relacionadas ao comércio de bens de serviço brasileiro |
| **Solução** | ComexServ |
| **Descrição da Solução** | Uma plataforma web que permita ao usuário o acesso aos dados de forma fácil e intuitiva, a partir de uso de filtros e detalhamento, e que estes possa ser obtido no formato .csv |
| **Diferenciais** | Facilidade no acesso à informação |

### 3. Descrição dos Envolvidos e dos Usuários

#### 3.1. Resumo dos Envolvidos

| Nome | Descrição | Responsabilidade|
|-----|-------|---------|
| Equipe de Programação | Estudantes da Universidade de Brasilia da disciplina de Métodos de Desenvolvimento de Software. | Desenvolvimento do software esclarecido nesse documento, além de implementar testes e fazer o deploy do mesmo. |
| Equipe de Gestão do Projeto | Estudantes da Universidade de Brasília da disciplina de Engenharia do Produto de Software | Acompanhar o processo de desenvolvimento da aplicação, identificando possíveis problemas e apontando caminhos e soluções. |

#### 3.2. Resumo dos Usuários

| Nome | Descrição |
|------|--------|
| Público Geral | Pessoas que tenham interesse em dados e informações sobre comércio de serviços. |
| Funcionários | Funcionários do MDIC que trabalham nas áreas administrativas e necessitam filtrar tais informações. |

#### 3.3. Ambiente do Usuário
O acesso aos serviços do software poderá ser feito por navegadores de internet, como:
* Google Chrome;
* Mozila Firefox;
* Apple Safari
* Opera

## 3.4 Perfis dos Usuários

### 3.4.1 Público Geral

| Representantes | Público Geral |
| :--------: | :-------: |  
| Descrição | Pessoas que buscam entender melhor o comercio de serviços |
| Tipo | Usuário interessado em estatísticas do comércio exterior de serviços |
| Responsabilidades | O usuário não tem responsabilidades sobre a plataforma web |
| Critérios de Sucesso | Achar o que o usuário deseja |
| Envolvimento | Baixo |
|Problemas/Comentários | - |

### 3.4.2 Funcionários

| Representantes | Funcionários |
| :--------: | :-------: |  
| Descrição | Funcionários do MDIC |
| Tipo | Funcionários que necessitam de dados para analise do comercio de serviços |
| Responsabilidades | Acessar a plataforma para obter os dados que precisa |
| Critérios de Sucesso | Conhecer a plataforma e toda suas funcionalidades |
| Envolvimento |  Alto |
| Problemas/Comentários | - |

## 3.6 Principais necessidades dos usuários ou envolvidos

| **Necessidade** | **Prioridade** | **Interesses** | **Solução Atual** | **Solução Proposta** |
| :--------: | :-------: | :--------: | :-------: | :--------: |
| Ter acesso aos dados em outros formatos, mais compactos e brutos | Alta | Ter tudo reunido em um arquivo para diversos usos como pesquisas, análise de dados, etc.  | Acessar o site do MDIC, procurar pelas estatísticas de 2017 e baixá-las | Disponibilizar o download através de botões na página de resultado da pesquisa |
| Filtrar a busca dos dados sobre o comércio de serviços | Alta | Facilitar ao usuário a obtenção dos dados de forma mais rápida e objetiva | Manualmente categorizar e filtrar os dados | Disponibilizar filtros e categorias na página de busca |
| Visualizar os dados de forma mais organizada | Baixa | Entender e absorver os dados com maior facilidade | Gerar gráficos manualmente usando as planilhas disponibilizadas pelo MDIC | Disponibilizar gráficos, tabelas e outras ferramentas interativas para uma descrição mais clara e visual das informações |

# 4.Visão Geral do Produto
## 4.1 Perspectiva do produto
 
 O Comexserv visa prover ao usuário facilidade de acesso a informações referentes ao comércio exterior brasileiro de serviços, viabilizando isso por meio de ferramentas de pesquisas no banco de dados, com a possibilidade da utilização de filtros e formas diferentes de visualização. Além disso, também são disponibilizadas formas coerentes para que os dados de interesse possam ser extraídos, em formato .csv ou similar.


## 4.2 Resumo das capacidades

| **Benefícios para o Cliente** | **Recursos de Suporte** |
| :--------: | :-------: |  
| Consulta rápida e fácil aos dados disponibilizados pelo MDIC | Pesquisa no banco de dados  |
| Capacidade de filtrar as informações pesquisadas | Opções para obter resultados de acordo com filtros de categorias pré-determinadas ou customizadas  |
| Possibilidade de fazer o download das informação desejadas| Recurso que permite ao usuário extrair uma determinada seleção de dados em formato tabular|