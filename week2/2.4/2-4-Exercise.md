2.4 Exercise
---------------------

This assignment is part two of two in which you will be improving upon a rather poorly-made information retrieval system. You will now make it even better by using term-frequency inverse-document-frequency weighting and cosine similarity to compare queries to your data set.

### Your Assignment

Continue improving the IR system given yesterday. This involves implementing:

- **TF-IDF:** Compute and store the term-frequency inverse-document- frequency value for every word-document co-occurrence: $w_{t,d}=(1+\text{log}_{10}\text{df}_{t,d})\times\text{log}_{10}(N/\text{df}_t)$
- **Cosine Similarity:** Implement cosine similarity in order to improve upon the ranked retrieval system, which currently retrieves documents based upon the Jaccard coefficient between the query and each document. The lecture on [Calculating TF-IDF Cosine Scores](https://class.coursera.org/nlp/lecture/189) will be helpful for this task. Specifically, you should look at slide 5 of the corresponding lecture slides. **Also** note that when computing $w_{t,q}$ (*i.e.* the weight for the word $w$ in the query) do *not* include the idf term. That is, $w_{t,q}=1+\text{log}_{10}\text{tf}_{t,q}$.

To improve upon the information retrieval system, you must implement and/or improve upon the following functions:

- `compute_tfidf():` This function computes and stores the tf-idf values for words and documents. For this you will probably want to be aware of the class variables `vocab` and `docs` which hold, respectively, the list of all unique words and the list of documents, where each document is a list of words.
- `get_tfidf():` You must implement this function to return the tf-idf weight for a particular word and document ID.
- `rank_retrieve():` This function returns a priority queue of the top ranked documents for a given query. Right now it ranks documents according to their Jaccard similarity with the query, but you will replace this method of ranking with a ranking using the cosine similarity between the documents and query.

### Evaluation
Your IR system will be evaluated on the same set of queries as yesterday.