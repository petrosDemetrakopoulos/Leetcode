class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt = 0
        for i in xrange(len(items)):
            crn_item = items[i]
            match ruleKey:
                case "type":
                    cnt += 1 if crn_item[0] == ruleValue else 0
                case "color":
                    cnt += 1 if crn_item[1] == ruleValue else 0
                case "name":
                    cnt += 1 if crn_item[2] == ruleValue else 0
        return cnt