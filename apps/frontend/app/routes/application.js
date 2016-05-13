import Ember from 'ember';
import ApplicationRouteMixin from 'ember-simple-auth/mixins/application-route-mixin';

export default Ember.Route.extend(ApplicationRouteMixin, {
  afterModel() {
    if (this.get('session.isAuthenticated')) {
      return this._populateCurrentUser();
    } else {
        this.transitionTo('about');
    }

  },

  actions: {
    sessionAuthenticationSucceeded() {
      this._populateCurrentUser().then(user => this.transitionTo('dashboard'));
    }
  },

  _populateCurrentUser() {
    console.log(Ember.inspect( this.get('session.data.authenticated')));
    //const { user_id, user_type } = this.get('session.data.authenticated.token');
    return this.store.findAll('aeupdates')
      .then(user => this.get('currentUser').set('content', user) && user);
  }
});
