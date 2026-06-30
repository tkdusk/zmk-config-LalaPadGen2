# LalaPadGen2 キーマップ運用メモ

## キーマップの編集・ビルド

Claude Code のスキル `lalapadgen2-keymap` を使う。

```
「キーマップを編集したい」
「ビルドして」
「左側だけビルドして」
```

## ビルド方法（手動）

```bash
./build.sh all    # 左右両方
./build.sh left   # 左側のみ
./build.sh right  # 右側のみ（ZMK Studio 有効）
```

成果物: `lalapadgen2_left.uf2` / `lalapadgen2_right.uf2`

## キーボードへの書き込み

1. リセットボタンをダブルクリック
2. マウントされたドライブに `.uf2` をコピー

## セットアップ（初回のみ）

### 1. 共有ビルド環境（~/src/zmk-workspace）を初期化

```bash
source ~/src/zmk-workspace/.venv/bin/activate
cd ~/src/zmk-workspace
west init -m https://github.com/zmkfirmware/zmk --mr v0.3-branch
west update
```

### 2. LalaPadGen2 固有モジュールを clone

```bash
mkdir -p ~/src/zmk-modules-lalapad
git clone --depth=1 https://github.com/ShiniNet/zmk-driver-iqs9151 ~/src/zmk-modules-lalapad/zmk-driver-iqs9151
git clone --depth=1 https://github.com/ShiniNet/zmk-easy-charge-indicator ~/src/zmk-modules-lalapad/zmk-easy-charge-indicator
git clone --depth=1 -b v0.3 https://github.com/caksoylar/zmk-rgbled-widget ~/src/zmk-modules-lalapad/zmk-rgbled-widget
```

Python venv: `~/src/zmk-workspace/.venv`（`build.sh` が自動で activate する。`west` コマンドを手動で使う場合は先に `source ~/src/zmk-workspace/.venv/bin/activate` が必要）

## keymap の git 管理について

`config/lalapadgen2.keymap` はパスワード入力マクロを含むため git に露出しない:

- `git update-index --skip-worktree` で保護済み
- `git status` に変更が出ない、`git push` にも含まれない
- `git pull` で他ファイルの変更は通常通り取得できる

**keymap のバックアップは別途必要**（1Password 等）

upstream の keymap 変更を取り込みたい場合のみ:
```bash
git update-index --no-skip-worktree config/lalapadgen2.keymap
git pull
git update-index --skip-worktree config/lalapadgen2.keymap
```

## gitignore 対象

```
build/
*.uf2
README.md   ← このファイル
```
