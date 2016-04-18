import DS from 'ember-data';
import DRFAdapter from './drf';
import DataAdapterMixin from 'ember-simple-auth/mixins/data-adapter-mixin';

export default DRFAdapter.extend({
  addTrailingSlashes: false
});

export default DS.RESTAdapter.extend({
  namespace: 'api',
  authorizer: 'authorizer:application',

  buildURL: function(type, id, record) {
    //call the default buildURL and then append a slash
    return this._super(type, id, record) + '/';
  }
});
