#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 上午10:27
# @Author  : cenchaojun
# @File    : test_serial.py
# @Software: PyCharm
import os

# os.system("python3 test.py ../configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py work_dirs/faster_rcnn_r50_fpn_1x_coco/epoch_50.pth --out work_dirs/faster_rcnn_r50_fpn_1x_coco/faster_rcnn_r50_fpn_1x_coco_result.pkl --eval mAP")
# os.system("python3 test.py ../configs/faster_rcnn/faster_rcnn_r101_fpn_1x_coco.py work_dirs/faster_rcnn_r101_fpn_1x_coco/epoch_50.pth --out work_dirs/faster_rcnn_r101_fpn_1x_coco/faster_rcnn_r101_fpn_1x_coco_result.pkl --eval mAP")
# os.system("python3 test.py ../configs/faster_rcnn/faster_rcnn_r152_fpn_1x_coco.py work_dirs/faster_rcnn_r152_fpn_1x_coco/epoch_50.pth --out work_dirs/faster_rcnn_r152_fpn_1x_coco/faster_rcnn_r152_fpn_1x_coco_result.pkl --eval mAP")
# os.system("python3 test.py ../configs/faster_rcnn/faster_rcnn_r50_rfp_coco.py work_dirs/faster_rcnn_r50_rfp_coco/epoch_50.pth --out work_dirs/faster_rcnn_r50_rfp_coco/faster_rcnn_r50_rfp_coco_result.pkl --eval mAP")
# os.system("python3 test.py ../configs/faster_rcnn/faster_rcnn_x50_32x4d_fpn_coco.py work_dirs/faster_rcnn_x50_32x4d_fpn_coco/epoch_50.pth --out work_dirs/faster_rcnn_x50_32x4d_fpn_coco/faster_rcnn_x50_32x4d_fpn_coco_result.pkl --eval mAP")
# os.system("python3 test.py ../configs/faster_rcnn/faster_rcnn_x101_32x4d_fpn_1x_coco.py work_dirs/faster_rcnn_x101_32x4d_fpn_1x_coco/epoch_50.pth --out work_dirs/faster_rcnn_x101_32x4d_fpn_1x_coco/faster_rcnn_x101_32x4d_fpn_1x_coco_result.pkl --eval mAP")
# os.system("python3 test.py ../configs/faster_rcnn/faster_rcnn_x101_64x4d_fpn_1x_coco.py work_dirs/faster_rcnn_x101_64x4d_fpn_1x_coco/epoch_50.pth --out work_dirs/faster_rcnn_x101_64x4d_fpn_1x_coco/faster_rcnn_x101_64x4d_fpn_1x_coco_result.pkl --eval mAP")
# os.system("python3 test.py ../configs/faster_rcnn/faster_rcnn_hrnet_w32_hrfpn_coco.py work_dirs/faster_rcnn_hrnet_w32_hrfpn_coco/epoch_50.pth --out work_dirs/faster_rcnn_hrnet_w32_hrfpn_coco/faster_rcnn_hrnet_w32_hrfpn_coco_result.pkl --eval mAP")

os.system("python3 test.py ../configs/faster_rcnn/faster_rcnn_r50_pafpn_coco.py work_dirs/faster_rcnn_r50_pafpn_coco/epoch_50.pth --out work_dirs/faster_rcnn_r50_pafpn_coco/faster_rcnn_r50_pafpn_coco_result.pkl --eval mAP")
os.system("python3 test.py ../configs/faster_rcnn/faster_rcnn_x101_64x4d_fpn_1x_coco_iou.py work_dirs/faster_rcnn_x101_64x4d_fpn_1x_coco_iou/epoch_50.pth --out work_dirs/faster_rcnn_x101_64x4d_fpn_1x_coco_iou/faster_rcnn_x101_64x4d_fpn_1x_coco_iou_result.pkl --eval mAP")
os.system("python3 test.py ../configs/faster_rcnn/faster_rcnn_x101_64x4d_fpn_1x_coco_ciou.py work_dirs/faster_rcnn_x101_64x4d_fpn_1x_coco_ciou/epoch_50.pth --out work_dirs/faster_rcnn_x101_64x4d_fpn_1x_coco_ciou/faster_rcnn_x101_64x4d_fpn_1x_coco_ciou_result.pkl --eval mAP")
os.system("python3 test.py ../configs/faster_rcnn/faster_rcnn_x101_64x4d_fpn_1x_coco_giou.py work_dirs/faster_rcnn_x101_64x4d_fpn_1x_coco_giou/epoch_50.pth --out work_dirs/faster_rcnn_x101_64x4d_fpn_1x_coco_giou/faster_rcnn_x101_64x4d_fpn_1x_coco_giou_result.pkl --eval mAP")