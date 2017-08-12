#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3


data_path = 'var/'
conn = sqlite3.connect(data_path + 'data.db')

def get_group():
    alphabet_list = _get_alphabet_list()
    alphabet_list_group = _grouping(alphabet_list)
    return alphabet_list_group


def _get_alphabet_list():
    cur = conn.cursor()
    alphabet = '''select * from alphabet'''
    cur.execute(alphabet)
    alphabet_list = [x for x in cur]
    cur.close()
    return alphabet_list


def _grouping(alphabet_list):
    alphabet_list_group = {}
    for id, raw_data, alphabet_list in alphabet_list:
        if not alphabet_list in alphabet_list_group:
            alphabet_list_group[alphabet_list] = []
        alphabet_list_group[alphabet_list].append({'id': id, 'text': raw_data})
    return alphabet_list_group

