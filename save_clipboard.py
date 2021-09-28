# 获取电脑剪切板信息

import time
import win32clipboard as wc


# 设计思路
# 先获取剪切板的内容，首先我们要打开剪切板，获取内容，这里我们需要定义一个函数实现其功能；
# 然后将内容存储到本地文件中，这里也需要定义一个函数；
# 最后我们在主函数实现循环获取剪切板内容。

# 获取剪切板的内容
def get_clipboard():
    try:
        # 调用win32clipboard的OpenClipboard方法打开剪切板
        wc.OpenClipboard()
        # 获取剪切板内容
        data = wc.GetClipboardData()
        # 关闭剪切板
        wc.CloseClipboard()
        # 返回获取的内容
        return str(data)
    except:
        print("剪切板内容获取失败！")


# 将内容存储到本地文件
def save_to_file(data):
    try:
        t = time.strftime('%Y-%m-%d')
        with open('剪切板内容-{}.txt'.format(t), 'a+') as f:
            f.write(data + '\n')
            print('已保存！')
    except:
        print('文件保存失败！')


if __name__ == '__main__':
    try:
        # 提示用户程序正在运行
        print('程序正在运行...')
        # 读取剪切板上一时刻的剪切内容
        last_data = get_clipboard()

        while True:
            # 每隔60s读取剪切板的内容
            time.sleep(60)
            # 读取剪切板内容
            now_data = get_clipboard()
            # 如果当前的内容与上一时刻的内容不一致,则写入文件
            if now_data != last_data:
                save_to_file(now_data)

                # 用当前的剪切板内容替换为上一时刻的内容,等待下一次的复制、剪切
                last_data = now_data
    except:
        print('程序运行出错！')
