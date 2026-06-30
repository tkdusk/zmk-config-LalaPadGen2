# LalaPadGen2 ZMK Config - ローカルコンテキスト

## パスワードマクロの仕組み

`enter_pass` マクロのキーコード列はリポジトリに平文で書かず、GitHub Secret `ENTER_PASS_BINDINGS` で管理している。

- `config/lalapadgen2.keymap` の bindings は `<&none>; // ENTER_PASS_PH` プレースホルダー
- `scripts/inject_secrets.py` がビルド前に置換する
- `.github/workflows/build.yml` の "West Zephyr export" と "West Build" の間に注入ステップがある

## build.yml に再挿入が必要な場合

```yaml
      - name: Inject secret macros
        env:
          ENTER_PASS_BINDINGS: ${{ secrets.ENTER_PASS_BINDINGS }}
        run: python3 scripts/inject_secrets.py
```

配置場所: `West Zephyr export` ステップと `West Build` ステップの間

## GitHub Secret の登録

リポジトリ Settings → Secrets and variables → Actions → Repository secrets で
`ENTER_PASS_BINDINGS` に `&kp` シーケンスをスペース区切りで登録する。
例: `&kp LS(K) &kp LS(A) &kp O ...`

## ZMK Extra Modules

```
${GITHUB_WORKSPACE};${GITHUB_WORKSPACE}/zmk-driver-iqs9151;${GITHUB_WORKSPACE}/zmk-easy-charge-indicator;${GITHUB_WORKSPACE}/zmk-rgbled-widget
```
