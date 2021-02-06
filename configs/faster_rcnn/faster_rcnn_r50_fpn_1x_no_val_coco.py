#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 下午5:11
# @Author  : cenchaojun
# @File    : faster_rcnn_r50_fpn_1x_no_val_coco.py
# @Software: PyCharm
_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py',
    '../_base_/datasets/coco_detection.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
total_epochs = 50
