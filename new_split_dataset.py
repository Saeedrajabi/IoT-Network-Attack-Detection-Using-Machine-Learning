
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split


#########################################
# Read the datasets
#########################################  
filePath_training = "./original_split/normalized_dataset_training.csv" 
filePath_testing = "./original_split/normalized_dataset_testing.csv" 

dataset_training = pd.read_csv(filePath_training)
dataset_testing = pd.read_csv(filePath_testing)


#########################################
# Combine the datasets
#########################################  

# print clean datasets size
print("\nCleaned training dataset size: " + str(dataset_training.shape))
print("Cleaned testing dataset size: " + str(dataset_testing.shape))
print("New dataset size should be " + str(dataset_training.shape[0] + dataset_testing.shape[0]) +" , "+ str(dataset_testing.shape[1]))


print("\nComparison of the columns of the two datasets:")
print((dataset_training.columns == dataset_testing.columns))


# concatenate the two datasets
dataset = pd.concat([dataset_training, dataset_testing], ignore_index=True)
print("\nCombined dataset size: " + str(dataset.shape))

# save the new combined dataset
dataset.to_csv('./new_split/combined_dataset_testing.csv', index=False)


#########################################
# New split
#########################################  

# separate features from labels for binary clasification
features = dataset.drop(["label"], axis=1) # the classes for the specfic attacks are going to be included in features for the split.
features = features.to_numpy()


labels = dataset["label"] # the classes for the specfic attacks are going to be included in features for the split.
labels = labels.to_numpy()

## checking that the rows indexing is kept consistent
# recombined = features
# recombined["attack_cat"] = dataset["attack_cat"] 
# recombined["label"] = dataset["label"] 
# print(recombined.equals(dataset))

percentage_training = 0.8
x_train, x_test, y_train, y_test = train_test_split(features, labels, train_size = percentage_training)

#########################################
# Recontruct the dataset to the same format as the orignal one
#########################################  

features_names = list( dataset.drop(["label"], axis=1).columns)
new_training_dataset_df = pd.DataFrame(columns=features_names)
new_testing_dataset_df = pd.DataFrame(columns=features_names)

for i in range(len(features_names)):
    new_training_dataset_df[features_names[i]] = x_train[:,i]
    new_testing_dataset_df[features_names[i]] = x_test[:,i]

new_training_dataset_df["label"] = y_train
new_testing_dataset_df["label"] = y_test

#########################################
# Save the new datasets
#########################################  

new_training_dataset_df.to_csv('./new_split/training_dataset.csv', index=False)
new_testing_dataset_df.to_csv('./new_split/testing_dataset.csv', index=False)

