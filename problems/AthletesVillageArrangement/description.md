# Athletes' Village Arrangement

You are in charge of arranging a ring-shaped athletes' village for countries joining the summer game. Each country has their preference of who they want to be neighbors with.

# Input

This input will consist of a positive integer n, indicating the number of countries. Next will follow 2 \* n lines. Every two lines will be in the format of:

```
finland
australia japan kenya
```

representing finland is happy to be neighbors with australia, japan, and kenya.

Here's an example input:

```
4
finland
australia japan kenya
japan
kenya finland australia
australia
japan kenya
kenya
finland australia
```

# Constraints

- Each country is represented by a unique name
- Each country name consists of only lower case letters
- Every country has their preference of at least two other countries they want to be neighbors with

# Output

Your output should be true or false depending on if there is at least one arrangement where every country stays next to two countries they are willing to be neighbors with.

Here is the output for the example given above:

```
true
```

### Explanation:

In the above example, one possible arrangement is:

```
finland - japan - australia - kenya
```

Note that because it is a ring-shaped athletes' village, in the above example, kenya and finland should also be willing to stay next to each other.

# Examples

The first 2 test cases are examples.
