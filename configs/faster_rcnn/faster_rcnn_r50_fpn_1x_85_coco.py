#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/5 下午4:13
# @Author  : cenchaojun
# @File    : faster_rcnn_r50_fpn_1x_85_coco.py
# @Software: PyCharm
_base_ = [
    '../_base_/models/faster_rcnn_r50_caffe_c4.py',
    '../_base_/datasets/coco_detection.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
total_epochs = 30