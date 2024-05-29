from PIL import Image

def display_image_info(image_path):
    try:
        img = Image.open(image_path)

        print("图像大小:", img.size)

        print("图像格式:", img.format)

        print("图像色彩模式:", img.mode)

        img.show()

    except FileNotFoundError:
        print("找不到文件，请确保路径正确。")

image_path = Z:\1-МД-17 алгоритмизация\1-МД-17-ZHAOZESEN\ZZSNB.jpg



display_image_info(image_path)