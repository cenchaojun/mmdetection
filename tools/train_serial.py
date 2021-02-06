#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/30 下午7:45
# @Author  : cenchaojun
# @File    : train_serial.py
# @Software: PyCharm
import os
import time

# config_list = ["python3 train.py ../configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py --no-validate",
#                "python3 train.py ../configs/faster_rcnn/faster_rcnn_r101_fpn_1x_coco.py --no-validate",
#                "python3 train.py ../configs/faster_rcnn/faster_rcnn_r152_fpn_1x_coco.py --no-validate",
#                "python3 train.py ../configs/faster_rcnn/faster_rcnn_x50_32x4d_fpn_coco.py --no-validate",
#                "python3 train.py ../configs/faster_rcnn/faster_rcnn_x101_32x4d_fpn_1x_coco.py --no-validate",
#                "python3 train.py ../configs/faster_rcnn/faster_rcnn_x101_64x4d_fpn_1x_coco.py --no-validate",
#                "python3 train.py ../configs/faster_rcnn/faster_rcnn_r50_rfp_coco.py --no-validate",
#                "python3 train.py ../configs/faster_rcnn/faster_rcnn_hrnet_w32_hrfpn_coco.py --no-validate"]
config_list = ["python3 train.py ../configs/faster_rcnn/faster_rcnn_x101_64x4d_fpn_1x_coco_giou.py --no-validate",
               "python3 train.py ../configs/faster_rcnn/faster_rcnn_x101_64x4d_fpn_1x_coco_ciou.py --no-validate",
               "python3 train.py ../configs/faster_rcnn/faster_rcnn_x101_64x4d_fpn_1x_coco_iou.py --no-validate",
               "python3 train.py ../configs/faster_rcnn/faster_rcnn_r50_pafpn_coco.py --no-validate"]
time_list = []
for config in config_list:
    start_time = time.time()
    os.system(config)
    end_time = time.time()
    min = str((end_time-start_time)/60)
    time_list.append(min)
    time.sleep(1)

str_time = str(time_list)

with open("ioutime.txt",'a+') as f:
    f.write(str_time)

#
# start_time = time.time()
# os.system("python3 train.py ../configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py --no-validate")
# end_time = time.time()
# faster_rcnn_r50_fpn_1x_coco = str((end_time-start_time))
# time.sleep(5)
# os.system("python3 train.py ../configs/faster_rcnn/faster_rcnn_r101_fpn_1x_coco.py --no-validate")
# time.sleep(5)
# os.system("python3 train.py ../configs/faster_rcnn/faster_rcnn_r152_fpn_1x_coco.py --no-validate")
# time.sleep(5)
# os.system("python3 train.py ../configs/faster_rcnn/faster_rcnn_x50_32x4d_fpn_coco.py --no-validate")
# time.sleep(5)
# os.system("python3 train.py ../configs/faster_rcnn/faster_rcnn_x101_32x4d_fpn_1x_coco.py --no-validate")
# time.sleep(5)
# os.system("python3 train.py ../configs/faster_rcnn/faster_rcnn_x101_64x4d_fpn_1x_coco.py --no-validate")
# time.sleep(5)
# os.system("python3 train.py ../configs/faster_rcnn/faster_rcnn_r50_rfp_coco.py --no-validate")
# time.sleep(5)
# os.system("python3 train.py ../configs/faster_rcnn/faster_rcnn_hrnet_w32_hrfpn_coco.py --no-validate")
