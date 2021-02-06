#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 上午11:09
# @Author  : cenchaojun
# @File    : model_epoch_test.py
# @Software: PyCharm
import os
import time

for epoch in range(1,51):
    config = 'python3 test.py ../configs/faster_rcnn/faster_rcnn_x101_64x4d_fpn_1x_coco_giou.py work_dirs/faster_rcnn_x101_64x4d_fpn_1x_coco_giou/epoch_{0}.pth --out work_dirs/faster_rcnn_x101_64x4d_fpn_1x_coco_giou/faster_rcnn_x101_64x4d_fpn_1x_coco_giou.pkl --eval mAP'.format(epoch)
    os.system(config)
    time.sleep(1)
