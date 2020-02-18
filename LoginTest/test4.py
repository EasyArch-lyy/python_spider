#自动打码
# 只能探测工整的数字或经过训练的模型
import pytesseract
from PIL import Image
image=Image.open('timdddg.jpeg')
code=pytesseract.image_to_string(image)
print(code)