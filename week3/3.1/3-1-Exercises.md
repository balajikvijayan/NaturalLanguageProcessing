3.1 Exercises
---------------------
Write a program to compute unsmoothed ([MLE](http://www.nltk.org/api/nltk.html#nltk.probability.MLEProbDist)) unigrams and bigrams. Add an option to your program to generate random sentences. You already saw a version of this in [Section 2.2](http://www.nltk.org/book_1ed/ch02.html#code-random-text) of the NLTK book, but this time:

1. `return` the results (don't `print` them). Save `print` for outside the function.
2. Allow it to use different language models, so that you can implement the features below.
3. Optional: refactor it to use recursion instead of a `for` loop.

Add an option to your program to do the following:

1. Good-Turing discounting
2. Kneser-Ney discounting
3. interpolation
4. compute the perplexity of a test set

You may use NLTK's functions to this effect but browse through the [code](http://www.nltk.org/_modules/nltk/probability.html) and [documentation](http://www.nltk.org/api/nltk.html) to make sure you understand what they're doing and that it jibes with what you learned from the lectures. Pay attention to how `SimpleGoodTuringProbDist ` and `KneserNeyProbDist` extend `ProbDistI`. Notice also that `LaplaceProbDist` extends `LidstoneProbDist` which, in turn, extends `ProbDistI`. Lidstone was not discussed in the lectures. Can you figure out how it works and how it differes from (generalizes?) Laplace smoothing from the documentation? Are there any other classes in the `probability` sub-module you might want to try (hint: look for other classes that extend `ProbDistI` and `LidstoneProbDist`)? See https://sites.google.com/site/gothnlp/exercises/jurafsky-martin/solutions for some sample code that might help.

Advanced:

- Create a new class, extending `ProbDistI`, that implements Stupid Backoff (Note: this will be helpful for tomorrow).