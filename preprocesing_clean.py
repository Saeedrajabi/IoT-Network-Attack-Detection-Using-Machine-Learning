import pandas as pd


def minmaxscaling(dataset):
    '''
    Normalize the dataset for the features of type intt 64 or float 64 using
    minmaxscaling.
    '''
    
    features = dataset.columns

    min_feature_range = 0
    max_feature_range = 1

    non_nomalized_features = []
    for feature in features:
        if str(dataset[feature].dtype) == "int64" or str(dataset[feature].dtype) == "float64":
            x_min = dataset[feature].min()
            x_max = dataset[feature].max()

            X_std = (dataset[feature] - x_min) / (x_max - x_min)
            X_nomalized = X_std * (max_feature_range - min_feature_range) + min_feature_range

            dataset[feature] = X_nomalized
        else:
            non_nomalized_features.append(feature)
    
    return dataset, non_nomalized_features




def qualitative_feature_encoding(feature, dataset):
    '''
    Encodes a specific features of the datset from text values to
    integersby assigning an integer to each of the possible original values.
    '''

    unique_values = dataset[feature].unique()
    encoding = {}
    number_of_unique_values = len(unique_values)

    i = 0
    for feature_value in unique_values:
        encoding[feature_value] = i
        i += 1


    encoded_values = []
    for j in range(len(dataset[feature])):
        encoded_values.append(encoding[dataset.loc[j, feature]])

    dataset[feature] = encoded_values

    return dataset


def dataset_preprocesing(filePath, dataset_type):
    '''
    Applies the prepocessing to the dataset.
    '''

    #########################################
    # Reading the original dataset
    #########################################

    # read the dataset
    dataset = pd.read_csv(filePath)

    # print dataset size
    dataset_size = dataset.shape
    print("Original " + dataset_type + " dataset size: " + str(dataset_size))

    #################
    # creating a copy of the dataset
    clean_dataset = dataset

    #########################################
    # Removing undefined or irrelevant features
    #########################################

    #################
    # Remove features that are not relevant

    clean_dataset.drop('id', axis=1, inplace=True)
    clean_dataset.drop('service', axis=1, inplace=True)
    clean_dataset.drop('rate', axis=1, inplace=True)
    clean_dataset.drop('ct_ftp_cmd', axis=1, inplace=True)

    #################
    # remove values that are not 0 or 1 for binary feature "is_ftp_login"

    clean_dataset = clean_dataset[clean_dataset["is_ftp_login"] != 2]
    clean_dataset = clean_dataset[clean_dataset["is_ftp_login"] != 4]
    clean_dataset.reset_index(drop=True, inplace=True)  # reset indexes of pandas dataframe
    #clean_dataset = clean_dataset[clean_dataset["is_ftp_login"] == 0 or clean_dataset["is_ftp_login"] == 1]

    #################
    # Remove features with undefined values
    clean_dataset = clean_dataset[clean_dataset["state"] != "no"]
    clean_dataset.reset_index(drop=True, inplace=True) # reset indexes of pandas dataframe


    #########################################
    # Enconding qualitative features
    #########################################

    feature_to_encode = "proto"
    clean_dataset = qualitative_feature_encoding(feature_to_encode, clean_dataset)

    feature_to_encode = "state"
    clean_dataset = qualitative_feature_encoding(feature_to_encode, clean_dataset)


    #########################################
    # Normalize Features
    #########################################

    clean_dataset, non_nomalized_features = minmaxscaling(clean_dataset) # using minmaxscaling


    #########################################
    # One hot encoding
    #########################################    

    one_hot_encoding = {'Normal': [0,0,0,0],
                        'Backdoor': [0,0,0,1],
                        'Analysis': [0,0,1,0],
                        'Fuzzers': [0,0,1,1],
                        'Shellcode': [0,1,0,0],
                        'Reconnaissance': [0,1,0,1],
                        'Exploits': [0,1,1,0],
                        'DoS': [0,1,1,1],
                        'Worms': [1,0,0,0],
                        'Generic': [1,0,0,1]}

    feature_to_encode = "attack_cat"

    one_hot_values = []
    for j in range(len(clean_dataset[feature_to_encode])):
        one_hot_values.append(one_hot_encoding[clean_dataset.loc[j, feature_to_encode]])

    clean_dataset[feature_to_encode] = one_hot_values


    return clean_dataset




################
# Change the file paths to the paths to the training and testing datasets
################
filePath_training = "./datasets/UNSW_NB15_training-set.csv"
filePath_testing = "./datasets/UNSW_NB15_testing-set.csv"



#########################################
# Preprocess the datasets
#########################################   
clean_training_dataset = dataset_preprocesing(filePath_training, "Training")
clean_testing_dataset = dataset_preprocesing(filePath_testing, "Testing")


# print clean datasets size
print("\nCleaned training dataset size: " + str(clean_training_dataset.shape))
print("Cleaned testing dataset size: " + str(clean_testing_dataset.shape))


#########################################
# Save the preprocessed datasets
#########################################  
clean_training_dataset.to_csv('normalized_dataset_training.csv', index=False)
clean_testing_dataset.to_csv('normalized_dataset_testing.csv', index=False)
print("The new datasets have been saved")


