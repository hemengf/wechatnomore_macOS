# -*- mode: python -*-

block_cipher = None


a = Analysis(['myclient.pyw'],
             pathex=['C:\\Users\\nagellab\\Desktop\\wechatnomore_macOS'],
             binaries=[],
             datas=[('ATone.mp3','.'),('Blop.mp3','.'),('transparent.png','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='myclient',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='myclient')
