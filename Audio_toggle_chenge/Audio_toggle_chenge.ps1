# ToggleAudio.ps1

# --- 設定：デバイス名のキーワード ---
# キーワード→ 完全に書く必要はない
# 日本語が含まれる場合は、ファイルの保存エンコードに注意してください(UTF-8 BOM付 推奨)
$Device1_Keyword = "*スピーカー (2- BRIDGE CAST V2*" #スピーカーA
$Device2_Keyword = "スピーカー (2- Yamaha ZG02)" #スピーカーB

# ----------------------------------

# 現在の既定の再生デバイスを取得
try {
    $CurrentDevice = Get-AudioDevice -Playback
} catch {
    Write-Host "AudioDeviceCmdletsが見つからないか、エラーが発生しました。"
    exit
}

# 現在のデバイス名とキーワードを比較して切り替え
if ($CurrentDevice.Name -like $Device1_Keyword) {
    # 現在が [A] なので -> [B] に切り替え
    Write-Host "Switching to MixAmp..."
    Get-AudioDevice -List | Where-Object Name -like $Device2_Keyword | Set-AudioDevice -Verbose
}
else {
    # 現在が [A] 以外 (A含む) なので -> [A] に切り替え
    Write-Host "Switching to BRIDGE CAST..."
    Get-AudioDevice -List | Where-Object Name -like $Device1_Keyword | Set-AudioDevice -Verbose
}