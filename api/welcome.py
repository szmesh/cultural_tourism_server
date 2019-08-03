#!/usr/bin/python
# coding: utf-8

from bottle import get, response
from common import web_helper


@get('/mcts/')
def welcome():
    """星河文旅云平台默认欢迎信息"""
    # return '欢迎来到星河文旅云平台'
    return web_helper.return_msg(0, '欢迎来到星河文旅云平台')
