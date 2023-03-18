# leetcode_solutions
My notes on how I solved some leetcode questions. I am hoping that this file will help me go over these questions before attending an interview. I have also included the python codes I used to solve these questions.

### 109. Convert Sorted List to Binary Search Tree
Use a function to find the mid of the linked list and put it into a root node. Use this function recursively in order to get the root.right and root.left. Find the mid with a function using slow and fast pointers.

### 382. Linked List Random Node
I planned to generate a random index using a random function. However, reaching that index in a linked list is O(n). To solve this, I transformed the linked list into a list, allowing O(1) index access.

### 433. Genetic Mutation
Create an adjacency list and put neighboring (ones with only 1 nucleotite difference) genes in it. Then run a bfs starting with the startGene until you arrive at the endGene. If the loop terminates, then it is impossible reaching the endGene.

### 795. Number of Subarrays with Bounded Maximum
Hold two pointers: l and r. l holds the leftmost index where a valid substring can be formed. Looping over all the elements, there are 3 main cases:
- nums[i] is bigger than the bound: In this case, it is impossible to form a valid substring with this index. So update l as i + 1.
- nums[i] is in the bound: We can update r as i and increment coun by r - l + 1 since that is how many substrings we can form with nums[i] being the rightmost element.
- nums[i] is smaller than the bound: We leave r and l where they are since it does not guarantee a substring can be formed but it does not guarantee that it cannot be formed either. Increment count by r - l + 1 since r is the last position a number inside the bound has been seen, and we can only form a valid substring when we include it.

### 870. Advantage Shuffle
In this question we want to match the smallest number from num1 that is greater than the number from num2. In order to do that efficiently, I first sorted num1 and num2, with also keeping the index positions of num2. After that I used 2 pointers to traverse the arrays.

### 901. Online Stock Span
The naive approach to search backwards each time is too slow. So next to each price, I store the closest point that price was exceeded. After that we move from pointer to pointer, until we reach a point where the price is larger than the target. This way we skip looking at each price.

### 1138. Alphabet Board Path
The first intuition is to do a bfs on a connected graph. However, since we know where each letter is on the table, we can store the locations in a hashmap. Then we can easily calculate our movements by `movement = map[character] - curLocation`.

### 1267. Count Servers that Communicate
For this question, initialize 2 arrays named rows and colums. In these arrays we will count how many servers are in each row and each column. Do a double for loop for updating these arrays and increment the row and the column of the found server. After that, for each server in a row and column, if the respective row in rows is bigger than 1 (meaning there is more than one server in that row) or the column is bigger than one, increment the answer.

### 1339. Maximum Product of Splitted Binary Tree
Since the sum of all the tree is constant, in order to maximize the product, we want to make the splits as close as to half of the sum. First I find the sum of all subtrees and put them into a list. Then I find the closes split to half of the total sum using a for loop on sums list.

### 1849. Splitting a String Into Descending Consecutive Values
I used a recursive function `canFormValidSplit` that takes two arguments: `currentString` and `value`. It tries slicing `currentString` into two pieces. The leftmost piece has to be equal to `value - 1`. If so, it calls itself with the right side of `currentString` and `value - 1`.

### 1947. Maximum Compatibility Score Sum
First I calculated the compability score of each mentor with each student since this will be accesed many times in the future. Then I generate all the permutations using a backtracking recursive function. I calculated the compability score of the permutations and returned the maximum one.

### 2008. Maximum Earnings From Taxi
Very interesting dp question. First need to create a dict that stores the rides that start on each spot. Then use dp to evaluate the two choices: Skip the spot or take the passenger thats on the spot.

### 2271. Maximum White Tiles Covered by a Carpet
Intuitively, this question screams that it can be solved with a sliding window technique. However, implementing the actual solution is very tricky in my opinion. So I start with sorting the tiles and declaring the variables `left`, `right` and `windowSize`. While left and right are smaller than the length of `tiles`, we will do one of the two operations:
- If `tiles[right][1] < tiles[left][0]` which means that we can include the `right` tile as a whole, we increase the window size by the size of the `right` tile. After that, we increase `right` by one.
- Else, we cannot include the `right` tile as a whole, so we add the partial area to our window length. Then, we increase `left` by one since our window is now bigger than the carpet size.

### 2279. Maximum Bags With Full Capacity of Rocks
The intuition is that we always want to put the rocks into the bag that needs the least amount to get full capacity. So I created list `empty`, which has the empty spots in each bag. We always want to pick the smallest element from that list, so using a heap is a great idea here. I formed a heap out of `empty` and picked the smallest elements in a while loop.
