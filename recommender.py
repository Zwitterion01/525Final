from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, query, tweets):

        self.tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
        self.query = query
        self.tweets = tweets
        self.results = []

    def __compute_score(self):
        for tweet in self.tweets:
            content = tweet['headline'] + ' ' + tweet['short_description']
            doc = [self.query, content]
            result = dict()
            doc_vector = self.tf.fit_transform(doc)
            cosine_sim = cosine_similarity(doc_vector, doc_vector)
            result['content'] = tweet
            result['sim_score'] = cosine_sim[0][1]
            self.results.append(result)
    
    def return_results(self):
        self.__compute_score()
        self.results = sorted(self.results, key = lambda i: i['sim_score'], reverse=True)
        for re in self.results:
          re['category']=re['content']['category']
          re['headline']=re['content']['headline']
          re['authors'] = re['content']['authors']
          re['link'] = re['content']['link']
          re['short_description'] = re['content']['short_description']
          re['date'] = re['content']['date']
          re.pop('content')
        return self.results[:10]




