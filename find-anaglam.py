#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bottle import route, redirect, post, run, template, request
from anaglam.disassembly import disassembly
from anaglam.grouping import get_group


@route('/')
def index():
    group = get_group()
    return template('index', group=group)

@post('/create')
def create():
    raw_str = request.forms.get('text')
    disassembly(raw_str)
    redirect('/')

if __name__ == '__main__':
    run(host='localhost', port=8080)
