import Ember from 'ember';

export default Ember.Controller.extend({
  session: Ember.inject.service('session'),

  data: false,
  aggregated_by_day_CHARTOPTIONS: {
    animation: true,
    responsive : false,
    tooltipTemplate: "<%= value %>",
    tooltipFillColor: "rgba(0,0,0,0)",
    tooltipFontColor: "#444",
    tooltipEvents: [],
    tooltipCaretSize: 0,
    bezierCurve : false,
    onAnimationComplete: function()
    {
        this.showTooltip(this.datasets[0].points, true);
    }
  },
  aggregated_by_user_CHARTOPTIONS: {
    animation: true,
    responsive : false,
    tooltipTemplate: "<%= value %>",
    tooltipFillColor: "rgba(0,0,0,0)",
    tooltipFontColor: "#444",
    tooltipEvents: [],
    tooltipCaretSize: 0,
    bezierCurve : false,
    onAnimationComplete: function()
    {
        this.showTooltip(this.datasets[0].bars, true);
    }
  },
  aggregated_unique_by_day_CHARTOPTIONS: {
    animation: true,
    responsive : false,
    tooltipTemplate: "<%= value %>",
    tooltipFillColor: "rgba(0,0,0,0)",
    tooltipFontColor: "#444",
    tooltipEvents: [],
    tooltipCaretSize: 0,
    bezierCurve : false,
    onAnimationComplete: function()
    {
        this.showTooltip(this.datasets[0].bars, true);
    }
  },

  all_data: Ember.computed('data', {
    get: function() {
      if (this.get('data')) {
        return {
          aggregated_by_day : {
            labels: this.get('data.aggregated_by_day').map((item) => {
            return item[0];
            }),
            datasets: [
              {
                label: "GifGun Active Users",
                fillColor: "rgba(220,220,220, 0.5)",
                strokeColor: "rgba(220,220,220, 0.8)",
                highlightFill: "rgba(220,220,220, 0.75)",
                highlightStroke: "rgba(220,220,220, 0.1)",
                data: this.get('data.aggregated_by_day').map((item) => {
                  return parseInt(item[1]);
                })
              }
            ]
          },
          aggregated_by_user : {
            labels: this.get('data.aggregated_by_user').map((item) => {
            return item[0];
            }),
            datasets: [
              {
                label: "GifGun Active Users",
                fillColor: "rgba(220,220,220, 0.5)",
                strokeColor: "rgba(220,220,220, 0.8)",
                highlightFill: "rgba(220,220,220, 0.75)",
                highlightStroke: "rgba(220,220,220, 0.1)",
                data: this.get('data.aggregated_by_user').map((item) => {
                  return parseInt(item[1]);
                })
              }
            ]
          },
          aggregated_unique_by_day : {
            labels: this.get('data.aggregated_unique_by_day').map((item) => {
            return item[0];
            }),
            datasets: [
              {
                label: "GifGun Active Users",
                fillColor: "rgba(220,220,220, 0.5)",
                strokeColor: "rgba(220,220,220, 0.8)",
                highlightFill: "rgba(220,220,220, 0.75)",
                highlightStroke: "rgba(220,220,220, 0.1)",
                data: this.get('data.aggregated_unique_by_day').map((item) => {
                  return parseInt(item[1]);
                })
              }
            ]
          }
        };
      }
    }
  })
});
