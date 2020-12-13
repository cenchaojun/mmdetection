#### 记录mmdetection安装过程

mmdetection是OpenMMLab开发的，还是很不错的，master 的分支是在pytorch1.3-1.6版本的，我先查看一下自己的版本

```python
import torch

print(torch.__version__)
```

1.4.0

可以看出我的版本是可以用这个master 分支的

如果想引用mmdetection的时候可以用https://arxiv.org/abs/1906.07155

但是有一个问题，就是我的python只是3.5,需要升级到3.6以上的，

果然不行，在安装mmcv的时候就出问题了，安装不上。

那首先升级python吧

See the [documentation](http://mmcv.readthedocs.io/en/latest) for more features and usage.

Note: MMCV requires Python 3.6+.

所以我将ubuntu升级一下，升级到18.04，希望不要出什么问题吧，出问题，我就去看电影去了

还是不乱动了，用conda来试一下吧，

首先安装一个anaconda

记得把anaconda加入到变量中

然后

```
conda create -n open-mmlab python=3.7 -y
conda activate open-mmlab
```

之后修改清华源

```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
```

再安装pytorch

```
conda install pytorch cudatoolkit=10.1 torchvision -c pytorch
```

一致安装不上这个

之后看到一个知乎上的一篇文章和我的很相似，我就用了他的方法，

[链接](https://zhuanlan.zhihu.com/p/102390034)

我刚开始也是安装官网的教程安装的

```
conda create -n open-mmlab python=3.7 -y
conda activate open-mmlab
```

因为我的cuda是10.1的，所以

```
conda install pytorch cudatoolkit=10.1 torchvision -c pytorch
```

之后安装下一步的操作的时候安装不上，没办法，看了别人的

中间还替换了清华源，因为我看下载太慢了

```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
```

下载速度超快，但是流量也花费的快

```
git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection
pip install mmcv # 这一部做错了，容易报错
python setup.py develop
```

```
, line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
ModuleNotFoundError: No module named 'mmcv._ext'

```

如果安装mmcv的话，就保存，后来查看了一下，mmdetection 和mmcv之间的版本匹配关系，发现我需要安装的是mmcv-full，碰巧在下面看到有安装全部的命令，并且要注意的是

在安装之前我需要把之前安装的mmcv的库卸载掉

```
pip unintall mmcv
```

之后才能安装full版本的库

```
pip install mmcv-full

```

这个安装需要花费一点时间，我的机器大概花费了4分钟，官网上说的是花费10分钟，耐心的等一下就可以了。

安装到这里，应该是可以了，明天好好学习一下，这个mmdetection怎么使用

###### 之后要在pycharm中，要打开的时候，需要将anaconda里面的python解释器，换成自己创建的环境中的python解释器
其实应该在git的时候要用自己的git帐号，这样好上传到自己的git上