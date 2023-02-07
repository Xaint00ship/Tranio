/* globals Chart:false, feather:false */

'use strict'
const host = "127.0.0.1";
const port = "8000"

let btnDrawGraph = document.querySelector("#btn-get-number")
let btnShortUrl = document.querySelector("#btn-shorten")

btnDrawGraph.addEventListener("click", drawGraph)
btnShortUrl.addEventListener("click", shortenerUrl)


function shortenerUrl() {
  
  let url = document.querySelector("#input-url").value;

  fetch(`http://${host}:${port}/API/GetHashURL/${url}`)
              .then((response) => response.json())
              .then((data) => {
                document.querySelector("#input-short-url").innerHTML = `Shorten URL: ${document.location.host}/${data["hash"]}`
              });
}


function drawGraph() {
  let hash = String(document.querySelector("#input-hash").value).slice(-6);

  fetch(`http://${host}:${port}/API/GetClicksNumShortURL/${hash}`)
  .then((response) => response.json())
  .then((data) => {
    document.querySelector("#all-click").innerHTML = `All clicks: ${data["clicks"]}`
  })
  
  fetch(`http://${host}:${port}/API/GetClicksStat/${hash}`)
              .then((response) => response.json())
              .then((data) => {
                feather.replace({ 'aria-hidden': 'true' })

                // Graphs
                var ctx = document.getElementById('myChart')
                // eslint-disable-next-line no-unused-vars
                var myChart = new Chart(ctx, {
                  type: 'line',
                  data: {
                    labels: Object.keys(data),
                    datasets: [{
                      data: Object.values(data),
                      lineTension: 0,
                      backgroundColor: 'transparent',
                      borderColor: '#007bff',
                      borderWidth: 4,
                      pointBackgroundColor: '#007bff'
                    }]
                  },
                  options: {
                    scales: {
                      yAxes: [{
                        ticks: {
                          beginAtZero: false
                        }
                      }]
                    },
                    legend: {
                      display: false
                    }
                  }
                })
              
              });

}


