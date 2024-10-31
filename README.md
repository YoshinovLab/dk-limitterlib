# LimiterLib

このプロジェクトは、日付ごとに CSV ファイルにログエントリを記録し、エントリ数が指定された制限に達したかどうかを確認するシンプルなログ記録システムです。Python を使用して実装されており、柔軟な設定と簡単な操作が特徴です。

## ディレクトリ構造

プロジェクトのディレクトリ構造は以下のようになります：

```
your_project/
├── limitterlib
├── your_project.py
└── logs/
    └── YYYYMMDD.csv
```

### 手順

1. **リポジトリのクローン**

   ```bash
   cd limitterlibをクローンしたいディレクトリ
   git clone https://github.com/YoshinovLab/dk-limitterlib.git
   ```


## 使用方法

[サンプルコードはこちら](samples/test.py)を参照してください。

- **LOG_DIR**: ログファイルを保存するディレクトリ。存在しない場合は自動的に作成されます。
- **LIMIT**: 各ログファイルに記録できるエントリの最大数。標準は6です。

