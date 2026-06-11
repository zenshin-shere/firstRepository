import os
import glob
import shutil

def move_mp4_to_parent():
    # プログラムが実行されたフォルダ（カレントディレクトリ）を取得
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    
    # サブフォルダ内も含めてすべての .mp4 ファイルを検索
    mp4_files = glob.glob(os.path.join(current_dir, "**", "*.mp4"), recursive=True)
    
    if not mp4_files:
        print("mp4ファイルが見つかりませんでした。")
        return

    for file_path in mp4_files:
        file_name = os.path.basename(file_path)
        dest_path = os.path.join(parent_dir, file_name)
        
        # 移動先に同名ファイルがないかチェック
        if os.path.exists(dest_path):
            print(f"スキップ（同名ファイルが既に存在します）: {file_name}")
            continue
            
        try:
            shutil.move(file_path, parent_dir)
            print(f"移動成功: {file_name} -> {parent_dir}")
        except Exception as e:
            print(f"エラー発生 ({file_name}): {e}")

if __name__ == "__main__":
    move_mp4_to_parent()