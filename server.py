from flask import Flask
from flask_cors import CORS
from flask import jsonify
from flask import request
from recommender import Recommender
import predictor
import json
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

app = Flask(__name__)
CORS(app)
categories = ['ENTERTAINMENT', 'FOOD & DRINK', 'POLITICS', 'STYLE & BEAUTY', 'TECH']
tweets = []
with open('data.json') as f:
    for jsonObject in f:
        tweet = json.loads(jsonObject)
        tweets.append(tweet)

dataset = dict((k,[]) for k in categories)
for t in tweets:
    try:
        dataset[t['category']].append(t)
    except KeyError:
        pass


@app.route('/')
def index():
    print(666666666)
    return 'GOOODDD!!!', 200

@app.route('/process/')
def process():
    tweets_filtered = []
    headline=request.args.get('headline')
    description=request.args.get('short_description')
    query = headline + ' ' + description
    prediction = predictor.predictor(query)
    prediction = sorted(prediction, key= lambda i:i[1], reverse=True)
    index = prediction[0][0]
    category = categories[index]
    r = Recommender(query, dataset[category])
    results = r.return_results()
    #category_index =
    print(results)
    return jsonify(results), 200

@app.route('/workload/<count>')
def workload(count):
    for i in range(int(count)):
        i += 1
    return 'success', 200

if __name__ == "__main__":
    app.run()

