---------------------
2.3 Exercise
---------------------

This assignment is part one of two in which you will be improving upon a rather poorly-made information retrieval system. You will build an inverted index to quickly retrieve documents that match queries.

### Data 

You will be using your IR system to find relevant documents among a collection of 60 short stories by the famed [Rider Haggard](http://en.wikipedia.org/wiki/H._Rider_Haggard). The training data is located in the `data/` directory under the subdirectory `RiderHaggard/`. Within this directory you will see yet another directory `raw/`. This contains the raw text files of 60 different short stories written by Rider Haggard. You will also see in the `data/` directory the files `queries.txt` and `solutions.txt`. We have provided these to you as a set of development queries and their expected answers to use as you begin implementing your IR system.

### Your Assignment

Improve upon the IR system provided in the github repository. This involves implementing:

- **Inverted Index:** Implement an inverted index - a mapping from words to the documents in which they occur.
- **Boolean Retrieval:** Implement a Boolean retrieval system, in which you return the list of documents that contain all words in a query (yes, we only support conjunctions...)

To improve upon the information retrieval system, you must implement and/or improve upon the following functions:

- `index():` This is where you will build the inverted index. The documents will have already been read in for you at this point, so you will want to look at some of the instance variables in the class:
    - `titles`
    - `docs`
    - `vocab`
- `get_posting():` This function returns a list of integers (document IDs) that identifies the documents in which the word is found. This is basically just an API into your inverted index, but you must implement it in order to be evaluated fully.
- `boolean_retrieve():` This function performs Boolean retrieval, returning a list of document IDs corresponding to the documents in which all the words in `query` occur.

### Evaluation
Your IR system will be evaluated on a development set of queries as well as a held-out set of queries. The queries are encoded in the file **queries.txt** and are:
- separation of church and state
- priestess ritual sacrifice
- demon versus man
- african marriage queen
- zulu king

### Running the code
For Python, execute
```
$ cd python
$ python IRSystem.py
```
This will run you IR system and test it against the development set of queries. If you want to run your IR system on other queries, you can do so by replacing the last line above with
```
$ python IRSystem.py "My very own query"
```
Note that the first time you run this, it will create a directory named `stemmed/` in `../data/RiderHaggard/.` This is meant to be a simple cache for the raw text documents. Later runs will be much faster after the first run. *However*, this means that if something happens during this first run and it does not get through processing all the documents, you may be left with an incomplete set of documents in `../data/RiderHaggard/stemmed/.` If this happens, simply remove the `stemmed/` directory and re-run!