# Codex作業指示書: One Strike Duel パリィ / 撤退ルール実装

このファイルは、CodexのGoal mode / Worktree / Cloud taskにそのまま渡すための作業チケットです。  
ゲームの面白さ・バランスの最終判断は人間が行います。Codexは、下記仕様を壊さずに最小実装・テスト・報告を行ってください。

---

## /goal 用プロンプト

```md
目的:
One Strike Duelの本戦に、検証用ルールとして「パリィ」と「撤退」を追加してください。

背景:
現在の本戦では、攻撃値を積めるだけ積む総力戦になりやすく、攻撃する/守る以外の行動選択が薄くなっています。
今回の検証では、一撃で勝敗が決まる思想は維持したまま、以下を狙います。

- 攻撃を「通れば勝ち」だけでなく「読まれると危険」な行動にする
- 防御を「耐える」だけでなく「読めばカウンターに繋がる」行動にする
- 勝てないと思った時に、戦わない選択肢として撤退を追加する
- 撤退は無料回避ではなく、明確なリソース損を伴う行動にする

対象範囲:
- 既存のBattle / Reveal / Result解決処理
- BattleAction / action_type 周辺
- Botの最低限の合法手判定
- 既存ログ / デバッグログ / summary出力
- 必要なテストまたは手動確認手順
- docs/DECISIONS.md, docs/TEST_PLAN.md など関連ドキュメント

成功条件:
- パリィ条件を満たした時、攻撃側にそのバトル中だけBlock -2が適用される
- パリィされたプレイヤーに、次のBattleだけ「相手より多く伏せられない」制限が付与される
- 撤退 action_type を追加し、自分のアクション時に宣言できる
- 撤退時、撤退側の伏せカードは全て捨て札へ移動する
- 撤退時、相手は自分の伏せカードから1枚を手札に戻せる
- 撤退したBattleは決着なしとして終了する
- 既存の通常勝敗判定、set / set_pass / pass の基本挙動を壊さない
- パリィ/撤退の発生がログとsummaryで追える
- 既存テスト・ビルド・実行可能なチェックを実行し、結果を報告する

制約:
- 大規模リファクタは禁止
- 保存形式や外部APIを勝手に変更しない
- 既存カードデータの大規模調整はしない
- 仕様判断が必要な場合は、最小実装を選び docs/DECISIONS.md に記録する
- 複数システムを大きく跨ぐ設計変更が必要になった場合は止まって報告する

停止条件:
- 既存のBattle解決モデルではパリィ/撤退を自然に表現できず、大規模な設計変更が必要な場合
- 撤退時のカード移動や非公開情報の扱いに、既存仕様と矛盾する不明点がある場合
- 実装後、既存の主要テストや基本対戦が壊れ、原因が特定できない場合

完了時の報告:
- 変更内容
- 変更ファイル
- 実行したチェック
- パリィ/撤退の簡単な動作例
- 既知の残課題
- 次に人間がテストプレイで確認すべき観点
```

---

# Task

## 目的

One Strike Duelの本戦に、以下の2ルールを追加する。

1. **パリィ**
2. **撤退**

この変更は、ゲームを完成仕様に固定するためではなく、  
**攻撃のリスク化と戦略的撤退が本戦の選択肢を増やすか検証するための強めのプロトタイプ実装**である。

---

## 背景

現状の本戦では、プレイヤーが以下のような行動に寄りやすい。

```txt
攻撃が多い手札なら決めに行く
防御が多い手札なら守る
判断というより、引いた手札の方向性に従う
攻撃値を積めるなら積む
負けたら終わりなので、温存や撤退がしづらい
```

今回の仮説は以下。

```txt
攻撃がパリィされるリスクを持てば、雑な攻撃が減る。
撤退を許せば、弱い手札でも無謀に突っ込む以外の選択ができる。
ただし撤退にはコストを持たせることで、逃げ得にはしない。
```

---

## 対象範囲

Codexは、実際のリポジトリ構造を調査したうえで、必要最小限の範囲を変更すること。

主な想定対象:

```txt
engine/
  phase_runner.py
  resolver.py
  effects.py
  analysis.py
  card.py

bots/
  base_bot.py
  public_info_bot.py
  registry.py

data/
  cards.json

docs/
  DECISIONS.md
  TEST_PLAN.md
  KNOWN_ISSUES.md
```

ただし、実際のファイル名や責務が異なる場合は、既存構造に従うこと。

---

## やらないこと

今回やらないこと:

- カードプール全体のバランス調整
- ドラフト仕様の変更
- UIの大規模リデザイン
- オンライン対戦実装
- セーブ形式の変更
- 既存Battle解決の大規模リファクタ
- パリィ/撤退前提のカード効果追加
- ルールの最終バランス確定

---

# 仕様1: パリィ

## 概要

攻撃が防御に大きく止められた場合、攻撃側はパリィされたものとして扱う。  
パリィされたプレイヤーは、以下の2つの不利を受ける。

1. **そのバトル中だけ Block -2**
2. **次のBattleだけ、相手より多く伏せられない**

今回の検証では、攻撃が読まれた時の重さをあえて強めに体験したい。  
そのため、パリィ不利はやや重めに実装する。

---

## パリィ発生条件

攻撃判定時、以下を満たした場合にパリィが発生する。

```txt
defender_block >= attacker_attack + PARRY_MARGIN
```

初期定数:

```python
PARRY_MARGIN = 2
PARRY_BLOCK_DEBUFF = -2
```

重要:

```txt
attacker_attack <= 0 の場合は攻撃していない扱いとし、パリィ判定対象外にする。
```

例:

```txt
攻撃側 Attack = 2
防御側 Block = 4

4 >= 2 + 2
→ パリィ発生
```

```txt
攻撃側 Attack = 3
防御側 Block = 4

4 >= 3 + 2 を満たさない
→ 攻撃は防がれるが、パリィは発生しない
```

---

## パリィ効果A: そのバトル中だけ Block -2

パリィされた攻撃側は、そのBattle解決中だけBlock -2を受ける。

```txt
parried_player.current_battle_block_modifier += PARRY_BLOCK_DEBUFF
```

初期実装では、同一Battle中に複数回パリィされた場合も、Block低下は累積させない。

```txt
同一Battle中のパリィBlock低下は最大 -2
```

理由:

- 初回検証で効果を読みやすくするため
- 多段パリィによる過剰な即死を避けるため
- ログ分析をしやすくするため

必要なら後で累積ルールを検討する。

---

## Block -2 の適用タイミング

Block -2 は、パリィ発生後の残りの攻撃判定に適用する。

```txt
先に攻撃
↓
防御側が大きく防ぐ
↓
攻撃側がパリィされる
↓
攻撃側のBlockがそのBattle中だけ-2
↓
防御側の反撃判定がある場合、その低下後Blockを参照する
```

同速などで同時攻撃がある場合は、既存の同時処理方針を尊重する。  
ただし、同時攻撃の片方で発生したパリィBlock低下が、同時解決中の相手攻撃に retroactive に影響しないように注意する。

方針:

```txt
同時攻撃は、同じタイミングの攻撃判定を先に処理し、
その後にパリィ由来のBlock低下を確定させる。
```

既存の処理モデル上これが難しい場合は、最小変更で実装できる形を選び、docs/DECISIONS.md に記録する。

---

## パリィ効果B: 次のBattleだけ相手より多く伏せられない

パリィされたプレイヤーは、次のBattle中、伏せ枚数制限を受ける。

通常ルール:

```txt
own_facedown_count <= opponent_facedown_count + 1
```

パリィ後の次Battle制限:

```txt
own_facedown_count <= opponent_facedown_count
```

つまり、パリィされた側は、次のBattleでは相手より多くカードを伏せられない。

この制限は、次のBattleが終了した時点で解除する。  
撤退・決着なし・通常決着のどれで終わっても解除する。

---

## 両者が同時に次Battle制限を持つ場合

両者が同時に「相手より多く伏せられない」制限を持つと、互いに最初の1枚を出せず、Battleが停滞する可能性がある。

初期実装では、以下の安全策を入れる。

```txt
両者が同時に parry_next_battle_limit を持つ場合、そのBattleでは両者の制限を相殺し、通常の伏せ枚数ルールを使う。
```

この場合はログに以下を記録する。

```txt
parry_limit_cancelled_for_both = true
```

---

## パリィ状態の管理

プレイヤーごとに、最低限以下の状態を持つ。

```python
current_battle_parried = bool
current_battle_block_debuff = int
parry_next_battle_limit = bool
```

ライフやHPのような永続リソースは追加しない。  
これはあくまで、一撃決殺ルールを維持したまま、攻撃失敗のリスクを表現するための一時状態である。

---

# 仕様2: 撤退

## 概要

Battle中、自分のアクション時に撤退を宣言できる。  
撤退は、そのBattleでの死亡リスクを避ける行動だが、リソース損を伴う。

---

## 撤退アクション

BattleActionに新しい action_type を追加する。

```txt
retreat
```

想定:

```python
BattleAction(
    player_id="p1",
    action_type="retreat",
    card_ids=[],
)
```

---

## 撤退の宣言タイミング

撤退は、自分のBattleアクション時に宣言できる。

```txt
set / set_pass / pass / retreat
```

の選択肢の1つとして扱う。

Reveal中、Reveal後、Result後の撤退はできない。

---

## 撤退の合法条件

初期検証では、無料撤退を避けるため、以下を合法条件にする。

```txt
own_facedown_count > 0
```

自分の伏せカードが0枚の場合、撤退は選べない。  
その場合は通常の pass を使う。

理由:

- 伏せ0枚で撤退できると、リソース損なしで危険だけを避けられる可能性がある
- 撤退に「すでに踏み込んだが、危険を感じて下がる」ニュアンスを持たせたい

この条件がプレイ感に合わなければ、後で緩和する。

---

## 撤退時の処理

プレイヤーが撤退した場合、以下の順で処理する。

```txt
1. Battleを即終了する
2. 撤退したプレイヤーの伏せカードをすべて捨て札へ移動する
3. 相手は自分の伏せカードから1枚選んで手札に戻してよい
4. 相手の残りの伏せカードは捨て札へ移動する
5. このBattleは win / loss ではなく no_decision として扱う
6. 次ターンへ進む
```

---

## 撤退時の公開情報

撤退で捨て札へ移動するカードは、既存の捨て札仕様に従う。

```txt
既存の捨て札が公開情報なら、撤退で捨てたカードも公開情報になる。
既存の捨て札が非公開情報なら、それに合わせる。
```

ただし、撤退によってReveal効果やon_reveal効果は発動しない。

```txt
撤退 = RevealせずにBattleを流す
```

として扱う。

---

## 相手の1枚回収

撤退された側は、自分の伏せカードから1枚を手札に戻してよい。

```txt
opponent may return 1 own facedown battle card to hand
```

- 相手の伏せカードが0枚なら、回収は発生しない
- 回収したカードはRevealされない
- 回収しなかったカードは捨て札へ移動する
- 初期Bot実装では、相手は最も評価値の高いカードを回収してよい
- Human UIが未実装の場合は、仮実装として自動選択でもよいが、TODOを残す

---

## 撤退とパリィ制限の関係

- 撤退ではパリィ判定は発生しない
- そのBattle中の一時Block低下は、Battle終了時に消える
- すでに持っている `parry_next_battle_limit` は、撤退したBattleにも適用される
- `parry_next_battle_limit` は、そのBattleが撤退で終わっても終了時に解除する

---

# Bot対応方針

## 最小対応

まずは以下を満たすこと。

```txt
- Botがretreatを不正actionとして扱わない
- legal_actionsにretreatが必要条件付きで含まれる
- 既存Botがretreatを選ばなくても、テストで直接使える
```

## 可能なら追加する簡易heuristic

可能であれば、PublicInfoBot等に以下の軽い判断を入れる。

```txt
- 推定で明確に負けそう
- 自分の伏せカードが1枚以上ある
- 相手が明らかに高い攻撃/速度を持ちそう
- 自分の勝ち筋が薄い
```

この場合、retreat候補にスコアを与える。

ただし、Botロジックの大規模改修は禁止。  
Botの本格調整は次タスクに回す。

---

# ログ出力仕様

パリィと撤退の分析ができるように、matchログに以下を記録する。

## Battle単位

```json
{
  "parry_events": [
    {
      "turn": 1,
      "attacker": "p1",
      "defender": "p2",
      "attacker_attack": 2,
      "defender_block": 4,
      "margin": 2,
      "block_debuff_applied": -2,
      "next_battle_limit_applied": true
    }
  ],
  "retreat_event": {
    "turn": 1,
    "player": "p1",
    "retreat_player_discarded_ids": ["..."],
    "opponent_returned_id": "...",
    "opponent_discarded_ids": ["..."]
  }
}
```

## Player単位 / Summary

可能であればsummaryに以下を追加する。

```txt
parry_count
parried_count
retreat_count
retreat_against_count
win_after_parry_count
loss_after_parried_count
win_after_retreat_count
loss_after_retreat_count
```

最低限、個別matchログで後から集計できる状態にする。

---

# UI / 表示の最低要件

UIを触る必要がある場合、最低限以下が分かるようにする。

```txt
- パリィが発生したこと
- パリィされた側にBlock -2が入ったこと
- 次Battleで伏せ枚数制限があること
- 撤退を選べるタイミング
- 撤退した時に何を失い、相手が何を回収したか
```

最初はデバッグ表示やログ中心でもよい。  
見た目の最終調整は人間が行う。

---

# 確認方法

Codexは、実装後に可能な範囲で以下を確認する。

## 自動テスト候補

1. パリィ発生

```txt
attacker_attack = 2
defender_block = 4
PARRY_MARGIN = 2
→ parry発生
→ attackerのcurrent battle Blockに-2
→ attackerにnext battle limit付与
```

2. パリィ非発生

```txt
attacker_attack = 3
defender_block = 4
PARRY_MARGIN = 2
→ 攻撃は防がれるがparryなし
```

3. Attack 0 はパリィ対象外

```txt
attacker_attack = 0
defender_block = 5
→ parryなし
```

4. 次Battle制限

```txt
parry_next_battle_limit = true
own_facedown = opponent_facedown + 1 になるsetは不許可
own_facedown <= opponent_facedown なら許可
Battle終了時に制限解除
```

5. 両者制限の相殺

```txt
p1.parry_next_battle_limit = true
p2.parry_next_battle_limit = true
→ 通常の伏せ枚数ルールを使用
→ parry_limit_cancelled_for_both = true をログ
```

6. 撤退

```txt
p1が伏せカード2枚、p2が伏せカード2枚
p1がretreat
→ p1の2枚は捨て札へ
→ p2は1枚を手札に戻す
→ p2の残り1枚は捨て札へ
→ Battle result = no_decision
→ Reveal効果は発動しない
```

7. 伏せ0枚撤退不可

```txt
own_facedown_count = 0
→ retreatはlegal_actionsに含めない
```

## 手動確認候補

```txt
- 通常のset / set_pass / passが壊れていない
- パリィが発生した時、ログ上で分かる
- パリィ後の反撃でBlock -2が効いている
- 次ターン、パリィされた側が相手より多く伏せられない
- 撤退時、カード移動が正しい
- 撤退後、次ターンへ進む
- 既存Bot同士の試合がクラッシュしない
```

---

# 制約

- 大規模リファクタは禁止
- 既存ルール名やカード名を不要に変更しない
- 保存形式や外部APIは変更しない
- カードデータの大幅な再調整はしない
- 仕様が曖昧なところは最小実装で仮決定し、docs/DECISIONS.md に記録する
- 実装上の都合で仕様を変えた場合は、必ず報告する

---

# docs/DECISIONS.md に記録してほしい仮決定

以下は、実装時にdocs/DECISIONS.mdへ追記すること。

```md
## Parry / Retreat prototype decisions

- Parry margin is initially 2.
- A parried attacker receives Block -2 for the current Battle only.
- The current Battle Block debuff does not stack multiple times in the same Battle.
- A parried player cannot set more facedown cards than the opponent in their next Battle.
- If both players have the next-Battle parry limit, the limits cancel for that Battle to avoid deadlock.
- Retreat is available only when the retreating player has at least one facedown card.
- Retreat ends the Battle as no_decision.
- Retreating player's facedown cards are discarded.
- The opponent may return one of their own facedown cards to hand.
- Retreat does not trigger reveal/on_reveal effects.
```

---

# 完了時の報告フォーマット

Codexは最後に以下の形式で報告すること。

```md
## 実装内容

- ...

## 変更ファイル

- ...

## 確認結果

- 実行したコマンド:
- 成功/失敗:
- 失敗した場合の理由:

## パリィ動作確認

- 発生条件:
- Block -2:
- 次Battle制限:

## 撤退動作確認

- 合法条件:
- カード移動:
- Battle result:

## 残課題

- ...

## 人間がテストプレイで見るべき観点

- 攻撃が怖くなりすぎていないか
- 防御待ちが強すぎないか
- 撤退が便利すぎないか
- 撤退が弱すぎて使われないか
- パリィ後のBlock -2が分かりやすいか
- 次Battle制限が重すぎないか
```

---

# 実装優先度

## Priority 1

```txt
- パリィ判定
- そのBattle中Block -2
- 次Battleの伏せ枚数制限
- 撤退action_type
- 撤退時カード移動
- 個別matchログ
```

## Priority 2

```txt
- Summary集計
- Botの簡易retreat判断
- UI上の表示
- docs/TEST_PLAN.md更新
```

## Priority 3

```txt
- Botの本格的なパリィリスク評価
- 人間向けの詳細演出
- バランス定数調整
```
