/*jshint node:true*/
/* global require, module */
var EmberApp = require('ember-cli/lib/broccoli/ember-app');

module.exports = function(defaults) {
  // var EmberApp = require('ember-cli/lib/broccoli/ember-app');
  var app = new EmberApp(defaults, {
    // Add options here
    fingerprint: {
        enabled: false
    }
  });

  // Use `app.import` to add additional libraries to the generated
  // output files.
  //
  // If you need to use different assets in different
  // environments, specify an object as the first parameter. That
  // object's keys should be the environment name and the values
  // should be the asset to use in that environment.
  //
  // If the library that you are including contains AMD or ES6
  // modules that you would like to import into your application
  // please specify an object with the list of modules as keys
  // along with the exports of each module as its value.
  //

  //Add CSS to build
  // app.import('bower_components/jquery/dist/jquery.min.js');
  app.import('bower_components/bootstrap/dist/js/bootstrap.min.js');
  app.import('bower_components/bootstrap/dist/css/bootstrap.css');
  app.import('bower_components/fastclick/lib/fastclick.js');
  app.import('bower_components/pace/pace.js');
  app.import('bower_components/pace/themes/yellow/pace-theme-corner-indicator.css');
  app.import('bower_components/aeupdates_css_js/nifty.min.js');
  app.import('bower_components/aeupdates_css_js/nifty.min.css');
  app.import('bower_components/aeupdates_css_js/theme-yellow.min.css');
  return app.toTree();
};
