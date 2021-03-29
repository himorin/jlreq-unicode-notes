# JLReq文字クラス

## v2文字クラスリスト

* 削除のものは<del>文字クラス</del>表記に
* Unicode属性での置き換え検討の場合はサマリーを（詳細は下）

### リスト＋検討状況

* cl-01 Opening brackets / 始め括弧類
  * Unicodeでの置換: [General Category = Ps/Pi, EAW = F/A/W, Decomposition Type != Vertical/Small](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%5B%3ADecomposition_Type%21%3DSmall%3A%5D%26%5B%3ADecomposition_Type%21%3DVertical%3A%5D%5D%26%5B%5B%3AGeneral_Category%3DPs%3A%5D%5B%3AGeneral_Category%3DPi%3A%5D%5D%26%5B%5B%3AEast_Asian_Width%3DW%3A%5D%5B%3AEast_Asian_Width%3DA%3A%5D%5B%3AEast_Asian_Width%3DF%3A%5D%5D&g=&i=)
* cl-02 Closing brackets / 終わり括弧類
  * Unicodeでの置換: [General Category = Pe/Pf, FAW = F/A/W, Decomposition Type =! Vertical/Small](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%5B%3ADecomposition_Type%21%3DSmall%3A%5D%26%5B%3ADecomposition_Type%21%3DVertical%3A%5D%5D%26%5B%5B%3AGeneral_Category%3DPe%3A%5D%5B%3AGeneral_Category%3DPf%3A%5D%5D%26%5B%5B%3AEast_Asian_Width%3DW%3A%5D%5B%3AEast_Asian_Width%3DA%3A%5D%5B%3AEast_Asian_Width%3DF%3A%5D%5D&g=&i=)
* cl-03 Hyphens / ハイフン類
* cl-04 Dividing punctuation marks / 区切り約物
* cl-05 Middle dots / 中点類
* cl-06 Full stops / 句点類
* cl-07 Commas / 読点類
* cl-08 Inseparable characters / 分離禁止文字
* cl-09 Iteration marks / 繰返し記号
* cl-10 Prolonged sound mark / 長音記号
* cl-11 Small kana / 小書きの仮名
* <del>cl-12 Prefixed abbreviations / 前置省略記号</del>
* <del>cl-13 Postfixed abbreviations / 後置省略記号</del>
* cl-14 Full-width ideographic space / 和字間隔
  * U+3000だけなので文字指定？
* cl-15 Hiragana / 平仮名
  * [Script = Hiragana, Identifier Type != Obsolete](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3AScript%3DHiragana%3A%5D%26%5B%3AIdentifier_Type%21%3DObsolete%3A%5D) 93文字、小書きが混じる
* cl-16 Katakana / 片仮名
  * [Script = Katakana, Decomposition Type != Circle/Square, EAW = F/A/W, Identifier Type != Obsolete](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3AScript%3DKatakana%3A%5D%26%5B%3AIdentifier_Type%21%3DObsolete%3A%5D%26%5B%5B%3AEast_Asian_Width%3DF%3A%5D%5B%3AEast_Asian_Width%3DA%3A%5D%5B%3AEast_Asian_Width%3DW%3A%5D%5D%26%5B%5B%3ADecomposition_Type%21%3DCircle%3A%5D%26%5B%3ADecomposition_Type%21%3DSquare%3A%5D%5D) 113文字、小書きが混じる
* cl-17 Math symbols / 等号類
  * 文字を縦書きでの扱いに特化して整理する
* cl-18 Math operators / 演算記号
  * 文字を縦書きでの扱いに特化して整理する
* cl-19 Ideographic characters / 漢字等（漢字以外の例）
* <del>cl-20 Characters as reference marks / 合印中の文字</del>
* <del>cl-21 Ornamented character complexes / 親文字群中の文字（添え字付き）</del>
* <del>cl-22 Simple-ruby character complexes / 親文字群中の文字（熟語ルビ以外のルビ付き）</del>
* <del>cl-23 Jukugo-ruby character complexes / 親文字群中の文字（熟語ルビ付き）</del>
* <del>cl-24 Grouped numerals / 連数字中の文字</del>
* <del>cl-25 Unit symbols / 単位記号中の文字</del>
* cl-26 Western word space / 欧文間隔
  * 現状はU+0020の半角空白のみ
* cl-27 Western characters / 欧文用文字
* <del>cl-28 Warichu opening brackets / 割注始め括弧類</del>
* <del>cl-29 Warichu closing brackets / 割注終わり括弧類</del>
* <del>cl-30 Characters in tate-chu-yoko / 縦中横中の文字</del>


## クラス自体の改廃

* [2020/10/20議論](https://lists.w3.org/Archives/Public/public-i18n-japanese/2020OctDec/0046.html)
  * 削除: cl-24 連数字中の文字
    * JLReq中での参照箇所10カ所
    * 記述ごと削除なので含まれる文字・別表での扱いは検証しない
  * 削除: cl-30 縦中横
    * JLReq中での参照カ所0カ所
    * 縦中横ブロックの塊で漢字1文字として扱う記述にして文字クラスは削除
  * 削除: cl-21 親文字群中の文字（添え字付き）
    * JLReq中での参照カ所4カ所
    * JLReqでは扱わない方向ということで検証しない
  * 削除: cl-25 単位記号中の文字
    * JLReq中での参照カ所5カ所
    * JLReqでは扱わない方向ということで検証しない
  * 削除: 文脈依存クラス
    * 参照カ所は要確認、機能を絞った扱いの表が必要かも、ただし文字クラスとしては不要
    * cl-20 合印中の文字
      * JLReq中での参照箇所4カ所
    * cl-22 親文字群中の文字（熟語ルビ以外のルビ付き）
      * JLReq中での参照箇所0カ所
    * cl-23 親文字群中の文字（熟語ルビ付き）
      * JLReq中での参照箇所0カ所
    * cl-28 割注始め括弧類
      * JLReq中での参照箇所3カ所
    * cl-29 割注終わり括弧類
      * JLReq中での参照箇所3カ所
* [2020/12/01議論](https://lists.w3.org/Archives/Public/public-jlreq-admin/2020OctDec/0009.html)
  * 1) JIS-Unicode対応への疑問符
  * 2) cl-03のハイフン類の波線と長音としての利用の分離？
  * 3) 抜くことにした文字: [U+00AB](https://util.unicode.org/UnicodeJsps/character.jsp?a=00AB) (cl-01 -> 27), [U+00BB](https://util.unicode.org/UnicodeJsps/character.jsp?a=00BB) (cl-02 -> 27)
  * 4) cl-12,13を削除
    * 全角のものは漢字と同じ扱い、欧文幅のものは cl-27 （日本語以外の放り込み場所）に分配することになりました
      * この区別は UAX 50 の Vertical Orientation が R のものは欧文、U/Tu は和文ということで明確
    * cl-12 前置省略記号、cl-13 後置省略記号、ともJLReq内での参照カ所2カ所（べた組と分割禁止）
  * 6) [U+4EDD](https://util.unicode.org/UnicodeJsps/character.jsp?a=4EDD)の挙動は漢字と同じ
* [2020/12/16議論](https://lists.w3.org/Archives/Public/public-i18n-japanese/2020OctDec/0200.html)
  * cl-15/16に変体かな・合字を追加、enclosed circleはcl-19のまま - cl-19とはルビがかかるかどうかの違い
    * cl-15/16とcl-19がJLReqで同時に出現していない箇所は、3.3.8のルビのはみ出し、部分のみ
  * cl-17/18は日本語縦組みで正立で利用される記号のみにして整理


## Unicode属性での表現

* JLReq v2の表でUnicodeでEAW=Naのものは対応するU+FFXXの文字で置き換える
  * NKFC_Casefoldなどで対応をみる ([例](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3ANFKC_Casefold=%E2%A6%85%3A%5D))
* 基本的にEAW=F/A/W + Decomposition Type != Vertial/Smallでフィルタリングしたものから

* cl-01 始め括弧類
  * 提案: [General Category = Ps/Pi, EAW = F/A/W, Decomposition Type != Vertical/Small](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%5B%3ADecomposition_Type%21%3DSmall%3A%5D%26%5B%3ADecomposition_Type%21%3DVertical%3A%5D%5D%26%5B%5B%3AGeneral_Category%3DPs%3A%5D%5B%3AGeneral_Category%3DPi%3A%5D%5D%26%5B%5B%3AEast_Asian_Width%3DW%3A%5D%5B%3AEast_Asian_Width%3DA%3A%5D%5B%3AEast_Asian_Width%3DF%3A%5D%5D&g=&i=)
    * 追加される文字は[U+2329](https://util.unicode.org/UnicodeJsps/character.jsp?a=2329), [U+301A](https://util.unicode.org/UnicodeJsps/character.jsp?a=301A)
    * U+2329はDeprecatedにマークされている
    * [JLReq表とUnicodeの対応](references/cl-01-diff.html) ([TSV](references/cl-01-diff.tsv))、[Unicode Ps/Piの全リスト](references/cl-01-unicode.html) ([TSV](references/cl-01-unicode.tsv))
  * [表にあるU+00ABは削除](https://lists.w3.org/Archives/Public/public-jlreq-admin/2020OctDec/0009.html)
* cl-02 終わり括弧類
  * 提案: [General Category = Pe/Pf, FAW = F/A/W, Decomposition Type =! Vertical/Small](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%5B%3ADecomposition_Type%21%3DSmall%3A%5D%26%5B%3ADecomposition_Type%21%3DVertical%3A%5D%5D%26%5B%5B%3AGeneral_Category%3DPe%3A%5D%5B%3AGeneral_Category%3DPf%3A%5D%5D%26%5B%5B%3AEast_Asian_Width%3DW%3A%5D%5B%3AEast_Asian_Width%3DA%3A%5D%5B%3AEast_Asian_Width%3DF%3A%5D%5D&g=&i=)
    * 追加される文字は[U+232A](https://util.unicode.org/UnicodeJsps/character.jsp?a=232A), [U+301B](https://util.unicode.org/UnicodeJsps/character.jsp?a=301B), [U+301E](https://util.unicode.org/UnicodeJsps/character.jsp?a=301E)
    * [JLReq表とUnicodeの対応](references/cl-02-diff.html) ([TSV](references/cl-02-diff.tsv))、[Unicode Pe/Pfの全リスト](references/cl-02-unicode.html) ([TSV](references/cl-02-unicode.tsv))
    * 表にあるU+00BBに対応するEAW=F/A/Wの文字が見当たらない
  * [表にあるU+00BBは削除](https://lists.w3.org/Archives/Public/public-jlreq-admin/2020OctDec/0009.html)
* cl-03 ハイフン類
  * [General Category = Pd, FAW = F/A/W, Decomposition Type =! Vertical/Small](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%5B%3ADecomposition_Type%21%3DSmall%3A%5D%26%5B%3ADecomposition_Type%21%3DVertical%3A%5D%5D%26%5B%3AGeneral_Category%3DPd%3A%5D%26%5B%5B%3AEast_Asian_Width%3DW%3A%5D%5B%3AEast_Asian_Width%3DA%3A%5D%5B%3AEast_Asian_Width%3DF%3A%5D%5D&g=&i=)との比較
    * [U+2014](https://util.unicode.org/UnicodeJsps/character.jsp?a=2014), [U+2015](https://util.unicode.org/UnicodeJsps/character.jsp?a=2015), [U+3030](https://util.unicode.org/UnicodeJsps/character.jsp?a=3030), [U+FF0D](https://util.unicode.org/UnicodeJsps/character.jsp?a=FF0D)が追加になる
    * [JLReq表とUnicodeの対応](references/cl-03-diff.html) ([TSV](references/cl-03-diff.tsv))、[Unicode Pdの全リスト](references/cl-03-unicode.html) ([TSV](references/cl-03-unicode.tsv))
* [cl-04からcl-10の文字とUnicodeの対応](references/cl-0410-diff.html) ([TSV](references/cl-0410-diff.tsv))
  * cl-08 U+2014 (Pd)以外はGeneral Category = Po/Lm
  * [General Category = Po, FAW = F/A/W, Decomposition Type =! Vertical/Small](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%5B%3ADecomposition_Type%21%3DSmall%3A%5D%26%5B%3ADecomposition_Type%21%3DVertical%3A%5D%5D%26%5B%3AGeneral_Category%3DPo%3A%5D%26%5B%5B%3AEast_Asian_Width%3DW%3A%5D%5B%3AEast_Asian_Width%3DA%3A%5D%5B%3AEast_Asian_Width%3DF%3A%5D%5D&g=&i=): [Unicodeの該当文字リストと対応文字クラス](references/cl-Po-unicode.html) ([TSV](references/cl-Po-unicode.tsv))
  * [General Category = Lm, FAW = F/A/W, Decomposition Type =! Vertical/Small](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%5B%3ADecomposition_Type%21%3DSmall%3A%5D%26%5B%3ADecomposition_Type%21%3DVertical%3A%5D%5D%26%5B%3AGeneral_Category%3DLm%3A%5D%26%5B%5B%3AEast_Asian_Width%3DW%3A%5D%5B%3AEast_Asian_Width%3DA%3A%5D%5B%3AEast_Asian_Width%3DF%3A%5D%5D&g=&i=): [Unicodeの該当文字リストと対応文字クラス](references/cl-Lm-unicode.html) ([TSV](references/cl-Lm-unicode.tsv))
* cl-15, cl-16については、Scriptだけで切ってくると小書きが入る。が、分離可能な属性がない
  * [Script = Hiragana](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3AScript%3DHiragana%3A%5D&g=&i=): 小書き、変体かなを含む379文字
    * ひらがな U+3041-3096 ([U+3041 小書きのぁ](https://util.unicode.org/UnicodeJsps/character.jsp?a=3041)などを含む)
    * 繰り返し U+309D,309E
    * [U+309F (より)](https://util.unicode.org/UnicodeJsps/character.jsp?a=309F), [U+1F200 (ほか)](https://util.unicode.org/UnicodeJsps/character.jsp?a=1F200)
    * 歴史的かな [U+1B001](https://util.unicode.org/UnicodeJsps/character.jsp?a=1B001),U+1B150-1B152
    * 変体かな U+1B002-U+1B11E
  * [Script = Katakana](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3AScript%3DKatakana%3A%5D&g=&i=): 小書き、丸付きなどを含む304文字
    * カタカナ U+30A1-30FA ([U+30A1 小書きのァ](https://util.unicode.org/UnicodeJsps/character.jsp?a=30A1)などを含む)
    * 繰り返し U+30FD,30FE
    * [U+30FF (こと)](https://util.unicode.org/UnicodeJsps/character.jsp?a=30FF)
    * アイヌ発音用小書きのカタカナ U+31F0-31FF
    * 丸付きカタカナ U+32D0-32FE
      * [Decomposition Type = Circle](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3ADecomposition_Type%3DCircle%3A%5D)で抜ける
    * 2-4文字組んだ文字 U+3300-3357
      * [Decomposition Type = Square](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3ADecomposition_Type%3DSquare%3A%5D)で抜ける
    * 半角カタカナ U+FF66-FF9D (EAW=Narrow)
    * 歴史的カタカナ [U+1B000](https://util.unicode.org/UnicodeJsps/character.jsp?a=1B000)、小書き U+1B164-1B167
      * U+1B000のみIdentifier Type = Obsolete
  * 歴史的を抜いてで、小書きを含めてしまっていいなら以下で対応つく
    * cl-15 [Script = Hiragana, Identifier Type != Obsolete](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3AScript%3DHiragana%3A%5D%26%5B%3AIdentifier_Type%21%3DObsolete%3A%5D) 93文字
    * cl-16 [Script = Katakana, Decomposition Type != Circle/Square, EAW = F/A/W, Identifier Type != Obsolete](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3AScript%3DKatakana%3A%5D%26%5B%3AIdentifier_Type%21%3DObsolete%3A%5D%26%5B%5B%3AEast_Asian_Width%3DF%3A%5D%5B%3AEast_Asian_Width%3DA%3A%5D%5B%3AEast_Asian_Width%3DW%3A%5D%5D%26%5B%5B%3ADecomposition_Type%21%3DCircle%3A%5D%26%5B%3ADecomposition_Type%21%3DSquare%3A%5D%5D) 113文字
* cl-11 小書きのかな
  * JLReq利用箇所は6カ所、2.1.2の小書きの定義、3.1.1.cの縦横で異なる字面、3.1.7行頭禁足(2)、3.3.8ルビ(2)
  * 条件付き行頭禁足は[Line Break = Consitional Japanese Starter](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3ALine_Break%3DConditional_Japanese_Starter%3A%5D)で実現


## 議論リストでのピックアップ参照リスト

* ミーティング議事録系
  * [2021/3/9 JL-TF](https://lists.w3.org/Archives/Public/public-i18n-japanese/2021JanMar/0050.html)
  * [2020/12/16](https://lists.w3.org/Archives/Public/public-i18n-japanese/2020OctDec/0200.html)
    * [資料@icloud](https://www.icloud.com/numbers/0Xum3DF6I232izGhfJdk3s7Pw)
  * [2020/12/1 JL-TF](https://lists.w3.org/Archives/Public/public-jlreq-admin/2020OctDec/0009.html)
  * [2020/10/20 JL-TF](https://lists.w3.org/Archives/Public/public-i18n-japanese/2020OctDec/0046.html)
* 文字クラス関係のサマリー
  * [利用箇所一覧の説明](https://lists.w3.org/Archives/Public/public-i18n-japanese/2021JanMar/0051.html)
