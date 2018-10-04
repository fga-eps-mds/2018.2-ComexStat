---
id: politicaBranches
title: Política de Branches
---

# Política de Branches

## Divisão e como usar as branches
Com o intuito de possuir uma melhor dinâmica de mudanças de código, é importante que tenhamos uma boa política de branches. Este documento servirá de base para criação de branches e como serão organizadas, estas baseadas no **git flow** que é um modelo de organização de branches.

Aqui será descrito como funcionará as branches do projeto.

* **Branch master** - Esta será a branch que contém o código em nível de produção, será o código mais consolidado existente na aplicação. Todo o código novo produzido eventualmente é juntado com a branch master, em algum momento do desenvolvimento;

* **Branch develop** - Develop é a branch que logo após releases deverá ser identica à master, porém, quando as features são terminadas, elas são juntadas nesta branch, testadas e somente depois as atualizações da develop passam pelo processo de juntar as novas atualizações com a branch master;

* **Branches feature** - Essas são as branches na qual são desenvolvidos novos recursos ao projeto, elas serão criadas com o nome começando **feature**/ (exemplo: feature/new-layout) e a partir da branch develop, e, ao final, são juntadas com a branch develop;

* **Branches hotfix** - São branches no qual são realizadas correções de bugs críticos encontrados em ambiente de produção, e que por isso são criadas a partir da branch master, e são juntadas diretamente com a branch master e com a branch develop. Por convenção, essas branches tem o nome começando com **hotfix**/ e terminando com o próximo sub-número de versão (exemplo: hotfix/2.31.1);

* **Branches release** -  São branches com um nível de confiança maior do que a branch develop, e que se encontram em nível de preparação para ser juntada com a branch master e com a branch develop, nessas branches, bugs encontrados durante os testes das features que vão para produção podem ser corrigidos mais tranquilamente, antes de irem efetivamente para produção. Por convenção, essas branches tem o nome começando com **release**/ e terminando com o número da próxima versão do software, exemplo (release/2.32.0);

* **Branches documentation** - Essas são as branches na qual são desenvolvidos os documentos do projeto, elas serão criadas com o nome começando **documentation**/ (exemplo: documentation/documento-visao), elas são criadas a partir da branch develop e, ao final, é feito um pull-request para a branch develop.

Para ir para a master, só é possível via requisição aqui na interface do github. E a branch tem q estar "rebased", ou seja, sem conflitos, com os commits que estão na master (e os commits que entraram na master) e o acréscimo dos commits que foram feitos efetivamente pela sua branch.

## Comandos básicos a serem seguidos

A branch master devemos sempre mantê-la atualizada, primeiro atualizando quais branches foram criadas ou deletadas no remoto, e depois dando pull na master:

    git fetch -p --all

A opção -p, ou --prune serve pra tbm deletar localmente as branchs q foram deletadas no remoto. --all serve para olhar para outros remotes (github, gitlab se tiver)

    git pull origin master

Isso atualiza a master, e por padrão não deve haver conflito.

Origin é o remoto padrão, o primeiro cadastrado. é a url do repositório.

Para ter certeza de que estamos na master:

    git checkout master

E a partir da master criamos a dev:

    git checkout -b develop # (nosso repo ja tem isso... nao rode "-b" com branches ja existentes)

A partir da develop diversos developers irão criar novas funcionalidades. Como exemplo podemos criar uma nova branch para desenvolver:

    git checkout -b feature/nova-func

Nessa nova branch iremos fazer diversos commits, de preferencia um commit a cada ponto importante, para termos pra onde voltar se algo der errado.

Ao finalizar o desenvolvimento, damos push nessa nossa branch.

    git add -u
    git commit -s
    # escreva mensagem
    git push origin feature/nova-func

Ao final de toda a funcionalidade temos que mandar o que fizemos para a branch develop, para de la mandar pra master via merge request.

Mas outras pessoas provavelmente ja mandaram modificações para a develop, de suas respectivas branchs. Isso pode gerar conflitos, commits de merge, entre outras coisas indesejadas.

Uma boa pratica é, ir para develop:

    git checkout develop

Fazer um pull, mas usando o --rebase, para evitar commits de merge. (uma alternativa é apagar a branch de develop local, dar um fetch, e dar um checkout pra ela)

    git pull origin develop --rebase

ou

    git branch -D develop # estando em outra branch qualquer
    git fetch -p
    git checkout develop

Isso atualiza a branch develop.

É interessante olhar os commits que estão acrescentados à develop por outras pessoas:

    git log

Agora de volta em nossa branch:

    git checkout feature/nova-func

Olhamos nossos commits e contamos quantos foram os que fizemos:

    git log

Se houver conflito basta dar

    git status

Corrigir o conflito no arquivo. Dar git add no mesmo, e entao

    git rebase --continue

Se nao houver conflito o rebase local ja está feito.

Para subir isso pro remoto é necessário usar a flag -f pois vamos fazer uma alteração na branch que não é somente acrescentar um commit a frente de tudo. Essas alterações demandam a flag force.

    git push origin feature/nova-fun -f

Mas ainda nao podemos mandar nada pra develop, por conta dos commits de outras pessoas que já entraram la.

Para solucionar isso fazemos um rebase com a develop:

    git rebase develop

Os commits que estão diferentes na branch develop, são aplicados à branch feature/nova-func.

Se houver conflito, temos que resolver da mesma maneira:

    git status

Editar os arquivos com conflito, dar git add, e entao git rebase --continue

Assim que a branch feature/nova-func estiver "rebased" podemos, ou fazer um merge request para a develop, ou mergir direto na develop, ja que a deve não precisa de tanta revisão. Isso vai depender da certeza de que as modificações estão ok.

Para mergir direto, vá para a branch develop, e fazer um

    git merge feature/nova-func # ou rebase
    git push origin develop # de maneira geral nao precia de -f, ja q a develop não foi ""rebased""

Já que os rebases foram feitos, não haverá conflito, por padrão.


Para efetuar um merge request, basta ir na interface do github e apertar o botão, e mandar comparar as branchs (develop, e feature/nova-func). E assinar um revisor para aceitar ou não o merge request.

Para mandar da develop para a master da org oficial só é possível via merge request, com branches rebased e sem conflitos. Nunca a pessoa que trabalhou na branch pode ser o próprio revisor. Deve-se ter cuidado ao aceitar merge requests na master, pois por padrão ela é uma brach protegida e que não pode sofrer nenhum rebase.

## Política de commits

Para que ocorra uma padronização, nossos commits serão em inglês, com mensagens curtas e que possuam significados relevantes sobre o conteúdo do commit, estas mensagens deverão possuir verbos conjulgados no tempo passado ou participio e serem feitos apenas quando os incremetos forem significativos, devem ser evitado commits alterando nome de variáveis, excluindo e adicionando linhas em branco.

Exemplo de commits

    Creating code of feature X.

Se estiver trabalhando em conjunto especifique os participantes no commit.

    git commit -s

Irá abrir o seu editor de texto e nele deverá ser acrescentado o(s) co-authored da seguindo o exemplo:

    Signed-off-by: Vinicius Rodrigues <vinifladf@gmail.com>
    Co-authored-by: João Victor <joao15victor08@gmail.com>

## Referências Bibliográficas

> * HADLER, Mikael. Utilizando o fluxo Git Flow. Disponível em: <https://medium.com/trainingcenter/utilizando-o-fluxo-git-flow-e63d5e0d5e04>. Acesso em: 26 ago. 2018.

> * MOTA, Fernando Jorge. Git Flow: Uma forma legal de organizar repositórios git. Disponível em: <https://fjorgemota.com/git-flow-uma-forma-legal-de-organizar-repositorios-git/>. Acesso em: 26 ago. 2018.
