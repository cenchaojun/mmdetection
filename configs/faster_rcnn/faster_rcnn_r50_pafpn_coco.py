#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 上午11:55
# @Author  : cenchaojun
# @File    : faster_rcnn_r50_pafpn_coco.py
# @Software: PyCharm
_base_ = '../faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'

model = dict(
    neck=dict(
        type='PAFPN',
        in_channels=[256, 512, 1024, 2048],
        out_channels=256,
        num_outs=5))
total_epochs = 50