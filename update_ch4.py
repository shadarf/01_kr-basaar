import re

with open("2-translation/04_Chapter-4.md", "r", encoding="utf-8") as f:
    content = f.read()

# Section 30 - Page 308 - The fourth fact (Earth's breathing, Moon's phases)
s30 = """§30

>[!summary] Arabic Text
>الحقيقة السا
>
>•
>من الحقائق العلمية في الصباح
>أن أشعة الشمس عندما تسقط على سطح الأرض،
>فإنها
>تسخن سطح الأرض؛ فتنقل حرارة الأرض إلى الهواء الملامس لها، وبالتالي
>في
>يسخن هذا الهواء ويتمدد ويقل ضغطه ويرتفع لأعلى، فيحل محله الهواء في
>الطبقات العليا
>•
>هذا الهواء الذي ارتفع لأعلى كان ناتجاً عن تنفس الكائنات الحية، طوال الليل
>،فتحصل هذه الظاهرة العجيبة صباحاً؛ حيث يتبدل هذا الهواء بهواءٍ جديدٍ نقر
>" وتعرف هذه العملية بعملية
>التيارات الحرارية الصاعدة أو تيارات الحمل "، وكأن
>!في الصباح
>الأرض مثل الرئة العملاقة، وهي تتنفس في
>
>
>قال ربنا سبحانه: ﭐﱡﭐ ﱴ ﱵ ﱶ ﱷﱸ ﱹ ﱺ ﱻ ﱼ ﱽ ﱾ ﱿ ﱠ
>﴿
>12
> .﴾ سورة التكوير
>
>•
>،فهذا حرفياً ما يحدث
>حيث تتنفس الأرض صباحاً تماماً كما الكائنات الحية ... تطرد
>!في أوكسيد الكربون، ثم يحل مكانه هواء جديد نقر
>الهواء المحمل بثاني
>
>الحقيقة
>
>
>قال ربنا سبحانه: ﭐﱡﭐ ﱴ ﱵ ﱶ ﱷﱸ ﱹ ﱺ ﱻ ﱼ ﱽ ﱾ ﱿ ﱠ
>﴿
>12
> .﴾ سورة الإنشاء
>
>•
>آية الليل هي القمر، وآية النهار هي الشمس
>
>•
>آية الليل مُحيت .أي انطفأ نورها
>
>•
>بينما بقيت آية النهار مبرصة .منيرة
>
>
>فهل القمر كان نوراً ثم مُحي؟ هل كان كتلة نارية كالشمس؟
>
>•
>!هذا يُعَد اليوم أحد أكبر الحقائق المكتشفة مؤخراً عن القمر
>
>•
>فالقمر بالفعل كان كتلة نارية، كما يقول عالم الجيولوجيا والأستاذ بجامعة
>كاليفورنيا
>دوغ ماكدوجل .(
>161
>)
>
>      
>
>(161) Dough Macdougall, why geology matters?, P.66

>[!summary] English Text
>The fourth fact
>
>•
>From the scientific facts in the morning
>that when the sun's rays fall on the earth's surface,
>they
>heat the earth's surface; so the earth's heat transfers to the air touching it, and consequently
>in
>this air heats up, expands, its pressure decreases and rises upward, and air from the
>upper layers takes its place
>•
>This air that rose upward was the result of the breathing of living creatures all night
>, so this amazing phenomenon occurs in the morning; where this air is replaced by fresh air
>"and this process is known as the process of
>thermal convection currents or convection currents", and as if
>!in the morning
>the earth is like a giant lung, breathing in
>
>
>Our Lord the Exalted said: Quranic verses
>ﭐﱡﭐ ﱴ ﱵ ﱶ ﱷﱸ ﱹ ﱺ ﱻ ﱼ ﱽ ﱾ ﱿ ﱠ
>﴿
>12
> .﴾ Surah At-Takwir
>
>•
>So this is literally what happens
>where the earth breathes in the morning exactly like living creatures ... expels
>!carbon dioxide, then fresh air takes its place
>the air laden with sec
>
>The fact
>
>
>Our Lord the Exalted said: Quranic verses
>ﭐﱡﭐ ﱴ ﱵ ﱶ ﱷﱸ ﱹ ﱺ ﱻ ﱼ ﱽ ﱾ ﱿ ﱠ
>﴿
>12
> .﴾ Surah Al-Inshiqaq
>
>•
>The sign of the night is the moon, and the sign of the day is the sun
>
>•
>The sign of the night is extinguished .i.e., its light went out
>
>•
>While the sign of the day remained glowing .illuminated
>
>
>So was the moon a light then extinguished? Was it a fiery mass like the sun?
>
>•
>!This is considered today one of the greatest recently discovered facts about the moon
>
>•
>For the moon was indeed a fiery mass, as stated by geologist and professor at the University of
>California
>Doug Macdougall.(
>161
>)
>
>      
>
>(161) Dough Macdougall, why geology matters?, P.66

>[!summary] Kurdish Text
>ڕاستیی چوارەم
>
>•
>لە ڕاستییەکانی زانستی بۆ بەیانی
>کە ھێزی خۆر دەکەوێتە سەر ڕووی زەوی،
>ئەوەش
>گەرم دەکاتەوە ڕووی زەوی؛ بۆیە گەرمی زەو دەگۆڕێتەوە بۆ ھاواکەی ھاوبەش، و بەتایبەت
>ئەم ھاوا گەرم دەبێتەوە و فڕاو دەبێتەوە و پیشی کەم دەبێتەوە و دەچێتە سەرەوە، بۆیە ھاوا لە
>قۆناغە سەرەوەی دەگەڕێتەوە
>•
>ئەم ھاواە کە چووە سەرەوە ھەڵبەرداری تەنفسی جیاوازی جیاوازیان بوو، ھەموو شەوە
>،بۆیە ئەم مێنەوەی سەیرکەرەوە بەیانی سەبەر دەکرێت؛ لێرەدا ئەم ھاوا دەگۆڕێت بە ھاوا نوێی نەوە
>" و ئەم پڕۆسەیە واتا پڕۆسەی
>جەریانە گەرمییەکانی سەرەوە یان جەریانە بارانەکان"، و وەک
>!بەیانی
>زەوی وەک پێشەوە گەورە، ھەست دەکات لە بەیانی
>
>
>راوەشمان گەورە وت: ئایەتی قورئان
>ﭐﱡﭐ ﱴ ﱵ ﱶ ﱷﱸ ﱹ ﱺ ﱻ ﱼ ﱽ ﱾ ﱿ ﱠ
>﴿
>12
> .﴾ سوورەی تکویر
>
>•
>ئەمە بە تەواوی وەک ئەمە دەرچووە
>لێرەدا زەوی بە بەیانی سەبەر ھەست دەکات وەک جیاوازی جیاوازیان... دەخەینەوە
>!بۆ ئەوکسید کاربۆن، پاشان ھاوا نوێی نەوە دەگەڕێتەوە
>ھەوای کە بارکراوە بە دوو
>
>ڕاستیی
>
>
>راوەشمان گەورە وت: ئایەتی قورئان
>ﭐﱡﭐ ﱴ ﱵ ﱶ ﱷﱸ ﱹ ﱺ ﱻ ﱼ ﱽ ﱾ ﱿ ﱠ
>﴿
>12
> .﴾ سوورەی ئینشاق
>
>•
>نیشانەی شەو مانگە، و نیشانەی ڕۆژ خۆرە
>
>•
>نیشانەی شەو مُحیت .واتە نوری لەدەستدا
>
>•
>بەھێز نیشانەی ڕۆژ روناک .ماوە
>
>
>بۆیە مانگ نوێر بوو پاشان مُحی؟ ئایا بەشی ناری وەک خۆر بوو?
>
>•
>!ئەمە لە ئێستادا یەکە لە گەورەترین ڕاستییەکانی دوایین دەربارەی مانگە
>
>•
>بۆوەی مانگ ڕاستەقینە بەشی ناری بوو، وەک وتووی زانای زەوی و مامۆستای زانکۆی
>کالیفۆرنیای
>دۆگ ماکدۆگەل .(
>161
>)
>
>      
>
>(161) Dough Macdougall, why geology matters?, P.66

---

```mermaid
flowchart LR
P(پەڕەی 308)
```"""

# Section 31 - Page 309 - The sixth fact (Water as basis of life)
s31 = """§31

>[!summary] Arabic Text
>الحقيقة السا
>
>•
>قال الله تعالى: ﭐﱡﭐ
>..ﲎ ﲏ ﲐ ﲑ ﲒ ﲓﲔ ﲕ ﲖ ﱠ ﴿٠٣ ﴾
> .سورة الأنبياء
>
>•
>
>وهذا أحد أسس علم الأحياء اليوم، أن
>ي نورةا في
>عنرص الماء داخل رص
>تركيب كل كائن حي .
>
>•
>
>حنر إن العلماء الباحثين عن حياة خارج الأرض هم ال يبحثون عن
>كائنات حية على الكواكب الأخرى، وإنما يبحثون عن الماء؛ لأنهم يعلمون أن ه
>!لا حياة بدون الماء
>
>
>ﱡﭐ ﱍ ﱎ ﱏ ﱐ ﱑ ﱒﱓ ..ﱠ﴿
>45 .﴾ سورة النور
>
>      

>[!summary] English Text
>The sixth fact
>
>•
>Allah the Exalted said: Quranic verses
>ﭐﱡﭐ
>..ﲎ ﲏ ﲐ ﲑ ﲒ ﲓﲔ ﲕ ﲖ ﱠ ﴿03 ﴾
> .Surah Al-Anbiya
>
>•
>
>And this is one of the foundations of biology today, that
>water is an essential element in
>the composition of every living organism.
>
>•
>
>When scientists searching for life outside Earth are not looking for
>living organisms on other planets, but rather they search for water; because they know that
>!there is no life without water
>
>
>Quranic verses
>ﱡﭐ ﱍ ﱎ ﱏ ﱐ ﱑ ﱒﱓ ..ﱠ﴿
>45 .﴾ Surah An-Nur
>
>      

>[!summary] Kurdish Text
>ڕاستیی شەشەم
>
>•
>خوا گەورە وت: ئایەتی قورئان
>ﭐﱡﭐ
>..ﲎ ﲏ ﲐ ﲑ ﲒ ﲓﲔ ﲕ ﲖ ﱠ ﴿٠٣ ﴾
> .سوورەی ئەنبیاء
>
>•
>
>و ئەمە یەکە لە بنەماکانی زانستی ژیوەوەری ئێستا، کە
>ئاو بەشێکی سەرەکییە لە
>پێکهاتەی ھەر ڕوونەوەرێکی ژیندار .
>
>•
>
>کاتێک زانایەکان کە دەگەڕێن بۆ ژیان لە دەرەوەی زەوی ناتوانن دۆزینەوە
>روونەوەرە ژیندارەکان لە پڵانێتەکانی دیکە، بەڵکو دەگەڕێن بۆ ئاو؛ بۆوەی دەزانیان کە
>!ھیچ ژیانێک بێ ئاو نییە
>
>
>ئایەتی قورئان
>ﱡﭐ ﱍ ﱎ ﱏ ﱐ ﱑ ﱒﱓ ..ﱠ﴿
>45 .﴾ سوورەی نۆر
>
>      

---

```mermaid
flowchart LR
P(پەڕەی 309)
```"""

# Section 32 - Page 310 - Hadith scientific miracles (Adam, Coccyx)
s32 = """§32

>[!summary] Arabic Text
>103
>-
>هل هناك إعجاز علمي في الأحاديث النبوية؟
>
>❑
>سأذكر بعض الحقائق العلمية التي تنحاز نحو الحديث النبوي الحديث الأول
>
>رُ وي عن النن ي
>ﷺ
>:أنه قال
>:"وَخَلَقَ آدَمَ عَلَيْهِ السَ لَ مُ بَعْدَ العَصْرِ مِن يَومِ الجُمُعَةِ، في آخِرِ الخَلْقِ، في آخِر
>."سَاعَة (
>169
>)
>
>•
>فآدم في آخر الخَ لْق
>عليه السالم ظهر في
>
>•
>!وهذه إحدى الحقائق العلمية التي ال خالف عليها اليوم بين العلماء
>
>•
>في آخر الكائنات الحية على الأرض
>فالإنسان ظهر في الحديث الثاني
>
>
>قال النن ي
>ﷺ
>في الحديث المت فق عليه صحته
>نف
>."كُ لُّ ابْنِ آدَمَ يَأْكُلُهُ التُرَابُ ، إال عَجْبَ الذَنَبِ منه، خُلِقَ وفيهِ يُرَكَب
>
>(
>169
>)صحيح
>مسلم ح2789
>.

>[!summary] English Text
>103
>-
>Is there a scientific miracle in the Prophetic hadiths?
>
>❑
>I will mention some scientific facts that lean toward the hadith first hadith
>
>Narrated from the Prophet
>ﷺ
>:that he said
>:"AND ADAM WAS CREATED AFTER THE AFTERNOON OF FRIDAY, IN THE LAST OF CREATION, IN THE LAST
>."HOUR (
>169
>)
>
>•
>So Adam appeared in the last of
>creation peace be upon him
>
>•
>!And this is one of the scientific facts that scientists do not differ on today
>
>•
>Man appeared in the last of living creatures on earth
>Second hadith
>
>
>The Prophet
>ﷺ
>said in the hadith agreed upon its authenticity
>in
>."EVERY SON OF ADAM IS EATEN BY THE EARTH, EXCEPT THE COCCYX FROM HIM, HE WAS CREATED FROM IT AND IN IT HE IS ASSEMBLED
>
>(
>169
>)Sahih
>Muslim 2789
>.

>[!summary] Kurdish Text
>103
>-
>ئایا مەعجەزە زانستییە ھەیە لە قسەی پێغەمبەر؟
>
>❑
>دەڵێم چەند ڕاستی زانستی توومار بکەم کە مالە بە قسەی پێغەمبەر جوانینێت یەکەم قسە
>
>نووسیایە لەسەر نێب
>ﷺ
>:کە وت
>:"و خەلقی ئەدەم سڵاو بێت لێی دوای نیوەی جومە، لە کۆتایی دا دروستکردندا، لە کۆتایی
>."كاتژمێر (
>169
>)
>
>•
>بۆیە ئەدەم لە کۆتایی دا دروستکردنەوە دەرکەوتووە
>سڵاو بێت لێی
>
>•
>!و ئەمە یەکە لە ڕاستییە زانستییەکاندا کە ھێشتا ناتوانن زانایان جیاوازی بکەن
>
>•
>لە کۆتایی کەسایەتییە ژیندارەکان لە زەوی
>مرۆڤ دەرکەوتووە قسەی دووەم
>
>
>نێب
>ﷺ
>وت لە قسیی سەحیحدا
>نف
>." ھەموو مناڵی ئەدەم خوێردەوە لە زەوی، بەبێ عەجەبە دوورەوە، خڵق کراوە و لێی دەستپێ دەکرێت
>
>(
>169
>)سەحیح
>مەسلم ح2789
>.

---

```mermaid
flowchart LR
P(پەڕەی 310)
```"""

# Section 33 - Page 311 - Hadith about coccyx/primitive streak
s33 = """§33

>[!summary] Arabic Text
>
>
>فهل نحن خُلقنا من عَجْب الذَنب؟
>
>
>عجب الذنب هو آخِرُ مِنقَة العُصْعُص
>بأسفل العمود الفقري
>
>
>فهل نحن خُلقنا من هذا المكان؟
>
>
>في أول الأسبوع الثالث من الحمل يظهر ما
>نف
>يُعرَف فن
>علم الأجن ة ب
>Primitive Streak
>
>أو
>الشرط الأولي
>
>هذا الشرط الصغير جداً تبين لنا اليوم أنه المسؤول عن تشكيل
>الجنين، فهو يقوم بتشكيل الجنين وتكوين الخلايا المتخصصة التي
>سيظهر منها الجنين
>و بنهاية الأسبوع الثالث من الحمل يبدأ هذا الشرط الأولي
>Primitive Streak
>
>،في الاختفاء تدريجياً
>فنت ر ک يترك مكانه ما يُعرَف
>بالCaudal Eminence
>.
>(
>170
>)

>[!summary] English Text
>
>
>So are we created from the coccyx?
>
>
>The coccyx is the last vertebra of the
>coccyx at the bottom of the spine
>
>
>So are we created from this place?
>
>
>In the first third week of pregnancy, what is known in
>embryology appears as
>Primitive Streak
>
>or
>the primitive streak
>
>This very small streak has become known to us today as responsible for forming
>the embryo, for it forms the embryo and creates the specialized cells that
>will form the embryo
>And by the end of the third week of pregnancy this primitive streak
>Primitive Streak
>
>begins to disappear gradually
>and leaves in its place what is known
>as the Caudal Eminence.
>(
>170
>)

>[!summary] Kurdish Text
>
>
>بۆیە ئێمە خڵق کراوین لە عەجەبە دوورەوە؟
>
>
>
>عجەبە دوورەوە کۆتایی فێقەکەی
>عەصعصە کە لە بنەڕەی مێرگەش
>
>
>بۆیە ئێمە خڵق کراوین لەم شوێنە؟
>
>
>لە یەکەم ھەفتەی سێیەم لە باردووەدا ئەو شتە دەرکەوێت کە
>ناسراوە لە زانستی جنین بە
>Primitive Streak
>
>یان
>شرطی سەرەتاکە
>
>ئەم شرطي بچووکە زۆر ئێستا دەزانین کە ئەوە بەرپرسیارە بۆ دروستکردن
>جنین، کەوە دەکرێتەوە دروستکردنی جنین و دروستکردنی ستانە تایبەتەکان کە
>دەرکەون بۆ جنین
>و بە کۆتایی ھەفتەی سێیەم لە باردووە دەستپێ دەکات ئەم شرطي سەرەتاکە
>Primitive Streak
>
>دەبێتەوە نادیار بە شێوەیەکی ڕووتین
>و دەوێتە شوێنی شتێک کە ناسراوە
>بە Caudal Eminence
>.
>(
>170
>)

---

```mermaid
flowchart LR
P(پەڕەی 311)
```"""

# Section 34 - Page 312 - Caudal Eminence becomes coccyx, 360 joints
s34 = """§34

>[!summary] Arabic Text
>
>
>سَيَتَضَاءَلُ ال
>Caudal Eminence
>
>مع الوقت ويتحول إلی مِنقَة
>العصعص! (
>171
>)
>
>
>
>فالعُصعص في الأصل الشرط الأولي
>هو في Primitive Streak
>
>الذي نشأ منه
>الجنين ... المكان الذي منه خُلقنا كما أخبرت النن ي
>ﷺ
>قبل أكثر من1400
>عام
>
>تخيَّلْ رجلاً يرع
>أغناماً على قراريط لأهل مكة، يُخبر بحقائق لم يعرف العلم دقائقها
>إلا منذ سنواتٍ قليلة
>!
>
>
>
>بل وأنا
>الطبيب المتخصص، والله عانيتُ حين
>أستوعب دقة هذا الحديث، وكيف
>في الأسبوع الثالث من عمر الجنين، الذي كان
>شيء الدقيق الذي ظهر في
>يتحول هذا الشرط الدقيق أن يختفين تماماً بعد ذلك من مشح
>منطقة العصعص
>الأحداث ليستقر في
>
>
>ما هذه الدقة وما هذا الإعجاز؟ الحديث الثالث
>
>
>قال النبي ﷺ :، والحديث في صحيح مسلم
>"إن ه خُلِقَ كُلُّ إِنْسَانٍ مِن بَنِي آدَمَ عَلَى سِتِّينَ وَثَلَاثِمِئَةِ مَفْصِلٍ، فَمن كَ بَرَ اهللَ، وَحَمِد
>،ًاهللَ، وَهَ ل لَاهللَ، وَسَ ب حَ اهللَ، وَعَزَلَ حَجَرًا عَن طَرِيقِ الن اسِ، أَوْ شَ وْكَ ة
>أوْ عَظْمَاً عَن طَرِيقَ الن َاسِ، وَأَمَرَ بِمَعْرُوفٍ، أَوْ نَهَى عَن مُنْكَ رٍ، عَدَدَ تِلكَ السِّ تِّين
>والث الثِمِئَةِ السُّ الَمَى، فَإِن ه يَمْشِ ي يَومَئِذٍ وَقَدْ زَحْزَحَ نَفْسَ هُ عَنِ الن ار
>(
>172
>)

>[!summary] English Text
>
>
>THE Caudal Eminence
>WILL DWINDLE
>over time and transform into the region of
>the coccyx! (
>171
>)
>
>
>
>For the coccyx is originally the primitive streak
>Primitive Streak
>
>from which
>the embryo emerged ... the place from which we were created as the Prophet
>ﷺ
>informed us more than 1400
>years ago
>
>Imagine a man herding
>sheep on the outskirts of Mecca, informing of facts that science did not know the details of
>until just a few years ago
>!
>
>
>
>And I
>as a specialist doctor, by Allah I suffered when
>I tried to comprehend the precision of this hadith, and how
>in the third week of the embryo's age, which was
>the precise thing that appeared in
>this primitive streak transforms, how this precise streak disappears completely after that from the scene
>to settle in the region of the coccyx
>events
>
>
>
>What is this precision and what is this miracle? The third hadith
>
>
>The Prophet ﷺ said: in Sahih Muslim
>"VERILY EVERY HUMAN FROM THE CHILDREN OF ADAM IS CREATED UPON THREE HUNDRED AND SIXTY JOINTS, SO WHOEVER GLORIFIES ALLAH, AND PRAISES
>ALLAH, AND SAYS THERE IS NO GOD BUT ALLAH, AND GLORIFIES ALLAH, AND SEEKS FORGIVENESS FROM ALLAH, AND REMOVES A STONE FROM THE PEOPLE'S PATH, OR A THORN
>FROM THE PEOPLE'S PATH, THE NUMBER OF THOSE THREE HUNDRED AND SIXTY JOINTS, THEN HE WALKS THAT DAY HAVING REMOVED HIMSELF FROM THE FIRE
>(
>172
>)

>[!summary] Kurdish Text
>
>
>Caudal Eminence
>دەبێتەوە بچووک
>بە کات
>و دەگۆڕێتەوە بۆ ناوچەی
>عصعص! (
>171
>)
>
>
>
>بۆوەی عەصعص لە سەرەتادا شرطي سەرەتاکەیە
>Primitive Streak
>
>کە لێی
>جنین دروست بووە ... شوێنەکەی کە ئێمە دروست کراوین وەک کە نێب
>ﷺ
>وتومان بە زیاتر لە 1400
>ساڵ پێش
>
>تخی لْ رێگەل کەسێک کە مێڵی چاوێر دەکات لە کەنار مەککە، وتووە بە ھەوڵەکە کە زانست نەزانستی وردەی
>ھەتا دوایین ساڵان
>!
>
>
>
>بەلکۆ من
>پزیشکی مامۆستا، و خوا من کێش کرد کە
>دەزانیم وردی ئەم قسییە، و چۆن
>لە ھەفتەی سێیەم لە تەمەنی جنین، کە
>شتە وردەکە دەرکەوتووە
>دەگۆڕێت، چۆن ئەم شرطي وردە تەواو نادیار دەبێت لە مێژوو
>نەوچەی عەصعص
>بەھێز دەکەوێتەوە
>
>
>
>چییە ئەم وردی و چییە ئەم مەعجەزە؟ قسەی سێیەم
>
>
>نێب
>ﷺ
>وت، و قسی لە سەحیح مەسلم
>"ھەر کەسێک لە کوردانی ئەدەم لەسەر ٣٦٠ مێوە دەستپێ دەکات، بۆیە کەسێک تەسبیح خوا بکات، و حەمد بۆ خوا، و لێ خوا نییە، و سووبان خوا، و بۆخۆت بکرێتەوە، و دەنگە دەر بکەیت لە ڕێگای خەڵک، یان تێخ، یان باوە، ئەم ژمارەی ٣٦٠ تەوە مێوە، بۆوە کە رووژێک دەچێتەوە و خۆی جێگیراوە لە نەر
>(
>172
>)

---

```mermaid
flowchart LR
P(پەڕەی 312)
```"""

# Section 35 - Page 313 - 360 joints confirmed
s35 = """§35

>[!summary] Arabic Text
>
>
>هذا العددُ الدقيقُ ثلاثمائة وستون مفصِلاً ظل محلاً خلافاً بين الأطباء لسنوات
>طويلةٍ، إلى أن استقر ت المراجع الطبية الحديثة على هذا الرقم
>بالتحديد: ثلاثمائة وستون مفصِلاً .
>
>•
>ففي الإنسان تحديداً ثلاثمائة وستون مفصل
>
>
>
>هذه القضية اليوم أصبحت
>إحدى الحقائق العلمية!
>
>      
>
>(172) صحيح
>مسلم ح1007
>.

>[!summary] English Text
>
>
>This precise number of three hundred and sixty joints remained a subject of dispute among physicians for
>many years, until modern medical references settled on this number
>precisely: three hundred and sixty joints.
>
>•
>In humans specifically there are three hundred and sixty joints
>
>
>
>This issue has become
>one of the scientific facts today!
>
>      
>
>(172) Sahih
>Muslim 1007
>.

>[!summary] Kurdish Text
>
>
>ئەم ژمارەی وردییە سێ سەد و شەشتی مێوە ماوە مێژووی دەروونی داکتۆران بۆ ساڵان درێژ
>مێن، ھەتا کە سەرچاوەکانی پزیشکی مۆدێرن بە تایبەتی ئەم ژمارەیە داڵنیاکرد
>بە تەواوی: سێ سەد و شەشتی مێوە .
>
>•
>لە مرۆڤیدا تایبەتە سێ سەد و شەشتی مێوە ھەیە
>
>
>
>ئەم کێشەیە ئێستا بووە
>یەکە لە ڕاستییەکانی زانستی!
>
>      
>
>(172) سەحیح
>مەسلم ح1007
>.

---

```mermaid
flowchart LR
P(پەڕەی 313)
```"""

# Section 36 - Page 314 - Chinese reference refutation, conclusion
s36 = """§36

>[!summary] Arabic Text
>104
>-
>لكن بعض المالحدة يقول: هناك مرجع صينيٌّ قديم ذَكَرَ هذا الرقم: ثلاثمائة وستين مفصِلاً؟
>
>• تبي   ن  بالعودة  للمرجع  أن   هذا كذبٌ ،  فالمرجعُ  يقول ،:  ثلاثمائة  وخمسة  وستين
>،ي الفلسفة الدينية الصينية
>وليس ثلاثمائة وستين، وهذا بناءا عىل عدد أيام العام في
>وارتباط أيام العام بالجسد البشر ي
>•
>فالمرجع ال يتحد ث عن عدد المفاصل تحديداً، وإنما عن أجزاء الهيكل العظمي التي
>تدخل منها الطاقة الكونية (
>173
>)
>
>•
>فالمرجع لا يتحد ث عن عدد المفاصل تحديداً، وإنما عن أجزاء الهيكل العظمي التي
>تدخل منها الطاقة الكونية (
>173
>)
>
>
>
>ثم أنا ال أدري كيف ينسب المالحدةُ للنبي ﷺ
>لمَ أهل الأرض: صينية
>،
>وسريانية وفرعونية كل هذا حتى ينفوا عنه
>معجزة واحدة?
>
>•
>! هذا موقفٌ بائس
>
>•
>في الحق بعدما تبي   ن
>سيبقون هكذا يجادلون فن
>
>•
>لقد ثبت بالتواتر وقوعُ المعجزات التي ال حرص لها على يد محمد
>ﷺ
>؛ فوالله إن
>القطع بنبوته هو رشاد العقل
>
>•
>قضية الإعجاز العلمي المُوثق تحتاج إىل عمل موسوعي حقيقي يعمل عليه علماء
>وباحثون متخصصون، فهذا ميدان عظيم، وفيه نفع للناس جميعً ا
>
>
>:د
>ِ
>وأقول لكل مُلحِد فَكِّرْ وَهللا وَستصل؛ وال تُصدِّقْ من يريدون أن
>يضلوك عن سبيل الله
>
>      
>
>(173) Huang Di's Inner Classic.

>[!summary] English Text
>104
>-
>But some atheists say: there is an ancient Chinese reference that mentioned this number: three hundred and sixty joints?
>
>• It became clear upon returning to the reference that this is a lie, for the reference says: three hundred and sixty
>five, in Chinese religious philosophy
>not three hundred and sixty, and this is based on the number of days in the year
>and the connection of the year's days with the human body
>•
>So the reference does not speak of the number of joints specifically, but rather about parts of the skeletal structure through which
>cosmic energy enters (
>173
>)
>
>•
>So the reference does not speak of the number of joints specifically, but rather about parts of the skeletal structure through which
>cosmic energy enters (
>173
>)
>
>
>
>Then I don't know how the atheists attribute to the Prophet ﷺ
>for the people of the earth: Chinese
>Syriac, and Egyptian all this just to deny him
>one miracle?
>
>•
>! This is a pathetic position
>
>•
>In the truth after it has become clear
>they will keep arguing like this
>
>•
>It has been proven by tawatur the occurrence of miracles that had no condition on the hand of Muhammad
>ﷺ
>; so by Allah truly
>the certainty of his prophethood is the guidance of reason
>
>•
>The issue of the documented scientific miracle needs a true encyclopedic work carried out by scholars
>and specialized researchers, for this is a great field, and in it is benefit for all people
>
>
>:D
>ِ
>And I say to every atheist: THINK, AND BY ALLAH YOU WILL ARRIVE; AND DO NOT BELIEVE THOSE WHO WANT TO
>MISLEAD YOU FROM THE PATH OF ALLAH
>
>      
>
>(173) Huang Di's Inner Classic.

>[!summary] Kurdish Text
>104
>-
>بەڵام ھەندێک لە بێباوەڕان دەڵێن: ھەیە سەرچاوەیەکی چینێ کۆن کە ئەم ژمارەیە وتووە: سێ سەد و شەستی مێوە?
>
>• دەرکەوتووە لە دوای گەڕانەوە بۆ سەرچاوەکە کە ئەمە درۆیە، بۆوەی سەرچاوەکە دەڵێت: سێ سەد و شەشتی و پێنج مێوە، لە فەلسەفەی ئایینی چینی
>نە سێ سەد و شەشتی، و ئەمە بەسەر بە ژمارەی ڕۆژەکان ساڵەکەدا
>و پەیوەندی ڕۆژەکان لەگەڵ لەشتی مرۆڤ
>•
>بۆیە سەرچاوەکە نەقسی دەکات لەسەر ژمارەی مێوە تایبەتە، بەڵکو لەبەر بەشەکانی ماوێژی ئاسۆی کە
>دەچنە ناو ھێنانی ھێزی کۆن
>(
>173
>)
>
>•
>بۆیە سەرچاوەکە نەقسی دەکات لەسەر ژمارەی مێوە تایبەتە، بەڵکو لەبەر بەشەکانی ماوێژی ئاسۆی کە
>دەچنە ناو ھێنانی ھێزی کۆن
>(
>173
>)
>
>
>
>پاشان من نازانم چۆن بێباوەڕان نێبەوە دابنێن بۆ پێغەمبەر ﷺ
>بۆ خەڵکی زەوی: چینی
>سریانی، و میسری ھەموو ئەمە ھەتا بۆ نەقین مەعجەزەیەک لێی
>
>•
>! ئەم شوێنە بایەسە
>
>•
>لە ڕاستییەوە دوای دەرکەوتنی
>ھێشتا وەک ئەمە دەقسی دەکەن
>
>•
>دڵنیاکراوە بە تواتر ڕوویداوەی مەعجەزەکان کە ھێشتا بێ شەرتبوون لەدەست محەمەد
>ﷺ
>؛ بۆوەی خوا ڕاستە
>دڵنیایی پێغەمبەرتییە ھێوازی بیرە
>
>•
>کێشەی مەعجەزە زانستییە توومار کراوە پێویستی بە کارێکی موسوعیدا ھەیە کە لێی زانایەکان و توێژینەوەکەرانی تایبەت کار بکەن، بۆوەی باوە مێدانی گەورەیەکە، و لێرەدا سودە ھەیە بۆ ھەموو خەڵک
>
>
>:د
>ِ
>و من بۆ ھەر بێباوەڕێک دەڵێم: بیر بکەرەوە و خوا، و دەرکەوە؛ و مەوەست مەکە لەوانەی کە دەوێن توو ببڕێنەوە لە ڕێگای خوا
>
>      
>
>(173) Huang Di's Inner Classic.

---

```mermaid
flowchart LR
P(پەڕەی 314)
```"""

# Apply all replacements
replacements = {
    "§30\n\n>[!summary] Arabic Text\n>\n\n>[!summary] English Text\n>\n\n>[!summary] Kurdish Text\n>\n\n---\n\n```mermaid\nflowchart LR\nP(پەڕەی 308)\n```": s30,
    "§31\n\n>[!summary] Arabic Text\n>\n\n>[!summary] English Text\n>\n\n>[!summary] Kurdish Text\n>\n\n---\n\n```mermaid\nflowchart LR\nP(پەڕەی 309)\n```": s31,
    "§32\n\n>[!summary] Arabic Text\n>\n\n>[!summary] English Text\n>\n\n>[!summary] Kurdish Text\n>\n\n---\n\n```mermaid\nflowchart LR\nP(پەڕەی 310)\n```": s32,
    "§33\n\n>[!summary] Arabic Text\n>\n\n>[!summary] English Text\n>\n\n>[!summary] Kurdish Text\n>\n\n---\n\n```mermaid\nflowchart LR\nP(پەڕەی 311)\n```": s33,
    "§34\n\n>[!summary] Arabic Text\n>\n\n>[!summary] English Text\n>\n\n>[!summary] Kurdish Text\n>\n\n---\n\n```mermaid\nflowchart LR\nP(پەڕەی 312)\n```": s34,
    "§35\n\n>[!summary] Arabic Text\n>\n\n>[!summary] English Text\n>\n\n>[!summary] Kurdish Text\n>\n\n---\n\n```mermaid\nflowchart LR\nP(پەڕەی 313)\n```": s35,
    "§36\n\n>[!summary] Arabic Text\n>\n\n>[!summary] English Text\n>\n\n>[!summary] Kurdish Text\n>\n\n---\n\n```mermaid\nflowchart LR\nP(پەڕەی 314)\n```": s36,
}

with open("2-translation/04_Chapter-4.md", "r", encoding="utf-8") as f:
    content = f.read()

for old, new in replacements.items():
    content = content.replace(old, new)

with open("2-translation/04_Chapter-4.md", "w", encoding="utf-8") as f:
    f.write(content)

print("All sections 30-36 updated successfully")
