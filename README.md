# CMPS 2200  Recitation 01

**Name (Team Member 1):**_Sam Cohen ________________________  
**Name (Team Member 2):**__Andrew Zimmerman _______________________

In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for collaborative coding.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`. All tests are in `test_main.py`.

## Install Python Dependency

We need Python library of "tabulate" to visualize the results in a good shape. Please install it by running 'pip install tabulate' or 'pip install -r requirements.txt' in Shell Tab of Repl.  

## Running and testing your code

- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

`Binary Search`: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

- [ ] 1. In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`. 

- [ ] 2. Test that your function is correct by calling from the command-line `pytest test_main.py::test_binary_search`

- [ ] 3. Write at least two additional test cases in `test_binary_search` and confirm they pass.

- [ ] 4. Describe the worst case input value of `key` for `linear_search`? for `binary_search`? 

**TODO: your answer goes here**

The worst case input value of key for linear search is when the element is in the last position of the list or not present at all.
The worst case input value of key for binary search is when the element is either in the first position, last position, or not present at all.
- [ ] 5. Describe the best case input value of `key` for `linear_search`? for `binary_search`?

**TODO: your answer goes here**
The best case input value of key for linear search is when the element is in the first position of the list.
The best case input value of key for binary search is when the element is exactly in the middle position of the list.

- [ ] 6. Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.

- [ ] 7. Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest test_main.py::test_compare_search`, which contains some simple checks.

- [ ] 8. Call `print_results(compare_search())` and paste the results here:

**TODO: add your timing results here**
 n |   linear |   binary |
|----------|----------|----------|
|       10 |    0.006 |    0.010 |
|      100 |    0.009 |    0.005 |
|     1000 |    0.127 |    0.009 |
|    10000 |    5.877 |    0.043 |
|   100000 |   41.804 |    0.034 |
|  1000000 |  138.645 |    0.033 |
| 10000000 | 2617.197 |    0.060 |

- [ ] 9. The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. Do these theoretical running times match your empirical results? Why or why not?
**TODO: your answer goes here**
As expected the running time of linear search increases linearaly as the size of the list increases.
The running time of binary search remains relatively constant even as the size of the list increases exponentially. This aligns with the O(log2(n)) complexity, where the running time grows logarithmically with the size of the list.

- [ ] 10. Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. Suppose you know ahead of time that you will search the same list $k$ times. 
  + What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search? ** Worst case time complexity: O(n). Since searching the list k times, overall worst case would be O(kn)**
  + For binary search? **O(log n + kn^2)**
  + For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting? **Therefore, for any positive value of k, it is more efficient to first sort and then use binary search when n is sufficiently large**
    
  
