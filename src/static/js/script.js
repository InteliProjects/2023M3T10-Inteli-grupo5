document.addEventListener("DOMContentLoaded", function () {
  document.querySelector("form").addEventListener("submit", function (e) {
      e.preventDefault();
      const formData = new FormData(this);

      // Enviar o arquivo CSV para a rota do Flask
      fetch("/", {
          method: "POST",
          body: formData,
      })
      .then((response) => {
          if (response.ok) {
              // Se o envio for bem-sucedido, ler o conteúdo CSV retornado
              return response.text();
          } else {
              throw new Error("Falha ao enviar o arquivo CSV.");
          }
      })
      .then((csvContent) => {
          // Exibir o conteúdo CSV em forma de objeto no console
          console.log("Conteúdo do CSV em forma de objeto:");
          console.log(csvContent); // Exibir o conteúdo CSV no console

          // Verificar se o CSV foi importado corretamente
          if (csvContent === "CLAYTON") {
              console.log("CLAYTON");
          }
      })
      .catch((error) => {
          console.error(error);
      });
  });
});

// Obtém o caminho da imagem do frontend ou de onde quer que seja
const caminhoDaImagem = "../backend/clusterizacao_Carteira_Cartao_Credito_clusters_3.png";

// Obtém a referência da tag <img>
const imagemGrafico = document.getElementById("imagem-grafico");

// Define o atributo src da tag <img> com o caminho da imagem variável
imagemGrafico.src = caminhoDaImagem;

const cluster = ['TARGET FUNDO DE INVESTIMENTO EM DIREITOS CREDITORIOS- MULTICREDITO', 'RED - FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS MULTISETORIAL LP','RSS FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS', 'W CAPITAL I - FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS']

document.addEventListener("DOMContentLoaded", function () {
  // Seu código existente

  const cluster = ['TARGET FUNDO DE INVESTIMENTO EM DIREITOS CREDITORIOS- MULTICREDITO', 'RED - FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS MULTISETORIAL LP', 'RSS FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS', 'W CAPITAL I - FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS'];

  const scrollbox = document.getElementById("scrollbox");

  // Adiciona elementos do array como itens da barra de rolagem
  cluster.forEach(item => {
      const clusterItem = document.createElement("div");
      clusterItem.classList.add("cluster-item");
      clusterItem.textContent = item;
      scrollbox.appendChild(clusterItem);
  });

  // Define o caminho da imagem
  const caminhoDaImagem = "../static/assets/output_plot.png";

  // Obtém a referência da tag <img>
  const imagemGrafico = document.getElementById("imagem-grafico");

  // Define o atributo src da tag <img> com o caminho da imagem variável
  imagemGrafico.src = caminhoDaImagem;
});


window.addEventListener("scroll", function() {
  var footer = document.querySelector(".footer");
  if (window.pageYOffset > 100) {
    footer.style.display = "flex"; // Mostra o footer quando a página é rolada
  } else {
    footer.style.display = "none"; // Oculta o footer quando a página é no topo
  }
});

function reloadPageAfterUpload() {
  // Aguarde um curto período de tempo antes de recarregar a página (para permitir que o formulário seja enviado)
  setTimeout(function () {
    window.location.reload();
  }, 5000); // 1000 milissegundos = 1 segundo (ajuste conforme necessário)
}
