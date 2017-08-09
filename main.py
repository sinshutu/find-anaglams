#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pykakasi import kakasi,wakati

text = "案内"
kakasi = kakasi()
kakasi.setMode("H","a") # default: Hiragana no conversion
kakasi.setMode("K","a") # default: Katakana no conversion
kakasi.setMode("J","a") # default: Japanese no conversion
kakasi.setMode("r","Hepburn") # default: use Hepburn Roman table
# kakasi.setMode("C", True) # add space default: no Separator
# kakasi.setMode("c", False) # capitalize default: no Capitalize

conv = kakasi.getConverter()
result = conv.do(text)
print(result)
