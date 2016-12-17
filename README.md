# bioplot

使用Python的matplotlib高仿各种生信工具的绘图结果。

High imitation some bioinformatics tools result by python matplotlib.

## 使用 Usage

```shell
$　python pyfile.py <INPUT-FILE>
```

本仓库中的大多数脚本都是这样使用的。

Most script of this repository use like this way.

## 依赖 Requirement

只能运行在Python3环境下，依赖包括但不限于以下的包：

Python3 only and they requirement packages include but not only:

- docopt 用于解析参数 use to parse command line args

- biopython 生信必备，你懂的  uah, you know it is for bioinformatics

- matplotlib 用于绘图 use to plot

- numpy 数据统计 data statistics

## 详细说明 description 

1. qualityboxplot.py

   这个脚本绘制了在测序质量检测中最重要的质量分布盒状图，原图

   ![qualityboxplot_by_fastqc.png]([https://raw.githubusercontent.com/yangmqglobe/bioplot/master/image/qualityboxplot_by_fastqc.png)

   使用我的脚本绘制的图片

   ![qualityboxplot_by_myscript.png](https://raw.githubusercontent.com/yangmqglobe/bioplot/master/image/qualityboxplot_by_myscript.png)

   整体视觉是差不多的，但是fastqc考虑到整体的效果，对中间的一些位置进行的合并，也即其并没有完全绘制出所有位置的质量效果。目前存在的问题是，如果reads输入很多，那么整个质量矩阵将非常大，那么首先内存可能就撑不住，可能处理上就会有问题。