# Number Triangle Patterns

This simple yet elegant Python program prints a **Mirrored Number Pyramid** using **nested loops**, **loop control**, and **sequence formatting**. It's a great practice for beginners to understand the flow of nested loops and console output alignment.

- An **Increasing Sequence Triangle** 
<pre>
1
12
123
1234
</pre>
- A **Repeating Row Number Triangle**
<pre>
1
22
333
4444
</pre>

These two pyramids are separated by spaces, creating a clean and symmetrical mirrored effect.

## Sample Output for input `5`
<pre>
1                 1
1 2             2 2
1 2 3         3 3 3
1 2 3 4     4 4 4 4
1 2 3 4 5 5 5 5 5 5
</pre>

## How It Works
- The **left half** of each row uses a loop to print `1` to `i`.
- The **right half** uses a loop to print the row number `i` repeated.
- Double spaces are printed in between to maintain symmetry.
