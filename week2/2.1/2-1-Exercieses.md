2.1  Exercise
---------------------
### 1. Change making problem

The objective of this part of the exercise is to introduce the concept of dynamic program and to see how the principles of recursion works. We will motivate Dynamic Programming through the change making problem. The objective is to determine the smallest number of coins (of particular denomination) required to make change for a given amount. For example, if the denomination of the coins are \$1 and \$2 and it was required to make change for \$3 then we would use \$1 + \$2 i.e. 2 coins. However if the amount was \$4 then we would could either use \$1+\$1+\$1+\$1 or \$1+\$1+\$2 or \$2+\$2 and the minimum number of coins would 2 (\$2+\$2). We can come to the solution by understand ing the fact, that the mininum number of coins required to make change for \$P is the number of coins required to make change for the amount \$P-x plus 1 (+1 because we need another coin to get us from \$P-x to P). These can be illustrated mathematically as : 

Let us assume that we have $n$ coins of distinct denomination. Where the denomination of coin $i$ is $v_i$. We can sort the coins according to denomination values such that $v_1<v_2<v_3<..<v_n$

Let us use $C(p)$ to denote the minimum number of coins required to make change for $ \$p$ 

Using the principles of recursion $C(p)=min_i C(p-v_i)+1$


For example, assume we want to make 5 cents, and $v_1=1, v_2=2, v_3=3$. Therefore $C(5) = min(C(5-1)+1, C(5-2)+1, C(5-3)+1)$  
$\Longrightarrow min(C(4)+1, C(3)+1, C(2)+1)$

### 2. Levenshtein Distance, cost of substitution = 2

In the lectures we saw that we can play with the cost of substitution. In other words, changing a letter in a word is more expensive than shifting its position. The `edit_distance` function in `nltk.metrics.distance` assumes a substitution cost of 1. In this excercise we will use dynamic program and change the cost of substitution. The idea is to start from:

```python
def levenshtein(s1, s2, cost_sub): ## creating a function that takes two words and a cost of substitution
    if len(s1) < len(s2): ## if one word is shorter than the other then change the order (book keeping to be consistent)
        return levenshtein(s2, s1, cost_sub)
 
    # len(s1) >= len(s2)
    if len(s2) == 0: ##another check to make sure we are getting a real word, 
        ##if we are not getting a real word the cost is simply dropping all the letters in one of the words i.e. the length
        
        return len(s1)
 
    previous_row = range(len(s2) + 1) ##initialization ; creating an array of length of the second word+1
    for i in range(len(s1)): ## going through each element of the first word 
        c1=s1[i] ## the particular letter being considered 
        current_row = [i + 1]
        for j in range(len(s2)):
            c2=s2[j]
            insertions = previous_row[j + 1] + 1 
            ##WRITE CODE TO DETEMINE DELETIONS     
            ##WRITE CODE TO DETEMINE SUBSTITUTION
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
 
    return previous_row[-1]
```

```python
levenshtein('intention', 'execution', cost_sub=2)
```
    ##OUTPUT 
    8