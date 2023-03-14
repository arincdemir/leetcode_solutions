# leetcode_solutions
My notes on how I solved some leetcode questions. I am hoping that this file will help me go over these questions before attending an interview. I have also shared the python codes I used to solve these questions.

### 109. Convert Sorted List to Binary Search Tree
Use a function to find the mid of the linked list and put it into a root node. Use this function recursively in order to get the root.right and root.left. Find the mid with a function using slow and fast pointers.

### 433. Genetic Mutation
Create an adjacency list and put neighboring (ones with only 1 nucleotite difference) genes in it. Then run a bfs starting with the startGene until you arrive at the endGene. If the loop terminates, then it is impossible reaching the endGene.

### 901. Online Stock Span
The naive approach to search backwards each time is too slow. So next to each price, I store the closest point that price was exceeded. After that we move from pointer to pointer, until we reach a point where the price is larger than the target. This way we skip looking at each price.

### 2008. Maximum Earnings From Taxi
Very interesting dp question. First need to create a dict that stores the rides that start on each spot. Then use dp to evaluate the two choices: Skip the spot or take the passenger thats on the spot.
