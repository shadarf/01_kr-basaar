with open("2-translation/05_Chapter-5.md", "r", encoding="utf-8") as f:
    content = f.read()

# Sections 13-22 replacements
replacements = {}

# Section 13 - Page 327
replacements[
    "§13\n\n>[!summary] Arabic Text\n>\n\n>[!summary] English Text\n>\n\n>[!summary] Kurdish Text\n>\n\n---\n\n```mermaid\nflowchart LR\nP(پەڕەی 327)\n```"
] = """§13

>[!summary] Arabic Text
>
>
>ولإلنسان أن يتساءل: كيف يجرؤ ُّالنبي ﷺ
>أن يتحدى أناسً ا في جنس
>ما يحسنون ويبدعون، ثم يتركهم وقد عالهم الخزي على مر السنين؟
>
>
>يقول د. عبد الله دراز :رحمه الله "ألم يكن يخشى الرسول
>ﷺ
>دألا مهتَّيمح ريثي نأ يدحتلا اذهب
>صيغة المعارضة، ثم يتناولها سائرهم ب
>نقد الشعر، ثم لو طوعت له نفسه صلى الله عليه وسلم أن ي
>هذا الحكم على أهل عصره أنهم يعجزون عن قبول تحدي
>وهو يعلم أن الجميع سيفشل على مر العصور
>•
>ر ي ءٍ يستر ي ح
>ي عباراتٍ محرجةٍ ، ولم يأتِ أحدٌ منهم بش
>لقد تحد ى القرآنُ أهلَ البيان في
>!له المالحدة
>
>
>يقول
>الأُلوشي :رحمه الله "فلم ينطق أحدٌ منهم إلى يو
>
>
>
>وقد رأى الكفار أنا تجميع الجيوش وتحزيب الأحزاب لمحاربة
>رسول
>الله ﷺ
>أُهون
>.وأيشُ من معارضة القرآن وقبول التحدي
>!فهذا منتهى ما يملكون
>ﭐﱡﭐ
>ﲞ ﲟ
>ﲠ ﲡ
>ﲢ ﲣ
>ﲤ
>ﲥ
>ﲦ
>ﲧ
>ﲨﱠ﴿
>26
> .﴾سورة
>فصلت.
>
>      
>
>(189) النبأ العظيم، د. عبد الله دراز، ص44
>- 45
>.
>(190)
>الدالئل العقلية، الأُلوسي. مخطوط
>.

>[!summary] English Text
>
>
>And for man to wonder: how dare the Prophet ﷺ
>challenge people in a field
>where they excel and innovate, then leave them humiliated for years?
>
>
>Dr. Abdullah Draz - may Allah have mercy on him - says: "Was the Messenger not afraid
>ﷺ
>that the opposition would take the form of
>poetry criticism, then all of them would engage in it,
>this judgment on his contemporaries that they are unable to accept the challenge
>and he knows that everyone will fail throughout the ages
>•
>Something that covers their
>embarrassing phrases, and none of them brought
>The Quran challenged the people of eloquence in
>!it is the end of what they have
>
>
>Al-Alusi says: may Allah have mercy on him: "No one of them spoke until today
>
>
>
>And the disbelievers saw that gathering armies and forming parties to fight
>the Messenger of Allah
>ﷺ
>is easier
>and less than opposing the Quran and accepting the challenge
>!This is the utmost they can do
>ﭐﱡﭐ
>ﲞ ﲟ
>ﲠ ﲡ
>ﲢ ﲣ
>ﲤ
>ﲥ
>ﲦ
>ﲧ
>ﲨﱠ﴿
>26
> .﴾Surah
>Fussilat.
>
>      
>
>(189) The Great News, Dr. Abdullah Draz, p44
>- 45
>.
>(190)
>Rational Proofs, Al-Alusi. Manuscript
>.

>[!summary] Kurdish Text
>
>
>و بۆ مرۆڤ دەبێت پرسیار بکات: چۆن پێغەمبەر ﷺ
>دەکرێت چالاکی بکات لە بەشێکدا کە ھەن ناسن و ھەن جوان دەکەن، پاشان دەخڵینێنێت و دڵیان لە شەرمەوە دەکەوێت بۆ ساڵان؟
>
>
>د. عەبدوڵڵا دراز وتووە: سڵاو ی خوا لێی بێت "ئایا پێغەمبەر
>ﷺ
>نەترسیدا لەوەی دژدارانەکە شێوازی قسە بکەن بۆ
>پێچەوانە، پاشان ھەموویان دەگرن بە قسەکردنەوە لەسەر شێعر، پاشان ئەگەر خۆی بە پێوەندی بەخۆی دەخاتە بەرچاو، کە
>ئەم ھێنانییە لەسەر کەسانەکانی دۆری خۆی کە ناتوانن چالاکی بکەن لە ھەموو کاتە
>•
>شتێک کە دابەش دەکات بۆ
>شەرمخوازیییان، و ھەیەک لەوانە ووشەی تەنھا نەهات، ھێشتا لەوانەش نەبوون
>قورئان چالاکی کردووە لە بەشێکدا لە بەشداریدا
>بە قسەی شێعر، پاشان لۆ لەوانە ناتوانن بە ھەموو دۆران
>•
>قسەیەکانی تەنھا پێش دڵدا، و ھیچ کەسێک لەوانەش ووشەی تەنھا نەهات
>قورئان چالاکی کرد لە بەشێکدا لە ناسنامەناسەکاندا
>!بۆوەی بێباوەڕان
>
>
>ئەلولوشی وتووە: سڵاو ی خوا لێی بێت "ھیچ کەسێک لەوانە نەقسی، ھەتا ئێستا
>
>
>
>و بێباوەڕان دەبینن کە ھێزەکانیان ھەیە بە ھێزکردنەوەی هێزەکان و بەندکردن پارتی بۆ جەنگی
>پێغەمبەر
>ﷺ
>ھەوە
>باشتر
>.و کەمتر لە مقابڵەکردنی قورئان و مقبولی چالاکی
>!ئەمە کۆتایی ئەوەی ھەیە لەدەستیان
>ﭐﱡﭐ
>ﲞ ﲟ
>ﲠ ﲡ
>ﲢ ﲣ
>ﲤ
>ﲥ
>ﲦ
>ﲧ
>ﲨﱠ﴿
>26
> .﴾سوورەی فەصڵەت.
>
>      
>
>(189) نەبەی گەورە، د. عەبدوڵڵا دراز، ص44
>- 45
>.
>(190)
>ھێنانی بیرکردنەوەیی، ئەلولوشی. دەستنووس
>.

---

```mermaid
flowchart LR
P(پەڕەی 327)
```"""

# Section 14 - Page 328
replacements[
    "§14\n\n>[!summary] Arabic Text\n>\n\n>[!summary] English Text\n>\n\n>[!summary] Kurdish Text\n>\n\n---\n\n```mermaid\nflowchart LR\nP(پەڕەی 328)\n```"
] = """§14

>[!summary] Arabic Text
>
>
>وعندما قدِ م الطفيل بن عمرو الدوشي-
>رئيس قبيلة دوس في اليمن-
>وكان شاعراً
>مُ فو هً ا، عندما قدم مكة استقبله كُفار مكة وكعادتهم حذ روه من سماع قرآن محمد
>ﷺ
>لئًل ينجذب لسحره، حنر حشا أذنه بالقطن لكن ه شعر أن هذا أسلوب سخيف، فقال
>ي نفسه
>نفس "إني لبيبٌ
>وشاعرٌ، ولا يخفى ع
>عليه قلبَهُ وأسلَمَ".(191)
>•
>ي الفِطر والنفوس عجيبٌ، فالقرآن يُذيب جبال الغِلظة، ويشرَح
>أثرُ القرآن في
>الصدر، ويخطف الألباب
>•
>وكان أبو بكر
>حين يقرأ القرآن تصطف نساء المشركين حول بيته من فرط انجذابهم
>وتأثرهم بالقرآن، حنر أفزع ذلك رجال قريش.(192)
>
>•
>ي القلب ويغرس الإيمان
>فأثرُ القرآن في
>
>
>ولما سمع الوليد بن المغيرة وهو من أشد الناس كفراً، لما سمع من النبي
>ﷺ
>بعض
>القرآن قال "وماذا أقولُ فواللهِ م
>
>
>أما ن بن الحارث
>الن رص :فكان يقول وقلتم شاعر، لا والله ما هو بشعر
>•
>فالكل كان يُجمع على إعجاز هذا القرآن، ولم يمنع المشركين من الإسلام إلا الكِت
>!والحقد
>ﭐﱡﭐ
>ﱁ
>ﱂ
>ﱃ
>ﱄ
>ﱅ ﱆﱇ ..
>ﱠ
>﴿
>14
> .﴾ سورة النمل 
>          
>
>(191) دلائل النبوة، الأصبهاني1
>/ 312
>.
>(192) صحيح
>البخاري، ح3905
>.
>(193) لباب النقول، السيوطي319، بإسناد صحيح على شرط الشيخين
>.

>[!summary] English Text
>
>
>And when Al-Tufayl ibn Amr al-Dawsi-
>the chief of the tribe of Daws in Yemen-
>came, and he was a poet
>highly articulate, when he came to Mecca the polytheists of Mecca received him and as usual warned him against listening to the Quran of Muhammad
>ﷺ
>lest he be attracted to its magic, but he felt that this was a silly method, so he said
>to himself
>"I am intelligent
>and a poet, and nothing is hidden from
>his heart, and he became Muslim".(191)
>•
>In the nature and souls is wondrous, the Quran melts mountains of harshness, and expands
>The effect of the Quran on
>the chest, and captures the hearts
>•
>And Abu Bakr
>when he recites the Quran, the polytheist women line up around his house from excessive attraction
>and their being moved by the Quran, when it terrified the men of Quraysh.(192)
>
>•
>On the heart and plants faith
>The effect of the Quran on
>
>
>And when Al-Walid ibn Al-Mughirah heard, and he was one of the most severe people in disbelief, when he heard from the Prophet
>ﷺ
>some
>of the Quran he said "And what do I say, by Allah, m
>
>
>As for Al-Nadr ibn Al-Harith
>may Allah be pleased with him: he used to say and you said poet, by Allah it is not poetry
>•
>Everyone used to agree on the miracle of this Quran, and nothing prevented the polytheists from Islam except arrogance
>!and malice
>Quranic verse
>ﭐﱡﭐ
>ﱁ
>ﱂ
>ﱃ
>ﱄ
>ﱅ ﱆﱇ ..
>ﱠ
>﴿
>14
> .﴾ Surah An-Naml 
>          
>
>(191) Evidence of Prophethood, Al-Asbahani1
>/ 312
>.
>(192) Sahih
>Bukhari 3905
>.
>(193) Lubab al-Nuqul, Al-Suyuti 319, with authentic chain on the condition of the two sheikhs
>.

>[!summary] Kurdish Text
>
>
>و کاتێک طەفیل بن عەمر دوشی-
>سەرۆکەی تایفەی دۆس لە یەمەن-
>ھات، و کە شایەرێک
>بەھێز بوو، کاتی کە گەیشتە مەککە مەشرکان مەککەی پێشووەی وەکو هەمیشە باوان لێی وای کردن لە گوێگرتنی قورئانی محەمەد
>ﷺ
>بۆوەی نەچێتەوە جادووە، بەڵام ھەستی کرد کە ئەم شێوەیە خەمە، بۆیە وت
>بۆ خۆی
>"من زۆر باشم و شایەرێکم، و ھیچ شتێک لێرەدا نەماوە
>لە دڵم و شێوازی، و موسڵمان بوو".(191)
>•
>بە فەطرەت و روون بەشیدا، قورئان چیاکان دەخۆشنەوە، و دەڕوون دەکات
>ھێنانی قورئان لەسەر
>سەین، و دڵەکان دەکەشێنەوە
>•
>و ئەبۆ بەکر لە کاتی خوێندنەوەی قورئان دەرچون ژنانی مشرکان لەبەر ماڵەکەی بەھۆی فڕاوەوە
>و کاریان بە ھۆی قورئان، کاتێک ترسیان لێیدا پیاوان قورەیش.(192)
>
>•
>لەسەر دڵ و ناسیان باوەڕ
>ھێنانی قورئان
>
>
>و کاتێک وەلید بن موعەیرە گوێی لەسەر، کە یەکە لە توندترین مرۆڤان بێباوەڕ، گوێی لە پێغەمبەر
>ﷺ
>ھەن
>قسەی قورئان وت "و چی د۵لیم بۆ خوا،
>
>
>بۆوەی ن بن حەریس
>نەزەر بێت: وت وەستای شایەر، بە خوا ما ھەیە شێعر
>•
>ھەمووان راون بە مەعجەزەکەی ئەم قورئان، و نەوەک مەترسی و حەقد مەنەوان لە ئیسلام(191)
>!و کەبر و حەقد
>ئایەتی قورئان
>ﭐﱡﭐ
>ﱁ
>ﱂ
>ﱃ
>ﱄ
>ﱅ ﱆﱇ ..
>ﱠ
>﴿
>14
> .﴾ سوورەی نەمڵ 
>          
>
>(191) دەلالێ نبووە، ئەسپێهان1
>/ 312
>.
>(192) سەحیح
>بوخاری 3905
>.
>(193) لەباب نووقڵ، سیووتی 319، بە سندە دروستەکە لە شەرتی دوو شێخ
>.

---

```mermaid
flowchart LR
P(پەڕەی 328)
```"""

# Section 15 - Page 329
replacements[
    "§15\n\n>[!summary] Arabic Text\n>\n\n>[!summary] English Text\n>\n\n>[!summary] Kurdish Text\n>\n\n---\n\n```mermaid\nflowchart LR\nP(پەڕەی 329)\n```"
] = """§15

>[!summary] Arabic Text
>
>
>وأثرُ القرآن في الفِطر والنفوس عجيبٌ، فالقرآن يُذيب جبالَ الغِلظةَ، ويشرَح
>الصدر، ويخطف الألباب
>•
>فأثرُ القرآن في
>ي القلب ويغرس الإيمان
>
>
>ولما سمع الوليد بن المغيرة وهو من أشد الناس كفراً، لما سمع من النبي
>ﷺ
>بعض
>القرآن قال "وماذا أقولُ فواللهِ م
>
>
>أما ن بن الحارث
>الن رص :فكان يقول وقلتم شاعر، لا والله ما هو بشعر
>•
>فالكل كان يُجمع على إعجاز هذا القرآن، ولم يمنع المشركين من الإسلام إلا الكِت
>!والحقد
>ﭐﱡﭐ
>ﱁ
>ﱂ
>ﱃ
>ﱄ
>ﱅ ﱆﱇ ..
>ﱠ
>﴿
>14
> .﴾ سورة النمل 
>          
>
>(191) دلائل النبوة، الأصبهاني1
>/ 312
>.
>(192) صحيح
>البخاري، ح3905
>.
>(193) لباب النقول، السيوطي319، بإسناد صحيح على شرط الشيخين
>.

>[!summary] English Text
>
>
>And the effect of the Quran on the nature and souls is wondrous, the Quran melts mountains of harshness, and expands
>the chest, and captures the hearts
>•
>So the effect of the Quran on
>the heart and plants faith
>
>
>And when Al-Walid ibn Al-Mughirah heard, and he was one of the most severe people in disbelief, when he heard from the Prophet
>ﷺ
>some
>of the Quran he said "And what do I say, by Allah, m
>
>
>As for Al-Nadr ibn Al-Harith
>may Allah be pleased with him: he used to say and you said poet, by Allah it is not poetry
>•
>Everyone used to agree on the miracle of this Quran, and nothing prevented the polytheists from Islam except arrogance
>!and malice
>Quranic verse
>ﭐﱡﭐ
>ﱁ
>ﱂ
>ﱃ
>ﱄ
>ﱅ ﱆﱇ ..
>ﱠ
>﴿
>14
> .﴾ Surah An-Naml 
>          
>
>(191) Evidence of Prophethood, Al-Asbahani1
>/ 312
>.
>(192) Sahih
>Bukhari 3905
>.
>(193) Lubab al-Nuqul, Al-Suyuti 319, with authentic chain on the condition of the two sheikhs
>.

>[!summary] Kurdish Text
>
>
>و ھێنانی قورئان لەسەر فەطرەت و روون بەشیدا، قورئان چیاکان دەخۆشنەوە، و دەڕوون دەکات
>سەین، و دڵەکان دەکەشێنەوە
>•
>بۆوەی بەکر لە کاتی خوێندنەوەی قورئان دەرچون ژنانی مشرکان لەبەر ماڵەکەی بەھۆی فڕاوەوە
>و کاریان بە ھۆی قورئان، کاتێک ترسیان لێیدا پیاوان قورەیش.(192)
>
>•
>لەسەر دڵ و ناسیان باوەڕ
>ھێنانی قورئان
>
>
>و کاتێک وەلید بن موعەیرە گوێی لەسەر، کە یەکە لە توندترین مرۆڤان بێباوەڕ، گوێی لە پێغەمبەر
>ﷺ
>ھەن
>قسەی قورئان وت "و چی د۵لیم بۆ خوا،
>
>
>بۆوەی ن بن حەریس
>نەزەر بێت: وت وەستای شایەر، بە خوا ما ھەیە شێعر
>•
>ھەمووان راون بە مەعجەزەکەی ئەم قورئان، و نەوەک مەترسی و حەقد مەنەوان لە ئیسلام(191)
>!و کەبر و حەقد
>ئایەتی قورئان
>ﭐﱡﭐ
>ﱁ
>ﱂ
>ﱃ
>ﱄ
>ﱅ ﱆﱇ ..
>ﱠ
>﴿
>14
> .﴾ سوورەی نەمڵ 
>          
>
>(191) دلائل النبوة، الأصبهاني1
>/ 312
>.
>(192) سەحیح
>بوخاری 3905
>.
>(193) لباب النقول، السيوطي 319، بە سندە دروستەکە لە شەرتی دوو شێخ
>.

---

```mermaid
flowchart LR
P(پەڕەی 329)
```"""

# Section 16 - Page 330
replacements[
    "§16\n\n>[!summary] Arabic Text\n>\n\n>[!summary] English Text\n>\n\n>[!summary] Kurdish Text\n>\n\n---\n\n```mermaid\nflowchart LR\nP(پەڕەی 330)\n```"
] = """§16

>[!summary] Arabic Text
>
>
>وهم يقتلون أولادهم خشية الإملاق وخوف الفقر ، وكان بعضهم ينذ ر إذا بلغ عدد
>أولاده عشراً نحر واحداً منهم، كما حصل مع عبد المطلب جد النبي ﷺ .
>
>•
>في هذه البيئة أتى الإسلام!
>•
>في هذا الجو ظهر النبيُّ محمد ﷺ .
>
>
>قال المقداد بن الأسود :
>"واللهِ لقد بُعِثَ النبي
>م ٌّيبن اهيلع ثِعُب ٍلاح ِّدشأ ىلعﷺ
>
>
>
>وانظر لقول رَ جَ اءٍ العُ طَ ارِدِ ي ي
>ذاك الوقت والحديث في
>ي حال العرب في
>فن البخاري :قال "كُنَّا نَعْبُدُ الحَجَرَ، فَإِذَا وَجَدْنَا حَجَراً هو أخْيَرُ منه ألْقَيْنَاهُ، وأَخَذْنَا الآخَرَ، فَإِ
>•
>فِيَدْخُلُونَ عَلى المَرْأَة، كُلُّهُم يُصِيبُهَا
>ي البيت، كُلُّهُم يُصِيبُهَا
>الخندق .
>الخندق .
>الحديث في
>البخاري
>(206
>)
>
>•
>،وكانت المرأة تُورَ ث كما يُورَ ث المتاع، وكانت بعض الأطعمة تُمنع النساء من أكلها
>ويختص بأكلها الرجال فقط: ﭐﱡﭐ ﱝ ﱞ ﱟ ﱠ ﱡ ﱢ ﱣ ﱤ
>ﱥ ﱦ ﱠﱧﱨ
>﴿
>193
> .﴾ سورة الأنعام
>
>
>حنر قال
>عمر بن الخطاب
>في الحديث المتفق على صحته
>ن ي هللا عنه
>رص "واللَّهِ إنْ كُنَّا في الجَاهِلِيَّةِ ما نَعُدُّ لِلنِّسَاءِ أمْراً، حتَّى أنْزَلَ اللَه ف
>❑
>
>في هذا العالم الحالك السواد جاء نورُ الإسلام، وأنزل الله كتابه؛ ليصحح كل هذا
>!الفساد والظلم والفجور
>
>      
>
>(204) صحيح
>ابن حبان ح6552
>.
>(205) صحيح
>البخاري ح4376
>.
>(206) صحيح
>البخاري ح5127
>.
>(207) صحيح
>البخاري ح4913
>.

>[!summary] English Text
>
>
>And they kill their children for fear of poverty and poverty, and some of them would vow that if the number
>of their children reached ten, they would slaughter one of them, as happened with Abdul Muttalib, the grandfather of the Prophet ﷺ .
>
>•
>In this environment Islam came!
>•
>In this atmosphere the Prophet Muhammad ﷺ appeared.
>
>
>Al-Miqdad ibn Al-Aswad said :
>"By Allah, the Prophet was sent
>peace be upon him between the predatory and the disruptive ones of creation."
>ﷺ
>
>
>
>And look at the saying of Rajâ' Al-'Utâridi in
>that time and the hadith in
>the condition of the Arabs in
>Al-Bukhari: he said "WE USED TO WORSHIP THE STONE, SO WHEN WE FOUND A STONE BETTER THAN IT WE THREW IT AWAY, AND TOOK THE OTHER, SO
>•
>AND THE GROUP WOULD ENTER THE WOMAN, ALL OF THEM HAVING INTERCOURSE WITH HER
>THE TRENCH .
>THE TRENCH .
>the hadith in
>Al-Bukhari
>(206
>)
>
>•
>And the woman was inherited as goods were inherited, and some foods were forbidden for women to eat
>and men only specialized in eating them: Quranic verse
>ﭐﱡﭐ ﱝ ﱞ ﱟ ﱠ ﱡ ﱢ ﱣ ﱤ
>ﱥ ﱦ ﱠﱧﱨ
>﴿
>193
> .﴾ Surah Al-An'am
>
>
>When Umar ibn Al-Khattab
>said in the hadith agreed upon its authenticity
>may Allah be pleased with him: "BY ALLAH, WE WERE IN THE JAHILIYYAH, WE DID NOT CONSIDER WOMEN A MATTER, UNTIL ALLAH REVEALED
>❑
>
>In this pitch-black world came the light of Islam, and Allah sent down His Book; to correct all this
>!corruption, oppression, and immorality
>
>      
>
>(204) Sahih
>Ibn Hibban 6552
>.
>(205) Sahih
>Bukhari 4376
>.
>(206) Sahih
>Bukhari 5127
>.
>(207) Sahih
>Bukhari 4913
>.

>[!summary] Kurdish Text
>
>
>و ھەیە دەکۆن منداڵەکانیان بە ھێزی نان و تەرسی مێشک، و ھەندێک لێیان بەھا دەبێنێت ئەگەر ژمارەی
>منداڵەکانیان دا ھەتاوە دەھێنێت، وەکو رویداوە لەگەڵ عەبدوڵمەتلەب باوکی باوکی نێب
>ﷺ .
>
>•
>لەم کەلتوورەدا ئیسلام ھات!
>•
>لەم کەلتوورەدا پێغەمبەر محەمەد ﷺ دەرکەوتووە.
>
>
>مەقداد بن ئەسوەد وتووە:
>"و خوا، پێغەمبەر
>ﷺ نێردرا بۆ
>نێوان خراپ و چالاکی دەرکەوتووە."
>ﷺ
>
>
>
>و چاوەڕوانی قسەی رەجای عوتەری لە
>و قسە لە کاتی
>دۆخی عەرەب فن
>بوخاری: وت "ئێمە کەو بەختیاری ھەن، بۆوەی کەو بەشوێنێکی باشتر دۆزینەوە ئەمە داھێنین، و ئەوەی دیکە گیرین، بۆیە
>•
>و گرووپێک دەچنە ناو ژن، ھەموویان دەخەونەوە
>خەندق .
>خەندق .
>قسە لە
>بوخاری
>(206
>)
>
>•
>، و ژن وەک شتێک میراسی بێت، و چەند خواردنەکە ھەر بۆ پیاوان ھەبوو
>ئایەتی قورئان
>ﭐﱡﭐ ﱝ ﱞ ﱟ ﱠ ﱡ ﱢ ﱣ ﱤ
>ﱥ ﱦ ﱠﱧﱨ
>﴿
>193
> .﴾ سوورەی ئینعام
>
>
>کاتێک عومەر بن خەتەب
>وت لە قسەی سەحیحدا
>خوا ڕەحمەتی لێی بێت: "و خوا، ئێمە لە جاهیلیا دەبووین شتێک بۆ ژنان نەناسن، ھەتا خوا دەرکەوت
>❑
>
>لەم جیهانە تاریدا نوری ئیسلام ھات، و خوا کتێبی خۆی نەزیر کرد؛ بۆ چارەسەرکردنی ھەموو ئەم
>!بەساد و زوور و فاجۆر
>
>      
>
>(204) سەحیح
>ئبن حەببانی 6552
>.
>(205) سەحیح
>بوخاری 4376
>.
>(206) سەحیح
>بوخاری 5127
>.
>(207) سەحیح
>بوخاری 4913
>.

---

```mermaid
flowchart LR
P(پەڕەی 330)
```"""

# Section 17 - Page 331
replacements[
    "§17\n\n>[!summary] Arabic Text\n>\n\n>[!summary] English Text\n>\n\n>[!summary] Kurdish Text\n>\n\n---\n\n```mermaid\nflowchart LR\nP(پەڕەی 331)\n```"
] = """§17

>[!summary] Arabic Text
>
>
>قال ربنا سبحانه : ﱡﭐ ﲡ ﲢ ﲣ ﲤ ﲥ ﲦ ﲧﲨ ﲩ ﲪ ﲫ ﲬ ﲭ
>ﲮ ﲯﲰ ﲱ ﲲ ﲳ ﲴ
>ﲵ ﲶ ﲷ ﲸﲹ ﲺ ﲻ
>ﲼ ﲽ ﲾ ﲿ ﳀ ﳁﳂ ﳃ ﳄ ﳅ ﳆ ﳇ ﳈ ﳉ ﳊ
>ﳌ ﳍ
>ﳎ ﳏ ﳐ ﳑ ﱁ ﱂ ﱃ ﱄ ﱅ ﱆ ﱇ ﱈ ﱉ ﱊ ﱋﱌ ﱍ ﱎ
>ﱏ ﱐﱑ ﱒ ﱓ ﱔ ﱕ
>ﱖﱗ ﱘ ﱙ ﱚ ﱛ ﱜ ﱝ ﱞﱟ ﱠ
>سورة
>الأعراف
>!عشر وصايا جمعت خصال الخير
>
>
>وقال سبحانه: ﱡﭐ ..ﱳ ﱴ ﱵ ﱶ ﱷ ﱠ
>﴿٣٣ .﴾ سورة النور
>
>
>وقال عز من قائل: ﱡﭐ
>ﲈ
>ﲉ
>ﲊ
>ﲋ ﲌﲍ ﱠ
>﴿
>228
> .﴾ سورة البقرة
>
>
>وقال: ﱡﭐ
>ﱁ
>ﱂ
>ﱃ ﱄ ﱅ
>ﱆ
>ﱇ
>ﱈ ﱉ
>ﱊ
>ﱋ
>ﱌ
>ﱍ ﱎ
>ﱏ ﱐ ﱑﱒ
>ﱓ
>ﱔ ﱠ
>﴿
>7
> .﴾ سورة النساء
>!للمرأة نصيب من التركة، وللرجل نصيب من التركة
>
>
>وقال تعاىل: ﱡﭐ
>ﲒ
>ﲓ
>ﲔ
>ﲕ
>ﲖ
>ﲗ
>ﲘ
>ﲙ
>ﲚ ﲛ
>ﲜ
>ﲝ
>ﲞ
>ﲟ
>ﲠ
>ﲡ
>ﲢ
>ﲣ
>ﲤ
>ﲥ
>ﲦ
>ﲧ
>ﲨ
>ﲩ
>ﲪ
>ﲫ
>ﲬ
>ﲭ
>ﲮ
>ﲯ ﱠ
>﴿٥٣ .﴾ سورة الأحزاب
>
>
>وقال
>ﷺ :
>"إنما النساء شقائقُ
>
>(208)
>سنن أبي دا:ود، ح236
>.
>
>      

>[!summary] English Text
>
>
>Our Lord the Exalted said: Quranic verses
>ﱡﭐ ﲡ ﲢ ﲣ ﲤ ﲥ ﲦ ﲧﲨ ﲩ ﲪ ﲫ ﲬ ﲭ
>ﲮ ﲯﲰ ﲱ ﲲ ﲳ ﲴ
>ﲵ ﲶ ﲷ ﲸﲹ ﲺ ﲻ
>ﲼ ﲽ ﲾ ﲿ ﳀ ﳁﳂ ﳃ ﳄ ﳅ ﳆ ﳇ ﳈ ﳉ ﳊ
>ﳌ ﳍ
>ﳎ ﳏ ﳐ ﳑ ﱁ ﱂ ﱃ ﱄ ﱅ ﱆ ﱇ ﱈ ﱉ ﱊ ﱋﱌ ﱍ ﱎ
>ﱏ ﱐﱑ ﱒ ﱓ ﱔ ﱕ
>ﱖﱗ ﱘ ﱙ ﱚ ﱛ ﱜ ﱝ ﱞﱟ ﱠ
>Surah
>Al-A'raf
>!Ten commandments gathered the qualities of goodness
>
>
>And the Exalted said: Quranic verse
>ﱡﭐ ..ﱳ ﱴ ﱵ ﱶ ﱷ ﱠ
>﴿33 .﴾ Surah An-Nur
>
>
>And the Mighty said from the Speaker: Quranic verse
>ﱡﭐ
>ﲈ
>ﲉ
>ﲊ
>ﲋ ﲌﲍ ﱠ
>﴿
>228
> .﴾ Surah Al-Baqarah
>
>
>And He said: Quranic verse
>ﱡﭐ
>ﱁ
>ﱂ
>ﱃ ﱄ ﱅ
>ﱆ
>ﱇ
>ﱈ ﱉ
>ﱊ
>ﱋ
>ﱌ
>ﱍ ﱎ
>ﱏ ﱐ ﱑﱒ
>ﱓ
>ﱔ ﱠ
>﴿
>7
> .﴾ Surah An-Nisa
>!For women is a share of inheritance, and for men is a share of inheritance
>
>
>And the Exalted said: Quranic verse
>ﱡﭐ
>ﲒ
>ﲓ
>ﲔ
>ﲕ
>ﲖ
>ﲗ
>ﲘ
>ﲙ
>ﲚ ﲛ
>ﲜ
>ﲝ
>ﲞ
>ﲟ
>ﲠ
>ﲡ
>ﲢ
>ﲣ
>ﲤ
>ﲥ
>ﲦ
>ﲧ
>ﲨ
>ﲩ
>ﲪ
>ﲫ
>ﲬ
>ﲭ
>ﲮ
>ﲯ ﱠ
>﴿53 .﴾ Surah Al-Ahzab
>
>
>And the Prophet
>ﷺ said:
>"Women are the sisters of
>
>(208)
>Sunan Abi Dawood, 236
>.

>[!summary] Kurdish Text
>
>
>راوەشمان گەورە وت: ئایەتی قورئان
>ﱡﭐ ﲡ ﲢ ﲣ ﲤ ﲥ ﲦ ﲧﲨ ﲩ ﲪ ﲫ ﲬ ﲭ
>ﲮ ﲯﲰ ﲱ ﲲ ﲳ ﲴ
>ﲵ ﲶ ﲷ ﲸﲹ ﲺ ﲻ
>ﲼ ﲽ ﲾ ﲿ ﳀ ﳁﳂ ﳃ ﳄ ﳅ ﳆ ﳇ ﳈ ﳉ ﳊ
>ﳌ ﳍ
>ﳎ ﳏ ﳐ ﳑ ﱁ ﱂ ﱃ ﱄ ﱅ ﱆ ﱇ ﱈ ﱉ ﱊ ﱋﱌ ﱍ ﱎ
>ﱏ ﱐﱑ ﱒ ﱓ ﱔ ﱕ
>ﱖﱗ ﱘ ﱙ ﱚ ﱛ ﱜ ﱝ ﱞﱟ ﱠ
>سوورەی ئەعراف
>!دەھ قسەیەک دەھێنێت خۆشین دەھێنێت
>
>
>و گەورە وت: ئایەتی قورئان
>ﱡﭐ ..ﱳ ﱴ ﱵ ﱶ ﱷ ﱠ
>﴿٣٣ .﴾ سوورەی نۆر
>
>
>و گەورە وت: ئایەتی قورئان
>ﱡﭐ
>ﲈ
>ﲉ
>ﲊ
>ﲋ ﲌﲍ ﱠ
>﴿
>228
> .﴾ سوورەی بەقەرە
>
>
>و وت: ئایەتی قورئان
>ﱡﭐ
>ﱁ
>ﱂ
>ﱃ ﱄ ﱅ
>ﱆ
>ﱇ
>ﱈ ﱉ
>ﱊ
>ﱋ
>ﱌ
>ﱍ ﱎ
>ﱏ ﱐ ﱑﱒ
>ﱓ
>ﱔ ﱠ
>﴿
>7
> .﴾ سوورەی نێسا
>!بۆ ژن بەشێک لە میراسە، و بۆ مێرد بەشێک
>
>
>و وت
>ﷺ :
>"نێوان ژن و مێرد پێشەوە بەشەوە
>
>(208)
>سەنەنی ئەبی داود، ٢٣٦
>.

---

```mermaid
flowchart LR
P(پەڕەی 331)
```"""

# Section 18 - Page 332
replacements[
    "§18\n\n>[!summary] Arabic Text\n>\n\n>[!summary] English Text\n>\n\n>[!summary] Kurdish Text\n>\n\n---\n\n```mermaid\nflowchart LR\nP(پەڕەی 332)\n```"
] = """§18

>[!summary] Arabic Text
>
>
>وكانت اليتيمة تُورَ ث بمالها لمن يُربيها، ويتركون وجُها الرجل ولا يدفع لها مهراً؛ لأنها
>يتيمة، فتنزل قوله تعاىل: ﱡﭐ
>ﱴ
>ﱵ
>ﱶ
>ﱷ ﱸ
>ﱹ
>ﱺ ﱻ
>ﱼ
>ﱽ
>ﱾ
>ﱿ
>ﲀ
>ﲁ ﲂﲃ ﲄ
>ﲅ ﲆ
>ﲇ
>ﲈ ..ﱠ
>﴿٣ ﴾
> .سورة النساء
>
>
>:ًَل تُقْ سِ طُوا فِي الْيَتَامَ فَانْكِحُوا مَا طَابَ لَكُمْ مِنَ النِّسَاءِ مَثْنَى وَ ثُلَثَ وَ رُبَاع
>
>وَ إِنْ خِفْتُمْ أ
>إن خفت أن تظلم هذه اليتيمة ولا تعطيه حق ها، فانكح غير ها كما تحب ، مثنى وثلاث
>ورباع، واترك هذه لمن يعطيها حقها كاملاً ... اتركها لمن يُكرمها
>
>
>جاء الإسلام بإصلاح عقيدة الناس، وبإصلاح سلوكهم وأخلاقهم
>ومعاملاتهم ... جاء بإكرام المرأة واليتيم والطفل، بل وحِفظ حقوق الدواب
>والشجر... الإسلام جاء بإصلاح العالم بما فيه
>
>
>استمِعْ لما قال جعفر بن أبي طالب الصحابي الجليل حين تكلَّم بين يدي ري
>النجاشي
>ملك
>الحبشة، وهو يصف له الإسلام ويختصر لماذا ضحوا كل هذه التضحيات من أجل هذا
>الدين، ولماذا تركوا الأهل والبلد وهاجروا في الله، قال جعفر:ن ي هللا عنه
>رص "أيُّها الملِكُ، كُنَّا قَومًا أهلَ جاهليَّةٍ، نَعبُدُ الأصنامَ، وَنَأكُلُ المَيْتَةَ، وَنَأتي
>فصدَّقْناه وآمَنَّا
>
>!بهذا جاء الإسلام... وبهذا ساد الإسلام
>
>
>وقد أختر الله عز وجل بنصرة نبيه، وكان العرب يسخرون حين يسمعون أن هذا الرجل
>سيبطل الباطل في شرق
>الأرض
>وغرب ها، فجاء الإسلامُ وفتح الله للمسلمين
>مشارق الأرض ومغاربها
>ممالك الأرض، وسادت كلمة التوحيد
>.فلم يطرق العالم ناموس أفضل ولا أعظم من هذا الناموس
>
>      
>
>(209)
>مسند أحمد، ح1740، بسند صحيح .

>[!summary] English Text
>
>
>And the orphan girl was inherited with her wealth by whoever raised her, and the man would marry her without giving her a dowry; because she is
>an orphan, so the Exalted's words descended: Quranic verse
>ﱡﭐ
>ﱴ
>ﱵ
>ﱶ
>ﱷ ﱸ
>ﱹ
>ﱺ ﱻ
>ﱼ
>ﱽ
>ﱾ
>ﱿ
>ﲀ
>ﲁ ﲂﲃ ﲄ
>ﲅ ﲆ
>ﲇ
>ﲈ ..ﱠ
>﴿3 ﴾
>Surah An-Nisa
>
>
>:Do not approach the orphans' wealth, so marry what pleases you from the women, two, three, and four
>
>And if you fear that
>you will wrong this orphan and not give her her full right, then marry others besides her, two, three
>and four, and leave this one to whoever gives her her full right ... leave her to whoever honors her
>
>
>Islam came to rectify people's beliefs, and to rectify their behavior and morals
>and their transactions ... It came to honor the woman, the orphan, and the child, and even to preserve the rights of animals
>and trees... Islam came to rectify the world in all that it contains
>
>
>Listen to what Ja'far ibn Abi Talib the noble companion said when he spoke before
>Al-Najashi
>the King
>of Abyssinia, as he described Islam to him and summarized why they sacrificed all these sacrifices for the sake of this
>religion, and why they left their families and country and migrated in the cause of Allah, Ja'far said: may Allah be pleased with him
>"O King, we were a people of Jahiliyyah, we worshipped idols, we ate dead meat, and we committed
>adultery, so the Messenger of Allah
>ﷺ
>came to us... and we believed in him
>and followed him.
>
>!It was by this that Islam came... and by this Islam prevailed
>
>
>And Allah the Exalted granted victory to His Prophet, and the Arabs mocked when they heard that this man
>will conquer the East of
>the earth
>and its West, so Islam came and Allah opened for the Muslims
>the East of the earth and its West
>kingdoms of the earth, and the word of monotheism prevailed
>.No law has touched the world better or greater than this law
>
>      
>
>(209)
>Musnad Ahmad, 1740, with authentic chain .

>[!summary] Kurdish Text
>
>
>و کچە باوەکەبێت مێرێتەوە بە پارەکەی بە کەسێک کە دەربەخشی، و مێرد دەھاوسەرگیری دەکات بێ مێھەر؛ بۆوەی
>مێنڈەکە بێ باوەکە، بۆیە قسەی گەورە دەرکەوتووە: ئایەتی قورئان
>ﱡﭐ
>ﱴ
>ﱵ
>ﱶ
>ﱷ ﱸ
>ﱹ
>ﱺ ﱻ
>ﱼ
>ﱽ
>ﱾ
>ﱿ
>ﲀ
>ﲁ ﲂﲃ ﲄ
>ﲅ ﲆ
>ﲇ
>ﲈ ..ﱠ
>﴿3 ﴾
> .سورة النسا
>
>
>:نەدەسین بۆ باوەکی کەم، بۆیە ھەوڵدەر بکە بەو شتەوە کە تو دەوێیت، ھەوڵبژاردن و سێ و چوار، و جێگەرەوە ئەمە لە کەسێک کە ھەوای تەواو دەدات بۆی ... جێگیرەوە بۆ کەسێک کە پارێزگارە
>
>
>ئیسلام ھات بۆ چارەسەرکردنی باوەڕەکانی خەڵک، و چارەسەرکردنی جەنگاوە و ڕەوەش و ھەولەیان
>و کاروبارەکانیان ... ھات بە پارێزکردنی ژن و مێنڈە باوەکە و منداڵ، بەھێز پارێزکردنی مافەکانی دەرەوە
>و دار... ئیسلام ھات بۆ چارەسەرکردنی جیهان بە تەواوی
>
>
>گوێگرە بۆ چی جەعفەر بن ئەبی طالب ھاوبەشی سەرهەڵبەردار وتووە کاتێک قسەی کرد لەبەر
>نەجاشی
>پاشا
>ئەبەسی، کە وتووە ئیسلام وەشاند و وتووە بۆ چی ھەموو ئەم قوربانییە دان بۆ ئەم
>دینە، و بۆ چی خێڵیان و وڵاتیان جێگیر کرد بۆ خوا، وت جەعفەر:ن ی خوا بێت لێی
>"ئی مێلک، ئێمە خەڵکێکین لە جاهیلیا، دەپرێستین بۆت، و مێرگ دەخۆین، و دەچینە
>، بەوە پێغەمبەر خوا
>ﷺ
>هات بە ناو ئێمە... و ئێمە باوەڕمان کرد و پێی ھەوڵدەرمان بەسەر
>!بەوەیە ئیسلام ھات... و بەوەیە سەرەکی بوو
>
>
>و خوا گەورە یارمەتیی پێغەمبەر کرد، و کورد بە خەندەک دەکەن کاتێک دەگەیشن کە ئەم مێرد
>پێشەوەی شاری مەککە
>سەنتەر بووە، دەخاتە ناو شاری مەککە، پاشان ئیسلام دەرکەوتووە و خوا کردنەوە بۆ موسڵمانان
>مشارق زەوی و مەغرەبە
>مێلەتە زەوی، و ناوی تەوحید سەرەوە بوو
>.بۆیە جیهان نامۆسێکی باشتر و گەورەتر نەبووە لەم نامۆسە
>
>      
>
>(209)
>مەسند ئەحمەد، 1740، بە سندە دروست .

---

```mermaid
flowchart LR
P(پەڕەی 332)
```"""

# Section 19 - Page 333
replacements[
    "§19\n\n>[!summary] Arabic Text\n>\n\n>[!summary] English Text\n>\n\n>[!summary] Kurdish Text\n>\n\n---\n\n```mermaid\nflowchart LR\nP(پەڕەی 333)\n```"
] = """§19

>[!summary] Arabic Text
>
>
>قال ربنا سبحانه : ﱡﭐ ﲡ ﲢ ﲣ ﲤ ﲥ ﲦ ﲧﲨ ﲩ ﲪ ﲫ ﲬ ﲭ
>ﲮ ﲯﲰ ﲱ ﲲ ﲳ ﲴ
>ﲵ ﲶ ﲷ ﲸﲹ ﲺ ﲻ
>ﲼ ﲽ ﲾ ﲿ ﳀ ﳁﳂ ﳃ ﳄ ﳅ ﳆ ﳇ ﳈ ﳉ ﳊ
>ﳌ ﳍ
>ﳎ ﳏ ﳐ ﳑ ﱁ ﱂ ﱃ ﱄ ﱅ ﱆ ﱇ ﱈ ﱉ ﱊ ﱋﱌ ﱍ ﱎ
>ﱏ ﱐﱑ ﱒ ﱓ ﱔ ﱕ
>ﱖﱗ ﱘ ﱙ ﱚ ﱛ ﱜ ﱝ ﱞﱟ ﱠ
>سورة
>الأعراف
>!عشر وصايا جمعت خصال الخير
>
>
>وقال سبحانه: ﱡﭐ ..ﱳ ﱴ ﱵ ﱶ ﱷ ﱠ
>﴿٣٣ .﴾ سورة النور
>
>
>وقال عز من قائل: ﱡﭐ
>ﲈ
>ﲉ
>ﲊ
>ﲋ ﲌﲍ ﱠ
>﴿
>228
> .﴾ سورة البقرة
>
>
>وقال: ﱡﭐ
>ﱁ
>ﱂ
>ﱃ ﱄ ﱅ
>ﱆ
>ﱇ
>ﱈ ﱉ
>ﱊ
>ﱋ
>ﱌ
>ﱍ ﱎ
>ﱏ ﱐ ﱑﱒ
>ﱓ
>ﱔ ﱠ
>﴿
>7
> .﴾ سورة النساء
>!للمرأة نصيب من التركة، وللرجل نصيب من التركة
>
>
>وقال تعاىل: ﱡﭐ
>ﲒ
>ﲓ
>ﲔ
>ﲕ
>ﲖ
>ﲗ
>ﲘ
>ﲙ
>ﲚ ﲛ
>ﲜ
>ﲝ
>ﲞ
>ﲟ
>ﲠ
>ﲡ
>ﲢ
>ﲣ
>ﲤ
>ﲥ
>ﲦ
>ﲧ
>ﲨ
>ﲩ
>ﲪ
>ﲫ
>ﲬ
>ﲭ
>ﲮ
>ﲯ ﱠ
>﴿٥٣ .﴾ سورة الأحزاب
>
>
>وقال
>ﷺ :
>"إنما النساء شقائقُ
>
>(208)
>سنن أبي دا:ود، ح236
>.

>[!summary] English Text
>
>
>Our Lord the Exalted said: Quranic verses
>ﱡﭐ ﲡ ﲢ ﲣ ﲤ ﲥ ﲦ ﲧﲨ ﲩ ﲪ ﲫ ﲬ ﲭ
>ﲮ ﲯﲰ ﲱ ﲲ ﲳ ﲴ
>ﲵ ﲶ ﲷ ﲸﲹ ﲺ ﲻ
>ﲼ ﲽ ﲾ ﲿ ﳀ ﳁﳂ ﳃ ﳄ ﳅ ﳆ ﳇ ﳈ ﳉ ﳊ
>ﳌ ﳍ
>ﳎ ﳏ ﳐ ﳑ ﱁ ﱂ ﱃ ﱄ ﱅ ﱆ ﱇ ﱈ ﱉ ﱊ ﱋﱌ ﱍ ﱎ
>ﱏ ﱐﱑ ﱒ ﱓ ﱔ ﱕ
>ﱖﱗ ﱘ ﱙ ﱚ ﱛ ﱜ ﱝ ﱞﱟ ﱠ
>Surah
>Al-A'raf
>!Ten commandments gathered the qualities of goodness
>
>
>And the Exalted said: Quranic verse
>ﱡﭐ ..ﱳ ﱴ ﱵ ﱶ ﱷ ﱠ
>﴿33 .﴾ Surah An-Nur
>
>
>And the Mighty said from the Speaker: Quranic verse
>ﱡﭐ
>ﲈ
>ﲉ
>ﲊ
>ﲋ ﲌﲍ ﱠ
>﴿
>228
> .﴾ Surah Al-Baqarah
>
>
>And He said: Quranic verse
>ﱡﭐ
>ﱁ
>ﱂ
>ﱃ ﱄ ﱅ
>ﱆ
>ﱇ
>ﱈ ﱉ
>ﱊ
>ﱋ
>ﱌ
>ﱍ ﱎ
>ﱏ ﱐ ﱑ ﱒ
>ﱓ
>ﱔ ﱠ
>﴿
>7
> .﴾ Surah An-Nisa
>!For women is a share of inheritance, and for men is a share of inheritance
>
>
>And the Exalted said: Quranic verse
>ﱡﭐ
>ﲒ
>ﲓ
>ﲔ
>ﲕ
>ﲖ
>ﲗ
>ﲘ
>ﲙ
>ﲚ ﲛ
>ﲜ
>ﲝ
>ﲞ
>ﲟ
>ﲠ
>ﲡ
>ﲢ
>ﲣ
>ﲤ
>ﲥ
>ﲦ
>ﲧ
>ﲨ
>ﲩ
>ﲪ
>ﲫ
>ﲬ
>ﲭ
>ﲮ
>ﲯ ﱠ
>﴿53 .﴾ Surah Al-Ahzab
>
>
>And the Prophet
>ﷺ said:
>"Women are the sisters of
>
>(208)
>Sunan Abi Dawood, 236
>.

>[!summary] Kurdish Text
>
>
>راوەشمان گەورە وت: ئایەتی قورئان
>ﱡﭐ ﲡ ﲢ ﲣ ﲤ ﲥ ﲦ ﲧﲨ ﲩ ﲪ ﲫ ﲬ ﲭ
>ﲮ ﲯﲰ ﲱ ﲲ ﲳ ﲴ
>ﲵ ﲶ ﲷ ﲸﲹ ﲺ ﲻ
>ﲼ ﲽ ﲾ ﲿ ﳀ ﳁﳂ ﳃ ﳄ ﳅ ﳆ ﳇ ﳈ ﳉ ﳊ
>ﳌ ﳍ
>ﳎ ﳏ ﳐ ﳑ ﱁ ﱂ ﱃ ﱄ ﱅ ﱆ ﱇ ﱈ ﱉ ﱊ ﱋﱌ ﱍ ﱎ
>ﱏ ﱐﱑ ﱒ ﱓ ﱔ ﱕ
>ﱖﱗ ﱘ ﱙ ﱚ ﱛ ﱜ ﱝ ﱞﱟ ﱠ
>سوورەی ئەعراف
>!دەھ قسەیەک دەھێنێت خۆشین دەھێنێت
>
>
>و گەورە وت: ئایەتی قورئان
>ﱡﭐ ..ﱳ ﱴ ﱵ ﱶ ﱷ ﱠ
>﴿٣٣ .﴾ سوورەی نۆر
>
>
>و گەورە وت: ئایەتی قورئان
>ﱡﭐ
>ﲈ
>ﲉ
>ﲊ
>ﲋ ﲌﲍ ﱠ
>﴿
>228
> .﴾ سوورەی بەقەرە
>
>
>و وت: ئایەتی قورئان
>ﱡﭐ
>ﱁ
>ﱂ
>ﱃ ﱄ ﱅ
>ﱆ
>ﱇ
>ﱈ ﱉ
>ﱊ
>ﱋ
>ﱌ
>ﱍ ﱎ
>ﱏ ﱐ ﱑ ﱒ
>ﱓ
>ﱔ ﱠ
>﴿
>7
> .﴾ سوورەی نێسا
>!بۆ ژن بەشێک لە میراسە، و بۆ مێرد بەشێک
>
>
>و وت
>ﷺ :
>"نێوان ژن و مێرد پێشەوە بەشەوە
>
>(208)
>سەنەنی ئەبی داود، ٢٣٦
>.

---

```mermaid
flowchart LR
P(پەڕەی 333)
```"""

# Section 20 - Page 334
replacements[
    "§20\n\n>[!summary] Arabic Text\n>\n\n>[!summary] English Text\n>\n\n>[!summary] Kurdish Text\n>\n\n---\n\n```mermaid\nflowchart LR\nP(پەڕەی 334)\n```"
] = """§20

>[!summary] Arabic Text
>
>
>وكانت اليتيمة تُورث بمالها لمن يُربيها، ويتركون وجُها الرجل ولا يدفع لها مهراً؛ لأنها
>يتيمة، فتنزل قوله تعاىل: ﱡﭐ
>ﱴ
>ﱵ
>ﱶ
>ﱷ ﱸ
>ﱹ
>ﱺ ﱻ
>ﱼ
>ﱽ
>ﱾ
>ﱿ
>ﲀ
>ﲁ ﲂﲃ ﲄ
>ﲅ ﲆ
>ﲇ
>ﲈ ..ﱠ
>﴿3 ﴾
>.سورة النساء
>
>
>:ًَل تُقْ سِ طُوا فِي الْيَتَامَ فَانْكِحُوا مَا طَابَ لَكُمْ مِنْ النِّسَاءِ مَثْنَى وَ ثُلَثَ وَ رُبَاع
>
>وَ إِنْ خِفْتُمْ أ
>إن خفت أن تظلم هذه اليتيمة ولا تعطيه حق ها، فانكح غير ها كما تحب ، مثنى وثلاث
>ورباع، واترك هذه لمن يعطيها حقها كاملاً ... اتركها لمن يُكرمها
>
>
>جاء الإسلام بإصلاح عقيدة الناس، وبإصلاح سلوكهم وأخلاقهم
>ومعاملاتهم ... جاء بإكرام المرأة واليتيم والطفل، بل وحِفظ حقوق الدواب
>والشجر... الإسلام جاء بإصلاح العالم بما فيه
>
>
>استمِعْ لما قال جعفر بن أبي طالب الصحابي الجليل حين تكلَّم بين يدي ري
>النجاشي
>ملك
>الحبشة، وهو يصف له الإسلام ويختصر لماذا ضحوا كل هذه التضحيات من أجل هذا
>الدين، ولماذا تركوا الأهل والبلد وهاجروا في الله، قال جعفر:ن ي هللا عنه
>رص "أيُّها الملِكُ، كُنَّا قَومًا أهلَ جاهليَّةٍ، نَعبُدُ الأصنامَ، وَنَأكُلُ المَيْتَةَ، وَنَأتي
>، فصدَّقْناه وآمَنَّا
>
>!بهذا جاء الإسلام... وبهذا ساد الإسلام
>
>
>وقد أختر الله عز وجل بنصرة نبيه، وكان العرب يسخرون حين يسمعون أن هذا الرجل
>سيبطل الباطل في شرق
>الأرض
>وغربها، فجاء الإسلامُ وفتح الله للمسلمين
>مشارق الأرض ومغاربها
>ممالك الأرض، وسادت كلمة التوحيد
>.فلم يطرق العالم ناموس أفضل ولا أعظم من هذا الناموس
>
>      
>
>(209)
>مسند أحمد، ح1740، بسند صحيح .

>[!summary] English Text
>
>
>And the orphan girl was inherited with her wealth by whoever raised her, and the man would marry her without giving her a dowry; because she is
>an orphan, so the Exalted's words descended: Quranic verse
>ﱡﭐ
>ﱴ
>ﱵ
>ﱶ
>ﱷ ﱸ
>ﱹ
>ﱺ ﱻ
>ﱼ
>ﱽ
>ﱾ
>ﱿ
>ﲀ
>ﲁ ﲂﲃ ﲄ
>ﲅ ﲆ
>ﲇ
>ﲈ ..ﱠ
>﴿3 ﴾
>Surah An-Nisa
>
>
>:Do not approach the orphans' wealth, so marry what pleases you from the women, two, three, and four
>
>And if you fear that
>you will wrong this orphan and not give her her full right, then marry others besides her, two, three
>and four, and leave this one to whoever gives her her full right ... leave her to whoever honors her
>
>
>Islam came to rectify people's beliefs, and to rectify their behavior and morals
>and their transactions ... It came to honor the woman, the orphan, and the child, and even to preserve the rights of animals
>and trees... Islam came to rectify the world in all that it contains
>
>
>Listen to what Ja'far ibn Abi Talib the noble companion said when he spoke before
>Al-Najashi
>the King
>of Abyssinia, as he described Islam to him and summarized why they sacrificed all these sacrifices for the sake of this
>religion, and why they left their families and country and migrated in the cause of Allah, Ja'far said: may Allah be pleased with him
>"O King, we were a people of Jahiliyyah, we worshipped idols, we ate dead meat, and we committed
>adultery, so the Messenger of Allah
>ﷺ
>came to us... and we believed in him
>and followed him.
>
>!It was by this that Islam came... and by this Islam prevailed
>
>
>And Allah the Exalted granted victory to His Prophet, and the Arabs mocked when they heard that this man
>will conquer the East of
>the earth
>and its West, so Islam came and Allah opened for the Muslims
>the East of the earth and its West
>kingdoms of the earth, and the word of monotheism prevailed
>.No law has touched the world better or greater than this law
>
>      
>
>(209)
>Musnad Ahmad, 1740, with authentic chain .

>[!summary] Kurdish Text
>
>
>و کچە باوەکەبێت مێرێتەوە بە پارەکەی بە کەسێک کە دەربەخشی، و مێرد دەھاوسەرگیری دەکات بێ مێھەر؛ بۆوەی
>مێنڈەکە بێ باوەکە، بۆیە قسەی گەورە دەرکەوتووە: ئایەتی قورئان
>ﱡﭐ
>ﱴ
>ﱵ
>ﱶ
>ﱷ ﱸ
>ﱹ
>ﱺ ﱻ
>ﱼ
>ﱽ
>ﱾ
>ﱿ
>ﲀ
>ﲁ ﲂﲃ ﲄ
>ﲅ ﲆ
>ﲇ
>ﲈ ..ﱠ
>﴿3 ﴾
> .سورة النسا
>
>
>:نەدەسین بۆ باوەکەبێت، بۆیە ھەوڵدەر بکە بەو شتەوە کە تو دەوێیت، ھەوڵبژاردن و سێ و چوار، و جێگەرەوە ئەمە لە کەسێک کە ھەوای تەواو دەدات بۆی ... جێگیرەوە بۆ کەسێک کە پارێزگارە
>
>
>ئیسلام ھات بۆ چارەسەرکردنی باوەڕەکانی خەڵک، و چارەسەرکردنی جەنگاوە و ڕەوەش و ھەولەیان
>و کاروبارەکانیان ... ھات بە پارێزکردنی ژن و مێنڈە باوەکە و منداڵ، بەھێز پارێزکردنی مافەکانی دەرەوە
>و دار... ئیسلام ھات بۆ چارەسەرکردنی جیهان بە تەواوی
>
>
>گوێگرە بۆ چی جەعفەر بن ئەبی طالب ھاوبەشی سەرهەڵبەردار وتووە کاتێک قسەی کرد لەبەر
>نەجاشی
>پاشا
>ئەبەسی، کە وتووە ئیسلام وەشاند و وتووە بۆ چی ھەموو ئەم قوربانییە دان بۆ ئەم
>دینە، وچی تێکەڵکردنەوەیان لێیان خوێن، وت جەعفەر:ن ی خوا بێت لێی
>"ئی مێلک، ئێمە خەڵکێکین لە جاهیلیا، دەپرێستین بۆت، و مێرە دەخۆین، و نەچین
>، فصدەقین و باوەڕمان کرد و پێی ھەوڵدەرمان بەسەر
>!بەوەیە ئیسلام ھات... و بەوەیە سەرەکی بوو
>
>
>و خوا گەورە یارمەتیی پێغەمبەر کرد، و کورد بە خەندەک دەکەن کاتێک دەگەیشن کە ئەم مێرد
>پێشەوەی شاری مەککە
>سەنتەر بووە، دەخاتە ناو شاری مەککە، پاشان ئیسلام دەرکەوتووە و خوا کردنەوە بۆ موسڵمانان
>مشارق زەوی و مەغرەبە
>مێلەتە زەوی، و ناوی تەوحید سەرەوە بوو
>.فلم يطرق العالم ناموس أفضل ولا أعظم من هذا الناموس
>
>      
>
>(209)
>مەسند ئەحمەد، 1740، بە سندە دروست .

---

```mermaid
flowchart LR
P(پەڕەی 334)
```"""

# Section 21 - Page 335
replacements[
    "§21\n\n>[!summary] Arabic Text\n>\n\n>[!summary] English Text\n>\n\n>[!summary] Kurdish Text\n>\n\n---\n\n```mermaid\nflowchart LR\nP(پەڕەی 335)\n```"
] = """§21

>[!summary] Arabic Text
>
>
>قال ربنا سبحانه : ﱡﭐ ﲡ ﲢ ﲣ ﲤ ﲥ ﲦ ﲧﲨ ﲩ ﲪ ﲫ ﲬ ﲭ
>ﲮ ﲯﲰ ﲱ ﲲ ﲳ ﲴ
>ﲵ ﲶ ﲷ ﲸﲹ ﲺ ﲻ
>ﲼ ﲽ ﲾ ﲿ ﳀ ﳁﳂ ﳃ ﳄ ﳅ ﳆ ﳇ ﳈ ﳉ ﳊ
>ﳌ ﳍ
>ﳎ ﳏ ﳐ ﳑ ﱁ ﱂ ﱃ ﱄ ﱅ ﱆ ﱇ ﱈ ﱉ ﱊ ﱋﱌ ﱍ ﱎ
>ﱏ ﱐﱑ ﱒ ﱓ ﱔ ﱕ
>ﱖﱗ ﱘ ﱙ ﱚ ﱛ ﱜ ﱝ ﱞﱟ ﱠ
>سورة
>الأعراف
>!عشر وصايا جمعت خصال الخير
>
>
>وقال سبحانه: ﱡﭐ ..ﱳ ﱴ ﱵ ﱶ ﱷ ﱠ
>﴿٣٣ .﴾ سورة النور
>
>
>وقال عز من قائل: ﱡﭐ
>ﲈ
>ﲉ
>ﲊ
>ﲋ ﲌﲍ ﱠ
>﴿
>228
> .﴾ سورة البقرة
>
>
>وقال: ﱡﭐ
>ﱁ
>ﱂ
>ﱃ ﱄ ﱅ
>ﱆ
>ﱇ
>ﱈ ﱉ
>ﱊ
>ﱋ
>ﱌ
>ﱍ ﱎ
>ﱏ ﱐ ﱑﱒ
>ﱓ
>ﱔ ﱠ
>﴿
>7
> .﴾ سورة النساء
>!للمرأة نصيب من التركة، وللرجل نصيب من التركة
>
>
>وقال تعاىل: ﱡﭐ
>ﲒ
>ﲓ
>ﲔ
>ﲕ
>ﲖ
>ﲗ
>ﲘ
>ﲙ
>ﲚ ﲛ
>ﲜ
>ﲝ
>ﲞ
>ﲟ
>ﲠ
>ﲡ
>ﲢ
>ﲣ
>ﲤ
>ﲥ
>ﲦ
>ﲧ
>ﲨ
>ﲩ
>ﲪ
>ﲫ
>ﲬ
>ﲭ
>ﲮ
>ﲯ ﱠ
>﴿٥٣ .﴾ سورة الأحزاب
>
>
>وقال
>ﷺ :
>"إنما النساء شقائقُ
>
>(208)
>سنن أبي دا:ود، ح236
>.

>[!summary] English Text
>
>
>Our Lord the Exalted said: Quranic verses
>ﱡﭐ ﲡ ﲢ ﲣ ﲤ ﲥ ﲦ ﲧﲨ ﲩ ﲪ ﲫ ﲬ ﲭ
>ﲮ ﲯﲰ ﲱ ﲲ ﲳ ﲴ
>ﲵ ﲶ ﲷ ﲸﲹ ﲺ ﲻ
>ﲼ ﲽ ﲾ ﲿ ﳀ ﳁﳂ ﳃ ﳄ ﳅ ﳆ ﳇ ﳈ ﳉ ﳊ
>ﳌ ﳍ
>ﳎ ﳏ ﳐ ﳑ ﱁ ﱂ ﱃ ﱄ ﱅ ﱆ ﱇ ﱈ ﱉ ﱊ ﱋﱌ ﱍ ﱎ
>ﱏ ﱐﱑ ﱒ ﱓ ﱔ ﱕ
>ﱖﱗ ﱘ ﱙ ﱚ ﱛ ﱜ ﱝ ﱞﱟ ﱠ
>Surah
>Al-A'raf
>!Ten commandments gathered the qualities of goodness
>
>
>And the Exalted said: Quranic verse
>ﱡﭐ ..ﱳ ﱴ ﱵ ﱶ ﱷ ﱠ
>﴿33 .﴾ Surah An-Nur
>
>
>And the Mighty said from the Speaker: Quranic verse
>ﱡﭐ
>ﲈ
>ﲉ
>ﲊ
>ﲋ ﲌﲍ ﱠ
>﴿
>228
> .﴾ Surah Al-Baqarah
>
>
>And He said: Quranic verse
>ﱡﭐ
>ﱁ
>ﱂ
>ﱃ ﱄ ﱅ
>ﱆ
>ﱇ
>ﱈ ﱉ
>ﱊ
>ﱋ
>ﱌ
>ﱍ ﱎ
>ﱏ ﱐ ﱑ ﱒ
>ﱓ
>ﱔ ﱠ
>﴿
>7
> .﴾ Surah An-Nisa
>!For women is a share of inheritance, and for men is a share of inheritance
>
>
>And the Exalted said: Quranic verse
>ﱡﭐ
>ﲒ
>ﲓ
>ﲔ
>ﲕ
>ﲖ
>ﲗ
>ﲘ
>ﲙ
>ﲚ ﲛ
>ﲜ
>ﲝ
>ﲞ
>ﲟ
>ﲠ
>ﲡ
>ﲢ
>ﲣ
>ﲤ
>ﲥ
>ﲦ
>ﲧ
>ﲨ
>ﲩ
>ﲪ
>ﲫ
>ﲬ
>ﲭ
>ﲮ
>ﲯ ﱠ
>﴿53 .﴾ Surah Al-Ahzab
>
>
>And the Prophet
>ﷺ said:
>"Women are the sisters of
>
>(208)
>Sunan Abi Dawood, 236
>.

>[!summary] Kurdish Text
>
>
>راوەشمان گەورە وت: ئایەتی قورئان
>ﱡﭐ ﲡ ﲢ ﲣ ﲤ ﲥ ﲦ ﲧﲨ ﲩ ﲪ ﲫ ﲬ ﲭ
>ﲮ ﲯﲰ ﲱ ﲲ ﲳ ﲴ
>ﲵ ﲶ ﲷ ﲸﲹ ﲺ ﲻ
>ﲼ ﲽ ﲾ ﲿ ﳀ ﳁﳂ ﳃ ﳄ ﳅ ﳆ ﳇ ﳈ ﳉ ﳊ
>ﳌ ﳍ
>ﳎ ﳏ ﳐ ﳑ ﱁ ﱂ ﱃ ﱄ ﱅ ﱆ ﱇ ﱈ ﱉ ﱊ ﱋﱌ ﱍ ﱎ
>ﱏ ﱐﱑ ﱒ ﱓ ﱔ ﱕ
>ﱖﱗ ﱘ ﱙ ﱚ ﱛ ﱜ ﱝ ﱞﱟ ﱠ
>سوورەی ئەعراف
>!دەھ قسەیەک دەھێنێت خۆشین دەھێنێت
>
>
>و گەورە وت: ئایەتی قورئان
>ﱡﭐ ..ﱳ ﱴ ﱵ ﱶ ﱷ ﱠ
>﴿33 .﴾ سوورەی نۆر
>
>
>و گەورە وت: ئایەتی قورئان
>ﱡﭐ
>ﲈ
>ﲉ
>ﲊ
>ﲋ ﲌﲍ ﱠ
>﴿
>228
> .﴾ سوورەی بەقەرە
>
>
>و وت: ئایەتی قورئان
>ﱡﭐ
>ﱁ
>ﱂ
>ﱃ ﱄ ﱅ
>ﱆ
>ﱇ
>ﱈ ﱉ
>ﱊ
>ﱋ
>ﱌ
>ﱍ ﱎ
>ﱏ ﱐ ﱑ ﱒ
>ﱓ
>ﱔ ﱠ
>﴿
>7
> .﴾ سوورەی نێسا
>!بۆ ژن بەشێک لە میراسە، و بۆ مێرد بەشێک
>
>
>و وت
>ﷺ :
>"نێوان ژن و مێرد پێشەوە بەشەوە
>
>(208)
>سەنەنی ئەبی داود، ٢٣٦
>.

---

```mermaid
flowchart LR
P(پەڕەی 335)
```"""

# Section 22 - Page 336
replacements[
    "§22\n\n>[!summary] Arabic Text\n>\n\n>[!summary] English Text\n>\n\n>[!summary] Kurdish Text\n>\n\n---\n\n```mermaid\nflowchart LR\nP(پەڕەی 336)\n```"
] = """§22

>[!summary] Arabic Text
>
>
>وكانت اليتيمة تُورث بمالها لمن يُربيها، ويتركون وجُها الرجل ولا يدفع لها مهراً؛ لأنها
>يتيمة، فتنزل قوله تعاىل: ﱡﭐ
>ﱴ
>ﱵ
>ﱶ
>ﱷ ﱸ
>ﱹ
>ﱺ ﱻ
>ﱼ
>ﱽ
>ﱾ
>ﱿ
>ﲀ
>ﲁ ﲂﲃ ﲄ
>ﲅ ﲆ
>ﲇ
>ﲈ ..ﱠ
>﴿3 ﴾
>.سورة النساء
>
>
>:ًَل تُقْ سِ طُوا فِي الْيَتَامَ فَانْكِحُوا مَا طَابَ لَكُمْ مِنَ النِّسَاءِ مَثْنَى وَ ثُلَثَ وَ رُبَاع
>
>وَ إِنْ خِفْتُمْ أ
>إن خفت أن تظلم هذه اليتيمة ولا تعطيه حق ها، فانكح غَيْرَهَا كَمَا تُحِب ، مثنى وثلاث
>ورباع، واترك هذه لمن يعطيها حقها كاملاً ... اتركها لمن يُكرمها
>
>
>جاء الإسلام بإصلاح عقيدة الناس، وبإصلاح سلوكهم وأخلاقهم
>ومعاملاتهم ... جاء بإكرام المرأة واليتيم والطفل، بل وحِفظ حقوق الدواب
>والشجر... الإسلام جاء بإصلاح العالم بما فيه
>
>
>استمِعْ لما قال جعفر بن أبي طالب الصحابي الجليل حين تكلَّم بين يدي رِي
>النجاشي
>ملك
>الحبشة، وهو يصف له الإسلام ويختصر لماذا ضحوا كل هذه التضحيات من أجل هذا
>الدين، ولماذا تركوا الأهل والبلد وهاجروا في الله، قال جعفر:ن ي هللا عنه
>رص "أيُّها الملِكُ، كُنَّا قَومًا أهلَ جاهليَّةٍ، نَعبُدُ الأصنامَ، وَنَأكُلُ المَيْتَةَ، وَنَأتي
>، فصدَّقْناه وآمَنَّا
>
>!بهذا جاء الإسلام... وبهذا ساد الإسلام
>
>
>وقد أختر الله عز وجل بنصرة نبيه، وكان العرب يسخرون حين يسمعون أن هذا الرجل
>سيبطل الباطل في شرق
>الأرض
>وغرب ها، فجاء الإسلامُ وفتح هللا للمسلمين
>مشارق الأرض ومغاربها
>ممالك الأرض، وسادت كلمة التوحيد
>.فلم يطرق العالم ناموس أفضل ولا أعظم من هذا الناموس
>
>      
>
>(209)
>مسند أحمد، ح1740، بسند صحيح .

>[!summary] English Text
>
>
>And the orphan girl was inherited with her wealth by whoever raised her, and the man would marry her without giving her a dowry; because she is
>an orphan, so the Exalted's words descended: Quranic verse
>ﱡﭐ
>ﱴ
>ﱵ
>ﱶ
>ﱷ ﱸ
>ﱹ
>ﱺ ﱻ
>ﱼ
>ﱽ
>ﱾ
>ﱿ
>ﲀ
>ﲁ ﲂﲃ ﲄ
>ﲅ ﲆ
>ﲇ
>ﲈ ..ﱠ
>﴿3 ﴾
>Surah An-Nisa
>
>
>:Do not approach the orphans' wealth, so marry what pleases you from the women, two, three, and four
>
>And if you fear that
>you will wrong this orphan and not give her her full right, then marry others besides her, two, three
>and four, and leave this one to whoever gives her her full right ... leave her to whoever honors her
>
>
>Islam came to rectify people's beliefs, and to rectify their behavior and morals
>and their transactions ... It came to honor the woman, the orphan, and the child, and even to preserve the rights of animals
>and trees... Islam came to rectify the world in all that it contains
>
>
>Listen to what Ja'far ibn Abi Talib the noble companion said when he spoke before
>Al-Najashi
>the King
>of Abyssinia, as he described Islam to him and summarized why they sacrificed all these sacrifices for the sake of this
>religion, and why they left their families and country and migrated in the cause of Allah, Ja'far said: may Allah be pleased with him
>"O King, we were a people of Jahiliyyah, we worshipped idols, we ate dead meat, and we committed
>adultery, so the Messenger of Allah
>ﷺ
>came to us... and we believed in him
>and followed him.
>
>!It was by this that Islam came... and by this Islam prevailed
>
>
>And Allah the Exalted granted victory to His Prophet, and the Arabs mocked when they heard that this man
>will conquer the East of
>the earth
>and its West, so Islam came and Allah opened for the Muslims
>the East of the earth and its West
>kingdoms of the earth, and the word of monotheism prevailed
>.No law has touched the world better or greater than this law
>
>      
>
>(209)
>Musnad Ahmad, 1740, with authentic chain .

>[!summary] Kurdish Text
>
>
>و کچە باوەکەبێت مێرێتەوە بە پارەکەی بە کەسێک کە دەربەخشی، و مێرد دەھاوسەرگیری دەکات بێ مێھەر؛ بۆوەی
>مێنڈەکە بێ باوەکە، بۆیە قسەی گەورە دەرکەوتووە: ئایەتی قورئان
>ﱡﭐ
>ﱴ
>ﱵ
>ﱶ
>ﱷ ﱸ
>ﱹ
>ﱺ ﱻ
>ﱼ
>ﱽ
>ﱾ
>ﱿ
>ﲀ
>ﲁ ﲂﲃ ﲄ
>ﲅ ﲆ
>ﲇ
>ﲈ ..ﱠ
>﴿3 ﴾
> .سورة النسا
>
>
>:نەدەسین بۆ باوەکەبێت، بۆیە ھەوڵدەر بکە بەو شتەوە کە تو دەوێیت، ھەوڵبژاردن و سێ و چوار، و جێگەرەوە ئەمە لە کەسێک کە ھەوای تەواو دەدات بۆی ... جێگیرەوە بۆ کەسێک کە پارێزگارە
>
>
>ئیسلام ھات بۆ چارەسەرکردنی باوەڕەکانی خەڵک، و چارەسەرکردنی جەنگاوە و ڕەوەش و ھەولەیان
>و کاروبارەکانیان ... ھات بە پارێزکردنی ژن و مێنڈە باوەکە و منداڵ، بەھێز پارێزکردنی مافەکانی دەرەوە
>و دار... ئیسلام ھات بۆ چارەسەرکردنی جیهان بە تەواوی
>
>
>گوێگرە بۆ چی جەعفەر بن ئەبی طالب ھاوبەشی سەرهەڵبەردار وتووە کاتێک قسەی کرد لەبەر
>نەجاشی
>پاشا
>ئەبەسی، کە وتووە ئیسلام وەشاند و وتووە بۆ چی ھەموو ئەم قوربانییە دان بۆ ئەم
>دینە، وچی تێکەڵکردنەوەیان لێیان خوێن، وت جەعفەر:ن ی خوا بێت لێی
>"ئی مێلک، ئێمە خەڵکێکین لە جاهیلیا، دەپرێستین بۆت، و مێرە دەخۆین، و نەچین
>، فصدەقین و باوەڕمان کرد و پێی ھەوڵدەرمان بەسەر
>!بەوەیە ئیسلام ھات... و بەوەیە سەرەکی بوو
>
>
>و خوا گەورە یارمەتیی پێغەمبەر کرد، و کورد بە خەندەک دەکەن کاتێک دەگەیشن کە ئەم مێرد
>پێشەوەی شاری مەککە
>سەنتەر بووە، دەخاتە ناو شاری مەککە، پاشان ئیسلام دەرکەوتووە و خوا کردنەوە بۆ موسڵمانان
>مشارق زەوی و مەغرەبە
>مێلەتە زەوی، و ناوی تەوحید سەرەوە بوو
>.فلم يطرق العالم ناموس أفضل ولا أعظم من هذا الناموس
>
>      
>
>(209)
>مەسند ئەحمەد، 1740، بە سندە دروست .

---

```mermaid
flowchart LR
P(پەڕەی 336)
```"""

with open("2-translation/05_Chapter-5.md", "r", encoding="utf-8") as f:
    content = f.read()

for old, new in replacements.items():
    content = content.replace(old, new)

with open("2-translation/05_Chapter-5.md", "w", encoding="utf-8") as f:
    f.write(content)

print("All sections 13-22 updated")
