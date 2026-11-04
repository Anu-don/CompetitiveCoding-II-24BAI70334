"""
Beyond Syllabus (Disjoint Set Union) - Problem 2: Accounts Merge
Link: https://leetcode.com/problems/accounts-merge/

Given a list of accounts (name followed by emails), merge accounts that share at
least one email. Return each person's account as the name followed by all unique
emails in sorted order (order of accounts does not matter).

Approach: union-find over emails. Every email in an account is united with the
account's first email; then group emails by their root.
Time: O(N log N) for sorting, N = total emails   Space: O(N)
"""
from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        owner = {}

        def find(x: str) -> str:
            parent.setdefault(x, x)
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for acc in accounts:
            name, first = acc[0], acc[1]
            for email in acc[1:]:
                owner[email] = name
                parent[find(email)] = find(first)

        groups = defaultdict(list)
        for email in list(parent):
            groups[find(email)].append(email)
        return [[owner[root]] + sorted(emails) for root, emails in groups.items()]


if __name__ == "__main__":
    s = Solution()
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    out = s.accountsMerge(accounts)
    expected = [
        ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    assert sorted(out) == sorted(expected)
    print("All tests passed")
