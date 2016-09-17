import Ember from 'ember';

export default Ember.Controller.extend({
  session: Ember.inject.service('session'),
  numberData: {
    labels: ["Dec", "Jan", "Feb", "Mar", "Apr", "May", "June"],
    datasets: [
      {
        label: "GifGun Active Users",
        fillColor: "rgba(220,220,220, 0.5)",
        strokeColor: "rgba(220,220,220, 0.8)",
        highlightFill: "rgba(220,220,220, 0.75)",
        highlightStroke: "rgba(220,220,220, 0.1)",
        data: [150,160, 190, 170, 90, 120, 140]
      }
    ]
  },

});
