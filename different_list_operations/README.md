# Different List Operations

Consider a list `(list = [])`. You can perform the following commands:

* `insert i e`: Insert integer `e` at position `i`.
* `print`: Print the list.
* `remove e`: Delete the first occurrence of integer `e`.
* `append e`: Insert integer `e` at the end of the list.
* `sort`: Sort the list.
* `pop`: Pop the last element from the list.
* `reverse`: Reverse the list.

Initialize your list and read in the value of `n` followed by `n` lines of commands where each command will be 
of the 7 types listed above.
Iterate through each command in order and perform the corresponding operation on your list.

**Example**
```
N = 4
append 1
append 2
insert 3 1
print
```

- Append 1 to the list, arr = [1].
- Append 2 to the list, arr = [1, 2].
- Insert 3 at index 1 , arr = [1, 3, 2].
- Print the array.

Output:
`[1, 3, 2]`

- Input Format

The first line contains an integer `n` denoting the number of commands.
Each line `i` of the `n` subsequent lines contains one of the commands described above.

- Constraints

The elements added to the list must be integers.

- Output Format

For each command of type print, print the list on a new line.
