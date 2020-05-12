import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.externals import joblib
def create_SVM_Model(data):

    (train_texts, train_labels), (test_texts, test_labels) = data 
    # Support Vectormachine
    svm_pip = Pipeline([ 
            ('tfidf_vector_com', TfidfVectorizer(
                input='array', encoding="ISO-8859-1",
                max_df=0.8,
                min_df=1,
                norm='l2',
                max_features=None,  
                lowercase = True,
                sublinear_tf = True,
                stop_words='english',
            )),

            ('clf', SVC(C=10 , 
                cache_size=10000, 
                kernel='rbf', 
                gamma = 0.1,
                probability =True, 
                class_weight=None,
                tol=0.001))
        ])
    #SVM
    print("\n --- TEST OUTPUT SVM ---")
    svm_pip.fit(train_texts,train_labels)
    print("\n --- SVM Training Done---")
    predicted_SWR = svm_pip.predict(test_texts)
    predicted_SWR_train = svm_pip.predict(train_texts)
    print("\n --- SVM Predicting Done---")
    joblib.dump(svm_pip, 'SVMClassifier.sav', protocol=2)
    #Metrics
    print("Accuracy SVM test data:  " + str(np.mean(predicted_SWR == test_labels)))  
    print("Accuracy SVM train data: " + str(np.mean(predicted_SWR_train == train_labels)))


