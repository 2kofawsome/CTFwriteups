print_flag = """.=Z4%\E4GDe4 eaZoPpUe:bDMoUEPZGt\ AwbbSUY YX@Wt{ZJZ]Sm1zYF5~ss3RGWKpYz,\\5O1@Y7{kn:,%Nm\p@`JJ]bbY @ZE a E\ ^\g/bZZZZE P%EeZ]]>zUDe^E a E\ Y^\ggbbY @ZSp Sl^g/bZZZZ]]]F+
Xf5}IX7|0X17s+XB&N)KXn+(X,O+1qXCQ*)`X7|0]]]bZZZZt\\ EPZY SUY X@Wt{>XXYUSXXZD\ZeUPZ,Ue ZteYZY SUY X@Wt{>XXYUSXX>%oo E^gjm/wh?ZJJZE a E\ ^Sp Sl>XXYUSXXgbbY @ZY SUY X@Wt{^SUY g/bZZZZ]]]y8Pp X	%DSlXGEUeX@U$Xz%Mo\XUa EXPp XWtkXYU{8/ZRm:whA~_3>6'Z8DP M\8/j?V]]]bZZZZE P%EeZGt\ Aw>GAwY SUY ^SUY g>Y SUY ^gbbD@ZXXetM XXZJJZ]XXMtDeXX]/bZZZZSp Sl^gbZZZZoEDeP^Y SUY X@Wt{^SUY YX@Wt{ggb"""

import string
charset: str = string.printable
chars_left = list(charset)
print(chars_left)

def findPattern(offsets):
    for char in charset:
        count = 0
        s = char + ": "
        indices = []
        for i in range(len(print_flag)):
            if char == print_flag[i]:
                count += 1
                indices.append(i)
        for i in range(len(indices) - 7): # the_quick_brown_fox_jumps_over_the_lazy_dog
            for n in range(7):
                if print_flag[indices[i+n]] != print_flag[indices[i+n] + offsets[n]]:
                    break
            if n > 5:
                print(s, end="")
                print(indices[i:i+8])

def buildKey(key, phrases, offsets):
    for n in range(len(phrases)):
        for i in range(len(phrases[n])):
            if (print_flag[offsets[n] + i]) not in key.keys():
                key[print_flag[offsets[n] + i]] = phrases[n][i]
                chars_left.remove(phrases[n][i])
    print(key)

def translate(key):
    for c in print_flag:
        if c in key.keys():
            print(key[c], end="")
        else:
            print("$", end="")
    print()

offsets = [6, 6, 4, 6, 5, 4, 5]
findPattern(offsets)
# X: [353, 359, 365, 369, 375, 380, 384, 389]

phrases = ["{'the_quick_brown_fox_jumps_over_the_lazy_dog': 123456789.0, 'items':[]}",
           "#! /usr/bin/env python3"]
offsets = [349, 0]
key = {}
buildKey(key, phrases, offsets)
# {'P': 't', 'p': 'h', ' ': 'e', 'X': '_', '\t': 'q', '%': 'u', 'D': 'i', 'S': 'c', 'l': 'k', 'G': 'b', 'E': 'r', 'U': 'o', '\x0b': 'w', 'e': 'n', '@': 'f', '$': 'x', 'z': 'j', 'M': 'm', 'o': 'p', '\\': 's', 'a': 'v', 'W': 'l', 't': 'a', 'k': 'z', '\x0c': 'y', 'Y': 'd', '{': 'g'}
# {'y': '{', '8': "'", 'P': 't', 'p': 'h', ' ': 'e', 'X': '_', '\t': 'q', '%': 'u', 'D': 'i', 'S': 'c', 'l': 'k', 'G': 'b', 'E': 'r', 'U': 'o', '\x0b': 'w', 'e': 'n', '@': 'f', '$': 'x', 'z': 'j', 'M': 'm', 'o': 'p', '\\': 's', 'a': 'v', 'W': 'l', 't': 'a', 'k': 'z', '\x0c': 'y', 'Y': 'd', '{': 'g', '/': ':', 'Z': ' ', 'R': '1', 'm': '2', ':': '3', 'w': '4', 'h': '5', 'A': '6', '~': '7', '_': '8', '3': '9', '>': '.', '6': '0', "'": ',', 'j': '[', '?': ']', 'V': '}', '.': '#', '=': '!', '4': '/'}

translate(key)
# .. .usr.bin.env python3.import base64..coded_flag . .c2.jd..7..91bl.hdj....fd.gz.3.u.2shf......def reverse.s.:.    return ...join.reversed.s....def check..:.    ......_...._..._...._....._..._....._....._.......    asert decode_flag.__doc__ is not .one and decode_flag.__doc__.upper..[2:45] .. reverse.check.__doc__...def decode_flag.code.:.    ...{'the_quick_brown_fox_jumps_over_the_lazy_dog': 123456789.0, 'items':[]}....    return base64.b64decode.code..decode....if __name__ .. .__main__.:.    check...    print.decode_flag.coded_flag...
# #! /usr/bin/env python3.import base64..coded_flag . .c2.jd..7..91bl.hdj....fd.gz.3.u.2shf......def reverse.s.:.    return ...join.reversed.s....def check..:.    ......_...._..._...._....._..._....._....._.......    asert decode_flag.__doc__ is not .one and decode_flag.__doc__.upper..[2:45] .. reverse.check.__doc__...def decode_flag.code.:.    ...{'the_quick_brown_fox_jumps_over_the_lazy_dog': 123456789.0, 'items':[]}....    return base64.b64decode.code..decode....if __name__ .. .__main__.:.    check...    print.decode_flag.coded_flag...

key["b"] = "\n"
chars_left.remove("\n")
key["^"] = "("
key["g"] = ")"
key["]"] = "'"
key["J"] = "="
chars_left.remove("=")
key[","] = "N"
chars_left.remove("N")
translate(key)
"""
#! /usr/bin/env python3
import base64

coded_flag = 'c2$jd$$7$$91bl$hdjN$$$fd$gz$3Nu$2shf$=='

def reverse.s$:
    return ''.join.reversed.s$$

def check.$:
    '''$$$_$$$$_$$$_$$$$_$$$$$_$$$_N$$$$_$$$$$_$$$'''
    asert decode_flag.__doc__ is not None and decode_flag.__doc__.upper.$[2:45] == reverse.check.__doc__$

def decode_flag.code$:
    '''{'the_quick_brown_fox_jumps_over_the_lazy_dog': 123456789.0, 'items':[]}'''
    return base64.b64decode.code$.decode.$

if __name__ == '__main__':
    check.$
    print.decode_flag.coded_flag$$"""


revoffsets = [5, 4, 5, 6, 4, 6, 6]
findPattern(revoffsets)
# X: [167, 172, 176, 181, 187, 191, 197, 203]

phrases = [("the_quick_brown_fox_jumps_over_the_lazy_dog".upper())[::-1]]
offsets = [165]
buildKey(key, phrases, offsets)
# {'y': '{', '8': "'", 'P': 't', 'p': 'h', ' ': 'e', 'X': '_', '\t': 'q', '%': 'u', 'D': 'i', 'S': 'c', 'l': 'k', 'G': 'b', 'E': 'r', 'U': 'o', '\x0b': 'w', 'e': 'n', '@': 'f', '$': 'x', 'z': 'j', 'M': 'm', 'o': 'p', '\\': 's', 'a': 'v', 'W': 'l', 't': 'a', 'k': 'z', '\x0c': 'y', 'Y': 'd', '{': 'g', '/': ':', 'Z': ' ', 'R': '1', 'm': '2', ':': '3', 'w': '4', 'h': '5', 'A': '6', '~': '7', '_': '8', '3': '9', '>': '.', '6': '0', "'": ',', 'j': '[', '?': ']', 'V': '}', '.': '#', '=': '!', '4': '/', 'b': '\n', '^': '.', ']': "'", 'J': '=', ',': 'N', 'F': 'G', '+': 'O', '\n': 'D', 'f': 'Y', '5': 'Z', '}': 'A', 'I': 'L', '7': 'E', '|': 'H', '0': 'T', '1': 'R', 's': 'V', 'B': 'S', '&': 'P', 'N': 'M', ')': 'U', 'K': 'J', 'n': 'X', '(': 'F', 'O': 'W', 'q': 'B', 'C': 'K', 'Q': 'C', '*': 'I', '`': 'Q'}

translate(key)
"""#! /usr/bin/env python3
import base64

coded_flag = 'c2RjdGZ7VV91blJhdjN$WRfdEgzX3NuM2shfQ=='

def reverse.s$:
    return ''.join.reversed.s$$

def check.$:
    '''GOD_YZAL_EHT_REVO_SPMUJ_XOF_NWORB_KCIUQ_EHT'''
    asert decode_flag.__doc__ is not None and decode_flag.__doc__.upper.$[2:45] == reverse.check.__doc__$

def decode_flag.code$:
    '''{'the_quick_brown_fox_jumps_over_the_lazy_dog': 123456789.0, 'items':[]}'''
    return base64.b64decode.code$.decode.$

if __name__ == '__main__':
    check.$
    print.decode_flag.coded_flag$$"""

print(chars_left)

import base64

print(base64.b64decode('c2RjdGZ7VV91blJhdjNsZWRfdEgzX3NuM2shfQ==').decode())