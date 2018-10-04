/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

const React = require('react');

const CompLibrary = require('../../core/CompLibrary.js');

const MarkdownBlock = CompLibrary.MarkdownBlock; /* Used to read markdown */
const Container = CompLibrary.Container;
const GridBlock = CompLibrary.GridBlock;

const siteConfig = require(`${process.cwd()}/siteConfig.js`);

function imgUrl(img) {
  return `${siteConfig.baseUrl}img/${img}`;
}

function docUrl(doc, language) {
  return `${siteConfig.baseUrl}docs/${language ? `${language}/` : ''}${doc}`;
}

function pageUrl(page, language) {
  return siteConfig.baseUrl + (language ? `${language}/` : '') + page;
}

class Button extends React.Component {
  render() {
    return (
      <div className="pluginWrapper buttonWrapper">
        <a className="button" href={this.props.href} target={this.props.target}>
          {this.props.children}
        </a>
      </div>
    );
  }
}

Button.defaultProps = {
  target: '_self',
};

const SplashContainer = props => (
  <div className="homeContainer">
    <div className="homeSplashFade">
      <div className="wrapper homeWrapper">{props.children}</div>
    </div>
  </div>
);

const Logo = props => (
  <div className="projectLogo">
    <img src={props.img_src} alt="Project Logo" />
  </div>
);

const Features = () => (
  <Block layout="fourColumn">
    {[
      {
        content: '</p align="justify"> O ComexStat, vem com o objetivo de facilitar o acesso aos dados relacionados ao comércio exterior de bens, e posteriormente serviços no Brasil. Proporcionando aos usuários a possibilidade de trabalhar com as informações desejadas de forma fácil e intuitiva. Aqui está registrada toda a documentação para que o usuário possa ter um bom entendimento do <i>software</i> e de como contribuir com o mesmo.</p>',
        image: imgUrl('sobre.jpg'),
        imageAlign: 'top',
        title: 'Sobre',
      },
      {
        content: '</p align="justify">O <i>software</i> é divido em dois repositórios, um dedicado ao <a href="https://github.com/fga-eps-mds/2018.2-ComexStat">Backend</a>, contendo a API, e o outro dedicado ao <a href="https://github.com/fga-eps-mds/2018.2-ComexStat-FrontEnd">Frontend</a>, contendo uma aplicação visual para facilitar a usabilidade do sistema.</p>',
        image: imgUrl('repositorio.jpg'),
        imageAlign: 'top',
        title: 'Repositório',
      },
    ]}
  </Block>
);

const ProjectTitle = () => (
  <h2 className="projectTitle">
    {siteConfig.title}
    <small>{siteConfig.tagline}</small>
  </h2>
);

const PromoSection = props => (
  <div className="section promoSection">
    <div className="promoRow">
      <div className="pluginRowBlock">{props.children}</div>
    </div>
  </div>
);

class HomeSplash extends React.Component {
  render() {
    const language = this.props.language || '';
    return (
      <SplashContainer>
        <Logo img_src={imgUrl('docusaurus.svg')} />
        <div className="inner">
          <ProjectTitle />
          <PromoSection>
            <Button href="#try">Try It Out</Button>
            <Button href={docUrl('contributing.html', language)}>Example Link</Button>
            <Button href={docUrl('contributing.html', language)}>Example Link 2</Button>
          </PromoSection>
        </div>
      </SplashContainer>
    );
  }
}

const Block = props => (
  <Container
    padding={['bottom', 'top']}
    id={props.id}
    background={props.background}>
    <GridBlock align="center" contents={props.children} layout={props.layout} />
  </Container>
);

const Header = () => {
  return (
    <div className="header">
      <div className="header__text-box">
        <h1 className="heading-primary">
          <img src='img/logo_grande.png' alt="Logo"  id="img_logo" />
        </h1>
      </div>
    </div>
  )
}

const Cards = (props) => {
  let photo, githubLink = null
  switch (props.name) {
    case "@rogerioo":
      photo = siteConfig.Rogerio
      githubLink = siteConfig.RogerioGithub
      break
    case "@marcosnbj":
      photo = siteConfig.Marcos
      githubLink = siteConfig.MarcosGithub
      break
    case "@joao15victor08":
      photo = siteConfig.Joao
      githubLink = siteConfig.JoaoGithub
      break
    case "@riquekaique":
      photo = siteConfig.Kaique
      githubLink = siteConfig.KaiqueGithub
      break
    case "@andrelucasf":
      photo = siteConfig.Andre
      githubLink = siteConfig.AndreGithub
      break
    case "@johanhezon":
      photo = siteConfig.Matheus
      githubLink = siteConfig.MatheusGithub
      break
    case "@vinicinolivera":
      photo = siteConfig.Vinicius
      githubLink = siteConfig.ViniciusGithub
      break
    case "@sannyaarvelos":
      photo = siteConfig.Sannya
      githubLink = siteConfig.SannyaGithub
      break
    default:
      break
  }

  return (
    <a href={githubLink} className="card-foto">
      <img src={photo} alt={props.name}  className="card-foto-perfil" />
      <div className="card-link">
        <p className="card-link-text">{props.name}</p>
      </div>
    </a>
  )
}

const LearnHow = () => (
  <Block background="light">
    {[
      {
        content: 'Talk about learning how to use this',
        image: imgUrl('docusaurus.svg'),
        imageAlign: 'right',
        title: 'Learn How',
      },
    ]}
  </Block>
);

const TryOut = () => (
  <Block id="try">
    {[
      {
        content: 'Talk about trying this out',
        image: imgUrl('docusaurus.svg'),
        imageAlign: 'left',
        title: 'Try it Out',
      },
    ]}
  </Block>
);

const Description = () => (
  <Block background="dark">
    {[
      {
        content: 'This is another description of how this project is useful',
        image: imgUrl('docusaurus.svg'),
        imageAlign: 'right',
        title: 'Description',
      },
    ]}
  </Block>
);

const Showcase = props => {
  if ((siteConfig.users || []).length === 0) {
    return null;
  }

  const showcase = siteConfig.users.filter(user => user.pinned).map(user => (
    <a href={user.infoLink} key={user.infoLink}>
      <img src={user.image} alt={user.caption} title={user.caption} />
    </a>
  ));

  return (
    <div className="productShowcaseSection paddingBottom">
      <h2>Who is Using This?</h2>
      <p>This project is used by all these people</p>
      <div className="logos">{showcase}</div>
      <div className="more-users">
        <a className="button" href={pageUrl('users.html', props.language)}>
          More {siteConfig.title} Users
        </a>
      </div>
    </div>
  );
};

class Index extends React.Component {
  render() {
    const language = this.props.language || '';

    return (
      <React.Fragment>
        <Header />
        <Features />
         <h1 className="heading-colaboradores">Colaboradores</h1>
        <div className="card-container">
          {siteConfig.members.map(member => <Cards key={member} name={member} />)}
        </div>
      </React.Fragment>
    );
  }
}

module.exports = Index;
