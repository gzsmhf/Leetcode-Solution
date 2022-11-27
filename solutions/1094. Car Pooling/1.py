'''
Runtime: 60 ms, faster than 95.94% of Python3 online submissions for Car Pooling.
Memory Usage: 15 MB, less than 18.85% of Python3 online submissions for Car Pooling.
'''

from collections import defaultdict

class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        '''
        遍历trips将车站和上车/下车的人数存入dict中，再对该dict遍历累加人数看是否超出capacity
        '''
        
        car_pooling = defaultdict(int)
        for t in trips:
            car_pooling[t[1]] += t[0]
            car_pooling[t[2]] -= t[0]
        num_passengers = 0
        for i in sorted(car_pooling.keys()):
            num_passengers += car_pooling[i]
            if num_passengers > capacity:
                return False
        return True