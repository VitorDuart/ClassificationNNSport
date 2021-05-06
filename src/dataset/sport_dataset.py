import pandas as pd
from sklearn import preprocessing

class SportDataset:
    def __init__(self):
        self.url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQawc5X-ze3k_jNJFQ094gVIhdyYHhcG74GR1dXDzoOe2Jbe858gkYvio46a9kXo_HZSt4b_2f3Bdzx/pub?gid=0&single=true&output=csv'
        self.dataset = pd.read_csv(self.url)
        self.class_col = 'Esporte'

        self.on_hot_encoder()
    
    def on_hot_encoder(self):
        self.dataset.pop('Nome')

        columns = ['Nacionalidade', 'Personalidade', 'Cor da Pele']

        for column in columns:
            column_values = self.dataset[column].drop_duplicates()
            for value in column_values:
                self.dataset[value] = self.dataset[column].copy()
                self.dataset.loc[self.dataset[value] != value, value] = 0
                self.dataset.loc[self.dataset[value] == value, value] = 1
            self.dataset.pop(column)

        
        i = 0
        values_class = self.dataset[self.class_col].drop_duplicates()
        for value in values_class:
            self.dataset.loc[self.dataset[self.class_col] == value, self.class_col] = i
            i +=1

    def l2_normalize(self):
        y = self.dataset.pop(self.class_col)
        
        X = preprocessing.normalize(self.dataset,norm='l2')
        
        columns = self.dataset.columns.tolist()

        self.dataset = pd.DataFrame(columns=columns, data=X)
        self.dataset[self.class_col] = y.tolist()

    def getXy(self):
        columns = self.dataset.columns.tolist()
        columns.remove(self.class_col)
        return (self.dataset[columns], self.dataset)



        

        
    



