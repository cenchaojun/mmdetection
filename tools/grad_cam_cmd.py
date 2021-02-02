#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/2 上午10:55
# @Author  : cenchaojun
# @File    : grad_cam_cmd.py
# @Software: PyCharm
import os

os.system('python3 grad_cam.py ../configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py ../work_dirs/faster_rcnn_r50_fpn_1x_coco/epoch_50.pth --input-img DJI_0012_38.jpg')