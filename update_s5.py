with open("2-translation/06_Chapter-6.md", "r", encoding="utf-8") as f:
    content = f.read()

old = """§5

>[!summary] Arabic Text
>

>[!summary] English Text
>

>[!summary] Kurdish Text
>

---

```mermaid
flowchart LR
P(پەڕەی 341)
```"""

new = """§5

>[!summary] Arabic Text
>
>
>:َفعندما يُقرر جميعُ الفقهاء هذه القاعدة
>،أنَّ الأحكام التشريعية التي عليها مدارُ حياة الناس تُستمدُّ من الحديث الصحيح
>فهذا  تابعٌ  لتسليمهم  اليقيني بوثوقية  نقل  هذا  الحديث  الصحيح  من  فم
>النبي
>ﷺ
>!
>
>فأُمَّتُنا ليست من الأمم التي تتبع هواها في مصادر تلقي الشريعة، بل لا بد أن
>يكون المصدرُ قطعيَّ الثبوت عندهم حتى تُقام عليه الأحكام التشريعية
>فالتاريخ  موضوعيٌّ،  ومَن  نظر  فيه  بتجرُّد  سيعرف  مصداقية  الأمم  في  نقلها
>!لِلأخبار من عدم مصداقيتها
>.ولذلك مَن نظر في شواهد التاريخ ازداد يقينًا من وثوقية الحديث الصحيح عقال
>
>
>:وسأذكر مثالًا من شواهد التاريخ على ما أقول
>الحديث الأخت  الذي أوردناه
>حديث "
>وَ ي   ْ حَ عَ مَ ارَ تَقْ تُلُهُ الفِئَةُ البَاغِيَة حِين حَصَلَتِ الفِتْنَةُ يَوْمَ صِفِّي نَ
>كِانَ كُلُّ فَرِيق
>يَنْظُرُ مَن سَيَقْتُلُ عَمَارً ا ي جَيْش
>، وَحِينَ قَتَلَ بَعْضِ الرِّجَالِ فِي نِ يْ هللا عنه
>مُعَاوِيَة رَضِي اللهُ عَنهُ عَمَّارَ
>قَامَ عَمْرُ بْنُ العَاصِ !فَزِعاً (
>216
>)
>
>•
>عمرو بن العاص  انزعج حين علم أن عماراً
>قُتل على يد بعض رجال جيش معاوية
>رَضِي اللهُ عَنهُ.
>
>•
>طبعاً وكلا الفريقي ن كان مجتهداً، فكان قتال فتنةٍ كما أخبرت
>ﷺ،
>فمعاوية كان يرى أنه
>لا بد من القصاص من قتلة عثمان، وكان رَضِي اللهُ
>عَلِيٌّ رَضِي عنه يرى تأجيل
>الأمر لحين اجتماع كلمة المسلمين ، فحصلت هذه الفتنة وقُتل عمار، فَعلِمَ أن
>عليًّا
>كان أقرب الطائفتين إلى الحق، كما ورد في
>حديث مسلم . (
>217
>)
>
>•
>فالشاهد أن وثوقية الحديث النبوي هي قضية عقلية وشواهد التاري خ : انتظار
>الصحابة أي الفريقي ن سيَقتل عماراً تعطيك مِ نانًا عقليًّا تُرجح به بيقين أن هذا
>حديث خرج من فم النبي
>ﷺ
>، وأن الصحابة كانوا يعلمون أن عماراً سيُقتل لكنهم
>!فقط يريدون أنْ يعرفوا أي الفريقي ن أذن للحق
>• فهذا الحديث وحده برهانٌ مستقلٌّ على صحة
>!الرسالة لمن تأمل
>
>      
>
>(216) الصحيح
>:المسند، الوادعي ح1012
>.
>
>(217) صحيح
>:مسلم ح1064
>.

>[!summary] English Text
>
>
>When all jurists establish this rule
>,that the legislative rulings upon which people's lives depend are derived from the authentic hadith
>So this  follows  their  certain acceptance of the reliability of the transmission of this authentic hadith from the mouth of
>the Prophet
>ﷺ
>!
>
>So our Ummah is not one of those nations that follow their whims in the sources of receiving legislation, but it is necessary that
>the source be definitive in authenticity for them so that legislative rulings can be established upon it
>History  is objective,  and whoever  examines  it  with  detachment  will  know  the  credibility  of  nations  in  their  transmission
>of
>news from their lack of credibility
>.Therefore whoever examines historical evidences will increase in certainty of the authenticity of the authentic hadith
>
>
>:And I will give an example from historical evidences for what I say
>The hadith we mentioned earlier
>Hadith "
>AND AMMAR, THE OPPRESSIVE FACTION WILL KILL HIM WHEN FITNA OCCURS ON THE DAY OF SIFFIN
>EACH
>TEAM
>LOOKED AT WHO WOULD KILL AMMAR, AND WHEN SOME MEN KILLED AMMAR IN MU'AWIYA'S ARMY
>AMR IBN AL-AS JUMPED IN TERROR (
>216
>)
>
>•
>Amr ibn al-As was disturbed when he learned that Ammar
>was killed by some men of Muawiya's army
>
>•
>Naturally both parties were mujtahids, so it was a fitna battle as the Prophet
>ﷺ
>foretold,
>so Muawiyah believed that he
>must exact retribution for Uthman's killers, and Ali
>may Allah be pleased with him believed in postponing
>the matter until the unity of the Muslims is achieved, so this fitna occurred and Ammar was killed, SO IT BECAME KNOWN THAT
>ALI
>was closer of the two parties to the truth, as mentioned in
>Muslim's hadith. (
>217
>)
>
>•
>So the evidence is that the reliability of the Prophetic Hadith is a rational issue and historical evidences: the Companions waiting for
>which of the two parties would kill Ammar gives you a rational certainty that strengthens certainty that this
>Hadith came from the mouth of the Prophet
>ﷺ
>and that the Companions knew Ammar would be killed, but they
>!only wanted to know which party was more deserving of the truth
>• So this hadith alone is an independent proof of
>the truth of the message for those who reflect
>
>      
>
>(216) Sahih
>:Al-Musnad, Al-Wadi'i 1012
>.
>
>(217) Sahih
>:Muslim 1064
>.

>[!summary] Kurdish Text
>
>
>کاتێک ھەموو فەقیهەکان ئەم بنەمایە دابین دەکەن
>،کە یاساکانی یاسایی کە ژیانی مرۆڤ بەسەرەوە دەبن بە سەرەوەی قسیی سەحیح
>بۆیە ئەمە دەیاتەوە
>بە یقینی قاچکردنەوەیان بە دروستی ڕوانەکردنی ئەم قسیی سەحیح لە دەمی
>نێب
>ﷺ
>!
>
>بۆیە نەتەوەی ئێمە نییە لە نەتەوەکانەوە کە دەچن بەرەو ھەواس خۆیان لە سەرچاوەکانی وەرگرتنی یاسا، بەڵکو دەبێت
>سەرچاوەکە قەطەعی بێت بۆ دروستییان ھەتا یاساکانی یاسایی دابنێرێنەوە لێی
>مێژوو بنەڕەتییە، و ھەرکەس لێی بە بينینی بێتاڵان دەزانیت باوەڕپێکردنی نەتەوەکان لە نووسینی خەبەرەکانیان
>!.بۆیە ھەرکەس مێژوو بینین بکات ھەوڵی زۆرتر دەکات بۆ یقین لە دروستی قسیی سەحیح
>
>
>:و من نموونەیەک دەھێنم لە مێژوو بۆ ئەوەی د۵ڵێم
>قسەکەی پێشتر ماوی مان
>قسە
>\"و یَح عَ مَارَ تَقْ تُلُهُ الفِئَةُ البَاغِيَة حِين حَصَلَتِ الفِتْنَةُ يَوْمَ صِفِّي نَ
>ھەر
>تاڵە
>چاوەڕوان بکات کە کەسێک لە هەردوو گرووپەکە دەبینێت کە دەکۆیەت عەمەر ی جەنگ
>مەعوïa
>، و کاتێک کەسێک لە مێردان لە جەنگی مەعوïa
>عەمرو بن عاص !ترسیان(
>216
>)
>
>•
>عەمرو بن عاص تەرس بوو کاتێک زانی کە عەمەر
>کوژرا لەلایەن ھێزەکانی مەعوïa
>
>•
>بە تەواوی ھەردوو گرووپەکە مجتھەد بوون، بۆیە جەنگی فتەنە بوو وەک کە پێغەمبەر
>ﷺ پێشەنگ کرد،
>بۆیە مەعوïa فکر کرد کە
>دەبێت قەصاص لە قاتیلانی عوسمان، و عەلی
>خوا ڕەحمەتی لێی بێت فکر کرد دوگەڕانەوە
>بۆوەی یەکگرتووی موسڵمانان، بۆیە ئەم فتەنە روویدا و کوژرا عەمەر، بۆیە دەزانی کە
>عەلی
>نزدیکتر بوو بە ھێوازی ھێوازییان بۆ ڕاستی، وەک کە لە قسیی مەسلم وتووە. (
>217
>)
>
>•
>بۆیە بەڵگەیەکە کە دڵنیای قسیی پێغەمبەری کێشەیەکە بیروانە و مێژووییە: چاوەڕوانی ھاوبەشەکانی کەو کەس دەکۆیەت عەمەر دەدەن بۆت یقین بیروانە بۆوەی قسییەکە لە دەم پێغەمبەر
>ﷺ دەرچووە، و ھاوبەشەکان ناسن کە عەمەر دەکۆیێت، بەڵام
>تەنها دەوێن کە کۆمەڵەکە کە باشتر دەبێت بۆ ڕاست
>• بۆیە ئەم قسەیە تەنها بەڵگەیەکی سەربەخۆیە بۆ ڕاستیی ڕسول
>بۆ کەسێک کە بیر دەکات
>
>      
>
>(216) سەحیح
>:مەسند، وادیعی ١٠١٢
>.
>
>(217) سەحیح
>:مەسلم ١٠٦٤
>.

---

```mermaid
flowchart LR
P(پەڕەی 341)
```"""

with open("2-translation/06_Chapter-6.md", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    "§5\n\n>[!summary] Arabic Text\n>\n\n>[!summary] English Text\n>\n\n>[!summary] Kurdish Text\n>\n\n---\n\n```mermaid\nflowchart LR\nP(پەڕەی 341)\n```",
    new,
)

with open("2-translation/06_Chapter-6.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Section 5 updated")
