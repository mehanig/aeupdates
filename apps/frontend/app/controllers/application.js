import Ember from 'ember';

export default Ember.Controller.extend({
  session: Ember.inject.service('session'),
  //user: Ember.store.get('user'),
  needs: ['session'],
  CurrentUser: null,
  isLoggedIn: Ember.computed.alias('controllers.session.isAuthenticated'),
  init: function(){
    let session = this.get('session');
    this.set('CurrentUser', session);
    if (session.isAuthenticated) {
      this.set('CurrentUser', 'Authenticated');
        alert(this.get('isLoggedIn'));
    //  return this._populateCurrentUser();
    } else {
      this.set('CurrentUser', 'NON');
       // this.transitionTo('about');
    }
  },

  actions: {
    logout(){
    alert(this.get('session').isAuthenticated);
      this.get('session').invalidate();
    }
  }
});
