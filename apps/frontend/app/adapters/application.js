import DS from 'ember-data';
import Ember from 'ember';
import DRFAdapter from './drf';
import DataAdapterMixin from 'ember-simple-auth/mixins/data-adapter-mixin';
import ENV from 'frontend/config/environment';

//$.ajaxSetup({
//  xhrFields: {
//    withCredentials: true
//  }
//});

export default DRFAdapter.extend({
  addTrailingSlashes: false
});


//export default DS.RESTAdapter.extend({
export default DS.JSONAPIAdapter.extend(DataAdapterMixin,{
  namespace: 'api',
  host: ENV.APP.API_HOST ,
  // authorizer: 'authorizer:application',
  authorizer: 'authorizer:token',
  buildURL: function(type, id, record) {
    //call the default buildURL and then append a slash
    return this._super(type, id, record) + '/';
  }
//  ajax: function(url, method, hash) {
//    hash = hash || {};
//    hash.xhrFields = {withCredentials: true};
//    return this._super(url, method, hash);
//  }
});



// export default DS.JSONAPIAdapter.extend({
//   host: ENV.host,
//   namespace: 'api'
// });
