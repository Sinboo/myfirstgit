#!/usr/bin/env python
# coding:utf-8
# weilib/router.py - router handlers for weilib
# include router function and router pattern response
# ver 0.1 by winkidney 2014.05.10

import re
import os
import logging
from weilib.handlers import default_handler
from weilib.models import (DBTextMsg, PatternT2T, DBImgTextMsg, PatternT2PT,
                           PatternE2PT, PatternE2T)
from weilib.lib import text_response, pic_text_response, PicTextMsg, PTItem


#先进行base_router,将用户发来的'text'类型的消息经过router_patterns路由到不同的handler上处理并返回给用户。
def base_router(recv_msg, router_patterns):
    for type, key, handler in router_patterns:
        if recv_msg.msg_type == 'text':
            match = re.search(key, recv_msg.content)
            if match:
                return handler(recv_msg)  #此处将消息分发给不同的handler处理。
        elif recv_msg.msg_type == type:
            return handler(recv_msg)

    # return default_handler(recv_msg)


def new_msg_from_db(pattern):
    """Convert PicTextMsg from db to PicTextMsg object for rendering"""
    items = []
    for item in pattern.handler.all():
        items.append(
            PTItem(item.title, item.description, item.pic_url, item.url))
    return items

#后进行db_router,将用户发来的不同类型的消息经过数据库中不同模型的Pattern(如PatternT2T、PatternE2T、PatternE2PT等)
#  路由到相应的pattern.handler.content
def db_router(recv_msg, *args):
    if recv_msg.msg_type == 'text':
        for pattern in PatternT2T.objects.all():
            match = re.search(
                pattern.content.encode('utf-8'), recv_msg.content)
            if match:
                return text_response(recv_msg, pattern.handler.content)

        for pattern in PatternT2PT.objects.all():
            match = re.search(
                pattern.content.encode('utf-8'), recv_msg.content)
            if match:
                return pic_text_response(recv_msg, new_msg_from_db(pattern))

    if recv_msg.msg_type == 'event':
        for pattern in PatternE2T.objects.all():

            if pattern.event == recv_msg.event:
                if recv_msg.event_key:
                    match = re.search(
                        pattern.event_key.encode('utf-8'), recv_msg.event_key)
                    if match:
                        return text_response(recv_msg, pattern.handler.content)
                else:
                    return text_response(recv_msg, pattern.handler.content)

        for pattern in PatternE2PT.objects.all():
            if pattern.event == recv_msg.event:
                if recv_msg.event_key:
                    match = re.search(
                        pattern.event_key.encode('utf-8'), recv_msg.event_key)
                    if match:
                        return pic_text_response(recv_msg, new_msg_from_db(pattern))
                else:
                    return pic_text_response(recv_msg, new_msg_from_db(pattern))
