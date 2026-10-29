# Data Quest — Pythonのコレクションを使いこなす

**バージョン：3.1**

**概要：** データエンジニアとしてデジタルの世界を冒険しよう！ゲームデータを構築・処理しながら、Pythonの強力なデータ構造を習得します。

> 原文：`py03.pdf`。本文を日本語訳し、ファイル名、識別子、許可事項、実行例の入出力は原文のまま掲載しています。PDFのページ区切りや、表示幅による実行例の折り返しは整理しています。

## 目次

1. 第I章：まえがき
2. 第II章：AIに関する指示
3. 第III章：はじめに
4. 第IV章：共通の指示
5. 第V章：演習0 — Command Quest
6. 第VI章：演習1 — Score Cruncher
7. 第VII章：演習2 — Position Tracker
8. 第VIII章：演習3 — Achievement Hunter
9. 第IX章：演習4 — Inventory Master
10. 第X章：演習5 — Stream Wizard
11. 第XI章：演習6 — Data Alchemist
12. 第XII章：提出について

## 第I章：まえがき

Twitterの成長初期、規模の拡大に対応するには、単にサーバーを追加するだけでは足りませんでした。巨大な規模になった途端に重要となる、小さな設計上の判断を見直す必要がありました。繰り返し見られたのは、リストや配列のような単純な逐次的データ構造を、扱いやすく、アクセス数が少ないうちは十分に機能するという理由で使うパターンです。その後、ユーザー数が爆発的に増えました。

以前はマイクロ秒で終わっていた「これはすでに存在するか？」といった操作が、毎秒数百万回も実行されるようになり、いつの間にか性能上のボトルネックになったのです。論理的に間違っているわけではありません。コードは明快で正しくても、不適切なコンテナを選んだことで、線形時間の処理が本番環境の悩みの種になりました。ハッシュベースの構造に置き換えると、まるで魔法のように問題が解決することもよくありました。大規模な環境では、データ構造そのものがアルゴリズムになる、ということを思い出させる好例です。

## 第II章：AIに関する指示

### 背景

学習の過程で、AIはさまざまな作業を支援できます。AIツールの多様な機能を調べ、どのように自分の作業に役立てられるか、時間をかけて探ってください。ただし、常に慎重に扱い、結果を批判的に評価してください。コード、ドキュメント、アイデア、技術的な説明のいずれであっても、自分の質問が適切だったか、生成された内容が正確かを完全に確信することはできません。仲間は、誤りや見落としを避けるための貴重な助けになります。

### 重要なメッセージ

- AIを使って、繰り返しの作業や退屈な作業を減らしましょう。
- コーディングに関するものも、それ以外も、将来の仕事に役立つプロンプト作成能力を身につけましょう。
- AIシステムの仕組みを学び、よくあるリスク、偏り、倫理的な問題を予測し、回避できるようになりましょう。
- 仲間と協力し、技術的な能力と対人面などの能力の両方を伸ばし続けましょう。
- AIが生成した内容は、自分で完全に理解し、責任を持てるものだけを使いましょう。

### 学習者のルール

- AIツールを倫理的に使い、潜在的な偏りを減らせるよう、時間をかけてツールを調べ、その仕組みを理解してください。
- プロンプトを書く前に、問題についてよく考えてください。そうすることで、正確な用語を使った、より明確で詳しく、目的に合ったプロンプトを書けます。
- AIが生成したものを、体系的に確認・レビューし、疑問を持ち、テストする習慣を身につけてください。
- 常に仲間によるレビューを求めてください。自分だけの検証に頼らないでください。

### この段階で目指す成果

- 汎用的なプロンプト作成能力と、専門分野に特化したプロンプト作成能力の両方を身につける。
- AIツールを効果的に使って、生産性を高める。
- 計算論的思考、問題解決能力、適応力、協働する力を引き続き伸ばす。

### 補足と例

- 試験や評価など、実際に理解していることを示さなければならない場面に、繰り返し直面します。それに備え、技術面と対人面の両方の能力を伸ばし続けてください。
- 自分の考えを説明し、仲間と議論すると、理解の抜けが見つかることがよくあります。仲間同士の学習を優先してください。
- AIツールは、あなた固有の状況を把握していないことが多く、一般的な回答をしがちです。同じ環境にいる仲間は、より適切で正確な知見を提供できます。
- AIが最もありそうな回答を生成しがちなのに対し、仲間は別の視点や有益な細部を示してくれます。品質を確認する相手として頼りにしてください。

**良い実践例：** AIに「ソート関数はどうテストすればよい？」と尋ねます。いくつかの案を得たら実際に試し、仲間と結果を検討します。一緒に方法を改善します。

**悪い実践例：** AIに関数全体を書かせ、プロジェクトにコピー＆ペーストします。相互評価で、その関数が何をしているのか、なぜそうするのかを説明できません。信頼を失い、プロジェクトも不合格になります。

**良い実践例：** パーサーの設計にAIを活用します。その後、仲間とロジックを一つずつ確認します。バグを2つ見つけ、一緒に書き直すことで、より良く、明快で、完全に理解できるものにします。

**悪い実践例：** プロジェクトの重要な部分のコードをCopilotに生成させます。コンパイルは通りますが、パイプをどう処理するのか説明できません。評価で根拠を示せず、プロジェクトは不合格になります。

## 第III章：はじめに

データエンジニアの皆さん、デジタルの世界へおかえりなさい！

Pythonの基礎を学ぶ旅を通して、十分な準備ができました。デジタルの庭を動かす基本構文を習得し、現実のシステムをモデル化する堅牢なクラス階層を構築し、適切な例外処理によって予期しない事態に対処する方法も学びました。いよいよ、ゲームの世界を舞台に、データエンジニアリングの中心となるコレクションとデータ構造を学びます。

想像してみてください。1980年、パックマンのゲーム状態は、すべてのドット、ゴーストの位置、スコアを含めても、わずか16KBのRAMに収まっていました。プログラマーは効率化の魔術師でなければなりませんでした！データを整理することは、単なるメモリ節約ではなく、ゲームの魔法を引き出すことだと気づいたのです。現代に目を向けると、Fortniteは同時に1,000万人を超えるプレイヤーを処理し、それぞれが毎秒何千ものデータを生み出しています。原則は同じで、舞台が大きくなったのです！

Pythonのコレクション型は、さまざまな用途に合わせて設計され、それぞれに固有の特徴があります。

- **リスト：** 順序があり、インデックスでアクセスでき、要素を追加できる。
- **タプル：** 順序があり、変更不可で、ハッシュ化可能。
- **集合：** 順序を持たず、重複しない要素を集める。
- **辞書：** キーと値の組を保持する。

さらに、ジェネレーターと内包表記によって、強力な構文と動作が加わります。

このクエストでは、ゲーム分析プラットフォームを支える構成要素を作ります。各演習で新たなデータ型が解禁され、最後にはデータエンジニアのようにPythonのコレクションを使いこなせるようになります！

> このプロジェクト以降、各演習で正式に導入された新しいPythonのデータ構造と、それに関連するすべてのクラスメソッドを使用できるようになります。

## 第IV章：共通の指示

### IV.1 一般ルール

- Python 3.10以降で作成してください。
- flake8のコーディング規約に従ってください。
- すべての関数とメソッドに型ヒントを付けてください。`mypy .` で確認してください。
- 関数では、クラッシュを避けるために適切に例外を処理してください。
- このプロジェクトではコマンドライン引数へのアクセスが必要です。インポートの仕組みを使い、`sys` モジュール経由でアクセスします。インポートの詳細は今後のプロジェクトで扱います。
- ファイル入出力は禁止です。すべてのデータはメモリ内、またはコマンドライン引数を通して処理してください。
- コレクションの使用パターンを明確に示すことに重点を置いてください。
- 各データ構造について、基本操作と高度な手法の両方を示してください。

> 標準型 `str`、`int`、`float` と、それらに関連するすべてのメソッドおよびコンストラクターを使用できます。

### IV.2 追加のガイドライン

- 指定されたGitリポジトリに提出してください。
- このリポジトリ内の内容だけが評価対象です。

## 第V章：演習0 — Command Quest（コマンドの冒険）

| 項目         | 内容                                                 |
| ------------ | ---------------------------------------------------- |
| 演習名       | `ft_command_quest`                                 |
| ディレクトリ | `ex0/`                                             |
| 提出ファイル | `ft_command_quest.py`                              |
| 使用許可     | `import sys`, `sys.argv`, `len()`, `print()` |

ようこそ、データの冒険者！壮大な冒険は、道具を理解するところから始まります。デジタルの世界では、プログラムは外の世界から指示を受け取る必要があります。最初の任務は、プログラムがユーザーからメッセージを受け取る方法を知ることです！

ここでリストを導入します。自分でリストを作る前に、すでに存在するリストを操作してみましょう。それは、`sys` モジュールから利用できるコマンドライン引数です。構造はCと似ており、文字列の配列になっています。リストの要素へのアクセス方法や操作方法を調べてください。

コマンドライン引数として受け取ったデータを表示する簡単なスクリプトを作成してください。以下の例にならってください。

```text
$> python3 ft_command_quest.py
=== Command Quest ===
Program name: ft_command_quest.py
No arguments provided!
Total arguments: 1

$> python3 ft_command_quest.py hello world 42
=== Command Quest ===
Program name: ft_command_quest.py
Arguments received: 3
Argument 1: hello
Argument 2: world
Argument 3: 42
Total arguments: 4

$> python3 ft_command_quest.py "Data Quest"
=== Command Quest ===
Program name: ft_command_quest.py
Arguments received: 1
Argument 1: Data Quest
Total arguments: 2
```

> `sys.argv` のリストにアクセスするには、スクリプトの先頭に `import sys` と書くだけです。

> 引数と一緒にプログラム名を再度表示しないようにする方法は複数あります。評価時に別の解決方法も議論できるよう準備してください。

## 第VI章：演習1 — Score Cruncher（スコア集計）

| 項目         | 内容                                                                                  |
| ------------ | ------------------------------------------------------------------------------------- |
| 演習名       | `ft_score_analytics`                                                                |
| ディレクトリ | `ex1/`                                                                              |
| 提出ファイル | `ft_score_analytics.py`                                                             |
| 使用許可     | `import sys`, `sys.argv`, `len()`, `sum()`, `max()`, `min()`, `print()` |

任務の説明：コマンドによるやり取りを習得したので、次はデータの整備です！プログラムにコマンドを送るユーザーは人間なので、間違えることがあります。

この演習では、スコアを保存するために**リスト**を使用し、無効な入力（数値でない値が渡された場合など）に適切に対処するために **`try/except` ブロック**を使用してください。

ゲームのスコアをコマンドライン引数で受け取ります。次のことを行ってください。

- コマンドライン引数を処理する。
- 引数なし、数値でない値など、さまざまな誤りに適切なメッセージで対処する。
- スコアを保存・整理するための新しいリストを作る。
- プレイヤーが喜ぶ基本統計量（件数、合計、平均、最大値、最小値、範囲）を計算する。
- ゲーム仲間に見せたくなるような出力にする（今回も実行例にならって構いません）。
- 有効な入力と無効な入力の両方が渡された場合は、無効なものを破棄し、有効な入力が一つでも残っていれば、それらを使って処理を続ける。

```text
$> python3 ft_score_analytics.py 1500 2300 1800 2100 1950
=== Player Score Analytics ===
Scores processed: [1500, 2300, 1800, 2100, 1950]
Total players: 5
Total score: 9650
Average score: 1930.0
High score: 2300
Low score: 1500
Score range: 800

$> python3 ft_score_analytics.py
=== Player Score Analytics ===
No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...

$> python3 ft_score_analytics.py ab ac
=== Player Score Analytics ===
Invalid parameter: 'ab'
Invalid parameter: 'ac'
No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...
```

## 第VII章：演習2 — Position Tracker（位置追跡）

| 項目         | 内容                                                                    |
| ------------ | ----------------------------------------------------------------------- |
| 演習名       | `ft_coordinate_system`                                                |
| ディレクトリ | `ex2/`                                                                |
| 提出ファイル | `ft_coordinate_system.py`                                             |
| 使用許可     | `import math`, `math.sqrt()`, `input()`, `round()`, `print()` |

レベルアップ！3D座標を習得しましょう！3D世界の特定の場所にテレポートするゲームや、3D空間の2点間の距離を求める場面を思い出してください。まさにそれを作ります！

この演習では、3D座標 `(x, y, z)` の保存に**タプル**を使用してください。

まず、次の処理を行う関数 `get_player_pos()` を作成してください。

- `x,y,z` 形式で、プレイヤーの新しい座標を入力するよう求める。
- 不適切な入力に対処する。
- 有効な座標が入力されるまで再試行する。
- プレイヤーの現在の3D座標を含むタプルを返す。

続いて、コードで次の処理を行います。

- 最初の座標を取得する。
- タプルを表示し、その後、各座標を個別に表示する。
- 3D空間の中心 `(0, 0, 0)` までの距離を計算する（下記参照）。
- 新しい座標を取得する。
- 2つ目と1つ目の座標の間の距離を計算する。

**距離の公式：** 3D空間の2点間の距離には、ユークリッド距離の公式を使用します。

$$
d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2}
$$

点 `(x1, y1, z1)` と `(x2, y2, z2)` の距離は、`math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)` です。これはピタゴラスの定理を3Dに拡張したものです！

```text
$> python3 ft_coordinate_system.py
=== Game Coordinate System ===

Get a first set of coordinates
Enter new coordinates as floats in format 'x,y,z': hello world
Invalid syntax
Enter new coordinates as floats in format 'x,y,z': 1.0 , 2.5, 3.0
Got a first tuple: (1.0, 2.5, 3.0)
It includes: X=1.0, Y=2.5, Z=3.0
Distance to center: 4.0311

Get a second set of coordinates
Enter new coordinates as floats in format 'x,y,z': 4,abc,5
Error on parameter 'abc': could not convert string to float: 'abc'
Enter new coordinates as floats in format 'x,y,z': 4,5,6
Distance between the 2 sets of coordinates: 4.9244
```

> `math.sqrt()` を使うには、スクリプトの先頭に `import math` と書くだけです。

> タプルは石に刻まれたデータのようなものです。一度作成すると変更できません。

## 第VIII章：演習3 — Achievement Hunter（実績ハンター）

| 項目         | 内容                                                                                                                              |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| 演習名       | `ft_achievement_tracker`                                                                                                        |
| ディレクトリ | `ex3/`                                                                                                                          |
| 提出ファイル | `ft_achievement_tracker.py`                                                                                                     |
| 使用許可     | `len()`, `print()`, `import random`, `random.*`, `set()`, `set.union()`, `set.intersection()`, `set.difference()` |

実績解除！最高の実績システムを作りましょう！珍しい実績を解除したときの満足感を知っていますか？今度は、それらすべてを管理するシステムを作ります！

この演習では、重複のない実績を保存するために**集合**を使用し、プレイヤー間の実績を分析するために集合演算（和集合、積集合、差集合）を使用してください。

多数の実績を含む固定のリストから、プレイヤーに実績の集合をランダムに割り当てる関数 `gen_player_achievements()` を作成してください。実績の個数をランダムに決め、その個数分の実績をリストから選んで集合を構築し、返してください。

続いて、コードで次の処理を行います。

- 少なくとも4人の異なるプレイヤーの実績集合を生成する。
- 全プレイヤーの実績を、重複を除いて把握する。
- 全プレイヤーに共通する実績を見つける。
- 各プレイヤーについて、その人だけが持つ実績を見つける。
- 各プレイヤーについて、すべての実績を揃えるために不足している実績を列挙する。

```text
$> python3 ft_achievement_tracker.py
=== Achievement Tracker System ===

Player Alice: {'Crafting Genius', 'World Savior', 'Master Explorer', 'Collector Supreme', 'Untouchable', 'Boss Slayer'}
Player Bob: {'Crafting Genius', 'Strategist', 'World Savior', 'Master Explorer', 'Unstoppable', 'Collector Supreme', 'Untouchable'}
Player Charlie: {'Strategist', 'Speed Runner', 'Survivor', 'Master Explorer', 'Treasure Hunter', 'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind'}
Player Dylan: {'Strategist', 'Speed Runner', 'Unstoppable', 'Untouchable', 'Boss Slayer'}

All distinct achievements: {'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer'}

Common achievements: {'Untouchable'}

Only Alice has: set()
Only Bob has: set()
Only Charlie has: {'Survivor', 'Treasure Hunter', 'First Steps', 'Sharp Mind'}
Only Dylan has: set()

Alice is missing: {'Strategist', 'Speed Runner', 'Survivor', 'Treasure Hunter', 'Unstoppable', 'Hidden Path Finder', 'First Steps', 'Sharp Mind'}
Bob is missing: {'Speed Runner', 'Survivor', 'Treasure Hunter', 'Hidden Path Finder', 'First Steps', 'Sharp Mind', 'Boss Slayer'}
Charlie is missing: {'Crafting Genius', 'World Savior', 'Hidden Path Finder', 'Unstoppable', 'Boss Slayer'}
Dylan is missing: {'Crafting Genius', 'World Savior', 'Survivor', 'Master Explorer', 'Treasure Hunter', 'Hidden Path Finder', 'First Steps', 'Collector Supreme', 'Sharp Mind'}
```

> 求められている各集合が空になりにくいように、実績の総数と、各プレイヤーに割り当てる実績数を調整してください。ところで、Pythonでは空の集合はどのように表示されますか？また、それはなぜでしょうか？

## 第IX章：演習4 — Inventory Master（インベントリ管理）

| 項目         | 内容                                                                                                                                            |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 演習名       | `ft_inventory_system`                                                                                                                         |
| ディレクトリ | `ex4/`                                                                                                                                        |
| 提出ファイル | `ft_inventory_system.py`                                                                                                                      |
| 使用許可     | `import sys`, `sys.argv`, `len()`, `print()`, `sum()`, `list()`, `round()`, `dict.keys()`, `dict.values()`, `dict.update()` |

戦利品の時間です！RPGで持ち物を整理したり、伝説の剣を持っているか確認したりしたことを思い出してください。究極のインベントリシステムを作りましょう！

この演習では、インベントリのデータを保存するために**辞書**を使用してください。

まず、コマンドライン引数を解析し、インベントリシステムにデータを登録します。各引数は `<item_name>:<quantity>` 形式でなければなりません。不正な構文や重複した引数など、無効な引数はエラーメッセージを出して破棄し、有効なものを辞書に入れてください。後で計算できるよう、辞書内の `<quantity>` の値は `int` として保存します。

次に、インベントリを操作します。

- インベントリを表示する。
- インベントリに含まれる全アイテムのリストを作成し、表示する。
- インベントリ内の全アイテムの数量の合計を計算し、表示する。
- 各アイテムの数量が、インベントリ全体に占める割合をパーセントで表示する。
- 数量が最も多いアイテムと、最も少ないアイテムを報告する（同数の場合はコマンドラインで先に指定されたものを選ぶ）。
- 最後に、新しいアイテムを追加し、インベントリを再表示する。

```text
$> python3 ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1 sword:2 hello key:value
=== Inventory System Analysis ===
Redundant item 'sword' - discarding
Error - invalid parameter 'hello'
Quantity error for 'key': invalid literal for int() with base 10: 'value'
Got inventory: {'sword': 1, 'potion': 5, 'shield': 2, 'armor': 3, 'helmet': 1}
Item list: ['sword', 'potion', 'shield', 'armor', 'helmet']
Total quantity of the 5 items: 12
Item sword represents 8.3%
Item potion represents 41.7%
Item shield represents 16.7%
Item armor represents 25.0%
Item helmet represents 8.3%
Item most abundant: potion with quantity 5
Item least abundant: sword with quantity 1
Updated inventory: {'sword': 1, 'potion': 5, 'shield': 2, 'armor': 3, 'helmet': 1, 'magic_item': 1}
```

> ゲーム開始時、インベントリはたいてい空ですよね ;)

## 第X章：演習5 — Stream Wizard（ストリームの魔術師）

| 項目         | 内容                                                                                                                      |
| ------------ | ------------------------------------------------------------------------------------------------------------------------- |
| 演習名       | `ft_data_stream`                                                                                                        |
| ディレクトリ | `ex5/`                                                                                                                  |
| 提出ファイル | `ft_data_stream.py`                                                                                                     |
| 使用許可     | `next()`, `range()`, `len()`, `print()`, `import typing`, `typing.Generator`, `import random`, `random.*` |

魔法の時間です！ゲームは何百万ものイベントを、クラッシュせずにどう処理するのでしょうか？Pythonのメモリ節約の切り札、ジェネレーターの世界へようこそ！

この演習では、`yield` キーワードを使う**ジェネレーター**によって、その場でデータストリームを生成してください。すべてをメモリに保存する代わりに、必要に応じて値を生成するジェネレーター関数を実装しなければなりません。

プレイヤーのリストから名前を、行動のリストから行動をランダムに選ぶ、無限に生成を続けるジェネレーター関数 `gen_event()` を作成してください。このジェネレーターに対して `next()` を呼び出すたび、新しいイベントをタプル `(name, action)` として返します。

スクリプトのメイン部分で1,000回ループし、`gen_event()` から得た1,000件のイベントをすべて表示してください。

次に、再び `gen_event()` を使って生成した10個のタプルからなるリストを作成してください。

最後に、先ほどのリストを受け取る、新しいジェネレーター関数 `consume_event` を作成してください。リストの要素をランダムに1つ選び、リストから削除してから `yield` し、リストが空になるまで続けます。このジェネレーターは `for .. in ..` 構文で直接使用しなければなりません。

```text
$> python3 ft_data_stream.py
=== Game Data Stream Processor ===
Event 0: Player bob did action run
Event 1: Player alice did action eat
Event 2: Player bob did action sleep
Event 3: Player bob did action grab
Event 4: Player dylan did action run
Event 5: Player bob did action move
Event 6: Player alice did action move
Event 7: Player dylan did action move
Event 8: Player alice did action climb
Event 9: Player bob did action sleep
Event 10: Player bob did action run
Event 11: Player bob did action swim
Event 12: Player dylan did action swim
Event 13: Player charlie did action sleep
Event 14: Player charlie did action sleep

[...]
Event 992: Player dylan did action eat
Event 993: Player alice did action sleep
Event 994: Player charlie did action move
Event 995: Player charlie did action climb
Event 996: Player bob did action release
Event 997: Player bob did action grab
Event 998: Player bob did action move
Event 999: Player alice did action move
Built list of 10 events: [('charlie', 'move'), ('dylan', 'grab'), ('alice', 'use'), ('alice', 'use'), ('charlie', 'swim'), ('bob', 'run'), ('charlie', 'move'), ('dylan', 'climb'), ('alice', 'use'), ('bob', 'release')]
Got event from list: ('charlie', 'swim')
Remains in list: [('charlie', 'move'), ('dylan', 'grab'), ('alice', 'use'), ('alice', 'use'), ('bob', 'run'), ('charlie', 'move'), ('dylan', 'climb'), ('alice', 'use'), ('bob', 'release')]
Got event from list: ('alice', 'use')
Remains in list: [('charlie', 'move'), ('dylan', 'grab'), ('alice', 'use'), ('bob', 'run'), ('charlie', 'move'), ('dylan', 'climb'), ('alice', 'use'), ('bob', 'release')]
Got event from list: ('charlie', 'move')
Remains in list: [('dylan', 'grab'), ('alice', 'use'), ('bob', 'run'), ('charlie', 'move'), ('dylan', 'climb'), ('alice', 'use'), ('bob', 'release')]
Got event from list: ('charlie', 'move')
Remains in list: [('dylan', 'grab'), ('alice', 'use'), ('bob', 'run'), ('dylan', 'climb'), ('alice', 'use'), ('bob', 'release')]
Got event from list: ('alice', 'use')
Remains in list: [('dylan', 'grab'), ('bob', 'run'), ('dylan', 'climb'), ('alice', 'use'), ('bob', 'release')]
Got event from list: ('bob', 'release')
Remains in list: [('dylan', 'grab'), ('bob', 'run'), ('dylan', 'climb'), ('alice', 'use')]
Got event from list: ('bob', 'run')
Remains in list: [('dylan', 'grab'), ('dylan', 'climb'), ('alice', 'use')]
Got event from list: ('dylan', 'climb')
Remains in list: [('dylan', 'grab'), ('alice', 'use')]
Got event from list: ('alice', 'use')
Remains in list: [('dylan', 'grab')]
Got event from list: ('dylan', 'grab')
Remains in list: []
```

## 第XI章：演習6 — Data Alchemist（データの錬金術師）

| 項目         | 内容                                                                            |
| ------------ | ------------------------------------------------------------------------------- |
| 演習名       | `ft_data_alchemist`                                                           |
| ディレクトリ | `ex6/`                                                                        |
| 提出ファイル | `ft_data_alchemist.py`                                                        |
| 使用許可     | `import random`, `random.*`, `print()`, `len()`, `sum()`, `round()` |

いよいよ最後のボスです！すべてのデータ構造を習得したので、今度はそれらを簡潔で洗練された形で扱う方法を学びましょう！ここで真のデータの錬金術師になります！

この演習では、データを効率的に変換・抽出するために、**リスト内包表記と辞書内包表記**を使用してください。これらは、データ処理におけるPythonの基本的な機能です。

先頭が大文字の名前と、そうでない名前が混在するプレイヤー名のリストを作成してください。リスト内包表記を2つ作成します。1つ目では、すべての名前の先頭を大文字にした新しいリストを作ります。2つ目では、元のリストから、先頭が大文字の名前だけを含む新しいリストを作ります。

次に、すべての名前の先頭を大文字にしたリストから辞書を作成します。名前をキーとし、指定した範囲でランダムに生成したスコアを値にします。もちろん、この辞書は内包表記で構築します。さらに、平均より高いスコアを持つ要素だけの2つ目の辞書も、内包表記で作成します。

```text
$> python3 ft_data_alchemist.py
=== Game Data Alchemist ===

Initial list of players: ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
New list with all names capitalized: ['Alice', 'Bob', 'Charlie', 'Dylan', 'Emma', 'Gregory', 'John', 'Kevin', 'Liam']
New list of capitalized names only: ['Alice', 'Charlie', 'Emma', 'Gregory', 'Liam']

Score dict: {'Alice': 263, 'Bob': 666, 'Charlie': 907, 'Dylan': 170, 'Emma': 568, 'Gregory': 446, 'John': 90, 'Kevin': 527, 'Liam': 54}
Score average is 410.11
High scores: {'Bob': 666, 'Charlie': 907, 'Emma': 568, 'Gregory': 446, 'Kevin': 527}
```

> 集合でも内包表記を使用できます。

> 各内包表記は、行の長さの制限を超える場合を除き、1行で記述してください。

## 第XII章：提出について

いつもどおり、課題をGitリポジトリに提出してください。口頭評価では、リポジトリ内の成果物だけが評価対象になります。ファイル名が正しいか、再確認することをためらわないでください。

> 評価中に、データ構造を選んだ理由の説明、コレクション操作の実演、分析システムへの新機能の追加を求められる場合があります。各データ構造の背後にある原理を理解しておいてください。

> このプロジェクトの課題文で指定されたファイルだけを提出してください。Pythonのコレクション型とデータ処理技法の習得が明確に伝わる、明快で十分に文書化されたコードに重点を置いてください。
