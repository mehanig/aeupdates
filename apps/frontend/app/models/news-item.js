import DS from 'ember-data';

export default DS.Model.extend({
  ver: DS.attr('string'),
  content: DS.attr('string')
});
