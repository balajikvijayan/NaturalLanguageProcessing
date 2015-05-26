1.1 Exercises
-------------
### 1. Zipf's Law:
Let $f(w)$ be the frequency of a word $w$ in free text. Suppose that all the words of a text are ranked according to their frequency, with the most frequent word first. Zipf's law states that the frequency of a word type is inversely proportional to its rank $(i.e.~f \times r = k$ for some constant $k)$. For example, the 50th most common word type should occur three times as frequently as the 150th most common word type.
1. Write a function to process a large text and plot word frequency against word rank using `plot`. Do you confirm Zipf's law? (Hint: it helps to use a logarithmic scale). What is going on at the extreme ends of the plotted line?
2. Generate random text, e.g., using `random.choice("abcdefg ")`, taking care to include the space character.  You will need to `import random` first. Use the string concatenation operator to accumulate characters into a (very)
long string.  Then tokenize this string, and generate the Zipf plot as before, and compare the two plots.  What do you make of Zipf's Law in the light of this?

### 2. Modify the text generation program: 
```python
def generate_model(cfdist, word, num=15):
    for i in range(num):
        print word,
        word = cfdist[word].max()

text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)
```
(from [2.5](http://www.nltk.org/book_1ed/ch02.html#code-random-text)) to do the following tasks:
1. Store the *n* most likely words in a list words then randomly choose a word from the list using `random.choice()`. (You will need to `import random` first.)
2. Select a particular genre, such as a section of the Brown Corpus, or a genesis translation, one of the Gutenberg texts, or one of the Web texts.  Train the model on this corpus and get it to generate random text.  You may have to experiment with different start words. How intelligible is the text?  Discuss the strengths and weaknesses of this method of generating random text.
3. Now train your system using two distinct genres and experiment with generating text in the hybrid genre.  Discuss your observations.

### 3. Define a function `find_language()` that takes a string as its argument, and returns a list of languages that have that string as a word. 
Use the `udhr` corpus and limit your searches to files in the Latin-1 encoding.

### 4. What is the branching factor of the noun hypernym hierarchy?
*i.e.* for every noun synset that has hyponyms — or children in the hypernym hierarchy — how many do they have on average? You can get all noun synsets using `wn.all_synsets('n')`.

### Bonus
The polysemy of a word is the number of senses it has. Using WordNet, we can determine that the noun *dog* has 7 senses with: `len(wn.synsets('dog', 'n'))`. Compute the average polysemy of nouns, verbs, adjectives and adverbs according to WordNet.