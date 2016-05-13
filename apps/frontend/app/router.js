import Ember from 'ember';
import config from './config/environment';

const Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.route('users');
  this.route('manage');
  this.route('login');
  this.route('products');
  this.route('signup');
  this.route('about');
  this.route('aeupdates');
});

export default Router;
