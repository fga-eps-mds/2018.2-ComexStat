---
id: microsserviços
title: Microsserviços
---

## 1. Definição

O estilo de arquitetura de microsserviços é uma abordagem que desenvolve um aplicativo único como uma suite de pequenos serviços, cada um executando seu próprio processo e se comunicando através de mecanismos leves, muitas vezes em uma API com recursos HTTP. Esses serviços são construídos em torno de capacidades de negócios e funcionam através de mecanismos de deploy independentes totalmente automatizados. Há o mínimo possível de gerenciamento centralizado desses serviços, que podem ser escritos em diferentes linguagens de programação e utilizam diferentes tecnologias de armazenamento de dados. Os micro serviços são componentes autônomos e de baixo acoplamento, logo, não há necessidade que sejam construídos com a mesma linguagem ou que sejam processados na mesma plataforma.

Para começar a explicar o estilo de microsserviços, é útil compará-lo com o estilo de aplicativo monolítico, construído como uma única unidade. Aplicativos corporativos geralmente são construídos em três partes principais: a interface de usuário do lado do cliente (que consiste em páginas HTML e JavaScript executadas em um navegador na máquina do usuário) um banco de dados (que consiste em muitas tabelas inseridas em um sistema de gerenciamento de banco de dados comum, geralmente relacional), e um aplicativo do lado do servidor. O aplicativo do lado do servidor lida com as solicitações HTTP, executa a lógica do domínio, recupera e atualiza dados do banco de dados, e seleciona e preenche as visualizações HTML a serem enviadas para o navegador. Esse aplicativo do lado do servidor é monolítico - um executável lógico único. Quaisquer mudanças no sistema envolvem criação e deploy de uma nova versão do aplicativo no lado do servidor.

O servidor monolítico é o caminho natural para abordar a construção de um sistema desse tipo. Toda a sua lógica para lidar com uma solicitação é executada em um único processo, o que lhe permite usar os recursos básicos de sua linguagem para dividir a aplicação em classes, funções e namespaces. Com um pouco de cuidado, você pode executar e testar o aplicativo no laptop de um desenvolvedor, usando um pipeline de deploy para garantir que as mudanças sejam devidamente testadas e colocadas em produção. Você pode escalar um aplicativo monolítico horizontalmente, executando muitas instâncias atrás de um balanceador de carga.

## 2. As vantagens da Arquitetura de Microserviços

Implantar a arquitetura de microsserviços vai proporcionar diferentes benefícios para a estrutura do seu negócio:
* Os desenvolvedores usufruem de liberdade maior para o desenvolvimento de serviços de modo independente;
* Implantação automática através de ferramentas de integração contínua e código aberto;
* O conteiner web tem inicialização mais rápida;
* Possibilidade de utilizar códigos escritos em linguagens diferentes para diferentes serviços, usando uma “língua franca” para comunicação entre eles (como Json ou XML);
* Oportunidade para os desenvolvedores usarem as tecnologias mais atuais;
* Arquitetura de fácil compreensão e bastante adaptável às mudanças, o que favorece o aprendizado dos profissionais novatos, contribuindo para maior produtividade da equipe;
* Fácil ampliação e integração dos microsserviços com serviços terceirizados, através de APIs, por exemplo;
* Código organizado em função de capacidades de negócio, dando mais visão das ofertas e necessidades dos clientes;
* Mudanças necessárias poderão ser aplicadas somente sobre o serviço específico, sem necessidade de modificar todo o aplicativo. Atualizações de funcionalidades também passam a ser menos complexas;
* Gerenciamento otimizado das falhas (por exemplo, caso um serviço venha a falhar, os outros continuarão trabalhando).

Através dos Microserviços, é possível identificar falhas e gargalos com mais eficiência, visto que o particionamento favorece uma visão mais detalhada de cada serviço.

## 3. Referências

> * FOWLER, Martin & LEWIS, James. "Microsserviços em Poucas Palavras". Disponível em: <https://www.thoughtworks.com/pt/insights/blog/microservices-nutshell>. Acessado em 22/08/2018.
>* PELOI, Ricardo. "Como Implementar uma Verdadeira Arquitetura de Microsserviços na sua Empresa". Disponível em: <https://sensedia.com/blog/soa/implantar-arquitetura-de-microservicos/>. Acessado em 22/08/2018.
>* SAMPAIO, Cleuton. "Micro Serviços: O que são e para que servem?" .Disponível em: <http://www.obomprogramador.com/2015/03/micro-servicos-o-que-sao-e-para-que.html>. Acessado em 22/08/2018.
>* "O que são Microsserviços? - Entrevista com Edson Yanaga".  Disponível em: <https://www.youtube.com/watch?v=pZjTBTpieOA>. Acessado em 22/08/2018.
