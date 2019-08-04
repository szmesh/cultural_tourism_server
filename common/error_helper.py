#!/usr/bin/evn python
# coding=utf-8


def login_success():
    return {'state': 200, 'err': '', 'tips': '登陆成功'}


def verify_invalid():
    return {'state': 403, 'err': '验证码错误', 'tips': '验证码错误'}


def user_notfound():
    return {'state': 404, 'err': '查找不到用户', 'tips': '账户不存在'}


def user_invalid():
    return {'state': 403, 'err': '用户已禁用', 'tips': '账号已被禁用'}


def password_invalid():
    return {'state': 403, 'err': '密码不匹配', 'tips': '密码错误'}
