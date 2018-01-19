### To create dictionary of features from training subtitles:

```bash
cat TrainSubtitles/* > allwords.txt
perl tokenizer.pl [allwords.txt] feats.dict
```
**WARNING:** The ```allwords.txt``` file could not be uploaded to GitHub due to file size limitations. Download it from [this link](https://drive.google.com/open?id=1kKu6ico7l_-9qW-d5WRevHu__t2AcG8d) instead.

### To create train, dev and test feature files:
```bash
perl createSet.pl Train [newfilms.json] feats.train
perl createSet.pl Dev [newfilms.json] feats.dev
perl createSet.pl Test [newfilms.json] feats.test
```

```newfilms.json``` contains both jsons here, duplicates are ignored

### To classify:

#### Simple SVM:
```bash
python classify_simple.py [size_of_training_data] [size_of_dev_data] [total_num_of_features]
```
for example: ```python classify_simple.py 3529 500 12706```

#### GridSearch SVM:
```bash
python classify_gs.py [size_of_training_data] [size_of_dev_data] [total_num_of_features]
```
for example: ```python classify_gs.py 3529 500 12706```
