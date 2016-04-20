import DS from 'ember-data';

export default DS.Model.extend({
  url: DS.attr('string'),
  product: DS.attr('string'),
  version: DS.attr('string'),
  news: DS.hasMany('news-item')
});
