import Ember from 'ember';

export default Ember.Route.extend({
  model() {
    return this.store.findAll('product');
  },

  afterModel: function (products, tr) {
    var l = products.get('length');
    for(var i=0; i< l; i++){
      products.objectAt(i).get('news');
    }
  }
});
