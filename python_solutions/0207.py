from typing import *


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursesPrerequisites = {i: set() for i in range(numCourses)}
        coursesFollowings = {i: set() for i in range(numCourses)}

        for pre in prerequisites:
            if pre[0] not in coursesPrerequisites:
                coursesPrerequisites[pre[0]] = set([pre[1]])
            else:
                coursesPrerequisites[pre[0]].add(pre[1])
            
            if pre[1] not in coursesFollowings:
                coursesFollowings[pre[1]] = set([pre[0]])
            else:
                coursesFollowings[pre[1]].add(pre[0])

        
        firstToRemove = []
        for course, pres in coursesPrerequisites.items():
            if len(pres) == 0:
                firstToRemove.append(course)
        
        while len(coursesFollowings) > 0 and len(firstToRemove) > 0:
            newToRemove = []
            for removal in firstToRemove:
                followings = coursesFollowings[removal]
                for fol in followings:
                    coursesPrerequisites[fol].remove(removal)
                    if len(coursesPrerequisites[fol]) == 0:
                        newToRemove.append(fol)
                coursesPrerequisites.pop(removal)
                coursesFollowings.pop(removal)
            
            firstToRemove = newToRemove
        
        if len(coursesFollowings) == 0:
            return True
        else:
            return False
            

        