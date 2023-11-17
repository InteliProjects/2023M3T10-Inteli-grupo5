from flask import (
    Flask,
    render_template,
    request,
    Response,
    jsonify,
    send_from_directory,
)
from modelo import main
from modelo import cluster_and_save_plot
import asyncio

app = Flask(__name__, template_folder="../frontend/", static_folder="../static")

cluster1 = []
cluster2 = []
cluster3 = []


@app.route("/", methods=["GET", "POST"])
async def upload_csv():
    if request.method == "POST":
        csv_file = request.files["csv_file"]
        if not csv_file:
            return "Não é um arquivo válido"

        # Lê o arquivo CSV e armazena seu conteúdo em uma variável
        csv_content = csv_file.read().decode("utf-8")

        # Chame a função main() para obter os clusters
        clusters = await main()

        global cluster1, cluster2, cluster3

        cluster1 = clusters[0]
        cluster2 = clusters[1]
        cluster3 = clusters[2]

        # Imprima os clusters no console
        for idx, cluster in enumerate(clusters):
            print(f"Cluster {idx + 1}: {cluster}")

        # Retorna a imagem diretamente no HTML
        image_path = "../static/assets/output_plot.png"
        # image_path = await cluster_and_save_plot(
        #     df_informe_mensal,
        #     carteira_selecionada,
        #     num_clusters,
        #     output_filename,
        # )
        return render_template("index.html", image_path=image_path)

    return render_template("index.html")


@app.route("/modelo", methods=["GET"])
def modelo():
    return render_template(
        "index.html", cluster1=cluster1, cluster2=cluster2, cluster3=cluster3
    )


if __name__ == "__main__":
    app.run(debug=True)
