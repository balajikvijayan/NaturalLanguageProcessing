5.2 Exercise
---------------------

In this exercise, we will extract named entities from New York Times articles and attempt to discover sentiment about them.
1. Build a Mongo collection of (at least) a thousand articles using api.nytimes.com
2. Scrape and parse the article content using the URLs provided with BeautifulSoup
3. Join the paragraphs and tokenize them.
4. Tag the tokens with part-of-speech tags.
5. Use [`nltk.ne_chunk`](http://www.nltk.org/api/nltk.chunk.html#nltk.chunk.ne_chunk) to recognize named entities and store them in Mongo along with the articles in a new field called `entities`. *e.g.* `(GPE New/NNP York/NNP)` should be stored as `{'entities': {'GPE': ['New York']}`. *Hint*: Use [`$addToSet`](http://docs.mongodb.org/manual/reference/operator/update/addToSet/) to avoid adding duplicates. While you're doing this, keep a count of document frequency of each named entity, that is, how many different articles include "New York", etc.
6. Pick a few named entities with the highest document frequency. Run your sentiment classifier from last week on them. Do some entities appear to have more positive or negative sentiment attached to them. (Beware, words that indicate positive or negative sentiment in movie reviews may not carry the same implication in New York Times articles.) Do a spot check on the articles classified with the greatest confidence (according to `.predict_proba`). Do you agree with your model's prediction? (*i.e.* do you think it correctly identified positive and negative sentiment?) What do you think you could do to improve your model?


Optional:
1. Try stemming both your training (IMDb) and test (NYT) set before training and testing your sentiment analysis classifier. (*N.B.* do **not** stem before tagging.)
2. Try improving your POS tags with word shape features as described in slide 20 of [the lecture](http://spark-public.s3.amazonaws.com/nlp/slides/Information_Extraction_and_Named_Entity_Recognition_v2.pdf) as follows:
    1. `a-z` –> `x`, `A-Z` –> `X`, `0-9` –> `d`, `,.;:”’?!$-` –> self, other –> `*`
    2. Trim sequences of length 3+ to 3  
    e.g. `'apples'` –> `'xxx'`, `'Apples'` –> `'Xxxx'`, `'app9LES@'` –> `'xxx9XXX*'`  
    Hint: use `.islower()`, `.isupper()`, and `.isdigit()`.  
    Does that improve your NER?
3. Try using [spaCy](https://honnibal.github.io/spaCy/)'s NER instead. (A brief spot check suggests that spaCy's is much better than NLTK's, but also much slower.)