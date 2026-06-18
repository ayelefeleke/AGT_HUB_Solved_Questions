class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []

        for i, x in enumerate(list1):
            for j, y in enumerate(list2):
                if x == y:
                    ans.append((i + j, x))
        ans.sort()
        best = ans[0][0]
        return [x for s, x in ans if s == best]
