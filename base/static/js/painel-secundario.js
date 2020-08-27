google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
    var data = google.visualization.arrayToDataTable([
      ['Gastos', 'Gastos por categoria'],
      ['Alimentação',     11],
      ['Casa',      2],
      ['Aluguel',  2],
      ['Educação', 2],
      ['Transporte',    7]
    ]);
    
    var options = {
      title: 'Gastos por categoria',
      titleTextStyle: {
          color: '#ffffff',
          backgroundColor: "#fff",
          bold: true,
          fontSize: 11,
      },
      pieHole: 0.4,
      backgroundColor: 'transparent',
      chartArea:{left:5, top:30, width:"100%", height:"100%"},
      legend: { position: 'right', textStyle: {color: 'white', } },
      slices: {
            0: { color: '#003049' },
            1: { color: '#d62828' },
            2: { color: '#f77f00' },
            3: { color: '#fcbf49' },
            4: { color: '#eae2b7' },
          },
      pieSliceBorderColor: {
          color: '#000',
      },
    };
    var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
    chart.draw(data, options);
}