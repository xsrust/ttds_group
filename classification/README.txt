To create dictionary of features from training subtitles:

cat TrainSubtitles/* > allwords.txt
perl tokenizer.pl < allwords.txt > feats.dict

To create train, dev and test feature files:

perl createSet.pl Train < newfilms.json > feats.train
perl createSet.pl Dev < newfilms.json > feats.dev
perl createSet.pl Test < newfilms.json > feats.test

newfilms.json contains both jsons here, duplicates are ignored

To classify:

Simple SVM:

python classify_simple.py <size_of_training_data> <size_of_dev_data> <total_num_of_features>
for example: python classify_simple.py 3529 500 12706

GridSearch SVM:

python classify_gs.py <size_of_training_data> <size_of_dev_data> <total_num_of_feature
s>
for example: python classify_gs.py 3529 500 12706
