function gera_cor(qtd = 1) {
  var bg_color = [];
  var border_color = [];
  for (let i = 0; i < qtd; i++) {
    let r = Math.random() * 255;
    let g = Math.random() * 255;
    let b = Math.random() * 255;
    bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`);
    border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`);
  }

  return [bg_color, border_color];
}

function renderiza_artigos_por_orientador(url) {
  fetch(url, {
    method: "get",
  })
    .then(function (result) {
      return result.json();
    })
    .then(function (data) {
      const ctx = document
        .getElementById("artigos_por_orientador")
        .getContext("2d");
      var cores_artigos_por_orientador = gera_cor((qtd = 12));
      const   myChart = new Chart(ctx, {
        type: "bar",
        data: {
          labels: data.labels,
          datasets: [
            {
              label: 'Quantidade de Artigos',
              data: data.data,
              backgroundColor: cores_artigos_por_orientador[0],
              borderColor: cores_artigos_por_orientador[1],
              borderWidth: 1,
            },
          ],
        },
        options: {
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      });
    });
}


function gera_grafico_qt_artigos_curso(url) {
  fetch(url, {
    method: "get",
  })
    .then(function (result) {
      return result.json();
    })
    .then(function (data) {
      const ctx = document
        .getElementById("quantidade_artigos_curso")
        .getContext("2d");
      var cores_quantidade_artigos_curso = gera_cor((qtd = 12));
      const   myChart = new Chart(ctx, {
        type: "bar",
        data: {
          labels: data.num_artigos,
          datasets: [
            {
              label: 'Quantidade de Artigos',
              data: data.data,
              backgroundColor: cores_quantidade_artigos_curso[0],
              borderColor: cores_quantidade_artigos_curso[1],
              borderWidth: 1,
            },
          ],
        },
        options: {
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      });
    });
}

