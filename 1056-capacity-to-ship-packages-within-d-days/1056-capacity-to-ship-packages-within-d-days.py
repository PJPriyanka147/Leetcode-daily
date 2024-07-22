class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(weights: List[int], days: int, capacity: int) -> bool:
            current_weight = 0
            day_count = 1
            
            for weight in weights:
                if current_weight + weight > capacity:
                    day_count += 1
                    current_weight = 0
                current_weight  += weight

                if day_count > days:
                    return False
            return True

        min_capacity = max(weights)
        max_capacity = sum(weights)

        left, right = min_capacity, max_capacity

        while left < right:
            mid = (left + right) // 2

            if canShip(weights, days, mid):
                right = mid
            else:
                left = mid + 1
        
        return left