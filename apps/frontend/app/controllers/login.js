import Ember from 'ember';
 
export default Ember.Controller.extend({
  session: Ember.inject.service('session'),
  queryParams: ['feedback'],
  feedback: null,

  feedbackHumanable: Ember.computed('feedback', function () {
    if (this.get('feedback') === 'success') {
      return  "Success! Now login with your user!";
    }
  }),

  actions: {
    authenticate() {
      let credentials = this.getProperties('identification', 'password');
      this.get('session').authenticate('authenticator:jwt', credentials).catch((reason) => {
        if (reason.non_field_errors) {
          this.set('error', reason.non_field_errors);
        } else {
          this.set('error', JSON.stringify(reason));
        }
      }); 
    }
  }
});
