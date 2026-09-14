import email
from email.header import decode_header
import imaplib
import os
import time

# --- 設定情報 ---
IMAP_SERVER = "imap.gmail.com"
EMAIL_ACCOUNT = "your_email@gmail.com"  # あなたのメールアドレス # 隠すこと
PASSWORD = "your_app_password"  # 発行したアプリパスワード # 隠すこと
TARGET_SUBJECT = "PC_SLEEP"  # トリガーとなる件名
CHECK_INTERVAL = 60  # チェック間隔（秒）


def check_email_and_sleep():
    try:
        # IMAPサーバーへ接続
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_ACCOUNT, PASSWORD)
        mail.select("inbox")

        # 未読メールを検索
        status, messages = mail.search(None, "UNSEEN")
        if status != "OK":
            return

        for num in messages[0].split():
            # メールデータを取得
            res, msg_data = mail.fetch(num, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])

                    # 件名の取得とデコード
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding or "utf-8")

                    # 件名が一致するか判定
                    if subject.strip() == TARGET_SUBJECT:
                        # 既読にして接続を閉じる
                        mail.store(num, "+FLAGS", "\\Seen")
                        mail.logout()

                        # Windowsをスリープ状態にするコマンド
                        os.system(
                            "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
                        )
                        return

        mail.logout()
    except Exception as e:
        print(f"エラーが発生しました: {e}")


if __name__ == "__main__":
    while True:
        check_email_and_sleep()
        time.sleep(CHECK_INTERVAL)