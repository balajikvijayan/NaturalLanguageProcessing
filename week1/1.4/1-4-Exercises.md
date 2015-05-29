1.4 Exercises
---------------------
###  Teams

| Team | A     | B      |
| ----:|:-----:|:------:|
| 1 | Michael Mansour   | Katherine Aquino  |
| 2 | Xiaolin Wang      | Andrew Huang      |
| 3 | Michael Thorne    | Brandon Fetters   |
| 4 | Balaji Vijayan    | Alexander Barriga |


1. **Soundex:** Read the Wikipedia entry on [*Soundex*](http://en.wikipedia.org/wiki/Soundex). Implement this algorithm in Python.

2. **Reading Difficulty:**
    1. Readability measures are used to score the reading difficulty of a text, for the purposes of selecting texts of appropriate difficulty for language learners. Let us define $\mu_w$ to be the average number of letters per word, and $\mu_s$ to be the average number of words per sentence, in a given text. The Automated Readability Index (ARI) of the text is defined to be: $4.71\mu_w+0.5\mu_s-21.43$. Compute the ARI score for various sections of the Brown Corpus, including section `f` (popular lore) and `j` (learned). Make use of the fact that `nltk.corpus.brown.words()` produces a sequence of words, while `nltk.corpus.brown.sents()` produces a sequence of sentences.
    2. Obtain raw texts from two or more genres and compute their respective reading difficulty scores as in the earlier exercise on reading difficulty. *e.g.* compare ABC Rural News and ABC Science News `(nltk.corpus.abc)`. Use Punkt to perform sentence segmentation.

3. **Tries:**
    1. Write a recursive function that pretty prints a trie in alphabetically sorted order, e.g.:
            chair: 'flesh'
            ---t: 'cat'
            --ic: 'stylish'
            ---en: 'dog'
    2. With the help of the trie data structure, write a recursive function that processes text, locating the uniqueness point in each word, and discarding the remainder of each word. How much compression does this give? How readable is the resulting text?

4. **Summarization:** Develop a simple extractive summarization tool, that prints the sentences of a document which contain the highest total word frequency. Use `FreqDist()` to count word frequencies, and use `sum` to sum the frequencies of the words in each sentence. Rank the sentences according to their score. Finally, print the *n* highest-scoring sentences in document order. Carefully review the design of your program, especially your approach to this double sorting. Make sure the program is written as clearly as possible.

5. **SIPs:** Design an algorithm to find the "statistically improbable phrases" of a document collection. http://www.amazon.com/gp/search-inside/sipshelp.html

6. **Justification:** Obtain some raw text, in the form of a single, long string. Use Python's `textwrap` module to break it up into multiple lines. Now write code to add extra spaces between words, in order to justify the output. Each line must have the same width, and spaces must be approximately evenly distributed across each lines. No line can begin or end with a space.