#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bottle import route, run, template
from anaglam.disassembly import disassembly


@route('/')
def index():
    return template('<h1>{{title}}</h1>', title='アナグラム一覧')

if __name__ == '__main__':
    # disassembly('旅人')
    run(host='localhost', port=8080)
