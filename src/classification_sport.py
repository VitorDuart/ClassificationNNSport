from dataset.sport_dataset import SportDataset

ds = SportDataset()

ds.l2_normalize()

print(ds.dataset)
