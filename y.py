import datetime
import pyqrcode
from PIL import Image

def generate_qr_code(input_text, mode):
    # 获取当前时间的时间戳
    current_time = datetime.datetime.now().timestamp()
    # 构建待转换的字符串
    encoded_text = f"{input_text}|{int(current_time)}|{mode}"
    # 生成二维码
    qr = pyqrcode.create(encoded_text)
    # 保存二维码图片
    qr.png(f'qrcode_{mode}.png', scale=8)
    # 直接展示二维码
    qr.show()

# 输入你的字符
input_text = input("请输入要转换为二维码的字符：")

# 生成 QD 二维码
generate_qr_code(input_text, "QD")

# 按下回车后生成 QT 二维码
input("按下回车键继续生成 QT 二维码：")
generate_qr_code(input_text, "QT")
