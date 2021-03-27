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
* cl-12 Prefixed abbreviations / 前置省略記号
* cl-13 Postfixed abbreviations / 後置省略記号
* cl-14 Full-width ideographic space / 和字間隔
* cl-15 Hiragana / 平仮名
* cl-16 Katakana / 片仮名
* cl-17 Math symbols / 等号類
* cl-18 Math operators / 演算記号
* cl-19 Ideographic characters / 漢字等（漢字以外の例）
* <del>cl-20 Characters as reference marks / 合印中の文字</del>
* <del>cl-21 Ornamented character complexes / 親文字群中の文字（添え字付き）</del>
* <del>cl-22 Simple-ruby character complexes / 親文字群中の文字（熟語ルビ以外のルビ付き）</del>
* <del>cl-23 Jukugo-ruby character complexes / 親文字群中の文字（熟語ルビ付き）</del>
* <del>cl-24 Grouped numerals / 連数字中の文字</del>
* <del>cl-25 Unit symbols / 単位記号中の文字</del>
* cl-26 Western word space / 欧文間隔
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



## Unicode属性での表現

* JLReq v2の表でUnicodeでEAW=Naのものは対応するU+FFXXの文字で置き換える
  * NKFC_Casefoldなどで対応をみる ([例](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3ANFKC_Casefold=%E2%A6%85%3A%5D))
* 基本的にEAW=F/A/W + Decomposition Type != Vertial/Smallでフィルタリングしたものから

* cl-01 始め括弧類
  * 提案: [General Category = Ps/Pi, EAW = F/A/W, Decomposition Type != Vertical/Small](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%5B%3ADecomposition_Type%21%3DSmall%3A%5D%26%5B%3ADecomposition_Type%21%3DVertical%3A%5D%5D%26%5B%5B%3AGeneral_Category%3DPs%3A%5D%5B%3AGeneral_Category%3DPi%3A%5D%5D%26%5B%5B%3AEast_Asian_Width%3DW%3A%5D%5B%3AEast_Asian_Width%3DA%3A%5D%5B%3AEast_Asian_Width%3DF%3A%5D%5D&g=&i=)
    * 追加される文字は[U+2329](https://util.unicode.org/UnicodeJsps/character.jsp?a=2329), [U+301A](https://util.unicode.org/UnicodeJsps/character.jsp?a=301A)
    * U+2329はDeprecatedにマークされている
    * [JLReq表とUnicodeの対応](references/cl-01-diff.html) ([TSV](references/cl-01-diff.tsv))、[Unicode Ps/Piの全リスト](references/cl-01-unicode.html) ([TSV](references/cl-01-unicode.tsv))
  * 表にあるU+00ABは削除
* cl-02 終わり括弧類
  * 提案: [General Category = Pe/Pf, FAW = F/A/W, Decomposition Type =! Vertical/Small](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%5B%3ADecomposition_Type%21%3DSmall%3A%5D%26%5B%3ADecomposition_Type%21%3DVertical%3A%5D%5D%26%5B%5B%3AGeneral_Category%3DPe%3A%5D%5B%3AGeneral_Category%3DPf%3A%5D%5D%26%5B%5B%3AEast_Asian_Width%3DW%3A%5D%5B%3AEast_Asian_Width%3DA%3A%5D%5B%3AEast_Asian_Width%3DF%3A%5D%5D&g=&i=)
    * 追加される文字は[U+232A](https://util.unicode.org/UnicodeJsps/character.jsp?a=232A), [U+301B](https://util.unicode.org/UnicodeJsps/character.jsp?a=301B), [U+301E](https://util.unicode.org/UnicodeJsps/character.jsp?a=301E)
    * [JLReq表とUnicodeの対応](references/cl-02-diff.html) ([TSV](references/cl-02-diff.tsv))、[Unicode Pe/Pfの全リスト](references/cl-02-unicode.html) ([TSV](references/cl-02-unicode.tsv))

## 議論リストでのピックアップ参照リスト

* ミーティング議事録系
  * [2021/3/9 JL-TF](https://lists.w3.org/Archives/Public/public-i18n-japanese/2021JanMar/0050.html)
  * [2020/12/1 JL-TF](https://lists.w3.org/Archives/Public/public-jlreq-admin/2020OctDec/0009.html)
  * [2020/10/20 JL-TF](https://lists.w3.org/Archives/Public/public-i18n-japanese/2020OctDec/0046.html)
