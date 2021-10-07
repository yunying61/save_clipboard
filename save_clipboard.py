# 获取电脑剪切板信息
import os.path
import time
import win32clipboard as wc


# 设计思路
# 先获取剪切板的内容，首先我们要打开剪切板，获取内容，这里我们需要定义一个函数实现其功能；
# 然后将内容存储到本地文件中，这里也需要定义一个函数；
# 最后我们在主函数实现循环获取剪切板内容。

# 输出为日志
def save_to_log(log):
    # 确认是否有 log 目录
    exist_dir = os.path.exists('log')
    if exist_dir is False:
        # 如果没有 log 目录则创建
        os.mkdir('log', 3)
    try:
        # 获取时间
        t = time.strftime('%Y-%m-%d-%H:%M:%S')
        # 打开 save_clipboard.log 文件，写入日志
        with open('.\\log\\save_clipboard.log', 'a+') as f:
            f.write('[' + t + ']    ' + log + '\n')
    except Exception as e_save_to_log:
        t = time.strftime('%Y-%m-%d-%H:%M:%S')
        # 打开 save_clipboard.log 文件，写入错误日志
        with open('.\\log\\save_clipboard.log', 'a+') as f:
            f.write('[' + t + ']    ' + '日志写入失败！错误内容：' + str(e_save_to_log) + '\n')


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
    except Exception as e_get_clipboard:
        t = time.strftime('%Y-%m-%d-%H:%M:%S')
        # 打开 save_clipboard.log 文件，写入错误日志
        with open('.\\log\\save_clipboard.log', 'a+') as f:
            f.write('[' + t + ']    ' + '剪贴板内容获取失败！错误内容：' + str(e_get_clipboard) + '\n')


# 将内容存储到本地文件
def save_to_file(data):
    # 确认是否有 Clipboard 目录
    exist_dir = os.path.exists('Clipboard')
    if exist_dir is False:
        # 如果没有 Clipboard 目录则创建
        os.mkdir('Clipboard', 3)
    try:
        t1 = time.strftime('%Y-%m-%d')
        t2 = time.strftime('%Y-%m-%d-%H:%M:%S')
        with open('.\\Clipboard\\剪切板内容-{}.txt'.format(t1), 'a+') as f:
            f.write(t2 + '----------------------------------------\n' + data + '\n' + '\n')
        with open('.\\log\\save_clipboard.log', 'a+') as f:
            f.write('[' + t2 + ']    ' + '剪贴板内容保存成功' + '\n')
    except Exception as e_save_to_file:
        t = time.strftime('%Y-%m-%d-%H:%M:%S')
        # 打开 save_clipboard.log 文件，写入错误日志
        with open('.\\log\\save_clipboard.log', 'a+') as f:
            f.write('[' + t + ']    ' + '文件保存失败！错误内容：' + str(e_save_to_file) + '\n')


if __name__ == '__main__':
    try:
        # 提示用户程序正在运行
        print('程序正在运行...')
        save_to_log('程序开始运行')
        # 读取剪切板上一时刻的剪切内容
        last_data = get_clipboard()

        while True:
            # 每隔2s读取剪切板的内容
            time.sleep(2)
            # 读取剪切板内容
            now_data = get_clipboard()
            # 如果当前的内容与上一时刻的内容不一致,则写入文件
            if now_data != last_data:
                save_to_file(now_data)

                # 用当前的剪切板内容替换为上一时刻的内容,等待下一次的复制、剪切
                last_data = now_data
    except Exception as e_main:
        t_main = time.strftime('%Y-%m-%d-%H:%M:%S')
        # 打开 save_clipboard.log 文件，写入错误日志
        with open('.\\log\\save_clipboard.log', 'a+') as f_main:
            f_main.write('[' + t_main + ']    ' + '程序运行出错！错误内容：' + str(e_main) + '\n')
