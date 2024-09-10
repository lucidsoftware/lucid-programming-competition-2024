# Lucid Programming Competition 2024

## Adding a Problem
Create a new folder for your problem, as in `problems/yourProblemName`

Inside of the `yourProblemName` folder, you should create two new folders called `solutions` and `tests`.

### Solutions Folder

The `solutions` folder should contain the source code for any solutions to the problem.

Typically we create a folder for each language (so you might have a `solutions/python3/` folder or a `solutions/typescript/` folder).

Also inside the `solutions` folder are one or more `.run` files. This is simply a bash script that executes one of the solutions. For example, if you had a Python 3 solution inside of `solutions/python3/main.py`, you could add a file named `solutions/python3.run` with the following contents:

```
#!/bin/bash
python3 $(dirname $0)/python3/main.py
```
> Note: You must mark the `.run` file as executable (as in `chmod +x python3.run`) or else you will get a permission denied problem when trying to run the tests.

### Tests Folder

Your input and expected outputs should go inside of the `tests` folder. The files inside this folder must follow a specific naming pattern. For inputs, you should name them with a number as the base name with `.in` as the extension, as in `0.in`, `1.in`, `2.in`, etc. Similarly, for the corresponding expected output file, you should use numbers as the base name with `.out` as the extension (as in `0.out`, `1.out`, `2.out`, etc).

### description.md

* Please refer to the `Problem Template` page in Confluence (link bookmarked in our channel Slack) for the most up to date instructions.

## Running Tests

To run the tests for a problem, run this fancy `make` command from the root of the repo.

```
make test-yourProblemName
```

This will run your `.run` program against each pair of inputs and outputs. You may have to install the `colordiff` program to have that work.

On Ubuntu, something like this:
```
sudo apt-get install colordiff
```
On Fedora/RHEL, something like this:
```
sudo dnf install colordiff
```
On Windows or Mac, I have no foggy clue how to install colordiff. If anyone cares, feel free to add a page for that.


## Generating the test cases zip

To generate the zip files for all problems in the HackerRank testcases.zip format, run this `make` command from the root of the repo. The created zip files can be found under `<repo root>/zips`

```
make zip
```