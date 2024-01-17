# Advent of Code 2023 ⭐⭐
My [Advent of Code 2023](https://adventofcode.com/2023) puzzles solutions in Python. Most solutions use only Python's standard library, some solutions use external libraries such as numpy, astar, networkx.

After placing your puzzle input in `input.txt`, run any day's solution (both parts except day 25) against your puzzle input.
Either paste your input manually, or use a simple script `fetch_input.py`. If you wish to use the script, copy your session cookie and paste it inside `session_cookie.txt`. For example, after pasting your session cookie, fetch your day 1 puzzle input:
```shell
$ python fetch_input.py session_cookie.txt input.txt -y 2023 -d 1
Accessing: https://adventofcode.com/2023/day/1/input

Success. Writing to input.txt...
Done
```
Then run the day 1 solutions against your input (all solutions assume the input file is `input.txt`):
```shell
$ python day01.py
54605
55429
```

