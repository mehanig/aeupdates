import DS from 'ember-data';
import DRFAdapter from './drf';
import DataAdapterMixin from 'ember-simple-auth/mixins/data-adapter-mixin';

export default DRFAdapter.extend({
  addTrailingSlashes: false
});


// export default DS.RESTAdapter.extend({
export default DS.JSONAPIAdapter.extend({
  namespace: 'api',
  // host: ENV.host,
  authorizer: 'authorizer:application',

  buildURL: function(type, id, record) {
    //call the default buildURL and then append a slash
    return this._super(type, id, record) + '/';
  }
});


import ENV from 'todo-ember/config/environment';

// export default DS.JSONAPIAdapter.extend({
//   host: ENV.host,
//   namespace: 'api'
// });
