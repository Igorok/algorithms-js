import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        countByDomain = defaultdict(int)

        for cpdom in cpdomains:
            cnt, domain = cpdom.split(' ')
            cnt = int(cnt)

            domains = domain.split('.')
            for i in range(len(domains)):
                dom = '.'.join(domains[i:])
                countByDomain[dom] += cnt

        res = []
        for key in countByDomain:
            res.append(f'{countByDomain[key]} {key}')

        return res


def test ():
    params = [
        {
            'input': ["9001 discuss.leetcode.com"],
            'output': ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"],
        },
        {
            'input': ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"],
            'output': ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"],
        },
    ]
    solution = Solution()

    for param in params:
        cpdomains = param['input']
        result = solution.subdomainVisits(cpdomains)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
