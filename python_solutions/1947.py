from typing import *
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        def findCompatibility (a, b):
            compatibility = 0
            for i in range(len(a)):
                if a[i] == b[i]:
                    compatibility += 1
            return compatibility

        mentorsCompatibility = []
        for mentor in mentors:
            compatibilities = []
            for student in students:
                compatibilities.append(findCompatibility(mentor, student))
            mentorsCompatibility.append(compatibilities)
        
        maxScore = 0
        def processPermutation(array):
            score = 0
            for i in range(len(array)):
                score += mentorsCompatibility[i][array[i]]
            nonlocal maxScore
            maxScore = max(score, maxScore)

        def swap(array, i, j):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

        def permutations(array, i):
            if i == len(array):
                processPermutation(array)
                return
            for j in range(i, len(array)):
                swap(array, i, j)
                permutations(array, i + 1)
                swap(array, i, j)
            
        permutations([i for i in range(len(mentors))], 0)
        return maxScore

            
    