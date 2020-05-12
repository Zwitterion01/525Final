from sklearn.externals import joblib
def predictor(query):
 loaded_model = joblib.load('SVMClassifier.sav')
 result = loaded_model.predict_proba([query])
 prob_per_class_dictionary_svm = sorted(zip(loaded_model.classes_, result[0]), key=lambda x: x[1], reverse=True)
 return prob_per_class_dictionary_svm
