# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/273/

debug = False

lower = {
    0: 'Zero',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    14: 'Fourteen',
    15: 'Fifteen',
    18: 'Eighteen',
}

tens = {
    2: 'Twenty',
    3: 'Thirty',
    4: 'Forty',
    5: 'Fifty',
    6: 'Sixty',
    7: 'Seventy',
    8: 'Eighty',
    9: 'Ninety',
}

class Solution:
    def onek(self, num:int) -> str:
        if num < 20:
            if num in lower:
                return lower[num]
            else:
                return lower[num % 10] + 'teen'

        if num < 100:
            rem = num % 10
            return \
                tens[num // 10] + \
                (' ' + lower[num % 10] if rem > 0 else "")

        if num < 1000:
            hundreds = num // 100
            rem = num % 100

            return \
                lower[hundreds] + " Hundred" + \
                (' ' + self.onek(rem) if rem > 0 else "")

    def numberToWords(self, num: int) -> str:
        global debug

        if num < 1000:
            out = self.onek(num)
        elif num < 1000000:
            first = num // 1000
            rem = num % 1000
            out = \
                self.onek(first) + ' Thousand' + \
                (' ' + self.numberToWords(rem) if rem > 0 else "")
        elif num < 1000000000:
            first = num // 1000000
            rem = num % 1000000
            out = \
                self.onek(first) + ' Million' + \
                (' ' + self.numberToWords(rem) if rem > 0 else "")
        else:
            first = num // 1000000000
            rem = num % 1000000000
            out = \
                self.onek(first) + ' Billion' + \
                (' ' + self.numberToWords(rem) if rem > 0 else "")

        if debug: print(f'num: {num} -> out: {out}')

        return out

if __name__ == '__main__':
    debug = True

    s = Solution()

    assert s.numberToWords(0) == "Zero"
    assert s.numberToWords(1) == "One"
    assert s.numberToWords(10) == "Ten"
    assert s.numberToWords(15) == "Fifteen"
    assert s.numberToWords(16) == "Sixteen"
    assert s.numberToWords(19) == "Nineteen"
    assert s.numberToWords(20) == "Twenty"
    assert s.numberToWords(21) == "Twenty One"
    assert s.numberToWords(39) == "Thirty Nine"
    assert s.numberToWords(90) == "Ninety"
    assert s.numberToWords(99) == "Ninety Nine"

    assert s.numberToWords(100) == "One Hundred"
    assert s.numberToWords(101) == "One Hundred One"
    assert s.numberToWords(250) == "Two Hundred Fifty"
    assert s.numberToWords(999) == "Nine Hundred Ninety Nine"

    assert s.numberToWords(1000) == "One Thousand"
    assert s.numberToWords(1001) == "One Thousand One"
    assert s.numberToWords(2020) == "Two Thousand Twenty"
    assert s.numberToWords(6500) == "Six Thousand Five Hundred"
    assert s.numberToWords(9500) == "Nine Thousand Five Hundred"
    assert s.numberToWords(9501) == "Nine Thousand Five Hundred One"
    assert s.numberToWords(9999) == "Nine Thousand Nine Hundred Ninety Nine"

    assert s.numberToWords(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

    assert s.numberToWords(1234567891) == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
