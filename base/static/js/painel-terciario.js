google.charts.load('current', {'packages':['bar']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
var data = google.visualization.arrayToDataTable([
    ['', 'Entradas', 'Saídas'],
    ['Entradas | Saídas', 3075, 1075],
]);

var options = {
  title: 'Receitas x Despesas',
  titleTextStyle: {
    color: '#ffffff',
    backgroundColor: "transparent",
    bold: true,
    fontSize: 11,
  },
  colors: ['lime', '#d62828'],
  backgroundColor: 'transparent',
  chartArea: {
      width: '100%',
      height: '100%',
      backgroundColor: 'transparent',
  },
  legend: {position: 'none'},
};

var chart = new google.charts.Bar(document.getElementById('chart_div'));
chart.draw(data, google.charts.Bar.convertOptions(options));
}