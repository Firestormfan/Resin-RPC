# Resin-RPC
Discord Rich Presenceに現在の樹脂量を表示するプログラムです。
## Setup
1. install.batを実行する。
2. [HoYoLAB](https://hoyolab.com)にアクセスし、デベロッパーツール(F12)を開く。
3. Applicationタブに移動し、ストレージ -> Cookie -> `https://hoyolab~~`に進む。
4. その中の`ltuid`/`ltoken`をconfig.jsonに入力する。
5. run.batを実行し、正常動作すれば完了。
## config
| key | value |
|:------------ |:------------|
| ltuid        | HoYoLABのltuid。 |
| ltoken       | HoYoLABのltoken。|
| details      | ステータスメッセージ。後述の変数が使用可能。|
| show_remains | 完全回復までの残り時間を表示するか。|
## dialogue
パイモンにカーソルを合わせたときのセリフを変更できる。5分ごとにランダムに変更される。
## 変数
| 変数名 | 効果 |
|:---|:---|
| {resin_now} | 現在の樹脂量を返す。 |
## Known Bugs
<dl>
    <dt>変数名を誤字った状態で起動すると、エラーが発生する</dt>
    <dd>・修正する気はありません。</dd>