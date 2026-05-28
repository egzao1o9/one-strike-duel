# Web版起動手順

## 概要

このプロジェクトの Web 版フロントエンドは `frontend/` 配下にあります。  
ローカルで起動すると、ブラウザ上でドラフト画面や対戦画面のプロトタイプを確認できます。

## 前提

- Node.js がインストールされていること
- `npm` が使えること

## 初回セットアップ

プロジェクトルートで以下を実行します。

```bash
cd frontend
npm install
```

## 開発サーバーを起動する

```bash
cd frontend
npm run dev
```

起動後、ターミナルに表示される URL をブラウザで開いてください。  
通常は以下です。

```text
http://127.0.0.1:5173/
```

## 型チェック

TypeScript の型エラー確認は以下です。

```bash
cd frontend
npm run typecheck
```

## 本番ビルド確認

ビルドが通るか確認する場合は以下を実行します。

```bash
cd frontend
npm run build
```

ビルド結果は `frontend/dist/` に出力されます。

## よく使う流れ

```bash
cd frontend
npm install
npm run dev
```

## 補足

- 開発中は `npm run dev` を起動したままにして、保存のたびにブラウザで確認します。
- 画面が更新されない場合は、ブラウザを再読み込みしてください。
- 依存関係を更新した後は、必要に応じて `npm install` を再実行してください。
