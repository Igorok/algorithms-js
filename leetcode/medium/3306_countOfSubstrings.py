from typing import List
import json
from collections import deque, defaultdict
import math

class Solution:
    def countOfSubstrings_0(self, word: str, k: int) -> int:
        n = len(word)
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        res = 0

        for i in range(n):
            countVowels = 0
            currentVowels = defaultdict(int)

            for j in range(i, n):
                if word[j] in vowels:
                    currentVowels[word[j]] += 1
                    if currentVowels[word[j]] == 1:
                        countVowels += 1

                if countVowels == 5:
                    totalVowels = sum(currentVowels.values())
                    notVowels = j - i + 1 - totalVowels
                    if notVowels == k:
                        res += 1
                    elif notVowels > k:
                        break
        return res

    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = ['a', 'e', 'i', 'o', 'u']

        def getCountMoreNum(num):
            currentVowels = {}
            consonantsCount = 0
            res = 0
            start = 0

            for i in range(n):
                char = word[i]

                if char in vowels:
                    currentVowels[char] = currentVowels.get(char, 0) + 1
                else:
                    consonantsCount += 1

                while len(currentVowels) == 5 and consonantsCount >= num:
                    count = n - i
                    res += count

                    prev = word[start]
                    if  prev in vowels:
                        currentVowels[prev] -= 1
                        if currentVowels[prev] == 0:
                            currentVowels.pop(prev)
                    else:
                        consonantsCount -= 1

                    start += 1

            return res


        return getCountMoreNum(k) - getCountMoreNum(k+1)

'''
1 1 1


"aaaaeiouquuuu", 1

a a a a e i o u q u u u u
- - - - - - - - +
- - - - - - - - + +
- - - - - - - - + + + + +
4 + 4
4 + 4 + 4


'''



def test ():
    params = [
        {
            'input': ["aeioqq", 1],
            'output': 0,
        },
        {
            'input': ["aeiou", 0],
            'output': 1,
        },
        {
            'input': ["ieaouqqieaouqq", 1],
            'output': 3,
        },
        {
            'input': ["aaaaeiouq", 1],
            'output': 4,
        },
        {
            'input': ["aaaaeiouquuuu", 1],
            'output': 20,
        },
        {
            'input': ["aaaaeiouquuuuaeio", 1],
            'output': 47,
        },
        {
            'input': [
                "cgkdcbeegaujojhgcfkbhhgaoukbjekhichdouffudefbdfejooigcabjgjdcffgfkfokibkofbfeuofauouuuadcabjghdbgubkduihckagoecbgdejehujgcadhffhucfjgjcougghhigodadibcfekdhkoibabdjgahdojjfdkieaufhojijgbuudefkfehejjcoguiajfgiaiuhaiaecgudfejbcokbkcfkjcbufhbeukdbaohhdkkjejgkbajecofjgkukkhidogiubdukfjiaeuddjfbkobigiihgeohjihdoiuidbcoegieeueaoehkfoobdeuoofaaiaaufcjfikbjaouobocjkkhgucuoiuckhodifiekdgdgiegiihdcckcfggjjboeucdihghaudcjhckbgguufckigebfjcodigbcuehaduikadbufguufegedcgfhighoaagcocgoagkfiggakoiiggigkufhfckcaohaaougecegfegkfdahkgugbueofeefbuchaiigcajakcuuaucedgggcjcbbuabieoagfgdeaghabkafjibdjddjcguoajkojbaoojehucubfookdadgjchgaiaokgcukkkcjcubikhjedaghocjbdhhuucbkccffiebihiehhgcacukfakakafiiaaobukghdeuaguoibuduaccjcuohjakbgcdaibhabdakuhkagkjkcguhjeguuduoujheoadcuuhegbabgbidbakkhcakffkiiccjdeheufiueedfifcibhoahbcdgfeukeoohieejdukbkdjhaoegajgcegieuuddhujdaifdckuocihbfghofgidkhdoikegdiiufgdchhckghegdideguaafihkigfbucdueocdcocdoobhjdkkoujoickuhjkfcugbhfeoadihgigfaohhbjhkiokjhjdckjdkhjhkcjhbfjaacgokeigaiogggojbcujobcuaodibffdaogeojjhidikiukebhjahabgibhikbociufjofiackckaoufuikjcaiajjfocuofoagacggjueaccjojciceiudijbiuugcufdbeiofibkgbhffgefgfhecheoadhubfbujucofoiigbabkfcikjefcoeboobobdodijgabfcihufakhbekghcgkcbfcgokhhbbfbkabbiefkaejuedikkokdgccageajkbkhahjijobfjoadjdohfcbejafafubifjkckachgcckuhehahabofhaeooodifakkdjudfefffobaiijdegcfjjbiudgbbbiigujugufdoedbagfgjjedcuaobhubgiighkdhdghdafggukaaoegackihgigfeeceficeahaajfuaajcouaodiogfihcuukeohbkaodhkcbcdagkfdfgcbjdkoabgehcadgfgeghdoichhfkbgedjgeojhuchoeaohhicuhocdakofufjficgcfeacudbdcgjaccchakiigdafuacchfchadaaiacahhcckuoiakhgdgjaujhaidckkiefahdhicjaihegufehfikouhfjjokcdugfguahcbdjobchdchgohkibhbafdeuoiejchjjjchufckgugfuboefiejfoucdhbcdhbkaejjagjuigucjcdcefiacjodkgbdiiddoidhfehfihgeabikbeukkuooojaahdjhioagbfhjjijdfcadkbodcbiubebdfceudbajakiaefgfggookbioedgcejoigeiddabedaucchbhbcdddjueeahdakojbcfcjjhgdekadfhigichehicobafahioahkjaujbeibbfocucakcafukaiaceacfehbajijbkaaiifjuuguhaegfohfkaujdkgkhkccbochchucoauebagbcaeibafcufefaodbjiadkafkoedejcakkdoihhdhjcieaekjhbejjkccogfeaofckbbcekjhhjcdfaoigcjbigjkfkobiddhofbkhkakicjdbgddfjkikiihkgahhdecokdjkuuhoakgiajjbjafihcgegkkeajcaddodibjfieededboajhahcueegubudcebedjkgfkhufaugahickugjbdjdhkuabudagjcdckcoaugohijuafbddacgfijgochcjuofagafecbjiickckiiheukicafeofuefhdahcfebeiahubogdgaiigkiefiehaucuogccbfdecaekgeodgdabjubbkgjhkhibdaaccofjujhdeugjcuafkkckbeueeddkgkbgejbaogkfgeebkbkbhoakdhdgogufgfadhfudbbhkgjdbuibucfuggaajufcukdijauhjjkhbhgcgdfaioffougikbbhidjegugujedhbbhagfibafhfiduifegfoaaugoaeciofdgaghfhgoefeghcagjjeueekefhjchobhgucdcaiffoouuioaccfihgcekjieufueeghicigufbiucjjouobcoibajougghoauhdgioagbfkkofbedkcfdibkhfbfbfjeibbuhajdgjceuiiihhoafcgcjdcuucbbiihuoaagduffecjijhijdcgdcghakuhebdjfjdahkekdjofuiuobgujijaakbdgukbhkuaciejbghccibbdgieffhiicoadkeiibdkhfjhchgokhhgkfadjgoeadghokfjjehgjbauebgdgoiohaofibgikhfafkooucjigohkukdhofokkccuciaaeaujbidgjouuaekfkuebodoukfiahehkjejiooajeodibcfdhuhcgfjkfihbdhheoduoujgjjoojegdehheijfaoaehiofoaaceedkjhfifiicgchfdgfodiujcdieihoguugcbafbujhdcuebabgddgadaejcjhdbjobgcighujhcdbeejbbfjdcbuhedckcehbhgkdoaugdcjcochudbafjejujifihdgajegkjbojaubbkedbauouhoudjbjhgihhgdaafkicibacekiaidjefbbeaggbujjuugkuiafuggeojejoiougubjhdfugedkeigadakkbhejgabidaehgugkbihgdifiobjhbeiuujgegcauekakkhdhgofhebkbejaejhecbouedfeebjaiebhkfofhioacaefbcdajuohdkgfbajbcefikifcfukbgkaofuudaefckjgbhkfojeajcdijdjejchbuhbbocgfjubiihuaobhhgudcibubbiicieiiakgkcdjabdkbedbaokcbhikudubujfbjfhoedkdubhgkcbuoeaidfebigcfkuudaoejbdgfhjfjbgkcueeogcfdiogbibeaguddkegaucjjfuhcuibgjujjkufjbgujbdjekegdfgbfidijadagkheauafofabochekaeedfjcakcoaeiufojueehehaagbjhehhghoegguhaiuuickhujhguhhfddccfaukbjicucfcdijubjdfeefhijhufuucdojbbuhfjfhbcduefebgkaaduhfaejhcafkucoeoudibbiaefufcgoiajubbjakehbcdajfofiijoehoedcgeuhecejdcfffhhaegufacubceguhhaikujbcebuoiikkdkdcceafdkkhocakguukcbfdcdgfgabobuajceadieuukaabkoibiekfjhhbgiddaiaehgfoaefkodiheekeghjgkfokojcadkdfkaajduagfkggfjfajhgcidoubkbeaoodhkidofdabohoehabbkhidocokgggcgdfgciueibjdfiuficacugjeajuafgeoehfggjdkhhkfdukujubgobjkbdibaieghckffgeojigkkucbejifuuekjoejfgkcbkcjhgoacbhdedhdagbiiaoeuoigihjfebjcfaacccadfcebeoukkjijooeeaaguafuihcgkiedfebdcuhfigdbbajeaduchedeigokjuojgacoaeeofjgfjddeoukcfddooghdddfcggiifcgkubchuhcfjfeiacikbkdcfokbbbdebagfugdeoedhogegkihhbcjfbcagggjbidiaghkobdhbcekkbcffjcgckgifjudifuuedakfggcjbdibjcfgudoukdiddkbibdguoiubojjhehedbogjoodkefefhgohackfgbhbdaobkbejkiokcbkiicidekcaecuiihddidbgujecodooeckjjfiahajajedoejjciggbfhckjdiacocfikfojodojgfbcjkbeugkebjijbkjhkhjokiogjfddbjdjoukkofohgukfiiadcfeigekufgbcucfacbbiicheogahcghecddgoabjkoffeaiikdbbbhijkghdbbhdkdajahbjuuiogbjoedcdfuiibdeighhoegidbodcuajjcegefffeeuhefhbfgeidokgijoadfkojhijkjuffgkdaiagihiijfdeioicdgdcggkfbcfaoehfdacifuaubciicaccibagauikabaahaiiegehfeebkkjidafiggjgocuckbggijihdbaiabogjjjaujughudfkccbjkobcudckoibudfaadjuioaakfhdfbeidhaaaogbgkjgecobiohhbufukjgcbhaaiojooicheuefaihifkujkukihcbofcjukhafjadodihufhgajjiibjdghhaahkooekfaeoudiagicbcuoehukeoiuuddjachcffhekujudjeuogicoeeoiouauubfuhcbbgjuhbfcdouaujfiugghfjdkacfadbuiakoacbikjfgkacfofaijbaohkchioedfegdhggccgbehuooh",
                1534,
            ],
            'output': 4049,
        },
    ]
    solution = Solution()

    for param in params:
        word, k = param['input']
        result = solution.countOfSubstrings(word, k)
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
