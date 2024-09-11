# Bouncy Castle Obstacle Course
You have been selected for the great honor of representing your country in the Summer Games Obstacle Course. Which obviously takes place in a bouncy house. The bouncy house is full of various obstacles, all of which you have trained diligently on and you know exactly how many minutes it takes you to complete the obstacle. There are several routes you can take through the maze, so it's up to you before you start to decide the fastest way through the course.

But! The course has been sabotaged by a rival nation! There's a leak in the bouncy house and the air is seeping out, making the bouncy house harder to traverse. For every 10 seconds you are in the obstacle course, each upcoming obstacle will take an additional second to complete. Can you still find your fastest path through the course?

**Important**: Everything is calculated in integers, and new time required is only evaluated for upcoming obstacles after completing an obstacle. If 15 seconds have passed, the time on following obstacles will still only increase by 1 second, not 1.5. If the first obstacle takes 12 seconds to clear, you do not need to add 1 extra second to the time partway through the obstacle.

# Input
The input format consists of a positive integer on a single line representing the number of 'nodes' between obstacles (places where obstacles start and stop), followed by the name of each node on a separate line. The first node listed is where you will begin the race. The final node listed is the one you are trying to reach in the fastest time.
Following the node list, you will receive another integer on a single line representing the number of obstacles connecting nodes, followed by the list of obstacles, describing which two nodes they connect and the integer time in seconds it takes you to clear the obstacle.
```
<number of nodes>
<node 0>
<node 1>
...
<node x>
<number of obstacles>
<node a> <node b> <time 1>
<node c> <node d> <time 2>
...
<node w> <node x> <time y>
```

# Constraints
* The number of nodes will always be between 5 and 10000 (inclusive)
* The number of obstacles will be between 5 and 50000 (inclusive)
* The number of seconds to complete an obstacle will always be between 1 and 50 (inclusive)
* Node names are always lowercase alphanumeric characters, with no spaces (or anything else that isn't alphanumeric)
* There will never be two obstacles that connect the same two nodes.
* There will never be two unique paths that can complete the course in the minimum time.
* There will always be at least one valid path from the start to the finish

# Output
The expected output is the path of nodes you should travel for your fastest time, with one node on each line, and then the number of seconds it will take to complete the course along that route
```
<node name 1>
<node name 2>
<node name 3>
...
<node name x>
<fastest possible time>
```

# Examples
The first 4 test cases are examples.
