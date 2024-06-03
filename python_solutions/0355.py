from typing import *
from heapq import *


class Twitter:

    def __init__(self):
        self.followers = {}
        self.feeds = {}
        self.tweets = {}
        self.time = 0

    def initialize(self, userId):
        if userId not in self.followers:
            self.followers[userId] = set([userId])
        if userId not in self.feeds:
            self.feeds[userId] = []
        if userId not in self.tweets:
            self.tweets[userId] = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.initialize(userId)
        self.tweets[userId].append((self.time, tweetId, userId))
        for follower in self.followers[userId]:
            heappush(self.feeds[follower], (self.time, tweetId, userId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.initialize(userId)
        feed = self.feeds[userId]
        first10 = []
        i = 0
        while feed and i < 10:
            tweet = heappop(feed)
            if userId in self.followers[tweet[2]]:
                first10.append(tweet)
                i += 1
        for tweet in first10:
            heappush(feed, tweet)
        ans = [tweet[1] for tweet in first10]
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.initialize(followerId)
        self.initialize(followeeId)
        if followerId not in self.followers[followeeId]:
            self.followers[followeeId].add(followerId)
            feed = self.feeds[followerId]
            for tweet in self.tweets[followeeId]:
                heappush(feed, tweet)

            

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.initialize(followerId)
        self.initialize(followeeId)
        if followerId in self.followers[followeeId]:
            self.followers[followeeId].remove(followerId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)