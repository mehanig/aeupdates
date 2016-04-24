import DS from 'ember-data';

// export default DS.RESTSerializer.extend({
export default DS.JSONAPISerializer.extend({
  // keyForAttribute: function(attr, method) {
  //   return Ember.String.underscore(attr).toUpperCase();
  // }
});
