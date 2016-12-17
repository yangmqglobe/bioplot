# -*- coding:utf-8 -*-
"""
@author: yangmqglobe
@file: qualityboxplot.py
@time: 2016/12/17
"""
from Bio import SeqIO
import numpy as np
import matplotlib.pyplot as plt
from docopt import docopt

USAGE = """
Usage:
    qualityboxplot.py <FASTQ-FILE>
"""
args = docopt(USAGE)
filepath = args['<FASTQ-FILE>']
# 使用Biopython读取quality
records = SeqIO.parse(filepath, 'fastq')
qualitylist = []
for record in records:
    qualitylist.append(record.letter_annotations['phred_quality'])
    # break
# 将质量二维数组转换为矩阵
qualities = np.array(qualitylist)
# 获得每个位点的平均值
means = qualities.mean(axis=0)
# 填充背景颜色
plt.axhspan(28, 40, facecolor='green', alpha=0.3, linewidth=0)
plt.axhspan(20, 28, facecolor='orange', alpha=0.3, linewidth=0)
plt.axhspan(0, 20, facecolor='red', alpha=0.3, linewidth=0)
# 填充白色的分隔条
for i in range(1, qualities.shape[1], 2):
    plt.axvspan(i+0.5, i+1.5, facecolor='white', alpha=0.3, linewidth=0)
# 绘制盒形图
qualitiesplot = plt.boxplot(qualities, showfliers=False, patch_artist=True)
# 填充盒形图的颜色
for patch in qualitiesplot['boxes']:
    patch.set_color('black')
    patch.set_facecolor('yellow')
# 填充盒形图须的颜色和线型
for patch in qualitiesplot['whiskers']:
    patch.set_color('black')
    patch.set_linestyle('-')
# 绘制平均值的折线
plt.plot([x for x in range(1, qualities.shape[1]+1)], means)
# 调整X轴坐标，防止其粘连
plt.xticks(rotation=90)
# 限制Y轴的大小
plt.ylim(ymax=40)
# 填充Y轴数字
plt.yticks([y for y in range(41)])
# X轴的标题
plt.xlabel("Position in read (bp)")
# 主标题
plt.title("Quality score across all bases")
plt.show()
