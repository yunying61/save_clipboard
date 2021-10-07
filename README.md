# save_clipboard（Windows剪贴板内容保存）

#### 介绍
本软件的用途是，把Windows剪贴板里的内容保存成文件。


#### 设计思路
先获取剪切板的内容，首先我们要打开剪切板，获取内容，这里我们需要定义一个函数实现其功能；
然后将内容存储到本地文件中，这里也需要定义一个函数；
最后我们在主函数实现循环获取剪切板内容。


#### 安装教程

1.  下载[发行版](https://gitee.com/yunying61/save_clipboard/releases)

#### 使用说明

1.  在英文路径下打开软件
2.  自动生成 'Clipboard' 和 'log' 目录
3.  'Clipboard' 目录保存的是剪贴板内容， 'log' 目录保存的是日志文件


#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支+
3.  提交代码
4.  新建 Pull Request

#### 原始贡献
感谢[Windows剪切板内容记录保存](https://cloud.tencent.com/developer/news/271514)的第一版代码给我的灵感
