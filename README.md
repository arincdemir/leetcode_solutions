# leetcode_solutions
My notes on how I solved some leetcode questions. I am hoping that this file will help me go over these questions before attending an interview. I have also shared the python codes I used to solve these questions.

### 433. Genetic Mutation
Create an adjacency list and put neighboring (ones with only 1 nucleotite difference) genes in it. Then run a bfs starting with the startGene until you arrive at the endGene. If the loop terminates, then it is impossible reaching the endGene.
