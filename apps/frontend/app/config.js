import 'ember';
;
import 'ember-data';
;
DS.RESTAdapter.reopen({coalesceFindRequests: true});

require.config({
  baseUrl: '/static',
  urlArgs: 'v=__BUILD_TIMESTAMP__',
  waitSeconds: 20,
  packages: [
    {
      name: 'app',
      location: 'js/app'
    },
    {
      name: 'moment-locales',
      location: 'components/moment/locale'
    },
    {
      name: 'plugins',
      location: 'stepic_plugins'
    }
  ],
  paths: {
    d3: 'components/d3/d3.min',
    'd3-box': 'components/d3-box/box.min',
    'cal-heatmap': 'components/cal-heatmap/cal-heatmap.min',
    mathjax: 'https://cdn.mathjax.org/mathjax/2.6-latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'
  },
  shim: {'d3-box': ['d3']}
});
