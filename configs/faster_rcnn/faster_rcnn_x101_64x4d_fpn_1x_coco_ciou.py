#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 上午11:41
# @Author  : cenchaojun
# @File    : faster_rcnn_x101_64x4d_fpn_1x_coco_ciou.py
# @Software: PyCharm
_base_ = './faster_rcnn_r50_fpn_1x_coco.py'
model = dict(
    pretrained='open-mmlab://resnext101_64x4d',
    backbone=dict(
        type='ResNeXt',
        depth=101,
        groups=64,
        base_width=4,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=dict(type='BN', requires_grad=True),
        style='pytorch'),
    roi_head=dict(
            bbox_head=dict(
                reg_decoded_bbox=True,
                loss_bbox=dict(type='CIoULoss', loss_weight=10.0))))
total_epochs = 50