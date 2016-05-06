import Ember from 'ember';
 
export default Ember.Controller.extend({
  session: Ember.inject.service('session'),
 
  actions: {
    register() {
      const { username, password1, password2 } = this.getProperties('username', 'password1', 'password2');
        if (password1 !== password2) {
            this.set('error', "Passwords doesn't match.");
            return -1;
        }
        this.store.createRecord('user',{
            username: username,
            password: password1,
            email: username
        }).save();
    }
  }
});
