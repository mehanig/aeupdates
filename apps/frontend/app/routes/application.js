import Ember from 'ember';
import ApplicationRouteMixin from 'ember-simple-auth/mixins/application-route-mixin';
var App = window.App = Ember.Application.extend();

const { service } = Ember.inject;

export default Ember.Route.extend(ApplicationRouteMixin, {
   afterModel() {
    if (this.session.isAuthenticated) {
      return this._populateCurrentUser();
    } else {
        this.transitionTo('about');
    }
  },

  sessionAuthenticated() {
    this._super(...arguments);
    this._loadCurrentUser().catch(() => this.get('session').invalidate());
  },

  _loadCurrentUser() {
    var currUser = this.get('sessionAccount').loadCurrentUser();
    alert(this.get('session.isAuthenticated'));
    console.log( Ember.inspect(currUser.authenticated) );
    return currUser
    },
    

  actions: {
    sessionAuthenticationSucceeded() {
      this._populateCurrentUser().then(user => this.transitionTo('manage'));
    }
  },

  _populateCurrentUser() {
    const { user_id, user_type } = this.get('session.secure');
    this.store.findAll('aeupdates');
    return this.store.find(user_type, user_id)
      .then(user => this.get('currentUser').set('content', user) && user);
  }
});
