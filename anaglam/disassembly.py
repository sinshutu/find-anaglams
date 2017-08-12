#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pykakasi import kakasi,wakati
import sqlite3
import os
import json

kakasi = kakasi()
kakasi.setMode("H","a") # default: Hiragana no conversion
kakasi.setMode("K","a") # default: Katakana no conversion
kakasi.setMode("J","a") # default: Japanese no conversion
kakasi.setMode("r","Hepburn") # default: use Hepburn Roman table
conv = kakasi.getConverter()

data_path = 'var/'
if not os.path.exists(data_path):
    os.mkdir(data_path)
conn = sqlite3.connect(data_path + 'data.db')


def disassembly(text):
    if not text:
        return None
    _pre_init()
    count_list = _alphabet_count(text)
    _save(text, count_list)
    return True


def _pre_init():
    # conn.execute('''drop table alphabet''')
    create_table = '''create table if not exists alphabet (
                                        id integer primary key autoincrement,
                                        raw_data text,
                                        alphabet_list text
                                        )'''
    conn.execute(create_table)


def _alphabet_count(text):
    romazi = conv.do(text)
    mozi_dict = {chr(i):0 for i in range(97, 123)}
    for mozi in romazi:
        mozi_dict[mozi] += 1
    return ''.join(map(str, [count for (mozi, count) in mozi_dict.items()]))


def _save(raw_data, count_list):
    count_list = json.dumps(count_list)
    insert_data = '''insert into alphabet
                                        (raw_data,
                                        alphabet_list) values (?, ?)'''
    conn.execute(insert_data, (raw_data, count_list))
    conn.commit()
