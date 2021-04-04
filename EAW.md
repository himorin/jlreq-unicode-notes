# East Asian Width (EAW) の分類ごとに何が入ってくるか

## EAWの概要

[UAX #11](http://www.unicode.org/reports/tr11/)にあるコードポイントごとのEast Asianでの字幅についての属性。
以下は[UAX #11 38 (Unicode 13.0.0)](http://www.unicode.org/reports/tr11/tr11-38.html)ベースでの概要。

Wide/NarrowがEAWとEast Asianの両方の文脈で利用されているように見えるので区別がつくように記述してもらえた方がいいかも？

- ED1: レガシーな文字セットの定義で全角・半角の対応付けがあるものについて、抽象的な値としてnarrowもしくはwideの値を持たせられる (EAWとしてのアサインの値ではない、本文中では&lt;narrow&gt;,&lt;wide&gt;表記になっている)
- ED2: EAW = Fullwidth (F)は、&lt;wide&gt;になるように設定された全角幅を持つ互換文字に割り当てられる
  - [EAW=F](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3AEast_Asian_Width%3DF%3A%5D) 104コードポイント、U+3000, U+FF01-FF60, U+FFE0-FFE6の全角形のもの
- ED3: EAW = Halfwidth (H)は、&lt;narrow&gt;になるように設定された全角幅を持つ互換文字に割り当てられる、またU+20A9 (Won)を追加
  - [EAW=H](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3AEast_Asian_Width%3DH%3A%5D) 123コードポイント、U+20A9, U+FF61-FF64, U+FF65-FF9F (半角かな), U+FFA0-FFBE/FFC2-FFC7/FFCA-FFCF/FFD2-FFD7/FFDA-FFDC (半角ハングル要素), U+FFE8-FFEE (半角記号)
- ED4: EAW = Wide (W)は、常に&lt;wide&gt;・全角で表示される文字として定義されており、対応する半角を持つ文字、Emoji_Presentation (UTS#51)を持つ文字を含み、[Regional_IndicatorがYes](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3ARegional_Indicator%3DYes%3A%5D)を除く
  - [絵文字](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3AEmoji_Presentation%3DYes%3A%5D&g=&i=East_Asian_Width+Decomposition_Type)
  - [ハングル系](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3AScript%3DHangul%3A%5D&g=&i=East_Asian_Width+Decomposition_Type) (半角系など除き)
    - [ハングル字素](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=[:Block=Hangul_Jamo:])
    - [ハングル文字](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5Cp%7BBlock%3DHangul+Syllables%7D&g=&i=East_Asian_Width+Decomposition_Type)
  - [漢字系](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3AHanType%21%3Dna%3A%5D&g=&i=East_Asian_Width+Decomposition_Type) (HanType = Han, Hans, Hant)
    - いわゆる漢字、CJK Ideograph (+ Extension A-F), [CJK Compativility Ideograph](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5Cp%7BBlock%3DCJK+Compatibility+Ideographs%7D&g=&i=East_Asian_Width+Decomposition_Type) + Supplement
    - Radicals: [CJK](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5Cp%7BBlock%3DCJK+Radicals+Supplement%7D&g=&i=East_Asian_Width+Decomposition_Type), [Kangxi](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5Cp%7BBlock%3DKangxi+Radicals%7D&g=&i=East_Asian_Width+Decomposition_Type)
    - U+3005, U+3007, U+303B
    - U+3021-303A
  - かな系
    - [Script = hiragana](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3AScript%3DHiragana%3A%5D&g=&i=East_Asian_Width+Decomposition_Type): [Hiraganaブロック](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5Cp%7BBlock%3DHiragana%7D&g=&i=East_Asian_Width+Decomposition_Type)を含む
    - カタカナ系: [Katakanaブロック](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5Cp%7BBlock%3DKatakana%7D&g=&i=East_Asian_Width+Decomposition_Type)、[四角に収めたカタカナ複数文字](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5Cp%7Bsubhead%3DSquared+Katakana+words%7D&g=&i=East_Asian_Width+Decomposition_Type)
  - [Tangut](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3AScript%3DTangut%3A%5D&g=&i=East_Asian_Width+Decomposition_Type)
  - [bopomofo](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3AScript%3DBopomofo%3A%5D&g=&i=East_Asian_Width+Decomposition_Type)
  - [Nushu](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3AScript%3DNushu%3A%5D&g=&i=East_Asian_Width+Decomposition_Type)
  - [残り 1765文字](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3AEast_Asian_Width%3DW%3A%5D%26%5B%3AHanType%3Dna%3A%5D%26%5B%5B%3Ascript%21%3DHangul%3A%5D%26%5B%3AEmoji_Presentation%21%3DYes%3A%5D%26%5B%3AScript%21%3DHiragana%3A%5D%26%5B%3AScript%21%3DKatakana%3A%5D%26%5B%3Ascript%21%3Dtangut%3A%5D%26%5B%3Ascript%21%3DBopomofo%3A%5D%26%5B%3AScript%21%3DNushu%3A%5D%5D&g=&i=)は大半が記号と囲み文字など？
- ED5: EWA = Narrow (Na)は、&lt;narrow&gt;になる文字で必ずF/Wの互換文字を持ち、East asianの半角文字であるもの
  - [EAW=Na](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3AEast_Asian_Width%3DNa%3A%5D&g=&i=) 111コードポイント
  - US-ASCIIのU+0020-007E
  - Latin 1のU+00A2,00A3,00A5,00A6,00AC,00AF
  - その他の数学記号 U+27E6-27ED, U+2985,2986
- ED6: EAW = Ambiguous (A)は、narrowとwideの両方に文脈依存でなりえる文字
  - [EAW=A](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3AEast_Asian_Width%3DA%3A%5D)
  - 4.2 文脈依存でnarrow/wideのどちらにもなりえる、レガシーコードに依存しない場合はnarrow。それ以外ではFかH。
- ED7: EAW = Neutral (N)は、その他で、古典的な東アジアのエンコーディングでは出現しない文字
  - 理論的にnarrow/wideのどちらかという議論は当てはまらない(東アジアの組版では存在しなかったもの)が、現実的にはNaとして扱われるのが現実に即す
  - [EAW=N](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5B%3AEast_Asian_Width%3DN%3A%5D)

幅広くは
- wide: W, F, A (in east asian文脈)
- narrow: N, Na, H, A (in not east asian文脈)

### 文字幅へのマッピング (レガシーコードへのマッピング)

[UAX #11の5章](http://www.unicode.org/reports/tr11/tr11-38.html#Recommendations)には、

- UnicodeからEast asian legacy character encodingsへのマッピングの場合
  - Wide => Fullwidth
  - Narrow (+ Neutral) => Halfwidth
  - Halfwidth => Halfwidth
  - Ambiguous => Fullwidth
- Unicodeからnon East Asian legacy character encodingsへのマッピングの場合
  - Wide => マッピングしない
  - Narrow (+ Neutral) => 通常(narrow)文字へマッピング
  - Halfwidth => マッピングしない
  - Ambiguous => 通常(Narrow)文字へマッピング
