# Decisions

## Parry / Retreat prototype decisions

- `parry` の発生条件は `defender_block >= attacker_attack + 2`。
- `attacker_attack <= 0` の場合はパリィ判定を行わない。
- パリィされた攻撃側は、そのバトル中だけ `Block -2` を受ける。
- 同一バトル中のパリィによる `Block` 低下は累積させず、最大 `-2` とする。
- パリィされたプレイヤーは、次のバトルだけ「相手より多く伏せられない」制限を受ける。
- 両者が同時に次バトル制限を持つ場合、そのバトルでは制限を相殺し、通常ルールを使う。
- `retreat` は、自分の伏せカードが 1 枚以上あるときだけ選べる。
- `retreat` はそのバトルを `no_decision` 扱いで終了させる。
- `retreat` した側の伏せカードはすべて捨て札へ移動する。
- 相手は自分の伏せカードから 1 枚を手札へ戻せる。残りは捨て札へ移動する。
- `retreat` では `reveal / on_reveal` 効果を発動しない。

## Frontend-first decisions

- 現段階では Python 完全一致より、Web 版で人間が遊べることを優先する。
- `parry / retreat` の実装はまず TypeScript 側の本戦ループへ入れる。
- 判定や確認 UI は、ログとデバッグモードで追えることを優先し、演出は最小限にとどめる。
- ドラフトや CPU 思考より、まず本戦のターン進行とカード効果の見える化を優先する。
