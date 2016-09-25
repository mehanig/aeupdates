import Ember from 'ember';


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

 
export default Ember.Controller.extend({
  session: Ember.inject.service('session'),
  is_subscribed: false,
  is_error: false,
  actions: {
    subscribeToNews() {
      let credentials = this.getProperties('email');
      Ember.$.ajax({
        beforeSend: cookie_csrf_updater,
        url: 'api/subscribe/',
        type: 'POST',
        data: JSON.stringify({
          email: credentials['email']
        }),
        contentType: 'application/json;charset=utf-8',
        dataType: 'json',
        error: () => {
          this.set('is_error', true);
        },
      }).then((resp) => {
        this.set('is_subscribed', true);
      });
    }
   }
});
