from dataset.sport_dataset import SportDataset
from sklearn.model_selection import train_test_split


ds = SportDataset()
ds.l2_normalize()

X, y = ds.getXy()

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.70)
