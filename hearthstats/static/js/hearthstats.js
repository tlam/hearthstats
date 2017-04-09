var app = angular.module('hearthstats-app', []);
app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

app.controller('RarityCtrl', function($scope, $http, $attrs) {
  if ($attrs.code !== '') {
    $http.get('/cards/' + $attrs.code + '/set_rarity.json').success(function(data) {

      function drawChart() {
        for (var rarity in data.rarity) {
          var stats = data.rarity[rarity];
          var total = stats['total'];
          var own = stats['own'];
          var chartData = google.visualization.arrayToDataTable([
            ['Card status', 'Number of cards'],
            ['Own', own],
            ['Missing', total - own],
          ]);

          var options = {
            title: rarity
          };

          var chart = new google.visualization.PieChart(document.getElementById(rarity.toLowerCase() + '-chart'));
          chart.draw(chartData, options);
        }
      }

      google.charts.setOnLoadCallback(drawChart);
    });
  }
});

$(document).ready(function(){
  $('a.card').on('click', function() {
    $('.modal-title').html('<span>' + $(this).attr('data-title') + '</span>');
    $('.modal-body').html('<img src="' + $(this).attr('data-content') + '" />');
  });
});
