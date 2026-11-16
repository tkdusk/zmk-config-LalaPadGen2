# LalaPadGen2 キーマップ運用メモ

## キーマップの編集・ビルド

Claude Code のスキル `lalapadgen2-keymap` を使う。

```
「キーマップを編集したい」
「ビルドして」
```

## ビルド方法

ビルドは GitHub Actions（`.github/workflows/build.yml`）で行う。ローカルビルド環境は持たない。

```bash
git add config/lalapadgen2.keymap
git commit -m "Update keymap"
git push
gh run watch -R tkdusk/zmk-config-LalaPadGen2
gh run download -R tkdusk/zmk-config-LalaPadGen2 <run-id> -D ~/Downloads/lalapadgen2-<run-id>
```

成果物: `lalapadgen2_left_rgbled_adapter-seeeduino_xiao_ble.uf2` / `lalapadgen2_right_rgbled_adapter-seeeduino_xiao_ble.uf2`（右側は ZMK Studio 有効）

## キーボードへの書き込み

1. リセットボタンをダブルクリック
2. マウントされたドライブに `.uf2` をコピー

## パスワードマクロ

`config/lalapadgen2.keymap` の `enter_pass` は `bindings = <&none>; // ENTER_PASS_PH` のプレースホルダーのまま commit する。
実際のキー列は GitHub Secret `ENTER_PASS_BINDINGS` に置き、ビルド時に `scripts/inject_secrets.py` が置換する（詳細は `CLAUDE.md`）。

commit 前にプレースホルダーが残っていることを必ず確認する:

```bash
grep -n "ENTER_PASS_PH" config/lalapadgen2.keymap
```
