import pandas as pd

pd.options.display.max_colwidth = -1
pd.options.display.max_columns = 10

from os.path import join


class Data:
    """ Loads and preprocesses data """
    def __init__(self):
        self.train_df, self.test_df = self.load_data()

    def load_data(self):
        train_path = join("/home/matt/kaggle/toxic_comment/toxic_data/train.csv")
        test_text_path = join("/home/matt/kaggle/toxic_comment/toxic_data/test.csv")
        test_labels_path = join("/home/matt/kaggle/toxic_comment/toxic_data/test_labels.csv")

        train_df = pd.read_csv(train_path)
        test_text_df = pd.read_csv(test_text_path)
        test_labels_df = pd.read_csv(test_labels_path)

        test_df = test_text_df.merge(test_labels_df, on='id')

        return train_df, test_df


class ModelDataManager:

    def __init__(self, data):
        text_mapper = TextMapper()
        label_mapper = LabelMapper()


class TextMapper:

    def __init__(self, text):


    def init_mappings(self, text):

class LabelMapper:
    def __init__(self, labels):