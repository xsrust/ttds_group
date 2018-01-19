import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.preprocessing import LabelBinarizer
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import CCA
from sklearn.model_selection import GridSearchCV
import sys

def hamming_score(y_true, y_pred, normalize=True, sample_weight=None):
    '''
    Compute the Hamming score (a.k.a. label-based accuracy) for the multi-label case
    '''
    acc_list = []
    for i in range(y_true.shape[0]):
        set_true = set( np.where(y_true[i])[0] )
        set_pred = set( np.where(y_pred[i])[0] )
        tmp_a = None
        if len(set_true) == 0 and len(set_pred) == 0:
            tmp_a = 1
        else:
            tmp_a = len(set_true.intersection(set_pred))/\
                    float( len(set_true.union(set_pred)) )
        acc_list.append(tmp_a)
    return np.mean(acc_list)

train_size = int(sys.argv[1])
dev_size = int(sys.argv[2])
feature_size = int(sys.argv[3])
num_classes = 24

print("Processing data");

train_X = np.zeros([train_size, feature_size]);
train_Y = np.zeros([train_size, num_classes]);
dev_X = np.zeros([dev_size, feature_size]);
dev_Y = np.zeros([dev_size, num_classes]);

file = open("feats.train", "r")
num = 0
for line in file:
	features = line.split()
	classes = features[1]
	if ':' not in classes:
		classes = classes.split(',')
		for y in classes:
			train_Y[num][int(y)-1] = 1;
		features = features[2:]
	else:
		features = features[1:]
	for feature in features:
		x, value = feature.split(':')
		train_X[num][int(x)-1] = int(value);
	num += 1
file.close()

file = open("feats.dev", "r")
num = 0
for line in file:
	features = line.split()
	classes = features[1]
	if ':' not in classes:
		classes = classes.split(',')
		for y in classes:
			dev_Y[num][int(y)-1] = 1;
		features = features[2:]
	else:
		features = features[1:]
	for feature in features:
		x, value = feature.split(':')
		dev_X[num][int(x)-1] = int(value);
	num += 1
file.close()

print("Training classifier");

classifier = OneVsRestClassifier(SVC())

parameters = {
    "estimator__C": [1,2,4,8,10,100],
    "estimator__kernel": ["rbf"],
    "estimator__gamma": ['auto', 1e-3, 1e-4],
    "estimator__degree": [2, 3, 4],
}

model_tunning = GridSearchCV(classifier, param_grid=parameters)

model_tunning.fit(train_X, train_Y)
model_tunning.best_score_
model_tunning.best_params_
print(model_tunning.best_params_)

print("Predicting outputs of dev set");

dev_output = model_tunning.predict(dev_X)

hamming_accuracy = hamming_score(dev_Y, dev_output)
print("Hamming score on dev set: {0}".format(hamming_accuracy))

sk_accuracy = accuracy_score(dev_Y, dev_output, normalize=True, sample_weight=None)
print("Skicit Accuracy on dev set: {0}".format(sk_accuracy))

