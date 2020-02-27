from ._unit import Unit

from abc import abstractmethod
import numpy as np
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests

ALPHA = 0.05
CORRECTION = 'hs'
MARKERS_N = 100


class Mark(Unit):
    """
    Base class for Marker Finding methods.
    """
    def __init__(self, verbose=False, **kwargs):
        """
        Args:
            verbose (bool): Printing flag.
            **kwargs: Argument dict.
        """
        super().__init__(verbose, **kwargs)

    @abstractmethod
    def get(self, x, labels):
        return np.zeros(shape=(len(np.unique(labels)), x.shape[1]))


class Mark_TTest(Mark):
    """
    One-vs-all T-Test.

    Two sided test for the null H_0: The two populations have the same average.
    If the p-value is small (<alpha), reject the null. Apply correction for
    multiple testing.
    """
    def __init__(self, verbose=False, **kwargs):
        super().__init__(verbose, **kwargs)
        self.alpha = kwargs.get('alpha', ALPHA)
        self.correction = kwargs.get('correction', CORRECTION)
        self.markers_n = kwargs.get('markers_n', MARKERS_N)

    def get(self, x, labels):
        assert len(x.shape) == 2
        # Infer unique labels from input
        unq_labels = np.unique(labels)
        if len(unq_labels) <= 1:
            self.vprint("Only one label found. Cannot run t-test.")
            return {}

        test_results = {}

        for i in unq_labels: # label to consider
            pvals = np.zeros(shape=(x.shape[1]))
            diffs = np.zeros_like(pvals)
            for j in range(x.shape[1]): # current column index (gene)
                x_ij = x[np.where(labels == i), j].squeeze() # Not empty
                x_not_ij = x[np.where(labels != i), j].squeeze() # Not empty

                #WARNING: ttest will throw error if cluster has single point
                t, pvals[j] = ttest_ind(x_ij, x_not_ij, equal_var=False)
                diffs[j] = np.mean(x_ij) - np.mean(x_not_ij)

            decision, pvals, _, _ = multipletests(
                pvals,
                alpha=self.alpha,
                method=self.correction,
                is_sorted=False,
                returnsorted=False
            )

            rejected_hs = np.where(decision == True)[0]
            sorted_diff_indices = np.flip(np.argsort(diffs[rejected_hs]))

            final_indices = rejected_hs[sorted_diff_indices][:self.markers_n]

            test_results[i] = {'indices': final_indices,
                               'pvals': pvals[final_indices],
                               'diffs': diffs[final_indices]}

        return test_results