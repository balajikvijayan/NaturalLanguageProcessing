4.3 Exercise
---------------------
## NYT articles 

For this assignment, we will apply the MaxEnt (a.k.a. Logistic Regrassion) algorithm to a corpus of NYT articles to classify from which section the article came.

1. Read the articles.pkl file using the read_pickle function in pandas. Look at the result and understand the structure of your data. Once you are comfortable with the data, store the 'content' series you read in, as this is what we will be working with for the rest of the assignment.

2. Use the Scikit-Learn's [CountVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) to turn the content of the news stories into a document-term matrix. 

3. Use [Logistic Regression](http://scikit-learn.org/stable/modules/linear_model.html#logistic-regression). Use `solver = 'lbfgs'`.

4. Compare results to [Naïve Bayes](http://scikit-learn.org/stable/modules/naive_bayes.html) (either [Multinomial](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html) or [Bernoulli](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html))

Optional:  

1. Compare results to NLTK's [Maximum Entropy](http://www.nltk.org/_modules/nltk/classify/maxent.html) classifier (see [HOWTO](http://www.nltk.org/howto/classify.html) for help)
2. Compare results to Scikit-Learn's [Linear SVM](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html) (see [documentation](http://scikit-learn.org/stable/modules/svm.html) for details on how it works)
