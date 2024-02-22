"""
Title: 933. Number of Recent Calls

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
"""



from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        # Add the current timestamp to the queue
        self.queue.append(t)
        # Remove timestamps that are outside the 3000ms window
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        # Return the size of the queue, which represents the number of valid pings
        return len(self.queue)

# Example usage
recentCounter = RecentCounter()
print(recentCounter.ping(1))    # Output: 1
print(recentCounter.ping(100))  # Output: 2
print(recentCounter.ping(3001)) # Output: 3