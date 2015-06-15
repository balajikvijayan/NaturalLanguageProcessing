4.1 Exercise
---------------------
Your goal for this exercise is to perform **Sentiment Analysis**: classifying movie reviews as positive or negative. Recall from lecture that sentiment analysis can be used to extract people's opinions about all sorts of things (congressional debates, presidential speeches, reviews, blogs) and at many levels of granularity (the sentence, the paragraph, the entire document). Our goal in this task is to look at an entire movie review and classify it as positive or negative.

### Algorithm

You will be using Multinomial Naïve Bayes with Laplace smoothing. Your classifier will use word counts as features and make a binary decision between positive and negative. You will also explore the effects of stop-word filtering. This means removing common words like "the", "a" and "it" from your train and test sets. 

### Assignment

Train a classifier on the [**imdb1** data set](http://www.cs.cornell.edu/People/pabo/movie-review-data/). This is the actual Internet Movie Database review data used in the original [Pang *et al.* (2002)](http://www.cs.cornell.edu/home/llee/papers/sentiment.pdf) paper. (This data set also exists as an NLTK corpus, but I want you to use the plain text version. There is [a copy in the github repo](https://github.com/zipfian/DSCI6004-student/blob/master/week4/sentiment.zip)). 

1. Start by using NLTK's [Naïve Bayes](http://www.nltk.org/_modules/nltk/classify/naivebayes.html) classifier on a single train/test split. (*N.B.* NLTK is not very efficient. So while this is running you may want to start 2 on your partner's computer.)
2. Do the same using Scikit-Learn's [Count Vectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) and [Multinomial Naïve Bayes](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html) classifier. 
3. Compare the results of the two classifiers. Are they the same? If not, what did you do differently in each case? (*N.B.* preprocessing can make a big difference here. For example, Scikit-Learn's Count Vectorizer does not use the same [token pattern](https://github.com/scikit-learn/scikit-learn/blob/bb39b49/sklearn/feature_extraction/text.py#L570) as NLTK's [word_tokenize](http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.word_tokenize). You may need to do some work to make sure the training data in each case are equivalent.) 
4. Use 10-fold cross-validation training and testing on this data. What is your average accuracy and $F_1$? 
5. Next, evaluate your model again with the stop words removed. Does this approach affect average accuracy and $F_1$ (for the current given data set)? (*Hint*: `sklearn.feature_extraction.text.CountVectorizer` includes a `stop_words` parameter. Check the documentation to see how it works.)
6. If there's time: try TF-IDF. Pay attention to the parameters in the `TfidfVectorizer`, especially `norm` and `sublinear_tf`. How do the defaults compare to what Manning described in the IR lectures a couple weeks ago? Does this help or hurt?
7. Compare the source code of each algorithm to the pseudocode in [Manning, Raghavan, and Schütze](http://nlp.stanford.edu/IR-book/html/htmledition/naive-bayes-text-classification-1.html)
8. Write your own version of Multinomial Naïve Bayes from scratch and check your results against NLTK's and Scikit-Learn's. (When doing this, try not to look at the source code from either of those two packages and use only [Chapter 13](https://github.com/zipfian/DSCI6004-student/blob/master/week4/4.1/13bayes.pdf) of [the IR book](http://nlp.stanford.edu/IR-book/).) You may use the cross-validation sections defined in the [README](http://www.cs.cornell.edu/People/pabo/movie-review-data/poldata.README.2.0.txt)