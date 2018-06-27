# Python Sentiment Classification
This repository contains a pre-trained SVM model for french sentiment classification. The model has been learned on more than 10000 tweets released in [DEFT 2015](https://deft.limsi.fr/2015/) and [DEFT 2017](https://deft.limsi.fr/2017/) chanllenges.

## Installing dependencies
The code runs under python 3.6.
```
pip install -r requirements.txt
```

## Using the model
You just need to import the module and call the `predictFrench` function.
```python
import predictSentiment as ps

print(ps.predictFrench('Je suis content, il fait beau c\'est super ! '))
print(ps.predictFrench('Je suis triste, il pleut c\'est horrible ! '))
```
