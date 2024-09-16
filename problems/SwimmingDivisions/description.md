# Swimming divisions
We've planned to host a lot of swimming competitions. And I mean, a LOT. However, someone forgot to create divisions for these competitions!

To overcome this issue, the summer games committee made a division for each competitor - so each competitor starts out in their own division.

When a competition takes place, **the divisions of everyone competing now combine to become one division**.

For example, assume:
- Alice, Bob, and Charlie are part of Division 1
- David, Emily are part of Division 2
- Frank, Grace are part of Division 3

If Alice, David, and Frank compete in a competition, all 7 competitors now belong to a new "Division 4". If there is another competition within these 7 people, no division changes occur, as they were already part of the same division.

As you may have realized, these swimming competitions are a bit weird. Not only do the competitors' divisions combine, but **each competition has exactly one winner, and the rest are losers**.

When a winner of a competition is announced, they are said to be **top-ranked** in their division, at that time. As soon as someone else in this same division wins, they will be top-ranked.

You will be given all the competition data, in chronological order. In between these events, competitors will ask for who is top-ranked in their division, **at that moment in time**. Your job is to tell them who it is.

# Input
The input starts with the integer $N$ (number of competitors). $N$ lines follow, with the names of each competitor on each line (competitor names only consist of the lowercase alphabet, a-z).
<br>
Following the names, the rest of the input happens in chronological order. One of the 3 events occurs:
1.  A competition takes place, in which the input is:
    - A line `COMPETITION [M]` where $M$ is an integer denoting the number of participants in this competition
    - $M$ lines follow with the names of the participants of this competition on each line. The first name is the winner, all the others are losers, in no particular order.
2. A participant requests who the top-ranker is in their division, **at this point in time**
    - A single line with the string `REQUEST [name]` where `name` is the competitor who made the request.
3. The swimming competitions end. A single line with the word `END`, denoting there is no more input to be expected.

## Example input
```
10
alice
bob
charlie
diana
emily
frank
grace
harry
isabella
jack
COMPETITION 4
alice
bob
charlie
diana
REQUEST charlie
COMPETITION 3
bob
charlie
diana
REQUEST alice
COMPETITION 3
jack
harry
isabella
COMPETITION 4
alice
charlie
emily
bob
REQUEST harry
COMPETITION 2
diana
harry
REQUEST jack
END
```
## Constraints
- $N \leq 10^5$
- The total number of requests will be at most $10^6$
- The sum of all competition sizes (i.e. number of competitors for each competition) is at most $10^7$
- Requests will only be made by people who have previously competed in a competition at some point

# Output
On each line, output the response to each request (i.e. the name of the top-ranked competitor in the requestor's division **at the moment of the request**).

The answer to the example input is:
```
alice
bob
jack
diana
```
### Explanation
We will shorten the names to the first letter for this explanation for brevity.

- First, `a, b, c, d` compete, and `a` wins. They now belong to one division.
- `c` requests who is top-ranked in their division, who is `a`, who was the last winner.
- `b, c, d` compete. `b` is now top-ranked in `a, b, c, d`'s division.
- `a` requests. The answer is `b`.
- `j, h, i` compete. They now belong to one division.
- `a, c, e, b` compete. They've been part of one division. `a` is now top-ranked in this division.
- `h` requests for their top-ranker, who is `j`. At this moment in time, `j` is the top-ranker of the division containing `j, h, i`.
- `d, h` compete. This means that the division that both `d` and `h` belong to, combine into one. Now, `a, b, c, d, e, f, g, h, i, j` are all in one division. And `d` is now top-ranked in this division.
- `j` requests for their top-ranker. This is `d`.
