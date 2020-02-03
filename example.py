from acip.acip import ACIP
from utils.utils_experiment import read_config, load_data
from matplotlib import pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')

if __name__ == '__main__':
    dataset = 'spleen'
    dataset = 'spleen'
    X, Y, gene_ids = load_data(dataset)
    w = ACIP(X, config=dataset, verbose=False, col_ids=gene_ids)
    w.get_clusters_csv()
    w.plot("top_markers")
    plt.show()