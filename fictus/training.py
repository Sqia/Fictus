#   Copyright 2023 Aqila
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
# Inspiration, template from: https://medium.com/analytics-vidhya/fake-news-detection-using-nlp-techniques-c2dc4be05f99
# Credits to: https://medium.com/@joyceannie111
# Modified for my own use
# SVM
import sklearn.metrics as metrics
import pandas as pd
import pickle
from pathlib import Path

from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

# news classifier training
news_classifier_data = pd.read_csv(Path("fictus/data/news_classifier_model.csv"), delimiter=";")

x_train,x_test,y_train,y_test = \
    train_test_split(news_classifier_data['text'],news_classifier_data["label"],test_size=0.2, random_state = 1)

pipe = Pipeline([
    ('vect', CountVectorizer(encoding="utf-8")),
    ('tfidf', TfidfTransformer()),
    ('clf', LinearSVC())
])

news_classifier_model = pipe.fit(x_train, y_train)
prediction = news_classifier_model.predict(x_test)
# Test
score = metrics.accuracy_score(y_test, prediction)
print("accuracy:   %0.3f" % (score*100))

# Saving model
pickle.dump(news_classifier_model, open(Path("models/news_classifier_model.model"), "wb")) # make sure folder exist

# Fake news classifier training
fake_news_classifier_data = pd.read_json(Path("fictus/data/fake_news_classifier_model.json"))

x_train,x_test,y_train,y_test = \
    train_test_split(fake_news_classifier_data['content'],fake_news_classifier_data["classification"],test_size=0.2, random_state = 1)

pipe = Pipeline([
    ('vect', CountVectorizer(encoding="utf-8")),
    ('tfidf', TfidfTransformer()),
    ('clf', LinearSVC())
])

fake_news_classifier_model = pipe.fit(x_train, y_train)
prediction = fake_news_classifier_model.predict(x_test)

# Test
score = metrics.accuracy_score(y_test, prediction)
print("accuracy:   %0.3f" % (score*100))


# Saving model
pickle.dump(fake_news_classifier_model, open(Path("models/fake_news_classifier_model.model"), "wb")) # make sure folder exist