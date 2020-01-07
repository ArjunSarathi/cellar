from acip.acip import ACIP
from utils.utils_experiment import load_data
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings('ignore')

if __name__ == '__main__':
    plt.ion()

    dataset = 'spleen'
    X, Y = load_data(dataset)
    w = ACIP(X, Y, config=dataset, verbose=True)
    w.pca_plot_var_ratio(20)
    w.reduce_dim(method='pca')
    w.cluster(method='kmedoids')
    w.reduce_plot(labels=w.y_train_pred, method='umap')

    plt.ioff()
    plt.show()