import DS from 'ember-data';
import DataAdapterMixin from 'ember-simple-auth/mixins/data-adapter-mixin';
import ENV from 'frontend/config/environment';

export default DS.JSONAPIAdapter.extend(DataAdapterMixin,{

  //Overwrite request headers for one endpoint
  // https://github.com/emberjs/data/blob/v2.7.0/addon/adapters/json-api.js#L20
  ajaxOptions: function ajaxOptions(url, type, options) {
      var hash = this._super.apply(this, arguments);

      if (hash.contentType) {
        hash.contentType = 'application/json';
      }

      var beforeSend = hash.beforeSend;
      hash.beforeSend = function (xhr) {
        xhr.setRequestHeader('Accept', 'application/json');
        if (beforeSend) {
          beforeSend(xhr);
        }
      };

      return hash;
    },
  namespace: 'api',
  host: ENV.APP.API_HOST ,
  authorizer: 'authorizer:token',
  //Append Slash! BAD
  buildURL: function(type, id, record) {
    //call the default buildURL and then append a slash
    return this._super(type, id, record) + '/';
  }
});
