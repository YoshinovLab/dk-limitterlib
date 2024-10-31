import limiterlib

if limiterlib.is_limited():
    print(f"ログのエントリ数が制限値 ({limiterlib.LIMIT}) に達しています。")
else:
    limiterlib.record()
    print("新しいログエントリを記録しました。")
