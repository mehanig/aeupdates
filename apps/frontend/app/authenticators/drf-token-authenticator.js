import Ember from 'ember';
import Base from 'ember-simple-auth/authenticators/base';

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
  xhr.setRequestHeader("X-CSRFToken", cookVal)
};

export default Base.extend({
  restore(data) {
    return new Ember.RSVP.Promise((resolve, reject) => {
      if (!Ember.isEmpty(data.token)) {
        resolve(data);
      } else {
        reject();
      }
    });
  },

  authenticate(username, password) {
    return new Ember.RSVP.Promise((resolve, reject) => {
      Ember.$.ajax({
        beforeSend: cookie_csrf_updater,
        url: '/token/',
        type: 'POST',
        data: JSON.stringify({
          username: username,
          password: password
        }),
        contentType: 'application/json;charset=utf-8',
        dataType: 'json'
      }).then((response) => {
        Ember.run(function () {
          resolve({
            token: response.token
          });
        });
      }, (xhr, status, error) => {
        var response = xhr.responseText;
        Ember.run(function () {
          reject(response);
        });
      });
    });
  },
});
