/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

const React = require('react');

class Footer extends React.Component {
  docUrl(doc, language) {
    const baseUrl = this.props.config.baseUrl;
    return `${baseUrl}docs/${language ? `${language}/` : ''}${doc}`;
  }

  pageUrl(doc, language) {
    const baseUrl = this.props.config.baseUrl;
    return baseUrl + (language ? `${language}/` : '') + doc;
  }

  render() {
    return (
      <footer className="nav-footer" id="footer">
        <section className="sitemap">
          <div>
            <h5>Universidade de Brasília</h5>
            <a href="https://github.com/fga-eps-mds/2018.2-ComexStat">
              Backend
            </a>
            <a href="https://github.com/fga-eps-mds/2018.2-ComexStat-Frontend">
              Frontend
            </a>
            <a href="https://fga-eps-mds.github.io/2018.2-ComexStat/docs/contributing">
              Contribuindo
            </a>
          </div>
          <div>
            <h5>Ministério da Indústria - MDIC</h5>
            <a href="http://comexstat.mdic.gov.br/pt/home">
              Sistema Antigo
            </a>
            <a
              href="http://www.mdic.gov.br/index.php/comercio-exterior/estatisticas-de-comercio-exterior/base-de-dados-do-comercio-exterior-brasileiro-arquivos-para-download"
              target="_blank"
              rel="noreferrer noopener">
              Base de Dados
            </a>
            <a
              href="http://www.mdic.gov.br/"
              target="_blank"
              rel="noreferrer noopener">
              Site Oficial
            </a>
          </div>
          <div>
            <h5>Outros</h5>
            <a href={`${this.props.config.baseUrl}blog`}>Últimas Sprints</a>
            <a href="https://github.com/">GitHub</a>
            <a
              className="github-button"
              href={this.props.config.repoUrl}
              data-icon="octicon-star"
              data-count-href="/facebook/docusaurus/stargazers"
              data-show-count="true"
              data-count-aria-label="# stargazers on GitHub"
              aria-label="Star this project on GitHub">
              Star
            </a>
          </div>
        </section>

        <a
          href={this.props.config.baseUrl}
          rel="noreferrer noopener"
          className="fbOpenSource">
          <img
            src={this.props.config.baseUrl + this.props.config.footerIcon}
            alt="Facebook Open Source"
            id="footer_logo"
          />
        </a>
        <section className="copyright">{this.props.config.copyright}</section>
      </footer>
    );
  }
}

module.exports = Footer;
