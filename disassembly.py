#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pykakasi import kakasi,wakati

kakasi = kakasi()
kakasi.setMode("H","a") # default: Hiragana no conversion
kakasi.setMode("K","a") # default: Katakana no conversion
kakasi.setMode("J","a") # default: Japanese no conversion
kakasi.setMode("r","Hepburn") # default: use Hepburn Roman table

conv = kakasi.getConverter()


def disassembly():
    text = _load_text()
    count_list = _alphabet_count(text)
    _save(count_list)


def _load_text():
    text = '案内'
    return text

def _alphabet_count(text):
    romazi = conv.do(text)
    mozi_dict = {chr(i):0 for i in range(97, 123)}
    for mozi in romazi:
        mozi_dict[mozi] += 1
    return [count for (mozi, count) in mozi_dict.items()]


def _save(count_list):
    pass
