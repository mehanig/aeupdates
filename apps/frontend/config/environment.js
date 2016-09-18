/* jshint node: true */

module.exports = function(environment) {
  var ENV = {
    modulePrefix: 'frontend',
    environment: environment,
    baseURL: '/',
    locationType: 'auto',
    EmberENV: {
      FEATURES: {
        // Here you can enable experimental features on an ember canary build
        // e.g. 'with-controller': true
      }
    },

    APP: {
      // Here you can pass flags/options to your application instance
      // when it is created
    }
  };

  ENV['ember-simple-auth'] = {
    authenticationRoute: 'login',
    routeAfterAuthentication: 'manage',
    routeIfAlreadyAuthenticated: 'manage',
    authorizer: 'authorizer:token'
    //crossOriginWhitelist: ['*']
  };

  ENV['ember-simple-auth-token'] = {
   serverTokenEndpoint: '/token/',
   serverTokenRefreshEndpoint: '/token-refresh/',
   refreshAccessTokens: true,
   identificationField: 'username',
   timeFactor: 1000,
   refreshLeeway: 3000,
   authorizationPrefix: 'Bearer ',
   authorizationHeaderName: 'Authorization',
   headers: {},
  };

  if (environment === 'development') {
    ENV.APP.API_HOST = 'http://localhost:8000';
    ENV.APP.API_NAMESPACE = 'api';
    // ENV.APP.LOG_RESOLVER = true;
    // ENV.APP.LOG_ACTIVE_GENERATION = true;
    // ENV.APP.LOG_TRANSITIONS = true;
    // ENV.APP.LOG_TRANSITIONS_INTERNAL = true;
    // ENV.APP.LOG_VIEW_LOOKUPS = true;
  }

  if (environment === 'test') {
    // Testem prefers this...

    // ENV.baseURL = '/';
    // ENV.locationType = 'none';
    ENV.APP.API_HOST = 'http://37.139.30.9:8080';
    ENV.APP.API_NAMESPACE = 'api';
    //
    // keep test console output quieter
    // ENV.APP.LOG_ACTIVE_GENERATION = false;
    // ENV.APP.LOG_VIEW_LOOKUPS = false;
    //
    // ENV.APP.rootElement = '#ember-testing';
  }

  if (environment === 'production') {
    ENV.APP.API_HOST  = 'https://aeupdates.com';
    ENV.APP.API_NAMESPACE = 'api';

    // UNCOMMENT FOR LOCAL DEVELOPMENT IF PRODUCTION BUILD NEEDED
    // ENV.APP.API_HOST = 'http://37.139.30.9:8080';
}
  return ENV;
};
