#!/usr/bin/env python
# coding: utf-8

# # GINZAとspaCy

# ## GINZAとは
# 
# 「GINZA」とは、リクルートと国立国語研究所の共同研究によって2019年4月に公開されたPython向け日本語自然言語処理ライブラリです。
# 
# 
# これまでの自然言語処理ライブラリは独立した機能の物が多く、例えば[「MeCab」](http://mecab.sourceforge.net/)や[「Janome」](https://mocobeta.github.io/janome/)、[「Juman」](http://nlp.ist.i.kyoto-u.ac.jp/index.php?%E6%97%A5%E6%9C%AC%E8%AA%9E%E5%BD%A2%E6%85%8B%E7%B4%A0%E8%A7%A3%E6%9E%90%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0JUMAN)等は形態素解析、[「CaboCha」](http://code.google.com/p/cabocha/)や[「KNP」](http://nlp.ist.i.kyoto-u.ac.jp/index.php?%E6%97%A5%E6%9C%AC%E8%AA%9E%E6%A7%8B%E6%96%87%E8%A7%A3%E6%9E%90%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0KNP)等は係り受け解析を担うなど、応用を目指すにはこれらを組み合わせる専門知識とエンジニアリングが必要でした。
# 
# そこで形態素解析、係り受け解析などを標準で扱えるライブラリとしてGINZAが登場しました。

# ## GINZAの概要と特徴
# 
# >「GiNZA」は、最先端の機械学習技術を取り入れた自然言語処理ライブラリ「spaCy」をフレームワークとして利用しており、また、オープンソース形態素解析器「SudachiPy」を内部に組み込み、トークン化処理に利用している。「GiNZA日本語UDモデル」にはMegagon Labsと国立国語研究所の共同研究成果が組み込まれています
# 
# またGINZAの特徴は以下の通りです。
# 
# >1.高度な自然言語処理をワンステップで導入完了
# >これまで、高度な自然言語処理を行うためには複雑な導入作業が必要でしたが、「GiNZA」はワンステップでモジュールとモデルファイルの導入を完了できます。これにより、エンジニアは即座に解析が可能です。
# > 
# >2.高速・高精度な解析処理と依存構造解析レベルの国際化に対応
# >産業用途で自然言語処理技術を活用するには、一定の処理速度を保ちながら解析精度を高めるためにチューニングを行うことが一般的です。「GiNZA」は、「spaCy」が提供する高速・高精度な依存構造解析器を使用して、産業用途に耐える性能を備えた高度な自然言語処理機能をライブラリとして提供します。同時に、「spaCy」の国際化機能により、複数の欧米言語と日本語の言語リソースを切り替えて使用することが可能となり、エンジニアは複数言語の解析を単一のライブラリで行うことができます。
# > 
# >3.国立国語研究所との共同研究成果の学習モデルを提供
# 自然言語処理系の学会を中心に、人類が用いる多様な言語を、一貫した構文構造・品詞体系で解析可能にする>「Universal Dependencies」の取組みが、2014年から全世界で始まっています。日本においても当初からUDの日本語への適用に関する研究と日本語版UDコーパス（データ）構築が同時に進められてきました。Megagon Labsは、国立国語研究所と共同で、日本語版UDに基づいた高精度な依存構造解析技術の研究を行い、その成果である学習済みモデルを「GiNZA日本語UDモデル」に組み込みました。
# 「GiNZA日本語UDモデル」は、国立国語研究所が長年の研究を通じて蓄積してきた大規模かつ高品質なテキストコーパスに加えて、日本語Wikipediaテキストも同時に用いて機械学習に適用することで、幅広い分野に適応可能なモデルを構築しています。
# 
# つまりはこれまで自然言語処理を始めるには機能独立したライブラリそれぞれを準備する必要がありましたが、「GINZA」を準備するだけで始める準備が終わることになります。
# 
# 引用元[リクルートのAI研究機関、国立国語研究所との共同研究成果を用いた日本語の自然言語処理ライブラリ「GiNZA」を公開](https://www.recruit.co.jp/newsroom/2019/0402_18331.html)
# 

# ## spaCyとは
# 「GINZA」が使用している「spaCy」は、Pythonで高度な自然言語処理(NLP)を行うためのフリーのオープンソースライブラリです。最新の研究を元に各機能は作られており、産業製品用途に耐えうるように特別に設計されています。この点が教育や研究用途のNLTKやCoreNLPのようなライブラリとは異なります。しかし、spaCyができることは数多く、情報抽出や自然言語理解システムの構築、またはDNNの前処理などに役立ちます。

# ## spaCyの機能
# spaCyの機能についてまとめた表を示します。
# 
# 処理 | 説明
# --- | ---
# トークン化 | テキストを単語や句読点などに分割します。
# 品詞（POS: Part-of-speech）タグ付け | 動詞や名詞などのトークンに単語タイプを割り当てます。
# 依存関係の解析 | 主語や目的語のように、個々のトークン間の関係を記述する構文依存性ラベルを割り当てます。
# 語の見出し語化(Lemmatization) | 単語の基本形を割り当てる。例えば、"was "の見出しは "be "であり、"rats "の見出しは "rat "である。
# 文境界検出 (SBD:Sentence Boundary Detection) | 個々の文を見つけてセグメント化します。
# 固有表現抽出(NER:Named Entity Recognition ) | 人、会社、場所など、名前のついた「実世界」のオブジェクトをラベリングします。
# エンティティリンク (EL:Entity Linking)  | テキストのエンティティを、知識ベース内の一意の識別子と区別します。
# 類似性(Similarity) | 単語、テキストスパン、ドキュメントを比較し、それらが互いにどの程度似ているかを比較します。
# テキスト分類 | 文書全体または文書の一部にカテゴリやラベルを割り当てます。
# ルールベースのマッチング | 正規表現に似た、テキストと言語的注釈に基づいて、トークンのシーケンスを見つけます。
# トレーニング | 統計モデルの予測を更新したり、改善したりすること。
# シリアライゼーション | オブジェクトをファイルやバイト文字列に保存します。
# 
# 上記の処理機能の一部は独立して使用可能ですが、その他は言語アノテーションを予測するための統計モデルをロードする必要があります。統計モデルには、通常、以下のコンポーネントが含まれています。
# 
# コンポーネント　|　説明
# --- | ---
# 品詞タグ付けのためのバイナリ重み | 依存性パーサ、および文脈でのアノテーションを予測するための名前付きエンティティ認識器に使用
# 語彙エントリ | 単語とその形やスペルなどの文脈に依存しない属性。
# データファイル | 見出し語化ルールやルックアップテーブルなど。
# 単語ベクトル　 | 単語の多次元的な意味表現で、単語同士の類似度を判断する。
# コンフィグレーション | 言語や処理パイプラインの設定のような設定オプション
# 
# 以降はコードと共に機能について見ていきます。

# ## Ref
# - [自然言語処理ライブラリ一覧](http://www.phontron.com/nlptools.php?lang=ja)
# 
# - [GiNZA - Japanese NLP Library](https://megagonlabs.github.io/ginza/)
# 
# - [日本語ライブラリGINZAのススメ](https://qiita.com/poyo46/items/7a4965455a8a2b2d2971)
# 
# - [自然言語処理ライブラリGiNZAをインストールして簡単に動かすまでの手順](https://www.virment.com/how-to-install-ginza-and-use/)
# 
# - [spaCyとGiNZAを用いた言語処理](https://www.koi.mashykom.com/spacy_ginza.html)
# 
# - [正規表現・自然言語処理](https://petitviolet.hatenablog.com/entry/20120523/1337760714)
# 
# 
# - [spacy](https://spacy.io/usage/spacy-101)
# 

# [spacy](https://spacy.io/usage/spacy-101) こちらの記事をDeepL翻訳しています。

# In[1]:


# !pip install ginzaå
# !python -m spacy download en_core_web_lg


# ## 言語アノテーション
# spaCyは、様々な言語アノテーションを提供します。
# これは「単語の種類」、「単語間の関係」などです。
# 例えば、「google」が動詞として使われているか、会社名などの名詞として使われているかを示します。
# 
# 統計モデルをインストールしたら、`spacy.load()`でモデルをロードします。これの戻り値はLanguageオブジェクトであり、通常nlpという変数に格納します。`nlp()`を呼び出すと、処理された`doc`が戻ります。

# In[2]:


from ginza import *
import spacy

nlp = spacy.load("ja_ginza")  # GiNZAモデルの読み込み
doc = nlp('吾輩は猫である。') # nlpにテキストを渡す

for token in doc:
    print(token.text, token.pos_, token.dep_, token.lemma_, token.lang_,)


# docが処理されても、元のテキストのすべての情報（空白文字など）が保持されています。
# トークンのオフセットで元の文字列に取得したり、トークンとその末尾の空白文字を結合して元の文字列を再構築したりすることができます。
# 
# pos_は品詞を取得します。コードの意味は[こちら](https://universaldependencies.org/docs/u/pos/)です。
# 
# dep_は構造依存関係を取得します。
# 
# 

# ## Token化
# 
# spaCyは最初にテキストをトークン化します, すなわち, 単語や句読点などにセグメント化します. これは各言語に固有のルールを適用することによって行われます．例えば, 文末の句読点は分割する必要があります - 一方 "U.K. "は1トークンのままにしておく必要があります. それぞれのDocは個々のトークンで構成されており、それらを反復処理することができます。

# In[3]:


from ginza import *
import spacy

nlp = spacy.load("ja_ginza")  # GiNZAモデルの読み込み
doc = nlp('吾輩は猫である。') # nlpにテキストを渡す

for token in doc:
    print(token.text)


# まず、生のテキストを text.split(' ' ') のように、空白文字で分割します。次に、トークナイザーはテキストを左から右へと処理します。それぞれの部分文字列に対して、2つのチェックを行います。
# 
# 1. その部分文字列はトークン化の例外ルールに合致していますか？
# 例えば、"don't "は空白を含まないが、"do "と "n't "の2つのトークンに分割されるべきであり、"U.K. "は常に1つのトークンのままであるべきである。
# 
# 2. 接頭辞、接尾辞、接頭辞を分割することはできますか？
# 例えば、カンマ、ピリオド、ハイフン、引用符などの句読点。
# 
# 
# 一致するものがあればルールが適用され、トークンライザはループを続け、新たに分割された部分文字列から開始します。このようにして、spaCy は略語の組み合わせや複数の句読点のような複雑で入れ子になったトークンを分割することができます。
# 
# 
# 
# ```
# トークン化例外：文字列を複数のトークンに分割したり、句読点規則を適用したときにトークンが分割されないようにするための特殊文字列規則。
# プレフィックス：文字列の先頭にある文字。
# 接頭：末尾の文字、例えば km, ), ", !
# インフィックス：間にある文字、例：-, --, /, ....
# ```
# 
# https://spacy.io/tokenization-57e618bd79d933c4ccd308b5739062d6.svg
# 
# 

# ## 品詞タグと依存関係
# 
# トークン化の後, spaCyは与えられたDocを解析してタグ付けすることができます. これは、統計モデルが出てくる場所です, これは、spaCyがこのコンテキストで最も適用される可能性が高いタグまたはラベルの予測を行うことができます. モデルは、バイナリデータで構成され、それが言語全体で一般化する予測を行うためにシステムに十分な例を示すことによって生成されます - 例えば, 英語で "the "に続く単語は、最も可能性の高い名詞です.
# 
# 
# 言語アノテーションはToken属性として利用可能です。多くのNLPライブラリと同様に、 spaCyはすべての文字列をハッシュ値にエンコードし、メモリ使用量を減らして効率を向上させます。そのため、属性の読める文字列表現を取得するには、その名前にアンダースコア_を追加する必要があります。
# 
# 

# In[4]:


from ginza import *
import spacy

nlp = spacy.load("ja_ginza")  # GiNZAモデルの読み込み
doc = nlp('タカシくんはスーパーへ牛乳を買いに行きました。') # nlpにテキストを渡す

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, 
            token.shape_, token.is_alpha, token.is_stop)


# 各々のオフセットの内容は下記の通りである。
# 
# ```
# テキスト：単語の原文。
# ルンマ：単語の基底形。
# POS（品詞）：単純なUPOS品詞タグ。
# タグ：詳細品詞タグ
# Dep:：構文依存性、つまりトークン間の関係
# Shape（形）： 単語の形。単語の形 - 大文字化、句読点、桁。
# はアルファです：トークンがアルファ文字であるかどうか。
# is stop:：トークンはストップリストの一部か、つまりその言語の最も一般的な単語か。
# ```
# 

# In[5]:


import spacy
from spacy import displacy

nlp = spacy.load('ja_ginza')
doc = nlp('吾輩は猫である。')

# https://qiita.com/youwht/items/b047225a6fc356fd56ee
###係り受け表示
#係り受けのグラフ形式を図示する
#Colaboratory上で直接表示するためには少々工夫を要する
#https://stackoverflow.com/questions/58892382/displacy-from-spacy-in-google-colab
displacy.render(doc, style='dep', jupyter=True, options={'distance': 90})


# ## 固有表現
# 固有表現とは名前が割り当てられた実世界のオブジェクトです。例えば、人、国、製品、書籍、映画などがこれにあたります。
# モデルは学習データに強く依存するため、ユースケースごとに調整が必要です。
# 
# 固有表現はdocのentで取得可能です。

# In[6]:


from ginza import * 
import spacy

nlp = spacy.load('ja_ginza')
doc = nlp('吾輩は猫である。')

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)


# ```
# Text: The original entity text.
# Start: Index of start of entity in the Doc.
# End: Index of end of entity in the Doc.
# Label: Entity label, i.e. type.
# ````

# In[7]:


import spacy
from spacy import displacy

nlp = spacy.load('ja_ginza')
doc = nlp('吾輩は猫である。')


displacy.render(doc, style='ent', jupyter=True, options={'distance': 90})


# ## 単語ベクトルと類似度
# 
# 単語の類似度は、単語ベクトル（word vector）を比較することによって計算します。
# 単語ベクトルはword2vecを使用して生成でき、次のような形式で表されます。
# 
# ```
# # BANANA.VECTOR
# array([2.02280000e-01,  -7.66180009e-02,   3.70319992e-01,
#      3.28450017e-02,  -4.19569999e-01,   7.20689967e-02,
#     -3.74760002e-01,   5.74599989e-02,  -1.24009997e-02,
#      5.29489994e-01,  -5.23800015e-01,  -1.97710007e-01,
#     -3.41470003e-01,   5.33169985e-01,  -2.53309999e-02,
#      1.73800007e-01,   1.67720005e-01,   8.39839995e-01,
#      5.51070012e-02,   1.05470002e-01,   3.78719985e-01,
#      2.42750004e-01,   1.47449998e-02,   5.59509993e-01,
#      1.25210002e-01,  -6.75960004e-01,   3.58420014e-01,
#      # ... and so on ...
#      3.66849989e-01,   2.52470002e-03,  -6.40089989e-01,
#     -2.97650009e-01,   7.89430022e-01,   3.31680000e-01,
#     -1.19659996e+00,  -4.71559986e-02,   5.31750023e-01], dtype=float32)
# ```
# 
# 
# ### 注意
# spacyにはいくつかモデルがあり、通常smで終わるものは小さなモデルを表します。そして、これには単語ベクトルが付属せず、similarity()を使用して各種属性を比較することはできますが、精度はそれほどよくありません。そのため、実際に単語ベクトルを使用する際にはlgで終わるものなどより大きなモデルを使用してください。

# 単語ベクトルが組み込まれたモデルではToken.vectorとして使用できます。Doc.vectorとSpan.vectorはデフォルトでトークンベクトルの平均になります。

# In[8]:


import spacy

nlp = spacy.load('ja_ginza')
tokens = nlp('犬　猫　亀　アップル　オレンジ')

for token in tokens:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)


# 上記の単語は動物と果物を表し、一般的な語彙の一部であるためベクトルがついているが、一般的な語彙に含まれないものにはベクトルがついていないことがあります。これをカバーするためにはより大きいモデルをロードすることを検討してください。
# 
# 
# spacyは2つのオブジェクトを比較し、それらがどの程度類似しているかを予測できます。
# 
# Doc、Span、Tokenにはsimilarity()が付属しており、これを使用して他のオブジェクトと比較し、類似度を判断できます。

# In[9]:


import spacy

nlp = spacy.load('ja_ginza')
tokens = nlp('犬　猫　アップル')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# この場合、モデルの予測はほぼ適切です。同一のトークンは明らかに100%互いに類似しています。ただし、ベクトル演算と浮動小数点の計算のために必ずしも1.0とは限りません。

# ## パイプライン
# 
# テキストに対してnlpを呼び出すと、spacyはテキストをトークン化してDocオブジェクトを生成します。その後、ドキュメントはいくつかのステップで処理されます。これを「処理パイプライン」とも呼ばれます。デフォルトモデルで使用されるパイプラインはタガー、パーサー、エンティティリコグナイざーを含みます。各要素は処理されたDocを返します。
# 
# 
# 名称 | コンポーネント | 生成物 | 説明
# --- | --- | --- | ---
# tokenizer | Tokenizer | Doc | テキストをトークンに分割
# tagger | Tagger | Doc[i].tag | 品詞タグ付け
# parser | DependencyParser | Doc[i].head, Doc[i].dep, Doc.sents, Doc.noun_chunks | 依存関係ラベルを割り当て
# ner | EntityRecognizer | Doc.ents, Doc[i].ent_iob, Doc[i].ent_type | 固有表現を検出してラベル付け
# textcat | TextCategorizer | Doc.cats | ドキュメントラベルを割り当て
# .... | custom components | Doc._.xxx, Token._.xxx, Span._.xxx | カスタム属性、メソッド、プロパティを割り当て
# 
# 
# 処理パイプラインは、常に統計モデルとその能力に依存する。例えば、モデルがエンティティラベルの予測を行うためのデータを含む場合にのみ、パイプラインはエンティティ認識コンポーネントを含むことができます。このため、各モデルは、コンポーネント名を含む単純なリストとして、そのメタデータで使用するパイプラインを指定します。
# 
# ```
# "pipeline": ["tagger", "parser", "ner"]
# ```

# ## 語彙(Vocab)、ハッシュ(hashe)、見出し(lexeme)
# 
# 
# 可能な限り, spaCyは複数のドキュメントで共有されるボキャブラリー, Vocabにデータを格納しようとします. メモリを節約するために, spaCyはまた、すべての文字列をハッシュ値にエンコードします - この例では, "coffee "はハッシュ3197928453018144401を持っています. ORG "のようなエンティティラベルや "VERB "のような品詞タグもエンコードされます. 内部的には、spaCyはハッシュ値の中で「話す」だけです。
# 
# https://spacy.io/vocab_stringstore-1d1c9ccd7a1cf4d168bfe4ca791e6eed.svg
# 
# 
# あなたは、すべての異なるコンテキストの種類の単語 "コーヒー "を含むドキュメントの多くを処理する場合, 毎回正確な文字列 "コーヒー "を格納するには、あまりにも多くのスペースを取るだろう. そこで代わりに、 spaCy は文字列をハッシュして StringStore に保存します。あなたは、両方の方向で動作するルックアップテーブルとしてStringStoreを考えることができます - あなたは、そのハッシュを取得するために文字列を調べることができます, またはその文字列を取得するためにハッシュ.
# 

# In[10]:


from ginza import *
import spacy

nlp = spacy.load("ja_ginza")
doc = nlp("私はコーヒーが好きです")
print(doc.vocab.strings["コーヒー"])  # 3197928453018144401
print(doc.vocab.strings[16003280304011083252])  # 'コーヒー'


# すべての文字列がエンコードされているので、語彙のエントリは単語テキストを含む必要はありません。その代わりに、ハッシュ値を使ってStringStoreで検索することができます。語彙の各エントリはLexemeとも呼ばれ、単語に関する文脈に依存しない情報を含んでいます。例えば、"love "がある文脈で動詞や名詞として使われていても、その綴りやアルファベットで構成されているかどうかは変わりません。また、そのハッシュ値も常に同じです。

# In[11]:


from ginza import *
import spacy

nlp = spacy.load("ja_ginza")
doc = nlp("私はコーヒーが好きです")

for word in doc:
    lexeme = doc.vocab[word.text]
    print(lexeme.text, lexeme.orth, lexeme.shape_, lexeme.prefix_, lexeme.suffix_,
            lexeme.is_alpha, lexeme.is_digit, lexeme.is_title, lexeme.lang_)


# 単語のハッシュへのマッピングは、どのような状態にも依存しません。各値が一意であることを確認するために, spaCyは、単語の文字列に基づいてハッシュを計算するためにハッシュ関数を使用しています. これはまた、 "コーヒー "のハッシュは常に同じになることを意味します, あなたが使用しているモデルやどのようにあなたがspaCyを設定したかに関係なく.
# 
# しかし, ハッシュを逆にすることはできませんし、3197928453018144401を解決する方法はありません。spaCyができるのは語彙で調べることだけです。だからこそ、あなたが作成するすべてのオブジェクトが同じ語彙にアクセスできることを常に確認する必要があります。彼らがそうでない場合、spaCyはそれが必要とする文字列を見つけることができないかもしれません。

# In[12]:


import spacy
from spacy.tokens import Doc
from spacy.vocab import Vocab

nlp = spacy.load('ja_ginza')
doc = nlp("私はコーヒーが好きです")

print(doc.vocab.strings['コーヒー'])  # 16003280304011083252
print(doc.vocab.strings[16003280304011083252])  # 'コーヒー'

empty_doc = Doc(Vocab())  # 空のVocabを含む新しいドキュメントを生成
# empty_doc.vocab.strings[16003280304011083252] エラー発生

empty_doc.vocab.strings.add("コーヒー")  # 「コーヒー」を追加してハッシュを生成
print(empty_doc.vocab.strings[16003280304011083252])  # 'コーヒー' 👍

new_doc = Doc(doc.vocab)  # 最初のドキュメントの語彙で新しいドキュメントを生成
print(new_doc.vocab.strings[16003280304011083252])  # 'コーヒー' 👍


# 語彙に3197928453018144401の文字列が含まれていない場合、spaCyはエラーを発生させます。あなたは手動で "coffee "を再追加することができますが、これはあなたが実際にドキュメントにその単語が含まれていることを知っている場合にのみ動作します。この問題を防ぐために, spaCy はまた、Doc または nlp オブジェクトを保存するときに Vocab をエクスポートします. これはあなたにオブジェクトとそのエンコードされた注釈を与えます, 加えてそれをデコードするための "キー".が提供されます。

# ## ナレッジベース
# 
# 「spaCy」はエンティティリンクタスクをサポートするために、外部ナレッジをナレッジベースに保存します。「ナレッジベース」（KB）はVocabを使用してデータを効率的に保存します。
# 
# 「ナレッジベース」は、最初にすべてのエンティティを追加することによって作成されます。次に、潜在的な言及またはエイリアスごとに、関連するKB IDとそれらの以前の確率のリストが追加されます。これらの事前確率の合計は、特定のエイリアスで1を超えてはなりません。

# In[13]:


import spacy
from spacy.kb import KnowledgeBase

# モデルを読み込み、空のナレッジベースを作成
nlp = spacy.load('ja_ginza')
kb = KnowledgeBase(vocab=nlp.vocab, entity_vector_length=3)

# エンティティの追加
kb.add_entity(entity="Q1004791", freq=6, entity_vector=[0, 3, 5])
kb.add_entity(entity="Q42", freq=342, entity_vector=[1, 9, -3])
kb.add_entity(entity="Q5301561", freq=12, entity_vector=[-2, 4, 2])

# エイリアスの追加
kb.add_alias(alias="Douglas", entities=["Q1004791", "Q42", "Q5301561"], probabilities=[0.6, 0.1, 0.2])
kb.add_alias(alias="Douglas Adams", entities=["Q42"], probabilities=[0.9])

print()
print("Number of entities in KB:",kb.get_size_entities()) # 3
print("Number of aliases in KB:", kb.get_size_aliases()) # 2


# ## 候補生成
# 
# テキストエンティティが与えられた場合、ナレッジベースは、もっともらしい候補またはエンティティ識別子のリストを提供します。EntityLinkerは、候補のこのリストを入力として受け取り、ドキュメントのコンテキストを前提として、言及を最も可能性の高い識別子に変換します。
# 

# In[14]:


import spacy
from spacy.kb import KnowledgeBase

nlp = spacy.load('ja_ginza')
kb = KnowledgeBase(vocab=nlp.vocab, entity_vector_length=3)

# エンティティの追加
kb.add_entity(entity="Q1004791", freq=6, entity_vector=[0, 3, 5])
kb.add_entity(entity="Q42", freq=342, entity_vector=[1, 9, -3])
kb.add_entity(entity="Q5301561", freq=12, entity_vector=[-2, 4, 2])

# エイリアスの追加
kb.add_alias(alias="Douglas", entities=["Q1004791", "Q42", "Q5301561"], probabilities=[0.6, 0.1, 0.2])

candidates = kb.get_candidates("Douglas")
for c in candidates:
    print(" ", c.entity_, c.prior_prob, c.entity_vector)


# ## シリアライズ
# 
# パイプライン、語彙、ベクトル、エンティティを変更したり、モデルを更新したりしている場合は、最終的には進捗状況を保存する必要があります（たとえば、nlpオブジェクトにあるものすべて）。つまり、その内容と構造を、ファイルやバイト文字列などの保存可能な形式に変換する必要があります。このプロセスはシリアル化と呼ばれます。 「spaCy」には、シリアル化メソッドが組み込まれており、Pickleプロトコルをサポートしています。
# 
# すべてのコンテナクラス、つまり言語（nlp）、Doc、Vocab、StringStoreには、次のメソッドが用意されています。
# 
# メソッド | 戻り値 | 例
# --- | --- | ---
# to_bytes | bytes | data=nlp.to_bytes()
# from_bytes | object | nlp.from_bytes(data)
# to_disk | - | nlp.to_disk("/path")
# from_disk | object | nlp.from_disk("/path")
# 

# ## 訓練
# 
# spaCyのモデルは統計的であり、彼らが行うすべての "決定" - 例えば, どの品詞タグを割り当てるための品詞タグ, または単語が名前付きエンティティであるかどうか - 予測です. この予測は、モデルが訓練中に見てきた例に基づいています. モデルを訓練するには、まず訓練データ、つまりテキストの例と、モデルに予測させたいラベルが必要です。これは、品詞タグ、名前付きエンティティ、またはその他の情報である可能性があります。
# 
# 次に、モデルはラベルの付いていないテキストを表示し、予測を行います。正解がわかっているので、学習例と期待される出力との差を計算する損失関数の誤差勾配の形で、予測に対するフィードバックをモデルに与えることができます。差が大きければ大きいほど、勾配はより重要になり、モデルの更新はより重要になります。
# 
# https://spacy.io/training-73950e71e6b59678754a87d6cf1481f9.svg
# 
# モデルを訓練するとき、我々はモデルに単に例を記憶させるだけではなく、他の例で一般化できる理論を考え出させたいのです。結局のところ、ここにある "Amazon "のインスタンスが会社であることをモデルに学習させるだけではなく、このような文脈で "Amazon "が会社である可能性が高いことをモデルに学習させたいのです。そのため、学習データは常に我々が処理したいデータを代表するものでなければなりません。一人称の文章が非常に稀であるWikipediaで訓練されたモデルは、おそらくTwitterでは悪い結果になるでしょう。同様に、恋愛小説で訓練されたモデルは、法的な文章では悪い結果になる可能性が高いです。
# 
# これは、モデルがどのように動作しているか、正しい学習をしているかどうかを知るためには、トレーニングデータだけではなく、評価データも必要であることを意味します。もしモデルが訓練されたデータだけでテストした場合、モデルがどれだけ一般化しているかはわかりません。ゼロからモデルを訓練したい場合、通常、訓練と評価の両方に少なくとも数百の例が必要です。既存のモデルを更新するには、非常に少ない例ですでにまともな結果を得ることができます。

# ## 言語データ
# 
# すべての言語は異なります - そして通常、特に最も一般的な単語の中には、例外や特殊なケースがたくさんあります。これらの例外の中には言語間で共有されているものもあれば、完全に特殊なものもあります - 通常はハードコーディングが必要なほど特殊です。langモジュールには、すべての言語固有のデータが含まれており、シンプルなPythonファイルにまとめられています。これにより、データの更新や拡張が容易になります。
# 
# 例えば、基本的な句読点、絵文字、エモジ、エモーティコン、一文字の略語、「」や「」のようなスペルの異なる等価トークンのための規範などです。これにより、モデルはより正確な予測を行うことができます。サブモジュールの個々の言語データには、特定の言語にのみ関連するルールが含まれています。また、すべてのコンポーネントをまとめたり、言語サブクラスを作成したりします。
# 
# https://spacy.io/language_data-ef63e6a58b7ec47c073fb59857a76e5f.svg
# 
# 

# In[15]:



from spacy.lang.en import English
from spacy.lang.de import German
from spacy.lang.ja import Japanese

nlp_en = English()  # Includes English data
nlp_de = German()  # Includes German data
nlp_ja = Japanese() # includes Japanese Data


# ## アーキテクチャ
# 
# spaCyの中心的なデータ構造はDocとVocabです。Docオブジェクトは，トークンのシーケンスとそのすべてのアノテーションを所有しています．Vocabオブジェクトは、ドキュメント間で共通の情報を利用可能にするルックアップテーブルのセットを所有しています。文字列、単語ベクトル、語彙属性を一元化することで、これらのデータの複数のコピーを保存する必要がなくなります。これにより、メモリを節約し、真実のソースが単一であることを保証します。
# 
# テキスト注釈はまた、単一の真実のソースを使用できるように設計されています：Doc オブジェクトはデータを所有し、Span と Token はそのデータを指すビューです。Doc オブジェクトは Tokenizer によって構築され、パイプラインのコンポーネントによってその場で修正されます。Language オブジェクトは、これらのコンポーネントを調整します。生のテキストを取得してパイプラインに送り、注釈付きのドキュメントを返します。また、トレーニングとシリアライゼーションのオーケストレーションも行います。
# 
# https://spacy.io/architecture-bcdfffe5c0b9f221a2f6607f96ca0e4a.svg

# In[ ]:




