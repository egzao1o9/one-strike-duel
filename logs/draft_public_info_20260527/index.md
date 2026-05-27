# Public-Info Draft Reports

## Summary

| Matchup | Matches | Draft Bot A | Win | Draft Bot B | Win | Draw |
|---|---:|---|---:|---|---:|---:|
| Standard vs Random | 100 | `StandardDraftBot` | 44.0% | `RandomDraftBot` | 45.0% | 11.0% |
| Standard vs Aggro | 100 | `StandardDraftBot` | 48.0% | `AggroDraftBot` | 41.0% | 11.0% |
| Standard vs Guard | 100 | `StandardDraftBot` | 38.0% | `GuardDraftBot` | 49.0% | 13.0% |

## Quick Read

- `StandardDraftBot` は `RandomDraftBot` とほぼ互角で、まだ明確な上振れは出ていません。
- `AggroDraftBot` には勝ち越しています。公開情報が増えた環境では、単純な高打点志向よりも受けと速度の両立が必要です。
- `GuardDraftBot` が現状最も安定しています。公開情報を見ながら防御寄りに組む方が、公開された強札への回答を用意しやすいです。
- `StandardDraftBot` は依然として `uncommon / rare` に寄りやすく、`common` の実戦投入が薄いです。`RandomDraftBot` が互角に持ち込めている理由の一つはここです。

## Action Shape

- `StandardDraftBot` のプレイ Bot は `set / set_pass / pass` がほぼ 1:1:1 に近く、旧 Bot 群よりは枚数の読み合いに入っています。
- `GuardDraftBot` 対戦では `StandardDraftBot` の先パス勝率が `30.4%` まで落ちており、公開情報を見て慎重に返す側が優勢です。
- `RandomDraftBot` 相手でも `StandardDraftBot` の勝者平均伏せ枚数はまだ高くなく、強カードを隠し持っての一撃に寄りがちです。

## Reports

- [Standard vs Random](./standard_vs_random/summary.md)
- [Standard vs Aggro](./standard_vs_aggro/summary.md)
- [Standard vs Guard](./standard_vs_guard/summary.md)
- [Sample Match: Standard vs Guard](./standard_vs_guard_match.md)
