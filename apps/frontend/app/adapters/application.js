import DS from 'ember-data';
import DRFAdapter from './drf';

export default DRFAdapter.extend({
  addTrailingSlashes: false
});

export default DS.RESTAdapter.extend({
  namespace: 'api'

});
