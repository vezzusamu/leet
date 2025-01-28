class Twitter:

    def __init__(self):
        self.last_tweet = []
        self.followed_by_user = {int:List[int]}
        self.tweet_by_user = {int:List[int]}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        ret = self.tweet_by_user.get(userId, [])
        if len(ret) >= 10:
            ret = ret[1:]
        ret.append((-self.time, tweetId))
        self.tweet_by_user[userId] = ret
        #heappush({userId, time})

    def getNewsFeed(self, userId: int) -> List[int]:
        ret_t = []
        max_heap = []
        for u_id in self.followed_by_user.get(userId, [userId]):
            tweets = self.tweet_by_user.get(u_id, [])
            for time, tweet_id in tweets:
                heapq.heappush(max_heap,(time, tweet_id))
        i = 0
        while(max_heap) and i < 10:
            time, tweet = heapq.heappop(max_heap)
            ret_t.append(tweet)
            i += 1
        return ret_t

    def follow(self, followerId: int, followeeId: int) -> None:
        ret = self.followed_by_user.get(followerId, [followerId])
        if followeeId in ret:
            return
        ret.append(followeeId)
        self.followed_by_user[followerId] = ret

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        ret = self.followed_by_user.get(followerId, [followerId])
        ret = [i for i in ret if not i == followeeId]
        if ret == []:
            ret = [followerId]
        self.followed_by_user[followerId] = ret