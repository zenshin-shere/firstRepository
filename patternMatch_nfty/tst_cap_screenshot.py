import cv2
import os
from datetime import datetime

# 設定
DEVICE_ID = 0
SAVE_DIR = "screenshots"

# 保存先フォルダを作成
os.makedirs(SAVE_DIR, exist_ok=True)

# キャプチャーボードを開く
cap = cv2.VideoCapture(DEVICE_ID, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("映像デバイスを開けませんでした")
    raise SystemExit(1)

try:
    # 映像を1フレーム取得
    ret, frame = cap.read()

    if not ret:
        print("映像を取得できませんでした")
        raise SystemExit(1)

    # ファイル名を生成
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = os.path.join(SAVE_DIR, f"capture_{timestamp}.jpg")

    # スクリーンショットを保存
    if cv2.imwrite(filename, frame):
        print(f"保存しました: {filename}")
    else:
        print("画像の保存に失敗しました")

finally:
    cap.release()
