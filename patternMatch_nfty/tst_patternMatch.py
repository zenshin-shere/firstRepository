import cv2
import numpy as np

img1 = cv2.imread("pic02_gameSS1.png")
img2 = cv2.imread("pic03_gameSS2.png")

if img1 is None or img2 is None:
    raise FileNotFoundError("画像を読み込めません")

if img1.shape != img2.shape:
    raise ValueError("画像のサイズが一致していません")

# 各画素のRGB値の絶対差
diff = np.abs(img1.astype(np.int16) - img2.astype(np.int16))

# 平均絶対誤差（0～255）
mae = np.mean(diff)

# 誤差を0～100%の範囲に変換した一致度
similarity = (1 - mae / 255) * 100

print(f"平均絶対誤差: {mae:.2f}")
print(f"一致度: {similarity:.2f}%")