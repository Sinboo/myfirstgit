#!/usr/bin/env python
#coding:utf-8
#weilib/plugin/acitvity.py - activity plugin for weilib
#ver 0.1 by winkidney 2014.05.10


def processor(recv_msg):
    """A processor must return a dict.
       If not ,program will throw the returned result.
    """
    from_user = recv_msg.from_user_name
    creat_time = recv_msg.create_time
    return {#'test_plugin': 'only_the test plugin output',
            'from_user': from_user ,
            'creat_time': creat_time ,
            }