class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = {}
        for x in paths:
            x = x.split()          
            folder = x[0]
          
            for file in x[1:]:
                name = file[:file.index("(")]
                content = file[file.index("(") + 1:-1]
                if content not in d:
                    d[content] = []
                d[content].append(folder + "/" + name)

        ans = []
        for group in d.values():
            if len(group) > 1:
                ans.append(group)

        return ans
