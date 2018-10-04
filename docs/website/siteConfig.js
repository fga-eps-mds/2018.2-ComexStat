/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

// See https://docusaurus.io/docs/site-config for all the possible
// site configuration options.

// List of projects/orgs using your project for the users page.
const users = [
  {
    caption: 'User1',
    // You will need to prepend the image path with your baseUrl
    // if it is not '/', like: '/test-site/img/docusaurus.svg'.
    image: '/img/docusaurus.sv',
    infoLink: 'https://www.facebook.com',
    pinned: true,
  },
];

const siteConfig = {
  title: 'Comex Stat', // Title for your website.
  tagline: 'Documentação do Comex Stat',
  url: 'https://fga-eps-mds.github.io/', // Your website URL
  baseUrl: '/2018.2-ComexStat/', // Base URL for your project */
  // For github.io type URLs, you would set the url and baseUrl like:
  //   url: 'https://facebook.github.io',
  //   baseUrl: '/test-site/',

  // Used for publishing and more
  projectName: '2018.2-ComexStat',
  organizationName: 'fga-eps-mds',
  // For top-level user or org sites, the organization is still the same.
  // e.g., for the https://JoelMarcey.github.io site, it would be set like...
  //   organizationName: 'JoelMarcey'

  // For no header links in the top nav bar -> headerLinks: [],
  headerLinks: [
    {doc: 'contributing', label: 'Docs'},
  //  {doc: 'contributing', label: 'API'},
//    {page: 'help', label: 'Help'},
    {blog: true, label: 'Sprints'},
  ],

  // If you have users set above, you add it here:
  users,

  /* path to images for header/footer */


  Rogerio: 'img/rogerio.jpg',
  Marcos: 'img/marcos.jpg',
  Joao: 'img/joao.jpg',
  Andre: 'img/andre.jpg',
  Kaique: 'img/kaique.jpeg',
  Matheus: 'img/matheus.jpg',
  Vinicius: 'img/vinicius.jpg',
  Sannya: 'img/sannya.jpg',

  RogerioGithub: 'https://github.com/rogerioo',
  MarcosGithub: 'https://github.com/marcosnbj',
  JoaoGithub: 'https://github.com/joao15victor08',
  AndreGithub: 'https://github.com/andrelucasf',
  KaiqueGithub: 'https://github.com/riquekaique',
  MatheusGithub: 'https://github.com/joranhezon',
  ViniciusGithub: 'https://github.com/vinicinolivera',
  SannyaGithub: 'https://github.com/sannyaarvelos',

  members: [
    "@rogerioo", "@marcosnbj", "@joao15victor08", "@andrelucasf",
    "@riquekaique", "@johanhezon", "@vinicinolivera", "@sannyaarvelos"
  ],

  /* path to images for header/footer */
  headerIcon: 'img/logo_header.png',
  footerIcon: 'img/logo_header.png',
  favicon: 'img/logo_header.png',

  /* Colors for website */
  colors: {
    primaryColor: '#17c13d',
    secondaryColor: '#17c13d',
  },

  /* Custom fonts for website */
  /*
  fonts: {
    myFont: [
      "Times New Roman",
      "Serif"
    ],
    myOtherFont: [
      "-apple-system",
      "system-ui"
    ]
  },
  */

  // This copyright info is used in /core/Footer.js and blog RSS/Atom feeds.
  copyright: `Copyright © ${new Date().getFullYear()} EPS e MDS UnB FGA`,

  highlight: {
    // Highlight.js theme to use for syntax highlighting in code blocks.
    theme: 'default',
  },

  // Add custom scripts here that would be placed in <script> tags.
  scripts: ['https://buttons.github.io/buttons.js'],

  // On page navigation for the current documentation page.
  onPageNav: 'separate',
  // No .html extensions for paths.
  cleanUrl: true,

  // Open Graph and Twitter card images.
  ogImage: 'img/docusaurus.png',
  twitterImage: 'img/docusaurus.png',

  // You may provide arbitrary config keys to be used as needed by your
  // template. For example, if you need your repo's URL...
  //   repoUrl: 'https://github.com/facebook/test-site',
};

module.exports = siteConfig;
