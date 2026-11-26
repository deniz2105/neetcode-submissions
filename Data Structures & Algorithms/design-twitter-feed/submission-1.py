class Twitter:

    def __init__(self):
        self.follows = defaultdict(list)
        self.tweets = defaultdict(list)
        self.counter = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.counter))
        self.counter+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        pointers = []
        if len(self.tweets[userId]) > 0:
            heapq.heappush(pointers,(-self.tweets[userId][-1][1], len(self.tweets[userId])-1, userId))
        for followed in self.follows[userId]:
            if len(self.tweets[followed]) > 0:
                heapq.heappush(pointers, (-self.tweets[followed][-1][1],len(self.tweets[followed])-1, followed))
        resp = []
        while pointers and len(resp) < 10:
            _, idx, user = heapq.heappop(pointers)
            if idx -1 >= 0:
                heapq.heappush(pointers, (-self.tweets[user][idx-1][1],idx-1, user))
            
            resp.append(self.tweets[user][idx][0])
        return resp
        

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in set(self.follows[followerId]):
            self.follows[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in set(self.follows[followerId]):
            self.follows[followerId].remove(followeeId)
        
