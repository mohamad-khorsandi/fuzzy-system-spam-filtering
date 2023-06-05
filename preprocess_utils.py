from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif

def process_data(sms_data_str):
    """
    convert `sms_data_str` into a pandas dataframe
    """
    data_arr = []

    data_records = sms_data_str.split('\n')[:-1]
    for data in data_records:
        label = None
        sample = None
        match data[:3]:
            case 'ham':
                label = 'legitimate'
                sample = data[4:]
            case 'spa':
                label = 'spam'
                sample = data[5:]
            case _:
                label = 'N/A'

        data_arr.append([label, sample])

    data_arr = np.array(data_arr)
    data_label = data_arr[:, 0]
    data_records = data_arr[:, 1]

    return data_records, data_label


def tfidf_vectorizer(records):
    vectorizer = TfidfVectorizer(
        lowercase=True,
        token_pattern=r'\b[A-Za-z]+\b',
        norm=None
    )

    records_transformed = vectorizer.fit_transform(records)

    return records_transformed.toarray(), vectorizer.get_feature_names_out()


def feature_extraction(X, n_components=5):
    reduction_pca = PCA(
        n_components=n_components,
        whiten=False
    )
    data_reduced = reduction_pca.fit_transform(X)
    return data_reduced


def feature_selection(df_records, labels, n_components=5):
    feature_selection_model = SelectKBest(mutual_info_classif, k=n_components)
    ## make a selection over the best features
    selected_record_features = feature_selection_model.fit_transform(df_records, labels)

    return selected_record_features, feature_selection_model.get_feature_names_out()