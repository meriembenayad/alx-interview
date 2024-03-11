## 0x01 - Lockboxes

### Essential Knowledge

To successfully complete this project, a firm grasp of several fundamental concepts is necessary. These concepts will enable you to devise a solution that can effectively ascertain if all boxes can be unlocked. Here are the concepts and resources that will be vital for this project:

#### Required Concepts:

1. **Lists and List Manipulation**:

   - It’s important to know how to handle lists, including accessing elements, iterating over lists, and dynamically altering lists.
   - [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html "Python Lists (Python Official Documentation)")

2. **Graph Theory Basics**:

   - While not strictly necessary, understanding graph theory (particularly traversal algorithms like Depth-First Search or Breadth-First Search) can greatly assist in solving this problem, as the boxes and keys can be viewed as nodes and edges in a graph.
   - [Graph Theory (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs "Graph Theory (Khan Academy)")

3. **Algorithmic Complexity**:

   - Comprehending the time and space complexity of your solution is crucial, as it can guide you in crafting more efficient algorithms.
   - [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/asymptotic-notation-and-analysis-based-on-input-size-of-algorithms/ "Big O Notation (GeeksforGeeks)")

4. **Recursion**:

   - Certain solutions may necessitate a recursive method to navigate through the boxes and keys.
   - [Recursion in Python (Real Python)](https://realpython.com/python-recursion/ "Recursion in Python (Real Python)")

5. **Queue and Stack**:

   - Proficiency in using queues and stacks is essential if you plan to implement a breadth-first search (BFS) or depth-first search (DFS) algorithm to navigate through the keys and boxes.
   - [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/queue-in-python/ "Python Queue and Stack (GeeksforGeeks)")

6. **Set Operations**:

   - Knowing how to use sets to keep track of visited boxes and available keys can streamline the search process.
   - [Python Sets (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html#sets "Python Sets (Python Official Documentation)")

By studying these concepts and making use of these resources, you’ll be well-prepared to create an efficient solution for this project, applying both your algorithmic thinking and Python programming abilities.

### Supplementary Resource

- [Mock Technical Interview](https://www.youtube.com/watch?feature=shared&v=V8DGdPkBBxg "Mock Technical Interview")

### Tasks

<details>
<summary>0. Lockboxe</summary>

You are presented with `n` locked boxes. Each box is sequentially numbered from `0` to `n - 1` and may contain keys to other boxes.

Develep a method that ascertains if all the boxes can be unlocked.

- Prototype: `def canUnlockAll(boxes)`
- `boxes` is a list of lists
- A key that has the same number as a box unlocks that box
- You can assume all keys will be positive integers
  - There might be keys that do not correspond to any box
- The first box `boxes[0]` is already unlocked
- Return `True` if all boxes can be unlocked, else return `False`

```sh
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

carrie@ubuntu:~/0x01-lockboxes$
```

```sh
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$
```

**File**

- `0-lockboxes.py`
</details>
