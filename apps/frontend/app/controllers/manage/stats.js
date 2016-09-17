import Ember from 'ember';

export default Ember.Controller.extend({
  session: Ember.inject.service('session'),

  data: false,
  days_data_CHARTOPTIONS: {
    animation: true,
    responsive : false,
    tooltipTemplate: "<%= value %>",
    tooltipFillColor: "rgba(0,0,0,0)",
    tooltipFontColor: "#444",
    tooltipEvents: [],
    tooltipCaretSize: 0,
    onAnimationComplete: function()
    {
        console.log(this);
        this.showTooltip(this.datasets[0].points, true);
    }
  },

  days_data: Ember.computed('data', {
    get: function() {
    if (this.get('data')) {
      return {
              labels: this.get('data.aggregated_by_day').map((item) => {return item[0];}),
              datasets: [
                          {
                            label: "GifGun Active Users",
                            fillColor: "rgba(220,220,220, 0.5)",
                            strokeColor: "rgba(220,220,220, 0.8)",
                            highlightFill: "rgba(220,220,220, 0.75)",
                            highlightStroke: "rgba(220,220,220, 0.1)",
                            data: this.get('data.aggregated_by_day').map((item) => {return parseInt(item[1]);})
                          }
                       ]
             };
    }}
  })
});
