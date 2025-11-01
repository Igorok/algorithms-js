from typing import List
import json
from collections import deque, defaultdict


class Solution_0:
    def largestVariance(self, s: str) -> int:
        n = len(s)
        codes = {}
        for i in range(ord('a'), ord('z') + 1):
            codes[chr(i)] = i - ord('a')

        res = 0
        for i in range(n):
            acc = [0] * 26

            for j in range(i, n):
                code = codes[s[j]]
                acc[code] += 1

                minCount = 10**6
                maxCount = -1

                for cnt in acc:
                    maxCount = max(maxCount, cnt)
                    if cnt > 0:
                        minCount = min(minCount, cnt)

                res = max(res, maxCount - minCount)

        return res


class Solution:
    def largestVariance(self, s: str) -> int:
        n = len(s)
        chars = {}
        for i in range(n):
            chars[s[i]] = i


        res = 0

        for char1 in chars:
            for char2 in chars:
                if char1 == char2:
                    continue

                cnt1 = 0
                cnt2 = 0
                acc = 0

                for i in range(n):
                    if s[i] != char1 and s[i] != char2:
                        continue

                    val = 1 if s[i] == char1 else -1

                    if acc + val < val and not (i > chars[char2]):
                        acc = val
                        cnt1 = 0
                        cnt2 = 0
                    else:
                        acc += val

                    cnt1 += 1 if s[i] == char1 else 0
                    cnt2 += 1 if s[i] == char2 else 0

                    if cnt1 != 0 and cnt2 != 0:
                        res = max(res, acc)

        return res


'''
aababbb

- a a b a b b b
a 1 2 2 3 3 3 3
b 0 0 1 1 2 3 4
...
z 0 0 0 0 0 0 0

---

- c a b a b a c
a 0 1 1 2 2 3 3
b 0 0 1 1 2 2 2
c 1 1 1 1 1 1 2

cababab


'''

def test ():
    params = [
        {
            'input': 'abbaaaaaaaaa',
            'output': 8,
        },
        {
            'input': 'aabbbb',
            'output': 3,
        },
        {
            'input': 'abbbaaaaaa',
            'output': 5,
        },
        {
            'input': 'aababbb',
            'output': 3,
        },
        {
            'input': 'abcde',
            'output': 0,
        },
        {
            'input': 'cababab',
            'output': 2,
        },
        {
            'input': 'lucmdweawziyvixyfesksmkxkbzzzqdmrmvdxeghlrlyteuhvumwppwltssrlboozoiudqegobjvnuinwoaaxbiqivtwabunqkzvjnczasvghsvrckpzelcqeloppxwmnbeocoiximllpvhahesjxznfphohoycaqsaghpoligtghoejodmhwuzjmpwkrpehheuubiespninbzfbqtiimtzbymdrxxbjzhqanmoocicqfhdrtfwjbxkgehjdqhmmjnrrgilsvyhonfmvywaejhxxgabogdqgttfiufrgpgpduwhzgmgoecwagwdvmnobiukuigphrkupqkeaphjsqhmetkgmcramydkosqqmayrdgfiokpanxznuknqpcqsbumyrxfsmmcxvherbjykpbwdzeqjgdhysauxflcdhkmlflmygylnxubaimtmsbbapfsrqdwwihubmemmhumzhmvalwkneehsxjofrcubyscgmlwfuzepmlyvpthqlvxrzcekmbemneozbtfajwkaizheoexbtdicgzmgnbytwyruexhigheujnolqafjmvtfgeduwtkisjovklsazfoslylmqjkgafbcfsawdjlyyobskeywidozxbmmapjrhqjjtoknpujwibccdotmnfxqcmhbelrireqfxmqoitciszlhecacxrpdbxeqravhrgwylhzpamvjjmghrzywpfpxjogidkkuolqscxuqgxzfmkuiagndjfhcmuwysojjmwtdrmicpnjpxonymsuwvrodwmfbtpwyxmesmkpuctrlabbknyoyueumfitkpdzsnkurzzyexeutmbqcdbmirqndghaksbpukszbkgvgswjrixuwvzsoymjuiungsnpytstwjbekzudtjxqkwkhgyophfllqvmdwvdlywtnsvlfwkesxdhdfwytgtwkgprlocjlcjqezcwpiwldnrqwyqxrgyyrkdotjhtsppwjkpecnpyarjftdbvzhdnqkqpbkwtkcfsomzwgxnwtsoslvxbwdkfvaeyxzkadctnngewqbwftphtfcdhjbwzytmrlolbgouoluyfyngtkijgwvxmjzqcapymvdssiirusnrnmuextfeosrdsudwixozufmwatfmjjumqmnprsqdrrerjkivjlnohkgckhuzbajvfjezbsivnhnexfryxghcxvetlwnjlutskdguwlsqhcuravxvfmzeycxifyjjqvbdmlmzfsuekrszqvdtmlfcytznjkplqpveqybkdmggrnyuoabxkepgbenzaufxwrmqufmnlgndjakvhbkkkzhgdoutdphnrqhtogbrpgdifgcqzheognwlgoqszqjsshaiciiwjqoxlznfgjtytrmkmypspmmsyencfxdjtzzlzgjzzoqwkzriqhvfqigezstcwcflbhyalipesdxddoyzcdskthyiasfdkgxgigirbixeaneynxedrbvfybpxxonssjylrahpkklrjgvbzllsfinxtcdkejynhxekkehqlizormtlmglsakfrketakpgsziogdgtfpwzeufejryluxjjuwfcgvbipmkrgtnfupqshysughfgnxtfgazdybvdtiqiimxibxlxhzsorqgshaauhgjszlfhaoxzfhnnfsdnsxqjmhaliuhavzqielpcqjzbzelrnruhqzxrynexubqpkhsoqrearfdxmliaiamfaorysjpuldzvuqnddmskegfmrxdgeonfhyuzhpgmghsvkvolhvrdyqvgqxshjjzrozkhkrsoktmvpkllizosqdsmybnwmybkyfqxyaeumgcubtdwtlbxuhcowgqvvrraazmeoamazjbljfzfvjmjhiifpskinydncsbcoefknvjzqinbfvgyyfjzqewxwdzivzeemqvxmjrsuxavjeqtbklezsqeas',
            'output': 45,
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.largestVariance(s)
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
