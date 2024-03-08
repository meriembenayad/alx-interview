## 0x00. Pascal's Triangle

### Resources:

- [What is Pascal’s triangle](https://www.cuemath.com/algebra/pascals-triangle/ "What is Pascal's triangle")
- [Pascal’s Triangle - Numberphile](https://www.youtube.com/watch?feature=shared&v=0iMtlus-afo "Pascal's Triangle - Numberphile")
- [What are Python Algorithms](https://builtin.com/data-science/python-algorithms "What are Python Algorithms")
- [Mock Technical Interview](https://www.youtube.com/watch?feature=shared&v=1qw5ITr3k9E "Mock Technical Interview")

Develop a function named `pascal_triangle` that takes an integer `n` as its argument. This function should return a list of lists containing integers, which represents the Pascal's triangle up to the nth row.

- If `n <= 0`, the function should return an empty list `[]`.
- It's assumed that `n` will always be an integer.

Here's an example of how you might use this function in a Python script:

```python
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

When you run this script, it will print the Pascal's triangle up to the 5th row, like so:

```shell
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```
