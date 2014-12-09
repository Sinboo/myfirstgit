#!/usr/bin/env python
#coding:utf-8
#tuwei/tests.py - test file of the lib
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

# from django.test import TestCase
from weilib.lib import create_menu,MButton,get_atoken


# class SimpleTest(TestCase):
#     def test_basic_addition(self):
#         """
#         Tests that 1 + 1 always equals 2.
#         """
#         self.assertEqual(1 + 1, 2)

def create_btns():
    btn1 = MButton('学生')
    btn2 = MButton('家长')
    btn3 = MButton('咨询')
    m_list = [btn1, btn2, btn3]
    
    btn1.add_button(MButton('我的练习', key='ALL_CLASS'))
    btn1.add_button(MButton('综合报告', key='CREATE_CLASS'))
    btn1.add_button(MButton('月度报告', key='MY_CONDITION'))
    
    btn2.add_button(MButton('我的练习', url='http://www.lagou.com/gongsi/40286.html'))
    btn2.add_button(MButton('综合报告', url='http://tiguanjia.com'))
    btn2.add_button(MButton('月度报告',key='CREATE_ACTIVITY'))
    
    # btn3.add_button(MButton('关于我们', url='http://tiguanjia.com'))
    # btn3.add_button(MButton('公司文化', key='ABOUT_TUWEI'))
    # btn3.add_button(MButton('成员介绍', key='ABOUT_MEMBERS'))
    # btn3.add_button(MButton('加入我们', key='JOIN_US'))

    return m_list

def post_menu(appid, appsecret):
    mlist = create_btns
    token = get_atoken(appid, appsecret)
    #print token
    create_menu(token, mlist)
    
    
    
    
    
    