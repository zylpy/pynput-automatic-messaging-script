from pynput import mouse,keyboard
import time as t

m = mouse.Controller()
c = keyboard.Controller()
tt = input('请输入文本:')
cc = int(input('请输入次数:'))
def debug_mouse():
    """调试用：打印当前鼠标位置"""
    print(f"当前鼠标位置: {m.position}")

def enter(text):
    c.type(text)          # 输入文本
    t.sleep(0.2)          # 短暂延迟
    c.press(keyboard.Key.enter)  # 按下回车
    c.release(keyboard.Key.enter)  # 释放回车
    print(f"已尝试发送: {text}")

def chat(message):
    # 1. 移动鼠标到输入框并点击（确保焦点）
    debug_mouse()  # 打印初始位置
    input("手动将鼠标移动到输入框，按回车记录位置...")
    input_x, input_y = m.position  # 记录输入框位置
    print(f"记录输入框位置: ({input_x}, {input_y})")

    # 2. 点击输入框激活
    m.position = (input_x, input_y)
    m.click(mouse.Button.left, 1)
    t.sleep(0.5)
    # 3. 输入并发送消息
    for i in range(cc+1):
        enter(message)
        t.sleep(0.5)

# 示例：发送消息
chat(tt)
