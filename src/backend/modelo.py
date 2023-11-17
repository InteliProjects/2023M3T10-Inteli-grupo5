import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os  # Importe a biblioteca os para lidar com caminhos de arquivos
import asyncio


def ler_arquivo_csv(nome_arquivo):
    df = pd.read_csv(nome_arquivo)
    return df


# Função para calcular a taxa de inadimplência
def calcular_taxa_inadimplencia(df):
    df_cleaned = df.dropna(subset=["Patrimonio_Liquido"])
    inadimplentes = df_cleaned["Carteira_Direitos_Aquisicao_Inadimplentes"]
    patrimonio_liquido = df_cleaned["Patrimonio_Liquido"]
    taxa_inadimplencia = inadimplentes / patrimonio_liquido
    df = df.assign(taxa_inadimplencia_series=taxa_inadimplencia)
    return df


def realizar_clusterizacao(df, carteira_selecionada, num_clusters):
    fundos_validos = df[df[carteira_selecionada].notna()]
    X = fundos_validos[[carteira_selecionada]]
    kmeans = KMeans(n_clusters=num_clusters)
    fundos_validos["grupo"] = kmeans.fit_predict(X)

    objetos_clusters = []

    for cluster_num in range(num_clusters):
        cluster_df = fundos_validos[fundos_validos["grupo"] == cluster_num]
        fundos_unicos = set(
            cluster_df["Nome_Fundo"].tolist()
        )  # Usar set() para remover duplicatas
        objetos_clusters.append(
            list(fundos_unicos)
        )  # Converter set de volta para lista

    return objetos_clusters


async def cluster_and_save_plot(
    df_informe_mensal, carteira_selecionada, num_clusters, output_filename
):
    # Filters the funds that have default value for the selected portfolio
    fundos_validos = df_informe_mensal[df_informe_mensal[carteira_selecionada].notna()]

    # Prepare data for clustering
    X = fundos_validos[[carteira_selecionada]]

    # Creating clusters using K-Means with the specified number of clusters
    kmeans = KMeans(n_clusters=num_clusters)
    fundos_validos["grupo"] = kmeans.fit_predict(X)

    # Plot the bar chart separating the clusters
    plt.figure(figsize=(10, 6))
    colors = ["blue", "orange", "red"]
    for grupo, color in zip(range(num_clusters), colors):
        grupo_df = fundos_validos[fundos_validos["grupo"] == grupo]
        plt.scatter(
            grupo_df.index,
            grupo_df[carteira_selecionada],
            color=color,
            label=f"Cluster {grupo}",
        )

    plt.title(
        f'Clusterização de Taxas de Inadimplência para a Carteira "{carteira_selecionada}"'
    )
    plt.xlabel("Fundo")
    plt.ylabel("Taxa de Inadimplência")
    plt.xticks([])
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    static_folder = "../static/assets"
    output_path = os.path.join(static_folder, output_filename)

    plt.savefig(output_path, format="png")

    plt.close()

    await asyncio.sleep(5)

    return output_path


# Função principal
async def main():
    # Ler o arquivo CSV
    nome_arquivo = "IM_230626_semNP.csv"
    df = ler_arquivo_csv(nome_arquivo)

    # Calcular a taxa de inadimplência
    df = calcular_taxa_inadimplencia(df)

    # Realizar clusterização
    carteira_selecionada = "Carteira_Cartao_Credito"
    num_clusters = 3
    objetos_clusters = realizar_clusterizacao(df, carteira_selecionada, num_clusters)

    # Atribuir os arrays de fundos em cada cluster a variáveis separadas
    cluster1 = objetos_clusters[0]
    cluster2 = objetos_clusters[1]
    cluster3 = objetos_clusters[2]
    # Realizar clusterização
    carteira_selecionada = "Carteira_Cartao_Credito"
    num_clusters = 3
    output_filename = "output_plot.png"
    await cluster_and_save_plot(df, carteira_selecionada, num_clusters, output_filename)

    return (
        cluster1,
        cluster2,
        cluster3,
    )


if __name__ == "__main__":
    cluster1, cluster2, cluster3 = main()
    print(f"Cluster 1: {cluster1}")
    print(f"Cluster 2: {cluster2}")
    print(f"Cluster 3: {cluster3}")
