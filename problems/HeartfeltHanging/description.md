# Heartfelt Hanging

Coach Erika is a world-renowned gymnast, and now she shares her talents with other budding athletes through personal training. After training with Coach Erika, an athlete's score on the Globally Accepted Universal Gymnast Judgement Exam (GAUGE) improvements. Each December, she accepts very detailed applications. She believes in philosophical utilitarianism, meaning that she wants to do the most good for the most people. It's your job to help her take advantage of her limited training time, and decide which athletes are worth training this season.

# Input

1. The first line of input is $S$, the number of available training sessions that Coach Erika can teach this season.
2. The second line is $A$, the number of athletes who have applied for coaching.
3. The third line shows the number of sessions Coach Erika would allocate to each athlete $X_a$.

   - `<athlete 1's training time> <athlete 2's training time> ... <athlete n's training time>`

4. The fourth line shows the number of points on the GAUGE that each athlete would improve $Y_a$.

   - `<athlete 1's score improvement> <athlete 2's score improvement> ... <athlete n's score improvement>`

# Constraints

- The number of available training sessions is between $1 \leq S \leq 10^6$
- The number of athlete applicants is between is between $1 \leq A \leq 10^5$
- Coach Erika may choose to train none, some, or all of the applicants, so long as the sum of their trainings $\sum X_b$ does not exceed her available sessions $S$.
- Coach Erika will not partially train any athlete.
- Each training session is one-on-one. Athletes do not share the coach's time.

# Output

Output the maximum sum of GAUGE score improvements that Coach Erika could facilitate by her coaching.

Notice you do not report which athletes she will train.

# Examples

The first 3 test cases are examples.
