import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# 載入圖片
image = cv2.imread('image.png')

# 將BGR轉換為RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pil_image = Image.fromarray(image)

# 在圖片上加入文字
font_path = "front.ttf"  # 替換成你的字型檔案路徑
font_size = 32
font = ImageFont.truetype(font_path, font_size)
draw = ImageDraw.Draw(pil_image)
text = "你要的中文字"  # 要顯示的中文文字
draw.text((50, 50), text, font=font, fill=(255, 0, 0))

# 將PIL圖片轉換回OpenCV格式
image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

# 顯示圖片
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
