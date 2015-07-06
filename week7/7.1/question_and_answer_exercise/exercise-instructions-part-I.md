7.1 Question Answering
--

**Can you make a system to compete with IBM's Jeopardy-playing "Watson"?**

Your job is to perform SPOUSE-OF(x, y) question answering via _relation extraction_ from Wikipedia.

You must use both of the following two methods:

1. Use structured info in Infoboxes
2. Use string text patterns such as those of Hearst (1992)

### How to do this

Start by taking a look at the data. You might have noticed that the Infobox for Arnold Schwarzenegger tells you that he is married to Maria Shriver:

```
{{Infobox Governor
|name         = Arnold Schwarzenegger  
...  
|spouse       = {{nowrap|[[Maria Shriver]] (1986&ndash;present)}}
```

You should process this structured Infobox data (however you like - regular expressions are fine) to pull out these "spouse" relationships. For this portion of the assignment, you should only be using the Infoboxes and no other information from the remainder of the article.

Next, use patterns like those of Hearst (1992) described in lecture to find example patterns like X is married to Y that could help you extract the spouse relation from text data. For example, we could extract Ingrid Selberg and Mustapha Matura from this sentence:

`Ingrid Selberg is married to playwright [[Mustapha Matura]].`

Finally, for each of these two methods (the method using the Infoboxes and the method using the text data) you need to output your guess of the spouse for each of the people in the input file "wives.txt". We will follow the Jeopardy format of returning a 'question' for each input 'answer'. For example, the first line of the input file is "Maria Shriver", so the first line of your output should be:

`Who is Arnold Schwarzenegger?`

We have given you the correct output for 20 wives/husbands in "wives.txt" and "husbands.txt" in the "gold.txt" file, and the starter code for a java version (that currently just outputs 'no answer').

**Please note:** You do not need to use XML. That is, you can use regular expressions rather than XML even for the Infoboxes part. However, I suggest exploring xml in The Standard Library or lxml.


