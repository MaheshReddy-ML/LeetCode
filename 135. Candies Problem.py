

class Solution(object):
    def candy(self, ratings):
        """
        Distribute candies to children based on their ratings.

        Each child must get at least one candy.
        Children with a higher rating than their immediate neighbors must get more candies.

        This implementation uses a greedy approach with two passes:
        - A forward pass to ensure the left neighbor condition.
        - A backward pass to ensure the right neighbor condition.

        Time Complexity: O(n)
        Space Complexity: O(n)

        :type ratings: List[int] - A list of integers representing children's ratings.
        :rtype: int - The minimum total number of candies needed.
        """
        candies = [1] * len(ratings)

        # Forward pass: Ensure right child gets more if rating is higher than left
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Backward pass: Ensure left child gets more if rating is higher than right
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candies[j] = max(candies[j], candies[j + 1] + 1)

        return sum(candies)
