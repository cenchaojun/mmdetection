#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/30 下午7:45
# @Author  : cenchaojun
# @File    : train_serial.py
# @Software: PyCharm
import os
import time
os.system("python3 tools/train.py configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py")
time.sleep(5)
os.system("python3 tools/train.py configs/faster_rcnn/faster_rcnn_r101_fpn_1x_coco.py")
time.sleep(5)
os.system("python3 tools/train.py configs/faster_rcnn/faster_rcnn_r152_fpn_1x_coco.py")
time.sleep(5)
os.system("python3 tools/train.py configs/faster_rcnn/faster_rcnn_x50_32x4d_fpn_coco.py")
time.sleep(5)
os.system("python3 tools/train.py configs/faster_rcnn/faster_rcnn_x101_32x4d_fpn_1x_coco.py")
time.sleep(5)
os.system("python3 tools/train.py configs/faster_rcnn/faster_rcnn_x101_64x4d_fpn_1x_coco.py")
time.sleep(5)
os.system("python3 tools/train.py configs/faster_rcnn/faster_rcnn_r50_rfp_coco.py")