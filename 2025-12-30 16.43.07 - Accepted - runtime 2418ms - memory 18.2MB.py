class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Sort points by x-coordinate ascending, then by y-coordinate descending
        points.sort(key=lambda p: (p[0], -p[1]))
        
        count = 0
        n = len(points)
        
        for i in range(n):
            # Alice is at points[i] (upper-left corner)
            alice_x, alice_y = points[i]
            
            # Track the maximum y seen for Bob candidates
            max_y = float('-inf')
            
            for j in range(i + 1, n):
                bob_x, bob_y = points[j]
                
                # Bob must be at lower-right corner
                # So bob_x >= alice_x (already satisfied by sorting)
                # And bob_y <= alice_y
                if bob_y <= alice_y:
                    # Check if no point is strictly inside the fence
                    # A point is inside if: alice_x < x < bob_x and bob_y < y < alice_y
                    # Or on the boundary but not at corners
                    # Since we sorted by x, all points between i and j have x >= alice_x
                    # We need to check if bob_y is greater than max_y seen so far
                    # If bob_y > max_y, then there's no point between Alice and Bob
                    if bob_y > max_y:
                        count += 1
                    max_y = max(max_y, bob_y)
        
        return count