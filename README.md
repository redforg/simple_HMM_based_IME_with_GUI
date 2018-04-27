# 介绍
简单的基于HMM模型的拼音输入法，利用PyQt5实现GUI界面。
# 环境要求
- python 3
- PyQt5 Qt Design([教程](https://www.jianshu.com/p/094928ac0b73))
- pickle

# 使用方法
## 可执行程序
- 下载文件夹，双击IME.exe
- 设置->训练，选择./data文件夹
- 设置->载入，选择*HMM_IME.pkl*文件
- 在输入框中输入拼音
- 若要选词或者是上下翻页，需要先回车。然后利用数字键选词、加减号翻页。再按回车，返回输入框。
## 源码运行
- 命令行输入
```{bash}
git clone https://github.com/cow8/simple_HMM_based_IME_with_GUI.git
cd simple_HMM_based_IME_with_GUI
python main.py
```
- 设置->训练，选择./data文件夹
- 设置->载入，选择*HMM_IME.pkl*文件
- 在输入框中输入拼音
- 若要选词或者是上下翻页，需要先回车。然后利用数字键选词、加减号翻页。再按回车，返回输入框。
## 修改源码
如果需要修改UI，可以利用Qt designer修改*.ui文件后，利用pyuic生成一个*.py的文件。这个*.py文件包含了对UI的定义。

# 代码结构
- ./main.py 生成一个UI窗口的实例
- ./viterbi.pypy 实现了Viterbi算法
- ./trainer.py 实现了从原始的语料数据中计算HMM模型的参数
- ./solver.py UI与viterbi算法中的中间层，主要将输入格式化成指定的格式、对多个子串调用viterbi算法、组织结构返回
- ./IME_UI.py 定义了UI窗口，调用trainer进行训练、调用mysolver更新候选词列表
- ./IME.ui 利用Qt designer生成的UI定义文件
- ./IME_generated.py 利用pyuic由IME.ui自动生成python的UI定义文件

## Viterbi算法中的变量定义
- encode_pinyin：将拼音字符串编码成数字
- encode_hanzi：将汉字编码成数字
- trans_mat：汉字与汉字之间的转移概率矩阵
- gen_mat：汉字生成某个拼音的矩阵
- pinyin2hanzi：某个拼音对应的所有可能汉字
- hanzi_fre：某个汉字的出现的频率（次数）