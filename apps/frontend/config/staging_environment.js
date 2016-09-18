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
  }

  if (environment === 'test') {
  }

  if (environment === 'production') {
    ENV.APP.API_HOST  = 'http://37.139.30.9:8080';
    ENV.APP.API_NAMESPACE = 'api';

}
  return ENV;
};
