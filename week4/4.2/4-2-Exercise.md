4.2 Exercise
---------------------
Your goal for this exercise is to improve the sentiment analysis classifier from yesterday. 

1. Go from counts to boolean incidence vectors (`binary = True`) for your document-term matrix. Stick with Multinomial Naïve Bayes for now. How does performance differ from yesterday? Compute a [confusion matrix](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html) to compare.
2. Use Negation: Add `NOT_` to every word between negation and following punctuation:  
    $e.g.$ `"didn’t like this movie , but I"`  
    $\rightarrow$ `"didn’t NOT_like NOT_this NOT_movie but I"`  
    See [Stack Overflow](http://stackoverflow.com/questions/29374157/negation-handling-in-sentiment-analysis) for how an example of how to do this.  
    ***Warning***: 
    - this code produces unigrams, bigrams, and trigrams. You may want to alter it for your purposes.
    - this code has a bug. It will detect any occurrance of "no" in a string (such as ar**no**ld) and count it as a negation. You will need to fix this.
3. Is [Bernoulli Naïve Bayes](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html) better or worse? Look at the `feature_log_prob_` property in each and see how they compare with the strongest and weakest features. Compute a confusion matrix to compare.
    
Advanced: Experiment with sentiment lexicons to find other ways of predicting sentiment.
- [SentiWordNet](http://www.nltk.org/howto/sentiwordnet.html)
- [Opinion Lexicon](http://www.cs.uic.edu/~liub/FBS/opinion-lexicon-English.rar)
- [General Inquirer](http://www.wjh.harvard.edu/~inquirer/inquirerbasic.xls)