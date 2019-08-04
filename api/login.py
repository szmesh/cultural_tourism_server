#!/usr/bin/evn python
# coding=utf-8

from bottle import put
from common import web_helper, encrypt_helper, db_helper, error_helper
from common.status_helper import Status


@put('/mcts/api/login/')
def post_login():
    """用户登陆验证"""
    ##############################################################
    # 获取并验证客户端提交的参数
    ##############################################################
    username = web_helper.get_form('username', '帐号')
    password = web_helper.get_form('password', '密码')
    verify = web_helper.get_form('verify', '验证码')
    ip = web_helper.get_ip()

    ##############################################################
    # 从session中读取验证码信息
    ##############################################################
    s = web_helper.get_session()
    verify_code = s.get('verify_code')
    # 删除session中的验证码（验证码每提交一次就失效）
    if 'verify_code' in s:
        del s['verify_code']
        s.save()
    # 判断用户提交的验证码和存储在session中的验证码是否相同
    if verify.upper() != verify_code:
        model = error_helper.verify_invalid()
        return web_helper.return_msg(model['state'], model['tips'], err=model['err'])

    ##############################################################
    ### 获取登录用户记录，并进行登录验证 ###
    ##############################################################
    sql = """select * from user where account='%s'""" % (username,)
    # 从数据库中读取用户信息
    manager_result = db_helper.read(sql)
    # 判断用户记录是否存在
    if not manager_result:
        model = error_helper.user_notfound()
        return web_helper.return_msg(model['state'], model['tips'], err=model['err'])

    ##############################################################
    ### 验证用户登录密码与状态 ###
    ##############################################################
    # 对客户端提交上来的验证进行md5加密将转为大写（为了密码的保密性，这里进行双重md5加密，加密时从第一次加密后的密串中提取一段字符串出来进行再次加密，提取的串大家可以自由设定）
    # pwd = encrypt_helper.md5(encrypt_helper.md5(password)[1:30]).upper()
    # 对客户端提交上来的验证进行md5加密将转为大写（只加密一次）
    pwd = encrypt_helper.md5(password).upper()
    # 检查登录密码输入是否正确
    if pwd != manager_result[0].get('password', ''):
        model = error_helper.password_invalid()
        return web_helper.return_msg(model['state'], model['tips'], err=model['err'])
    # 检查该账号虽否禁用了
    if manager_result[0].get('status', 0) == Status.INVALID:
        model = error_helper.user_invalid()
        return web_helper.return_msg(model['state'], model['tips'])

    ##############################################################
    ### 把用户信息保存到session中 ###
    ##############################################################
    manager_id = manager_result[0].get('mid', 0)
    s['mid'] = manager_id
    s['account'] = username
    s.save()

    ##############################################################
    ### 更新用户信息到数据库 ###
    ##############################################################
    # 更新当前管理员最后登录时间、Ip与登录次数（字段说明，请看数据字典）
    sql = """update user set last_login_time=%s, last_login_ip=%s where id=%s"""
    # 组合更新值
    vars = ('now()', ip, manager_id)
    # 写入数据库
    db_helper.write(sql, vars)

    model = error_helper.login_success()
    return web_helper.return_msg(model['state'], model['tips'])
