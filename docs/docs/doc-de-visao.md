---
id: docVisao
title: Documento de Visão
---

## 1. Introdução


 Nesta introdução serão abordados tópicos referentes a uma visão geral do produto, definindo seu propósito, escopo, definições, acrônimos, abreviações e referências.

### 1.1 Propósito

 Esse documento visa especificar todo o escopo de funcionamento do ComexStat, deixando claro seu objetivo, a razão de sua necessidade e a forma como busca solucionar os problemas aos quais se propõe, deixando claro possíveis restrições. Dessa forma, sua principal utilidade objetiva também, ao esclarecer o que é o sistema para os desenvolvedores, clientes e usuários, estabelecer entre os mesmos um eficiente alinhamento de ideias.

### 1.2 Escopo

Suprir a necessidade de um sistema proeminente na visualização de dados relacionados ao comércio de bens no Brasil. Proporcionando algo que seja mais intuitivo ao usuário, o ComexStat será integrado por uma plataforma web, cujas capacidades abrangem funcionalidades como:

* Ter uma API de pesquisa bem documentada e de fácil uso, com querys estruturados de maneira intuitiva
* Gerar tabelas a partir de dados providos pelo banco de dados do MDIC, dando ao usuário a possibilidade de filtrar os resultados a partir de informações específicas, de acordo com as suas necessidades;
* Disponibilizar os resultados de tais tabelamentos para download, de tal forma que o usuário tenha facilidade para salvar os dados que são de seu interesse;


Além disso, o sistema também deverá ser feito de forma adequada para integrar posteriormente, além das informações relacionadas ao comércio exterior de bens, os dados relacionados ao comércio exterior de serviços no Brasil.


### 1.3 Definições, acrônimos e abreviações

| **Abreviação** | **Definição** |
| :--------: | :-------: |
| MDIC | Ministério da Industria, Comércio Exterior e Serviços |
| MDS | Métodos de Desenvolvimento de Software |
| EPS | Engenharia do Produto de Software |
| FGA | Faculdade do Gama |
| UnB | Universidade do Brasília |

### 1.4 Referências

  **PORTAL IFRN .MODELO DE UM DOCUMENTO DE VISÃO.** Disponível em:
  <http://docente.ifrn.edu.br/abrahaolopes/2015.1-integrado/3.2401.1m-projeto-integrador/modelo-de-documento-de-visao-do-sistema/view>. Acessado em: 29 de Agosto de 2018.

  **SISTEMA DE PESQUISA DE DADOS RELACIONADOS AO COMÉRCIO EXTERNO BRASILEIRO DE BENS.** Disponível em:
  <http://comexstat.mdic.gov.br/pt/home>. Acessado em: 29 de Agosto de 2018.

  **FILTROS PARA ANÁLISE DE DADOS DO SISCOSERV.** Disponível em:
   <http://www.mdic.gov.br/portal/dashboard.html>. Acessado em: 28 de Agosto de 2018.

### 1.5 Visão Geral

A organização do documento é feita de maneira a prover ao leitor a capacidade de através do mesmo entender o produto em seus vários aspectos de forma coesa. Para tal, são apresentados primeiramente os tópicos referentes a função geral do software e as motivações que levaram a sua criação, após isso, é descrito o posicionamento do produto em relação ao mercado e as partes interessadas, incluindo a forma como a criação do sistema afetará os usuários. Por fim, são descritas as principais funcionalidades do software, bem como algumas de suas restrições e requisitos.

***
## 2. Posicionamento
***

### 2.1 Oportunidade de Negócios

O ComexStat, tornando mais fácil o acesso aos dados relacionados ao comércio exterior de bens, e posteriormente serviços, no Brasil, proporciona também aos usuários a possibilidade de trabalhar com as informações desejadas de forma mais adequada as suas necessidades. Resolvendo portanto principalmente os problemas relacionados a atual dificuldade em acessar os dados e tirar deles alguma conclusão, por conta da forma pela qual os mesmos são disponibilizados e por seu grande volume, além da falta de ferramentas que possibilitem ao usuário filtrar, visualizar graficamente, e exportar de formas variadas esses dados, recursos estes que são presentes no ComexStat. Dessa forma, o sistema dá mais eficiência para as funções do MDIC quanto a exposição das informações, bem como para qualquer gestor ou produtor de bens ou serviços que tenha interesse nos dados disponibilizados para fazer qualquer tipo de análise.

### 2.2 Instrução do Problema

|  | |
| :--------: | :-------: |
| **Problema**| Dados relacionados ao comércio exterior de bens e serviços no Brasil são abertos a população porém de difícil uso e interpretação, por conta do seu grande volume e formato disponibilizado|
| **Funções afetadas** | Análise e visualização dos dados de comércio de bens e serviços |
| **Efeito** | Os dados acabam por não serem utilizados|
| **Solução** | Uma plataforma web que permita ao usuário um acesso mais fácil aos dados e as ferramentas de filtragem e pesquisa|

### 2.3 Instrução de Posição do produto

|  |  |
| :--: | :--: |
| **Público Alvo** | Gestores e produtores de bens ou serviços|
| **Carência** | Necessidade de um melhor acesso e ferramentas de manejo a informações relacionadas ao comércio exterior de bens e serviço no Brasil |
| **Solução** | ComexStat |
| **Descrição da Solução** | Uma plataforma web que permita ao usuário o acesso aos dados de forma fácil e intuitiva, a partir de uso de filtros de filtros e agrupamentos, além da possibilidade de exportação das informações em formatos como .csv  |
| **Diferenciais** | Facilidade no acesso e ferramental para proporcionar uma melhor interpretação dos dados, oferecendo diversos recursos que não estão presentes no atual sistema, como permalinks para compartilhamento de resultados e as já citadas soluções de exportação. Isso tudo contando com uma API bem documentada  |

***
## 3. Descrição dos Envolvidos e dos Usuários
***

### 3.1. Resumo dos Envolvidos

| Nome | Descrição | Responsabilidade|
|-----|-------|---------|
| Equipe de Programação | Estudantes da UnB da disciplina de MDS | Elaboração dos documentos de visão e de arquitetura; Desenvolvimento do software esclarecido nesse documento; Atendendo aos requisitos definidos; Utilizar as práticas ágeis para otimizar o processo. |
| Devops | Estudante da UnB da disciplina de EPS |  Configurar ambiente de desenvolvimento, homologação e produção utilizando contâiners; Definir política de commits e branchs de acordo com o git flow; Garantir que o time siga o git flow; Construir o pipeline de integração e deploy contínuos; Definir roadmap de deploy contínuo. |
| Arquiteto | Estudante da UnB da disciplina de EPS | Definir o roadmap de requisitos; Garantir que o time de desenvolvimento siga a arquitetura; Propor arquitetura de micro serviços e a configuração de contâiners com micro serviços. |
| Scrum Master (SM) | Estudante da UnB da disciplina de EPS | Gerenciar comunicação do Time; Garantir que os membros sigam o processo Definido; Gerenciar riscos; Definir, monitorar e controlar indicadores e metricas de produtividade, utilizando-os para tomadas de decisões no projeto; Definir e seguir roadmap para produtividade máxima do time. |
| Product Owner (PO) | Estudante da UnB da disciplina de EPS | Ter a visão de Produto; Elaborar o Termo de Abertura; Elaborar a Estrutura Analítica do Projeto (EAP); Definir plano de negócio; Gerenciar backlog de histórias; Desenvolver identidade visual e guia de usabilidade do produto; Definir roadmap de produto. |
| Cliente | Requisitou a aplicação | Fornecer e validar os requisitos da aplicação |

### 3.2. Descrição dos Usuários   

| Representantes | Gestores em empresas ou autônomos provedores de bens ou serviços |
| :--------: | :-------: |
| Descrição | Indivíduos que por sua função/ocupação profissional podem ter interesse em acessar os dados disponibilizados pelo MDIC, para finalidades como análise de mercado ou similares, muitas vezes servindo como base para tomada de decisões relacionadas a investimentos/negócios|
| Responsabilidades | Fazer pesquisas filtrando os resultados e utilizar ferramentas de visualização gráfica |
| Critérios de Sucesso | Entender de forma adequada os dados pesquisados sobre bens e serviços e conseguir exportá-los caso desejado |

### 3.3. Ambiente do Usuário
O acesso aos serviços do software poderá ser feito por navegadores de internet, como:
* Google Chrome;
* Mozila Firefox;


### 3.4 Principais necessidades dos usuários ou envolvidos

| **Necessidade** | **Prioridade** | **Interesses** | **Solução Atual** | **Solução Proposta** |
| :--------: | :-------: | :--------: | :-------: | :--------: |
| Ter acesso aos dados em outros formatos | Alta | Ter tudo reunido em um arquivo para diversos usos como pesquisas, análise de dados, etc.  | Acessar o site do MDIC, procurar pelas estatísticas de 2017 e baixá-las | Disponibilizar o download dos dados em diversos formatos através de botões na página de resultado da pesquisa |
| Filtrar a busca dos dados | Alta | Facilitar ao usuário a obtenção dos dados de forma mais rápida e objetiva | Manualmente categorizar e filtrar os dados | Disponibilizar filtros e categorias na página de busca |
| Agrupar os dados | Alta | Permitir ao usuário visualizar os dados em forma de agrupamentos, constituindo agregações de dados com base em um período de datas especificadas | Manualmente agrupar os dados disponíveis | Agrupar os dados pela utilização dos tipos de query previamente definidos  e disponíveis na API|
| Ter uma API de fácil uso | Alta| Poder realizar todas as etapas de pesquisa e filtragem por meio da API | Não há | API em GraphQL bem documentada e com querys estruturados de forma intuitiva |
| Permalinks para as pesquisas| Média|Sistema de permalinks para permitir o compartilhamento das pesquisas feitas |Não há | Páginas de pesquisa geram permalinks com a pesquisa e os filtros/agrupamentos utilizados |
| Visualizar os dados de forma mais organizada | Baixa | Entender e absorver os dados com maior facilidade | Gerar gráficos manualmente usando as planilhas disponibilizadas pelo MDIC | Disponibilizar tabelas e outras ferramentas interativas para uma descrição mais clara e visual das informações |

***
## 4.Visão Geral do Produto
***

### 4.1 Perspectiva do produto

  O ComexStat visa prover ao usuário facilidade de acesso a informações referentes ao comércio exterior brasileiro de bens, descomplicando a interpretação e visualização dos dados por meio de filtros de pesquisas, agrupamentos e uma fácil visualização do resultado. Além disso, também são disponibilizadas formas coerentes para que os dados de interesse possam ser extraídos, em formato .csv.


### 4.2 Resumo das capacidades

| **Benefícios para o Cliente** | **Recursos de Suporte** |
| :--------: | :-------: |
| Consulta rápida e fácil aos dados disponibilizados pelo MDIC | Pesquisa no banco de dados  |
| Capacidade de filtrar as informações pesquisadas | Opções para obter resultados de acordo com filtros de categorias pré-determinadas ou customizadas  |
| Possibilidade de fazer o download das informações desejadas| Recurso que permite ao usuário extrair uma determinada seleção de dados, em formatos como .csv|


***
## 5.Recursos do Produto
***

   * Área de acesso aos dados disponibilizados acerca do comércio externo brasileiro de bens.
   * Opções para filtrar as pesquisas por categorias específicas.
   * Opções para agrupar os dados por quaisquer formas desejadas.
   * Layout intuitivo, para que o usuário possa selecionar os filtros que melhor se encaixam as suas necessidades.
   * Opções para ordenar os resultados encontrados a partir de uma coluna específica.
   * Opções para incluir ou retirar colunas de informação da pesquisa feita.
   * Permitir ao usuário, pelo uso de permalinks, compartilhar facilmente um conjunto específico de resultados.

***
## 6: Restrições
***

### 6.1 Restrições de implementação

 O sistema deverá ser implementado na linguagem Python, construindo uma aplicação web com o uso do framework Django.

### 6.2 Restrições externas

 Dentre as restrições externas as que mais irão influenciar são a inexperiência com a linguagem e frameworks, além de possíveis transtornos entre a equipe de desenvolvimento.

### 6.3 Restrições de design

O sistema deve ter uma interface que seja de fácil uso para pessoas. Dessa forma, será necessária uma plataforma intuitiva, com ícones e botões de fácil pesquisa e acesso.

### 6.4 Restrições de confiabilidade

O sistema deverá ter cobertura de testes - mínimo de 90%.

***
## 7:	Faixas de Qualidade
***

 Para maior eficiência, a aplicação será web, pois o gerenciamento de dados e informações seria dificultado no caso de uma aplicação exclusiva para aparelhos mobile.

***
## 8. Requisitos do Produto
***

### 8.1 Requisitos do Sistema

 O sistema poderá ser acessado pelo usuário através de um navegador, tendo a necessidade de conexão com a internet.

### 8.2 Requisitos de Design

 O sistema deverá ser intuitivo e autoexplicativo, possibilitando uma fácil interação com o usuário, seguindo uma estruturação de querys em JSON na API com os campos da pesquisa e os filtros desejados bem explicitos.

### 8.3 Requisitos de Portabilidade

 O sistema é utilizável através da maior parte dos navegadores web atuais, sendo compatível com os principais sistemas operacionais como Windows, Mac OS e Linux.

### 8.4 Requisitos de Confiabilidade

 O sistema deve se comprometer em disponibilizar os dados de maneira transparente e confiável aos usuários.

## Histórico da Revisão

| **Data** | **Versão** | **Descrição** | **Autor** |
| :------: | :--------: | :-----------: | :-------: |
|29/08/2018|0.1.0|Abertura do documento|Rogério Junior, Marcos Nery e André Lucas|
|29/08/2018|0.2.0|Preenchimento dos tópicos da introdução|Rogério Junior, Marcos Nery e André Lucas|
|30/08/2018|0.3.0|Preenchimento inicial dos tópicos do Posicionamento|Marcos Nery|
| 30/08/2018 | 0.4.0 | Finalização dos tópicos de Posicionamento | Rogério Júnior |
| 30/08/2018 | 0.5.0 | Preenchimento inicial dos tópicos de Descrição | André Lucas |
| 30/08/2018 | 0.6.0 | Preenchimento do tópico Perfis dos Usuários | João Victor |
| 30/08/2018 | 0.7.0 | Preenchimento inicial dos tópicos da visão geral | Marcos Nery|
| 30/08/2018 | 0.8.0 | Melhorias e preenchimento dos Tópicos 6 e 7 | André Lucas |
| 30/08/2018 | 0.9.0 | Preenchimento do tópico referente aos recursos do sistema |Marcos Nery|
| 30/08/2018 | 0.10.1| Preenchimento das referências e correções gerais|Marcos Nery|
| 30/08/2018 | 0.11.1| Preenchimento do tópico Requisitos do Produto | Caio Santos |
| 31/08/2018 | 1.0.0 | Correções ortográficas e organização final da primeira versão do documento|Marcos Nery|
| 06/09/2018 | 1.1.1 | Alterações no documento com base nas revisões feitas e novas informações acrescentadas| Marcos Nery, Rogério Júnior, Kaique Borges, André Lucas, João Victor e Caio Santos|
| 08/09/2018 | 2.0.0 | Feitas as revisões solicitadas pela Scrum Master | Marcos Nery e Rogério Júnior |
| 25/11/2018 | 3.0.0 | Refatoração de alguns tópicos após mudanças de visão durante o projeto | Marcos Nery |
