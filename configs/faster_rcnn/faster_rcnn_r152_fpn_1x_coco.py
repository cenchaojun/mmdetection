#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/30 下午2:43
# @Author  : cenchaojun
# @File    : faster_rcnn_r152_fpn_1x_coco.py
# @Software: PyCharm
_base_ = './faster_rcnn_r50_fpn_1x_coco.py'
model = dict(pretrained='torchvision://resnet152', backbone=dict(depth=152))
total_epochs = 50
