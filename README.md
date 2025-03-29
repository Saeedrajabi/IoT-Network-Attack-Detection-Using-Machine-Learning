# IoT Network Attack Detection Using Machine Learning 

This repository contains comprehensive implementations and analyses of various Machine Learning models aimed at detecting malicious activities on IoT networks. With an extensive dataset of 257,000 network traffic samples, the models explored in this project showcase impressive results in classifying network traffic as either malicious or benign.

## 🌟 Overview
Internet of Things (IoT) devices have exponentially increased in number, becoming vital yet vulnerable parts of everyday infrastructure. Ensuring IoT network security through rapid and accurate detection of malicious packets is crucial to prevent significant damage. This project explores the effectiveness of several Machine Learning (ML) methodologies in identifying attacks on IoT networks.

## 🗃️ Data Source
Dataset Name: [**UNSW-NB15: a comprehensive data set for network intrusion detection systems (UNSW-NB15 network data set)**](https://ieeexplore.ieee.org/abstract/document/7348942?casa_token=wYP4KsHhAAgAAAAA:XHuaWFYxBwAeA1dflzrxK7BBKftMf2se-RMtitw0bZLeznBXeAji_IajYf2JtKsy5SfENeWf)
The dataset utilized contains network traffic samples labeled as malicious or benign, encompassing features such as IP addresses, protocol types, and other significant metrics related to IoT traffic.

## 🛠️ Machine Learning Models Explored
1. **Logistic Regression**
   - Optimization: SGD and Adam
   - Feature selection via PCA and parameter analysis

2. **Decision Tree**
   - Fast training and robust accuracy even with smaller data splits
   - Achieved 94.12% accuracy

3. **Multi-Layer Perceptron (MLP)**
   - Multiple hidden layers with ReLU and Dropout
   - Hyperparameter tuning through grid search
   - Highest achieved accuracy: 94.91%

4. **Support Vector Machine (SVM)**
   - Kernel: RBF
   - Optimal performance at 92.61% accuracy

## Results
| Model                    | Accuracy (%) |
|--------------------------|--------------|
| Multi-Layer Perceptron   | 94.91%       |
| Decision Tree            | 94.12%       |
| Logistic Regression      | 90.59%       |
| Support Vector Machine   | 92.61%       |

## 📈 Key Highlights
- Effective data preprocessing including normalization, encoding, and balancing.
- Utilized PCA for dimensionality reduction and efficient feature selection.
- Comprehensive hyperparameter optimization to ensure model robustness.
- Easy to reproduce and extendable codes provided in notebooks and scripts.
