import Ember from 'ember';
import ApplicationRouteMixin from 'ember-simple-auth/mixins/application-route-mixin';
var App = window.App = Ember.Application.extend();

const { inject: { service }, RSVP } = Ember;
export default Ember.Route.extend(ApplicationRouteMixin, {
  beforeModel() {
    return this._loadCurrentUser();
  },

  sessionAuthenticated() {
    this._super(...arguments);
    this._loadCurrentUser().catch(() => this.get('session').invalidate());
  },

  _loadCurrentUser() {
    return new RSVP.Promise((resolve, reject) => {
      var accountId;
      const Token =  this.get('session.data.authenticated.token');
      if (Token) {
        const tokenObj = JSON.parse(atob(Token.split('.')[1]));
        accountId = tokenObj.user_id;
      }
      if (!Ember.isEmpty(accountId)) {
        return this.get('store').findRecord('user', accountId).then((account) => {
          this.set('user', account);
          resolve();
        }, reject);
      } else {
        resolve();
      }
    });
  }
});
