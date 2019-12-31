
# Pair Matching Problem

  

- Input: **Distinct** Rational Numbers between 0 and 1 (inclusive).

- For every such rational number x_i, the algorithm looks for j in 1,2,...n and then assigns **R** (reject) and **A** (accept), on the basis of following:

  

![enter image description here](https://i.imgur.com/ywT84HO.png)

  

- This is an online problem in the sense that, the input is received in sequential manner and the algorithm has to take irrevocable decisions.

- Hence, there will be cases when online algorithm makes wrong decisions.

# Deterministic Online Algorithm
The deterministic case is straightforward. 

 - When an item x is encountered, we try to match it with all the items y received before that item. If we find such a y, we assign 'A' to x, else 'R'.
 - Note that, in the case when we assigned 'A' to x,  y must have been assigned 'R' before. We cannot change y's assignment because online algorithms cannot revoke their decisions. So, the algorithm took wrong decision for y. 
  

# Randomized Online Algorithm
In randomized algorithm,

 - 2/3 is the probability that the algorithm will assign 'R' to a non-matching value.
 - This number is proved to give a better competitive ratio than the deterministic case in the paper listed in references. 
 - We generate the randomized output on the fly as well taking irrevocable decisions.
 - For larger length sequences, the "expected" number of wrong decisions made by randomized scenario is less than the number of wrong decisions made by deterministic scenario.
 - Check the function randomized_online() for details.

  # Offline Algorithm 
  

 - Once, the user presses 'E' for exit, we have the entire list now, which becomes an offline case. 
 - We then find the correct results by offline algorithm (see offline()).
 - The number of wrong decisions taken by both deterministic and randomized algorithm are also returned by comparing with corresponding decisions taken by offline algorithm.

# References

  

The python code is an implementation of the problem introduced in the research paper "Advice Complexity of Priority Algorithms" by Allan Borodin, Joan Boyar, Kim S. Larsen and Denis Pankratov. Their paper can be accessed here: [https://arxiv.org/abs/1806.06223](https://arxiv.org/abs/1806.06223)
  
