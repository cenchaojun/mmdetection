#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 下午3:28
# @Author  : cenchaojun
# @File    : faster_rcnn_x50_32x4d_fpn_coco.py
# @Software: PyCharm
_base_ = './faster_rcnn_r50_fpn_1x_coco.py'
model = dict(
    pretrained='open-mmlab://resnext50_32x4d',
    backbone=dict(
        type='ResNeXt',
        depth=50,
        groups=32,
        base_width=4,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=dict(type='BN', requires_grad=True),
        style='pytorch'))
total_epochs = 50