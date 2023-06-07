from enum import Enum

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif

from preprocess_utils import process_data, tfidf_vectorizer, feature_extraction, feature_selection

class Features(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    def __init__(self, index):
        self.min_value = None
        self.max_value = None
        self.index = index

def main():
    sms_data_str = None
    with open('SMSSpamCollection') as file:
        sms_data_str = file.read()

    records, labels = process_data(sms_data_str)
    records_vectorized, feature_names = tfidf_vectorizer(records)

    ## one hot encoding labels
    labels = np.array([0 if y == 'legitimate' else 1 for y in labels])

    # reducing dimension
    records_dim_reduced = feature_extraction(records_vectorized)

    print(records_dim_reduced[:5])
    calculate_min_max(records_dim_reduced[:5])

    # records_vectorized = pd.DataFrame(records_vectorized, columns=feature_names)
    # records_selection, feature_name_selection = feature_selection(records_vectorized, labels=labels)
    #
    #
    # ## for better visualization
    # print(pd.DataFrame(records_selection, columns=feature_name_selection).head())


def calculate_min_max(feature_list):
    min_list = feature_list.min(axis=0)
    max_list = feature_list.max(axis=0)

    for i, f in enumerate(list(Features)):
        f.min_value = min_list[i]
        f.max_value = max_list[i]


if __name__ == '__main__':
    main()

