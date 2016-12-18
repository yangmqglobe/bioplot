# -*- coding:utf-8 -*-
"""
@author: yangmqglobe
@file: qualitylineplot.py
@time: 2016/12/18
"""
from docopt import docopt
from Bio import SeqIO
from matplotlib import pyplot as plt
import numpy as np

USAGE = """
Usage:
    qualitylineplot.py <FASTQ-FILE>
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
# 统计各个分数出现的频数
quality, counts = np.unique(qualities, return_counts=True)
# 求得质量最小值
minquality = min(quality)
# 填充背景条纹
for x in range(minquality-1, 40, 2):
    plt.axvspan(x+0.5, x+1.5, facecolor='grey', alpha=0.3, linewidth=0)
# 添加X轴标题
plt.xlabel("Mean Sequence Quality (Phred Score)")
# 添加X轴标尺
plt.xlim(minquality-1, 40)
plt.xticks([x for x in range(minquality-1, 41)])
# 添加横向网格
plt.grid(axis='y', linestyle='-', color='grey')
# 添加标题
plt.title("Quality score distribution over all sequence")
# 绘制折线
plt.plot(quality, counts, 'r',  label='Average Quality per read', linewidth=2)
# 开启示例
plt.legend()
plt.show()
