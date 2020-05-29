from ast import literal_eval

import numpy as np

from .exceptions import InvalidArgument
from .exceptions import InappropriateArgument
from .exceptions import MethodNotImplementedError


def _validate_dim_n_components(dim_n_components, method, h, w):
    if isinstance(dim_n_components, str):
        if dim_n_components != 'knee':
            try:
                dim_n_components = literal_eval(dim_n_components)
            except:
                raise InvalidArgument(
                    "Incorrect number of components specified.")
        elif method != 'PCA':
            raise InvalidArgument(
                "Incorrect number of components specified.")
        else:
            return dim_n_components

    if isinstance(dim_n_components, int):
        if dim_n_components >= h or dim_n_components >= w:
            raise InappropriateArgument(
                "Number of components needs to be less than "
                f"min(width, height)={min(w, h)}.")
        if dim_n_components < 1:
            raise InappropriateArgument(
                "Number of components needs to be greater than 0.")
    else:
        raise InvalidArgument("Incorrect number of components specified.")

    return dim_n_components


def _validate_n_clusters(n_clusters, h):
    if n_clusters >= h:
        raise InappropriateArgument("Number of clusters needs to be less than "
                                    "the number of samples.")
    if n_clusters < 2:
        raise InappropriateArgument("Number of clusters needs to be greater "
                                    "than 1.")


def _validate_clu_n_clusters(clu_n_clusters, h):
    if isinstance(clu_n_clusters, str):
        try:
            clu_n_clusters = literal_eval(clu_n_clusters)
        except:
            raise InvalidArgument(
                "Incorrect format for the number of clusters.")

    if isinstance(clu_n_clusters, int):
        _validate_n_clusters(clu_n_clusters, h)
        return clu_n_clusters
    elif isinstance(clu_n_clusters, tuple):
        try:
            clu_n_clusters = list(range(*clu_n_clusters))
        except:
            raise InvalidArgument("Incorrect tuple specified for the number of "
                                  "clusters.")
        if len(clu_n_clusters) < 1:
            raise InappropriateArgument(
                "Empty tuple encountered for the number of "
                "clusters.")
    elif isinstance(clu_n_clusters, list):
        if len(clu_n_clusters) < 1:
            raise InappropriateArgument(
                "Empty list encountered for the number of "
                "clusters.")
    else:
        raise InvalidArgument("Incorrect format for the number of clusters.")

    _validate_n_clusters(clu_n_clusters[0], h)
    _validate_n_clusters(clu_n_clusters[-1], h)

    return clu_n_clusters


def _validate_n_jobs(n_jobs):
    if isinstance(n_jobs, str):
        try:
            n_jobs = literal_eval(n_jobs)
        except:
            raise InvalidArgument("Incorrect number of jobs specified.")

    if isinstance(n_jobs, float):
        n_jobs = int(n_jobs)

    if isinstance(n_jobs, int):
        if n_jobs < -1:
            raise InvalidArgument("Incorrect number of jobs specified.")
        elif n_jobs > 8:
            raise InappropriateArgument("Number of jobs is too high.")
        elif n_jobs == 0:
            raise InappropriateArgument("Number of jobs is 0.")
    elif n_jobs is None:
        n_jobs = 1
    elif n_jobs is not None:
        raise InvalidArgument("Incorrect number of jobs specified.")

    return n_jobs


def _validate_mark_alpha(mark_alpha):
    if isinstance(mark_alpha, str):
        try:
            mark_alpha = literal_eval(mark_alpha)
        except:
            raise InvalidArgument("Incorrect significance alpha set.")

    if isinstance(mark_alpha, int):
        mark_alpha = float(mark_alpha)

    if isinstance(mark_alpha, float):
        if mark_alpha > 0.15 or mark_alpha < 0.001:
            raise InappropriateArgument(
                "Significance alpha needs to be in the interval (0.001, 0.15)")
    else:
        raise InvalidArgument("Incorrect significance alpha set.")

    return mark_alpha


def _validate_mark_markers_n(mark_markers_n, h):
    if isinstance(mark_markers_n, str):
        try:
            mark_markers_n = literal_eval(mark_markers_n)
        except:
            raise InvalidArgument("Incorrect number of markers set.")

    if isinstance(mark_markers_n, float):
        mark_markers_n = int(mark_markers_n)

    if isinstance(mark_markers_n, int):
        if mark_markers_n < 1:
            raise InappropriateArgument(
                "Number of markers needs to be greater than 1.")
        if mark_markers_n > h:
            raise InappropriateArgument(
                "Number of markers needs to be less "
                "than number of genes.")
    else:
        raise InvalidArgument("Incorrect number of markers set.")

    return mark_markers_n


def _validate_mark_correction(mark_correction):
    corrections_methods = ["bonferroni", "sidak", "holm-sidak", "holm",
                           "simes-hochberg", "hommel", "fdr_bh", "fdr_by",
                           "fdr_tsbh", "fdr_tsbky"]

    if isinstance(mark_correction, str):
        if mark_correction not in corrections_methods:
            raise MethodNotImplementedError("Incorrect correction method.")
    else:
        raise InvalidArgument("Incorrect correction method.")

    return mark_correction


def _validate_con_convention(con_convention):
    conventions = ["id-to-name", "name-to-id"]

    if isinstance(con_convention, str):
        if con_convention not in conventions:
            raise InvalidArgument("Incorrect convention specified.")
    else:
        raise InvalidArgument("Incorrect convention specified.")

    return con_convention


def _validate_ensemble_methods(ensemble_methods):
    methods = [
        "All",
        "KMeans",
        "KMedoids",
        "Spectral",
        "Agglomerative",
        # "DBSCAN",
        # "Birch",
        "GaussianMixture",
        "Leiden",
        "Scanpy"
    ]

    if isinstance(ensemble_methods, list):
        for method in ensemble_methods:
            if method not in methods:
                raise MethodNotImplementedError(
                    "Incorrect method encountered in ensemble clustering.")
            if method == 'All':
                return methods[1:]
    elif ensemble_methods is None:
        return "default"
    elif isinstance(ensemble_methods, str):
        if ensemble_methods not in methods:
            raise MethodNotImplementedError(
                "Incorrect method encountered in ensemble clusering.")
        if ensemble_methods == 'All':
            return methods[1:]
        else:
            return [ensemble_methods]
    else:
        raise InvalidArgument(
            "Incorrect list provided for ensemble clustering.")
    return ensemble_methods


def _validate_subset(subset):
    if subset is None:
        return None

    if isinstance(subset, (int, float)):
        return np.array([subset]).astype(np.int)
    elif isinstance(subset, list):
        if len(subset) == 0:
            return None
        return np.array(subset).astype(np.int)
    else:
        raise InvalidArgument("Invalid subset encountered.")