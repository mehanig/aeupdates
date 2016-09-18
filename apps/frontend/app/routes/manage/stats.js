import Ember from 'ember';

function ajax (url, options, headerValue) {
  return new Ember.RSVP.Promise(function (resolve, reject) {
    options = options || {};
    options.url = url;
    options.headers = {
      'Authorization': headerValue
    };

    options.success = function (data) {
      Ember.run(null, resolve, data);
    };

    // TODO: Make it generic!
    options.error = function (jqxhr, status, respdata) {
      if (status === 'error' && respdata === 'Unauthorized') {
        window.location = '/login?feedback=needlogin';
      }
      Ember.run(null, reject, arguments);
    };
    Ember.$.ajax(options);
  });
}

export default Ember.Route.extend({

  session: Ember.inject.service('session'),

  model() {
    let bearer = null;
    this.get('session').authorize('authorizer:token', (headerName, headerValue) => {
      bearer = headerValue;
    });
    return ajax('/api/stats', {}, bearer);
  },
  afterModel(model, transition) {
    this.controllerFor('manage.stats').set('data', model.data);
  }
});
