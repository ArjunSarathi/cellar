defaults <- list(
    "dim" = '10',
    "clu" = '(3, 5, 1)',
    "mark_alpha" = 0.05,
    "mark_no" = 200
)

options <- list(
    "dim" = c("PCA", "Kernel PCA", "Diffusion Map", "MDS", "UMAP", "Isomap",
              "Feature Agglomeration"),
    "clu" = c("Leiden", "KMeans", "KMedoids", "Spectral", "Agglomerative",
              "GaussianMixture", "Scanpy", "Ensemble"),
    "clu_ensemble" = c("All"="All", "KMeans"="KMeans", "KMedoids"="KMedoids",
                       "GaussianMixture"="GaussianMixture",
                       "Spectral"="Spectral", "Agglomerative"="Agglomerative",
                       "Leiden"="Leiden", "Scanpy"="Scanpy"),
    "clu_no_n_clusters" = c("DBSCAN", "Leiden", "Scanpy"),
    "eval" = c("Silhouette", "DaviesBouldin", "CalinskiHarabasz"),
    "correction" = c("holm-sidak", "bonferroni", "sidak", "holm",
                     "simes-hochberg", "hommel", "fdr_bh", "fdr_by",
                     "fdr_tsbh", "fdr_tsbky", "None"),
    "converter" = c("id-to-name", "name-to-id"),
    "tissues" = c("all", "blood", "brain", "embryo", "eye", "heart", "kidney",
                  "large intestine", "liver", "lymph", "muscle", "other",
                  "placenta", "small intestine", "spleen", "stomach", "thymus",
                  "thyroid", "clusters", "user defined"),
    "vis" = c("UMAP", "TSNE", "Diffusion Map", "MDS", "PCA", "Kernel PCA",
              "Isomap", "Feature Agglomeration"),
    "ssclu" = c("ConstrainedKMeans", "SeededKMeans",
                "ConstrainedSeededKMeans"),
    "de" = c("TTest"),
    "ali" = c("Scanpy Ingest", "SingleR"),
    "tissues" = c('Clusters','User defined')
)
