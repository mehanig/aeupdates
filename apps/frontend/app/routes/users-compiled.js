import Ember from 'ember';

export default Ember.Route.extend({
  model() {
    return this.store.findAll('user');
  }
});

//# sourceMappingURL=users-compiled.js.map