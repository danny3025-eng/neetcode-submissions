from collections import defaultdict  # Import defaultdict to initialize empty lists/sets automatically
import heapq  # Import heapq to maintain a min-heap for getting the most recent tweets
from typing import List  # Import List for type hinting return values


class Twitter:

    def __init__(self):
        self.count = 0  # Global timestamp counter; decrements so newer tweets have smaller (more negative) values
        self.tweetMap = defaultdict(list)  # Maps userId -> list of [count, tweetId] pairs in chronological order
        self.followMap = defaultdict(set)  # Maps followerId -> set of followeeIds they follow

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])  # Append the tweet with its current timestamp to the user's list
        self.count -= 1  # Decrement counter so the next tweet has a smaller value (higher priority in a min-heap)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []  # List to store up to 10 most recent tweetIds for the news feed
        minHeap = []  # Min-heap to merge tweets from all followees, ordered by most recent (smallest count)

        self.followMap[userId].add(userId)  # Ensure the user follows themselves so their own tweets appear in their feed
        for followeeId in self.followMap[userId]:  # Iterate through everyone the user follows (including themselves)
            if followeeId in self.tweetMap:  # Check if this followee has posted any tweets
                index = len(self.tweetMap[followeeId]) - 1  # Get the index of this followee's most recent tweet
                count, tweetId = self.tweetMap[followeeId][index]  # Retrieve the timestamp and ID of that latest tweet
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])  # Push tweet data and next older index onto heap

        while minHeap and len(res) < 10:  # Continue until the heap is empty or we have collected 10 tweets
            count, tweetId, followeeId, index = heapq.heappop(minHeap)  # Pop the most recent tweet across all followees
            res.append(tweetId)  # Add the tweetId to the final news feed result
            if index >= 0:  # Check if this followee has any older tweets left to process
                count, tweetId = self.tweetMap[followeeId][index]  # Fetch the followee's next older tweet
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])  # Push that older tweet onto the heap
        return res  # Return the list of up to 10 most recent tweetIds

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)  # Add followeeId to the follower's set of followed users

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:  # Check if the follower actually follows the followee
            self.followMap[followerId].remove(followeeId)  # Remove followeeId from the follower's set
