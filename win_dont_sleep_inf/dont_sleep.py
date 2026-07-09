import time
import ctypes
import sys

# 設定：分単位
minutes = 15
total_seconds = minutes * 60
end_time = time.time() + total_seconds

print("このウィンドウがある間はスリープは停止されます")
print(f"予定時間: {minutes} 分")

# スリープとスクリーンセーバーの両方を無効化 (ES_CONTINUOUS | ES_SYSTEM_REQUIRED)
# →OS機能を使用
ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

# カウントダウン
try:
    while time.time() < end_time:
        # 残り時間を計算
        remaining = int(end_time - time.time())
        mins, secs = divmod(remaining, 60)
        
        # 同じ行に残り時間を表示
        # \r はカーソルを行頭に戻し、end="" で改行を防ぎます
        print(f"\r残り時間: {mins:02d}:{secs:02d} ", end="", flush=True)
        
        # 1秒待機
        time.sleep(1)

    print("\n予定時間が経過しました。")

except KeyboardInterrupt:
    print("\nユーザーによって中断されました。")

finally:
    # スリープとスクリーンセーバーの設定を元に戻す (ES_CONTINUOUS)
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
    print("スリープ防止機能を解除しました。")