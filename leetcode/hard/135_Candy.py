class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        # at least one for each
        candies = [1] * n
        
        # rating value map
        rating_map = {}
        for i, r in enumerate(ratings):
            if r not in rating_map:
                rating_map[r] = []
            rating_map[r].append(i)
        
        # from lowest to highest
        for r in sorted(rating_map.keys()):
            for i in rating_map[r]:
                # see if neighbors is lagrer (LEFT)
                if i > 0 and ratings[i] > ratings[i - 1]:
                    candies[i] = max(candies[i], candies[i - 1] + 1)
                # see if neighbors is lagrer (RIGHT)
                if i < n - 1 and ratings[i] > ratings[i + 1]:
                    candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)