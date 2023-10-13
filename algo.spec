# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['algo.py'],
    pathex=[],
    binaries=[('ffmpeg.exe', '.')],
    datas=[('topic.csv', '.'), ('audio', '.'), ('chatgpt_dumps', '.'), ('generated_video', '.'), ('srt', '.'), ('stock_image', '.'), ('subtitle_generator', '.'), ('ffmpeg.exe', '.'), ('C:\\Users\\wind\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python38\\site-packages\\whisper', 'whisper'), ('api_keys.txt', '.'), ('youtube_uploader', '.'), ('client_secrets.json', '.')],
    hiddenimports=['googleapiclient', 'googleapiclient.discovery', 'googleapiclient.errors', 'googleapiclient.http', 'oauth2client', 'oauth2client.client', 'oauth2client.file', 'oauth2client.tools'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='algo',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='algo',
)
