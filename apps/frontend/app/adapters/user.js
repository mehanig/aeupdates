import DS from 'ember-data';
import DataAdapterMixin from 'ember-simple-auth/mixins/data-adapter-mixin';
import ENV from 'frontend/config/environment';

//TODO: MAKE MODULAR!! REFACTOR THIS! (HOW?)
var cookie_csrf_updater = function (xhr) {
  var cookie = null;
  var cookVal = null;
  var cookies = document.cookie.split(';');
  for (var i = 0; i < cookies.length; i++) {
    cookie = jQuery.trim(cookies[i]);
    if (cookie.substring(0, "csrftoken".length + 1) == "csrftoken=") {
      cookVal = decodeURIComponent(cookie.substring("csrftoken".length + 1));
      break;
    }
  }
  xhr.setRequestHeader("X-CSRFToken", cookVal);
};

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
          cookie_csrf_updater(xhr);
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
