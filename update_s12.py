with open("2-translation/05_Chapter-5.md", "r", encoding="utf-8") as f:
    content = f.read()

old = """§12

>[!summary] Arabic Text
>

>[!summary] English Text
>

>[!summary] Kurdish Text
>

---

```mermaid
flowchart LR
P(پەڕەی 326)
```"""

new = """§12

>[!summary] Arabic Text
>109
>-
>لكن بعض الملحدين المعاصرين حاولوا أن يُحاكوا أسلوب القرآن
>
>❑
>
>مشر كو العرب كادت تطت قلوب هم من قوة القرآن، ويأتيك ملحد معارص ال يجيد نطق
>ي لمحاكاة بعض نصوص القرآن مستخدمً ا نفس العبارات
>العربية نطقً ا صحيحاً، فيأبر
>.القرآنية واألساليب القرآنية واللغة القرآنية
>
>
>فطاحل المشركين شعراء الجاهلية لو عرفوا أنَّ تحدي القرآن
>سيكون بهذه !الطريقة لربما انتحروا كمدًا
>•
>فالملحد .يستخدم عبارات قرآنية خالصة وأساليب قرآنية حرصية
>•
>فهل هذا تحدٍّ للقرآن؟
>•
>ي بنسقٍ جديدٍ كالذي جاء به القرآن، وليس
>الذي يريد تحدي القرآن عليه أنْ يأبر
>!مجرد التقليد المضحك
>•
>ن نفس
>تخي ل شخصً ا يتحدى الري
>دافنش فيُحرص
>المرين دافنش !
>ي
>ن دان
>تخي ل رد فعل ر ي
>دافنش !
>
>•
>سيسخر ر ي
>دافنش .من هذا الأسلوب السمج
>•
>إذا أردت تحدي القرآن، فأنت مُ طالب بنسق ثوري
>ي اللغة كالنسق الثوري الذي أحدثه القرآن
>جديد في .
>
>•
>.ولغة العرب شعر ونتر وقرآن
>
>•
>ولذلك توقف كُ فار العرب عن تحدي القرآن، ومن تقد م منهم كمسيلمة الكذ اب
>.صار أضحوكة
>•
>فهذا الطرح السمج من بعض الملحدين المعارصين دليلٌ مستقلٌ على إعجاز
>.القرآن
>•
>ولم يزل القرآن يقرع ،المشركين البلغاء أشد التقري ع ويُسفه ،أحالمهم ويذم
>،آلهتهم ويتحداهم ،أن يأتوا بمثله أو بسورةٍ من مثله وهم في كل هذا
>.منكصون عن معارضته، مُ حج ناكصون
>•
>بل لقد قال الله عز وجل للمشركين :ﭐﱡﭐﭐ
>ﳆ ﳇ
>ﳈ
>ﳉ
>ﳊ ..
>ﱠ
>﴿
>24
> .﴾ سورة
>البقرة
>•
>.فما فعلوا، وال قدروا

>[!summary] English Text
>109
>-
>But some contemporary atheists have attempted to imitate the style of the Quran
>
>❑
>
>The chieftains of the Arabs almost had their hearts fly from the power of the Quran, and there comes an atheist, a contemporary who does not master the pronunciation
>to imitate some Quranic texts using the same
>Quranic phrases, proper pronunciation, emerging
>.with Quranic styles and Quranic language
>
>
>The giants of the polytheists, the poets of the Jahiliyyah, if they knew that the Quran's challenge
>would be in this !way, perhaps they would have committed suicide out of grief
>•
>The atheist .uses purely Quranic phrases and Quranic styles, purely imitative
>•
>Is this a challenge to the Quran?
>•
>The one who wants to challenge the Quran must present a revolutionary
>system in language like the revolutionary system that the Quran brought
>!not just a ridiculous imitation
>•
>Imagine a person who challenges
>Da Vinci by knitting
>Mona Lisa !
>imagines
>Mona Lisa and paints her hair, and says to you: Here I am challenging
>Da Vinci!
>
>•
>Imagine the reaction of
>Da Vinci!
>
>•
>He will mock
>Da Vinci .for this ridiculous style
>•
>If you want to challenge the Quran, you are required to have a revolutionary
>linguistic system like the revolutionary system the Quran brought
>new in language.
>
>•
>.The language of the Arabs is poetry, prose, and Quran
>
>•
>Therefore the disbelievers of the Arabs stopped challenging the Quran, and those who advanced among them like Musaylimah the liar
>.became a laughingstock
>•
>So this ridiculous argument by some contemporary atheists is independent evidence of the
>miracle of the Quran
>•
>And the Quran never ceases to strike, the polytheist eloquent ones with the most severe rebuke, shattering their dreams, and cursing
>their idols, and challenging them to bring its like or a surah like it, and they in all this
>.are retreating from opposing it, humiliated
>•
>For Allah the Exalted said to the polytheists: Quranic verse
>ﭐﱡﭐﭐ
>ﳆ ﳇ
>ﳈ
>ﳉ
>ﳊ ..
>ﱠ
>﴿
>24
> .﴾ Surah
>Al-Baqarah
>•
>.They did not do it, nor were they able to

>[!summary] Kurdish Text
>109
>-
>بەڵام ھەندێک لە بێباوەڕان دواوینیان ھەوڵ دەدەن شێوازی قورئان بینین
>
>❑
>
>سەرۆکەکانی عەرەب دەقریب بوون دڵەیان فڕێن بە ھێزی قورئان، و ئێستا بێباوەڕێک دێتەوە کە نازان بۆ نووسینی
>بۆ محاکاتە بە کەمەکانی نوسی قورئان بەکاردێنەوە هەمان
>وشەکانی قورئان بە نووسینی دروست، دەرکەوتوون
>.بە شێوازی قورئانی و زمانی قورئانی
>
>
>سەرۆکەکانی مشرکان، شایریانەکانی جاهیلیا ئەگەر ناساند کە چالاکی قورئان
>بەم شێوەیە بێت، ھەندێ لەوانەش ھیوای خۆیان دەکەن بە تێکێشکراوێ
>•
>بێباوەڕ .بەکارھێنەرە وشەکانی قورئان و شێوازی قورئان، تەنها مانێ
>•
>ئایا ئەمە چالاکییەکە بۆ قورئان؟
>•
>کەسێک کە دەوێت قورئان چالاکی بکات دەبێت سیستەمێکی بانگەشکراو
>زمان بە هەمان سیستەمی بانگەشکراو کە قورئان ھاتووە
>نە تەنها مانێپولاسیون خەندە
>•
>بیر بکەرەوە کەسێک دژمن داڤینچی دەکرێت بە خێزاندن
>مۆنالیزا!
>تخی ل کەسێک کە مۆنالینزا ڕوون دەکات و جگە دەکات، و لێت دەڵێت: ھێرە من چالاک دەکەم
>داڤینچی!
>
>•
>بیر بکەرەوە وەڵامی داڤینچی!
>
>•
>دافینچی خەندە دەکات لەم شێوازی سمجمێ
>
>•
>ئەگەر دەوێت قورئان چالاکی بکەیت، دەبێت سیستەمێکی بانگەشکراو
>زمانی بە هەمان سیستەمی بانگەشکراو کە قورئان ھاتووە
>نوێ لە زمانی.
>
>•
>.زمان عەرەب شێعر و نثر و قورئان
>
>•
>بۆیە کافران عەرەب وەستاند لە چالاکی قورئان، و ھەوەکانیان بەربەخشیان وەک مێسێلەمە کذ اب
>.بووە خەنکە
>•
>بۆیە ئەم قسەی سمجم لە کەسێک لە بێباوەڕان دواوینیان بەڵگەی سەربەخۆیە بۆ مەعجەزە
>.قورئان
>•
>و نەوەستا قورئان ناوەستا دەدەق، مشرکانە بەھاوردان زۆر توندترین تێبینی، شاردن بیرۆکەیان و لێبێن
>،بۆتەکانیان و چالاکیان دەکەن کە ھاتن بە مێلەکی وەک ئەوە یان سورەیەک وەک ئەوە و ھەمەشە لەم
>.منکصن لە مقابڵە، مەتەکن
>•
>بۆیە خوا گەورە وت بۆ مشرکان: ئایەتی قورئان
>ﭐﱡﭐﭐ
>ﳆ ﳇ
>ﳈ
>ﳉ
>ﳊ ..
>ﱠ
>﴿
>24
> .﴾ سوورەی بەقەرە
>•
>.نەکرد، نە توانیان

---

```mermaid
flowchart LR
P(پەڕەی 326)
```"""

with open("2-translation/05_Chapter-5.md", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    "§12\n\n>[!summary] Arabic Text\n>\n\n>[!summary] English Text\n>\n\n>[!summary] Kurdish Text\n>\n\n---\n\n```mermaid\nflowchart LR\nP(پەڕەی 326)\n```",
    new,
)

with open("2-translation/05_Chapter-5.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Section 12 updated")
