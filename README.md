# leetcode_solutions
My notes on how I solved some leetcode questions. I am hoping that this file will help me go over these questions before attending an interview. I have also shared the python codes I used to solve these questions.

### 109. Convert Sorted List to Binary Search Tree
Use a function to find the mid of the linked list and put it into a root node. Use this function recursively in order to get the root.right and root.left. Find the mid with a function using slow and fast pointers.

### 433. Genetic Mutation
Create an adjacency list and put neighboring (ones with only 1 nucleotite difference) genes in it. Then run a bfs starting with the startGene until you arrive at the endGene. If the loop terminates, then it is impossible reaching the endGene.

### 2008. Maximum Earnings From Taxi
Very interesting dp question. First need to create a dict that stores the rides that start on each spot. Then use dp to evaluate the two choices: Skip the spot or take the passenger thats on the spot.
