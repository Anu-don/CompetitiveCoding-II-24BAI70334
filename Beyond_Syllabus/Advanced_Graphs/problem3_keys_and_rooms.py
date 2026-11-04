"""
Beyond Syllabus (Advanced Graphs) - Problem 3: Keys and Rooms
Link: https://leetcode.com/problems/keys-and-rooms/

rooms[i] holds the keys found in room i. Starting in room 0, a room can be
entered only if you have its key. Return True if every room can be visited.

Approach: graph reachability - DFS from room 0 and check that all rooms are seen.
Time: O(V + E)   Space: O(V)
"""
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = {0}
        stack = [0]
        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if key not in seen:
                    seen.add(key)
                    stack.append(key)
        return len(seen) == len(rooms)


if __name__ == "__main__":
    s = Solution()
    assert s.canVisitAllRooms([[1], [2], [3], []]) is True
    assert s.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]) is False
    print("All tests passed")
