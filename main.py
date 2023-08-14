import sys
sys.path.insert(1, "../")
import numpy as np
import pandas as pd
from aif360.datasets import StandardDataset

np.random.seed(0)

default_mappings = {
    'label_maps': [],
    'protected_attribute_maps': [],
}

def default_preprocessing(df):
    return df


class MetaDataset(StandardDataset):

    def __init__(self, label_name='image', favorable_classes=[1],
                 protected_attribute_names=[],
                 privileged_classes=[],
                 instance_weights_name=None,
                 categorical_features=[],
                 features_to_keep=[], features_to_drop=['lesion_id'],
                 na_values=[], custom_preprocessing=default_preprocessing,
                 metadata=default_mappings):
        df = None
        column_names = ['image', 'age_approx', 'anatom_site_general', 'lesion_id', 'sex']
        try:
            df = pd.read_csv('ISIC_2019_Training_Metadata.csv', sep=',', header=1, names=column_names,
                             na_values=[])
        except IOError as err:
            print("IOError: {}".format(err))
            import sys
            sys.exit(1)

        super(MetaDataset, self).__init__(df=df, label_name=label_name,
                                          favorable_classes=favorable_classes,
                                          protected_attribute_names=protected_attribute_names,
                                          privileged_classes=privileged_classes,
                                          instance_weights_name=instance_weights_name,
                                          categorical_features=categorical_features,
                                          features_to_keep=features_to_keep,
                                          features_to_drop=features_to_drop, na_values=na_values,
                                          custom_preprocessing=custom_preprocessing, metadata=metadata)