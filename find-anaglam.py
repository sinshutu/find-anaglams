#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pykakasi import kakasi,wakati

kakasi = kakasi()
kakasi.setMode("H","a") # default: Hiragana no conversion
kakasi.setMode("K","a") # default: Katakana no conversion
kakasi.setMode("J","a") # default: Japanese no conversion
kakasi.setMode("r","Hepburn") # default: use Hepburn Roman table
# kakasi.setMode("C", True) # add space default: no Separator
# kakasi.setMode("c", False) # capitalize default: no Capitalize

conv = kakasi.getConverter()

def converion(romazi):
    mozi_dict = {chr(i):0 for i in range(97, 123)}
    for mozi in romazi:
        mozi_dict[mozi] += 1
    return mozi_dict

if __name__ == '__main__':
    text = input()
    result = conv.do(text)
    print('out: ', end='')
    print(result)
    print(converion(result))
