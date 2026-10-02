# 注記

[notes.md](notes.md) の日本語訳。このディレクトリで整理した4つの版の詩行と、各版の注解の項目と索引の日本語訳を、The Latin Library（[ilias.txt](ilias.txt)）の順に詩行ごとに並べる。このディレクトリの `make notes`（[notes.py](notes.py)）が [concordance.md](concordance.md)、各版の `ilias.md`、`COMMENTARY-ja.md` と `INDEX-ja.tsv` から生成し、それらが変わると作り直す。手で修正しないこと。

- 各詩行は The Latin Library（LL）の行番号と本文で始まる。「79a」「79b」は The Latin Library にない詩行で、各版でその前にある詩行の後に置く。
- 続いて各版、[2] Lemaire（ヴェルンスドルフの行番号）、[3] Baehrens、[4] Plessis、[6] Vollmer を箇条書きにし、対照表のとおりにその版の行番号と本文を示す（「[n]」はその版が括弧に入れる詩行、「below」はプレシが本文の下に印刷する詩行、「—」は該当なし）。その下の入れ子にその版の COMMENTARY-ja.md のうち、その詩行の項目を置く。詩行はラテン語のまま。
- 項目のラベルは、上に示した詩行の番号以上の情報がある場合に限って残す。すなわち詩行の範囲（項目はその最初の詩行に置く）と、前の頁から続く Lemaire の注「(cont.)」である。フォルマーの証言には「（証言）」と記す。
- [4] Plessis と [6] Vollmer では、項目の後にその版の INDEX-ja.tsv のうちその詩行を挙げる行を、表の順に「語形 (見出し語; 見出し語の日本語): 説明」の形で置く。語形はその詩行にあるラテン語の形（詩行にない場合は「—」）、見出し語はラテン語、説明は日本語訳。詩行の範囲を挙げる行はその最初の詩行に、複数の詩行を挙げる行はそれぞれの詩行に置く。ただし連続する詩行では最初の詩行だけに置く。詩行のない相互参照は省く。
- 本文と項目は各ファイルにあるとおりに引く。何を残し何を省いたかは各版の COMMENTARY-ja.md と README.md を参照。

## Book 1

1 Iram pande mihi Pelidae, Diua, superbi
- [2] 1 Iram pande mihi Pelidae, Diva, superbi,
- [3] 1 Iram pande mihi Pelidae, Diua, superbi,
- [4] 1 Iram pande mihi Pelidae, Diva, superbi,
  - Pelidae (ACHILLES; アキレウス): Pelidae:驕れるペレウスの子の怒り
  - Diva (DIVA; 女神): (すなわちムーサ)
- [6] 1 Iram pande mihi Pelidae, Diva, superbi,
  - — (Baebius; バエビウス): および 1—8 行のアクロスティックを参照
  - Diva (Diva; 女神): Diva 1:ムーサ
  - Pelidae (Pelides; ペリデス): -dae . . . superbi 1

2 Tristia quae miseris iniecit funera Grais
- [2] 2 Tristia quae miseris injecit funera Graiis ,
  - *Injecit funera*（死をもたらした）。より古い詩人たちは *immittere* または *dare funera* と言う。Virg. Aen. X, 13: « Quum fera Carthago Romanis arcibus olim Exitium magnum atque Alpes immittet apertas »；Val. Flaccus, III, 681: « nec enim solis dare funera Colchis Sit satis »。――もっともプラウトゥスは Amphitr. I, 1, 35 で *objicere funera* と言っている: « Qui multa Thebano populo objecit funera »。パリ編者。
- [3] 2 Tristia quae miseris iniecit funera Grais
- [4] 2 Tristia quae miseris injecit funera Grais
  - Grais (GRAI; ギリシア人): Grais:アキレウスの怒りが哀れなギリシア人に死をもたらした
- [6] 2 Tristia quae miseris iniecit funera Grais
  - Grais (Graius; ギリシアの): Grais 2. 277. 614

3 Atque animas fortes heroum tradidit Orco
- [2] 3 Atque animas fortes heroum tradidit Orco,
- [3] 3 Atque animas fortes heroum tradidit orco,
- [4] 3 Atque animas fortes heroum tradidit orco,
- [6] 3 Atque animas fortes heroum tradidit Orco
  - Orco (Orcus; オルクス): animas . . . tradidit Orco 3

4 Latrantumque dedit rostris uolucrumque trahendos
- [2] 4 Latrantumque dedit rostris volucrumque trahendos
  - *Volucrumque trahendos*（鳥たちに引き裂かれるべき）。P・ボンダムは『異読考』(*Var. Lect.*) II, 4 で、作者がここで Ovid. Ib. 171 を模倣したと指摘している: « Unguibus et rostro tardus trahet ilia vultur, Et scindent avidae perfida corda canes »。
- [3] 4 Latrantumque dedit rostris uolucrumque trahendos
- [4] 4 Latrantumque dedit rostris volucrumque trahendos
- [6] 4 Latrantumque dedit rostris volucrumque trahendos

5 Illorum exsangues, inhumatis ossibus, artus.
- [2] 5 Illorum exsangues inhumatis ossibus artus.
  - *Exsangues inhumatis ossibus*（血の気のない、埋葬されぬ骨のままの）。Virgil. Aen. XI, 22: « socios inhumataque corpora terrae Mandemus »。Ovid. Her. XI, 123: « Ossa superstabunt volucres inhumata marinae »。
- [3] 5 Illorum exsangues inhumatis ossibus artus.
- [4] 5 Ipsorum exsangues inhumatis ossibus artus.
  - Ipsorum …。『イリアス』I, 4 αὐτοὺς δέ を参照。
- [6] 5 Illorum exsangues inhumatis ossibus artus.

6 Confiebat enim summi sententia regis,
- [2] 6 Confiebat enim summi sententia regis,
  - **(cont.)** … 動詞 *confiebat* はホメロスのギリシア語 Διὸς δ᾽ ἐτελείετο βουλή を最も見事に表現しており、同様に Virg. Aeneid. IV, 116 でもその動詞が用いられている: « nunc qua ratione, quod instat, Confieri possit, paucis, adverte, docebo »。ルクレーティウスもこれを用いており、III, 413: « Id quoque enim sine pernicie confiet eorum »、同 IV, 292: « quoniam res confit utroque »。
- [3] 6 Confiebat enim summi sententia regis,
- [4] 6 Confiebat enim summi sententia regis,
- [6] 6 Confiebat enim summi sententia regis,
  - regis (Iuppiter; ユピテル): summi . . . regis 6. 105

7 protulerant* ex quo discordia pectora pugnas,
- [2] 7 Ex quo contulerant discordi pectore pugnas
  - … 同様に Virg. Aen. X, 146: « Illi inter sese duri certamina belli Contulerant »。
- [3] 7 Ut primum tulerant discordi pectore pugnas
- [4] 7 Volverunt ex quo discordi pectore turbas
- [6] 7 † Protulerant ex quo discordia pectora turbas,
  - （証言） エルメンリクス『グリマルドゥス宛書簡』(850–55年頃)、*Mon. Germ. hist. Epist.* V 545, 24: 「ホメロスの『イリアス』において E が詩的に短音化されている: *Pertulĕrunt ex quo discordia pectora turmas*」

8 Sceptriger Atrides et bello clarus Achilles.
- [2] 8 Sceptriger Atrides, et bello clarus Achilles.
- [3] 8 Sceptriger Atrides et bello clarus Achilles.
- [4] 8 Sceptriger Atrides et bello clarus Achilles.
  - Achilles (ACHILLES; アキレウス): 主格、主語として:戦で名高く、アガメムノンに怒る
  - Atrides (AGAMEMNON; アガメムノン): Atrides:笏を持つ者、アキレウスに怒る
- [6] 8 Sceptriger Atrides et bello clarus Achilles.
  - Achilles (Achilles; アキレウス): bello clarus -es 8
  - Atrides (Atrides (Agamemno); アトリデス（アガメムノン）): sceptriger -es 8

9 Quis deus hos ira tristi contendere iussit?
- [2] 9 Quis Deus hos ira tristi contendere jussit?
  - … さらにホメロスの言葉 ἔριδι ξυνέηκε μάχεσθαι もこの読みを要求している。
- [3] 9 Quis deus hos ira tristi contendere iussit?
- [4] 9 Quis deus hos jussit ira contendere tristi ?
- [6] 9 quis deus hos ira tristi contendere iussit?

10 Latonae et magni proles Iouis. Ille Pelasgum
- [2] 10 Latonae et magni proles Jovis. Ille Pelasgum
- [3] 10 Latonae et magni proles Iouis. ille Pelasgum
- [4] 10 Latonae et magni proles Jovis. Ille Pelasgum
  - proles (APOLLO; アポロ): Proles Jovis et Latonae:ユピテルとラトナの子
  - Pelasgum (GRAI; ギリシア人): Pelasgum:ペラスゴイの王に敵意を抱くアポロ
  - Jovis (JUPPITER; ユピテル): Jovis 属格:偉大なユピテルの子(アポロ)
  - Latonae (LATONA; ラトナ): Latonae et Jovis proles:ラトナとユピテルの子
- [6] 10 Latonae et magni proles Iovis. ille Pelasgum
  - regi (Agamemnon; アガメムノン): Pelasgum . . . regi 10 を参照
  - Iovis (Iuppiter; ユピテル): 属格:magni proles . . . Iovis 10:アポロ
  - Latonae (Latona; ラトナ): Latonae et magni proles Iovis 10:アポロ
  - Pelasgum (Pelasgi; ペラスゴイ): -um . . . regi 10

11 infestam regi pestem in praecordia misit
- [2] 11 Infestus regi pestem in praecordia misit,
  - … というのも、ホメーロスの言葉、9 行の ὃ γὰρ βασιλῆϊ χολωθείς がそれを意味しており、作者自身も下の 55 行で « Haec ait: Infesti placemus numina Phoebi » と確証しているからである。…*Pestem in praecordia misit*（胸のうちに破滅を送り込んだ）：すなわち、彼らにとって破滅的なものとなる怒りのことである。オウィディウスの Metam. VIII, 791 で、ケーレースがエリュシクトーンに送り込まれた飢餓について次のように述べるのと同様である: « ea se in praecordia condat Sacrilegi scelerata jube »。
- [3] 11 Infestus regi pestem in praetoria misit
- [4] 11 Infestus regi pestem in praecordia misit
  - Infestus …。『イーリアス』I, 9 : βασιλῆϊ χολωθείς を参照。…
- [6] 11 infestus regi pestem in praecordia misit
  - Infestus (χολωθείς) … pestem すなわち amorem Chryseidos (26行を参照) …

12 implicuitque graui Danaorum corpora morbo.
- [2] 12 Implicuitque gravi Danaorum corpora morbo.
  - *Implicuit morbo*（病に巻き込んだ）。実に不作法な言い回しであり、ほとんど直後の 14 行で *implicitus* が再び現れるため、なおさら耳障りである。パリ編者。
- [3] 12 Inplicuitque graui Danaorum corpora morbo.
- [4] 12 Implicuitque gravi Danaorum corpora morbo.
  - Danaorum (GRAI; ギリシア人): Danaorum:アポロはダナオイの身体を病に巻き込んだ
- [6] 12 implicuitque gravi Danaorum corpora morbo.
  - Danaorum (Danai; ダナオイ): -orum 12

13 Nam quondam Chryses, sollemni tempora uitta
- [2] 13 Nam quondam Chryses solenni tempora vitta
  - … 彼は鉢巻（*vitta*）を頭に結ばれた祭司の印と呼んでおり、これはアポロの犠牲式や奉仕において厳かに用いられるべきものであった。オウィディウスの Met. V, 110 でケーレースの祭司が « albenti velatus tempora vitta » と言われているのと同様である。…
- [3] 13 Nam quondam Chryses, sollemni tempora uitta
- [4] 13 Nam Chryses quondam, sollemni tempora vitta
  - Chryses (CHRYSES; クリュセス): 奪われた娘のために泣く
- [6] 13 nam quondam Chryses, sollemni tempora vitta
  - Chryses (Chryses; クリュセス): Chryses 13

14 implicitus, raptae fleuit solacia natae
- [2] 14 Implicitus, raptae flevit solatia natae,
- [3] 14 Inplicitus, raptae fleuit solatia natae
- [4] 14 Implicitus, raptae flevit solacia natae
- [6] 14 implicitus, raptae flevit solacia natae
  - natae (Chryseis; クリュセイス): raptae . . . natae 14 を参照

15 inuisosque dies inuisaque tempora noctis
- [2] 15 Invisosque dies invisaque tempora noctis
  - … クリュセスが日夜嘆いていたことを
  - **(cont.)** （前頁からの続き）作者はここでクリュセスについて述べており、おそらくウェルギリウスがオルペウスについて Georg. IV, v. 464 で次のように歌ったのを模倣したのであろう: « Ipse cava solans aegrum testudine amorem, Te dulcis conjux, te solo in litore secum, Te veniente die, te decedente canebat »。ホメロスは嘆きの時間や永続性には触れず、それに対してクリュセスをただ一人浜辺を歩む者としている。ウェルギリウスがオルペウスにおいて表現したそのことを、われらの作者は省いている。悲嘆に暮れる者にとって光や生命が忌まわしい（*invisam*）と言うのは詩人たち、とりわけウェルギリウスの常である（Aen. IV, 631, XII, 177 など）。
- [3] 15 Inuisosque dies inuisaque tempora noctis
- [4] 15 Invisosque dies invisaque tempora noctis
- [6] 15 invisosque dies invisaque tempora noctis

16 egit et assiduis impleuit questibus auras.
- [2] 16 Egit, et assiduis implevit questibus auras.
- [3] 16 Egit et assiduis impleuit questibus auras.
- [4] 16 Egit et assiduis implevit questibus auras.
- [6] 16 egit et assiduis implevit questibus auras.

17 Postquam nulla dies animum maerore leuabat
- [2] 17 Postquam nulla dies animum moerore levabat,
  - … バルトは『雑考』(*Advers.*) LVIII, 14 で、続くこの 5 行は際立った才知と判断力をもって書かれていると断言し、その甘美さを称賛している。…
- [3] 17 Postquam nulla dies animum maerore leuabat
- [4] 17 Postquam nulla dies animum maerore levabat
- [6] 17 postquam nulla dies animum maerore levabat

18 nullaque lenibant patrios solacia fletus,
- [2] 18 Nullaque lenibant patrios solatia fletus,
- [3] 18 Nullaque lenibant patrios solatia fletus,
- [4] 18 Nullaque lenibant patrios solacia fletus,
- [6] 18 nullaque lenibant patrios solacia fletus,
  - fletus (Chryses; クリュセス): patrios . . . fletus 18

19 castra petit Danaum genibusque affusus Atridae
- [2] 19 Castra petit Danaum, genibusque adfusus Atridae,
- [3] 19 Castra petit Danaum genibusque affusus Atridae
- [4] 19 Castra petit Danaum genibusque affusus Atridae
  - Atridae (AGAMEMNON; アガメムノン): Atridae 属格:クリュセスはその膝元にひれ伏す
  - Danaum (GRAI; ギリシア人): Danaum:クリュセスはダナオイの陣営を目指す
- [6] 19 castra petit Danaum genibusque affusus Atridae
  - Atridae (Atrides (Agamemno); アトリデス（アガメムノン）): -dae 属格:19
  - Danaum (Danai; ダナオイ): -um(属格):19. 50. 67. 124. 153. 251. 268. 357. 389. 496. 631. 686. 691. 698. 705. 743. 747. 794. 1025

20 per superos regnique decus miserabilis orat,
- [2] 20 Per Superos regnique decus miserabilis orat,
- [3] 20 Per superos regnique decus miserabilis orat,
- [4] 20 Per superos regnique decus miserabilis orat,
- [6] 20 per superos regnique decus miserabilis orat,

21 ut sibi causa suae reddatur nata salutis.
- [2] 21 Ut sibi caussa suse reddatur nata salutis:
  - *Ut sibi caussa suae*（みずからの…の原因として彼に）。Ovid. Met. VI, 499 で、パンディオーンが娘について次のように述べている: « Per Superos oro ..... Et mihi sollicitae lenimen dulce senectae Quamprimum (omnis erit nobis mora longa) remittas »。
- [3] 21 Ut sibi causa suae reddatur nata salutis.
- [4] 21 Ut sibi causa suae reddatur nata salutis.
- [6] 21 ut sibi causa suae reddatur nata salutis.
  - nata (Chryseis; クリュセイス): nata 21. 42

22 Dona simul praefert. Vincuntur fletibus eius
- [2] 22 Dona simul profert : vincuntur fletibus ejus
- [3] 22 Dona simul praefert. uincuntur fletibus eius
- [4] 22 Dona simul praefert. Vincuntur fletibus ejus
- [6] 22 dona simul praefert. vincuntur fletibus eius

23 Myrmidones reddique patri Chryseida censent.
- [2] 23 Myrmidones , reddique patri Chryseida censent.
  - *Myrmidones*（ミュルミドン）。バルトは前掲箇所で、十分な慎重さを欠いて、この作者によって「ミュルミドン」が全ギリシア人の換称として用いられていると述べ、ウェルギリウス（マロー）は同じ意味でダナオイ、アルゴス人、ペラスゴイを用いているが、この用法は新しいがゆえに賛同できない、その上ミュルミドンは事情が異なり、その名においてまったく固有の民族的起源を示しており、それを他の者たちにまで拡張することは歴史を知らぬ者のような印象を与える、と論じている。
- [3] 23 Myrmidones reddique patri Chryseida censent.
- [4] 23 Myrmidones reddique patri Chryseida censent.
  - Chryseida (CHRYSEIS; クリュセイス): Chryseida:ミュルミドンは彼女を父に返すべきだと考える
  - Myrmidones (MYRMIDONES; ミュルミドン): クリュセスの涙に打ち負かされ、娘を返すべきだと考える
- [6] 23 Myrmidones reddique patri Chryseida censent.
  - Chryseida (Chryseis; クリュセイス): -da 23. 56. 64
  - patri (Chryses; クリュセス): patri 23 を参照
  - Myrmidones (Myrmidones; ミュルミドン): Myrmidones(すなわちギリシア人)23

24 Sed negat Atrides Chrysenque excedere castris
- [2] 24 Sed negat Atrides, Chrysenque excedere castris
- [3] 24 Sed negat Atrides Chrysenque excedere castris
- [4] 24 Sed negat Atrides Chrysenque excedere castris
  - Atrides (AGAMEMNON; アガメムノン): — クリュセイスを返すことを拒む
  - Chrysen (CHRYSES; クリュセス): Chrysen:アガメムノンはクリュセスに陣営から去るよう命じる
- [6] 24 sed negat Atrides Chrysenque excedere castris
  - Atrides (Atrides (Agamemno); アトリデス（アガメムノン）): -es 24. 510(?) 663
  - Chrysen (Chryses; クリュセス): -en 24

25 despecta pietate iubet: ferus ossibus imis
- [2] 25 Despecta pietate jubet : ferus ossibus imis
- [3] 25 Despecta pietate iubet; ferus ossibus imis
- [4] 25 Despecta pietate jubet ; ferus ossibus imis
- [6] 25 despecta pietate iubet; ferus ossibus imis

26 haeret amor spernitque preces damnosa libido.
- [2] 26 Haeret amor, spernitque preces damnosa libido.
  - … 高名な P・ボンダムには、これが Ovid. Heroid. IV, 70: « Acer in extremis ossibus haesit amor » から写されたものと思われ、オウィディウスは Metam. III, 395 でも « Sed tamen haeret amor » と言っている。――*Damnosa libido*（身を滅ぼす情欲）は Horat. Epist. II, 1, 107 に由来する。
- [3] 26 Haeret amor, spernitque preces damnosa libido.
- [4] 26 Haeret amor, spernitque preces damnosa libido.
- [6] 26 haeret amor spernitque preces damnosa libido.

27 Contemptus repetit Phoebeia templa sacerdos
- [2] 27 Contemptus repetit Phoebeia templa sacerdos,-
- [3] 27 Contemptus repetit Phoebeia templa sacerdos
- [4] 27 Contemptus repetit Phoebeia templa sacerdos
  - Phoebeia (PHOEBEIUS; ポエブスの): Phoebeia templa:ポエブスの神殿
- [6] 27 contemptus repetit Phoebeia templa sacerdos
  - sacerdos (Chryses; クリュセス): sacerdos 27. 35
  - Phoebeia (Phoebeius; ポエブスの): Phoebeia templa 27

28 squalidaque infestis maerens secat unguibus ora
- [2] 28 Squalidaque infestis moerens secat unguibus ora,
  - *Secat unguibus ora*（爪で顔を引き裂く）。ボンダムはこれが Ovid. Her. V, 72: « Et secui madidas ungue rigente genas » に負うていると考え、オウィディウスはまた *squalida ora*（汚れやつれた顔）という表現を
  - **(cont.)** （前頁からの続き）Trist. IV, 2, 34 で用いている。以下、1012 行でも « arat unguibus ora » とある。
- [3] 28 Squalidaque infestis maerens secat unguibus ora
- [4] 28 Squalidaque infestis maerens secat unguibus ora
- [6] 28 squalidaque infestis maerens secat unguibus ora

29 dilaceratque comas annosaque tempora plangit.
- [2] 29 Dilaceratque coinas, annosaque pectora plangit.
- [3] 29 Dilaceratque comas annosaque pectora plangit.
- [4] 29 Dilaceratque comas annosaque pectora plangit.
- [6] 29 dilaceratque comas annosaque tempora plangit.
  - tempora … Φ 33 κεφαλήν を参照

30 Mox ubi depositi gemitus lacrimaeque quierunt,
- [2] 30 Mox ubi depositi gemitus, lacrymaeque quierunt,
- [3] 30 Mox ubi depositi gemitus lacrimaeque quierunt,
- [4] 30 Mox ubi depositi gemitus lacrimaeque quierunt,
- [6] 30 mox ubi depositi gemitus lacrimaeque quierunt,

31 Fatidici his sacras compellat uocibus aures:
- [2] 31 Fatidici sacras compellat vocibus aras :
  - … われらの作者は神々をその職能の名だけで呼ぶのが常であり、ユピテルを *rex*（王）、ウルカヌスを *ignipotens*（火を支配する者）、ミネルウァを *armigera*（武具を帯びる者）と呼ぶごときである。アポロが神託を下し、未来のことをあらかじめ予言して告げる（*fatur*）がゆえに *Fatidicus* の名が帰せられることは周知の通りである。オウィディウスは Fast. II, 262 および V, 626 でポエブスを明白にそう呼んでいる。またホラーティウスが Carm. I, 2, 32 でアポロに帰している *augur*（占い師）の名も同じことを意味している。…なぜなら君主や神々の「聖なる耳」に祈りを届けるというのは、とりわけラテン語の後代において一般的な言い回しだからである。カルプルニウス第 1 詩最終行に対するわれわれの注を参照のこと。またアポロには、祈る者たちに傾けられやすい耳が特に帰せられる。それゆえアポロに捧げられる祈りにおいては叫び声がとりわけ頻繁に現れ、ここホメロスの Κλῦθί μευ と同様に、ラテン人たちの間では *Audi Apollo*（聞きたまえ、アポロ）となる。Horat. Carm. Saec. v. 34 を見よ。それどころかスパルタ人たちの間ではアポロンが τετράωτος（四つの耳をもつ者）と呼ばれ、その神像が四つの耳を備えて作られていたことを、ジラルドゥスが『諸神の歴史論纂』(*Histor. Deor. Syntagm.*) VII の冒頭近くで注記している。
- [3] 31 Fatidici sacras compellat uocibus aras:
- [4] 31 Fatidici sacras compellat vocibus aures :
  - Fatidici (APOLLO; アポロ): Fatidicus Fatidici:クリュセスは予言の神の耳に言葉で呼びかける
- [6] 31 Fatidici his sacras compellat vocibus aures:
  - Fatidici (Fatidicus; 予言の): Fatidici . . . aures 31:アポロの

32 "Quid coluisse mihi tua numina, Delphice, prodest
- [2] 32 « Quid coluisse mihi tua numina, Delphice , prodest ,
- [3] 32 'Quid coluisse mihi tua numina, Delphice, prodest
- [4] 32 « Quid coluisse mihi tua numina, Delphice, prodest
  - Delphice (APOLLO; アポロ): Delphicus Delphice(クリュセスが奪われた娘について嘆く)
- [6] 32 'quid coluisse mihi tua, Delphice, numina prodest
  - Delphice (Delphicus; デルポイの): Delphice 32:おおアポロよ

33 aut castam uitam multos duxisse per annos?
- [2] 33 Aut castam vitam multos duxisse per annos?
- [3] 33 Aut castam multos uitam duxisse per annos?
- [4] 33 Aut castam multos vitam duxisse per annos ?
- [6] 33 aut castam multos vitam duxisse per annos?

34 Quidue iuuat sacros posuisse altaribus ignes,
- [2] 34 Quidve juvat sacros posuisse altaribus ignes,
- [3] 34 Quidue iuuat sacros posuisse altaribus ignes,
- [4] 34 Quidve juvat sacros posuisse altaribus ignes,
- [6] 34 quidve iuvat sacros posuisse altaribus ignes,

35 si tuus externo iam spernor ab hoste sacerdos?
- [2] 35 Si tuus externo jam spernor ab hoste sacerdos?
- [3] 35 Si tuus externo iam spernor ab hoste sacerdos?
- [4] 35 Si tuus externo jam spernor ab hoste sacerdos ?
- [6] 35 si tuus externo iam spernor ab hoste sacerdos?
  - sacerdos (Chryses; クリュセス): sacerdos 27. 35

36 En, haec desertae redduntur dona senectae?
- [2] 36 En haec desertae redduntur dona senectae.
  - … なぜならこの語は老境にとってほぼ固有かつ最も慣用される語であり、娘の喪失が語られているこの箇所にきわめて適切だからである。――本叢書第 2 巻 263 頁のルケイウスの墓碑銘（*Epitaph. Luceii*）でも同様である: « Me desolatum, me desertum ac spoliatum Clamarem »。この箇所およびペトローニウス『内乱』(*Bellum civile*) 286 行に対するわれわれの注を参照のこと。パリ編者。
- [3] 36 En, haec desertae redduntur dona senectae?
- [4] 36 En, haec desertae redduntur dona senectae?
- [6] 36 en, haec desertae redduntur dona senectae?
  - senectae (Chryses; クリュセス): desertae . . . senectae 36

37 Si gratus tibi sum, sim te sub uindice tutus.
- [2] 37 Si gratus tibi sum, sim te sub judice tutus,
- [3] 37 Si gratus tibi sum, sim te sub uindice tutus.
- [4] 37 Si gratus tibi sum, sim te sub vindice tutus.
- [6] 37 si gratus tibi sum, sim te sub vindice tutus.

38 Aut si qua, ut luerem sub acerbo crimine poenas,
- [2] 38 Aut si quam ut luerem sub acerbo crimine poenam
  - … なお、作者がこの行および続く 3 行で書いた内容について、バルトは『雑考』(*Advers.*) LVIII, 14 で、きわめて美しく、より良き時代にふさわしいものであり、才能の最高度の恵まれた発露を示していると評している。しかしボンダムとファン・デル・デュッセンがすでに指摘したように、彼がこれらの中で Ovid. Met. II, 279 におけるパエトーンの大火の際のテルス（大地）のユピテルへの嘆きを念頭に置き、模倣したことも明白である: « Si placet hoc meruique, quid o tua fulmina cessant, Summe Deum? liceat periturae viribus ignis Igne perire tuo, clademque auctore levare »。
- [3] 38 Aut si qua, ut luerem sub acerbo crimine poenam,
- [4] 38 Aut si qua, ut luerem sub acerbo crimine poenam,
- [6] 38 aut si qua, ut luerem sub acerbo crimine poenas,

39 inscius admisi, cur o tua dextera cessat?
- [2] 39 Inscius admisi, cur o tua dextera cessat?
- [3] 39 Inscius admisi, cur o tua dextera cessat?
- [4] 39 Inscius admisi, cur o tua dextera cessat?
- [6] 39 inscius admisi, cur o tua dextera cessat?

40 Posce sacros arcus, in me tua derige tela:
- [2] 40 Posce sacros arcus ; in me tua dirige tela :
  - *Posce sacros arcus*（聖なる弓を求めよ）。コロイボスのアポロに対する同様の演説が Stat. Theb. I, 651 に見られる: « Quid meruere Argi? me me, Divum optime, solum Objecisse caput fatis praestabit »；また 658 行: « Proinde move pharetras, arcusque intende sonoros, Insignemque animam leto demitte »。
- [3] 40 Posce sacros arcus, in me tua derige tela:
- [4] 40 Posce sacros arcus, in me tua derige tela :
- [6] 40 posco sacros arcus: in me tua derige tela;

41 auctor mortis erit certe deus. Ecce, merentem
- [2] 41 Auctor mortis eris certe Deus : ecce merentem
- [3] 41 Auctor mortis erit certe deus. ecce merentem
- [4] 41 Auctor mortis erit certe deus. Ecce merentem
- [6] 41 auctor mortis erit certe deus. ecce merentem

42 fige patrem; cur nata luit peccata parentis
- [2] 42 Fige patrem : cur nata luit peccata parentis,
- [3] 42 Fige patrem: cur nata luit peccata parentis
- [4] 42 Fige patrem : cur nata luit peccata parentis
- [6] 42 fige patrem: cur nata luit peccata parentis
  - nata (Chryseis; クリュセイス): nata 21. 42
  - patrem (Chryses; クリュセス): patrem 42

43 atque hostis duri patitur miseranda cubile?."
- [2] 43 Atque hostis duri patitur miseranda cubile?»
  - *Patitur miseranda cubile*（哀れにも閨を耐え忍んでいる）。同様に Virg. Georg. III, 60 に *pati hymenaeos*、Ovid. Art. Am. III, 766 に *pati concubitus*、同 Art. Am. III, 486 に *pati servitium* とある。――そしてわれらの作者は、おそらくホメロスが Iliad. XVIII, 433 で καὶ ἔτλην ἀνέρος εὐνήν と言っているのを表現しようとしたのであろう。パリ編者。
- [3] 43 Atque hostis duri patitur miseranda cubile?'
- [4] 43 Atque hostis duri patitur miseranda cubile ? »
- [6] 43 atque hostis duri patitur miseranda cubile?'
  - hostis (Agamemnon; アガメムノン): hostis duri 43

44 Dixerat. Ille sui uatis prece motus acerbis
- [2] 44 Dixerat. Ille sui vatis prece motus, acerbis
- [3] 44 Dixit; at ille sui uatis prece motus acerbis
- [4] 44 Dixit; at ille sui vatis prece motus acerbis
- [6] 44 dixerat. ille sui motus prece vatis acerbis
  - vatis (Chryses; クリュセス): vatis 44

45 luctibus infestat Danaos pestemque per omnes
- [2] 45 Luctibus infestat Danaos , pestemque per omnes
  - *Luctibus infestat Danaos*（嘆きをもってダナオイを苦しめる）。すなわち、悩ます（*vexat*）、荒廃させる（*desolatur*）の意。またしばしば *infestare* は敵意を向ける、悩ます（*infestum facere*）の意味でも用いられる。Sil. Ital. II, 277: « Ductorem infestans odiis »。パリ編者。
- [3] 45 Luctibus infestat Danaos pestemque per omnes
- [4] 45 Luctibus infestat Danaos pestemque per omnes
  - Danaos (GRAI; ギリシア人): Danaos:アポロはダナオイを悲しみで苦しめる
- [6] 45 luctibus infestat Danaos pestemque per omnes
  - Danaos (Danai; ダナオイ): -os 45. 492. 659. 808. 912. 950. 1001

46 immittit populos: uulgus ruit undique Graium
- [2] 46 Immittit populos : vulgus ruit undique Graium,
  - *Vulgus ruit undique*（民衆は至る所で斃れる）。すなわち、倒れる、死んで斃れるの意。Seneca, Oedipi v. 53: « sed omnis aetas pariter et sexus ruit » と同様である。バルトは前掲箇所で、この殺戮の描写が詩的で機知に富んでいる（*argutam*）ことを認めている。しかしボンダムとファン・デル・デュッセンは、同じバルトとともに、これがオウィディウスに負うていることを認めている。実際 Ovid. Metam. VII, 611 にこうある: « Qui lacryment, desunt, indefletaeque vagantur Natarum matrumque animae, juvenesque senesque. Nec locus in tumulos, nec sufficit arbor in ignes »。アッティカの疫病について述べる Manilius, lib. I, 883 seqq. や、テーバイの殺戮について述べるセネカの『オイディプース』第 1 幕 37 行以下（これもオウィディウスの箇所ときわめてよく似ている）を付け加えることができる。
- [3] 46 Inmittit populos: uulgus ruit undique Graium,
- [4] 46 Immittit populos : vulgus ruit undique Grajum,
  - Grajum (GRAI; ギリシア人): Grajum:ギリシア人の群れが四方から押し寄せる
- [6] 46 immittit populos: vulgus ruit undique Graium
  - Graium (Graius; ギリシアの): vulgus . . . Graium 46

47 uixque rogis superest tellus, uix ignibus aer,
- [2] 47 Vixque rogis superest tellus, vix ignibus arbor:
  - … その中でもセネカの Oed. v. 68 の次の箇所が、われらの作者の言葉にきわめてよく適合している: « Pars quota in cineres abit? Deest terra tumulis: jam rogos silvae negant »。
- [3] 47 Vixque rogis superest tellus, uix ignibus arbor,
- [4] 47 Vixque rogis superest tellus, vix ignibus arbor,
  - arbor …（オウィディウス『変身物語』VII, 613 を参照）…
- [6] 47 vixque rogis superest tellus, vix ignibus aer;

48 deerat ager tumulis. Iam noctis sidera nonae
- [2] 48 Deerat ager tumulis : jam noctis sidera nonae
- [3] 48 Derat ager tumulis. iam noctis sidera nonae
- [4] 48 Deerat ager tumulis. Jam noctis sidera nonae
- [6] 48 deerat ager tumulis. iam noctis sidera nonae

49 transierant decimusque dies patefecerat orbem,
- [2] 49 Transierant, decimusque dies patefecerat orbem;
  - *Patefecerat orbem*（世界を照らし出した）。これもバルトの指摘どおり、Ovid. Metam. IX, 794: « Postera lux radiis latum patefecerat orbem » から取られている。
- [3] 49 Transierant decimusque dies patefecerat orbem,
- [4] 49 Transierant decimusque dies patefacerat orbem,
- [6] 49 transierant decimusque dies patefecerat orbem,

50 cum Danaum proceres in coetum clarus Achilles
- [2] 50 Tunc Danaum proceres in coetum clarus Achilles
- [3] 50 Cum Danaum proceres in coetum clarus Achilles
- [4] 50 Cum Danaum proceres in coetum clarus Achilles
  - Achilles (ACHILLES; アキレウス): — 名高く、カルカスが疫病の原因を明かすよう、ギリシアの将たちを呼び集める
  - Danaum (GRAI; ギリシア人): — アキレウスはダナオイの首領たちを集会に呼び集める
- [6] 50 cum Danaum proceres in coetum clarus Achilles
  - Achilles (Achilles; アキレウス): clarus -es 50
  - Danaum (Danai; ダナオイ): -um(属格):19. 50. 67. 124. 153. 251. 268. 357. 389. 496. 631. 686. 691. 698. 705. 743. 747. 794. 1025

51 conuocat et causas hortatur pestis iniquae
- [2] 51 Convocat, et caussas hortatur pestis iniquae
- [3] 51 Conuocat et causas hortatur pestis iniquae
- [4] 51 Convocat et causas hortatur pestis iniquae
- [6] 51 convocat et causas hortatur pestis iniquae

52 edere Thestoriden. Tunc Calchas numina diuum
- [2] 52 Edere Thestoridem. Tunc Calchas numina Divum
- [3] 52 Edere Thestoriden. tunc Calchas numina diuum
- [4] 52 Edere Thestoriden. Tunc Calchas numina divum
  - Calchas (CALCHAS; カルカス): 神々の神意を問う
  - Thestoriden (CALCHAS; カルカス): Thestorides Thestoriden:アキレウスはテストルの子に疫病の原因を述べるよう促す
- [6] 52 edere Thestoriden. tunc Calchas numina divum
  - Calchas (Calchas; カルカス): 予言者カルカス:52. 152
  - Thestoriden (Thestorides; テストリデス): Thestoriden 52. 59:カルカス

53 consulit et causam pariter finemque malorum
- [2] 53 Consulit,et caussas pariter finemque malorum
- [3] 53 Consulit et causam pariter finemque malorum
- [4] 53 Consulit et causam pariter finemque malorum
- [6] 53 consulit et causam pariter finemque malorum

54 inuenit effarique uerens ope tutus Achillis
- [2] 54 Invenit, effarique verens , ope tutus Achillis
- [3] 54 Inuenit; effarique uerens ope tutus Achillis
- [4] 54 Invenit, effarique verens ope tutus Achillis
  - Achillis (ACHILLES; アキレウス): Achillis:彼の庇護のもとで安全に、カルカスは疫病の原因を明かす
- [6] 54 invenit effarique verens ope tutus Achillis
  - Achillis (Achilles; アキレウス): -is 54. 689. 719. 806

55 haec ait: "Infesti placemus numina Phoebi
- [2] 55 Haec ait : « Infesti placetnus numina Phoebi ,
- [3] 55 Haec ait: 'infesti placemus numina Phoebi
- [4] 55 Haec ait : « Infesti placemus numina Phoebi
  - Phoebi (APOLLO; アポロ): Phoebi:敵意あるポエブスの神威を宥めよう(カルカスが語る)
- [6] 55 haec ait 'infesti placemus numina Phoebi
  - Phoebi (Phoebus; ポエブス): infesti . . . numina Phoebi 55. 68

56 reddamusque pio castam Chryseida patri,
- [2] 56 Reddamusque pio castam Chryseida patri,
- [3] 56 Reddamusque pio castam Chryseida patri,
- [4] 56 Reddamusque pio castam Chryseida patri,
  - Chryseida (CHRYSEIS; クリュセイス): — 彼女を貞潔なまま父に返そう(カルカスが語る)
- [6] 56 reddamusque pio castam Chryseida patri,
  - Chryseida (Chryseis; クリュセイス): -da 23. 56. 64
  - patri (Chryses; クリュセス): pio . . . patri 56. 64

57 si uolumus, Danai, portus intrare salutis."
- [2] 57 Si volumus Danai portus intrare salutis ».
  - *Portus intrare salutis*（救いの港に入る）。これらの言葉についてバルトは言う：「疫病から解放されるという意味で *portum salutis intrare* と言ったのは、ある種の時代の退廃によるものであり、この箇所では主要な大詩人（*majorum gentium vates*）であれば確かに別の書き方をしたであろう」。「しかし私は、作者がその
  - **(cont.)** （前頁からの続き）語句を適切に用いたか否かについては論争しないが、この語句自体は擁護することができる。*intrare portum*（港に入る）が十分に優れており一般的であることは誰も否定しないであろうし、ウェルギリウスもオウィディウスもこれを用いている。また *portus salutis*（救いの港）も同じオウィディウスに由来し、彼は Rem. amoris, v. 610 でこう述べている: « Inque suae portu poene salutis erat »」。
- [3] 57 Si uolumus Danai portus intrare salutis'.
- [4] 57 Si volumus Danai portus intrare salutis ».
  - Danai (DANAUS; ダナオイの): 形容詞:Danai salutis
- [6] 57 si volumus, Danai, portus intrare salutis'.
  - Danai (Danai; ダナオイ): 呼格:57

58 Dixerat. Exarsit subito uiolentia regis:
- [2] 58 Dixerat, exarsit subito violentia regis.
- [3] 58 Dixerat; exarsit subito uiolentia regis:
- [4] 58 Dixerat; exarsit subito violentia regis;
- [6] 58 dixerat; exarsit subito violentia regis:
  - regis (Agamemnon; アガメムノン): rex 58. 134. 691

59 Thestoriden dictis primum compellat amaris
- [2] 59 Thestoridem dictis primum compellat amaris,
- [3] 59 Thestoriden dictis primum compellat amaris
- [4] 59 Thestoriden dictis primum compellat amaris
  - Thestoriden (CALCHAS; カルカス): — アガメムノンは苦い言葉で彼を責める
- [6] 59 Thestoriden dictis primum compellat amaris
  - Thestoriden (Thestorides; テストリデス): Thestoriden 52. 59:カルカス

60 mendacemque uocat. Tum magnum incusat Achillem
- [2] 60 Mendacemque vocat, magnumque incusat Achillem,
- [3] 60 Mendacemque uocat; tum magnum incusat Achillem
- [4] 60 Mendacemque vocat; tum magnum incusat Achillem
  - Achillem (ACHILLES; アキレウス): Achillem:アガメムノンは偉大なアキレウスを咎める
- [6] 60 mendacemque vocat; tum magnum incusat Achillem
  - Achillem (Achilles; アキレウス): magnum . . . -em 60. 72. 934

61 inque uicem ducis inuicti conuicia suffert.
- [2] 61 Inque vicem ducis invicti convicia sufFert.
  - *Convicia suffert*（罵詈雑言に耐える）。下の 104 行および 537 行と比較せよ。
- [3] 61 Inque uicem ducis inuicti conuicia suffert.
- [4] 61 Inque vicem ducis invicti convicia suffert.
- [6] 61 inque vicem ducis invicti convicia suffert.
  - ducis (Achilles; アキレウス): ducis invicti 61

62 Confremuere omnes. Tandem clamore represso
- [2] 62 Confremuere omnes : tandem clamore represso
  - *Confremuere omnes*（一同はざわめいた）。名高いボンダムは、これがオウィディウスの Met. I, 199 の半詩行（ヘミスティキオン）であると指摘している。
- [3] 62 Confremuere omnes. tandem clamore represso
- [4] 62 Confremuere omnes. Tandem clamore represso
- [6] 62 confremuere omnes: tandem clamore represso

63 cogitur inuitos aeger dimittere amores
- [2] 63 Cogitur invitos aeger dimittere amores,
  - … 流布本が持つ *invitos amores*（不本意な愛）が正しい。なぜならクリュセイスは不本意ながらアガメムノンのもとにいたのであり、ここで彼が彼女を痛心して（*aeger*）解放すると言われているからである。Propert. III, 20, 30: « Atridae magno quum stetit alter amor »。
- [3] 63 Cogitur inuisos aeger dismittere amores
- [4] 63 Cogitur invictos aeger dimittere amores
- [6] 63 cogitur invitos aeger dimittere amores
  - inuitos … 〜と解せよ: 王を愛していなかった女; amores はクリュセイス自身を指す
  - amores (Chryseis; クリュセイス): invitos . . . amores 63

64 intactamque pio reddit Chryseida patri
- [2] 64 Intactamque pio reddit Chryseida patri ,
- [3] 64 Intactamque pio reddit Chryseida patri,
- [4] 64 Intactamque pio reddit Chryseida patri,
  - Chryseida (CHRYSEIS; クリュセイス): — アガメムノンは彼女を手つかずのまま父に返す
- [6] 64 intactamque pio reddit Chryseida patri
  - Chryseida (Chryseis; クリュセイス): -da 23. 56. 64
  - patri (Chryses; クリュセス): pio . . . patri 56. 64

65 multaque dona super. Quam cunctis notus Vlixes
- [2] 65 Multaque dona super : quam cunctis notus Ulysses
  - … ――*Cunctis notus Ulysses*（万人に知られたオデュッセウス）。…ギリシア語ではオデュッセウスは πολύμητις（多くの計略をもつ者）と呼ばれる。要約（エピトメー）の作者はこの語を、あたかも多くの人々の口の端に上る者、あるいは多くの物語が語られる者を意味する πολύμυθος や πολύμνητος であるかのように理解し、その結果 *cunctis notus*（万人に知られた）と解釈したように思われる。
- [3] 65 Multaque dona super; quam cunctis notus Ulixes
- [4] 65 Multaque dona super; quam cunctis notus Ulixes
  - Ulixes (ULIXES; ウリクセス): 皆に知られた者、クリュセイスを祖国に連れ帰る
- [6] 65 multaque dona super; quam cunctis notus Vlixes
  - Vlixes (Vlixes; ウリクセス): cunctis notus -es 65

66 impositam puppi patrias deuexit ad arces
- [2] 66 Impositam puppi patrias devexit ad arces,
- [3] 66 Inpositam puppi patrias deuexit ad arces
- [4] 66 Impositam puppi patrias devexit ad arces
- [6] 66 impositam puppi patrias devexit ad arces
  - arces (Chryse; クリュセ): (都市クリュセ)patrias ad arces 66

67 atque iterum ad classes Danaum sua uela retorsit.
- [2] 67 Atque iterum ad classes Danaum sua vela retorsit.
  - *Sua vela retorsit*（その帆を折り返した）。Ovid. Trist. I, 1, 84: « Semper ab Euboicis vela retorquet aquis »。
- [3] 67 Atque iterum ad Danaum classes sua uela retorsit.
- [4] 67 Atque iterum ad Danaum classes sua vela retorsit.
  - Danaum (GRAI; ギリシア人): — クリュセイスが父に返されると、ウリクセスはダナオイの艦隊に戻る
- [6] 67 atque iterum ad Danaum classes sua vela retorsit.
  - Danaum (Danai; ダナオイ): -um(属格):19. 50. 67. 124. 153. 251. 268. 357. 389. 496. 631. 686. 691. 698. 705. 743. 747. 794. 1025

68 Protinus infesti placantur numina Phoebi
- [2] 68 Protinus infesti placantur numina Phoebi,
- [3] 68 Protinus infesti placantur numina Phoebi.
- [4] 68 Protinus infesti placantur numina Phoebi.
  - Phoebi (APOLLO; アポロ): — クリュセイスが父に返されると、神威が宥められる
- [6] 68 protinus infesti placantur numina Phoebi
  - Phoebi (Phoebus; ポエブス): infesti . . . numina Phoebi 55. 68

69 et prope consumptae uires redduntur Achiuis.
- [2] 69 Et prope consumptae vires redduntur Achivis.
- [3] —
- [4] 69 below Et prope consumptae vires redduntur Achivis
  - Achivis (GRAI; ギリシア人): Achivis:[アカイア人に力が戻される]
- [6] 69 et prope consumptae vires redduntur Achivis.
  - Achivis (Achivi; アカイア人): -is 69. 387

70 Non tamen Atridae Chryseidis excidit ardor:
- [2] 70 Non tamen Atridae Chryseidis excidit ardor :
- [3] 69 Non tamen Atridae Chryseidis excidit ardor:
- [4] 70 Non tamen Atridae Chryseidis excidit ardor
  - Atridae (AGAMEMNON; アガメムノン): Atridae 与格:クリュセイスへの熱情が彼から去らない
  - Chryseidis (CHRYSEIS; クリュセイス): Chryseidis:クリュセイスへの熱情がアガメムノンから去らない
- [6] 70 non tamen Atridae Chryseidos excidit ardor:
  - Atridae (Atrides (Agamemno); アトリデス（アガメムノン）): -dae 与格:(一部の写本では -di)70
  - Chryseidos (Chryseis; クリュセイス): -dos (-dis trad.) . . . ardor 70

71 maeret et amissos deceptus luget amores.
- [2] 71 Moeret , et amissos deceptus luget amores.
- [3] 70 Maeret et amissos deceptus luget amores.
- [4] 71 Maeret, et amissos deceptus luget amores.
- [6] 71 maeret et amissos deceptus luget amores.
  - amores (Chryseis; クリュセイス): amissos . . . amores 71

72 Mox rapta magnum Briseide priuat Achillem
- [2] 72 Mox rapta magnum Briseide privat Achillem ,
- [3] 71 Mox rapta magnum Briseide priuat Achillem
- [4] 72 Mox rapta magnum Briseide privat Achillem
  - Achillem (ACHILLES; アキレウス): — 同じ者が偉大なアキレウスからブリセイスを奪う
  - Briseide (BRISEIS; ブリセイス): Briseide:アガメムノンはアキレウスからブリセイスを奪う
- [6] 72 mox rapta magnum Briseide privat Achillem
  - Achillem (Achilles; アキレウス): magnum . . . -em 60. 72. 934
  - Briseide (Briseis; ブリセイス): -ide privat Achillem 72

73 solaturque suos alienis ignibus ignes.
- [2] 73 Solaturque suos alienis ignibus ignes.
  - *Ignibus ignes*（火をもって火を）。Ovid. Trist. IV, 3, 65: « compescuit ignibus ignes » と同様。同様の趣旨で Val. Flaccus, II, 151（ハインシウスの校訂による）: « Attamen hos aliis forsan solabere casus Tu thalamis »。Quintilianus, Declam. II, 3: « Hoc juveni fuit consilium, ut pater, cui matrimonium filiumque abstulerat incendium, residua senectutis alia solaretur uxore »。
- [3] 72 Solaturque suos alienis ignibus ignes.
- [4] 73 Solaturque suos alienis ignibus ignes.
- [6] 73 solaturque suos alienis ignibus ignes.

74 At ferus Aeacides nudato protinus ense
- [2] 74 At ferus Aeacides nudato protinus ense
- [3] 73 At ferus Aeacides nudato protinus ense
- [4] 74 At ferus Aeacides nudato protinus ense
  - Aeacides (ACHILLES; アキレウス): Aeacides:猛々しく、抜き身の剣でアガメムノンに向かう
- [6] 74 at ferus Aeacides nudato protinus ense
  - Aeacides (Aeacides (Achilles); アエアキデス（アキレウス）): ferus -es 74. [844]

75 tendit in Atriden et, ni sibi reddat honestae
- [2] 75 Tendit in Atriden , cui , ni sibi reddat honestae
- [3] 74 Tendit in Atriden et, ni sibi reddat honestae
- [4] 75 Tendit in Atriden et, ni sibi reddat honestae
  - Atriden (AGAMEMNON; アガメムノン): In Atriden:アキレウスはアトレウスの子に向かう
- [6] 75 tendit in Atriden et, ni sibi reddat honestae
  - Atriden (Atrides (Agamemno); アトリデス（アガメムノン）): -dēn 75

76 munera militiae, letum crudele minatur,
- [2] 76 Munera militiae , letum crudele minatur.
  - *Munera militiae*（兵役の贈り物）。*praemia*（褒賞）と言ったほうがより適切であっただろう。というのも、彼は戦利品や鹵獲物のように、戦争の褒賞としてアキレウスのものとなったブリセイスを意味しているからである。
- [3] 75 Munera militiae, letum crudele minatur;
- [4] 76 Munera militiae, letum crudele minatur;
- [6] 76 munera militiae, letum crudele minatur
  - munera (Briseis; ブリセイス): munera militiae 76 を参照

77 nec minus ille parat contra defendere se ense.
- [2] 77 Nec minus ille parat contra defendere sese,
- [3] 76 Nec minus ille parat contra defendere sese.
- [4] 77 Nec minus ille parat contra defendere sese.
- [6] 77 nec minus ille parat contra defendere se ense.

78 Quod nisi casta manu Pallas tenuisset Achillem,
- [2] 78 Et nisi casta manu Pallas tenuisset Achillem,
  - *Et nisi casta manu*（そして貞淑な女神がその手で…でなかったなら）。要約（エピトメー）の作者は、ホメロスが保っていた事象の順序と叙述を少し変更している。ホメロスは、ブリセイスがアキレウスから奪い去られる前に、アキレウスがアガメムノンに対して剣を抜こうとしてミネルウァに制止されたと物語る。われらの作者はその衝突について、あたかもブリセイスが連れ去られた後に生じたかのように語っている。
- [3] 77 Quod nisi casta manu Pallas tenuisset Achillem,
- [4] 78 Quod nisi casta manu Pallas tenuisset Achillem.
  - Achillem (ACHILLES; アキレウス): — パラスは、アキレウスが剣でアガメムノンに向かわぬよう、手で押さえる
  - Pallas (MINERVA; ミネルウァ): Pallas 主格:貞潔な女神は、アキレウスが剣でアガメムノンに向かわぬよう手で押さえる
- [6] 78 quod nisi casta manu Pallas tenuisset Achillem,
  - Achillem (Achilles; アキレウス): -em 78
  - Pallas (Pallas; パラス): casta . . . -as 78

79 turpem caecus amor famam liquisset in aeuum
- [2] 79 Turpem caecus amor famam liquisset in aevum
  - *Turpem caecus amor famam*（盲目の愛が…恥ずべき評判を）。これはホメロスの趣旨や古代の英雄たちの気風に適った発言とは思われない。彼らは少女のゆえに愛の激情によって武器をとることを決して恥ずべきこととは考えなかった。しかし作者は、パラスから警告を受けたアキレウスが、自分は少女のためには決して手ずから戦わないと言明する 298 行の言葉からこの発言の根拠を引き出したように思われる：Χερσὶ μὲν οὔτι ἔγωγε μαχήσομαι εἵνεκα κούρης。
- [3] 78 Turpem caecus amor famam liquisset in aeuum
- [4] 79 Turpem caecus amor famam liquisset in aevum
- [6] 79 turpem caecus amor famam liquisset in aevum

80 gentibus Argolicis. Contempta uoce minisque
- [2] 80 Gentibus Argolicis : contentus voce minisque ,
  - … すなわち、アキレウスは（ミネルウァが彼に命じたように）手や刃によってではなく、声と罵倒と脅迫によってアガメムノーンと争ったことに満足し、自身に加えられた不正に対する復讐を母に求めるのである。
- [3] 79 Gentibus Argolicis. contempta uoce minisque
- [4] 80 Gentibus Argolicis. Contenta voce minisque
  - Argolicis (ARGOLICUS; アルゴスの): Argolicis gentibus
  - Argolicis (GRAI; ギリシア人): Argolicae gentes gentibus Argolicis:アキレウスの恋はアルゴスの民の間に恥ずべき名を残したであろう
- [6] 80 gentibus Argolicis. contenta voce minisque
  - Argolicis (Argolicus; アルゴスの): gentibus -is 80

80a
- [2] —
- [3] 80 . . . . . . . . . . . . . . . . . . . .
- [4] —
- [6] —

81 inuocat aequoreae Pelides numina matris
- [2] 81 Invocat aequorese Pelides numina matris ,
- [3] 81 Inuocat aequoreae Pelides numina matris,
- [4] 81 Invocat aequoreae Pelides numina matris,
  - Pelides (ACHILLES; アキレウス): Pelides:母の神威に呼びかける
- [6] 81 invocat aequoreae Pelides numina matris,
  - Pelides (Pelides; ペリデス): Pelides 81
  - numina (Thetis; テティス): aequoreae . . . numina matris 81 を参照

82 ne se Plistheniden contra patiatur inultum.
- [2] 82 Ne se plus contra Atridem patiatur inultum.
  - … バルトは『雑考』(*Advers.*) 2753 頁でこの詩行について、*plus* がプラウトゥス、クラウディアヌス、シドニウス、アプレイウス他にあるように *amplius*（もはや／さらに多く）を意味すると注記しているが、…
- [3] 82 Ne se Plistheniden contra patiatur inultum.
- [4] 82 Ne se plus, populis coram, patiatur inultum.
- [6] 82 ne se Plistheniden contra patiatur inultum.

83 At Thetis audita nati prece deserit undas
- [2] 83 At Thetis, audita nati prece, deserit undas,
- [3] 83 At Thetis audita nati prece deserit undas
- [4] 83 At Thetis audita nati prece deserit undas
  - Thetis (THETIS; テティス): アキレウスの祈りを聞く
- [6] 83 at Thetis audita nati prece deserit undas
  - nati (Achilles; アキレウス): nati 83. 88. 95
  - Thetis (Thetis; テティス): Thetis 83. 860

84 castraque Myrmidonum iuxta petit et monet armis
- [2] 84 Castraque Myrmidonum praetervolat, inde per auras
- [3] 84 Castraque Myrmidonum iuxta petit et monet, armis
- [4] 84 Castraque Myrmidonum juxta petit et monet, armis
  - Myrmidonum (MYRMIDONES; ミュルミドン): Myrmidonum:テティスはミュルミドンの陣営を目指す
- [6] 84 castraque Myrmidonum iuxta petit et monet, armis
  - Myrmidonum (Myrmidones; ミュルミドン): -um 84

85 abstineat dextram ac congressibus; inde per auras
- [2] —
- [3] 85 Abstineat dextra, e congressuque inde per auras
- [4] 85 Abstineat dextra, gressuque exinde per auras
- [6] 85 abstineat dextram ac congressibus: inde per auras

86 emicat aetherias et in aurea sidera fertur.
- [2] 85 Emicat aethereas, et in aurea sidera fertur;
- [3] 86 Emicat aethereas et in aurea sidera fertur.
- [4] 86 Emicat aethereas et in aurea sidera fertur.
- [6] 86 emicat aethereas et in aurea sidera fertur.

87 Tunc genibus regis sparsis affusa capillis:
- [2] 86 Tunc genibus regis sparsis affusa capillis:
  - … ここでわれらの作者は、娘プロセルピナのためにユピテルに嘆願するケーレースについて語るオウィディウスの Met. V, 513 を明白に模倣している: « Ante Jovem passis stetit invidiosa capillis, Proque meo venio supplex tibi, Jupiter, inquit, Sanguine, proque tuo。
- [3] 87 Tunc genibus regis sparsis affusa capillis
- [4] 87 Tunc genibus regis sparsis affusa capillis :
- [6] 87 tunc genibus regis sparsis affusa capillis
  - regis (Iuppiter; ユピテル): regis 87

88 "Pro nato ueni genetrix en ad tua supplex
- [2] 87 c( Pro nato veni genitrix en ad tua supplex
- [3] 88 'Pro nato ueni genetrix en ad tua supplex
- [4] 88 « Pro nato venio genetrix, en, ad tua supplex
  - … 『アエネーイス』VIII, 382 および『変身物語』V, 514 を参照）。
- [6] 88 'pro nato veni genetrix en ad tua supplex
  - nato (Achilles; アキレウス): nati 83. 88. 95
  - genetrix (Thetis; テティス): genetrix 88

89 numina, summe parens; ulciscere meque meumque
- [2] 88 Numina , suiome parens : ulciscere meque meumque
- [3] 89 Numina, summe parens! ulciscere meque meumque
- [4] 89 Numina, summe parens! ulciscere meque meumque
- [6] 89 numina, summe parens: ulciscere meque meumque
  - parens (Iuppiter; ユピテル): summe parens 89

90 corpus ab Atrida, quodsi permittitur illi
- [2] 89 Corpus ab Atride : quod si permittitur illi ,
  - … バルトが前掲箇所で指摘するように、テティスは息子アキレウスを自身の肉体（*corpus suum*）と呼んでおり、これは作者による斬新な表現であって、他の詩人には容易に見出せないものだと私は考える。子供たちが親の *viscera*（内臓／肉親）や *sanguis*（血）と呼ばれるのは一般的である。
- [3] 90 Pignus ab Atrida. quodsi permittitur illi,
- [4] 90 Pignus ab Atrida; quodsi permittitur illi,
  - Atrida (AGAMEMNON; アガメムノン): Ab Atrida:テティスは、ユピテルが自分と息子のためにアトレウスの子に報復してくれるよう祈る
- [6] 90 pignus ab Atrida. quodsi permittitur illi,
  - pignus (Achilles; アキレウス): meum . . . pignus 90
  - Atrida (Atrides (Agamemno); アトリデス（アガメムノン）): -dā 奪格:90

91 ut flammas impune mei uiolarit Achillis,
- [2] 90 Ut flammas impune mei violarit Achillis,
- [3] 91 Ut flammas inpune mei uiolarit Achillis,
- [4] 91 Ut flammas impune mei violarit Achillis,
  - Achillis (ACHILLES; アキレウス): — テティスは、アキレウスの愛がアガメムノンによって罰されずに踏みにじられたままにならぬよう、ユピテルに祈る
- [6] 91 ut flammas inpune mei violarit Achillis,
  - Achillis (Achilles; アキレウス): mei -is(テティスが語る)91

92 turpiter occiderit superata libidine uirtus."
- [2] 91 Turpiter occiderit superata libidine virtus».
  - … 作者はこの趣旨を自らの創意から付け加えている。ホメロスではテティスはそのようなことは語らない。他方で彼は、テティスがユピテルに何よりも求めたこと、そしてそれに続くユノーの詰問が念頭に置いていること、すなわちギリシア勢が
  - **(cont.)** （前頁からの続き）心を改め、彼女の息子に受けるべき名誉を回復するまで（許すよう求めたこと）。
- [3] 92 Turpiter occiderit superata libidine uirtus.'
- [4] 92 Turpiter occiderit superata libidine virtus. »
- [6] 92 turpiter occiderit superata libidine virtus.'

93 Iuppiter haec contra: "Tristes depone querelas,
- [2] 92 Jupiter huic contra : « Tristes depone querelas ,
- [3] 93 Iuppiter huic contra 'tristis depone querellas,
- [4] 93 Juppiter huic contra : « Tristes depone querellas,
  - Juppiter (JUPPITER; ユピテル): Juppiter:テティスに答える
- [6] 93 Iuppiter haec contra 'tristes depone querelas,
  - Iuppiter (Iuppiter; ユピテル): Iuppiter 93

94 magni diua maris, mecum labor iste manebit.
- [2] 93 Magni Diva maris , mecum labor iste manebit :
  - … すなわち、私はこの事を丹念に、たゆまず配慮するであろう、の意。Homer. v. 523: ἐμοὶ δέ κε ταῦτα μελήσεται, ὄφρα τελέσσω。――われらの作者は Virg. Aeneid. IV, 115: « Mecum erit iste labor » を模倣しており、同時に Virg. Aen. I, 256 におけるユピテルのウェヌスへの言葉 « Parce metu, Cytherea: manent immota tuorum Fata tibi »、あるいは Aen. I, 76 でアイオロスがユノーに述べた言葉 « tuus, o regina, quid optes, Explorare labor, mihi jussa capessere fas est » を念頭に置いていたように思われる。われらの作者の言葉と反対なのは、Virg. Aen. II, 595 の « quonam nostri tibi cura recessit » である。
- [3] 94 Magni diua maris, mecum labor iste manebit.
- [4] 94 Magni diva maris, mecum labor iste manebit.
  - diva (THETIS; テティス): ユピテルがテティスに呼びかけて「大いなる海の女神」という言葉を用いていることもここに加えよ
- [6] 94 magni diva maris, mecum labor iste manebit.
  - diva (Thetis; テティス): magni diva maris 94

95 Tu solare tui maerentia pectora nati."
- [2] 94 Tu solare tui moerehtia pectora nati».
- [3] 95 Tu solare tui maerentia pectora nati'.
- [4] 95 Tu solare tui maerentia pectora nati »
- [6] 95 tu solare tui maerentia pectora nati'.
  - nati (Achilles; アキレウス): nati 83. 88. 95

96 Dixit. At illa leues caeli delapsa per auras
- [2] 95 Dixit ; at illa leves caeli delapsa per auras
- [3] 96 Dixit; at illa leuis caeli delapsa per auras
- [4] 96 Dixit; at illa leves caeli delapsa per auras
- [6] 96 dixit, at illa leves caeli delapsa per auras
  - leues … ウェルギリウス『アエネーイス』11, 595 を参照

97 litus adit patrium gratasque sororibus undas.
- [2] 96 Litus adit patrium gratasque sororibus undas.
- [3] 97 Litus adit patrium gratasque sororibus undas.
- [4] 97 Litus adit patrium gratasque sororibus undas.
- [6] 97 litus adit patrium gratasque sororibus undas.
  - sororibus (Nereis; ネレイス): sororibus 97 を参照

98 Offensa est Iuno: "Tantum"que ait, "optime coniunx,
- [2] 97 Ofiensa est Juno, aTantumque, ait, optime conjux,
- [3] 98 Offensa est Iuno 'tantum'que ait, 'optime coniunx,
- [4] 98 Offensa est Juno : « Tantumque » ait « optime conjunx,
  - Juno (JUNO; ユノー): 気を損ねて
- [6] 98 offensa est Iuno 'tantum'que ait, 'optime coniunx,
  - Iuno (Iuno; ユノー): Iuno 98. 894
  - coniunx (Iuppiter; ユピテル): optime coniunx 98

99 Doride nata ualet, tantum debetur Achilli,
- [2] 98 Doride nata valet, tantum debetur Achilli,
  - … アントン・デ・ローイによってプロペルティウスが引用されている（第 1 巻 18, 25）: « At vos aequoreae formosa Doride natae, Candida felici solvite vela choro »。ドリスから生まれた娘たちとは、ウェルギリウスが Georg. IV, 341 で呼んでいるように、オーケアニデス（大洋の娘たち）のことである。バルトは『雑考』2753 頁でこう述べている：「しかしこのように、ユノーは自らもまたオーケアノスの娘であることを忘れて、罵倒としてテティスを愚かにもそのように呼んでいる。ホメロスは『イリアス』第 23 巻でオーケアノスについてこう書いている：Ὠκεανόν τε θεῶν γένεσιν καὶ μητέρα Τηθύν」。
- [3] 99 Doride nata ualet, tantum debetur Achilli,
- [4] 99 Doride nata valet, tantum debetur Achilli,
  - Achilli (ACHILLES; アキレウス): Achilli:彼にはそれほどのものが負われている(ユノーが語る)
  - Doride (THETIS; テティス): Doride nata:ドリスの娘はそれほどの力を持つ(ユノーがユピテルに呼びかける)
- [6] 99 Doride nata valet, tantum debetur Achilli,
  - Achilli (Achilles; アキレウス): -i 99
  - Doride (Doris; ドリス): -de nata 99

100 ut mihi quae coniunx dicor tua quaeque sororis
- [2] 99 Ut mihi, quse conjux dicor tua , quaeque sororis
  - *Ut mihi, quae conjux*（妻である私に対して…）。同様に Virg. Aen. I, 46 のユノー：« Ast ego, quae Divum incedo regina, Jovisque Et soror et conjux »。――そして同様の強調をもって、われらの卓越した詩人ラシーヌの『ブリタニクス』第 1 幕第 2 場 29 行：« Moi, fille, femme, soeur et mère de vos maîtres »。パリ編者。
- [3] 100 Ut mihi, quae coniunx dicor tua quaeque sororis
- [4] 100 Ut mihi, quae conjunx dicor tua quaeque sororis
- [6] 100 ut mihi, quae coniunx dicor tua quaeque sororis
  - coniunx (Iuno; ユノー): coniunx tua 100 を参照

101 dulce fero nomen, dilectos fundere Achiuos
- [2] 100 Dulce fero nomen, dilectos fundere Achivos,
- [3] 101 Dulce fero nomen, dilectos fundere Achiuos
- [4] 101 Dulce fero nomen, dilectos fundere Achivos
  - Achivos (GRAI; ギリシア人): Achivos:愛するアカイア人たち(怒ったユノーが言葉でユピテルを責める)
- [6] 101 dulce fero nomen, dilectos fundere Achivos
  - Achivos (Achivi; アカイア人): -os 101

102 et Troum renouare uelis in proelia uires?
- [2] 101 Et Troum renovare velis in praelia vires?
- [3] 102 Et Troum renouare uelis in praelia uires?
- [4] 102 Et Troum renovare velis in proelia vires ?
  - Troum (TROJANI; トロイア人): Troum:トロイア人の力を戦いのために新たにしようと望むのか(ユノーがユピテルに呼びかける)
- [6] 102 et Troum renovare velis in proelia vires?
  - Troum (Tros; トロイア人): Troum 102. 281. 339. 357. 438. 631. 641. 701. 963

103 Haec ita dona refers nobis? sic diligor a te?"
- [2] 102 Haec ita dona refers nobis? sic diligor a te? »
  - … なお、この発言の形式は Virg. Aen. I, 253 におけるウェヌスのユピテルへの言葉に明白に倣っている: « Hic pietatis honos? sic nos in sceptra reponis? »。
- [3] 103 Haec tu dona refers nobis? sic diligor a te?'
- [4] 103 Haec tu dona refers nobis? sic diligor a te? »
- [6] 103 haec ita dona refers nobis? sic diligor a te?'

104 Talibus incusat dictis irata Tonantem
- [2] 103 Talibus incusat dictis irata Tonantem ,
  - *Talibus incusat*（そのような言葉で非難する）：ウェルギリウスの Aen. I, 410 より。
- [3] 104 Talibus incusat dictis irata Tonantem
- [4] 104 Talibus incusat dictis irata Tonantem
  - Tonantem (JUPPITER; ユピテル): Tonantem:怒ったユノーが言葉で雷神を責める
- [6] 104 talibus incusat dictis irata Tonantem
  - Tonantem (Tonans; 雷神): -tem 104

105 inque uicem summi patitur conuicia regis.
- [2] 104 Inque vicem summi patitur convicia regis.
- [3] 105 Inque uicem summi patitur conuicia regis.
- [4] 105 Inque vicem summi patitur convicia regis.
- [6] 105 inque vicem summi patitur convicia regis.
  - regis (Iuppiter; ユピテル): summi . . . regis 6. 105

106 Tandem interposito lis Ignipotente resedit
- [2] 105 Tandem interposito lis Ignipotente resedit,
  - … ウルカヌスが理解される。なぜなら彼が諍いを起こしているユピテルとユノーの間に割って入り、激励し、多くの杯を勧めることによって両親を宥め、陽気さへと転じさせたからである。Hom. Iliad. I, 571: Τοῖσιν δ᾽ Ἥφαιστος κλυτοτέχνης ἦρχ᾽ ἀγορεύειν と同様である。ウルカヌスはわれらの作者や他の詩人たちによって *Ignipotens*（火の主）と呼ばれている。下の 867 行：« Illic Ignipotens mundi caelaverat axem »；また Virg. Aen. VIII, 414: « Haud secus Ignipotens, nec tempore segnior illo »。さらに Aen. X, 243 の « clypeum cape quem dedit ipse Invictum Ignipotens, etc. » を付け加えるべきである。パリ編者。
- [3] 106 Tandem interposito lis Ignipotente resedit,
- [4] 106 Tandem interposito lis Ignipotente resedit,
  - Ignipotente (VULCANUS; ウルカヌス): Ignipotente interposito:火の主が間に入ると、ユノーとユピテルの争いが収まる
- [6] 106 tandem interposito lis Ignipotente resedit
  - Ignipotente (Ignipotens; イグニポテンス): *-nte (omnipot- trad.) 106:ウルカヌス

107 conciliumque simul genitor dimittit Olympi.
- [2] 106 Conciliumque simul genitor dimittir ab aula.
- [3] 107 Conciliumque simul genitor dimittit ab aula;
- [4] 107 Conciliumque simul genitor dimittit [Olympo];
  - genitor (JUPPITER; ユピテル): Genitor:父が会議を解散する
  - Olympo (OLYMPUS; オリュンポス): [—]
- [6] 107 conciliumque simul genitor dimittit Olympi
  - genitor (Iuppiter; ユピテル): genitor . . . Olympi 107
  - Olympi (Olympus; オリュンポス): genitor . . . Olympi 107

108 Interea sol emenso decedit Olympo
- [2] 107 Interea sol immenso decedit Olympo,
- [3] 108 Interea sol emenso decedit Olympo,
- [4] 108 Interea sol emenso decedit Olympo.
  - Olympo (OLYMPUS; オリュンポス): Olympo emenso:オリュンポスを渡り終えて太陽が沈む
- [6] 108 interea sol emenso decedit Olympo:
  - Olympo (Olympus; オリュンポス): sol emenso decedit -po 108
  - sol (Sol; 太陽): Sol . . . decedit Olympo 108

109 et dapibus diui curant sua corpora largis;
- [2] 108 Et dapibus largis curant sua corpora Divi ,
  - … Virgil. Aen. III, 510: « passimque in litore sicco Corpora curamus »。
- [3] 109 Et dapibus diui curant sua corpora largis.
- [4] 109 Et dapibus divi curant sua corpora largis.
- [6] 109 et dapibus divi curant sua corpora largis.

110 inde petunt thalamos iucundaque dona quietis.
- [2] 109 Inde petunt thalamos jucundaque dona quietis.
  - *Dona quietis*（休息の賜物）。Virg. Aen. II, 369: « quies ... dono Divum gratissima serpit »。Ovid. Am. II, 9, 40: « et somnos praemia magna vocat »。Stat. Silv. V, 4, 2: « donis ut solus egerem, Somne, tuis »。
- [3] 110 Inde petunt thalamos iocundaque dona quietis.
- [4] 110 Inde petunt thalamos jocundaque dona quietis.
- [6] 110 inde petunt thalamos iucundaque dona quietis.

## Book 2

111 Nox erat et toto fulgebant sidera mundo
- [2] 110 II. Nox erat et toto fulgebant sidera caelo,
  - *Nox erat*（夜であった）。われらの作者は、夜に関するこのより簡潔な描写を、Virg. Aen. IV, 522 seqq. や VIII, 26 seq. が持つより詳細な描写から汲み取ることができたであろう。…
- [3] 111 Nox erat et toto fulgebant sidera mundo
- [4] 111 Nox erat et toto fulgebant sidera mundo
- [6] 111 nox erat et toto fulgebant sidera mundo
  - （証言） 『ベレンガリウスの事績』(*Gesta Berengarii*, PMA IV) 1, 127 を参照

112 humanumque genus requies diuumque tenebat,
- [2] 111 Humanumque genus requies Divumque tenebat;
- [3] 112 Humanumque genus requies diuumque tenebat,
- [4] 112 Humanumque genus requies divumque tenebat,
- [6] 112 humanumque genus requies divumque tenebat,

113 cum pater omnipotens Somnum uocat atque ita fatur:
- [2] 112 Tunc pater omnipotens Somnum vocat,atque ita fatur :
- [3] 113 Cum pater omnipotens somnum uocat atque ita fatur:
- [4] 113 Cum pater omnipotens somnum vocat atque ita fatur :
  - pater (JUPPITER; ユピテル): Pater 主格:全能の父がソムヌスを呼ぶ
- [6] 113 cum pater omnipotens Somnum vocat atque ita fatur:
  - pater (Iuppiter; ユピテル): pater omnipotens 113
  - Somnum (Somnus; ソムヌス): -um 113

114 "Vade age per tenues auras, lenissime diuum,
- [2] 113 « Vade, age, per tenues auras, lenissime Divum ,
  - *Vade, age*（行け、さあ）。バルトは前掲箇所で、これらが傑出しており最高の詩人に値するものとして称賛している。しかし作者にはここで模倣すべき古代の詩人たちの多くの箇所があった。とりわけアルキュオネーに送り込まれた夢に関するオウィディウスの Met. XI, 586 seqq.、およびオウィディウスを模倣したスタティウスの Theb. X, 84 seqq. である。――*Lenissime divum*（神々の中で最も穏やかなる者よ）。Ovid. Met. XI, 623: « placidissime, Somne, Deorum »。Stat. Silv. V, 4, 1: « placidissime Divum »、および Theb. X, 126: « mitissime Divum »。
- [3] 114 'Vade age per tenues auras, lenissime diuum,
- [4] 114 « Vade age per tenues auras, lenissime divum,
- [6] 114 'vade age per tenues auras, lenissime divum,
  - divum (Somnus; ソムヌス): lenissime divum 114 を参照

115 Argolicique ducis celeri pete castra uolatu
- [2] 114 Argolicique ducis celeri pete castra volatu,
- [3] 115 Argolicique ducis celeri pete castra uolatu;
- [4] 115 Argolicique ducis celeri pete castra volatu;
  - Argolici (AGAMEMNON; アガメムノン): Argolicus dux:「アルゴスの将の陣営へ飛んで行け」(ユピテルがソムヌスに呼びかける)
  - Argolici (ARGOLICUS; アルゴスの): Argolici ducis
- [6] 115 Argolicique ducis celeri pete castra volatu
  - Argolici (Argolicus; アルゴスの): Argolici . . . ducis 115:アガメムノンの

116 dumque tuo premitur sopitus pondere dulci,
- [2] 115 Dumque tuo premitur sopitus pondere dulci,
  - … 作者は眠りに重さ（*pondus*）を帰しているが、詩人たちは他の箇所でも眠りによって重荷を負わされる（*gravari*）、圧倒される（*opprimi*）、屈服する（*succumbere*）と言っている。Virg. Aen. VI, 520；Ovid. Her. XII, 49 を参照せよ。
- [3] 116 Dumque tuo premitur sopitus pondere dulci,
- [4] 116 Dumque tuo premitur sopitus pondere dulci,
- [6] 116 dumque tuo premitur sopitus pondere dulci,

117 haec illi mandata refer: cum crastina primum
- [2] 116 Haec illi mandata refer : quum crastina primum
- [3] 117 Haec illi mandata refer: cum crastina primum
- [4] 117 Haec illi mandata refer : cum crastina primum
- [6] 117 haec illi mandata refer: cum crastina primum

118 extulerit Titana dies noctemque fugarit,
- [2] 117 Extulerit Titana dies, noctemque fugarit,
- [3] 118 Extulerit Titana dies noctemque fugarit,
- [4] 118 Extulerit Titana dies noctemque fugarit,
  - Titana (TITAN; ティタン): Titana:日がティタンを昇らせたとき
- [6] 118 extulerit Titana dies noctemque fugarit,
  - Titana (Titan; ティタン): cum crastina . . . extulerit -ana dies 118

119 cogat in arma uiros incautumque occupet hostem."
- [2] 118 Cogat in arma viros , incautumque occupet hostem ».
  - *Cogat in arma viros*（男たちを武装へと駆り立てるように）。Virg. Aen. IX, 463: « Turnus in arma viros armis circumdatus ipse, Suscitat, aeratasque acies in praelia cogit »。
- [3] 119 Cogat in arma uiros incautumque occupet hostem.'
- [4] 119 Cogat in arma viros incautumque occupet hostem. »
- [6] 119 cogat in arma viros incautumque occupet hostem.'

120 Nec mora: Somnus abit leuibusque per aera pennis
- [2] 119 Nec mora, Somnus abit, levibusque per aera pennis
- [3] 120 Nec mora: somnus abit leuibusque per aera pennis
- [4] 120 Nec mora : somnus abit levibusque per aera pennis
- [6] 120 nec mora, Somnus abit levibusque per aera pennis
  - Somnus (Somnus; ソムヌス): Somnus 120

121 deuolat in thalamos Agamemnonis: ille sopore
- [2] 120 Devolat in thalamos Agamemnonis : ille sopore
- [3] 121 Deuolat in thalamos Agamemnonis: ille sopore
- [4] 121 Devolat in thalamos Agamemnonis : ille sopore
  - Agamemnonis (AGAMEMNON; アガメムノン): Agamemnonis:ユピテルに送られたソムヌスが、アガメムノンの寝室へ飛び降りる
- [6] 121 devolat in thalamos Agamemnonis: ille sopore
  - Agamemnonis (Agamemnon; アガメムノン): -onis 121. 795

122 corpus inundatum leni prostratus habebat.
- [2] 121 Corpus inundatum leni prostratus habebat.
  - *Corpus inundatum*（浸された身体）。バルトは前掲箇所 2752 頁で、ここにこの箇所の最良の韻律にそぐわない何某かの気取り（*affectatiuncula*）を嗅ぎ取っている。しかし私は *inundatum* という語をきわめて優雅であると考え、詩人たちが他の箇所で *irrigare somnum*（眠りを注ぐ）や *soporem irriguum*（潤す眠り）と言うあの慣習に倣って造られたものと考える。Virg. Aen. III, 511；Lucret. IV, 906；Claudian. praef. ad VI Cons. Hon. v. 9 を参照せよ。
- [3] 122 Corpus inundatum leni prostratus habebat.
- [4] 122 Corpus inundatum leni prostratus habebat.
- [6] 122 corpus inundatum leni prostratus habebat.

123 Ad quem sic loquitur curarum operumque leuator:
- [2] 122 Ad quem sic loquitur curarum operumque levator:
  - *Curarum operumque levator*（憂いと労苦を和らげる者）。ナーソー（オウィディウス）が Met. XI, 624 でより冗長に述べていることを、作者はより簡潔に言い表している：« Pax animi, quem cura fugit; qui corda diurnis Fessa ministeriis mulces, reparasque labori »。
- [3] 123 Ad quem sic loquitur curarum operumque leuator:
- [4] 123 Ad quem sic loquitur curarum operumque levator :
- [6] 123 ad quem sic loquitur curarum operumque levator:
  - levator (Somnus; ソムヌス): curarum operumque levator 123

124 "Rex Danaum, Atrida, uigila et mandata Tonantis
- [2] 123 «RexDanaum, Atrida, vigila, et mandata Tonantis,
- [3] 124 'Rex Danaum Atride, uigila et mandata Tonantis,
- [4] 124 « Rex Danaum Atride, vigila et mandata Tonantis,
  - Atride (AGAMEMNON; アガメムノン): Atride:ダナオイの王よ(ユピテルに送られたソムヌスが語る)
  - Danaum (GRAI; ギリシア人): — 王(アガメムノン)
  - Tonantis (JUPPITER; ユピテル): Tonans Tonantis:雷神の命令を受けよ(ソムヌスがアガメムノンに呼びかける)
- [6] 124 'rex Danaum Atrida, vigila et mandata Tonantis,
  - rex (Agamemnon; アガメムノン): また rex Danaum 124. 496 を参照
  - Atrida (Atrides (Agamemno); アトリデス（アガメムノン）): 呼格:rex Danaum -da(他の写本では -de)124
  - Danaum (Danai; ダナオイ): -um(属格):19. 50. 67. 124. 153. 251. 268. 357. 389. 496. 631. 686. 691. 698. 705. 743. 747. 794. 1025
  - Tonantis (Tonans; 雷神): mandata Tonantis 124

125 quae tibi iussa simul delatus ab aethere porto,
- [2] 124 Quae tibi missa simul delapsus ab aethere porto ,
- [3] 125 Quae tibi missa simul delatus ab aethere porto,
- [4] 125 Quae tibi missa simul delatus ab aethere porto.
- [6] 125 quae tibi iussa simul delatus ab aethere porto,

126 accipe: cum primum Titan se emerserit undis,
- [2] 125 Accipe : quum primum Titan emerserit undis,
- [3] 126 Accipe: cum primum Titan emerserit undis,
- [4] 126 Accipe : cum primum Titan se emerserit undis,
  - Titan (TITAN; ティタン): 波から現れたとき
- [6] 126 accipe: cum primum Titan se emerserit undis,
  - se emerserit … マニリウス 5, 198、アウィエヌス『世界周航記』126 を参照 …
  - Titan (Titan; ティタン): cum . . . Titan se emerserit undis 126

127 fortibus arma iube socios aptare lacertis
- [2] 126 Fortibus arma jube socios aptare lacertis,
  - *Aptare lacertis*（腕に装着する）。Ovid. Am. I,
  - **(cont.)** ［前頁の Ovid. Am. I, からの続き］13, 14行: « Miles et armiferas aptat ad arma manus »。
- [3] 127 Fortibus arma iube socios aptare lacertis
- [4] 127 Fortibus arma jube socios aptare lacertis
- [6] 127 fortibus arma iube socios aptare lacertis

128 et petere Iliacos instructo milite campos."
- [2] 127 Et petere Iliacos instructo milite campos ».
  - *Et petere Iliacos*（そしてイリオンの……を目指すことを）。作者は下の 159 行でこの詩行を繰り返しているが、彼が縮約している相手であるホメロス自身の前例にならって、こうしたことをしばしば行っている。
- [3] 128 Et petere Iliacos instructo milite campos.'
- [4] 128 Et petere Iliacos instructo milite campos. »
  - Iliacos (ILIACUS; イリオンの): Iliacos campos:整えた軍勢とともにイリオンの野を目指す
- [6] 128 et petere Iliacos instructo milite campos.'
  - （証言） 『ベレンガリウスの事績』3, 37 を参照
  - Iliacos (Iliacus; イリオンの): -cos . . . campos 128. 160

129 Dixit, et has repetit per quas modo uenerat auras.
- [2] 128 Dixity et has repetit, per quas modo venerat, auras.
  - … そしてこれは、ソムヌスのもとから帰るイリスについて述べるオウィディウスの Met. XI, 632 の明白な模倣である: « remeat, per quos modo venerat, arcus »。
- [3] 129 Dixit et has repetit per quas modo uenerat auras.
- [4] 129 Dixit et has repetit per quas modo venerat auras.
- [6] 129 dixit et has repetit per quas modo venerat auras.

130 Interea lucem terris dedit ignea lampas.
- [2] 129 Interea lucem terris dedit ignea lampas ;
- [3] 130 Interea lucem terris dedit ignea lampas.
- [4] 130 Interea lucem terris dedit ignea lampas.
- [6] 130 interea lucem terris dedit ignea lampas.
  - lampas (Sol; 太陽): ignea lampas 130 を参照

131 Conuocat attonitus iussis Pelopeius heros
- [2] 130 Convocat attonitus jussis Pelopeius heros
- [3] 131 Conuocat adtonitus uisis Pelopeius heros
- [4] 131 Convocat attonitus visis Pelopeius heros
  - Pelopeius (AGAMEMNON; アガメムノン): Pelopeius heros:将たちを呼び集める
- [6] 131 convocat attonitus iussis Pelopeius heros
  - iussis … ウェルギリウス『アエネーイス』3, 172 を参照
  - Pelopeius (Pelopeius; ペロプス家の): Pelopeius heros 131. 739:アガメムノン

132 in coetum proceres remque omnibus ordine pandit:
- [2] 131 In coetum proceres, remque omnibus ordine pandit
  - *Remque omnibus ordine pandit*（そして事の次第を順序立てて皆に明かす）。Virg. Aen. III, 179。
- [3] 132 In coetum proceres remque omnibus ordine pandit.
- [4] 132 In coetum proceres remque omnibus ordine pandit.
- [6] 132 in coetum proceres remque omnibus ordine pandit.

133 cuncti promittunt socias in proelia uires
- [2] 132 Cuncti promittunt socias in praelia vires ,
- [3] 133 Cuncti promittunt socias in praelia uires
- [4] 133 Cuncti promittunt socias in proelia vires
- [6] 133 cuncti promittunt socias in proelia vires

134 hortanturque ducem. Quorum rex fortia dictis
- [2] 133 Hortanturque ducem : quorum rex fortia dictis
- [3] 134 Hortanturque duces; quorum rex fortia dictis
- [4] 134 Hortanturque ducem ; quorum rex fortia dictis
- [6] 134 hortanturque ducem; quorum rex fortia dictis
  - ducem Ω: 彼らはアガメムノンをも駆り立てる
  - rex (Agamemnon; アガメムノン): rex 58. 134. 691
  - ducem (Agamemnon; アガメムノン): dux 134. 156. 739

135 pectora collaudans grates agit omnibus aequas.
- [2] 134 Pectora collaudat , grates agit omnibus sequas.
- [3] 135 Pectora conlaudat gratesque agit omnibus aequas.
- [4] 135 Pectora collaudat, grates agit omnibus aequas.
- [6] 135 pectora collaudat: grates agit omnibus aequas.

136 Hic tunc Thersites, quo non deformior alter
- [2] 135 Hic tum Thersites, quo non deformior alter
- [3] 136 Hic tum Thersites, quo non deformior alter
- [4] 136 Hic tum Thersites, quo non deformior alter
  - Thersites (THERSITES; テルシテス): 彼より醜い者も、舌の不遜な者も他にいない者、もはや戦を続けるべきではないと言う
- [6] 136 hic tunc Thersites, quo non deformior alter
  - Thersites (Thersites; テルシテス): Thersites, quo non deformior alter venerat ad Troiam nec lingua protervior ulli 136

137 uenerat ad Troiam nec lingua proteruior ulli,
- [2] 136 Venerat ad Trojam , linguaque protervior alter,
- [3] 137 Venerat ad Troiam linguaue proteruior, ultra
- [4] 137 Venerat ad Trojam linguave protervior, ultra
  - Trojam (TROJA; トロイア): Trojam:テルシテスより醜い者はトロイアに来ていなかった
- [6] 137 venerat ad Troiam nec lingua protervior ulli,
  - Troiam (Troia; トロイア): venerat ad -iam 137

138 bella gerenda negat patriasque hortatur ad oras
- [2] 137 Bella gerenda negat, patriasque hortatur ad oras
- [3] 138 Bella gerenda negat patriasque hortatur ad oras
- [4] 138 Bella gerenda negat patriasque hortatur ad oras
- [6] 138 bella gerenda negat patrias hortatus ad oras
  - oras (Graecia; ギリシア): patrias . . . ad oras 138 を参照

139 uertere iter, quem consiliis illustris Vlixes
- [2] 138 Vertere iter : quem consiliis illustris Ulysses
  - *Consiliis illustris Ulysses*（深慮に名高いウリクセス）。バルトは前掲箇所 2754 頁でこれを称賛し、それが πολύμητις（知謀に富む）、πολυμήχανος（機知縦横の）、δῖος（神のような）といったホメロスの複数の添え名を美しく表現していると述べている。
- [3] 139 Vertere iter; quem consiliis inlustris Ulixes
- [4] 139 Vertere iter; quem consiliis illustris Ulixes
  - Ulixes (ULIXES; ウリクセス): — 思慮で名高い者、笏でテルシテスを打つ
- [6] 139 vertere iter; quem consiliis inlustris Vlixes
  - Vlixes (Vlixes; ウリクセス): consiliis illustris -es 139

140 correptum dictis sceptro percussit eburno.
- [2] 139 Correptum dictis sceptro percussit eburno.
- [3] 140 Correptum dictis sceptro percussit eburno.
- [4] 140 Correptum dictis sceptro percussit eburno.
- [6] 140 correptum dictis sceptro percussit eburno.

141 Tum uero ardescit conceptis litibus ira:
- [2] 140 Tunc vero ardescit conceptis litibus ira;
  - … *Ardescit ira*（怒りに燃え上がる）。ウェルギリウスの Aen. IX, 66 に従っている: « Ignescunt irae, duris dolor ossibus haeret »。
- [3] 141 Tum uero ardescit conceptis litibus ira:
- [4] 141 Tunc vero ardescit conceptis litibus ira :
- [6] 141 tum vero ardescit conceptis litibus ira:

142 uix telis caruere manus, ad sidera clamor
- [2] 141 Vix telis caruere manus, ad sidera clamor
- [3] 142 Vix telis caruere manus, ad sidera clamor
- [4] 142 Vix telis caruere manus, ad sidera clamor
- [6] 142 vix telis caruere manus, ad sidera clamor

143 tollitur et cunctos pugnandi corripit ardor.
- [2] 142 Tollitur, et cunctos pugnandi corripit ardor.
- [3] 143 Tollitur, et cunctos pugnandi corripit ardor.
- [4] 143 Tollitur, et cunctos pugnandi corripit ardor.
- [6] 143 tollitur et cunctos pugnandi corripit ardor.

144 Tandem sollertis prudentia Nestoris aeuo
- [2] 143 Tandem solertis prudentia Nestoris aevo
  - … *Prudentia Nestoris aevo*（年齢においてネストルの思慮分別）、すなわち年齢と経験により思慮深いネストルのこと。われらの詩人はしばしば抽象概念によって自身の英雄たちを
  - **(cont.)** （前頁からの続き）指し示すのが常であり、これはホメロスやその他の前例にならったものである。別の箇所における、ネストル自身を表す *Nestoris aetas*（ネストルの年齢）、*Menelai ardor*（メネラオスの熱情）、*Ithaci solertia*（イタケ人の老練さ）、またホラーティウスにおける *virtus Catonis*（カトーの徳）などがそれである。
- [3] 144 Tandem sollertis prudentia Nestoris aeuo
- [4] 144 Tandem sollerti prudentia Nestoris aevo
  - Nestoris (NESTOR; ネストル): Nestoris:ネストルの思慮が、年の功で群衆を鎮める
- [6] 144 tandem sollertis prudentia Nestoris aevo
  - Nestoris (Nestor; ネストル): sollertis prudentia -oris aevo 144

145 compressam miti sedauit pectore turbam
- [2] 144 Compressam miti sedavit pectore turbam ,
  - *Compressam miti sedavit*（穏やかに抑えつけ鎮めた）。おそらくウェルギリウスの Georg. IV, 86 の次の言葉から取られたものであろう: « Hi motus animorum atque haec certamina tanta Pulveris exigui jactu compressa quiescent »。またウェルギリウスは Aen. IX, 740 で *sedato pectore*（鎮まった胸で）と言っている。
- [3] 145 Compresssam miti sedauit pondere turbam
- [4] 145 Compressam miti sedavit pectore turbam
- [6] 145 compressam miti sedavit pectore turbam

146 admonuitque duces dictis responsa recordans
- [2] 145 Admonuitque,duces dictis, responsa recordans
  - *Responsa recordans Temporis illius*（あの時代の神託を思い起こし）。著名なボンダムは 144 頁で、これがオウィディウスの Met. [XIII,] 280 の次の言葉から模作されたと考えている: « quanto cogor meminisse dolore Temporis illius, quo Graium murus Achilles Procubuit »。
- [3] 146 Admonuitque duces dictis, responsa recordans
- [4] 146 Admonuitque duces dictis, responsa recordans
- [6] 146 admonuitque duces dictis, responsa recordans

147 temporis illius, quo uisus in Aulide serpens
- [2] 146 Temporis illius, quo visus in Aulide serpens
- [3] 147 Temporis illius, quo uisus in Aulide serpens
- [4] 147 Temporis illius, quo visus in Aulide serpens
  - Aulide (AULIS; アウリス): in Aulide:アウリスで(大蛇が見られた)
- [6] 147 temporis illius, quo visus in Aulide serpens
  - Aulide (Aulis; アウリス): visus in Aulide serpens 147

148 consumpsit uolucrum bis quattuor arbore fetus
- [2] 147 Consumpsit volucrum bis quatuor arbore fetus,
  - … 作者がここでオウィディウスの Met. XII, 15 を念頭に置いていたことはほぼ確実である: « Nidus erat volucrum bis quatuor arbore summa, Quas simul et matrem circum sua damna volantem Corripuit serpens »。…
- [3] 148 Consumpsit uolucrum bis quattuor arbore fetus
- [4] 148 Consumpsit volucrum bis quattuor arbore fetus
- [6] 148 consumpsit volucrum bis quattuor arbore fetus

149 atque ipsam inualido pugnantem corpore contra
- [2] 148 Atque ipsam invalido pugnantem pectore contra
- [3] 149 Atque ipsam inualido pugnantem corpore contra
- [4] 149 Atque ipsam invalido pugnantem corpore contra
- [6] 149 atque ipsam invalido pugnantem corpore contra

150 addidit extremo natorum funere matrem.
- [2] 149 Addidit extremo natorum funere matrem.
- [3] 150 Addidit extremo natorum funere matrem.
- [4] 150 Addidit extremo natorum funere matrem.
- [6] 150 addidit extremo natorum funere matrem.

151 Tunc "sic deinde" senex "moneo remoneboque, Achiui:
- [2] 150 Infit deinde senex : « Maneo, remaneteque, Achivi,
  - … ホメロスの『イリアス』II, 331 でオデュッセウスが Ἀλλ᾽ ἄγε, μίμνετε πάντες ἐϋκνήμιδες Ἀχαιοί と促している。むろんホメロスにおいてこれはオデュッセウスの演説であるが、われらの詩人はそれをネストルに帰しているのである。
- [3] 151 Tum sic deinde: 'senex remoror, remoramini, Achiui:
- [4] 151 Tum sic deinde senex : « Moneo, remanete, Pelasgi;
  - — (GRAI; ギリシア人): [呼格、一般に:ネストルが語る]
  - Pelasgi (GRAI; ギリシア人): <呼格:— 留まれ>
- [6] 151 tunc 'sic deinde' senex 'moneo remoneboque, Achivi:
  - Achivi (Achivi; アカイア人): 呼格:151
  - senex (Nestor; ネストル): senex 151 を参照

152 in decimo labor est, Calchas quem dixerat, anno,
- [2] 151 In decimo labor est, quem Calchas dixerat, anno,
  - *In decimo labor est*（十番目に労苦がある）、すなわち
  - **(cont.)** （前頁からの続き）実に十年目になって初めて、われわれがイリオンを攻略するための労苦が予言され、定められている、ということである。しかし私はむしろ *In decimum annum usque labor*、すなわち「われわれは労苦せねばならない」と読みたいところである。というのも、彼はイリオンが攻略されるまで戦争がその年へと引き延ばされることを意味しているからである。ウェルギリウスもこのように語るのが常であり、Aen. IX, 155: « decimum quos distulit Hector in annum »、また XI, 289: « Hectoris Aeneaeque manu victoria Graium Haesit, et in decimum vestigia rettulit annum »。
- [3] 152 In decimo labor est, Calchas quem dixerat, anno,
- [4] 152 In decimo labor est, Calchas quem dixerat, anno,
  - Calchas (CALCHAS; カルカス): — トロイアが倒れる年を告げていた
- [6] 152 in decimo labor est, Calchas quem dixerat, anno,
  - Calchas (Calchas; カルカス): 予言者カルカス:52. 152

153 quo caderet Danaum uictricibus Ilion armis."
- [2] 152 Quo caderet Danaum victricibus Ilion armis».
- [3] 153 Quo cadet ec Danaum uictricibus Ilion armis.'
- [4] 153 Quo caderet Danaum victricibus Ilion armis. »
  - Danaum (GRAI; ギリシア人): — トロイアはダナオイの勝利の武器によって倒れるであろう
  - Ilion (TROJA; トロイア): Ilion:イリオンが倒れる日
- [6] 153 quo caderet Danaum victricibus Ilion armis
  - Danaum (Danai; ダナオイ): -um(属格):19. 50. 67. 124. 153. 251. 268. 357. 389. 496. 631. 686. 691. 698. 705. 743. 747. 794. 1025
  - Ilion (Ilion; イリオン): Ilĭŏn 153. 1056

154 Assensere omnes, laudatur Nestoris aetas
- [2] 153 Adsensere omnes, laudatur Nestoris aetas:
  - *Nestoris aetas*（ネストルの年齢）、すなわち老年の知慮、あるいは老ネストルのこと。
- [3] 154 Assensere omnes, laudatur Nestoris aetas,
- [4] 154 Assensere omnes, laudatur Nestoris aetas,
  - Nestoris (NESTOR; ネストル): — 彼の年齢が称えられる
- [6] 154 assensere omnes, laudatur Nestoris aetas
  - Nestoris (Nestor; ネストル): -oris aetas 154. 737

155 conciliumque simul dimittitur. Arma parari
- [2] 154 €k)nciliuinque simul dimittitur; arma parari
- [3] 155 Conciliumque simul dimittitur; arma parari
- [4] 155 Conciliumque simul dimittitur; arma parari
- [6] 155 conciliumque simul dimittitur; arma parari

156 dux iubet atque animos aptare et pectora pugnae.
- [2] 155 Dux jubet, atque animos aptari et pectora pugnae.
  - … 同写本は *aptare* ともする。Virg. Aen. X, 258: « sociis edicit, signa sequantur, Atque animos aptent armis: pugnaeque parent se »。
- [3] 156 Dux omnis iubet atque aptari corpora pugnae.
- [4] 156 Dux jubet atque animos, aptari et corpora pugnae.
- [6] 156 dux iubet atque animos aptare et corpora pugnae.
  - dux (Agamemnon; アガメムノン): dux 134. 156. 739

157 Postera lux tacitas ut primum dispulit umbras
- [2] 156 Postera lux tacitas ut primum depulit umbras ,
- [3] 157 Postera lux tacitas ut primum dispulit umbras
- [4] 157 Postera lux tacitas ut primum depulit umbras
- [6] 157 postera lux tacitas ut primum depulit umbras

158 et nitidum Titan radiis caput extulit undis,
- [2] 157 Et nitidum Titan radiis caput extulit undis,
- [3] 158 Et nitidum Titan radiis caput extulit undis,
- [4] 158 Et nitidum Titan radiis caput extulit undis,
  - Titan (TITAN; ティタン): — 光線で輝く頭を波から上げた
- [6] 158 et nitidum Titan radiis caput extulit undis,
  - Titan (Titan; ティタン): nitidum -an radiis caput extulit undis 158

159 protinus armari socios iubet acer Atrides
- [2] 158 Protinus armari socios jubet acer Atrides,
- [3] 159 Protinus armari socios iubet acer Atrides
- [4] 159 Protinus armari socios jubet acer Atrides
  - Atrides (AGAMEMNON; アガメムノン): — 猛き者、仲間たちに武装を命じる
- [6] 159 protinus armari socios iubet acer Atrides
  - Atrides (Atrides (Agamemno); アトリデス（アガメムノン）): acer -es 159

160 et petere Iliacos instructo milite campos.
- [2] 159 Et petere Iliacos instructo milite campos.
  - … 127 行が繰り返されている。…
- [3] 160 Et petere Iliacos instructo milite campos.
- [4] 160 Et petere Iliacos instructo milite campos.
  - Iliacos (ILIACUS; イリオンの): — 同
- [6] 160 et petere Iliacos instructo milite campos.
  - Iliacos (Iliacus; イリオンの): -cos . . . campos 128. 160

161 Vos mihi nunc, Musae - quid enim non ordine nostis? -,
- [2] 160 Vos mihi nunc, Musae, quid enim non ordine nostis?
  - *Quid enim non ordine nostis?*（あなた方が順序正しく知らぬものなどあろうか）。同様にマロー［ウェルギリウス］も Aen. VII, 645 および IX, 529 で: « Et meministis enim, Divae, et memorare potestis »。
- [3] 161 Vos mihi nunc, Musae (quid enim non ordine nostis?),
- [4] 161 Vos mihi nunc, Musae (quid enim non ordine nostis ?),
  - Musae (MUSAE; ムーサたち): 呼格
- [6] 161 vos mihi nunc, Musae (quid enim non ordine nostis?),
  - Musae (Musa; ムーサ): Musae 呼格 161

162 nomina clara ducum clarosque referte parentes
- [2] 161 Nomina clara ducum clarosque referte parentes,
- [3] 162 Nomina clara ducum clarosque referte parentes
- [4] 162 Nomina clara ducum clarosque referte parentes
- [6] 162 nomina clara ducum clarosque referte parentes

163 et dulces patrias: nam sunt haec munera uestra.
- [2] 162 Et dulces patrias : nam sunt haec munera vestra.
- [3] 163 Et dulces patrias: nam sunt haec munera uestra.
- [4] 163 Et dulces patrias : nam sunt haec munera vestra.
- [6] 163 et dulces patrias: nam sunt haec munera vestra.

164 Dicamus quot quisque rates ad Pergama duxit
- [2] 163 Dicamus, quot quisque rates ad Pergama duxit,
- [3] 164 Dicamus, quot quisque rates ad Pergama duxit,
- [4] 164 Dicamus quot quisque rates ad Pergama duxit,
  - Pergama (TROJA; トロイア): Pergama:ペルガマへ、ギリシアの将それぞれが何隻の船を率いたか
- [6] 164 dicamus, quot quisque rates ad Pergama duxit,
  - Pergama (Pergama; ペルガマ): ad Pergama 164

165 et coeptum peragamus opus, sitque auctor Apollo
- [2] 164 Et cceptum peragamus opus, sitque auctor Apollo,
- [3] 165 Et coeptum peragamus opus, sitque auctor Apollo
- [4] 165 Et coeptum peragamus opus, sitque auctor Apollo
  - Apollo (APOLLO; アポロ): われらの詩人の守り手とならんことを
- [6] 165 et coeptum peragamus opus, sitque auctor Apollo
  - Apollo (Apollo; アポロ): Apollo 165

166 aspiretque libens operi per singula nostro.
- [2] 165 Adspiretque libens operi per singula nostro.
  - *Adspiretque libens operi*（そして快く事業に息吹を吹き込まれんことを）。Virg. Aen. IX, 525: « Vos, o Calliope, precor, adspirate canenti »。Ovid. Met. I, 3: « Di coeptis ... adspirate meis »。――なお、この軍勢の列挙はホメロス以降のすべての叙事詩人にとってほぼ恒例のものである。とりわけホメロスの巧みな模倣者にして競演者であるウェルギリウスの Aen. VII, 641 を参照すべし。近世の詩人ではトルクワート・タッソの『解放されたエルサレム』(Gerus. lib.) 第 1 歌 36 連が挙げられる。パリ編者。
- [3] 166 Aspiretque libens operi per singula nostro.
- [4] 166 Aspiretque libens operi per singula nostro.
- [6] 166 aspiretque libens operi per singula nostro.

167 Peneleos princeps et bello Leitus acer,
- [2] 166 Peneleus princeps, et bello Leitus acer.
  - … というのも、ホメロスのボイオティア（軍船表）の 1 行目で Πηνέλεως καὶ Λήϊτος が並べられているからである。写字生たちはこの名前から、よりよく知られた *Laertius*、すなわちウリクセスを誤って作り出したのである。
- [3] 167 Peneleus princeps et bello Leitus acer
- [4] 167 Peneleus princeps et bello Leitus acer
  - Leitus …（『イリアス』II, 494 を参照）。
  - Leitus (LEITUS; レイトス): 戦において猛き者、ギリシアの将たちの中に
  - Peneleus (PENELEUS; ペネレオス): ギリシアの他の将たちとともにトロイアを目指す
- [6] 167 Peneleus princeps et bello Leïtus acer
  - Leïtus (Leitus; レイトス): bello *Leitus (lertius trad.) acer 167:アレクトリュオンの子、ボイオティア人の将
  - Peneleus (Peneleos; ペネレオス): Peneleos (-leus trad.) princeps 167

168 Arcesilaus atrox Prothoenorque Cloniusque
- [2] 167 Arcesilaus atrox, Prothoenorque, Cloniusque
- [3] 168 Arcesilaus atrox Prothoenorque Cloniusque
- [4] 168 Arcesilaus atrox Prothoenorque Cloniusque
  - Arcesilaus (ARCESILAUS; アルケシラオス): 猛き者、トロイアに来る
  - Clonius (CLONIUS; クロニオス): ボイオティア人、プロトエノルとともにトロイアを目指す
  - Prothoenor (PROTHOENOR; プロトエノル): ボイオティア人、ギリシアの将たちの中に
- [6] 168 Arcesilaus atrox Prothoënorque Cloniusque
  - Arcesilaus (Arcesilaus; アルケシラオス): Arcesilaus atrox 168:ボイオティア人
  - Clonius (Clonius; クロニオス): Prothoenorque Cloniusque Boeoti 168
  - Prothoënor (Prothoenor; プロトエノル): *Prothoënor Boeotus:168

169 Boeoti decies quinas egere carinas
- [2] 168 Boeotas decies quinas duxere carinas,
  - … ホメーロスの『イーリアス』II, 510 から *Boeotas* または *Boeotum* と読むべきである。…
- [3] 169 Boeoti decies quinas egere carinas
- [4] 169 Boeoti decies quinas egere carinas
  - Boeoti（同所 495 および 509）。…
  - Boeoti (BOEOTUS; ボイオティア人): — Boeoti(プロトエノルとクロニオス)
- [6] 169 Boeoti decies quinas egere carinas
  - Boeoti (Boeotus; ボイオティア人): 複数 Boeoti (-tes trad.) 169

170 et tumidos ualido pulsarunt remige fluctus.
- [2] 169 Et tumidos valido pulsarunt remige fluctus.
- [3] 170 Et tumidos ualido pulsarunt remige fluctus.
- [4] 170 Et tumidos valido pulsarunt remige fluctus.
- [6] 170 et tumidos valido pulsarunt remige fluctus.

171 Inde Mycenaeis Agamemnon moenibus ortus,
- [2] 170 Inde Mycenaels Agamemnon finibus ortus,
- [3] 171 Inde Mycenaeis Agamemnon moenibus ortus,
- [4] 171 Inde Mycenaeis Agamemnon moenibus ortus,
  - Agamemnon (AGAMEMNON; アガメムノン): 百隻の船を率いる
  - Mycenaeis (MYCENAEUS; ミュケナイの): Mycenaeis moenibus:ミュケナイの城壁の内に生まれたアガメムノン
- [6] 171 inde Mycenaeis Agamemnon moenibus ortus,
  - Agamemnon (Agamemnon; アガメムノン): Mycenaeis -on moenibus ortus 171
  - Mycenaeis (Mycenaeus; ミュケナイの): Mycenaeis . . . moenibus 171

172 quem sibi bellatrix delegit Graecia regem,
- [2] 171 Quem sibi delegit bellatrix Graecia regem,
- [3] 172 Quem sibi delegit bellatrix Graecia regem,
- [4] 172 Quem sibi delegit bellatrix Graecia regem,
  - Graecia (GRAECIA; ギリシア): 好戦的な国、アガメムノンを自らの王に選んでいた
- [6] 172 quem sibi bellatrix delegit Graecia regem,
  - Graecia (Graecia; ギリシア): bellatrix . . . Graecia 172

173 centum egit plenas armato milite puppes;
- [2] 172 Centum egit plenas armato milite puppes :
- [3] 173 Centum egit plenas armato milite puppes.
- [4] 173 Centum egit plenas armato milite puppes.
- [6] 173 centum egit plenas armato milite puppes.

174 et bis tricenis Menelai nauibus ardor
- [2] 173 Et bis tricenis Menelai navibus ardor
  - … *Menelai ardor*（メネラオスの熱情）、すなわち燃え立つメネラオスのこと。
- [3] 174 Et bis tricenis Menelai nauibus ardor
- [4] 174 Et bis tricenis Menelai navibus ardor
  - Menelai (MENELAUS; メネラオス): Menelai:メネラオスの熱情が六十隻でトロイアを目指した
- [6] 174 et bis tricenis Menelai navibus ardor
  - Menelai (Menelaus; メネラオス): -lai . . . ardor 174

175 insequitur totidemque ferox Agapenoris ira;
- [2] 174 Insequitur, totidemque ferox Agapenoris ira.
- [3] 175 Insequitur totidemque ferox Agapenoris ira.
- [4] 175 Insequitur totidemque ferox Agapenoris ira.
  - Agapenoris (AGAPENOR; アガペノル): Agapenoris:アガペノルの猛き怒り
- [6] 175 insequitur totidemque ferox Agapenoris ira.
  - Agapenoris (Agapenor; アガペノル): ferox Agapenoris ira 175:アルカディア人、アンカイオスの子

176 quos iuxta fidus sollerti pectore Nestor
- [2] 175 Quos juxta fidus solerti pectore Nestor,
- [3] 176 Quos iuxta fidus sollerti pectore Nestor
- [4] 176 Quos juxta fidus sollerti pectore Nestor
  - Nestor (NESTOR; ネストル): 忠実な者、巧みな心を持ち、思慮に優れた者、息子たちとともに九十隻をトロイアへ率いる
- [6] 176 quos iuxta fidus sollerti pectore Nestor
  - Nestor (Nestor; ネストル): fidus sollerti pectore Nestor consilioque potens 176

177 consilioque potens gemina cum prole suorum
- [2] 176 Consilioque potens, gemina cum prole suorum
  - *Gemina cum prole suorum*（みずからの二人の子供とともに）。ネストルが二人の息子とともに到来したと彼が書いていることは、ホメロスに由来するのではなく、おそらくクレタのディクテュスから取ったものであろう。ディクテュスは第 1 巻 13 章で次のように述べている: « Nestor cum Antilocho et Thrasymede, quos ex Anaxibia susceperat, supervenit »。
- [3] 177 Consilioque potens gemina cum prole suorum
- [4] 177 Consilioque potens gemina cum prole suorum
- [6] 177 consilioque potens gemina cum prole suorum
  - prole (Antilochus; アンティロコス): および 177 gemina cum prole
  - prole (Thrasymedes; トラシュメデス): (Thrasymedes、ネストルの子)。177 行:gemina cum prole

178 it ter tricenis munitus in arma carinis.
- [2] 177 It ter tricenis munitus in arma carinis.
  - … なぜならホメロスは『イリアス』II, 602 で彼に 90 隻の船を割り当てているからである。
- [3] 178 It ter tricenis munitus in arma carinis.
- [4] 178 It ter tricenis munitus in arma carinis.
- [6] 178 it ter tricenis munitus in arma carinis.

179 At Schedius uirtute potens et Epistrophus ingens,
- [2] 178 At Schedius virtute potens et Epistrophus ingens
  - … ホメロスの『イリアス』II, 517 から *At Schedius virtute potens et Epistrophus* と読むべきである。
- [3] 179 At Schedius uirtute potens et Epistrophus ingens
- [4] 179 At Schedius virtute potens et Epistrophus ingens
  - Epistrophus (EPISTROPHUS Iphiti filius; エピストロポス、イピトスの子): — 巨大な者、ミュルミドンの栄光、残忍な戦の力
  - Schedius (SCHEDIUS; スケディオス): 武勇に優れた者、残忍な戦の力、ギリシアの将たちの中に
- [6] 179 at Schedius virtute potens et Epistrophus ingens,
  - Epistrophus (Epistrophus 1; エピストロポス 1): Schedius . . . et Epistrophus ingens, gloria Myrmidonum, saevi duo robora belli 179
  - Schedius (Schedius; スケディオス): Schedius virtute potens et Epistrophus ingens, gloria Myrmidonum 179

180 gloria Myrmidonum, saeui duo robora belli,
- [2] 179 Gloria Myrmidonum, saevi duo robora belli,
- [3] 180 Gloria Myrmidonum, saeui duo robora belli,
- [4] 180 Gloria Myrmidonum, saevi duo robora belli,
  - Myrmidonum (MYRMIDONES; ミュルミドン): — ミュルミドンの栄光、エピストロポス
- [6] 180 gloria Myrmidonum, saevi duo robora belli,
  - Myrmidonum (Myrmidones; ミュルミドン): Epistrophus . . . gloria -um 180

181 longa quaterdenis pulsarunt aequora proris
- [2] 180 Longa quater denis pulsarunt aequora proris.
  - … なぜならホメロスは前掲箇所で 40 隻の船を置いているからである。…
- [3] 181 Longa quaterdenis sulcarunt aequora proris.
- [4] 181 Longa quaterdenis sulcarunt aequora proris.
- [6] 181 longa quaterdenis pulsarunt aequora proris.

182 et bis uicenas Polypoetes atque Leonteus
- [2] 181 At bis vicenas Polypoetes atque Leonteus
  - … しかし *Polypoetes atque Leonteus* と
  - **(cont.)** （前頁からの続き）読むべきであることは、ホメロスの『イリアス』II, 740 および 745 から明らかである。…
- [3] 182 Et bis uicenas Polypoetes atque Leonteus
- [4] 182 Et bis vicenas Polypoetes atque Leonteus
  - Leonteus (LEONTEUS; レオンテウス): とポリュポイテス、トロイアの地へ四十隻を率いる
  - Polypoetes (POLYPOETES; ポリュポイテス): とレオンテウス、トロイアに向けて二十隻の船を整えた
- [6] 182 et bis vicenas Polypoetes atque Leonteus
  - Leonteus (Leonteus; レオンテウス): Leonteus 182:コロノスの子
  - Polypoetes (Polypoetes; ポリュポイテス): *Polypoetes 182. 1012:ヒッポダメイアの子

183 instruxere rates ornatas milite forti.
- [2] 182 Instruxere rates omatas milite forti.
- [3] 183 Instruxere rates, ornatas milite forti.
- [4] 183 Instruxere rates, ornatas milite forti.
- [6] 183 instruxere rates oneratas milite forti.

184 Euryalus Sthenelusque duces et fortis in armis
- [2] 183 Euryalus, Sthenelusque ferox, et fortis in armis
  - … ホメロス自身が『イリアス』II, 565 で彼をステネロスやディオメデスと結びつけているからである。またプリュギアのダレース第 14 章にも、「アルゴスからのディオメデス、エウリュアロス、ステネロス」が 80 隻の船を率いたとある（« Diomedes, Euryalus, Sthenelus ex Argis », navibus LXXX）。これに対して、ホメロスが 736 行でギリシア勢の指揮官の一人として 40 隻の船とともに数え上げているものの、われらの駄作詩人（poetaster）は名を挙げていないように思われるエウリュピュロスについて、ボンダムは 189 行で導入されていると考えており、そのことはわれわれ自身もその詩行において注記することとする。
- [3] 184 Euryalus Sthenelusque . . . . et fortis in armis
- [4] 184 Euryalus Sthenelusque duces et fortis in armis
  - Euryalus …――duces クーテンが正当にも保持。『イリアス』II, 563 以下 ἡγεμόνευε、およびヴァイティングが見事に称賛する『アエネーイス』II, 261「Thessandrus Sthenelusque duces」を参照。…
  - Tydides (DIOMEDES; ディオメデス): Tydides:武器において勇敢
  - Euryalus (EURYALUS; エウリュアロス): メキステウスの子、ディオメデスの下の将
  - Sthenelus (STHENELUS; ステネロス): ギリシアの将たちの中に
- [6] 184 Euryalus Sthenelique decus et fortis in armis
  - Euryalus (Euryalus; エウリュアロス): Euryalus 184:メキステウスの子、ディオメデスの仲間
  - Stheneli (Sthenelus; ステネロス): Stheneli (-us trad.) . . . decus 184:カパネウスの子

185 Tydides ualido pulsarunt remige pontum:
- [2] 184 Tydides, valido pulsarunt remige pontum,
- [3] 185 Tydides ualido pulsantes remige fluctus
- [4] 185 Tydides valido pulsarunt remige fluctus
- [6] 185 Tydides valido pulsarunt remige pontum:
  - Tydides (Tydides; テュディデス): fortis in armis -des 185

186 bis quadragenas onerarunt milite puppes;
- [2] 185 Bisque quadragenas onerarunt milite puppes:
  - … ホメロスは彼らに 80 隻の船を割り当てており、…
- [3] 186 Bis quadragenas onerarunt milite puppes.
- [4] 186 Bisque quadragenas onerarunt milite puppes.
- [6] 186 bis quadragenas onerarunt milite puppes.

187 Ascalaphusque potens et Ialmenus, acer uterque,
- [2] 186 Ascalaphusque potens, et lalmenus acer, uterque
  - … ホメロスの『イリアス』II, 512 で彼がアスカラポスに並べられていることから …
- [3] 187 Ascalaphusque potens et Ialmenus, acer uterque,
- [4] 187 Ascalaphusque potens et Ialmenus, acer uterque,
  - Ascalaphus (ASCALAPHUS; アスカラポス): 力強き者、とイアルメノス、二人とも猛き者で、三十隻を率いる
  - Ialmenus (IALMENUS; イアルメノス): とアスカラポス、二人とも猛き者で、三十隻をトロイアへ率いる
- [6] 187 Ascalaphusque potens et Ialmenus, acer uterque,
  - Ascalaphus (Ascalaphus; アスカラポス): Ascalaphus . . . potens 187:マルスの子、ミニュアイ人の将
  - Ialmenus (Ialmenus; イアルメノス): Ascalaphus . . . et *Ialmenus, acer uterque 187:マルスの子、ボイオティア人の将

188 ter denas ualido complerunt remige naues
- [2] 187 Ter denas valido complerunt milite naves.
- [3] 188 Ter denas ualido complerunt remige naues.
- [4] 188 Ter denas valido complerunt remige naves.
- [6] 188 ter denas valido complerunt remige naves.

189 et bis uicenas Locrum fortissimus Aiax
- [2] 188 At bis vicenas equitum fortissimus Ajax
- [3] 189 Et bis uicenas Locrum fortissimus Aiax
- [4] 189 Et bis vicenas Locrum fortissimus Ajax
  - Ajax (AJAX Oilei filius; アイアス、オイレウスの子): — ロクリス人の最も勇敢な者、トロイアに向けて四十隻の船を整えた
  - Locrum (LOCRI; ロクリス人): Locrum:ロクリス人の最も勇敢な者アイアス
- [6] 189 et bis vicenas Locrum fortissimus Aiax
  - Aiax (Aiax (Locrus); アイアス（ロクリス人）): Locrum fortissimus Aiax 189
  - Locrum (Locrus; ロクリス人): Locrum fortissimus Aiax 189

190 instruxit puppes totidemque Euhaemone natus,
- [2] 189 Instruxit puppes , totidemque Evaemone natus ;
  - … しかし私はホメロスの軍船表にアバントールの息子を見出さない。著名なボンダムは『異読考』146 頁で、ホメロスによって指揮官の中に名を挙げられているもののわれらの詩人には見出されないエウリュピュロスがこの詩行で示されていると考え、したがって次のように書かれていたと推測している: « Instruxit puppes, totidemque Evaemone natus »。なぜならエウリュピュロスはホメロスの 736 行で Εὐαίμονος ἀγλαὸς υἱός（エウアイモンの輝かしき息子）と呼ばれ、同じく 40 隻の船を率いたと述べられているからである。彼はヒュギーヌスの『神話集』(fab.) 94 でもエウアイモンとオーピスの息子と呼ばれている。…
- [3] 190 Instruxit puppes totidemque Euhaemone natus.
- [4] 190 Instruxit puppes totidemque Euhaemone natus.
  - Euaemone …（『イリアス』II, 736 を参照）。
  - Euhaemone (EUHAEMO; エウアイモン): Euhaemone
  - Euhaemone (EURYPYLUS; エウリュピュロス): Euhaemone natus:エウアイモンの子が四十隻の船を整えた
- [6] 190 instruxit puppes totidemque Euhaemone natus.
  - Euhaemone (Euhaemon; エウアイモン): Euhaemone natus 190:エウリュピュロス

191 quos iuxta Graium murus comitatur Achilles
- [2] 190 Quos juxta Graium ductor comitatur Achilles ,
  - バルトは『雑考』2754 頁で、*Graium ductor*（ギリシア勢の指揮官）を「戦いにおいて卓越し、武勇において至高である」と解釈している。…
- [3] 191 Quos iuxta Graium murus comitatur Achilles,
- [4] 191 Quos juxta Danaum murus comitatur Achilles,
  - Achilles (ACHILLES; アキレウス): — ダナオイの城壁、他のギリシアの将たちとともにトロイアを目指した
  - Danaum (GRAI; ギリシア人): — ダナオイの城壁、アキレウス
- [6] 191 quos iuxta Graium durus comitator Achilles
  - Achilles (Achilles; アキレウス): Graium durus comitator -es 191

192 cum quinquaginta materna per aequora uectus.
- [2] 191 Cum quinquaginta materna per aequora vectus.
- [3] 192 Cum quinquaginta materna per aequora uectus.
- [4] 192 Cum quinquaginta materna per aequora vectus.
- [6] 192 cum quinquaginta materna per aequora vectus
  - materna (Thetis; テティス): materna per aequora 192

193 Thessalici iuuenes Phidippus et Antiphus ibant
- [2] 192 Thessalici juvenes Phidippus et Antiphus ibant,
  - 私はホメロスの『イリアス』II, 678 に基づいて *Phidippus et Antiphus* と記した。…
- [3] 193 Thessalici iuuenes Phidippus et Antiphus ibant
- [4] 193 Thessalici juvenes Phidippus et Antiphus ibant
  - Antiphus (ANTIPHUS [Thessalicus] Thessali filius; アンティポス [テッサリアの]、テッサロスの子): — ペイディッポスとともに三十隻を率いる
  - Phidippus (PHIDIPPUS; ペイディッポス): とアンティポス、テッサリアの若者たち、三十隻をトロイアへ率いる
- [6] 193 Thessalici iuvenes Phidippus et Antiphus ibant
  - Antiphus (Antiphus 1; アンティポス 1): Thessalici iuvenes, Phidippus et Antiphus 193:テッサロスの子ら
  - Phidippus (Phidippus; ペイディッポス): Thessalici iuvenes *Phidippus (ped- trad.) et Antiphus 193
  - Thessalici (Thessalicus; テッサリアの): Thessalici iuvenes, Phidippus et Antiphus 193

194 altaque ter denis pulsarunt aequora proris
- [2] 193 Altaque ter denis sulcarunt aequora proris:
- [3] 194 Altaque ter denis sulcarunt aequora proris.
- [4] 194 Altaque ter denis sulcarunt aequora proris.
- [6] 194 altaque ter denis pulsarunt aequora proris.

195 et tribus assumptis ratibus secat aequora Teucer
- [2] 194 Et tribus adsumptis ratibus secat aequora Nireus,
  - … ホメロスが自らの軍船表においてこのテウクロスに全く言及していないだけでなく、その兄であるテラモンの子アイアスが 12 隻の船をトロイアへ率いたと語っており（これにはわれらの詩人も 204 行で一致している）、さらに他の著述家たち、例えばディクテュス（第 1 巻 13 章および 17 章）もアイアスを船団の指揮官とし、弟のテウクロスはその同行者にして同胞であったと述べているからである。プリュギアのダレース第 14 章は明快に「サラミスからのテラモンの子アイアスは弟テウクロスを伴った」（« Ajax Telamonius ex Salamine adduxit secum Teucrum fratrem »）と記している。ヒュギーヌスはたしかに『神話集』(fab.) 97 でテラモンの子アイアスが 12 隻の船を率い、弟テウクロスも同数を率いたと述べている。しかし、われらの詩人において流布本の読みがテウクロスに割り当てている船の数はこれとは異なり、彼がわずか 3 隻の船を率いたとされている。しかるにホメロスにおいて 3 隻の船が割り当てられているのはニレウスだけであり、この人物だけが、テウクロスの代わりに名指しされるのでない限り、梗概作者によって沈黙されているのである。…なぜならディクテュス I, 17 に「シュメからのニレウスが 3 隻、ピュラケからのポダルケスとプロテシラオスが 40 隻の船」（« Nireus ex Syme tres, Podarces et Protesilaus ex Phylaca naves XL »）とあるからである。
- [3] 195 Et tribus assumptis ratibus secat aequora Nireus,
- [4] 195 Et tribus ab Sume ratibus secat aequora Nireus,
  - … Nireus ボンダム、ヒヒト（『イリアス』II, 671 以下）。
  - Nireus (NIREUS; ニレウス): 三隻でトロイアを目指す
  - Sume (SUME; シュメ): ab Sume:シュメから
- [6] 195 et tribus † assumptis ratibus secat aequora Nireus,
  - Nireus (Nireus; ニレウス): *Nireus (teucer trad.) 195:アグライアとカロプスの子
  - — (Syme; シュメ): ab Syme (Σύμηθεν) 195 (assumptis trad.) ?
  - Nireus (Teucer; テウクロス): [195 trad.]

196 Tlepolemusque nouem Rhodius, quos uiribus acer
- [2] 195 Tlepolemusque novem Rhodius, quos viribus acer
  - … ホメロスは『イリアス』II, 653 で、彼がロドスから 9 隻の船を率いてきたと述べている。ディクテュス前掲箇所: 「トレポレモスはロドスおよびその周囲の他の島々から 8 隻の船でやって来た」。プリュギアのダレース第 14 章: « Tlepolemus ex Rhodo navibus numero novem »（ロドスからのトレポレモスは 9 隻の船で）。
- [3] 196 Tlepolemusque nouem Rhodius, quos uiribus acer
- [4] 196 Tlepolemusque novem Rhodius, quos viribus acer
  - Tlepolemus …（『イリアス』II, 653 を参照）。
  - Eumelus (EUMELUS; エウメロス): 力において猛き者、テラモンの子より一隻少なく率いる
  - Tlepolemus (TLEPOLEMUS; トレポレモス): ロドスの人、九隻をトロイアへ率いる
- [6] 196 Tlepolomusque novem Rhodius, quos viribus acer
  - Rhodius (Rhodius; ロドスの): Tlepolemus . . . Rhodius 196
  - Tlepolomus (Tlepolomus; トレポレモス): *Tlepolomus . . . Rhodius 196

197 Eumelus sequitur, minus una naue profectus
- [2] 196 Eumelus sequitur, minus una nave profectus.
  - … ホメロスの権威（『イリアス』II, 714）に基づくものであり、そこではアドメトスの息子 Εὔμηλος がペライからの 11 隻の船を指揮したと述べられている。ペライはテッサリアの都市である。ディクテュス前掲箇所: « Eumelus XI Pheris »（ペライからのエウメロスが 11 隻）。ここから、エウメロスがペライビア出身であると書くヒュギーヌスは訂正されるべきと思われる。われらの作者は *minus una nave*（1隻少ない船で）によって、11隻で出発した（profe-）と述べており――
  - **(cont.)** （前頁からの続き）[-profe-]ctum dicit（出航したと言う）。というのも、彼は先行する指導者たちの船、すなわちニレウスの3隻とトレポレモスの9隻を合算しているからである。
- [3] 197 Eumelus sequitur, minus una naue profectus
- [4] 197 Eumelus sequitur, minus una nave profectus
- [6] 197 Eumelus sequitur, minus una nave profectus
  - … minus una すなわち11 …
  - Eumelus (Eumelus; エウメロス): viribus acer *Eumelus 197:アドメトスの子

198 quam duxit Telamone satus Salaminius Aiax.
- [2] [197] [Quam duxit Telamone satus Salaminius Ajax.]
- [3] 198 Quam duxit Telamone satus Salaminius Aiax.
- [4] 198 Quam duxit Telamone satus Salaminius Ajax.
  - Ajax (AJAX Telamonis filius; アイアス、テラモンの子): — テラモンから生まれたサラミスの人、エウメロスより一隻多く率いる
- [6] 198 quam duxit Telamone satus Salaminius Aiax.
  - Aiax (Aiax (Telamonius); アイアス（テラモンの子）): Telamone satus Salaminius Aiax 198
  - Salaminius (Salaminius; サラミスの): Telamone satus Salaminius Aiax 198
  - Telamone (Telamon; テラモン): Telamone satus . . . Aiax 198

199 Ast Prothous Magnes Tenthredone natus et una
- [2] 198 At Prothous Magnes , Tenthredone natus , et una
  - … なぜならホメロスはプロトオスをマグネシア人の首領と呼んでおり、ディクテュスもトロイアを包囲した英雄たちの目録（第1巻17章）で « Prothous, Magnes, XL naves » と記しているからである。
- [3] 199 At Prothous Magnes Tenthredone natus et una
- [4] 199 At Prothous Magnes Tenthredone natus et una
  - At Prothous …（同所 756）。… Magnes …（同所）。…
  - Prothous (PROTHOUS; プロトオス): マグネシア人、テントレドンの子、ギリシアの将たちの中に
- [6] 199 ast Prothous Magnes Tenthredone natus et una
  - Magnes (Magnes; マグネシア人): Prothous *Magnes 199
  - Prothous (Prothous; プロトオス): *Prothous Magnes Tenthredone natus 199
  - Tenthredone (Tenthredon; テントレドン): Prothous Magnes *Tenthredone natus 199

200 Euboeae magnis Elephenor finibus ortus
- [2] 199 Eubceae magnis Elephenor finibus ortus,
  - … オウィディウス『悲歌』(*Trist.*) 第3巻において、おそらく同じエルペーノール、すなわちキルケーによって豚に変えられ、その後に人間の姿に戻されて、軽率な逃走の熱意に駆られてウリクセスのもとへ急ぐあまり、高所から転落して死んだウリクセスの部下の一人が言及されている。パリ編者。
- [3] 200 Euboeae magnis Elephenor finibus ortus
- [4] 200 Euboeae longis Elephenor finibus ortus
  - Elephenor (ELEPHENOR; エレペノル): エウボイアの<長い>地に生まれた者
  - Euboeae (EUBOEA; エウボイア): Euboeae
- [6] 200 Euboeae a † magnis Elephenor finibus ortus
  - Elephenor (Elephenor; エレペノル): Euboeae . . . *Elephenor finibus ortus 200
  - Euboeae (Euboea; エウボイア): Euboeae . . . finibus 200

201 Dulichiusque Meges, animisque insignis et armis,
- [2] 200 Dulichiusque Meges, auimisque insignis et armis
- [3] 201 Dulichiusque Meges, animisque insignis et armis,
- [4] 201 Dulichiusque Meges, animisque insignis et armis,
  - Meges (MEGES; メゲス): ドゥリキオンの人、ギリシアの将たちの中に
  - Thoas (THOAS; トアス): 心と武器に際立ち、アイトリアの民、アンドライモンの子、ギリシアの将たちの中に
- [6] 201 Dulichiusque Meges, animisque insignis et armis,
  - Dulichius (Dulichius; ドゥリキオンの): Dulichius . . . Meges 201
  - Meges (Meges; メゲス): Dulichius . . . Meges 201

202 Aetola de gente Thoas Andraemone natus,
- [2] 201 Aetola de gente Thoas Andraemone natus,
  - … ホメロス『イリアス』II, 638 に基づいて…
- [3] 202 Aetola de gente Thoas Andraemone natus,
- [4] 202 Aetola de gente Thoas Andraemone natus,
  - Aetola (AETOLUS; アイトリア人): de gente Aetola
  - Andraemone (ANDRAEMO; アンドライモン): Andraemone natus:アンドライモンの子トアス
- [6] 202 Aetola de gente Thoas Andraemone natus,
  - Aetola (Aetolus; アイトリア人): Aetola de gente Thoas 202
  - Andraemone (Andraemon; アンドライモン): Thoas Andraemone natus 202. 583
  - Thoas (Thoas; トアス): Aetola de gente Thoas Andraemone natus 202

203 hi quadragenas omnes duxere carinas;
- [2] 202 Hi quadragenas omnes duxere carinas :
- [3] 203 Hi quadragenas omnes duxere carinas.
- [4] 203 Hi quadragenas omnes duxere carinas.
- [6] 203 hi quadragenas omnes duxere carinas.

204 et bis sex Ithaci naues sollertia duxit,
- [2] 203 Et bis sex Ithaci naves solertia duxit,
- [3] 204 Et bis sex Ithaci naues sollertia duxit;
- [4] 204 Et bis sex Ithaci naves sollertia duxit;
  - Ithaci (ULIXES; ウリクセス): Ithacus Ithaci:イタケの人の巧みさが十二隻をトロイアへ率いる
- [6] 204 et bis sex Ithaci naves sollertia duxit;
  - Ithaci (Ithacus; イタケ人): Ithaci . . . sollertia 204:ウリクセス

205 quem sequitur totidem ratibus Telamonius Aiax,
- [2] 204 Quam sequitur totidem ratibus Telamonius Ajax ,
- [3] 205 Quem sequitur totidem ratibus Telamonius Aiax,
- [4] 205 Quem sequitur totidem ratibus Telamonius Ajax,
  - Ajax (AJAX Telamonis filius; アイアス、テラモンの子): — テラモンの子、際立った武勇に優れ、十二隻でトロイアを目指す
- [6] 205 quem sequitur totidem ratibus Telamonius Aiax,
  - Aiax (Aiax (Telamonius); アイアス（テラモンの子）): Telamonius -ax 205. 363. 602. 623. 787. 836
  - Telamonius (Telamonius; テラモンの): Telamonius Aiax 205. 363. 602. 623. 787. 836

206 egregia uirtute potens; simul horrida Guneus
- [2] 205 Egregia virtute poLens : simul ordine Guneus
  - グネウスはキュポスから22隻の船を率いた。ホメロス『イリアス』II, 648（実際は748）。…
- [3] 206 Egregia uirtute potens; simul horrida Guneus
- [4] 206 Egregia virtute potens; simul horrida Gunei
  - **206-207** Gunei Ira … 『イリアス』II, 748）。
  - Gunei (GUNEUS; グネウス): Gunei:グネウスの恐るべき怒りが二十二隻の船を率いる
- [6] 206 egregia virtute potens; simul horrida Guneus
  - Guneus (Guneus; グネウス): *Guneus 206:アカルナーニア人の将

207 ire bis undenis temptabat in arma carinis.
- [2] 206 Ire bis undenis tentabat in arma carinis.
- [3] 207 Ire bis undenis tendebat in arma carinis.
- [4] 207 Ira his undenis tendebat in arma carinis.
- [6] 207 ire bis undenis temptabat in arma carinis.

208 Idomeneus et Meriones, Cretaeus uterque,
- [2] 207 Idomeneus et Meriones, Cretaeus uterque
- [3] 208 Idomeneus et Meriones, Cretaeus uterque,
- [4] 208 Idomeneus et Meriones, Cretaeus uterque,
  - Cretaeus (CRETAEUS; クレタ人): uterque(両者とも)(イドメネウスとメリオネス)
  - Idomeneus (IDOMENEUS; イドメネウス): クレタ人、メリオネスとともに八十隻をトロイアへ率いる
  - Meriones (MERIONES; メリオネス): とイドメネウス、二人ともクレタ人で、八十隻を率いる
- [6] 208 Idomeneus et Meriones, Cretaeus uterque,
  - Cretaeus (Cretaeus; クレタ人): Idomeneus et Meriones, Cretaeus uterque 208
  - Idomeneus (Idomeneus; イドメネウス): Idomeneus et Meriones, Cretaeus uterque 208
  - Meriones (Meriones; メリオネス): Idomeneus et Meriones, Cretaeus uterque 208

209 bis quadragenis muniti nauibus ibant;
- [2] 208 Bis quadragenis muniti navibus ibant;
- [3] 209 Bis quadragenis muniti nauibus ibant.
- [4] 209 Bis quadragenis muniti navibus ibant.
- [6] 209 bis quadragenis muniti navibus ibant.

210 et totidem puppes clara de gente Menestheus
- [2] 209 Et totidem puppes clara de gente Menestheus
  - メネステウスはアテナイから50隻の船を率いた。ホメロス『イリアス』II, 552。ディクテュスとダレースは彼をムネステウス（Mnestheus）と呼び、同数の船を彼に割り当てている。…
- [3] 210 Et totidem puppes clara de gente Menestheus
- [4] 210 Et totidem puppes clara de gente Menestheus
  - Menestheus …（同所 552）。
  - Menestheus (MENESTHEUS; メネステウス): 名高い家柄の者、アテナイ人、五十隻を率いる
- [6] 210 et totidem puppes clara de gente Menestheus
  - Menestheus (Menestheus; メネステウス): *Menestheus . . . Athenaeus 210

211 duxit Athenaeus, quot uiribus ambit Achilles;
- [2] 210 Duxit Athenaeus, quot viribus ambit Achilles:
  - *Athenaeus*（アテナイ人）。アテナイ人の指揮官だからである。…というのも、メネステウスはアキレウスが率いていたのと同じ数、すなわち50隻の船を有していたことを言おうとしているからである。191行を参照。…
- [3] 211 Duxit Athenaeus, quot uiribus addit Achilles.
- [4] 211 Duxit Athenaeus, quot viribus addit Achilles.
  - Achilles (ACHILLES; アキレウス): — 五十隻の船を率いた
- [6] 211 duxit Athenaeus, quot viribus ambit Achilles.
  - Achilles (Achilles; アキレウス): -es 211. 988. 997. 1014. 1043
  - Athenaeus (Athenaeus; アテナイ人): Menestheus . . . Athenaeus 211

212 Amphimachusque ferox et Thalpius, Elide nati,
- [2] 211 Amphimachusque ferox etThalpius, Elide nati,
  - *Et Thalpius*（そしてタルピオス）は、ホメロス『イリアス』II, 620 に基づいて私が復元した。…
- [3] 212 Amphimachusque ferox et Thalpius, Elide nati,
- [4] 212 Amphimachusque ferox et Thalpius, Elide nati,
  - Thalpius …（同所 620）。
  - Amphimachus (AMPHIMACHUS princeps Epeorum; アムピマコス、エペイオス人の将): — 猛き者、エリス生まれ
  - Elide (ELIS; エリス): Elide nati:エリス生まれのアムピマコスとタルピオス
  - Thalpius (THALPIUS; タルピオス): エリス生まれ、ギリシアの将たちの中に
- [6] 212 Amphimachusque ferox et Thalpius, Elide nati,
  - Amphimachus (Amphimachus 1; アムピマコス 1): Amphimachus . . . ferox et Thalpius, Elide nati 212:エペイオス人の将たち
  - Elide (Elis; エリス): Amphimachus . . . et Thalpius, Elide nati 212
  - Thalpius (Thalpius; タルピオス): Amphimachus . . . et *Thalpius (alpinus trad.), Elide nati 212

213 et clara uirtute Polyxenus atque Diores,
- [2] 212 Et clari virtute Polyxenus atque Diores,
  - … ホメロスは彼らをエリス出身のアムピマコスおよびタルピオスとともに結びつけており、ディクテュス（I, 17）も同様である。
- [3] 213 Et clara uirtute Polyxenus atque Diores.
- [4] 213 Et clara virtute Polyxenus atque Diores.
  - Diores (DIORES; ディオレス): ギリシアの他の将たちとともに
  - Polyxenus (POLYXENUS; ポリュクセノス): 名高い武勇の者、ギリシアの将たちの中に
- [6] 213 et clara virtute Polyxenus atque Diores,
  - Diores (Diores; ディオレス): Diores 213:エペイオス人の将
  - Polyxenus (Polyxenus; ポリュクセノス): clara virtute Polyxenus 213:エリスの人、アガステネスの子

214 hi bis uicenas onerarunt milite puppes.
- [2] 213 Hi bis vicenas onerarunt milite naves :
- [3] 214 Hi bis uicenas onerarunt milite naues.
- [4] 214 Hi bis vicenas onerarunt milite naves.
- [6] 214 hi bis vicenas onerarunt milite puppes.

215 Protesilaus agit totidem fortisque Podarces
- [2] 214 Protesilaus agit totidem, fortisque Podarces
  - ポダルケスとプロテシラオスはピュラケおよび支配下の他の地から40隻の船を率いてきた。ホメロス『イリアス』II, 704、およびディクテュス前掲書。…
- [3] 215 Protesilaus agit totidem fortisque Podarces
- [4] 215 Protesilaus agit totidem fortisque Podarces
  - Podarces (PODARCES; ポダルケス): 勇敢な者、ギリシアの将たちの中に
  - Protesilaus (PROTESILAUS; プロテシラオス): 四十隻をトロイアへ率いる
- [6] 215 Protesilaus agit totidem fortisque Podarces
  - Podarces (Podarces; ポダルケス): fortis . . . Podarces 215:プロテシラオスの兄弟、イピクロスの子
  - Protesilaus (Protesilaus; プロテシラオス): Protesilaus 215

216 instructas puppes, quot duxit Oileos Aiax;
- [2] [215] [Instructas puppes, quas duxit Oileus Ajax].
- [3] 216 Iustructas puppes, quot duxit Oileos Aiax.
- [4] 216 Instructas puppes, quot duxit Oileos Ajax.
  - Ajax (AJAX Oilei filius; アイアス、オイレウスの子): — オイレウスの子:プロテシラオスとポダルケスは彼と同じ数の船を整えた
- [6] 216 instructas puppes, quot duxit Oileos Aiax.
  - Aiax (Aiax (Locrus); アイアス（ロクリス人）): Oileos (-us trad.) -ax 216
  - Oileos (Oileus; オイレウス): Oileos (-us trad.) Aiax 216

217 et septem Poeante satus tulit arma carinis,
- [2] 216 At septem Poeante satus tulit arma cariBis,
  - … すなわちピロクテテスのことであり、ホメロス『イリアス』II, 719 は彼が7隻の船を指揮したと記している。…
- [3] 217 Et septem Poeante satus dat in arma carinas.
- [4] 217 Et septem Poeante satus dat in arma carinas.
  - Poeante (POEAS; ポイアス): Poeante satus:ポイアスの子(ピロクテテス)
- [6] 217 et septem Poeante satus tulit arma carinis.
  - Poeante (Poeas; ポイアス): *Poeante (phetonte trad.) satus 217:ピロクテテス

218 quem sequitur iuxta Podalirius atque Machaon,
- [2] 217 Quem sequitur juxta Podalirius atque Machaon,
  - … 両者とも医者であり、ともにアエスクラピウスの子であった。そしてマカオンは Virg. Aen. II, 263 にも言及されている。パリ編者。
- [3] 218 Quem sequitur iuxta Podalirius atque Machaon,
- [4] 218 Quem sequitur juxta Podalirius atque Machaon,
  - Machaon (MACHAON; マカオン): ギリシアの将たちの中に
  - Podalirius (PODALIRIUS; ポダレイリオス): ギリシアの将たちの中に
- [6] 218 quem sequitur iuxta Podalirius atque Machaon,
  - Machaon (Machaon; マカオン): Machaon 218:アエスクラピウスの子
  - Podalirius (Podalirius; ポダレイリオス): Podalirius *218

219 altaque ter denis sulcarunt aequora proris.
- [2] 218 Altaque ter denis sulcarunt aequora proris.
  - *Altaque ter denis*（そして深き海を30隻の）。上の193行と同じ行である。われらの詩人は、自身が編纂の拠り所としているホメロス自身の例に倣って、同じ事柄について同一または類似の行を作ることを好む。
- [3] 219 Altaque ter denis sulcarunt aequora proris.
- [4] 219 Altaque ter denis sulcarunt aequora proris.
- [6] 219 altaque ter denis sulcarunt aequora proris.

220 His ducibus Graiae Troiana ad litora puppes
- [2] 219 His ducibus Graiae Trojana ad litora puppes
- [3] 220 His ducibus Graiae Troiana ad litora puppes
- [4] 220 His ducibus Grajae Trojana ad litora puppes
  - Grajae (GRAJUS; ギリシアの): Grajae puppes:ギリシアの船尾
  - Trojana (TROJANUS; トロイアの): ad Trojana litora:トロイアの岸へ
- [6] 220 his ducibus Graiae Troiana ad litora puppes
  - Graiae (Graius; ギリシアの): -ae . . . puppes 220
  - Troiana (Troianus; トロイアの): -na ad litora 220

221 bis septem uenere minus quam mille ducentae.
- [2] 220 Bis septem venere minus, quam mille ducentae.
  - *Quam mille ducentae*（1200隻より）、すなわち1186隻の船［1200隻より2×7＝14隻少ない］。ホメロス自身の数である。バルトが前掲書で指摘しているように、ディクテュスはトロイアに来航した船の数を1117隻、ダレースは1148隻としている。アンヌ・ダシエはディクテュスからギリシア軍の船を1153隻、ダレースから1140隻と数えており、エウリーピデース『オレステース』の古註者は1155隻、ケドレーノスは1148隻、ツゥキュディデースおよびクリュソストモスは1200隻と数えていると述べている。
- [3] 221 Bis septem uenere minus quam mille ducentae.
- [4] 221 Bis septem venere minus quam mille ducentae.
- [6] 221 bis septem venere minus quam mille ducentae.

222 Iamque citi appulerant classes camposque tenebant,
- [2] 221 Jamque citae adpulerant classes, camposquetenebant,
- [3] 222 Iamque citam appulerant classem camposque tenebant,
- [4] 222 below Jamque citam appulerant classem camposque tenebant
- [6] 222 iamque citae appulerant classes camposque tenebant,
  - … 作者は詩的許容を過分に行使している
  - campos (Troia; トロイア): また campos 222 を参照

223 cum pater ad Priamum mittit Saturnius Irim,
- [2] 222 Tunc pater ad Priamum misit Saturnius Irim,
- [3] 223 Cum pater ad Priamum mittit Saturnius Irim,
- [4] 223 Tum pater ad Priamum mittit Saturnius Irim
  - Irim (IRIS; イリス): Irin:ユピテルがイリスをプリアモスのもとへ送る
  - pater (JUPPITER; ユピテル): — サトゥルヌスの子がイリスをプリアモスのもとへ送る
  - Priamum (PRIAMUS; プリアモス): Ad Priamum:ユピテルがイリスをプリアモスのもとへ送る
- [6] 223 cum pater ad Priamum mittit Saturnius Irin,
  - Irin (Iris; イリス): Irin 223
  - pater (Iuppiter; ユピテル): pater . . . Saturnius 223
  - Priamum (Priamus; プリアモス): ad -mum 223
  - Saturnius (Saturnius; サトゥルヌスの子): pater . . . Saturnius 223:ユピテル

224 quae doceat fortes uenisse ad bella Pelasgos.
- [2] 223 Quae doceat, fortes venisse ad bella Pelasgos.
- [3] 224 Quae doceat fortes uenisse ad bella Pelasgos.
- [4] 224 Quae doceat fortes venisse ad bella Pelasgos.
  - Pelasgos (GRAI; ギリシア人): Pelasgos:イリスはユピテルの命により、ペラスゴイがトロイアに来たことをトロイア人に告げる
- [6] 224 quae doceat fortes venisse ad bella Pelasgos.
  - Pelasgos (Pelasgi; ペラスゴイ): fortes . . . -os 224. 353

225 Nec mora: continuo iussu capit arma parentis
- [2] 224 Nec mora, continuo jussu capit arma parentis
- [3] 225 Nec mora: continuo iussu capit arma parentis
- [4] 225 Nec mora : continuo jussu capit arma parentis
- [6] 225 nec mora, continuo iussu capit arma parentis
  - parentis (Priamus; プリアモス): parentis 225. 1038. 1044

226 Priamides Hector totamque in proelia pubem
- [2] 225 Priamides Hector, totamque in praelia pubem
  - *Totamque in praelia pubem*（そしてすべての若者を戦いへと）。Virgil. Aen. VII, 429: « armari pubem, portisque moveri Laetus in arma para »。
- [3] 226 Priamides Hector totamque in praelia pubem
- [4] 226 Priamides Hector totamque in proelia pubem
  - Hector (HECTOR; ヘクトル): 主格:プリアモスの子が父の命で武器をとる
- [6] 226 Priamides Hector totamque in proelia pubem
  - Hector (Hector; ヘクトル): Priamides -or 226
  - Priamides (Priamides; プリアミデス): -es Hector 226
  - pubem (Troianus; トロイアの): 226 pubem

227 festinare iubet portisque agit agmen apertis.
- [2] 226 Festinare jubet, portisque agit agmen apertis.
  - *Portis ... agmen apertis*（開かれた門から……隊列を）。Virg. Aen. XII, 121: « pilataque plenis Agmina se fundunt portis »。
- [3] 227 Festinare iubet portisque agit agmen apertis.
- [4] 227 Festinare jubet portisque agit agmen apertis.
- [6] 227 festinare iubet portisque agit agmen apertis.
  - portis (Troia; トロイア): portis 227. 575

228 Cui fulgens auro cassis iuuenile tegebat
- [2] 227 Cui fulgens auro cassis juvenile tegebat
- [3] 228 Cui fulgens auro cassis iuuenile tegebat
- [4] 228 Cui fulgens auro cassis juvenile tegebat
- [6] 228 cui fulgens auro cassis iuvenile tegebat

229 omni parte caput, munibat pectora thorax
- [2] 228 Omni parte caput, munibat pectora thorax,
- [3] 229 Omni parte caput, munibat pectora thorax,
- [4] 229 Omni parte caput, munibat pectora thorax,
- [6] 229 omni parte caput, munibat pectora thorax

230 et clipeus laeuam, dextram decorauerat hasta
- [2] 229 Et laevam clypeus, dextram decoraverat hasta,
- [3] 230 Et clipeus laeuam, dextram decorauerat hasta
- [4] 230 Et clipeus laevam, dextram decoraverat hasta
- [6] 230 et clipeus laevam, dextram decoraverat hasta

231 ornabatque latus mucro; simul alta nitentes
- [2] 230 Ornabatque latus mucro, simui alta nitentes
- [3] 231 Ornabatque latus mucro; simul alta nitentes
- [4] 231 Ornabatque latus mucro; simul alta nitentes
- [6] 231 ornabatque latus mucro; simul alta nitentes

232 crura tegunt ocreae, quales decet Hectoris esse.
- [2] 231 Crura tegunt ocrea, quales decet Hectoris essc.
  - *Quales decet Hectoris esse*（ヘクトルのものにふさわしいような）。オウィディウス風の定型表現である、Met. II, 14: « facies non omnibus una, Non diversa tamen: qualem decet esse sororum »。バルトは前掲書で、パリスに関するこの行およびそれに続く諸行について、見事で重厚であり、必要な事柄のすべてを簡潔に包括しているとして称賛すべきであると見なしている。
- [3] 232 Crura tegunt ocreae, quales decet Hectoris esse.
- [4] 232 Crura tegunt ocreae, quales decet Hectoris esse.
  - Hectoris (HECTOR; ヘクトル): Hectoris:ふさわしいように、輝く脛当てがヘクトルの脚を覆う
- [6] 232 crura tegunt ocreae, quales decet Hectoris esse.
  - Hectoris (Hector; ヘクトル): -oris 232. 565. 1006. 1040

233 Hunc sequitur forma melior, tunc fortis in armis,
- [2] 232 Hunc sequitur forma melior, non fortis in armis,
- [3] 233 Hunc sequitur forma melior nec fortis in armis
- [4] 233 Hunc sequitur forma melior quam fortior armis,
- [6] 233 hunc sequitur forma melior, tunc fortis in armis,

234 belli causa Paris, patriae funesta ruina,
- [2] 233 Belli caussa Paris, patriaa funesta ruina,
- [3] 234 Belli causa Paris, patriae funesta ruina;
- [4] 234 Belli causa Paris, patriae funesta ruina
  - Paris (PARIS; パリス): 主格:戦の原因、祖国の死をもたらす破滅、トロイア人の他の将たちとともに武器をとる
- [6] 234 belli causa Paris, patriae funesta ruina,
  - Paris (Paris; パリス): tunc fortis in armis belli causa Paris, patriae funesta ruina 234

235 Deiphobusque Helenusque simul fortisque Polites
- [2] 234 Deiphobusque , Helenusque simul, fortisque Polites,
  - … ホメロス『イリアス』II, 701（実際は791）にあるように *Polites* …
- [3] 235 Deiphobusque Helenusque simul fortisque Polites,
- [4] 235 Deiphobusque Helenusque simul fortisque Polites,
  - Deiphobus (DEIPHOBUS; デイポボス): トロイア人の他の将たちとともに
  - Helenus (HELENUS; ヘレノス): トロイア人の将たちの中に
  - Polites (POLITES Priami filius; ポリテス、プリアモスの子): 勇敢な者、トロイア人の将たちの中に
- [6] 235 Deiphobusque Helenusque simul fortisque Polites,
  - Deiphobus (Deiphobus; デイポボス): Deiphobus 235
  - Helenus (Helenus; ヘレノス): Helenus 235
  - Polites (Polites; ポリテス): fortis . . . Polites 235:プリアモスの子

236 et sacer Aeneas, Veneris certissima proles,
- [2] 235 Et sacer Aeneas, Veneris certissima proles,
- [3] 236 Et sacer Aeneas, Veneris certissima proles,
- [4] 236 Et sacer Aeneas, Veneris certissima proles,
  - Aeneas (AENEAS; アイネイアス): 聖なる者、ウェヌスのまごうかたなき子(われらの詩人がトロイア人の将たちを列挙する)
  - Veneris (VENUS; ウェヌス): Veneris:ウェヌスの子、アイネイアス
- [6] 236 et sacer Aeneas, Veneris certissima proles,
  - Aeneas (Aeneas; アイネイアス): sacer -as, Veneris certissima proles 236
  - Veneris (Venus; ウェヌス): Aeneas, -eris . . . proles 236. 483

237 Archelochusque Acamasque ferox Antenore creti;
- [2] 236 Archilochusque, Acamasque ferox, Antenore nati:
  - *Acamasque*（そしてアカマス）。ホメロス『イリアス』II, 823。…
- [3] 237 Archilochusque Acamasque ferox Antenore creti.
- [4] 237 Archilochusque Acamasque ferox Antenore creti.
  - Acamas (ACAMAS Antenoris filius; アカマス、アンテノルの子): — 猛き者、アンテノルから生まれた者
  - Antenore (ANTENOR; アンテノル): Antenore creti:アンテノルから生まれたアルケロコスとアカマス
  - Archilochus (ARCHILOCHUS; アルケロコス): アンテノルから生まれた者、トロイア人の他の将たちとともに
- [6] 237 Archelochusque Acamasque ferox Antenore creti.
  - Acamas (Acamas 1; アカマス 1): Acamas、アンテノルの子、トロイア人 237
  - Antenore (Antenor 1; アンテノル 1): Archelochusque Acamasque ferox Antenore creti 237:トロイア人の
  - Archelochus (Archelochus; アルケロコス): Archelochusq. Acamasque . . . Antenore creti 237

238 nec non et proles generosa Lycaonis ibat
- [2] 237 Nec non et proles generosa Lycaonis ibat
- [3] 238 Nec non et proles generosa Lycaonis ibat
- [4] 238 Nec non et proles generosa Lycaonis ibat
  - Pandarus (PANDARUS; パンダロス): リュカオンの高貴な子、トロイア人の援軍の中に
- [6] 238 nec non et proles generosa Lycaonis ibat
  - Lycaonis (Lycaon; リュカオン): proles generosa Lycaonis . . . Pandarus 238

239 Pandarus et magnae Glaucus uirtutis in armis
- [2] 238 Pandarus , et magn» virtutis Glaucus in armis ,
  - *Glaucus in armis*（武装せるグラウコス）。ホメロスは『イリアス』第2巻末尾で、彼をリュキア人の指導者サルペドンと結びつけており、われらの詩人も下の248行で彼について述べている。
- [3] 239 Pandarus et magnae Glaucus uirtutis in armis;
- [4] 239 Pandarus et magnae Glaucus virtutis in armis;
  - Glaucus (GLAUCUS Lyciorum dux; グラウコス、リュキア人の将): — 武器において大いなる武勇の者、トロイア人の援軍の中に
- [6] 239 Pandarus et magnae Glaucus virtutis in armis;
  - Glaucus (Glaucus; グラウコス): magnae Glaucus virtutis in armis 239
  - Pandarus (Pandarus; パンダロス): proles generosa Lycaonis . . . Pandarus 239

240 Amphiusque et Adrastus et Asius atque Pylaeus.
- [2] 239 Amphionque, Adrastus, et Asius, atque Pylaeus.
  - 私はホメロス『イリアス』II, 830 に基づいて *Amphiusque Adrastus* と記し、同 838 に基づいて *Asius* と記す。…ホメロスは彼をラリサのヒッポトオスと結びつけており（II, 842）、われらの詩人が他の箇所で彼を持ち出しているのを私は見ていないからである。…
- [3] 240 Amphiusque et Adrastus et Asius atque Pylaeus.
- [4] 240 Amphiusque et Adrastus et Asius atque Pylaeus.
  - Amphius …（『イリアス』II, 830）。… Pylaeus …（同所 842）。
  - Adrastus (ADRASTUS; アドラストス): トロイア人の将たちの中に
  - Amphius (AMPHIUS; アムピオス): トロイア人の同盟者
  - Asius (ASIUS Hyrtaci filius; アシオス、ヒュルタコスの子): — トロイア人の他の同盟者たちとともに
  - Pylaeus (PYLAEUS; ピュライオス): トロイア人の将たちの中に
- [6] 240 Amphiusque et Adrastus et Asius atque Pylaeus.
  - Adrastus (Adrastus; アドラストス): Amphiusque et Adrastus、メロプスの子ら 240
  - Amphius (Amphius; アムピオス): Amphīus 240
  - Asius (Asius; アシオス): Asius 240. 774:ヒュルタコスの子、トロイア側
  - Pylaeus (Pylaeus; ピュライオス): *Pylaeus (ephialtes trad.) 240:レトスの子、ペラスゴイ

241 Ibat et Amphimachus Nastesque, insignis uterque,
- [2] 240 Ibat et Amphimachus, Nastesque, insignis uterque,
  - カリアのアムピマコスとナステスは、ホメロス『イリアス』II, 870 によって結びつけられている。…
- [3] 241 Ibat et Amphimachus Nastesque, insignis uterque,
- [4] 241 Ibat et Amphimachus Nastesque, insignis uterque,
  - Nastes …（同所 870）。
  - Amphimachus (AMPHIMACHUS princeps Carum; アムピマコス、カリア人の将): トロイア人の他の同盟者たちとともに際立つ
  - Nastes (NASTES; ナステス): 際立った者、トロイア人の同盟者の中に
- [6] 241 ibat et Amphimachus Nastesque, insignis uterque,
  - Amphimachus (Amphimachus 2; アムピマコス 2): Amphimachus Nastesque 241:カリア人の将たち
  - Nastes (Nastes; ナステス): Amphimachus *Nastesque, insignis uterque 241:カリア人の将たち

242 magnanimique duces Odiusque et Epistrophus ingens
- [2] 241 Magnanimique duces Hodius et Epistrophus ingens,
  - オディオスとエピストロポスはハリゾネスの王ミーノースの子である。ディクテュス II, 35 はこのように記し、ホメロスも856行で同じ両者を結びつけている。…
- [3] 242 Magnanimique duces Hodiusque et Epistrophus ingens
- [4] 242 Magnanimique duces Hodiusque et Epistrophus ingens
  - **242, 243, 244** Hodius, Pyraechmes, Mesthles …（同所 856, 848, 864）。
  - Epistrophus (EPISTROPHUS Halizonum dux; エピストロポス、ハリゾネスの将): — 巨大な者、心大いなる将
  - Hodius (HODIUS; オディオス): 心大いなる将、トロイア人の援軍の中に
- [6] 242 magnanimique duces Odiusque et Epistrophus ingens
  - Epistrophus (Epistrophus 2; エピストロポス 2): Epistrophus ingens 242:トロイア側のハリゾネスの将
  - Odius (Odius; オディオス): Odius . . . et Epistrophus 242:ハリゾネスの将たち

243 Euphemusque ferox clarusque aetate Pyraechmes,
- [2] 242 Euphemusque ferox, clarusque aetate Pyraechmes,
  - … キコネスの指揮官エウペモスとパイオニア人のピュライクメスは、ホメロス（846行および848行）に言及されている。…
- [3] 243 Euphemusque ferox clarusque aetate Pyraechmes;
- [4] 243 Euphemusque ferox clarusque aetate Pyraechmes;
  - Euphemus (EUPHEMUS; エウペモス): 猛き者
  - Pyraechmes (PYRAECHMES; ピュライクメス): 年齢で名高い者、トロイア人の同盟者の中に
- [6] 243 Euphemusque ferox clarusque aetate Pyraechmes;
  - Euphemus (Euphemus; エウペモス): Euphemus . . . ferox 243:トロイア側のキコネスの将
  - Pyraechmes (Pyraechmes; ピュライクメス): clarus . . . aetate *Pyraechmes 243:パイオニア人の将

244 cum quibus et Mesthles atque Antiphus et bonus armis
- [2] 243 Cum quibus etMesthlesatque Antiphus, et bonusarmis
  - *Et Mesthles atque Antiphus*（そしてメストレスとアンティポス）、マイオニア人。ホメロス 864 行。…
- [3] 244 Cum quibus et Mesthles atque Antiphus et bonus armis
- [4] 244 Cum quibus et Mesthles atque Antiphus et bonus armis
  - Antiphus (ANTIPHUS Maeonum ductor; アンティポス、マイオニア人の指揮者): — トロイア人に助けをもたらす
  - Hippothous (HIPPOTHOUS; ヒッポトオス): 武器に優れた者、トロイア人の同盟者の中に
  - Mesthles (MESTHLES; メストレス): トロイア人の援軍の中に
- [6] 244 cum quibus et Mesthles atque Antiphus et bonus armis
  - Antiphus (Antiphus 2; アンティポス 2): Antiphus 244:タライメネスの子、トロイア側のマイオニア人の将
  - Mesthles (Mesthles; メストレス): *Mesthles 244:タライメネスの子、アンティポスの兄弟、マイオニア人の将

245 Hippothous uenere Acamasque et Pirous una,
- [2] 244 Hippdthus atque Acamas venere, et Pirous una,
  - … しかし、ホメロスが主要な指揮官たちの間で、かつアカマスの直前に名を挙げているヒッポトオスを、われらの詩人が省いたとは思われないし、この箇所以外のどこかに置いたとも思われない。…なぜならホメロスは844行でペイロスあるいはペイロオスをアカマスと結びつけており、ピュライオスはすでに上で場所を見出しているからである。
- [3] 245 Hippothousque Acamasque iuere et Pirous una,
- [4] 245 Hippothous venere Acamasque et Pirous, \< ense
  - Hippothous …（同所 840）…
  - Acamas (ACAMAS dux Thracum; アカマス、トラキア人の将): — トロイア人の同盟者の中に
  - Pirous (PIROUS; ペイロオス): <剣と武勇に優れた者> トロイア人の援軍の中に
- [6] 245 Hippothous † atque Acamas † venere Pirous una,
  - Acamas (Acamas 2; アカマス 2): Acamas (ath- trad.)、トラキア人 245
  - Hippothous (Hippothous; ヒッポトオス): bonus armis *Hippothous 245:レトスの子
  - Pirous (Pirous; ペイロオス): *Pirous (pierius trad.) 245:トラキア人の将

245a
- [2] —
- [3] —
- [4] 245 bis Et virtute potens, animique Pylaemenis > una,
  - Pylaemenis (PYLAEMEN; ピュライメネス): < Pylaemenis animi >
- [6] —

246 Arsinooque sati Chromiusque atque Ennomus, ambo
- [2] 245 Alcinoque sati, Chromiusque ac Ennomus, ambo
  - … そしてこのきわめて博学な人物（ボンダム）自身、アウソニウスの『英雄たちの墓碑銘』第22詩を引用しており、そこではエンノモスとクロミオスの父はアルキノス（Alcinus）と呼ばれている。…ホメロスのもとには父の名は現れず、858行でクロミスとエンノモスがミュシア人を率いていたと述べるのみである。しかしわれらの詩人は他の諸源泉から多くのものを汲み取るのが常である。
- [3] 246 Alcinooque sati Chromiusque atque Ennomus, ambo
- [4] 246 Alcinooque sati Chromiusque atque Ennomus, ambo
  - Alcinoo (ALCINOUS; アルキノオス): Alcinoo sati:アルキノオスの子クロミオスとエンノモス
  - Chromius (CHROMIUS dux Mysorum; クロミオス、ミュシア人の将): 年盛りの男、トロイア人の同盟者の中に
  - Ennomus (ENNOMUS; エンノモス): 年盛りの男、トロイア人の同盟者の中に
- [6] 246 Arsinooque sati Chromiusque atque Ennomus, ambo
  - Arsinooque … (アポロドロス『サマリー』3, 35 p. 199 ワーグナーによる) …
  - Arsinoo (Arsinous; アルシノオス): *Arsinooque sati Chromiusque atque Ennomus 246
  - Chromius (Chromius 1; クロミオス 1): Arsinooque sati Chromiusque atque Ennomus, ambo florentes aetate viri 246:トロイア側のミュシア人の将たち(ホメロスでは Χρόμις)
  - Ennomus (Ennomus; エンノモス): *Ennomus 246

247 florentes aetate uiri, quos Phorcus et ingens
- [2] 246 Florentes aetate viri , quos Phorcis et ingens
  - … 862行でポルキュスとアスカニオスをプリュギア人の指揮官として結びつけているホメロスの典拠に基づいて … このアスカニオスは、アイネイアスの息子（当時はまだほんの幼子であった）と区別されねばならない。
- [3] 247 Florentes aetate uiri, quos Phorcus et ingens
- [4] 247 Florentes aetate viri, quos Phorcus et ingens
  - Ascanius (ASCANIUS Hippotionis filius; アスカニオス、ヒッポティオンの子): — 巨大な者、トロイア人の同盟者
  - Phorcus (PHORCUS; ポルキュス): トロイア人の将たちの中に
- [6] 247 florentes aetate viri, quos Phorcus et ingens
  - Phorcus (Phorcus; ポルキュス): Phorcus 247:プリュギア人の将

248 Ascanius sequitur, simul et Iouis inclita proles
- [2] 247 Ascanius sequitur, simul et Jovis inciyta proles
  - *Jovis inclyta proles*（ユピテルの名高き末裔）。Ovidius, Met. IX, 229。
- [3] 248 Ascanius sequitur, simul et Iouis inclita proles
- [4] 248 Ascanius sequitur, simul et Jovis inclita proles
  - Jovis (JUPPITER; ユピテル): — 子(サルペドン)
  - Sarpedon (SARPEDON; サルペドン): ユピテルの名高き子、トロイア人の同盟者の中に
- [6] 248 Ascanius sequitur, simul et Iovis inclita proles
  - Ascanius (Ascanius; アスカニオス): ingens Ascanius 248:プリュギア人の将
  - Iovis (Iuppiter; ユピテル): Iovis inclita proles Sarpedon 248. 520

249 Sarpedon claraque satus tellure Coroebus.
- [2] 248 Sarpedon, claraque satus tellure Coroebus.
  - … なおホメロスはこのコロイボスを挙げていないが、ウェルギリウスは彼をミュグドンの子と呼び、トロイア軍の救援に駆けつけてペネレオスに討たれたと伝えている（Aen. II, 341 および 425）。クイントゥス・スミュルナエウス（クイントゥス・カラベル）XIII, 168 以下では、彼はディオメデスに討たれるとされている。これに対してホメロスはパプラゴニア人の指導者ピュライメネスをトロイア軍の同盟者の中に挙げているが、われらの詩人は、私の見誤りでなければ、彼を省いている。コロイボスについては、名士ハイネが『アエネーイス』第2巻への補論（Excurs. X）で記した多くの注記を参照されたい。――別のコロイボスがスターティウスの Theb. I, 650 で言及されている。パリ編者。
- [3] 249 Sarpedon claraque satus tellure Pylaemen.
  - … Coroebus …しかしこの人物はホメロスにおいて言及されておらず、Pylaemenes だけがいまだ名指されずに残っている。書写者たちがウェルギリウスから彼を持ち込んだのである。…
- [4] 249 Sarpedon claraque satus tellure Coroebus.
  - Coroebus …（『アエネーイス』II, 342 を参照）。…
  - Coroebus (COROEBUS; コロイボス): 名高い土地から生まれた者
- [6] 249 Sarpedon claraque satus tellure Coroebus.
  - Coroebus (Coroebus; コロイボス): clara . . . satus tellure Coroebus 249:ホメロスでは名を挙げられない
  - — (Pylaemenes; ピュライメネス): また 249 行も参照
  - Sarpedon (Sarpedon; サルペドン): Iovis inclita proles Sarpedon 249. 521

250 His se defendit ducibus Neptunia Troia
- [2] 249 His se defendit ducibus Meptunia Troja,
  - *Neptunia Troja*（ネプトゥヌスのトロイア）：Virgilius, Aen. II, 625 および III, 3 より。
- [3] 250 His se defendit ducibus Neptunia Troia,
- [4] 250 His se defendit ducibus Neptunia Troja,
  - Neptunia (NEPTUNIUS; ネプトゥヌスの): Neptunia Troja:ネプトゥヌスのトロイア
  - Troja (TROJA; トロイア): ネプトゥヌスのトロイアはこれらの将たち(われらの詩人がすでに列挙した者たち)で身を守る
- [6] 250 his se defendit ducibus Neptunia Troia,
  - Neptunia (Neptunius; ネプトゥヌスの): Neptunia Troia 250
  - Troia (Troia; トロイア): Neptunia -ia 250

251 uicissetque dolos Danaum, ni fata fuissent.
- [2] 250 Vicissetque doios Danauin , nisi fata vetassent.
- [3] 251 Uicissetque dolos Danaum, ni fata fuissent.
- [4] 251 Vicissetque dolos Danaum, ni fata fuissent.
  - Danaum (GRAI; ギリシア人): — 運命がなかったならば、トロイアはダナオイの策略に打ち勝ったであろう
- [6] 251 vicissetque dolos Danaum, ni fata fuissent.
  - Danaum (Danai; ダナオイ): -um(属格):19. 50. 67. 124. 153. 251. 268. 357. 389. 496. 631. 686. 691. 698. 705. 743. 747. 794. 1025

## Book 3

252 Iamque duae stabant acies fulgentibus armis,
- [2] 251 III. Jamque duae stabant acies fulgentibus armisy
- [3] 252 Iamque duae stabant acies fulgentibus armis,
- [4] 252 Jamque duae stabant acies fulgentibus armis,
- [6] 252 iamque duae stabant acies fulgentibus armis,

253 cum Paris, exitium Troiae funestaque flamma,
- [2] 252 Quum Paris, exitium Trojae funestaque flamma,
  - … バルトはこの箇所について『雑考』LIX, 第1章で、致命的な災厄をもたらす張本人を災厄そのものの名で呼ぶのが最良の著作家たちの慣習であると指摘している。ユウェナーリスがドミティアヌス帝について次のように述べる通りである: « si peste et clade sub illa Saevitiam damnare, et honestum afferre liceret Consilium »。カティリーナ弾劾演説の著者: « vigent enim in illa clade res diversissimae pariter, continentia et libido »。ラムプリディウス『ヘリオガバルス伝』: « mirum fortasse cuipiam videatur, quod haec clades, quam retuli, loco principis fuerit »。セネカ『メーデア』について: « Abolere ferro pessimam propera luem »。クラウディアヌス『ルフィヌス論』第1巻: « quo tanta lues eruperit ortu »。バルト。――また *flamma*（炎）が保たれるべき最大の理由は、それがパリスの生母ヘカベが松明を産み落とし、それによってトロイアと全アジアが火災で荒廃するという夢を見たという神話により適切に合致するからである。パリ編者。
- [3] 253 Cum Paris, exitium Troiae funestaque flamma,
- [4] 253 Cum Paris, exitium Trojae funestaque flamma,
  - Paris (PARIS; パリス): — トロイアの滅亡、死をもたらす炎、武装したメネラオスを見つける
  - Trojae (TROJA; トロイア): Trojae:トロイアの滅亡(パリス)
- [6] 253 cum Paris, exitium Troiae funestaque flamma,
  - Paris (Paris; パリス): Paris, exitium Troiae funestaque flamma 253
  - Troiae (Troia; トロイア): Paris exitium -iae 253

254 armatum aduerso Menelaum ex agmine cernit
- [2] 253 t Armatum adverso Menelaum ex agmine vidit,
- [3] 254 Armatum aduerso Menelaum ex agmine cernit
- [4] 254 Armatum adverso Menelaum ex agmine cernit
  - Menelaum (MENELAUS; メネラオス): Menelaum:パリスは武装したメネラオスを見つける
- [6] 254 armatum adverso Menelaum ex agmine cernit
  - Menelaum (Menelaus; メネラオス): -laum ex 254

255 seque uelut uiso perterritus angue recepit
- [2] 254 Seque velut viso perterritus angue recepit
  - … ホメロスが『イリアス』III, 33 以下で行い、われらの詩人がここでごく簡潔に表現している比喩を、ウェルギリウスは『アエネーイス』II, 378 以下でアンドロゲオースについて用いた: « Obstupuit, retroque pedem cum voce repressit. Improvisum aspris veluti qui sentibus anguem Pressit humi nitens, trepidusque repente refugit »。オウィディウスはより簡潔に Fast. II, 341 で: « Attonitusque metu rediit: ceu saepe viator Turbatum viso rettulit angue pedem »。ユウェナーリス I, 43: « Palleat, ut nudis pressit qui calcibus anguem »。
- [3] 255 Seque uelut uiso perterritus angue recepit
- [4] 255 Seque velut viso perterritus angue recepit
- [6] 255 seque velut viso perterritus angue recepit

256 ad socios amens. Quem postquam turpiter Hector
- [2] 255 Ad socios amens : quem postquam turpiter Hector
- [3] 256 Ad socios amens; quem postquam turpiter Hector
- [4] 256 Ad socios amens; quem postquam turpiter Hector
  - Hector (HECTOR; ヘクトル): — 恐怖に取り乱したパリスに呼びかける
- [6] 256 ad socios amens; quem postquam turpiter Hector
  - Hector (Hector; ヘクトル): Hector 256. 277. 491. 626. 677. 774. 959. 967. 979. 996. 1051

257 confusum terrore uidet: "O dedecus - inquit -
- [2] 256 Confusum terrore videt, «Proh! dedeciis, inquit,
- [3] 257 Confusum terrore uidet, 'o dedecus' inquit
- [4] 257 Confusum terrore videt : « O dedecus » inquit
  - — (PARIS; パリス): (ヘクトルがパリスを次のように言っていることもここに加えよ。「祖国の…永遠の恥辱、われらの一族の汚名」)
- [6] 257 confusum terrore videt, 'o dedecus' inquit
  - dedecus (Paris; パリス): ヘクトルの言葉 257 を参照:o dedecus . . . aeternum patriae generisque infamia nostri

258 "aeternum patriae generisque infamia nostri,
- [2] 257 Aeternum patriae, generisque infamia nostri,
  - *Generisque infamia nostri*（そしてわれらの種族の汚辱）。Ovid. Metam. VIII, 97: « o nostri infamia saecli »。
- [3] 258 'Aeternum patriae generisque infamia nostri,
- [4] 258 « Aeternum patriae generisque infamia nostri,
- [6] 258 'aeternum patriae generisque infamia nostri,

259 terga refers? At non dubitabas hospitis olim
- [2] 258 Terga refers? atnon dubitabas hospitis olim
- [3] 259 Terga refers? at non dubitabas hospitis olim
- [4] 259 Terga refers? at non dubitabas hospitis olim
- [6] 259 terga refers? at non dubitabas hospitis olim
  - hospitis (Menelaus; メネラオス): hospitis 259

260 expugnare toros, cuius nunc defugis arma
- [2] 259 Expugnare toros, cujus nunc defugis arma,
  - *Hospitis expugnare toros*（主人の床を強奪する）、すなわち言い寄りによって妻を捕らえ堕落させること。ちょうど〜のように攻め落と（ex- / -pugnari）...
  - **(cont.)** （前頁からの続き）［攻め落とされる（ex-）］pugnari とは、意に反して抵抗しながらも懇願によって屈服させられる者たちのことを言う。スエートーニウスもこのように用いている（Caes. 1, Tiber. 21）。オウィディウスの Her. XVII, 3 で、ヘレネはパリスに向かって次のように言う: « Ausus es, hospitii temeratis, advena, sacris, Legitimam nuptae sollicitare fidem »。プロペルティウス、III, 13, 9: « Haec etiam clausas expugnant arma pudicas »。――ルティリウス、Itin. I, 359: « Aurea legitimas expugnant munera taedas, Virgineosque sinus aureus imber emit »。パリ編者。――動詞 expugnare の用法については、バルトがスタティウスの Theb. IV, 187 への注でさらに多くを記している。
- [3] 260 Expugnare toros, cuius nunc defugis arma
- [4] 260 Expugnare toros, cujus nunc defugis arma
- [6] 260 expugnare toros, cuius nunc defugis arma

261 uimque times. Vbi sunt uires, ubi cognita nobis
- [2] 260 Vimque times : ubi nunc vires, ubi cognita nobis
- [3] 261 Uimque times! ubi sunt artes, ubi cognita nobis
- [4] 261 Vimque times! ubi sunt vires, ubi cognita nobis
- [6] 261 vimque times. ubi sunt vires, ubi cognita nobis

262 ludorum quondam uaria in certamina uis est?
- [2] 261 Ludorum quondam vario certamine vis est?
- [3] 262 Ludorum quondam uario in certamine mens est?
- [4] 262 Ludorum quondam vario in certamine virtus?
- [6] 262 ludorum quondam vario in certamine virtus?

263 Hic animos ostende tuos: nihil adiuuat armis
- [2] 262 Hic animos ostende tuos, nil adjuvat arnia
  - *Hic animos ostende*（ここで勇気を示せ）。ウェルギリウス『アエネーイス』VI, 261: « Nunc animis opus, Aenea, nunc pectore firmo »。…
- [3] 263 Hic animos ostende tuos: nihil adiuuat arma
- [4] 263 Hic animos ostende tuos : nihil adjuvat arma
- [6] 263 hic animos ostende tuos: nihil adiuvat armis
  - armis (すなわち戦いにおいて) …

264 nobilitas formae: duro Mars milite gaudet.
- [2] 263 Nobilitas formae, duro Mars miiite gaudet.
  - *Duro Mars milite gaudet*（マルスは頑強な兵士を喜ぶ）。ヘレネがパリスに向かって言う前掲箇所（オウィディウス『求愛書簡』XVII）、253 行: « Apta magis Veneri, quam sint tua corpora Marti »。
- [3] 264 Nobilitas formae: duro Mars milite gaudet.
- [4] 264 Nobilitas formae : duro Mars milite gaudet.
  - Mars (MARS; マルス): 頑強な兵士を喜ぶ
- [6] 264 nobilitas formae: duro Mars milite gaudet.
  - Mars (Mars; マルス): duro Mars milite gaudet 264

265 Dum iaceas in amore tuo, nos bella geremus
- [2] 264 Dum jaceas in amore tuo, nos beila geremus
  - *Dum jaceas in amore*（お前が愛の中に横たわっている間に）。すなわち、情欲に挫かれて倦怠し怠惰に過ごし、軍務に堪えられないこと。ウェルギリウス『カタレプトン』(Catal.) V, 1 にも同様の表現がある: « Jacere me, quod alta non possim, putas, Ut ante, vectari freta, Nec ferre durum frigus, aut aestum pati, Neque arma victoris sequi »。
- [3] 265 Dum iaceas in amore tuo, nos bella geremus
- [4] 265 Dum jaceas in amore tuo, nos bella geremus
- [6] 265 dum iaceas in amore tuo, nos bella geremus

266 scilicet et nostrum fundemus in hoste cruorem.
- [2] 265 Scilicet, et nostrum fundemus in hoste cniorem.
  - … *In hoste*（敵を相手に）は、前の *in amore tuo*（お前の愛の中に）に対比されている。なお、これらの詩行において作者はウェルギリウス『アエネーイス』XI, 371 を念頭に置いていたと思われる。そこではドランケースがトゥルヌスに向かって次のように言っている: « Scilicet, ut Turno contingat regia conjux, Nos, animae viles, inhumata infletaque turba, Sternamur campis »。また、我々が上に掲げたパルテノンにおけるアキレウスの演説の作者も、57 行で次のように言っている: « Scilicet, ut conjux viduo reddatur Atridi, Procumbat vilis Teucrorum victima Achilles »。
- [3] 266 Scilicet et nostrum fundemus in hoste cruorem!
- [4] 266 Scilicet et nostrum fundemus in hoste cruorem !
- [6] 266 scilicet et nostrum fundemus in hoste cruorem.

267 Aequius aduersis tecum concurrat in armis
- [2] 266 iEquius adversis tecum concurrat in armis
- [3] 267 Aequius aduersis tecum concurret in armis
- [4] 267 Aequius adversis tecum concurrat in armis
- [6] 267 aequius adversis tecum concurrat in armis

268 impiger Atrides, spectet Danaumque Phrygumque
- [2] 267 Impiger Atrides : spectet Danaumque Phrygumque
- [3] 268 Impiger Atrides: spectet Danaumque Phrygumque
- [4] 268 Impiger Atrides : spectet Danaumque Phrygumque
  - Danaum (GRAI; ギリシア人): — 民
  - Atrides (MENELAUS; メネラオス): Atrides:疲れを知らぬ者、武器をとってパリスと戦うがよい
  - Phrygum (TROJANI; トロイア人): Phrygum:プリュギア人の民
- [6] 268 impiger Atrides: spectet Danaumque Phrygumque
  - Atrides (Atrides (Menelaus); アトリデス（メネラオス）): impiger -des 268
  - Danaum (Danai; ダナオイ): -um(属格):19. 50. 67. 124. 153. 251. 268. 357. 389. 496. 631. 686. 691. 698. 705. 743. 747. 794. 1025
  - Phrygum (Phryges; プリュギア人): -gum . . . populus 268

269 depositis populus telis. Vos, foedere iuncto,
- [2] 268 Depositis telis populus, vos foedere juncto
  - *Populus*（民、人々）：*exercitus*（軍隊）の意味で用いられており、バルトが『雑考』(Adv.) LIX, 1 で指摘した通りである。下方の 280 行および 342 行でも同様である。
- [3] 269 Depositis populus telis, uos foedere iuncto
- [4] 269 Depositis populus telis, vos foedere juncto
- [6] 269 depositis populus telis, vos foedere iuncto

270 aduersas conferte manus, decernite ferro."
- [2] 269 Adversas conferle manus, decernite ferro
  - *Conferte manus*（手を交えよ／白兵戦を交えよ）。Virg. Aen. X, 876; XI, 283。
- [3] 270 Aduersas conferte manus, decernite ferro.'
- [4] 270 Adversas conferte manus, decernite ferro. »
- [6] 270 adversas conferte manus, decernite ferro.'

270a
- [2] 270 Vestrum nunc Helenam sumat quis rectius ipsam ».
- [3] —
- [4] —
- [6] —

271 Dixit. Quem contra paucis Priameius heros:
- [2] 271 Dixit, quae contra paucis Priameias heros,
- [3] 271 Dixit. quem contra paucis Priameius heros
- [4] 271 Dixit ; quem contra paucis Priameius heros
  - Priameius (PARIS; パリス): Priameius heros:プリアモスの子なる英雄がヘクトルに手短に答える
- [6] 271 dixit. quem contra paucis Priameius heros
  - Priameius (Priameius; プリアモスの): Priameius heros:パリス 271、ヘクトル 960

272 "Quid nimis indignis" - inquit - "me uocibus urges,
- [2] 272 «Quid nimis indignis, inquit, me vocibus urges,
- [3] 272 'Quid nimis indignis' inquit 'me uocibus urgues,
- [4] 272 « Quid nimis indignis » inquit « me vocibus urgues,
- [6] 272 'quid nimis indignis' inquit 'me vocibus urges,

273 o patriae, germane, decus? Nam nec mihi coniunx
- [2] 273 O patriae, germane, decus? natn nec mihi conjux
- [3] 273 O patriae, germane, decus? nam nec mihi coniunx
- [4] 273 O patriae, germane, decus? nam nec mihi conjunx
- [6] 273 o patriae, germane, decus? nam nec mihi coniunx
  - decus (Hector; ヘクトル): o patriae, germane, decus 273
  - coniunx (Helene; ヘレネ): coniunx 273. 276. 285. 301

274 prauaque luxuria est potior uirtutis honore
- [2] 274 Pronaque luxuria est potior virtutis Iionore,
  - *Pronaque luxuria*（そして放縦に傾き）、すなわち愛欲（ウェヌス）に染まりやすく傾きやすいこと。…
- [3] 274 Priuaque luxuria est potior uirtutis honore;
- [4] 274 Pravaque luxuria est potior virtutis honore;
- [6] 274 pravaque luxuria est potior virtutis honore

275 nec uires temptare uiri dextramque recuso,
- [2] 275 Nec vires dextramque viri tentare recuso,
  - *Dextramque viri tentare*（そして勇士の右腕を試すこと）、戦うことによって勇士の武力と右腕に何ができるかを経験してみること。Virg. Aen. II, 334: « vix primi praelia tentant »。…――タキトゥス『ゲルマーニア』(Germ.) XXXIV: « Ipsum quin etiam Oceanum tentavimus »。オウィディウス『書簡詩』(Epist.) VII, 121: « bellis peregrina et femina tentor »。このように *tentare* は企てや試みについて用いられ、*tentare aequor*（海を試みる）、*vias*（道を試みる）などのようである。ウァレリウス・フラックス『アルゴナウティカ』I, 529 へのブルマンの注を参照。パリ編者。
- [3] 275 Nec uires temptare uiri dextramque recuso,
- [4] 275 Nec vires temptare viri dextramque recuso,
- [6] 275 nec vires temptare viri dextramque recuso,
  - viri (Menelaus; メネラオス): viri 275. 288. 329

276 dummodo uictorem coniunx cum pace sequatur."
- [2] 276 Dummodo victorem conjux cum pace sequatur ».
- [3] 276 Dummodo uictorem coniunx cum pace sequatur.'
- [4] 276 Dummodo victorem conjunx cum pace sequatur. »
- [6] 276 dummodo victorem coniunx cum pace sequatur.'
  - coniunx (Helene; ヘレネ): coniunx 273. 276. 285. 301

277 Dicta refert Hector: placuit sententia Grais.
- [2] 277 Dicta refert Hector:placuit sententia Graiis.
- [3] 277 Dicta refert Hector; placuit sententia Grais.
- [4] 277 Dicta refert Hector; placuit sententia Grais.
  - Grais (GRAI; ギリシア人): — ヘクトルの意見がギリシア人の気に入る
  - Hector (HECTOR; ヘクトル): — パリスの言葉を伝える
- [6] 277 dicta refert Hector; placuit sententia Grais.
  - （証言） 『ベレンガリウスの事績』2, 3 を参照
  - Grais (Graius; ギリシアの): Grais 2. 277. 614
  - Hector (Hector; ヘクトル): Hector 256. 277. 491. 626. 677. 774. 959. 967. 979. 996. 1051

278 Protinus accitur Priamus sacrisque peractis
- [2] 278 Protinus accitur Priamus, sacrisque peractis
- [3] 278 Protinus accitur Priamus, sacrisque peractis
- [4] 278 Protinus accitur Priamus, sacrisque peractis
  - Priamus (PRIAMUS; プリアモス): ギリシア人と休戦協定を結ぶために呼ばれる
- [6] 278 protinus accitur Priamus sacrisque peractis
  - Priamus (Priamus; プリアモス): Priamus 278 [983] 1046

279 foedera iunguntur. Post haec discedit uterque
- [2] 279 Foedera junguntur : post haec discedit uterque
  - … ウェルギリウスは『アエネーイス』XII, 696 でトゥルヌスとアイネイアスの同様の一騎打ちを論じて次のように述べる: « Discessere omnes medii, spatiumque dedere »。…
- [3] 279 Foedera iunguntur; post haec decedit uterque
- [4] 279 Foedera junguntur; post haec decedit uterque
- [6] 279 foedera iunguntur; post haec discedit uterque

280 depositis populus telis campusque patescit.
- [2] 280 Depositis telis populus, campusque patescit.
  - … オウィディウス『変身物語』(Met.) XII, 147 でも同様である: « positis pars utraque substitit armis »。ウェルギリウス『アエネーイス』XII, 707: « Armaque deposuere humeris »；および 710 行: « ut vacuo patuerunt aequore campi »。
- [3] 280 Depositis populus telis, campusque patescit.
- [4] 280 Depositis populus telis, campusque patescit.
- [6] 280 depositis populus telis campusque patescit.

281 Interea toto procedit ab agmine Troum
- [2] 281 Interea toto procedit ab agmine Troum
- [3] 281 Interea toto procedit ab agmine Troum
- [4] 281 Interea toto procedit ab agmine Troum
  - Troum (TROJANI; トロイア人): — パリスがトロイア人の戦列から進み出る
- [6] 281 interea toto procedit ab agmine Troum
  - Troum (Tros; トロイア人): Troum 102. 281. 339. 357. 438. 631. 641. 701. 963

282 pulcher Alexander, clipeoque insignis et hasta.
- [2] 282 Pulcher Alexander, clypeoque insignis et hasta,
- [3] 282 Pulcher Alexander, clipeoque insignis et hasta.
- [4] 282 Pulcher Alexander, clipeoque insignis et hasta.
  - Alexander (PARIS; パリス): Alexander:美しき者、盾と槍で際立ち、メネラオスに対して進み出る
- [6] 282 pulcher Alexander, clipeoque insignis et hasta.
  - Alexander (Alexander; アレクサンドロス): pulcher Alexander 282

283 Quem contra paribus fulgens Menelaus in armis
- [2] 283 Quem contra paribus fulgens Menelaus in armis
- [3] 283 Quem contra paribus fulgens Menelaus in armis
- [4] 283 Quem contra paribus fulgens Menelaus in armis
  - Menelaus (MENELAUS; メネラオス): 武具に輝き、パリスに対して立った
- [6] 283 quem contra paribus fulgens Menelaus in armis
  - Menelaus (Menelaus; メネラオス): Menelaus 283. 312. 339. 539

284 constitit et: "Tecum mihi sint certamina - dixit -
- [2] 284 Constitit, et, «Tecum mihi sunt certamina, dixit,
- [3] 284 Constitit et 'tecum mihi sint certamina' dixit;
- [4] 284 Constitit et « Tecum mihi sint certamina » dixit;
- [6] 284 constitit et 'tecum mihi sint certamina' dixit

285 "nec longum nostra laetabere coniuge, quae te
- [2] 285 Nec longum nostra iaetabere conjuge, quae te
  - *Nec longum laetabere*（お前は長く喜ぶことはないだろう）。ウェルギリウス『アエネーイス』X, 740。しかしこの表現全体はオウィディウス『変身物語』(Metam.) V, 64 から採られたものである: « arcus Arripit, et, Mecum tibi sint certamina, dixit, Nec longum pueri fato laetabere »。
- [3] 285 'Nec longum nostra laetabere coniuge, quae te
- [4] 285 « Nec longum nostra laetabere conjuge, quam te
- [6] 285 'nec longum nostra laetabere coniuge, quae te
  - coniuge (Helene; ヘレネ): coniunx 273. 276. 285. 301

286 mox raptum ire gemet, tantummodo Iuppiter adsit."
- [2] 286 Mox rapuit regem , tantummodo Jupiter adsit ».
  - **(cont.)** … 原作者ホメロスでは、勝利者がすべてを手に入れることになっている。…この作者が常にホメロスに厳密に従っているわけでもなく、ホメロスにはそのようなことは何もない。むしろメネラオスは戦い、すなわち一騎打ちに入るにあたってユピテル自身に祈りかけているのである。…
- [3] 286 Mox raptum ire gemet, tantummodo Iuppiter adsit.'
- [4] 286 Mox rapuisse gemes, tantummodo Juppiter adsit. »
  - Juppiter (JUPPITER; ユピテル): — ただ彼が味方してくれさえすれば(メネラオスが語る)
- [6] 286 mox raptum regemet, tantummodo Iuppiter adsit.'
  - Iuppiter (Iuppiter; ユピテル): tantummodo -er adsit 286

287 Dixit et aduersum se concitat acer in hostem.
- [2] 287 Dixit, et adversum se concitat acer in hostem.
- [3] 287 Dixit et aduersum se concitat acer in hostem.
- [4] 287 Dixit et adversum se concitat acer in hostem.
- [6] 287 dixit et adversum se concitat acer in hostem.

288 Ille uirum forti uenientem reppulit ictu
- [2] 288 Ille virum forti venientem reppulit ictu ,
- [3] 288 Ille uirum forti uementem reppulit ictu
- [4] 288 Ille virum forti venientem reppulit ictu
- [6] 288 ille virum forti venientem reppulit ictu
  - forti uenientem … 434行、ウェルギリウス『アエネーイス』12, 510 他を参照
  - virum (Menelaus; メネラオス): viri 275. 288. 329

289 seque gradu celeri recipit longeque frementem
- [2] 289 Seque gradu celeri recipit, longeque frementem
  - *Frementem hastam*（唸る槍）。放たれて空気を切り裂きながら音を立てる槍のこと。…
- [3] 289 Seque gradu celeri recipit longeque frementem
- [4] 289 Seque gradu celeri recipit longeque trementem
- [6] 289 seque gradu celeri recipit longeque frementem

290 hastam deinde iacit, quam deuitauit Atrides
- [2] 290 Hastam deinde jacit, quam devitavit Atrides,
  - … ホメロス『イリアス』III, 360 によれば、アトレウスの子の槍をかわしたのはパリスであって、パリスの槍をアトレウスの子がかわしたのではない。われらの作者はこの戦いの多くの点をホメロスと異なって語っている。
- [3] 290 Hastam deinde iacit, quam deuitauit Atrides.
- [4] 290 Hastam deinde jacit, quam devitavit Atrides.
  - Atrides (MENELAUS; メネラオス): — パリスの槍を避ける
- [6] 290 hastam deinde iacit; quam devitavit Atrides
  - Atrides (Atrides (Menelaus); アトリデス（メネラオス）): -des 290. 301. 332. 349. (510?)

291 inque uicem misso fixisset corpora telo
- [2] 291 Inque vicemi misso fixisset pectora telo
- [3] 291 Inque uicem misso fixisset corpora telo
- [4] 291 Inque vicem misso fixisset corpora telo
- [6] 291 inque vicem misso fixisset corpora telo

292 praedonis Phrygii, ni uastum ferrea pectus
- [2] 292 Praedonis Phrygii, nisi vastum ferrea corpus
  - *Praedonis Phrygii*（プリュギアの略奪者の）。姦通者や娘の略奪者に対する *praedo*（強盗、略奪者）という罵倒は頻繁に見られ、とりわけヘレネの略奪ゆえにパリスに対して（スタティウス『アキレイス』I, 45）、またラーウィーニアのゆえにアイネイアスに対して用いられる。ウェルギリウス『アエネーイス』VII, 362: « Perfidus alta petens, abducta virgine, praedo »；および同 XI, 484 では « Phrygius praedo » と呼ばれている。プルートーもプロセルピナの略奪ゆえに、オウィディウスの Met. V, 521 や Fast. IV, 591 でこのように呼ばれている。…
- [3] 292 Praedonis Phrygii, ni uastum ferrea pectus
- [4] 292 Praedonis Phrygii, ni vastum ferrea pectus
  - Praedonis (PARIS; パリス): Praedo Phrygius praedonis Phrygii:鉄の胸甲が覆っていなかったならば、メネラオスの槍はプリュギアの略奪者の身体を傷つけていたであろう
  - Phrygii (PHRYGIUS; プリュギアの): Phrygii praedonis
- [6] 292 praedonis Phrygii, ni vastum ferrea pectus
  - Phrygii (Phrygius; プリュギアの): praedonis Phrygii 292

293 texisset lorica uiri septemplice tergo.
- [2] 293 Texisset lorica viri septemplice tergo.
  - *Septemplice tergo*（七重の革の）：七枚の牛革で覆われ防御されていたもの。他の箇所でも七重の盾は英雄たちに帰せられるのが通例である。ウェルギリウス『アエネーイス』XII, 925；オウィディウス『変身物語』XIII, 2 および 347。
- [3] 293 Texisset lorica uiri septemplice tergo.
- [4] 293 Texisset lorica viri septemplice tergo.
- [6] 293 texisset lorica viri, septemplice tergo

294 Insequitur iuxta clamor; tum aduersus uterque
- [2] 294 Insequitur juxta clamor, tuni adversus uterque
- [3] 294 Insequitur iuxta clamor; tum aduersus uterque
- [4] 294 Insequitur clamor; tum vero adversus uterque
- [6] 294 insequitur iuxta clamor; tum adversus uterque

295 constitit et galeam galea terit et pede plantam
- [2] 295 Constitit, et galea galeam terit, et pede plantam
  - *Constitit, et galea galeam ferit*（立ち止まり、兜が兜を打つ）。名高きボンダムは前掲書 153 頁で、作者がこれを書く際にオウィディウスの次の詩行（Met. IX, 43）を心に思い浮かべていたと考えている: « eratque Cum pede pes junctus: totoque ego pectore pronus, Et digitos digitis, et frontem fronte premebam »。そして確かにここでも、他の箇所と同様に、作者がオウィディウスを模倣する好機を捉えていることが明らかである。ホメロス自身の物語はそのような描写を示唆していないからである。
- [3] 295 Constitit et galeam galea terit et pede plantam
- [4] 295 Constitit et galeam galea terit et pede plantam
- [6] 295 constitit et galeam galea terit et pede plantam

296 coniungit stridetque mucro mucrone corusco;
- [2] 296 Conjungit, stridet mucro mucrone corusco,
- [3] 296 Coniungit, stridetque mucro mucrone corusco.
- [4] 296 Conjungit, stridetque mucro mucrone corusco.
- [6] 296 coniungit, stridetque mucro mucrone corusco,

297 corpus collectum tegitur fulgentibus armis.
- [2] 297 Corpus collectum tegitur fulgentibus armis.
  - *Corpus collectum*（身を縮めて）、すなわち盾の内側に身を引き隠すこと。Virg. Aen. XII, 491: « Substitit Aeneas, et se collegit in arma »；および X, 412: « seque in sua colligit arma »。…――キュペル『観察録』(Observ.) 第I巻12章、90頁を参照。パリ編者。
- [3] [297] [Corpus collectum tegitur fulgentibus armis.]
- [4] 297 below Corpus collectum tegitur fulgentibus armis
- [6] 297 corpus collectum tegitur fulgentibus armis.
  - … ウェルギリウス『アエネーイス』12, 491 および 10, 412 を参照; armis すなわち盾

298 Non aliter fortes nitida de coniuge tauri
- [2] 298 !Non aliter fortes nitida pro conjuge tauri
  - *Non aliter fortes*（勇猛な……も同様である）。この直喩は明らかにオウィディウスから採られたものであり、彼は Met. IX, 46 で、上に引用した言葉に続けて次のように述べている: « Non aliter fortes vidi concurrere tauros, Quum pretium pugnae, toto nitidissima saltu Expetitur conjux »。
- [3] 298 Non aliter fortes nitida de coniuge tauri
- [4] 298 Non aliter fortes nitida de conjuge tauri
- [6] 298 non aliter fortes nitida de coniuge tauri

299 bella gerunt uastisque replent mugitibus auras.
- [2] 299 Bella gerunt, vastisque replent mugitibus auras.
- [3] 299 Bella gerunt uastisque replent mugitibus auras.
- [4] 299 Bella gerunt vastisque replent mugitibus auras.
- [6] 299 bella gerunt vastisque replent mugitibus auras.

300 Atque diu rigido captabant corpora ferro,
- [2] 300 Jamque diu rigido captabant corpora ferro ;
  - … *Captabant pectora*（胸を狙っていた）、すなわち身体を傷つけるのに都合のよい場所を狙うこと。――ウェルギリウス『アエネーイス』XII, 920 においても同様である: « telum Aeneas fatale coruscat, Sortitus fortunam oculis »。パリ編者。…
- [3] 300 Utque diu rigido captabant corpora ferro,
- [4] 300 Jamque diu rigido captarant corpora ferro,
- [6] 300 atque diu rigido rimabant corpora ferro,

301 cum memor Atrides raptae sibi coniugis instat
- [2] 301 Tunc memor Atrides raptae sibi conjugis instat,
- [3] 301 Tum memor Atrides raptae sibi coniugis instat
- [4] 301 Cum memor Atrides raptae sibi conjugis instat
  - Atrides (MENELAUS; メネラオス): — 奪われた妻を思い、迫る
- [6] 301 cum memor Atrides raptae sibi coniugis instat
  - Atrides (Atrides (Menelaus); アトリデス（メネラオス）): -des 290. 301. 332. 349. (510?)
  - coniugis (Helene; ヘレネ): coniunx 273. 276. 285. 301

302 Dardaniumque premit iuuenem. Mox ense rigente
- [2] 302 Dardaniumque premit juvenem mox ense rigenti ,
- [3] 302 Dardaniumque premit iuuenem mox ense rigente;
- [4] 302 Dardaniumque premit juvenem mox ense rigente ;
  - Dardanium (PARIS; パリス): Dardanius juvenis Dardanium juvenem:メネラオスはダルダニアの若者に剣で迫る
- [6] 302 Dardaniumque premit iuvenem. mox ense rigente
  - 近年の刊本は誤って iuvenem の後に句読点を打たなかった
  - Dardanium (Dardanius; ダルダニアの): -um . . . iuvenem 302:パリス

303 cedentem retro dum desuper appetit hostem,
- [2] 303 Cedentemque retro dum desuper adpetit hostem ,
- [3] 303 Cedentemque retro dum desuper appetit hostem,
- [4] 303 Cedentemque retro dum desuper appetit hostem,
- [6] 303 cedentem retro dum desuper appetit hostem,

304 splendidus extremas galeae percussus ad oras
- [2] 304 Splendidus extremas galeae percussus ad oras
- [3] 304 Splendidus extremas galeae percussus ad oras
- [4] 304 Splendidus extremas galeae percussus ad oras
- [6] 304 splendidus extremas galeae percussus ad oras

305 dissiluit mucro; gemuerunt agmina Graium.
- [2] 305 Dissiluit mucro : gemuerunt agmina Graium.
  - … われらの作者自身も下方の 968 行で詩行全体としてこれを繰り返している。そしてこれはウェルギリウスの模倣から得たものであり、ウェルギリウスはトゥルヌスの同様の不運を記して『アエネーイス』XII, 741 で次のように述べている: « Mortalis mucro, glacies seu futilis, ictu Dissiluit »。オウィディウス『変身物語』V, 171 以下も同様である: « Non circumspectis exactum viribus ensem Fregit, et extrema percussae parte columnae Lamina dissiluit; dominique in gutture fixa est »。
- [3] 305 Dissiluit mucro; gemuerunt agmina Graium.
- [4] 305 Dissiluit mucro; gemuerunt agmina Grajum.
  - Grajum (GRAI; ギリシア人): — パリスが傷つけられると、ギリシア人の隊列は呻いた
- [6] 305 dissiluit mucro; gemuerunt agmina Graium.
  - Dis(s)iluit … ウェルギリウス『アエネーイス』12, 741 を参照
  - Graium (Graius; ギリシアの): agmina -um 305. 487

306 Tum uero ardescit, quamuis manus ense carebat,
- [2] 306 Tunc vero ardescit, quamvis manus ense careret,
- [3] 306 Tum uero ardescit, quamuis manus ense carebat,
- [4] 306 Tum vero ardescit, quamvis manus ense carebat,
- [6] 306 tum vero ardescit, quamvis manus ense carebat,

307 et iuuenem arrepta prosternit casside uictor
- [2] 307 Et juvenem arrepta prosternit casside victor,
- [3] 307 Et iuuenem arrepta prosternit casside uictor
- [4] 307 Et juvenem arrepta prosternit casside victor
- [6] 307 et iuvenem arrepta prosternit casside victor
  - victor (Menelaus; メネラオス): victor 307. 352
  - iuvenem (Paris; パリス): iuvenem 307

308 ad socios traheretque, et, ni caligine caeca
- [2] 308 Ad socios traheretque , nisi caligine csca
- [3] 308 Ad sociosque trahit; et ni caligine caeca
  - … trahit における末尾音節の長母音化については 257 および 966 を参照
- [4] 308 Ad sociosque trahit, et ni caligine caeca
- [6] 308 ad socios † traheretque nisi caligine caeca

309 texisset Cytherea uirum subiectaque mento
- [2] 309 Texisset Cytherea virum , subjectaque mento
- [3] 309 Texisset Cytherea uirum subiectaque mento
- [4] 309 Texisset Cytherea virum subjectaque mento
  - Cytherea (VENUS; ウェヌス): Cytherea:メネラオスと戦うパリスを霧で覆う
- [6] 309 texisset Cytherea virum subiectaque mento
  - Cytherea (Cytherea; キュテレア): Cythereă 309. 335. 470:ウェヌス
  - virum (Paris; パリス): virum 309

310 fortia rupisset laxatis uincula nodis,
- [2] 310 Fortia rupisset iaxatis vincula nodis,
- [3] 310 Fortia rupisset laxatis uincula nodis,
- [4] 310 Fortia laxatis rupisset vincula nodis,
- [6] 310 fortia rupisset laxatis vincula nodis,

311 ultimus ille dies Paridi foret. Abstrahit auro
- [2] 311 Ultimus ilie dies Paridi foret : abstrahit auro
- [3] 311 Ultimus ille dies Paridi foret. abstrahit auro
- [4] 311 Ultimus ille dies Paridi foret. Abstrahit auro
  - Paridi (PARIS; パリス): Paridi:ウェヌスが彼を覆わなかったならば、それはパリスの最後の日となったであろう
- [6] 311 ultimus ille dies Paridi foret. abstrahit auro
  - Paridi (Paris; パリス): Paridī 311

312 fulgentem galeam secum Menelaus et ardens
- [2] 312 Fuigentem galeam secum Mehelaus, et ardens
- [3] 312 Fulgentem galeam secum Menelaus et ardens
- [4] 312 Fulgentem galeam secum Menelaus et ardens
  - Menelaus (MENELAUS; メネラオス): — パリスの兜を引きはがし、燃え立って再び彼に向かって走る
- [6] 312 fulgentem galeam secum Menelaus et ardens
  - Menelaus (Menelaus; メネラオス): Menelaus 283. 312. 339. 539

313 in medios mittit proceres rursumque recurrit
- [2] 313 In medios mittit proceres, rursumque recurrit,
- [3] 313 In medios mittit proceres rursumque recurrit
- [4] 313 In medios mittit proceres rursusque recurrit
- [6] 313 in medios mittit proceres rursumque recurrit

314 et magnam ualidis contorsit uiribus hastam
- [2] 314 Et magnam validis contorsit viribus hastam
  - *Contorsit viribus hastam*（渾身の力で槍を投げつけた）は、ウェルギリウス『アエネーイス』II, 50 の言葉である。
- [3] 314 Et magnam ualidis contorsit uiribus hastam
- [4] 314 Et magnam validis contorsit viribus hastam
- [6] 314 et magnam validis contorsit viribus hastam

315 in cladem Phrygii, sua quem Venus eripit hosti
- [2] 315 In ciadem Phrygii; sua quem Yenus eripit hosti,
  - *Sua quem Venus*（彼自身のウェヌスが……彼を）。なぜならアレクサンドロス（パリス）は彼女の熱心な信奉者であり、それゆえ彼自身の神と呼んだのである。同様に 877 行でも、海自身の神々が海に加えられたとして次のように言っている: « Addideratque freto sua numina, Nerea magnum »。またホメロスにおいても、ウェヌス自身がパリスをメネラオスの手から救い出した後、自分に献身する彼をヘレネに推薦している。バルト『雑考』(Adv.) LIX, 1。代名詞 *suus* が「好意的な、都合のよい、有益な」を意味することがしばしばあるのは、ローマの作家の読書に親しんだ者なら誰もが知るところであり、これをより多くの例引で示すのは余計なことであろう。ホラーティウス『エポードス』9, 30: « Cretam ventis iturus non suis »。
- [3] 315 In cladem Phrygii, sua quem Uenus eripit hosti
- [4] 315 In cladem Phrygii, sua quem Venus eripit hosti
  - Phrygii (PARIS; パリス): Phrygius in Phrygii cladem:メネラオスはプリュギア人を滅ぼすために槍を投げる
  - Phrygii (PHRYGIUS; プリュギアの): Phrygii
  - Venus (VENUS; ウェヌス): パリスをメネラオスから奪い去る
- [6] 315 in cladem Phrygii, sua quem Venus eripit hosti
  - Phrygii (Phrygius; プリュギアの): Phrygii、すなわちパリスの、315
  - Venus (Venus; ウェヌス): Venus 315. 464. 911

316 et secum in thalamos defert testudine cultos.
- [2] 316 Et secum in thalamos defert testudine cultos :
  - … バルトはこの箇所から、われらの作者は他の詩人たちのように後続する文字 *sc* や *st* のために先行する音節を長音化することを常としないと指摘し、われらの作者からの別の例として 791 行の *Promachum quoque sternit atrocem* を挙げている。しかし私としては、優れた詩人たちにおいてこれがなされるのは、語の途中にある場合を除けば極めて稀であると考える。ウェルギリウス『アエネーイス』VI, 687 に例があるが、そこでも異読がある。…なぜならわれらの作者が好んでオウィディウスを模倣しており、オウィディウスは Met. II, 737 で次のように述べているからである: « Pars secreta domus ebore et testudine cultos Tres habuit thalamos »。なお、われらの作者が鼈甲（べっこう）張りの寝室（*thalamos testudineos*）と述べたのは、ホメロスの趣旨や英雄時代の習俗に従ったのではなく、より新しい時代の贅沢によるものである。ホメロスのこの箇所（III, 390）でも寝室に言及されているが、何の素材も示されていない。しかしプリニウスは第 IX 巻第 13 節で、「亀の甲羅を薄板に切り、寝台や戸棚をこれで覆うこと」は、スッラの時代前後に生きたコルネリウス・ポッリオによってローマで最初に始められたと記している。この時代以前には、ユウェナーリス（XI, 93）の言葉を借りるなら、« Nemo inter curas et seria duxit habendum, Qualis in Oceani fluctu testudo na-
  - **(cont.)** （前頁からの続き）[-taret, Clarum Trojugenis factura ac nobile fulcrum »]。ウェルギリウスは『農耕詩』(Georg.) II, 463 で *varios pulchra testudine postes*（美しい鼈甲で彩られた扉の柱）と言っている。――鼈甲張りの寝台（*testudineum lectum*）については本書第 II 巻 460 頁で見たが、その箇所にマルティアリス XII, 66 [67] を補うことができる: « Gemmantes prima fulgent testudine lecti »。パリ編者。
- [3] 316 Et secum in thalamos defert testudine cultos.
- [4] 316 Ac secum in thalamos defert testudine cultos.
- [6] 316 et secum in thalamos defert testudine cultos.
  - … cultos … オウィディウス『変身物語』2, 737 を参照

317 Ipsa dehinc Helenam muris accersit ab altis
- [2] 317 Ipsa dehinc Helenam muris arcessit ab aitis,
- [3] 317 Ipsa dehinc Helenam muris arcessit ab altis
- [4] 317 Ipsa dehinc Helenam muris arcessit ab altis
  - Helenam (HELENA; ヘレネ): Helenam:ウェヌスがヘレネをパリスのもとへ連れて行く
- [6] 317 ipsa dehinc Helenam muris accersit ab altis
  - Helenam (Helene; ヘレネ): Helenam 317. 343

318 Dardanioque suos Paridi deducit amores.
- [2] 318 Dardanioque suos Paridi deducit amores.
- [3] 318 Dardanioque suos Paridi deducit amores.
- [4] 318 Dardanioque suos Paridi deducit amores.
  - Paridi (PARIS; パリス): — ウェヌスはダルダニアの者のもとへヘレネを連れて行く
- [6] 318 Dardanioque suos Paridi deducit amores.
  - Dardanio (Dardanius; ダルダニアの): Dardanio . . . Paridi 318
  - Paridi (Paris; パリス): Dardanio . . . dī 318

319 Quem tali postquam conspexit uoce locutast:
- [2] 319 Quam taii postquam conspexit voce loquuta est
- [3] 319 Quem tali postquam conspexit uoce locuta est
- [4] 319 Quem tali postquam conspexit voce locuta est
- [6] 319 quem tali postquam conspexit voce locuta est

320 "Venisti mea flamma, Paris, superatus ab armis
- [2] 320 ttVenisti, mea flamma, Paris superatus ab armis
- [3] 320 'Uenisti, mea flamma, Paris, superatus ab armis
- [4] 320 « Venisti, mea flamma, Paris, superatus ab armis
  - Paris (PARIS; パリス): 呼格:「わが炎よ」(ヘレネが呼びかける)
- [6] 320 'venisti, mea flamma, Paris, superatus ab armis
  - Paris (Paris; パリス): 呼格:mea flamma, Paris(ヘレネが語る)320

321 coniugis antiqui? Vidi puduitque uidere,
- [2] 321 Conjugis antiqui : vidi, puduilque videre,
  - *Vidi puduitque videre*（私は見た、そして見るのを恥じた）。ボンダムは 154 頁で、この半行もオウィディウス『変身物語』XIII, 223 のものであると指摘している。そこではウリクセスがアイアスに向かって次のように言っている: « Vidi, puduitque videre, Quum tu terga dares »。そして、アキレウスの武具をめぐるウリクセスとアイアスの争論やトロイア戦争における主要な出来事が要約して述べられているこの第 XIII 巻を、われらの作者が『梗概』(*Epitome*) を著すにあたってとりわけ念頭に置き、そこからきわめて多くの詩句を借用したことは、これらをより注意深く検討し比較する者には容易に見て取れるであろう。
- [3] 321 Coniugis antiqui? uidi puduitque uidere,
- [4] 321 Conjugis antiqui? vidi puduitque videre,
- [6] 321 coniugis antiqui? vidi puduitque videre,
  - coniugis (Menelaus; メネラオス): coniugis antiqui 321

322 arreptum cum te traheret uiolentus Atrides
- [2] 322 Arreptum quum te tralieret violientus Atrides,
- [3] 322 Arreptum cum te traheret uiolentus Atrides
- [4] 322 Arreptum cum te traheret violentus Atrides
  - Atrides (MENELAUS; メネラオス): — 乱暴な者(ヘレネがパリスに呼びかける)
- [6] 322 arreptum cum te traheret violentus Atrides
  - Atrides (Atrides (Menelaus); アトリデス（メネラオス）): violentus -es 322

323 Iliacoque tuos foedaret puluere crines.
- [2] 323 Iliacoque tuos foedaret pulvere crines :
  - *Pulvere crines*（髪を塵で［汚す］）。Virg. Aeneid. XII, 99; Ovid. Metam. VIII, 529。
- [3] 323 Iliacoque tuos foedaret puluere crines.
- [4] 323 Iliacoque tuos foedaret pulvere crines.
  - Iliaco (ILIACUS; イリオンの): Iliaco pulvere:メネラオスがパリスの髪をイリオンの塵で汚していたとき、ヘレネは恐れていた
- [6] 323 Iliacoque tuos foedaret pulvere crines.
  - Iliaco (Iliacus; イリオンの): Iliaco . . . pulvere 323

324 Nostraque - me miseram! - timui ne Doricus ensis
- [2] 324 Nostraque ( me miseram ! ) timui ne Doricus ensis
- [3] 324 Nostraque (me miseram!) timui ne Doricus ensis
- [4] 324 Nostraque, me miseram! timui ne Doricus ensis
  - Doricus (DORICUS; ドリスの): Doricus ensis:ドリスの剣
- [6] 324 nostraque (me miseram) timui ne Doricus ensis
  - Doricus (Doricus; ドリスの): Doricus ensis 324

325 oscula discuteret; totus mihi, mente reuincta,
- [2] 325 Oscula discuteret : totus mihi mente relicta
  - *Discuteret*（打ち砕く、追い払う）：フロンティーヌスが IV, 7, 31 で « consilia hostium discutere »（敵の計略を打ち破る）と言い、シリウス・イタリクス VII, 153（ドラケンボルヒの校訂による）で « discutere dolos »（奸策を打ち破る）と言っているのと同様である。…
- [3] 325 Oscula dissiceret; toto mihi mente reuincta
- [4] 325 Oscula disiceret; toto mihi mente relapsa
- [6] 325 oscula discuteret; totus mihi mente † relicta

326 fugerat ore color sanguisque reliquerat artus.
- [2] 326 Fugerat ore coior, sanguisque reliquerat artus.
  - *Fugerat ore color*（顔から色が失われていた）。この半行もオウィディウス『求愛書簡』(Her.) XI, 27 のものである。…
- [3] 326 Fugerat ore color, sanguisque reliquerat artus.
- [4] 326 Fugerat ore color, sanguisque reliquerat artus.
- [6] 326 fugerat ore color sanguisque reliquerat artus.

327 Quis te cum saeuo contendere suasit Atrida?
- [2] 327 Quis te cum saevo contendere jussit Atrida?
- [3] 327 Quis tibi cum saeuo contendere suasit Atrida?
- [4] 327 Quis tibi cum saevo suasit contendere Atrida?
  - Atrida (MENELAUS; メネラオス): Cum Atrida:誰が汝に残忍なアトレウスの子と争うよう勧めたのか(ヘレネがパリスに呼びかける)
- [6] 327 quis te cum saevo contendere suasit Atrida?
  - Atrida (Atrides (Menelaus); アトリデス（メネラオス）): cum saevo . . . -da 327

328 An nondum uaga fama tuas peruenit ad aures
- [2] 328 An nondum vaga fama tuas pervenit ad aures
  - … ――*Pervenit ad aures*（耳に届いた）。オウィディウス『変身物語』V, 256: « Fama novi fontis nostras pervenit ad aures »；およびウェルギリウス『アエネーイス』II, 81: « Fando aliquid, si forte tuas pervenit ad aures »。パリ編者。
- [3] 328 An nondum uaga fama tuas peruenit ad aures
- [4] 328 An nondum vaga fama tuas pervenit ad aures
- [6] 328 an nondum vaga fama tuas pervenit ad aures

329 de uirtute uiri? Moneo ne rursus inique
- [2] 329 De virtute viri? moneo, ne rursus iniquae
- [3] 329 De uirtute uiri? moneo, ne rursus inique
- [4] 329 De virtute viri? moneo, ne rursus iniquae
- [6] 329 de virtute viri? moneo, ne rursus inique
  - viri (Menelaus; メネラオス): viri 275. 288. 329

330 illius tua fata uelis committere dextrae."
- [2] 330 Illius tua fata velis committere dextrae ».
- [3] 330 Illius tua fata uelis committere dextrae.'
- [4] 330 Illius tua fata velis committere dextrae. »
- [6] 330 illius tua fata velis committere dextrae.'

331 Dixit. Tum largis perfudit fletibus ora.
- [2] 331 Dixerat, et iargis perfudit fietibus ora.
- [3] 331 Dixit, tum largis perfudit fletibus ora.
- [4] 331 Dixerat, et largis perfundit fletibus ora.
- [6] 331 dixit, tum largis perfudit fletibus ora.

332 Tristis Alexander: "Non me superauit Atrides,
- [2] 332 Tristis Aiexander, «Non me superavit Atrides,
- [3] 332 Tristis Alexander 'non me superauit Atrides,
- [4] 332 Tristis Alexander « Non me superavit Atrides,
  - Atrides (MENELAUS; メネラオス): — 私に勝ったのではない(パリスがヘレネに呼びかける)
  - Alexander (PARIS; パリス): — 悲しげに、ヘレネに答える
- [6] 332 tristis Alexander 'non me superavit Atrides,
  - Alexander (Alexander; アレクサンドロス): -er 332
  - Atrides (Atrides (Menelaus); アトリデス（メネラオス）): -des 290. 301. 332. 349. (510?)

333 o meus ardor" - ait - "sed castae Palladis ira.
- [2] 333 O meus ardor, ait, sed castae Palladis ira.
- [3] 333 O meus ardor' ait, 'sed castae Palladis ira.
- [4] 333 O meus ardor! » ait, « sed castae Palladis ira.
  - Palladis (MINERVA; ミネルウァ): Palladis:貞潔なパラスの怒りがパリスを打ち負かした
- [6] 333 o meus ardor' ait, 'sed castae Pallados ira.
  - ardor (Helene; ヘレネ): o meus ardor 333
  - Pallados (Pallas; パラス): castae -dos ira 333

334 Mox illum nostris succumbere turpiter armis
- [2] 334 Mox illum Dostris succumbere turpiter armis
- [3] 334 Mox illum nostris succumbere turpiter armis
- [4] 334 Mox illum nostris succumbere turpiter armis
- [6] 334 mox illum nostris succumbere turpiter armis

335 aspicies aderitque meo Cytherea labori."
- [2] 335 Adspicies, aderitque meo Cytherea labori.»
- [3] 335 Aspicies, aderitque meo Cytherea labori.'
- [4] 335 Aspicies, aderitque meo Cytherea labori. »
  - Cytherea (VENUS; ウェヌス): — わが労苦に味方してくれるであろう(パリスが語る)
- [6] 335 aspicies aderitque meo Cytherea labori.'
  - Cytherea (Cytherea; キュテレア): Cythereă 309. 335. 470:ウェヌス

336 Post haec amplexus per mutua corpora iunctis
- [2] 336 Post haec ampiexu per mutua corpora juncto
  - … 作者がこれらの詩行においてマロー（ウェルギリウス）のよく知られた箇所、Aeneid. VIII, 405: « Optatos dedit amplexus, placidumque petivit Conjugis infusus gremio per membra soporem » を念頭に置いていたことは疑いようがない。
- [3] 336 Post haec amplexu per mutua corpora iuncto
- [4] 336 Post haec amplexu per mutua corpora juncto
- [6] 336 post haec amplexus per mutua corpora iunctis

337 incubuit membris Cygneidos; illa soluto
- [2] 337 Incubuit membris Cygneidos; illa soluto
  - … ところでヘレネが *Cygneis* と呼ばれるのは、白鳥に変じたユピテルの娘と信じられていたからである。その名前を他の詩人が用いたかどうかは私は知らないが、もっともウェルギリウス（伝）の Eleg. ad Messal. 27 では「白鳥の卵から生まれたティンダレオス家の娘」« cygneo edita Tyndaris ovo » と言われており、オウィディウスの Her. XVII, 55 でもヘレネ自身が « Dat mihi Leda Jovem, cygno decepta, parentem » と述べている。
- [3] 337 Incubuit membris Cygneidos; illa soluto
- [4] 337 Incubuit membris Cygneidos; illa soluto
  - Cygneidos (HELENA; ヘレネ): Cygneis Cygneidos:パリスは白鳥の娘の肢体の上に横たわる
- [6] 337 incubuit membris Cygneidos; illa soluto
  - Cygneidos (Cygneis; キュグネイス): Cygneidos(一部の写本では -dus)337:ヘレネ

338 accepit flammas gremio Troiaeque suasque.
- [2] 338 Accepit flammas gremio Trojaeque, suasque.
  - *Flammas Trojaeque suasque*（トロイアの炎と彼女自身の炎）。ヘレネへの愛がトロイアの破滅となる運命にあったパリスについて、機知に富んだ表現である。この言辞もまた、オウィディウスの『名婦の書簡』(Heroid.) XVI, 45 以下のパリスの書簡の箇所に基づいているように思われる。そこではパリスが、出産の日を前に燃え盛る松明を産む夢を見た母親の夢を、トロイアに破滅をもたらす自らの胸の熱情と解釈している: « Arsuram Paridis vates canit Ilion igni; Pectoris, ut nunc est, fax fuit illa mei »。
- [3] 338 Accepit flammas gremio Troiaeque suasque.
- [4] 338 Accepit flammas gremio Trojaeque suasque.
  - Trojae (TROJA; トロイア): ヘレネはトロイアの炎と自らの炎(すなわちパリス)を膝に受け入れる
- [6] 338 accepit flammas gremio Troiaeque suasque.
  - Troiae (Troia; トロイア): flammas . . . -iaeque suasque Parin 338

339 Interea toto Menelaus in agmine Troum
- [2] 339 Interea toto Meneiaus in agmine Troum
- [3] 339 Interea toto Menelaus in agmine Troum
- [4] 339 Interea toto Menelaus in agmine Troum
  - Menelaus (MENELAUS; メネラオス): — 軍勢全体の中でパリスを探す
  - Troum (TROJANI; トロイア人): — メネラオスはトロイア人の戦列の中にパリスを探す
- [6] 339 interea toto Menelaus in agmine Troum
  - Menelaus (Menelaus; メネラオス): Menelaus 283. 312. 339. 539
  - Troum (Tros; トロイア人): Troum 102. 281. 339. 357. 438. 631. 641. 701. 963

340 quaerit Alexandrum uictorque huc fertur et illuc.
- [2] 340 Quaerit Alexandrum, victorque huc fertur et illuc.
- [3] 340 Quaerit Alexandrum uictorque huc fertur et illuc.
- [4] 340 Quaerit Alexandrum victorque huc fertur et illuc.
  - Alexandrum (PARIS; パリス): Alexandrum:メネラオスはアレクサンドロスを探す
- [6] 340 quaerit Alexandrum victorque huc fertur et illuc.
  - Alexandrum (Alexander; アレクサンドロス): -drum 340

341 Quem frater socias acuens in bella cateruas
- [2] 341 Quem frater socias acuens in bella catervas
- [3] 341 Quem frater socias acuens in bella cateruas
- [4] 341 Quem frater socias acuens in bella catervas
- [6] 341 quem frater socias acuens in bella catervas
  - frater (Hector; ヘクトル): frater 341

342 adiuuat et forti pulsos Phrygas increpat ore
- [2] 342 Adjuvat, et forti pulsos Phrygas increpat ore,
- [3] 342 Adiuuat et forti pulsos Phrygas increpat ore
- [4] 342 Adjuvat et forti pulsos Phrygas increpat ore
  - Phrygas (TROJANI; トロイア人): Phrygas:アガメムノンは敗走したプリュギア人を口で叱りつける
- [6] 342 adiuvat et forti pulsos Phrygas increpat ore
  - Phrygas (Phryges; プリュギア人): pulsos -as (-es trad.) 342

343 seruarique iubet leges Helenamque reposcit.
- [2] 343 Servarique jubet leges, Heienamque reposcit.
- [3] 343 Seruarique iubet leges Helenamque reposcit.
- [4] 343 Servarique jubet leges Helenamque reposcit.
  - Helenam (HELENA; ヘレネ): — メネラオスがヘレネの返還を求める
- [6] 343 servarique iubet leges Helenamque reposcit.
  - Helenam (Helene; ヘレネ): Helenam 317. 343

## Book 4

344 Dumque inter sese proceres certamen haberent,
- [2] 344 IV. Quumque inter sese proceres certamen haberent ,
  - *Certamen haberent*（勝負を行うように）。この言い回しは
  - **(cont.)** （前頁からの続き）詩的文体に十分ふさわしいとは思われず、次の詩行に現れる *concilium habuit*（集会を開いた）という表現も不快な重複である。そしてオウィディウスの Met. XIII, 159 の詩行 « Ergo operum quoniam nudum certamen habetur » によっても十分に弁護されるとは思われない。
- [3] 344 Cumque inter sese proceres certamen haberent,
- [4] 344 Cumque inter sese proceres certamen haberent,
- [6] 344 dumque inter sese proceres certamen haberent,

345 concilium omnipotens habuit regnator Olympi
- [2] 345 Conriiium omnipotens liabuit regnator Olympi;
- [3] 345 Concilium omnipotens habuit regnator Olympi,
- [4] 345 Concilium omnipotens habuit regnator Olympi,
  - regnator (JUPPITER; ユピテル): Regnator Olympi:オリュンポスの全能の支配者が会議を開く
  - Olympi (OLYMPUS; オリュンポス): Olympi regnator:オリュンポスの支配者(ユピテル)
- [6] 345 concilium omnipotens habuit regnator Olympi
  - regnator (Iuppiter; ユピテル): omnipotens . . . regnator Olympi 345
  - Olympi (Olympus; オリュンポス): regnator -pi 345:ユピテル

346 foederaque intento turbauit Pandarus arcu,
- [2] 346 Foedcraque intento turbavit Pandarus arcu,
  - … ウェルギリウスは動詞 *confundere* を用いてホメロスの συγχέειν をより適切に表現している（Aen. V, 496: « Pandare, qui quondam jussus confundere foedus, In medios telum torsisti primus Achivos »）。
- [3] 346 Foederaque intento turbauit Pandarus arcu,
- [4] 346 Foederaque intento turbavit Pandarus arcu,
  - Pandarus (PANDARUS; パンダロス): — 弓で休戦協定を乱す
- [6] 346 foederaque intento turbavit Pandarus arcu,
  - Pandarus (Pandarus; パンダロス): -us 346. 436

347 te, Menelae, petens; laterique uolatile telum
- [2] 347 Te, Menelae, petens, laterique volatile telum
  - *Volatile telum*（飛ぶ矢/飛び道具）は Virg. Aen. IV, 71 および Ovid. Metam. VII, 841 より。…
- [3] 347 Te, Menelae, petens; laterique uolatile telum
- [4] 347 Te, Menelae, petens; laterique volatile telum
  - Menelae (MENELAUS; メネラオス): Menelae:メネラオスよ、パンダロスが汝を狙う
- [6] 347 te, Menelae, petens; laterique volatile telum
  - Menelae (Menelaus; メネラオス): te, Menelae 347

348 incidit et tunicam ferro squamisque rigentem
- [2] 348 Incidit, et tunicam ferro squamisque rigeotem
- [3] 348 Incidit et tunicam ferro squamisque rigentem
- [4] 348 Incidit et tunicam ferro squamisque rigentem
- [6] 348 incidit et tunicam ferro squamisque rigentem

349 dissecat. Excedit pugna gemebundus Atrides
- [2] 349 Dissecat : excedit bello gemebundus Atrides,
  - … この事柄において *dissecare* という動詞は他の詩人にはあまり用いられず、彼らは通常 *rumpere* や *lacerare* を用いる。Virg. Aeneid. XII, 98；Ovid. Met. XII, 117 を参照。
- [3] 349 Dissecat: excedit pugna tremebundus Atrides
- [4] 349 Dissecat : excedit pugna gemebundus Atrides
  - Atrides (MENELAUS; メネラオス): — 呻きながら、パンダロスの矢で傷つけられたので戦いから退く
- [6] 349 dissecat: excedit pugna gemebundus Atrides
  - Atrides (Atrides (Menelaus); アトリデス（メネラオス）): -des 290. 301. 332. 349. (510?)

350 castraque tuta petit, quem doctus ab arte paterna
- [2] 350 Castraque tuta petit; quem doctus ab arte paterna
- [3] 350 Castraque tuta petit; quem doctus ab arte paterna
- [4] 350 Castraque tuta petit. Quem doctus ab arte paterna
- [6] 350 castraque tuta petit; quem doctus ab arte paterna
  - arte (Aesculapius; アエスクラピウス): arte paterna 350 を参照

351 Paeoniis curat iuuenis Podalirius herbis,
- [2] 351 Paeoniis curat juvenis Podalirius herbis,
  - … ――*Paeoniis herbis*（パイオンの薬草で）はウェルギリウスの Aen. VII, 769 から取られている。われらの詩人はここでメネラオスの傷を手当てする者としてポダレイリオスを挙げているが、ホメロスではマカオンである（IV, 193）。――ポダレイリオスへの言及については上掲 217 行を見よ。パリ編者。
- [3] 351 Paeoniis curat iuuenis Podalirius herbis;
- [4] 351 Paeoniis curat juvenis Podalirius herbis
  - Paeoniis (PAEONIUS; パイオンの): Paeoniis herbis:ポダレイリオスはパイオンの薬草でメネラオスを治療する
  - Podalirius (PODALIRIUS; ポダレイリオス): — パンダロスに傷つけられたメネラオスを治療する
- [6] 351 Paeoniis curat iuvenis Podalirius herbis
  - Paeoniis (Paeonius; パイオンの): Paeoniis . . . herbis 351
  - Podalirius (Podalirius; ポダレイリオス): iuvenis -ius 351:アエスクラピウスの子

352 itque iterum in caedes horrendaque proelia uictor.
- [2] 352 Atque iterum in caedes horrendaque praelia niittit.
  - *Atque iterum in caedes ..... mittit*（そして再び……を殺戮へと送り出す）。ウェルギリウスはアイネイアスについて、その傷が癒えた後、Aen. XII, 429 で « atque opera ad majora remittit » と述べている。…
- [3] 352 Atque iterum in caedes horrendaque praelia uisit.
- [4] 352 Atque iterum in caedes horrendaque proelia mittit.
- [6] 352 itque iterum in caedes horrendaque proelia victor.
  - victor (Menelaus; メネラオス): victor 307. 352

353 Armauit fortes Agamemnonis ira Pelasgos
- [2] 353 Armavit fortes Agamemnonis ira Pelasgos,
- [3] 353 Armauit fortes Agamemnonis ira Pelasgos,
- [4] 353 Armavit fortes Agamemnonis ira Pelasgos,
  - Agamemnonis (AGAMEMNON; アガメムノン): — パンダロスがメネラオスを傷つけた後、彼の怒りがギリシア人を殺戮へと武装させる
  - Pelasgos (GRAI; ギリシア人): — アガメムノンの怒りが勇敢なペラスゴイを武装させる
- [6] 353 armavit fortes Agamemnonis ira Pelasgos
  - Agamemnonis (Agamemnon; アガメムノン): -onis ira 353
  - Pelasgos (Pelasgi; ペラスゴイ): fortes . . . -os 224. 353

354 et dolor in pugnam cunctos communis agebat.
- [2] 354 Et dolor in pugnam cunctos comnuinis agebat.
  - *Et dolor in pugnam*（そして悲憤が戦いへと［駆り立てる］）。同様に Virg. Aen. VIII, 500: « quos justus in hostem Fert dolor, et merita incendit Mezentius ira »。
- [3] 354 Et dolor in pugnam cunctos communis agebat.
- [4] 354 Et dolor in pugnam cunctos communis agebat.
- [6] 354 et dolor in pugnam cunctos communis agebat.

355 Bellum ingens oritur multumque utrimque cruoris
- [2] 355 Bellum ingens oritur, multumque Utrimque cmoris
- [3] 355 Bellum ingens oritur, multumque utrimque cruoris
  - **355 sq.** 『ベレンガリウス事績録』II 180 以下が有する
- [4] 355 Bellum ingens oritur, multumque utrimque cruoris
- [6] 355 bellum ingens oritur multumque utrimque cruoris
  - **355/6** （証言） = 『ベレンガリウスの事績』2, 180/1 (*multum hinc illincque*)

356 funditur et totis sternuntur corpora campis
- [2] 356 Funditur, et totis stemuntur corpora campis,
  - *Sternuntur corpora campis*（野原に屍が打ち倒される）。Virg. Aen. II, 364: « Plurima perque vias sternuntur inertia passim Corpora »。
- [3] 356 Funditur et totis sternuntur corpora campis;
- [4] 356 Funditur et totis sternuntur corpora campis ;
- [6] 356 funditur et totis sternuntur corpora campis;

357 inque uicem Troumque cadunt Danaumque cateruae
- [2] 357 Inque vicem Troumque cadunt Danaumque catervae :
- [3] 357 Inque uicem Troumque cadunt Danaumque cateruae.
- [4] 357 Inque vicem Troumque cadunt Danaumque catervae.
  - Danaum (GRAI; ギリシア人): — ダナオイの部隊が倒れる
  - Troum (TROJANI; トロイア人): — トロイア人の部隊が倒れる
- [6] 357 inque vicem Troumque cadunt Danaumque catervae.
  - Danaum (Danai; ダナオイ): -um(属格):19. 50. 67. 124. 153. 251. 268. 357. 389. 496. 631. 686. 691. 698. 705. 743. 747. 794. 1025
  - Troum (Tros; トロイア人): Troum 102. 281. 339. 357. 438. 631. 641. 701. 963

358 nec requies datur ulla uiris: sonat undique Mauors
- [2] 358 Nec requies datur ulla viris, sonat undique Mavors, ,
- [3] 358 Nec requies datur ulla uiris; sonat undique Mauors,
- [4] 358 Nec requies datur ulla viris; sonat undique Mavors,
  - Mavors (MARS; マルス): Mavors:四方に響く
- [6] 358 nec requies datur ulla viris; sonat undique Mavors
  - Mavors (Mavors; マウォルス): sonat undique Mavors、すなわち戦闘、358

359 telorumque uolant cunctis e partibus imbres.
- [2] 359 Telorumque volat cunctis de partibus imber.
  - … Virg. Aen. XII, 283: « it toto turbida caelo Tempestas telorum, ac ferreus ingruit imber »。――逆の隠喩によって、アウィアーヌスは『寓話』XLI, 16 で矢筒を帯びた雨あるいは雲（*pharetratos imbres seu nubes*）と呼んでいる。われらの詩人の 746 行を比較せよ。パリ編者。
- [3] 359 Telorumque uolant cunctis e partibus imbres.
- [4] 359 Telorumque volat cunctis e partibus imber.
- [6] 359 telorumque volant cunctis e partibus imbres.

360 Occidit Antilochi rigido demersus in umbras
- [2] 360 Occidit Antilochi rigido demissus ad umbras
  - … なお、*Antilochus* は必然的に誤りでなければならない。なぜならアンティロコスはギリシア勢の側であり、この箇所ではトロイア勢の殺戮について語られているからである。したがってボンダムが 154 頁で « Occidit Antilochi rigido demersus in umbra Ense Thalysiades »（タリュシアデスがアンティロコスの冷たい剣に倒れ、冥府へと落とされた）と校訂したのは正当であった。すなわちホメロスの『イリアス』IV, 458 に見えるエケポロスである。そしてこのことは、*Ense Thalacides* と記す写本 H. によって確証される。G. 2 は *Chalestiades* とする。
- [3] 360 Occidit Antilochi rigido demersus ad umbras
- [4] 360 Occidit Antilochi rigido demissus ad umbras
  - Antilochi (ANTILOCHUS; アンティロコス): Antilochi:タリュシオスの子(エケポロス)がアンティロコスの剣で殺される
  - Thalysiades (THALYSIADES; タリュシアデス): (エケポロス)アンティロコスに殺される
- [6] 360 occidit Antilochi rigido demersus in umbras
  - Antilochi (Antilochus; アンティロコス): Antilochi . . . -ense 360

361 ense Thalysiades optataque lumina linquit.
- [2] 361 Ense Thalysiades, optataque lumina Hnquit.
- [3] 361 Ense Thalysiades optataque lumina linquit.
- [4] 361 Ense Thalysiades optataque lumina linquit.
  - Thalysiades …（『イリアス』IV, 458）。
- [6] 361 ense Thalysiades optataque lumina linquit.
  - Thalysiades (Thalysiades; タリュシアデス): *Thalysiades (tales(t)- trad.) 361:エケポロス

362 Inde manu forti Graiorum terga prementem
- [2] 362 Inde manu forti Graiorum terga prementem
- [3] 362 Inde manu forti Graiorum terga prementem
- [4] 362 Inde manu forti Grajorum terga prementem
  - Grajorum (GRAI; ギリシア人): Grajorum:ギリシア人の背後に迫るシモイシオス
- [6] 362 inde manu forti Graiorum terga prementem
  - Graiorum (Graius; ギリシアの): 名詞として:Graiorum terga 362

363 occupat Anthemione satum Telamonius Aiax
- [2] 363 Occupat Anthemione satum Telamonius Ajax ,
  - … ボンダムが『イリアス』IV, 473 に基づいて *Anthemione satum*（アンテミオンの御子）と訂正した。
- [3] 363 Occupat Anthemione satum Telamonius Aiax
- [4] 363 Occupat Anthemione satum Telamonius Ajax
  - Anthemione …（同所 473）。
  - Ajax (AJAX Telamonis filius; アイアス、テラモンの子): — テラモンの子がアンテミオンの子を倒す
  - Anthemione (ANTHEMIO; アンテミオン): Anthemione satum:テラモンの子アイアスがアンテミオンの子(シモイシオス)を殺す
- [6] 363 occupat Anthemione satum Telamonius Aiax
  - Aiax (Aiax (Telamonius); アイアス（テラモンの子）): Telamonius -ax 205. 363. 602. 623. 787. 836
  - Anthemione (Anthemion; アンテミオン): *Anthemione satum 363:トロイア人シモイシオス
  - Telamonius (Telamonius; テラモンの): Telamonius Aiax 205. 363. 602. 623. 787. 836

364 et praedurato transfixit pectora telo:
- [2] 364 Et praedurato transfigit pectora telo.
  - … とりわけホメロスが IV, 480 でそう述べているからである。…先端を固めた槍（*praedurato telo*）についてはホメロスには何もないが、作者はおそらくウェルギリウスの Aeneid. VII, 524: « Stipitibus duris agitur sudibusve praeustis »［硬い杭や先を焼いて固めた棒で戦われる］を暗示しているのであろう。オウィディウスの Met. XII, 299: « sude figit obusta » も参照。
- [3] 364 Et praedurato transfixit pectora telo:
- [4] 364 Et praedurato transfigit pectora telo :
- [6] 364 et praedurato transfixit pectora telo:

365 purpuream uomit ille animam cum sanguine mixtam,
- [2] 365 Purpuream vomit ille animam cum sanguine mixtam,
  - *Purpuream vomit* 等（深紅の［命を］吐き出す）。この詩行はウェルギリウスの Aen. IX, 349 である。――またブルマン編『ラテン詩選』(Anth. Lat. Burm.) 第1巻 45 頁、作者不詳のエピタフ (Epith. Incertae) 8 行: « Nunc animam quoque tu purpuream vomeres »。パリ編者。
- [3] 365 Purpuream uomit ille animam, cum sanguine misso
- [4] 365 Purpuream vomit ille animam, sua sanguine multo
- [6] 365 purpureo vomit ille animam cum sanguine mixtam,
  - … ウェルギリウス『アエネーイス』9, 349 を参照

366 ora rigat moriens. Tum magnis Antiphus hastam
- [2] 366 Ora rigat moriens : tunc maximus Antiphus hastam
- [3] 366 Ora rigat moriens. tum magnis Antiphus hastam
- [4] 366 Arma rigat moriens. Tum magnis Antiphus hastam
  - Antiphus (ANTIPHUS Priami filius; アンティポス、プリアモスの子): — アイアスに向けて槍を投げる
- [6] 366 ora rigat moriens. tum magnis Antiphus hastam
  - Antiphus (Antiphus 3; アンティポス 3): Antiphus 366

367 uiribus aduersum conatus corpore toto
- [2] 367 Viribus adversum, conatus corpore toto,
  - … ――また *Viribus* は *maximus* にかかる。オウィディウスは Met. XII, 116 で次のように語っている: « hastam Misit in adversum Lycia de plebe Menoeten »。…
- [3] 367 Uiribus aduersum conisus corpore toto
- [4] 367 Viribus adversum conisus corpore toto
  - conisus …（『アエネーイス』V, 642 および X, 127 より校訂）。
- [6] 367 viribus adversum conatus corpore toto
  - … conatus … (462行およびオウィディウス『変身物語』8, 366 を参照) …

368 torquet in Aeaciden; telumque errauit ab hoste
- [2] 368 Torquet in Ajacem, telumque erravit ab hoste,
- [3] 368 Torquet in Aiacem: telum derrauit ab hoste
- [4] 368 Torquet in Ajacem : telumque erravit ab hoste
  - Ajacem (AJAX Telamonis filius; アイアス、テラモンの子): In Ajacem:アンティポスはアイアスに向けて槍を投げる
- [6] 368 torquet in Aeaciden: telumque erravit ab hoste
  - Aeaciden (Aeacides (Aiax Telamonius); アエアキデス（テラモンの子アイアス）): -den 368
  - Aeaciden (Aiax (Telamonius); アイアス（テラモンの子）): -acem は Aeaciden 368. 628 を参照

369 inque hostem cecidit, transfixit et inguina Leucon:
- [2] 369 Inque liostem cecidit; nam flxit in inguine Leucon.
  - … というのも、ここで話題になっている人物は、ホメロス（IV, 491）ではレウコーンではなくレウコス（Leucos）と呼ばれているからである。
- [3] 369 Inque hostem cecidit transfixitque inguine Leucon:
- [4] 369 Inque hostem cecidit, namque ictus in inguine Leucus.
  - Leucus (LEUCUS; レウコス): アンティポスがアイアスに向けて投げた槍に打たれる
- [6] 369 inque hostem cecidit, transfixit et inguine Leucon:
  - Leucon (Leucus; レウコス): Leucon 対格 369:ウリクセスの仲間

370 concidit infelix prostratus uulnere forti
- [2] 370 Concidit infelix prostratus vulnere forti,
- [3] 370 Concidit infelix prostratus uulnere tristi
- [4] 370 Concidit infelix prostratus vulnere tristi
- [6] 370 concidit infelix prostratus vulnere forti

371 et carpit uirides moribundus dentibus herbas.
- [2] 371 Et carpit virides moribundus dentibus berbas.
  - *Et carpit virides moribundus*（そして瀕死のうちに青草を喰む）。ここに私は、討たれて瀕死の者が大地に倒れ伏すさまについての異例な表現を見出す。ホメロスの定型句は ὀδὰξ ἑλεῖν οὖδας［歯で大地を噛む］（『イリアス』II, 418；XI, 748 参照）であり、ラテン詩人たち、少なくとも古代の詩人たちは、これを模倣して *mordere* や *mandere humum*（土を噛む、咀嚼する）、あるいは口や噛むことによって土を求める（*petere, adpetere ore, morsu, terram*）と言う。ウェルギリウスの Aen. XI, 418: « Procubuit moriens et humum semel ore momordit »；同書 669 行: « cruentam Mandit humum, moriensque suo se in vulnere versat »。シリウス・イタリクス IX, 383: « Volvitur ille ruens, atque arva hostilia morsu Adpetit »。しかしその意味で *mordere* や *mandere humum* の代わりに、詩人たちが家畜の草食みについて用いる *carpere dentibus herbas*（歯で草を喰む/引きちぎる）と言った者を、私はこれまで誰も見出していない。もっとも文法家ディオメーデースは第1巻 336 頁で、クナエウス・マティウスの『イリアス』第20巻から似た詩行を引いている: « Ille hietans herbam moribundo tenuit ore »。
- [3] 371 Et carpit uirides moribundus dentibus herbas.
  - 『ベレンガリウス事績録』II 213 参照 …
- [4] 371 Et carpit virides moribundis dentibus herbas.
- [6] 371 et carpit virides moribundus dentibus herbas.
  - （証言） ほぼ = 『ベレンガリウスの事績』2, 213

372 Impiger Atrides casu commotus amici
- [2] 372 linpiger Atrides casu commotus amici
  - **372–373** … ここで友、すなわちレウコスの死に心を動かされたと言われている人物は、ホメロスではアトレウスの子ではなく、オデュッセウスである。そこではレウコスは Ὀδυσσέος ἐσθλὸς ἑταῖρος［オデュッセウスの気高き戦友］と呼ばれており（『イリアス』IV, 491）、オデュッセウスが彼の殺害に激怒して戦列に進み出て、行き当たったデモコオンを討ったのである。…――*Teloque trabali*、すなわち巨大な槍（*hasta magna*）のこと。Virg. Aen. XII, 294。
- [3] 372 Impiger Atrides casu commotus amici
  - ホメロスはアトレウスの子の代わりにオデュッセウスを名指しているので、…
- [4] 372 Impiger Atrides casu commotus amici
  - Atrides (AGAMEMNON; アガメムノン): — 疲れを知らぬ者、デモコオンに向かう
- [6] 372 † impiger † Atrides casu concussus amici
  - Atrides (Atrides (Agamemno); アトリデス（アガメムノン）): [impiger -es 372]
  - Atrides (Laertiades; ラエルティアデス): *Laertiades (atrides trad.) 372:ウリクセス

373 Democoonta petit teloque aduersa trabali
- [2] 373 Democoonta petit , teloque adversa trabali
- [3] 373 Democoonta petit teloque aduersa trabali
- [4] 373 Democoonta petit teloque adversa trabali
  - Democoonta …（『イリアス』IV, 499）。
  - Democoonta (DEMOCOON; デモコオン): Democoonta:アガメムノンがデモコオンに向かう
- [6] 373 Democoonta petit teloque adversa trabali
  - Democoonta (Democoon; デモコオン): *Democoonta 373:プリアモスの庶子

374 tempora transadigit uaginaque horridus ensem
- [2] 374 Tempora transadigit, vaginaque horridus ensem
  - … ――*Vagina ensem eripit*（鞘から剣を抜く）はウェルギリウス的な言い回し（Aen. IV, 579）であるが、この箇所にはあまり適していない。なぜなら別の戦いが準備されているわけではないからである。
- [3] 374 Tempora transadigit uaginaque horridus ensem
- [4] 374 Tempora transadigit vaginaque horridus ensem
- [6] 374 tempora transadigit vaginaque horridus ensem

375 eripit; ille suis moriens resupinus in armis
- [2] 375 Eripit : ille suis raoriens resupinus in armis
- [3] 375 Eripit; ille suis moriens resupinus in armis
- [4] 375 Eripit; ille suis moriens resupinus in armis
- [6] 375 eripit; ille suis moriens resupinus in armis

376 concidit et terram moribundo uertice pulsat.
- [2] 376 Occidit, et terram moribundus vertice pulsat.
  - … オウィディウスを表現したと思われるからである。オウィディウスは Met. V, 84 で « Et resupinus humum moribundo vertice pulsat »、同書 XII, 118 で « Quo plangente gravem moribundo vertice terram » と述べている。
- [3] 376 Concidit et terram moribundo uertice pulsat.
- [4] 376 Concidit et terram moribundo vertice pulsat.
  - … moribundo …（『変身物語』V, 83 および XII, 118 を参照）。
- [6] 376 concidit et terram moribundo vertice pulsat.
  - moribundo … オウィディウス『変身物語』5, 84 を参照

377 Iamque Amarynciden saxi deiecerat ictu
- [2] 377 Jamque A.marynciden saxi dejecerat ictu
  - … しかしホメロス（IV, 517）の叙述の順序を比較すると、この箇所でインブラソスの子ペイロオスがアマリュンケウスの子ディオレスを投石で討っており、残存する名前 *Umbrasides* が真相に酷似していることから、われらの作者が彼について語っていることは明らかである。…
- [3] 377 Iamque Amarynciden saxi deiecerat ictu
- [4] 377 Jamque Amarynciden saxi dejecerat ictu
  - Jamque Amarynciden …（『イリアス』IV, 517）。
  - Amarynciden (DIORES; ディオレス): Amaryncides Amarynciden:ペイロオスがアマリュンケウスの子を殺す
- [6] 377 iamque Amarynciden saxi deiecerat ictu
  - Amarynciden (Amaryncides; アマリュンキデス): *Amaryncīden 377

378 Pirous Imbrasides dederatque silentibus umbris;
- [2] 378 Impiger Imbrasides, dederatque silentibus umbris;
- [3] 378 Pirous Imbrasides dederatque silentibus umbris;
- [4] 378 Pirous Imbrasides dederatque silentibus umbris;
  - Pirous …（同所 520）。
  - Pirous (PIROUS; ペイロオス): — インブラソスの子が、アマリュンケウスの子ディオレスを殺す
- [6] 378 impiger Imbrasides dederatque silentibus umbris:
  - Imbrasides (Imbrasides; インブラシデス): impiger *Imbrasides (umbr- trad.) 378:ペイロオス

379 dumque auidus praedae iuuenem spoliare parabat,
- [2] 379 Dum cupidus praedae juvenem spoliare parabat,
- [3] 379 Dumque auidus praedae iuuenem spoliare parabat,
- [4] 379 Dumque avidus praedae juvenem spoliare parabat,
- [6] 379 dumque avidus praedae iuvenem spoliare parabat,

380 desuper hasta uenit dextra librata Thoantis
- [2] 380 Desuper hasta venit dextra vibrata Thoantis,
- [3] 380 Desuper hasta uenit dextra librata Thoantis,
- [4] 380 Desuper hasta venit dextra librata Thoantis,
  - Thoantis (THOAS; トアス): Thoantis:トアスの右手が、構えた槍でペイロオスに向かう
- [6] 380 desuper hasta venit dextra librata Thoantis
  - Thoantis (Thoas; トアス): dextrā . . . Thoantis 380

381 perque uiri scapulas animosaque pectora transit;
- [2] 381 Perque viri scapulas annosaque pectora transit.
  - … *Scapulas*（肩甲骨/肩）という単語は、われらの作者がしばしば用いているが、私の知る限り、叙事詩人の中でこれを用いた者は誰もいない。卑俗で平民的な語とみなされていたからであろう。とりわけ喜劇作家たちに見出されるからである。われらの作者はその配慮を承知の上で無視したか、
  - **(cont.)** （前頁からの続き）あるいは知らなかったのである。――もっともオウィディウスは軽い主題において、身体のその部分を固有に指すものとして用いている（Art. Am. III, 273: « Conveniunt tenues scapulis analectides altis »）。またクラウディアヌスもこの語を用いている。パリ編者。
- [3] 381 Perque uiri scapulas annosaque pectora transit.
- [4] 381 Perque viri scapulas annosaque pectora transit.
- [6] 381 perque viri scapulas animosaque pectora transit.

382 in uultus ruit ille suos calidumque cruorem
- [2] 382 In vultus ruit ille suos, calidumque cruorem
- [3] 382 In uultus ruit ille suos calidumque cruorem
- [4] 382 In vultus ruit ille suos calidumque cruorem
- [6] 382 in vultus ruit ille suos calidumque cruorem

383 ore uomit stratusque super sua palpitat arma.
- [2] 383 Ore vomit, stratusque supersua palpitat arma.
  - *Stratusque super sua palpitat arma*（そして己の武具の上に横たわり身もだえする）。Virg. Aen. X, 488: « Corruit in vulnus: sonitum super arma dedere » に似ている。
- [3] 383 Ore uomit stratusque super sua palpitat arma.
- [4] 383 Ore vomit stratusque super sua palpitat arma.
- [6] 383 ore vomit stratusque super sua palpitat arma.

384 Sanguine Dardanii manabant undique campi,
- [2] 384 Sanguine Dardanii manabant undique campi ,
- [3] 384 Sanguine Dardanii manabant undique campi,
- [4] 384 Sanguine Dardanii manabant undique campi,
  - Dardanii (DARDANIUS; ダルダニアの): Dardanii campi:ダルダニアの野は血に濡れる
- [6] 384 sanguine Dardanii manabant undique campi,
  - Dardanii (Dardanius; ダルダニアの): -ii . . . campi 384:トロイアの

385 manabant amnes passim. Pugnabat ubique
- [2] 385 Manabant amnes passim , puguabat ubique
- [3] 385 Manabant amnes passim; pugnatur ubique
- [4] 385 Manabant amnes passim ; pugnatur ubique,
- [6] 385 manabant amnes passim; pugnatur ubique
  - amnes (Xanthus (fluvius); クサントス(河)): amnes 385

386 immixtis ardens amborum exercitus armis
- [2] 386 Immixtis ardens amborum exercitus armis ,
- [3] 386 [Inmixtis ardens amborum exercitus armis]
- [4] 386 Ardet et immixtis amborum exercitus armis,
- [6] 386 inmixtis ardens amborum exercitus armis

387 et modo Troianis uirtus, modo crescit Achiuis
- [2] 387 Et modoTrojanis virtus, modo crescit Achivis ,
- [3] 387 Et modo Troianis uirtus, modo crescit Achiuis,
- [4] 387 Et modo Trojanis virtus, modo crescit Achivis,
  - Achivis (GRAI; ギリシア人): — 彼らの武勇が増す
  - Trojanis (TROJANI; トロイア人): Trojanis:トロイア人の武勇が増す
- [6] 387 et modo Troianis, modo virtus crescit Achivis
  - Achivis (Achivi; アカイア人): -is 69. 387
  - Troianis (Troianus; トロイアの): Troianis . . . virtus crescit 387

388 laetaque per uarios petitur uictoria casus.
- [2] 388 Lsetaque per varios petitur victoria casus.
- [3] 388 Laetaque per uarios petitur uictoria casus.
- [4] 388 Laetaque per varios petitur victoria casus.
- [6] 388 laetaque per varios petitur victoria casus.

## Book 5

389 Hic postquam Danaum longe cedentia uidit
- [2] 389 V. Sed postquam Danaum longe cedentia vidit
- [3] 389 Hic postquam Danaum longe cedentia uidit
- [4] 389 Hic postquam Danaum longe cedentia vidit
  - Danaum (GRAI; ギリシア人): — 退く隊列
- [6] 389 hic postquam Danaum longe cedentia vidit
  - Danaum (Danai; ダナオイ): -um(属格):19. 50. 67. 124. 153. 251. 268. 357. 389. 496. 631. 686. 691. 698. 705. 743. 747. 794. 1025

390 agmina Tydides tumidumque increscere Martem,
- [2] 390 Agmina Tydides, tumidumque increscere Martem,
  - *Tumidumque increscere Martem*（そして高まる軍神［戦い］が増大するのを）：おそらくマロー（ウェルギリウス）の次の箇所（Aen. IX, 687: « Tum magis increscunt animis discordibus irae »）から形作られたのであろう。
- [3] 390 Agmina Tydides tumidumque increscere Martem,
- [4] 390 Agmina Tydides tumidumque increscere Martem.
  - Tydides (DIOMEDES; ディオメデス): — ダナオイが退くのを見る
  - Martem (MARS; マルス): Martem:ディオメデスはマルスが膨れ上がり大きくなるのを見る
- [6] 390 agmina Tydides tumidumque increscere Martem,
  - Martem (Mars; マルス): tumidumque increscere Martem、すなわち戦争、390
  - Tydides (Tydides; テュディデス): Tydides 390. 408. 530. 665. 1008

391 in medias acies, qua plurimus imminet hostis,
- [2] 391 In medias acies, qua plurimus imminet hostis,
- [3] 391 In medias acies, qua plurimus imminet hostis,
- [4] 391 In medias acies, qua plurimus imminet hostis,
- [6] 391 in medias acies, qua plurimus imminet hostis,

392 irruit et uersas prosternit caede phalangas;
- [2] 392 Irruit, et versas prosternit caede phalanges,
- [3] 392 Inruit et uersas prosternit caede phalanges:
- [4] 392 Irruit et versas prosternit caede phalanges
- [6] 392 inruit et versas prosternit caede phalangas:

393 huc illuc ensemque ferox hastamque coruscat.
- [2] 393 Huc illuc ensemque ferox hastamque coruscat.
- [3] 393 Huc illuc ensemque ferox hastamque coruscat.
- [4] 393 Huc illuc ensemque ferox hastamque coruscat.
- [6] 393 huc illuc ensemque ferox hastamque coruscat.

394 Bellica Pallas adest flagrantiaque ignibus arma
- [2] 394 Bellica Pallas adest, flagrantiaque ignibus arma
  - *Bellica Pallas adest*（戦のパラスが寄り添う）。これらはオウィディウスの Met. V, 47: « Bellica Pallas adest, et protegit aegide fratrem, Datque animos » から取られている。――ディオメデスに火と燃える武具（*flagrantia ignibus arma*）を与えるのは、パラスが彼の兜と楯から絶え間ない火を輝かせたとするホメロス（V, 4: Δαῖέ οἱ ἐκ κόρυθός τε καὶ ἀσπίδος ἀκάματον πῦρ）に基づいている。また下掲 467 行で、われらの詩人はディオメデスについて *flagrantibus irruit armis* と述べている。
- [3] 394 Bellica Pallas adest flagrantiaque ignibus arma
- [4] 394 Bellica Pallas adest flagrantiaque ignibus arma
  - Pallas (MINERVA; ミネルウァ): — 戦の女神は戦いでディオメデスに付き添う
- [6] 394 bellica Pallas adest flagrantiaque ignibus arma
  - Pallas (Pallas; パラス): bellica -as 394

395 adiuuat atque animos iuueni uiresque ministrat.
- [2] 395 Adjuvat, atque animos juveni viresque ministrat
- [3] 395 Adiuuat atque animos iuueni uiresque ministrat.
- [4] 395 Adjuvat atque animos juveni viresque ministrat.
- [6] 395 adiuvat atque animos iuveni viresque ministrat.
  - iuveni (Diomedes; ディオメデス): 395 iuveni

396 Ille, boum ueluti uiso grege saeua leaena,
- [2] 396 lile, boum veiuti viso grege saeva leasna,
  - *Saeva leaena*（獰猛な雌獅子）。群れに襲いかかるライオンの比喩をウェルギリウスはしばしば用いている（Aen. IX, 339 以下、X, 723 以下など）。ホメロスは確かにディオメデスの突撃を激-
  - **(cont.)** （前頁からの続き）［-流に、橋や垣根や作物を押し流す激流に］なぞらえているが、われらの詩人はホメロスの手本を捨てることのほうが多く、好機があればいつでもウェルギリウスやオウィディウスから提供された題材を用いるほうを好む。
- [3] 396 Atque boum ueluti uiso grege saeua leaena,
- [4] 396 Ille, boum veluti viso grege saeva leaena,
- [6] 396 ille — boum veluti viso grege saeva leaena,

397 quam stimulat ieiuna fames, ruit agmina contra
- [2] 397 Quam stimulat jejuna fames, ruit agmina contra,
- [3] 397 Quam stimulat ieiuna fames, ruit agmina contra
- [4] 397 Quam stimulat jejuna fames, ruit agmina contra
- [6] 397 quam stimulat ieiuna fames, ruit agmina contra

398 et prostrata necat uesano corpora dente,
- [2] 398 Et prostrata necat vesano corpora dente;
- [3] 398 Et prostrata necat uesano corpora dente:
- [4] 398 Et prostrata necat vesano corpora dente :
- [6] 398 et prostrata necat vesano corpora dente:

399 sic ruit in medios hostes Calydonius heros,
- [2] 399 Sic ruit in medios hostes Calydonius heros,
- [3] 399 Sic ruit in medios hostes Calydonius heros,
- [4] 399 Sic ruit in medios hostes Calydonius heros,
  - Calydonius (DIOMEDES; ディオメデス): Calydonius heros:敵の只中に突進する
- [6] 399 sic ruit in medios hostes Calydonius heros,
  - Calydonius (Calydonius; カリュドンの): Calydonius heros 399. 454

400 uirginis armigerae monitis et numine tutus.
- [2] 400 Virginis armigerse monitis et numine tutus.
  - *Virginis armigerae*（武具を帯びた乙女の）：パラスのこと。…ウェルギリウスにおいては Aen. II, 425 および XII, 483 で *armipotens*（武勇に秀でた）と呼ばれている。
- [3] 400 Virginis armigerae monitis et numine tutus.
- [4] 400 Virginis armigerae monitis et numine tutus.
  - Virginis (MINERVA; ミネルウァ): Virgo armigera Virginis armigerae:武装した乙女の忠告と神威
- [6] 400 virginis armigerae monitis et numine tutus.
  - armigerae (armigera; 武装した): virginis armigerae 400. 545:ミネルウァの

401 Conuersi dant terga Phryges, fugientibus ille
- [2] 401 Conversi dant terga Phryges ; fugientibus iile
- [3] 401 Conuersi dant terga Phryges; fugientibus ille
- [4] 401 Conversi dant terga Phryges; fugientibus ille
  - Phryges (TROJANI; トロイア人): Phryges:逃げる
- [6] 401 conversi dant terga Phryges; fugientibus ille
  - Phryges (Phryges; プリュギア人): Phryges 401. 493. 636. 682. 762. 803

402 instat et exstructos morientum calcat aceruos.
- [2] 402 Instat, et exstructos morientum calcat acervos.
  - … そしてこれがナーソー（オウィディウス）から借用されたものであることは Met. V, 88 から明らかである: « Sternit, et exstructos morientum calcat acervos »。…
- [3] 402 Instat et exstructos morientum calcat aceruos.
- [4] 402 Instat et exstructos morientum calcat acervos.
- [6] 402 instat et exstructos morientum calcat acervos.

403 Dumque ferit sternitque uiros, uidet ecce Daretis
- [2] 403 Dumque furit stemitque viros, videt ecce Daretis
  - … それどころか、ホラーティウスが Carm. I, 15, 27 でディオメーデスの固有の描写であるかのように用いているため、*furit* のほうがなおさら優れている: « Ecce furit te reperire atrox Tydides, melior patre »。…ホメロスが V, 10 でペゲウスとイダイオスの父と呼んでいる *Daretis*（ダレスの）…
- [3] 403 Dumque furit sternitque uiros, uidet ecce Daretis
- [4] 403 Dumque ferit sternitque viros, videt ecce Daretis
  - Daretis (DARES; ダレス): Daretis:ディオメデスは敵の戦列にダレスの息子たちを見つける
- [6] 403 dumque ferit sternitque viros, videt ecce Daretis
  - Daretis (Dares; ダレス): *Daretis . . . natos, Phegeaque Idaeumque 403. トロイア人の間のウルカヌスの神官の

404 aduerso stantes furibundus in agmine natos,
- [2] 404 Adverso stantes furibundus in agmine natos,
- [3] 404 Aduerso stantes fremibundus in agmine natos,
- [4] 404 Adverso stantes furibundus in agmine natos,
- [6] 404 adverso stantes furibundus in agmine natos,

405 Phegeaque Idaeumque simul; quem cuspide Phegeus
- [2] 405 Phegeum Idaeumque simul, quem cuspide praeceps
- [3] 405 Phegeaque Idaeumque simul; quem cuspide Phegeus
- [4] 405 Phegeaque Idaeumque simul; quem cuspide Phegeus
  - Phegeaque …（『イリアス』V, 9 以下）。…
  - Idaeum (IDAEUS Daretis filius; イダイオス、ダレスの子): Idaeum:ディオメデスは戦列の中に兄弟とともにいるイダイオスを見つける
  - Phegeus (PHEGEUS; ペゲウス): ディオメデスに向けて槍を放つ
  - Phegea (PHEGEUS; ペゲウス): Phegea:ディオメデスは戦列の中にペゲウスを見る
- [6] 405 Phegeaque Idaeumque simul; quem cuspide Phegeus
  - Idaeum (Idaeus 1; イダイオス 1): Daretis . . . natos, Phegeaque Idaeumque 405
  - Phegeus (Phegeus; ペゲウス): *Phegeus 405
  - Phegea (Phegeus; ペゲウス): Daretis natos . . . *Phegeaque Idaeumque 405

406 occupat ante graui, sed uulnera depulit umbo
- [2] 406 Occupat ille gravi, sed vulnera depulit umbo,
- [3] 406 Occupat ante graui, sed uulnera depulit umbo,
- [4] 406 Occupat ante gravi, sed vulnera depulit umbo,
- [6] 406 occupat ante gravi, sed vulnera depulit umbo

407 uitatumque solo ferrum stetit. Haud mora: totis
- [2] 407 Vibratumque solo ferrum stetit : haud mora , totis
  - … ――*Stetit*（立った、刺さった）はラオコオンの槍についてのウェルギリウス Aen. II, 52 から採られている: « stetit illa tremens »。パリ編者。
- [3] 407 Uitatumque solo ferrum stetit: haut mora, totis
- [4] 407 Vitatumque solo ferrum stetit : haut mora, totis
- [6] 407 vitatumque solo ferrum stetit: haud mora, totis

408 ingentem torquet Tydides uiribus hastam
- [2] 408 Ingentem torquet Tydides viribus hastam,
  - *Ingentem torquet* 等（巨大な［槍を］投げつける）は、『アエネーイス』の引用箇所におけるウェルギリウス自身の言葉である。
- [3] 408 Ingentem torquet Tydides uiribus hastam
- [4] 408 Ingentem torquet Tydides viribus hastam
  - Tydides (DIOMEDES; ディオメデス): — ペゲウスを殺す
- [6] 408 ingentem torquet Tydides viribus hastam
  - Tydides (Tydides; テュディデス): Tydides 390. 408. 530. 665. 1008

409 transadigitque uiri pectus: pars cuspidis ante
- [2] 409 Transadigitque viri pectus : pars cuspidis ante
  - … われわれは *Transadigit*（そして突き通す）を置いた。Virg. Aen. IX, 544: « pectora duro Transfossi ligno »。
- [3] 409 Transadigitque uiri pectus; pars cuspidis ante
- [4] 409 Transadigitque viri pectus ; pars cuspidis ante
- [6] 409 transadigitque viri pectus; pars cuspidis ante
  - viri (Phegeus; ペゲウス): viri 409 を参照

410 eminet et prodit scapulis pars altera fossis.
- [2] 410 Eininet, et prodit scapulis pars altera fossis.
  - *Eminet, et prodit* 等（突き出て、現れ出る）。オウィディウス Metam. IX, 127 と同様である: « terga sagitta Trajicit: exstabat ferrum de pectore aduncum »；また同第 V 巻 138: « Torquet in hunc hastam, media quae nare recepta Cervice exacta est, in partesque eminet ambas »。この意味で、反対側に突き抜ける放たれた飛び道具について、グラッティウスの Halieut. 62 行で言及されている。――本著作第 I 巻第 1 部 224 頁を見よ。パリ編者。
- [3] 410 Eminet, et prodit scapulis pars altera fossis.
- [4] 410 Eminet, et prodit scapulis pars altera fossis.
- [6] 410 eminet et prodit scapulis pars altera fossis.

411 Hunc ubi fundentem calidum de pectore flumen
- [2] 411 Hunc ubi fundentem calidum de pectore flumen,
  - *Calidum de pectore flumen*（胸から温かい奔流を）。Virg. Aen. IX, 414: « Volvitur ille, vomens calidum de pectore flumen »；また同第 XI 巻 668: « Sanguinis ille vomens rivos cadit »。
- [3] 411 Hunc ubi fundentem calidum de pectore flumen
- [4] 411 Hunc ubi fundentem calidum de pectore flumen
- [6] 411 hunc ubi fundentem calidum de pectore flumen

412 uersantemque oculos animamque per ora uomentem
- [2] 412 Versantemque oculos, animamque per ora vomentem
- [3] 412 Uersantemque oculos animamque per ora uomentem
- [4] 412 Versantemque oculos animamque per ora vomentem
- [6] 412 versantemque oculos animamque per ora vomentem

413 conspexit frater, stricto celer aduolat ense
- [2] 413 Conspexit frater, stricto celer advolat ense ,
- [3] 413 Conspexit frater, stricto celer aduolat ense
- [4] 413 Conspexit frater, stricto celer advolat ense
- [6] 413 conspexit frater, stricto celer advolat ense
  - frater (Idaeus 1; イダイオス 1): frater 413 を参照

414 germanique cupit fatorum exsistere uindex.
- [2] 414 Germanique cupit fatorum exsistere vindex.
  - *Cupit exsistere vindex*（復讐者として立ち現れることを望む）。この言い回しはバルトにとって野蛮語の匂いがするものと思われる（『雑考』LVIII, 14 および LIX, 1, p. 2770）。彼は長老アルボインのある箇所から、中世の著述家たちが動詞 *subsistere* を同様に用いたことを論証している。そして確かにこの語法は詩行を緩慢なものにしており、古き時代の詩人たちは概してこれを避けていたように見える。しかしだからといって私はこれを野蛮語に帰そうとは思わない。おそらくこの箇所での *exsistere* は、*exstare*（際立つ）、*eminere*（抜きん出る）、*conspicuum esse*（目立つ）の代わりに置かれているのであろう。動詞 *subsistere* については、それがスコラ学者たちの野蛮なラテン語に属することはより確実である。――しかし *fieri*（なる）や *esse*（である）の意で *exsistere* を用いるのは、下層の時代の著述家たちによって導入されたように思われる。実際、ユリウス・エクススペランティウスは次のように述べている: « Facile enim poterant exsistere proditores; quia egestas haud facile habetur sine damno »。またラクタンティウス・プラキドゥスも『オウィディウス変身物語綱要』第 VI 巻第 3 話で次のように述べている: « Latona questa cum filiis, quod suarum injuriarum ultores non exsisterent »。パリ編者。
- [3] 414 Germanique cupit fatorum existere uindex.
- [4] 414 Germanique cupit fatorum existere vindex.
- [6] 414 germanique cupit fatorum existere vindex.
  - germani (Phegeus; ペゲウス): germani 414. 421

415 Sed neque uim saeui nec fortia sustinet arma
- [2] 415 Sed neque vim saevi , nec fortia sustinet arma
- [3] 415 Sed neque uim saeui nec fortia sustinet arma
- [4] 415 Sed neque vim saevi nec fortia sustinet arma
- [6] 415 sed neque vim saevi nec fortia sustinet arma
  - Tydidae (Tydides; テュディデス): saevi . . . -dae 415

416 Tydidae contraque tamen defendere temptat.
- [2] 416 Tydidae , contraque tamen defendere tentat.
- [3] 416 Tydidae contraque tamen defendere temptat.
- [4] 416 Tydidae contraque tamen defendere temptat.
  - Tydidae (DIOMEDES; ディオメデス): Tydidae:イダイオスは残忍なテュディデスの強い武器に耐えられない
- [6] 416 Tydidae contraque tamen defendere temptat.

417 Vt uolucris, discerpta sui cum corpora nati
- [2] 417 Ut volucris , derepta sui quum corpora nati
- [3] 417 Ut uolucris, derepta sui cum corpora nati
- [4] 417 Ut volucris, derepta sui cum corpora nati
- [6] 417 ut volucris, discerpta sui cum corpora nati

418 accipitrem laniare uidet nec tendere contra,
- [2] 418 Accipitrem laniare videt, nec tendere contra,
- [3] 418 Accipitrem laniare uidet nec tendere contra
- [4] 418 Accipitrem laniare videt, nec tendere contra
- [6] 418 accipitrem laniare videt nec tendere contra,

419 auxilium neque ferre suo ualet anxia nato
- [2] 419 Auxilium nec ferre suo valet anxia nato,
- [3] 419 Auxilium nec ferre suo ualet anxia nato,
- [4] 419 Auxilium nec ferre suo valet anxia nato,
- [6] 419 auxilium neque ferre suo valet anxia nato

420 quodque potest, leuibus plaudit sua pectora pennis,
- [2] 420 Quodque potest , levibus plangit sua pectora pennis ;
- [3] 420 Quodque potest, leuibus plangit sua pectora pennis:
- [4] 420 Quodque potest, levibus plangit sua pectora pennis :
- [6] 420 quodque potest, levibus plaudit sua pectora pennis:

421 sic hostem Idaeus germani caede superbum
- [2] 421 Sic hostem Idaeus germani caede superbum
- [3] 421 Sic hostem Idaeus germani caede superbum
- [4] 421 Sic hostem Idaeus germani caede superbum
  - Idaeus (IDAEUS Daretis filius; イダイオス、ダレスの子): — ディオメデスが傷つけた兄弟を助けることができない
- [6] 421 sic hostem Idaeus germani caede superbum
  - Idaeus (Idaeus 1; イダイオス 1): -us 421
  - germani (Phegeus; ペゲウス): germani 414. 421

422 spectat atrox miseroque nequit succurrere fratri
- [2] 422 Spectat atrox, miseroque nequit succurrere fratri.
- [3] 422 Spectat atrox miseroque nequit succurrere fratri;
- [4] 422 Spectat atrox miseroque nequit succurrere fratri;
- [6] 422 spectat atrox miseroque nequit succurrere fratri
  - fratri (Phegeus; ペゲウス): fratri 422

423 et, nisi cessisset, dextra cecidisset eadem.
- [2] 423 Et nisi cessisset, dextra cecidisset eadem.
- [3] 423 Et nisi cessisset, dextra cecidisset eadem.
- [4] 423 Et nisi cessisset, dextra cecidisset eadem.
- [6] 423 et, nisi cessisset, dextra cecidisset eadem.

424 Nec minus in Teucros armis furit alter Atrides
- [2] 424 Nec minus in Teucros armis furit acer Atrides ,
- [3] 424 Nec minus in Teucros armis furit alter Atrides
- [4] 424 Nec minus in Teucros armis furit alter Atrides
  - Atrides (AGAMEMNON; アガメムノン): — トロイア人に対し武器をとって荒れ狂う
  - Teucros (TROJANI; トロイア人): In Teucros:アガメムノンはテウクロイに対して荒れ狂う
- [6] 424 nec minus in Teucros armis furit † alter Atrides
  - Atrides (Atrides (Agamemno); アトリデス（アガメムノン）): alter(?) -es 424
  - Teucros (Teucri; テウクロイ): -os 424. 903

425 insequiturque acies et ferro funera miscet.
- [2] 425 Insequiturque acies, et ferro vulnera miscet.
- [3] 425 Insequiturque acies et ferro funera miscet.
- [4] 425 Insequiturque acies et ferro funera miscet.
- [6] 425 insequiturque acies et ferro funera miscet.

426 Obuius huic fatis occurrit ductus iniquis
- [2] 426 Obvius huic JTatis occurrit ductus iniquis
- [3] 426 Obuius huic fatis occurrit ductus iniquis
- [4] 426 Obvius huic fatis occurrit ductus iniquis
- [6] 426 obvius huic fatis occurrit ductus iniquis

427 infelix Odius, quem uastae cuspidis ictu
- [2] 427 Infelix Hodius, quem vasto cuspidis ictu
  - … ホメロス『イリアス』V, 39 から *Hodius*（オディオス）と読むべきである。
- [3] 427 Infelix Hodius, quem uastae cuspidis ictu
- [4] 427 Infelix Hodius, quem jactae cuspidis ictu
  - Hodius …（『イリアス』V, 39）。…
  - Hodius (HODIUS; オディオス): — 不幸な者、アガメムノンに打ち倒される
- [6] 427 infelix Odius, quem vastae cuspidis ictu
  - Odius (Odius; オディオス): infelix -us 427

428 sternit et ingenti scapulas transuerberat hasta.
- [2] 428 Sternit, et ingenti scapulas transverberat hasta.
- [3] 428 Sternit et ingenti scapulas transuerberat hasta.
- [4] 428 Sternit et ingenti scapulas transverberat hasta.
- [6] 428 sternit et ingenti scapulas transverberat hasta.

429 Hinc petit Idomeneus aduersa parte ruentem
- [2] 429 Hinc petit Idomeneus adversa parte ruentem
  - … そしてこれはホメロスの詩行 V, 43: Ἰδομενεὺς δ᾽ ἄρα Φαῖστον ἐνήρατο Μῄονος υἱόν をより完全に表現している。…
- [3] 429 Hinc ferit Idomeneus aduersa parte ruentem
- [4] 429 Hinc petit Idomeneus adversa ex parte ruentem
  - Idomeneus (IDOMENEUS; イドメネウス): — パイストスを斬り殺す
- [6] 429 hinc petit Idomeneus adversa parte ruentem
  - Idomeneus (Idomeneus; イドメネウス): -eus 429

430 Maeoniden Phaestum, cuius post funera laetus
- [2] 430 Maeoniden Phaestum, cujus postfunera Atrides
- [3] 430 Maeoniden Phaestum; cuius post funera Atrides
- [4] 430 Maeoniden Phaestum; cujus post funera laetus
  - Maeoniden Phaestum …（『イリアス』V, 43）。…
  - Phaestum (PHAESTUS; パイストス): Phaestum:イドメネウスがマイオニア人パイストスを打つ
- [6] 430 Maeoniden Phaestum; cuius post funera laetus
  - Maeoniden (Maeonides; マエオニデス): *Maeoniden Phaestum 430
  - Phaestum (Phaestus; パイストス): Maeoniden *Phaestum 430:Μήονος υἱὸν Βώρου ἐκ Τάρνης(「タルネから来たマイオニア人ボロスの子」)

431 et Strophio genitum Stygias demittit ad umbras.
- [2] 431 Et Strophio genitum Stygias demittit ad umbras.
  - … ――同様に上の 360 行でも *demissus ad umbras*。パリ編者。
- [3] 431 E Strophio genitum Stygias demittit ad umbras.
- [4] 431 E Strophio genitum Stygias demittit ad umbras.
  - … Strophio …（『イリアス』V, 49）。
  - Strophio (STROPHIUS; ストロピオス): e Strophio genitum:イドメネウスがストロピオスの子(すなわちスカマンドリオス)を斬り殺す
  - Stygias (STYGIUS; ステュクスの): ad Stygias undas:ステュクスの波へ
- [6] 431 et Strophio genitum Stygias demittit ad umbras.
  - Strophio (Strophius; ストロピオス): Strophio genitum 431:スカマンドリオス
  - Stygias (Stygius; ステュクスの): Stygias . . . ad umbras 431

432 Meriones Phereclum librata percutit hasta
- [2] 432 Meriones Phereclum vibrata percutit hasta,
- [3] 432 Meriones Phereclum uibrata perculit hasta,
- [4] 432 Meriones Phereclum vibrata perculit hasta,
  - **432-433** Meriones Phereclum（『イリアス』V, 59）、vibrata perculit, Pedaeumque Meges（『イリアス』V, 69）…
  - Meriones (MERIONES; メリオネス): — ペレクロスを斬り殺す
  - Phereclum (PHERECLUS; ペレクロス): Phereclum:メリオネスがペレクロスを殺す
- [6] 432 Meriones Phereclum librata percutit hasta,
  - Meriones (Meriones; メリオネス): -nes *432. 1013
  - Phereclum (Phereclus; ペレクロス): *Phereclum 432:Τέκτονος υἱὸν Ἁρμονίδεω(「ハルモンの子テクトンの子」)

433 Pedaeumque Meges. Tum uastis horridus armis
- [2] 433 Pedaeumque Meges , vastisque horrendus in armis
- [3] 433 Pedaeumque Meges; tum uastis horridus armis
- [4] 433 Pedaeumque Meges ; tum vastis horridus armis
  - Eurypylus (EURYPYLUS; エウリュピュロス): 巨大な武具で恐るべき者、ヒュプセノルを殺す
  - Meges (MEGES; メゲス): — ペダイオスを斬り殺す
  - Pedaeum (PEDAEUS; ペダイオス): Pedaeum:メゲスがペダイオスを殺す
- [6] 433 Pedaeumque Meges; tum vastis horridus armis
  - Meges (Meges; メゲス): *Meges 433. ピュレウスの子、ギリシア側
  - Pedaeum (Pedaeus; ペダイオス): *Pedaeum 433:アンテノルの庶子

434 Eurypylus gladio uenientem Hypsenora fundit
- [2] 434 Eurypyius gladio venieutem Hypsenora fundit,
  - ボンダムの指摘（p. 158）にも従い、ホメロス『イリアス』V, 76 に基づいて *Hypsenora*（ヒュプセノルを）と記した。…
- [3] 434 Eurypylus gladio metuentem Hypsenora fundit
- [4] 434 Eurypylus gladio venientem Hypsenora fundit
  - … Hypsenora …（『イリアス』V, 76 以下）。
  - Hypsenora (HYPSENOR; ヒュプセノル): Hypsenora:エウリュピュロスは向かって来るヒュプセノルを斬り殺す
- [6] 434 Eurypylus gladio venientem Hypsenora fundit
  - Eurypylus (Eurypylus; エウリュピュロス): vastis horridus armis Eurypylus 434
  - Hypsenora (Hypsenor; ヒュプセノル): *Hypsenoră 434:ドロピオンの子

435 et pariter uita iuuenem spoliauit et armis.
- [2] 435 Et pariter juvenem vita spoliavit et arnris.
- [3] 435 Et pariter uita iuuenem spoliauit et armis.
- [4] 435 Et pariter vita juvenem spoliavit et armis.
- [6] 435 et pariter vita iuvenem spoliavit et armis.

436 Parte alia uolitat sinuoso Pandarus arcu
- [2] 436 Parte alia volitat sinuoso Pandarus arcu,
- [3] 436 Parte alia uolitat sinuoso Pandarus arcu
- [4] 436 Parte alia volitat sinuoso Pandarus arcu
  - Pandarus (PANDARUS; パンダロス): — 軍勢の中を飛び回る
- [6] 436 parte alia volitat sinuoso Pandarus arcu
  - Pandarus (Pandarus; パンダロス): -us 346. 436

437 Tydidenque oculis immensa per agmina quaerit;
- [2] 437 Tydidemque oculis immensa per agmina quaerit :
- [3] 437 Tydidenque oculis inmensa per agmina quaerit.
- [4] 437 Tydidenque oculis immensa per agmina quaerit.
  - Tydiden (DIOMEDES; ディオメデス): Tydiden:パンダロスはテュディデスを探す
- [6] 437 Tydidenque oculis inmensa per agmina quaerit.
  - Tydiden (Tydides; テュディデス): -den 437:ディオメデス

438 quem postquam Troum sternentem corpora uidit,
- [2] 438 Quem postquam vidit sternentem corpora Troum ,
- [3] 438 Quem postquam Troum sternentem corpora uidit,
- [4] 438 Quem postquam Troum sternentem corpora vidit,
  - Troum (TROJANI; トロイア人): — パンダロスはディオメデスがトロイア人の身体を打ち倒すのを見る
- [6] 438 quem postquam Troum sternentem corpora vidit,
  - Troum (Tros; トロイア人): Troum 102. 281. 339. 357. 438. 631. 641. 701. 963

439 horrida contento derexit spicula cornu
- [2] 439 Horrida direxit contento spicula cornu ,
- [3] 439 Horrida contento derexit spicula cornu
- [4] 439 Horrida contento derexit spicula cornu
- [6] 439 horrida contento derexit spicula cornu

440 et summas umeri destringit acumine partes.
- [2] 440 Et summas humeri distrinxit acumine partes.
- [3] 440 Et summas humeri destrinxit acumine partes.
- [4] 440 Et summas umeri destrinxit acumine partes.
- [6] 440 et summas umeri destringit acumine partes.

441 Tum uero ardescit iuuenis Calydonius ira
- [2] 441 Tunc vero ardescit juvenis Calydonius ira,
- [3] 441 Tum uero ardescit iuuenis Calydonius ira
- [4] 441 Tum vero ardescit juvenis Calydonius ira,
  - Calydonius (DIOMEDES; ディオメデス): Calydonius juvenis:怒りに燃える
- [6] 441 tum vero ardescit iuvenis Calydonius ira
  - Calydonius (Calydonius; カリュドンの): iuvenis -us 441:ディオメデス

442 in mediasque acies animosi more leonis
- [2] 442 In medias acies animosi more leonis
- [3] 442 In mediasque acies animosi more leonis
- [4] 442 In mediasque acies animosi more leonis
- [6] 442 in mediasque acies animosi more leonis

443 fertur et Astynoum, magnum quoque Hypirona fundit,
- [2] 443 Fertur, et Astynoum magnumque Hypenora fundit,
  - … この行も続く 4 行とともに、名高いボンダムがホメロス『イリアス』V, 144–160 の導きによって健全な形に復元した（pp. 158 以下の）とおりに提示した。
- [3] 443 Fertur et Astynoum magnumque in Hypirona tendit:
- [4] 443 Fertur et Astynoum magnumque in Hypirona tendit :
  - Astynoum, Hypirona …（『イリアス』V, 144）。…
  - Astynoum (ASTYNOUS; アステュノオス): Astynoum:ディオメデスが彼を殺す
  - Hypirona (HYPIRON; ヒュペイロン): Hypirona:ディオメデスが偉大なヒュペイロンに襲いかかる
- [6] 443 fertur et Astynoum magnumque † Hyperona fundit:
  - Astynoum (Astynous; アステュノオス): *Astynoum 443
  - Hyperona (Hyperon; ヒュペイロン): magnum . . . *Hyperonă 443

444 comminus hunc gladio, iaculo ferit eminus illum;
- [2] 444 Cominus hunc gladio, jaculo ferit eminus illum.
- [3] 444 Cominus hunc gladio, iaculo ferit eminus illum.
- [4] 444 Cominus hunc gladio, jaculo ferit eminus illum.
- [6] 444 comminus hunc gladio, iaculo ferit eminus illum.

445 inde premit Polyidon Abantaque cuspide forti
- [2] 445 Inde premit Polyidon Abantaque cuspide forti ,
- [3] 445 Inde premit Polyidon Abantaque cuspide forti
- [4] 445 Inde premit Polyidon Abantaque cuspide forti
  - **445-446** Polyidon, Thoonem …（『イリアス』V, 148, 152）。
  - Abanta (ABAS; アバス): Abanta:ディオメデスが彼を殺す
  - Polyidon (POLYIDOS Eurydamantis filius; ポリュイドス、エウリュダマスの子): Polyidon:ディオメデスがポリュイドスを殺す
- [6] 445 inde premit Polyïdon Abantaque cuspide forti
  - Abanta (Abas; アバス): Abanta:ディオメデスが、エウリュダマスの子でポリュイドスの兄弟であるトロイア人アバスを殺した 445
  - Polyïdon (Polyidos; ポリュイドス): *Polyïdŏn (polidona trad.) 445:エウリュダマスの子

446 et notum bello Xanthum uastumque Thoonem.
- [2] 446 Et notum bello Xanthum , vastumque Thoonem.
- [3] 446 Et notum bello Xanthum uastumque Thoonem.
- [4] 446 Et notum bello Xanthum vastumque Thoonem.
  - Thoonem (THOON Phaenopis filius; トオン、パイノプスの子): Thoonem:ディオメデスが巨大なトオンを殺す
  - Xanthum (XANTHUS Phaenopis filius; クサントス、パイノプスの子): Xanthum:ディオメデスが戦で知られたクサントスを殺す
- [6] 446 et notum bello Xanthum vastumque Thoonem.
  - Thoonem (Thoon; トオン): vastum . . . *Thoonem 446:パイノプスの子
  - Xanthum (Xanthus (Phaenopis f.); クサントス(パイノプスの子)): notum bello Xanthum 446:パイノプスの子、トオンの兄弟

447 Post hos infestus Chromiumque et Echemmona telo
- [2] 447 Post hos infestus Chromiumque et Echemona telo
- [3] 447 Post hos infestos Chromiumque et Echemona telo
- [4] 447 Post hos infestus Chromiumque et Echemona telo
  - … Chromium, Echemona …（『イリアス』V, 159–160）。
  - Chromium (CHROMIUS Priami filius; クロミオス、プリアモスの子): Chromium:ディオメデスが彼を斬り殺す
  - Echemona (ECHEMON; エケムモン): Echemona:ディオメデスが彼を斬り殺す
- [6] 447 post hos infestos Chromiumque et Echemmona telo
  - Chromium (Chromius 2; クロミオス 2): Chromiumque et Echemmona 447:プリアモスの子ら
  - Echemmona (Echemmon; エケムモン): Echemmona 447:プリアモスの子

448 proturbat celeri pariterque ad Tartara mittit.
- [2] 448 Proturbat celeri, pariterque ad Tartara mittit.
- [3] 448 Proturbat celeri pariterque ad Tartara mittit.
- [4] 448 Proturbat celeri pariterque ad Tartara mittit.
  - Tartara (TARTARA; タルタロス): ad Tartara:ディオメデスがエケムモンをタルタロスへ送る
- [6] 448 proturbat celeri pariterque ad Tartara mittit.
  - Tartara (Tartara; タルタロス): ad Tartara mittit 448

449 Tu quoque Tydidae prostratus, Pandare, dextra
- [2] 449 Tu quoque Tydidae prostratus, Pandare, dextra
- [3] 449 Tu quoque Tydidae prostratus, Pandare, dextra
- [4] 449 Tu quoque Tydidae prostratus, Pandare, dextra
  - Tydidae (DIOMEDES; ディオメデス): — 彼の右手に倒されたパンダロス
  - Pandare (PANDARUS; パンダロス): Pandare:パンダロスよ、汝はディオメデスの手に倒れる
- [6] 449 tu quoque Tydidae prostratus, Pandare, dextra
  - Pandare (Pandarus; パンダロス): -re 449
  - Tydidae (Tydides; テュディデス): -dae . . . dextra 449

450 occidis, infelix, accepto uulnere tristi,
- [2] 450 Occidis infelix, accepto vulnere" tristi,
- [3] 450 Occidis, infelix, accepto uulnere tristi,
- [4] 450 Occidis, infelix, accepto vulnere turpi,
- [6] 450 occidis, infelix, accepto vulnere tristi,

451 dextera qua naris fronti coniungitur imae;
- [2] 451 Dextera qua naris fronti conjungitur imae ,
  - *Qua naris fronti conjungitur imae*（鼻が額の最下部に接するところ）。これはオウィディウス Met. XII, 315 から借用されたものと思われる: « inter duo lumina ferrum, Qua naris fronti committitur, accipit, imae »。
- [3] 451 Dextera qua naris fronti coniungitur imae.
- [4] 451 Dextera qua naris fronti conjungitur imae.
- [6] 451 dextera qua naris fronti coniungitur imae;

452 dissipat et cerebrum galeae cum parte reuulsum
- [2] 452 Dissipat et cerebrum galeae cum parte revulsum ,
- [3] 452 Dissipat et cerebrum galeae cum parte reuulsum
- [4] 452 Dissipat et cerebrum galeae cum parte revulsum
- [6] 452 dissipat et cerebrum galeae cum parte revulsum

453 ossaque confossa spargit Tydideus ensis.
- [2] 453 Ossaque confossi spargit Tydideus ensis.
- [3] 453 Ossaque confossi spargit Tydeius ensis.
- [4] 453 Ossaque confossi spargit Tydeius ensis.
  - Tydeius (TYDEIUS; テュディデスの): (ディオメデスの)ensis:テュディデスの剣
- [6] 453 ossaque confossa spargit Tydeius ensis.
  - Tydeius (Tydeius; テュディデスの): Tydeius ensis、ディオメデスの:453

454 Iamque manum Aeneas simul et Calydonius heros
- [2] 454 Jamque manum Aeneas simul et Calydonius heros
- [3] 454 Iamque manum Aeneas simul et Calydonius heros
- [4] 454 Jamque manum Aeneas simul et Calydonius heros
  - Aeneas (AENEAS; アイネイアス): — ディオメデスと戦う
  - Calydonius (DIOMEDES; ディオメデス): — アイネイアスと戦う
- [6] 454 iamque manum Aeneas simul et Calydonius heros
  - Aeneas (Aeneas; アイネイアス): -as 454. 516
  - Calydonius (Calydonius; カリュドンの): Calydonius heros 399. 454

455 contulerant, iactis inter se comminus hastis;
- [2] 455 Contulerant jactis inter se cominus hastis ,
- [3] 455 Contulerant iactisque inter se cominus hastis
- [4] 455 Contulerant jactisque inter se cominus hastis
- [6] 455 contulerant: iactis inter se comminus hastis

456 undique rimabant inimico corpora ferro,
- [2] 456 Undique rimabant inimico pectora ferro,
  - … しかし、この動詞が能動態の形でより高名な詩人に見出されるとは到底思えない。だがこれは、とっくに廃れていたこれらの動詞の形態を再び使用へと呼び戻すことが通例であった、後代の証左である。――われわれは別の例、*contemplaverit* を、ネメシアヌスの『鳥刺しについて』断片 3 行（本著作第 I 巻 182 頁）において見た。パリ編者。――なお、*rimabant pectora ferro*（剣で胸を探っていた）という言葉の意味は、敵のどの部分、どの場所に傷を負わせるかを窺い、試みていたということであり、そのことは第 458 行でより明瞭に示され、さらに第 593 行で同じ言回しがより完全に繰り返されている。…サレイウス・バッススも『ピソーへの詩』171 行で同様に述べている: « Et nunc vivaci scrutaris pectora dextra, Nunc latus adversum nec opino percutis ictu »。――シリオスは XIII, 163 で、この探り窺う動作を実に一層見事に描写しているように思われる: « At non idem animus Rutulo; spectatur, et omni Corpore perlustrat, qua sit certissima ferro In vulnus via, nunc vibrat, nunc comprimit hastam, etc. » パリ編者。
- [3] 456 Undique rimabant inimico corpora ferro
- [4] 456 Undique rimabant inimico corpora ferro,
- [6] 456 undique rimabant inimico corpora ferro

457 et modo cedebant retro, modo deinde coibant.
- [2] 457 Et modo cedebant retro, modo deinde coibant.
- [3] 457 Et modo cedebant retro, modo deinde coibant.
- [4] 457 Et modo cedebant retro, modo deinde coibant.
- [6] 457 et modo cedebant retro, modo deinde coibant.

458 Postquam utrique diu steterant nec uulnera magnus
- [2] 458 Postquani utrique diu steterant, nec vulnera magnus
- [3] 458 Postquam utrique diu steterant nec uulnera magnus
- [4] 458 Postquam utrique diu steterant nec vulnera magnus
  - Tydides (DIOMEDES; ディオメデス): — 偉大なる者、どこでアイネイアスを傷つけるべきかわからない
- [6] 458 postquam utrique diu steterant nec vulnera magnus

459 qua daret infesto Tydides ense uidebat,
- [2] 459 Qua daret infesto Tydides ense Videbat,
- [3] 459 Qua daret infesto Tydides ense uidebat,
- [4] 459 Qua daret infesto Tydides ense videbat,
- [6] 459 qua daret infesto Tydides ense videbat,
  - Tydides (Tydides; テュディデス): magnus . . . -des 459

460 saxum ingens medio quod forte iacebat in agro,
- [2] 460 Saxuin ingens, medio quod forte jacebat in agro,
- [3] 460 Saxum ingens, medio quod forte iacebat in agro,
- [4] 460 Saxum ingens, medio quod forte jacebat in agro,
- [6] 460 saxum ingens, medio quod forte iacebat in agro,

461 bis seni quod uix iuuenes tellure mouerent,
- [2] 461 Bisseni quod vix juvenes tellure levarent,
  - … なお、われらの詩人はこのくだり［ῥῆσιν］のほぼ全体をウェルギリウス Aen. XII, 896 以下から自らのものとして翻案した: « Nec plura effatus, saxum circumspicit ingens, Saxum antiquum, ingens, campo quod forte jacebat: Vix illud lecti bis sex cervice subirent »。ホメロスは、ディオメデスが投げた岩の大きさについてずっと控えめに、V, 303 で、現代の二人の男でも運べないような岩であったと述べている。
- [3] 461 Bis seni quod uix iuuenes tellure mouerent,
- [4] 461 Bis seni quod vix juvenes tellure levarent,
- [6] 461 bis seni quod vix iuvenes tellure moverent,
  - … ウェルギリウス『アエネーイス』12, 899 を参照

462 sustulit et magno conamine misit in hostem.
- [2] 462 Sustulit, et magno conamine misit in hostem.
- [3] 462 Sustulit et magno conamine misit in hostem.
- [4] 462 Sustulit et magno conamine misit in hostem.
- [6] 462 sustulit et magno conamine misit in hostem.

463 Ille ruit prostratus humi cum fortibus armis,
- [2] 463 Ille ruit prostratus humi cum fortibus armis,
- [3] 463 Ille ruit prostratus humi cum fortibus armis;
- [4] 463 Ille ruit prostratus humi cum fortibus armis;
- [6] 463 ille ruit prostratus humi cum fortibus armis;

464 quem Venus aetherias genetrix delapsa per auras
- [2] 464 Quem Yenus aethereas genitrix delapsa per auras
- [3] 464 Quem Uenus aethereas genetrix delapsa per auras
- [4] 464 Quem Venus aethereas genetrix delapsa per auras
  - Venus (VENUS; ウェヌス): — アイネイアスをディオメデスから
- [6] 464 quem Venus aethereas genetrix delapsa per auras
  - Venus (Venus; ウェヌス): Venus 315. 464. 911

465 accipit et nigra corpus caligine condit.
- [2] 465 Accipit, et nigra corpus caligine condit
- [3] 465 Excipit et nigra corpus caligine texit.
- [4] 465 Excipit, et nigra corpus caligine texit.
- [6] 465 accipit et nigra corpus caligine condit.
  - Accipit … だが Thes. I 311, 44 を参照 …

466 Non tulit Oenides animo nebulasque per ipsas
- [2] 466 Non tulit OEnidesanimo, nebulasque per ipsas
  - … バルトは『雑考』p. 2770 末で、続く詩行をきわめて優雅なものとして称賛すべきであると見なしている。
- [3] 466 Non tulit Oenides animis nebulasque per ipsas
- [4] 466 Non tulit Oenides animis nebulasque per ipsas
  - Oenides (DIOMEDES; ディオメデス): Oenides:ウェヌスの手を傷つける
- [6] 466 non tulit Oenides animis nebulasque per ipsas
  - … animis … ウェルギリウス『アエネーイス』8, 256 を参照 …
  - Oenides (Oenides; オエニデス): *Oenides 466:ディオメデス

467 fertur et in Venerem flagrantibus irruit armis,
- [2] 467 Fertur, etin Venerem flagrantibus irruit armis,
  - *Flagrantibus armis*（燃え盛る武具で）。第 394 行への注を見よ。
- [3] 467 Fertur et in Uenerem flagrantibus irruit armis
- [4] 467 Fertur et in Venerem flagrantibus irruit armis
  - Venerem (VENUS; ウェヌス): In Venerem:ディオメデスは武器をとってウェヌスに襲いかかる
- [6] 467 fertur et in Venerem flagrantibus irruit armis
  - Venerem (Venus; ウェヌス): in -rem 467

468 et neque quem demens ferro petat inspicit aruis
- [2] 468 Et neque, quem demens ferro petat, inspicit ante,
- [3] 468 Et neque quem demens ferro petat inspicit ante
- [4] 468 Et neque quem demens ferro petat inspicit ante
- [6] 468 et neque quem demens ferro petat inspicit . . . . .

469 caelestemque manum mortali uulnerat hasta.
- [2] 469 Caelestemque manum mortali vulnerat hasta.
  - … ホメロスが『イリアス』V, 337 でそう伝えており…。ウェルギリウス『アエネーイス』XI, 276 でもディオメデスが自分自身について同様に告白している: « quum ferro caelestia corpora demens Adpetii, et Veneris violavi vulnere dextram »。またオウィディウス Met. XV, 769 でも、ウェヌスが自らについて次のように述べている: « Quam modo Tydidae Calydonia vulneret hasta »。
- [3] 469 Caelestemque manum mortali uulnerat hasta.
- [4] 469 Caelestemque manum mortali vulnerat hasta.
- [6] 469 caelestemque manum mortali vulnerat hasta.

470 Icta petit caelum terris Cytherea relictis
- [2] 470 Icta petit caelum terris Cytherea relictis,
- [3] 470 Icta petit caelum terris Cytherea relictis
- [4] 470 Icta petit caelum terris Cytherea relictis
  - Cytherea (VENUS; ウェヌス): — ディオメデスの槍に打たれ、天へ向かう
- [6] 470 icta petit caelum terris Cytherea relictis
  - Cytherea (Cytherea; キュテレア): Cythereă 309. 335. 470:ウェヌス

471 atque ibi sidereae queritur sua uulnera matri.
- [2] 471 Atque ibi sidereae queritur sua vulnera malri.
  - … ホメロスも同様のことを命じている。彼は実に、傷ついたウェヌスがその兄-
  - **(cont.)** （前頁からの続き）［兄］マルスに戦車と馬を求めて天へと運ばれ、そこで母ディオネーに訴え出たと語っている（Iliad. V, 370: Ἡ δ᾽ ἐν γούνασι πῖπτε Διώνης δῖ᾽ Ἀφροδίτη Μητρὸς ἑῆς）。…
- [3] 471 Atque ibi sidereae queritur sua uulnera matri.
- [4] 471 Atque ibi sidereae queritur sua vulnera matri.
- [6] 471 atque ibi sidereae queritur sua vulnera matri.
  - matri (Dione; ディオネ): (Dione)、ウェヌスの母:sidereae . . . matri 471

472 Dardanium Aenean seruat Troianus Apollo
- [2] 472 Dardanium Aenean servat Trojanus Apollo ,
- [3] 472 Dardanium Aenean seruat Troianus Apollo
- [4] 472 Dardanium Aenean servat Trojanus Apollo
  - Aenean (AENEAS; アイネイアス): Aenean:トロイアのアポロがダルダニアのアイネイアスを救う
  - Apollo (APOLLO; アポロ): — トロイアの[アポロ]がアイネイアスを救う
- [6] 472 Dardanium Aenean servat Troianus Apollo
  - Aenean (Aeneas; アイネイアス): Dardanium -an 472
  - Apollo (Apollo; アポロ): Troianus -o 472. 830
  - Dardanium (Dardanius; ダルダニアの): -um Aenean 472

473 accenditque animos iterumque ad bella reducit.
- [2] 473 Accenditque aniinos, iterumque ad bella reducit.
- [3] 473 Accenditque animos iterumque ad bella reducit.
- [4] 473 Accenditque animos iterumque ad bella reducit.
- [6] 473 accenditque animos iterumque ad bella reducit.

474 Vndique consurgunt acies et puluere caelum
- [2] 474 Undique consurgunt acies, et pulvere caelum
- [3] 474 Undique consurgunt acies et puluere caelum
  - **474—482** 『ベレンガリウス事績録』I 195–202 が有する
- [4] 474 Undique consurgunt acies et pulvere caelum
- [6] 474 undique consurgunt acies et pulvere caelum
  - **474—481** （証言） = 『ベレンガリウスの事績』1, 195–202 (476 *in aequore cursu*)

475 conditur horrendisque sonat clamoribus aether.
- [2] 475 Conditur, horrendisque sonat clamoribus aether.
- [3] 475 Conditur horrendisque sonat clamoribus aether.
- [4] 475 Conditur horrendisque sonat clamoribus aether.
- [6] 475 conditur horrendisque sonat clamoribus aether.

476 Hic alius rapido deiectus in aequora curru
- [2] 476 Hic aUus rapido dejectus in aequora curru
- [3] 476 Hic alius rapido deiectus in aequora curru
- [4] 476 Hic alius rapido dejectus in aequora curru
- [6] 476 hic alius rapido deiectus in aequora curru

477 proteritur pedibusque simul calcatur equorum
- [2] 477 Proteritur, pedibusque simul calcatur equorum;
  - … 同様に Virgilii Aen. XII, 329: « Semineces volvit multos, aut agmina curru Proterit »。
- [3] 477 Proteritur pedibusque simul calcatur equorum;
- [4] 477 Proteritur pedibusque simul calcatur equorum;
- [6] 477 proteritur pedibusque simul calcatur equorum

478 atque alius uolucri traiectus corpora telo
- [2] 478 Atque alius volucri trajectus corpora telo,
- [3] 478 Atque alius uolucri traiectus pectora telo
- [4] 478 Atque alius volucri trajectus pectora telo
- [6] 478 atque alius volucri traiectus tempora telo

479 quadrupedis tergo pronus ruit; illius ense
- [2] 479 Quadrupedis tergo pronus ruit : illius ense
  - *Quadrupedis tergo*（四足獣の背から）。もし作者が、傷のために馬から転落する騎馬の兵士を意味しているのだとすれば、彼はホメロスの趣意に反し、また戦場における騎兵を知らず、英雄たちが戦車から戦うものと伝えるトロイア戦争の著述家たちの慣習に反して書いたことになる。同様の誤りは下の 496 行でも生じており、そこではアガメムノンが *sublimis equo volat agmina circum*（馬上に高く陣列の周りを馳せ巡る）とある。確かに騎乗を支持するものとしてホメロスの箇所 Il. X, 513 を引くことはできるが、ホメロスは ἵππων ἐπεβήσατο（馬に乗った）と言っているため、戦車に繋がれた馬と解するのが自然であろう。ウェルンスドルフ、補遺にて。
- [3] 479 Quadrupedis tergo pronus ruit; illius ense
- [4] 479 Quadrupedis tergo pronus ruit; illius ense
- [6] 479 cornipedis tergo pronus ruit; illius ense

480 deiectum longe caput a ceruice cucurrit;
- [2] 480 Dejectum longe caput a cervice cucurrit;
- [3] 480 Deiectum longe caput a ceruice cucurrit;
- [4] 480 Dejectum longe caput a cervice cucurrit;
- [6] 480 deiectum longe caput a cervice cucurrit;

481 hic iacet exanimis fuso super arma cerebro:
- [2] 481 Hic jacet exanimis fuso super arma cerebro.
  - … 同様に Virg. Aen. IX, 753: « Collapsos artus atque arma cruenta cerebro Sternit humi moriens »。
- [3] 481 Hic iacet exanimis fuso super arma cerebro:
- [4] 481 Hic jacet exanimis fuso super arma cerebro :
- [6] 481 hic iacet exanimis fuso super arma cerebro:

482 sanguine manat humus, campi sudore madescunt.
- [2] 482 Sanguine manal humus, campi sudore madescunt,
- [3] 482 Sanguine manat humus, campi sudore madescunt.
- [4] 482 Sanguine manat humus, campi sudore madescunt.
- [6] 482 sanguine manat humus, campi sudore madescunt.
  - （証言） = 『ベレンガリウスの事績』1, 204 以下

483 Emicat interea Veneris pulcherrima proles
- [2] 483 Emicat interea Veneris pulcherrima proles,
- [3] 483 Emicat interea Ueneris pulcherrima proles
- [4] 483 Emicat interea Veneris pulcherrima proles
  - Veneris (AENEAS; アイネイアス): Veneris proles:ウェヌスのいと麗しき子が軍勢の中に躍り出る
  - Veneris (VENUS; ウェヌス): Veneris:ウェヌスの子、アイネイアス
- [6] 483 emicat interea Veneris pulcherrima proles
  - proles (Aeneas; アイネイアス): および Venus 483
  - Veneris (Venus; ウェヌス): Aeneas, -eris . . . proles 236. 483

484 densaque Graiorum premit agmina nudaque late
- [2] 484 Densaque Graiorum premit agmina, nudaque late
- [3] 484 Densaque Graiorum premit agmina nudaque late
- [4] 484 Densaque Grajorum premit agmina nudaque late
  - Grajorum (GRAI; ギリシア人): — アイネイアスは彼らの隊列に迫る
- [6] 484 densaque Graiorum premit agmina nudaque late
  - Graiorum (Graius; ギリシアの): -orum . . . agmina 484

485 terga metit gladio funestaque proelia miscet.
- [2] 485 Terga metit gladio, funestaque praelia miscet.
  - **(cont.)** … おそらくウェルギリウスの半行 Aen. X, 513: « Proxima quaeque metit gladio »（剣で手当たり次第に薙ぎ払う）が彼の念頭にあったのかもしれない。
- [3] 485 Terga metit gladio funestaque praelia miscet.
- [4] 485 Terga metit gladio funestaque proelia miscet.
- [6] 485 terga metit gladio funestaque proelia miscet.

486 Nec cessat spes una Phrygum fortissimus Hector
- [2] 486 Nec cessat spes una PhryguiTi , fortissimus Hector,
  - *Spes una Phrygum*（プリュギア人たちの唯一の希望）。ヘクトルに対して頻出する賛辞である。ペンタディウスの「ヘクトルの墓碑銘」に *Occubuere simul spesque salusque Phrygum*（プリュギア人の希望と救いとが同時に倒れた）とあり、また以下の 944 行でわれらの詩人は « Unus, tota salus in quo Trojana manebat, Hector adest » と述べている。――とりわけ Virgil. Aen. II, 281: « O lux Dardaniae! spes o fidissima Teucrum! »。パリ編者。――なおバルトは Adv. p. 2771 で、これおよび後続の箇所が実に見事に書かれていると明言している。
- [3] 486 Nec cessat spes una Phrygum fortissimus Hector
- [4] 486 Nec cessat spes una Phrygum fortissimus Hector
  - Hector (HECTOR; ヘクトル): — 最も勇敢な者、ギリシア人を殺戮で打ち倒す
  - Phrygum (TROJANI; トロイア人): — プリュギア人のただ一つの希望、ヘクトル
- [6] 486 nec cessat spes una Phrygum fortissimus Hector
  - Hector (Hector; ヘクトル): fortissimus -or 486. 820
  - Phrygum (Phryges; プリュギア人): spes una -um 486

487 sternere caede uiros atque agmina uertere Graium.
- [2] 487 Sternere caede viros atque agmina vertere Graium.
- [3] 487 Sternere caede uiros atque agmina uertere Graium.
- [4] 487 Sternere caede viros atque agmina vertere Grajum.
  - Grajum (GRAI; ギリシア人): — ヘクトルはギリシア人の隊列を敗走させる
- [6] 487 sternere caede viros atque agmina vertere Graium.
  - Graium (Graius; ギリシアの): agmina -um 305. 487

488 Vt lupus in campis pecudes cum uidit apertis
- [2] 488 Ut lupus in campis pecudes quum vidit apertis,
  - … 群れに襲いかかる狼のこの描写は、とりわけ結びの言葉によって、全体として引き締まり生き生きとした（ἐνεργὴς）ものである。しかし私としては、狼の代わりにライオンを置いてほしかった。狼の力は、ここで描写されているほど恐れを知らず番人を意に介さないものではなく、それはむしろライオンのものであって、ウェルギリウスも Aen. XI, 810 以下で狼を勇敢というよりは狡猾なものとして巧みに描いているからである。バルトの判定（2771 頁）によれば、作者はこの直喩を少なからず気に入り、少し後にライオンの同様の直喩を繰り返した。この点において作者は誤りを犯し、過度に筆を弄したように見えるかもしれないが、それはホメロス自身の模倣からなされたものであろう。ホメロスも近接した二箇所（Iliad. V, 136 および 161）でディオメデスを家畜に襲いかかるライオンになぞらえている。その比喩はホメロス自身と同様、ウェルギリウスにも頻出する（Aen. IX, 339 以下、X, 723 以下を参照）。Ovid. Metam. V, 164 以下の虎の比喩と比較せよ。
- [3] 488 Ut lupus in campis pecudes cum uidit apertis,
- [4] 488 Ut lupus in campis pecudes cum vidit apertis,
- [6] 488 ut lupus in campis pecudes cum vidit apertis
  - **488—490** （証言） *canum* = 『ベレンガリウスの事績』2, 163–5

489 (non actor gregis ipse, comes non horrida terret
- [2] 489 Non ductor gregis ipse comes , non horrida terret
- [3] 489 Non actor gregis ipse comes, non horrida terret
  - **489—91** canum を『ベレンガリウス事績録』II 163–65 が有する
- [4] 489 Non actor gregis ipse comes, non horrida terret
- [6] 489 (non actor gregis ipse, comes non horrida terret
  - … 私は ipse の後に句読点を打った。通常は comes の後に打たれる

490 turba canum), fremit esuriens et neglegit omnes
- [2] 490 Turba canum , premit esuriens et negligit omnes ,
  - … ――なお、Val. Flaccus, VI, 615 にこれと類似の表現がある: « nec caede moratur in una Turbidus, inque omnes pariter furit »。パリ編者。
- [3] 490 Turba canum; fremit esuriens et neglegit omnes
- [4] 490 Turba canum; fremit esuriens et neglegit omnes
- [6] 490 turba canum), fremit esuriens et neglegit omnes

491 in mediosque greges auidus ruit, haut secus Hector
- [2] 491 In mediosque greges avidus ruit; haud secus Hector
- [3] 491 In mediosque greges auidus ruit: haut secus Hector
- [4] 491 In mediosque greges avidus ruit : haut secus Hector
  - Hector (HECTOR; ヘクトル): — まさに狼のようにギリシア人に襲いかかる
- [6] 491 in mediosque greges avidus ruit: haut secus Hector
  - Hector (Hector; ヘクトル): Hector 256. 277. 491. 626. 677. 774. 959. 967. 979. 996. 1051

492 inuadit Danaos et territat ense cruento.
- [2] 492 Invadit Danaos et territat ense cruento.
- [3] 492 Inuadit Danaos et territat ense cruento.
- [4] 492 Invadit Danaos et territat ense cruento.
  - Danaos (GRAI; ギリシア人): — ヘクトルはダナオイに襲いかかる
- [6] 492 invadit Danaos et territat ense cruento.
  - Danaos (Danai; ダナオイ): -os 45. 492. 659. 808. 912. 950. 1001

493 Deficiunt Graiorum acies, Phryges acrius instant
- [2] 493 Deficiunt Graiorum acies, Phryges acrius instant,
- [3] 493 Deficiunt Graiorum acies, Phryges acrius instant
- [4] 493 Deficiunt Grajorum acies, Phryges acrius instant
  - Grajorum (GRAI; ギリシア人): — 彼らの戦列が崩れる
  - Phryges (TROJANI; トロイア人): — より激しく迫る
- [6] 493 deficiunt Graiorum acies, Phryges acrius instant
  - Graiorum (Graius; ギリシアの): -orum acies 493
  - Phryges (Phryges; プリュギア人): Phryges 401. 493. 636. 682. 762. 803

494 attolluntque animos: geminat uictoria uires.
- [2] 494 A.dtoUuntque animos : geminat victoria vires.
  - *Adtolluntque animos*（そして気力を奮い立たせる）は、先行する *Deficiunt*（気落ちする）と同様、ウェルギリウスの Aen. XII, 2, 4 に由来する。――*Geminat victoria vires*（勝利が力を倍加させる）は重みのある表現であり、768 行でも繰り返されている。
- [3] 494 Adtolluntque animos: geminat uictoria uires.
- [4] 494 Attolluntque animos : geminat victoria vires.
- [6] 494 attolluntque animos: geminat victoria vires.

495 Vt uidit socios infesto cedere Marte,
- [2] 495 Ut vidit socios infesto cedere Marti
- [3] 495 Ut uidit socios infesto cedere Marti
- [4] 495 Ut vidit socios infesto cedere Marti
  - Marti (MARS; マルス): Marti:ギリシア人は敵意あるマルスの前に退く
- [6] 495 ut vidit socios infesto cedere marte
  - marte (Mars; マルス): infesto Marte 495

496 rex Danaum sublimis equo uolat agmina circum
- [2] 496 Rex Danaum, sublimis equo volat agmina circum,
- [3] 496 Rex Danaum, sublimis equo uolat agmina circum
- [4] 496 Rex Danaum, sublimis equo volat agmina circum
  - Danaum (AGAMEMNON; アガメムノン): Danaum rex:敵意あるマルスの前に仲間たちが退くのを見る
  - Danaum (GRAI; ギリシア人): — 王(アガメムノン)
- [6] 496 rex Danaum, sublimis equo volat agmina circum
  - rex (Agamemnon; アガメムノン): また rex Danaum 124. 496 を参照
  - Danaum (Danai; ダナオイ): -um(属格):19. 50. 67. 124. 153. 251. 268. 357. 389. 496. 631. 686. 691. 698. 705. 743. 747. 794. 1025

497 hortaturque duces animosque in proelia firmat.
- [2] 497 Hortaturque duces , animosque in praelia iBrmat.
- [3] 497 Hortaturque duces animosque in praelia firmat.
- [4] 497 Hortaturque duces animosque in proelia firmat.
- [6] 497 hortaturque duces animosque in proelia firmat.

498 Mox ipse in medios audax se proripit hostes
- [2] 498 Mox ipse in medios audax se proripit hostes ,
- [3] 498 Mox ipse in medios audax se proripit hostes
- [4] 498 Mox ipse in medios audax se proripit hostes
- [6] 498 mox ipse in medios audax se proripit hostes

499 oppositasque acies stricto diuerberat ense.
- [2] 499 Oppositasque acies stricto diverberat ense.
- [3] 499 Oppositasque acies stricto diuerberat ense.
- [4] 499 Oppositasque acies stricto diverberat ense.
- [6] 499 oppositasque acies stricto diverberat ense.

500 Vt Libycus cum forte leo procul agmina uidit
- [2] 500 Ut Libycus quum forte leo procul agmina vidit
- [3] 500 Ut Libycus cum forte leo procul agmina uidit
  - **500—504** : 『ベレンガリウス事績録』I 207–210 参照
- [4] 500 Ut Libycus cum forte leo procul agmina vidit
  - Libycus (LIBYCUS; リビュアの): ut Libycus leo:リビュアの獅子のように(アガメムノン)
- [6] 500 ut Libycus cum forte leo procul agmina vidit
  - **500—508** （証言） ほぼ = 『ベレンガリウスの事績』1, 208–10 (500 *cernit*, 502 *Attollens*)
  - Libycus (Libycus; リビュアの): Libycus . . . leo 500

501 laeta boum passim uirides errare per herbas,
- [2] 501 Lseta boum passim virides errare per berbas,
- [3] 501 Laeta boum passim uirides errare per herbas,
- [4] 501 Laeta boum passim virides errare per herbas,
- [6] 501 laeta boum passim virides errare per herbas,

502 attollit ceruice iubas sitiensque cruoris
- [2] 502 Adtollit cervice jubas, sitiensque cruoris
  - *Adtollit cervice jubas*（首のたてがみを逆立てる）。Virgil. Aen. X, 726、ライオンについて: « Gaudet hians immane, comasque arrexit »。Lucanus, I, 209: « Erexitque jubam »。同様にオリュンピウス・ネメシアヌスの Laud. Hercul. 93: « Excussis movet arma toris »。
- [3] 502 Adtollit ceruice iubas sitiensque cruoris
- [4] 502 Attollit cervice jubas sitiensque cruoris
- [6] 502 attollit cervice iubas sitiensque cruoris

503 in mediam erecto contendit pectore turbam,
- [2] 503 In mediam erecto contendit pectore turbam :
- [3] 503 In mediam erecto contendit pectore turbam:
- [4] 503 In mediam erecto contendit pectore turbam :
- [6] 503 in mediam erecto contendit pectore turbam:

504 sic ferus Atrides aduersos fertur in hostes
- [2] 504 Sic ferus Atrides adversos fertur in hostes,
- [3] 504 Sic ferus Atrides aduersos fertur in hostes
- [4] 504 Sic ferus Atrides adversos fertur in hostes
  - Atrides (AGAMEMNON; アガメムノン): — 敵に対し猛々しく、リビュアの獅子のように突進する
- [6] 504 sic ferus Atrides adversos fertur in hostes
  - Atrides (Atrides (Agamemno); アトリデス（アガメムノン）): ferus -es 504

505 infestasque Phrygum proturbat cuspide turmas.
- [2] 505 Infestasque Phrygum proturbat cuspide turmas.
- [3] 505 Infestasque Phrygum proturbat cuspide turmas.
- [4] 505 Infestasque Phrygum proturbat cuspide turmas.
  - Phrygum (TROJANI; トロイア人): — アガメムノンがプリュギア人の部隊を押し返す
- [6] 505 infestaque Phrygum proturbat cuspide turmas.
  - Phrygum (Phryges; プリュギア人): -um . . . turmas 505

506 Virtus clara ducis uires accendit Achiuum
- [2] 506 Virtus clara ducis vires accendit Achivum,
- [3] 506 Uirtus clara ducis uires accendit Achiuum,
- [4] 506 Virtus clara ducis vires ascendit Achivum,
  - Achivum (GRAI; ギリシア人): Achivum:アガメムノンの武勇がアカイア人の力を燃え立たせる
- [6] 506 virtus clara ducis vires accendit Achivum
  - Achivum (Achivi; アカイア人): -um 506. 657

507 et spes exacuit languentia militis arma:
- [2] 507 Et spes exacuit languentia militis arma.
  - *Et spes exacuit*（そして希望が研ぎ澄ます）。Virg. Aen. X, 263: « spes addita suscitat iras: Tela manu jaciunt »。
- [3] 507 Et spes exacuit languentia militis arma:
- [4] 507 Et spes exacuit languentia militis arma :
- [6] 507 et spes exacuit languentia militis arma:

508 funduntur Teucri, Danai laetantur ouantes.
- [2] 508 Funduntur Teucri , Danai laetantur ovantes.
- [3] 508 Funduntur Teucri, Danai laetantur ouantes.
- [4] 508 Funduntur Teucri, Danai laetantur ovantes.
  - Danai (GRAI; ギリシア人): Danai:喜ぶ
  - Teucri (TROJANI; トロイア人): Teucri:敗走させられる
- [6] 508 funduntur Teucri, Danai laetantur ovantes.
  - Danai (Danai; ダナオイ): Danai 508. 542. 646. 679. 766. 802. 838. 960. 978. 1002
  - Teucri (Teucri; テウクロイ): Teucri 508

509 Tandem hic Aenean immisso tendere curru
- [2] 509 Tandem hic ,neam immisso contendere curru
  - … Virg. Aeneid. XI, 889: « immissis pars caeca et concita frenis Arietat in portas »。Ovid. Met. I, 280: « Fluminibus vestris totas immittite habenas »。
- [3] 509 Tandem hic Aenean inmisso tendere curru
- [4] 509 Tandem hic Aenean immisso tendere curru
  - Aenean (AENEAS; アイネイアス): — アガメムノンは戦車で進むアイネイアスを見つける
- [6] 509 tandem hic Aenean immisso tendere curru
  - Aenean (Aeneas; アイネイアス): -ān 509

510 conspicit Atrides: stricto concurrere ferro
- [2] 510 Conspicit Atrides, strictoque occurrere ferro
- [3] 510 Conspicit Atrides strictoque occurrere ferro
- [4] 510 Conspicit Atrides strictoque occurrere ferro
  - Atrides (AGAMEMNON; アガメムノン): — 戦車で進むアイネイアスを見つける
- [6] 510 conspicit Atrides: stricto concurrere ferro
  - Atrides (Atrides (Agamemno); アトリデス（アガメムノン）): -es 24. 510(?) 663
  - Atrides (Atrides (Menelaus); アトリデス（メネラオス）): -des 290. 301. 332. 349. (510?)

511 comparat et iaculum, quantum furor ipse mouebat,
- [2] 511 Apparat , et jaculum , quantum furor ipse movebat ,
- [3] 511 Conparat et iaculum, quantas furor ipse mouebat,
- [4] 511 Comparat et jaculum, quantas furor ipse movebat,
- [6] 511 comparat et iaculum, quantas furor ipse movebat,

512 uiribus intorquet, quod detulit error ab illo
- [2] 512 Viribus intorquet, quod depulit error ab illo
  - *Depulit error*（手元が狂って逸らした）。Ovid. Metam. XII, 83: « quamquam certa nullus fuit error in hasta »。
- [3] 512 Uiribus intorquet, quod detulit error ab illo
- [4] 512 Viribus intorquet, quod detulit error ab illo
- [6] 512 viribus intorquet, quod detulit error ab illo
  - detulit シュラーダー(オウィディウス『変身物語』5, 90 より) …

513 pectus in aurigae stomachoque infigitur alto;
- [2] 513 Pectus in aurigse, stomachoque infigitur alto.
  - *Stomachoque infigitur*（そして胃に突き刺さる）。Virgil. Aen. IX, 698: « volat Itala cornus Aera per tenerum, stomachoque infixa sub altum Pectus abit »。
- [3] 513 Pectus in aurigae stomachoque infigitur alto:
- [4] 513 Pectus in aurigae stomachoque infigitur alto :
- [6] 513 pectus in aurigae stomachoque infigitur alto:
  - alto … だがウェルギリウス『アエネーイス』9, 699 を参照
  - — (Aeneae auriga; アイネイアスの御者): アイネイアスの御者、名は挙げられない 513

514 ille ruens ictu media inter lora rotasque
- [2] 514 Ille ruens ictu medla inter lora rotasque
  - *Media inter lora*（手綱のただ中に）。Virg. Aen. XII, 468: « Aurigam Turni media inter lora Metiscum Excutit »。
- [3] 514 Ille ruens ictu media inter lora rotasque
- [4] 514 Ille ruens ictu media inter lora rotasque
- [6] 514 ille ruens ictu media inter lora rotasque

515 uoluitur et uitam calido cum sanguine fundit.
- [2] 515 Yolvitur, et vitam calido cum sanguine fundit.
- [3] 515 Uoluitur et uitam calido cum sanguine fundit.
- [4] 515 Volvitur et vitam calido cum sanguine fundit.
- [6] 515 voluitur et vitam calido cum sanguine fundit.

516 Ingemit Aeneas curruque animosus ab alto
- [2] 516 Ingemit Aeneas, curruque animosus ab alto
- [3] 516 Ingemit Aeneas curruque animosus ab alto
- [4] 516 Ingemit Aeneas curruque animosus ab alto
  - Aeneas (AENEAS; アイネイアス): — 御者がアガメムノンに殺されると、呻き、勇んで戦車から飛び降りる
- [6] 516 ingemit Aeneas curruque animosus ab alto
  - Aeneas (Aeneas; アイネイアス): -as 454. 516

517 desilit et ualido Crethona<que> comminus ictu
- [2] 517 Desilit, et valido Crethonem cominus ictu
  - … Hom. Il. V, 542 から *Crethona* と読まれるべきであるが、韻律の都合がこれを拒むため、私はラテン語の格語尾 *Crethonem* を復元した。
- [3] 517 Desilit et ualido Crethonaque cominus ictu
- [4] 517 Desilit et valido Crethonaque cominus ictu
  - Crethona …（『イリアス』V, 541 以下）。
  - Crethona (CRETHON; クレトン): Crethona:アイネイアスが彼を殺す
- [6] 517 desilit et valido Crethona\<que> comminus ictu
  - Crethona (Crethon; クレトン): Crethona 517:ディオクレスの子、ペライの人

518 Orsilochumque ferit, quorum post funera uictus
- [2] 518 Orsilochumque ferit : quorum post fiinera victus
  - ホメロスの前掲箇所は *Orsilochum* を要求している。…
- [3] 518 Orsilochumque ferit, quorum post funera uictus
- [4] 518 Orsilochumque ferit, quorum post funera victus
  - **518, 520** Orsilochum, Antilochique Mydon …（『イリアス』同所および 580）。
  - Orsilochum (ORSILOCHUS; オルシロコス): Orsilochum:アイネイアスがオルシロコスを斬り殺す
- [6] 518 Orsilochumque ferit, quorum post funera victor
  - … アエネーアースはメネラーオスとアンティロコスを避けた (E 571 以下)
  - Orsilochum (Orsilochus; オルシロコス): *Orsilochum 518:ディオクレスの子、ペライの人

519 Paphlagonum ductor Menelai concidit armis,
- [2] 519 Paphlagonum ductor Menelai concidit armis,
- [3] 519 Paphlagonum ductor Menelai concidit armis,
- [4] 519 Paphlagonum ductor Menelai concidit armis,
  - Menelai (MENELAUS; メネラオス): — ピュライメネスがメネラオスの武器に倒れる
  - Paphlagonum (PYLAEMEN; ピュライメネス): Paphlagonum ductor:パフラゴニア人の指揮者がメネラオスに殺される
- [6] 519 Paphlagonum ductor Menelai concidit armis,
  - Menelai (Menelaus; メネラオス): -lai 519. 639
  - Paphlagonum (Paphlagones; パフラゴニア人): Paphlagonum ductor 519:ピュライメネス

520 Antilochique Mydon. Post hos Iouis inclita proles
- [2] 520 Antilochique Mydon : post hos Jovis inclyta proles
  - *Antilochique Mydon*。ホメロスに基づいてこのように読まれるべきであることをボンダムが示した。…
- [3] 520 Antilochique Mydon; post hos Iouis inclita proles
- [4] 520 Antilochique Mydon ; post hos Jovis inclita proles
  - Antilochi (ANTILOCHUS; アンティロコス): — ミュドンが彼の武器に倒れる
  - Jovis (JUPPITER; ユピテル): — 子(サルペドン)
  - Mydon (MYDON; ミュドン): アンティロコスの武器に倒れる
  - Sarpedon (SARPEDON; サルペドン): — ユピテルの名高き子が戦う
- [6] 520 Antilochique Mydon; post hos Iovis inclita proles
  - Antilochi (Antilochus; アンティロコス): armis . . . -i 520:ネストルの子
  - Iovis (Iuppiter; ユピテル): Iovis inclita proles Sarpedon 248. 520
  - Mydon (Mydon; ミュドン): *Mydon 520:ピュライメネスの御者、アテュムニオスの子

521 Sarpedon bellum funestaque proelia miscet.
- [2] 521 Sarpedon sequitur, funestaque praelia miscet.
- [3] 521 Sarpedon subiit funestaque praelia miscet.
- [4] 521 Sarpedon subiit funestaque proelia miscet.
- [6] 521 Sarpedon bellum funestaque proelia miscet.
  - Sarpedon (Sarpedon; サルペドン): Iovis inclita proles Sarpedon 249. 521

522 Quem contra infelix non aequis dimicat armis
- [2] 522 Quem contra infehx non aequis dimicat arrais
- [3] 522 Quem contra infelix non aequis dimicat armis
- [4] 522 Quem contra infelix non aequis dimicat armis
- [6] 522 quem contra infelix non aequis dimicat armis

523 Tlepolemus magno satus Hercule, sed neque uires
- [2] 523 Tlepolemus, magno satus Hercule; sed neque vires
  - Hom. Il. V, 628 から *Tlepolemus*（トレポレモス）と読むべきであることは明らかであり、…
- [3] 523 Tlepolemus magno satus Hercule, sed neque uires
- [4] 523 Tlepolemus magno satus Hercule, sed neque vires
  - Tlepolemus …（『イリアス』V, 628）。
  - Hercule (HERCULES; ヘラクレス): Hercule magno:偉大なヘラクレスの子トレポレモス
  - Tlepolemus (TLEPOLEMUS; トレポレモス): — 偉大なヘラクレスの子、サルペドンに殺される
- [6] 523 Tlepolomus magno satus Hercule, sed neque vires
  - Hercule (Hercules; ヘラクレス): Tlepolomus magno satus Hercule 523
  - Tlepolomus (Tlepolomus; トレポレモス): *-us magno satus Hercule 523

524 hunc seruare patris nec tot potuere labores,
- [2] 524 Hunc servare patris, nec tot potuere labores,
- [3] 524 Hunc seruare patris nec tot potuere labores,
- [4] 524 Hunc servare patris nec tot potuere labores,
- [6] 524 hunc servare patris nec tot potuere labores,
  - labores (Hercules; ヘラクレス): patris . . . labores 524 を参照

525 quin caderet tenuemque daret de corpore uitam.
- [2] 525 Quin caderet, tenuemque daret de corpore vitam.
  - *Tenuemque daret de corpore vitam*（肉体から微かな命を差し出した）、すなわち息を引き取ったということ。彼が *tenuem vitam*（微かな命）と呼ぶのは、ウェルギリウスが Georg. IV, 223 で讃えている人々、すなわち生き物の個々の魂は世界霊魂（anima mundi）の微粒子であり、死を通じてそこへと還っていくと説いた人々の考えに即している。ウェルギリウスは前掲箇所で「ここから、生まれるときに各人が自分自身のためにかす-
  - **(cont.)** （前頁からの続き）-かな命を引き寄せる［« Quemque sibi tenues nascentem arcessere vitas »］」と述べている。また Aen. IV, 705: « omnis et una Dilapsus calor, atque in ventos vita recessit »（熱気はことごとく去り、命は風の中へと退いた）。
- [3] 525 Quin caderet tenuemque daret de corpore uitam.
- [4] 525 Quin caderet tenuemque daret de corpore vitam.
- [6] 525 quin caderet tenuemque daret de corpore vitam.

526 Saucius egreditur medio certamine belli
- [2] 526 Saucius egreditur medio certamine belli
- [3] 526 Saucius, egreditur medio certamine belli
- [4] 526 Saucius egreditur medio certamine belli
- [6] 526 saucius egreditur medio certamine belli

527 Sarpedon fraudisque subit commentor Vlixes
- [2] 527 Sarpedon, fraudisque subit cotnmentor Ulysses,
  - ウリクセスは *fraudis commentor*（詐術の考案者）と呼ばれているが、それはあたかもこれが彼の特技であるかのようであり、ホメロスや他の古代人によって常に彼に帰せられている性質である、とバルトは Adv. LIX, 15 で述べている。Virgil. Aen. II, 164: « scelerumque inventor Ulysses »（悪謀の考案者ウリクセス）。われらの詩人も下の 579 行で同じ表現を繰り返している。同様にオウィディウスも彼について Met. XIII, 31 で « quid sanguine cretus Sisyphio, furtisque et fraude simillimus illi » と述べており、すぐ後の 38 行でもその偽り言（*commenta*）を指摘している。ここからまた、ファン・デル・デュッセンがわれらの詩人の 65 行への注で指摘しているように、ドーシアダースの第二の『祭壇』においてウリクセスは φὼρ（盗人）と呼ばれており、サルマシウス（Salmasius）が注釈 156 頁で詳述している通りである。
- [3] 527 Sarpedon, fraudisque subit commentor Ulixes
- [4] 527 Sarpedon, fraudisque subit commentor Ulixes
  - Sarpedon (SARPEDON; サルペドン): — 傷を負って戦いから退く
  - Ulixes (ULIXES; ウリクセス): — 欺瞞の考案者、七人のトロイアの若者を殺す
- [6] 527 Sarpedon, fraudisque subit commentor Vlixes
  - Sarpedon (Sarpedon; サルペドン): -don 527
  - Vlixes (Vlixes; ウリクセス): fraudis . . . commentor -es 527. 579

528 et septem iuuenum fortissima corpora fundit.
- [2] 528 'Et septem juvenum pulcherrima corpora fundit.
  - *Et septem juvenum*（そして七人の若者の）。ホメロスが Il. V, 677 で列挙しているリュキア人たち、すなわちコイラノス、アラストル、クロミオス、アルカンドロス、ハリオス、ノエモン、プリュタニスのことである。
- [3] 528 Et septem iuuenum pulcherrima corpora fundit.
- [4] 528 Et septem juvenum fortissima corpora fundit.
- [6] 528 et septem iuvenum pulcherrima corpora fundit.

529 Hinc pugnat patriae columen Mauortius Hector,
- [2] 529 Hinc pugnat patriae culmen, Mavortius Hector,
  - ヴォルフェンビュッテル第2写本（G. 2）は語順を異にして *Hinc patriae culmen pugnat* とする。ファン・デル・デュッセンは 29 頁で *columen*（大黒柱／支柱）と読む方を好んでおり、それは実にヘクトルに極めて適しており、上にわれらの詩人が 486 行で彼に与えたもう一つの賛辞 *spes una Phrygum*（プリュギア人の唯一の希望）にも最もよく合致している。同様にセネカの Troad. 126 行で、ヘクトルについて次のようにある: « Columen patriae, mora fatorum, Tu praesidium Phrygibus fessis, Tu murus eras »。――« Graium murus Achilles »（ギリシア人の防壁アキレウス）、Ovid. Met. XIII, 281。スカーエワについて Lucan. VI, 201: « stat non fragilis pro Caesare murus, Pompeiumque tenet »。なおセネカが前掲箇所で付け加えている « Tecum cecidit, summusque dies Hectoris idem patriaeque fuit » を、われらの詩人は下の 1061 行で模倣したように思われる。本著作第2巻329頁のペンタディウスの「ヘクトルの墓碑銘」に対するわれわれの注を参照。パリ編者。――とはいえ、本文自体の語を変更したいとは思わない。なぜなら *culmen*（頂／頂点）もヘクトルに不適切ではなく、少なくとも彼の最高の尊厳を示しているからである。まさしく同様にコルネリウス・セウェルスはキケローを « Egregium semper patriae caput »（常に祖国の卓越した首領）と呼んでいる（本巻の上の211頁）。
- [3] 529 Hinc pugnat patriae columen Mauortius Hector,
- [4] 529 Hinc pugnat patriae columen Mavortius Hector,
  - Hector (HECTOR; ヘクトル): — 祖国の柱、マウォルスのヘクトルが戦う
- [6] 529 hinc pugnat patriae columen Mavortius Hector,
  - Hector (Hector; ヘクトル): patriae columen Mavortius -or 529

530 illinc Tydides: sternuntur utrimque uirorum
- [2] 530 lUinc Tydides : stemuntur utrimque virorum
- [3] 530 Illinc Tydides: sternuntur utrimque uirorum
- [4] 530 Illinc Tydides : sternuntur utrimque virorum
  - Tydides (DIOMEDES; ディオメデス): — 戦う
- [6] 530 illinc Tydides: sternuntur utrimque virorum
  - Tydides (Tydides; テュディデス): Tydides 390. 408. 530. 665. 1008

531 corpora per campos et sanguine prata rigantur.
- [2] 531 Corpora per campos, et sanguine prata rigantur.
- [3] 531 Corpora per campos et sanguine prata rigantur.
- [4] 531 Corpora per campos et sanguine prata rigantur.
- [6] 531 corpora per campos et sanguine prata rigantur;

532 Pugnat bellipotens casta cum Pallade Mauors
- [2] 532 Pugnat bellipotens casta cum Pallade Mavors ,
- [3] 532 Pugnat bellipotens casta cum Pallade Mauors
- [4] 532 Pugnat bellipotens casta cum Pallade Mavors
  - Mavors (MARS; マルス): — 戦の力を持つ者、パラスと戦う
  - Pallade (MINERVA; ミネルウァ): Cum Pallade:マルスは貞潔なパラスと戦う
- [6] 532 pugnat bellipotens casta cum Pallade Mavors
  - bellipotens (bellipotens; 戦の力を持つ者): bellipotens . . . Mavors 532
  - Mavors (Mavors; マウォルス): bellipotens . . . Mavors 532
  - Pallade (Pallas; パラス): casta cum -de 532. 894

533 ingentemque mouet clipeum, quem sancta uirago
- [2] 533 Ingentemque movet clypeum, quem sancta virago
  - … *Virago*（女傑／男勝りの乙女）はパラスに関して頻出する語であり、ほぼ彼女固有の呼称である。オウィディウスは Met. VI, 130 で *flava virago*（金髪の女傑）と呼び、バルトの判断（前掲書 2806 頁）によれば、*sancta virago*（聖なる女傑）は純潔であると同時にマルス的、すなわち好戦的であることを示唆している。
- [3] 533 Ingentemque mouet clipeum, quem sancta uirago
- [4] [533] Ingentemque movet clipeum; quem sancta virago
  - virago (MINERVA; ミネルウァ): sancta virago:聖なる女戦士がマルスを傷つける
- [6] 533 ingentemque movet clipeum; quem sancta virago
  - virago (virago; 戦乙女): sancta virago 533:ミネルウァ

534 egit et extrema percussum cuspide caedit
- [2] 534 Aegide et extrema percussum cuspide caedit,
  - **(cont.)** … そしてこの出来事を語るホメーロス（Iliad. V, 841）はアイギスについて全く言及していないものの、ホメーロスに忠実に従うことは稀でラテン詩人たちに追随することの多いわれらの詩人は、おそらくこの箇所でホラーティウスを念頭に置いていたのであろう。ホラーティウスは Carm. I, 15, 11 で、パッラスがまさにこの戦いでアイギスを用いたと述べている: « Jam galeam Pallas et aegida Currusque et rabiem parat »。――またオウィディウスも Met. V, 47 で次のように述べている: « Bellica Pallas adest, et protegit aegide fratrem »。パリ編者。
- [3] 534 Egit et extrema percussum cuspide caedit
- [4] 534 Egit et extrema percussum cuspide caedit,
- [6] 534 egit et extrema percussum cuspide caedit

535 attonitumque simul caelum petere ipsa coegit.
- [2] 535 Attonitumque simul caelum petere ipsa coegit.
- [3] 535 Attonitumque simul caelum petere inde coegit;
- [4] 535 Attonitumque simul caelum petere ipsa coegit;
- [6] 535 attonitumque simul caelum petere ipsa coegit;

536 Hic ille aetherio queritur sua uulnera regi
- [2] 536 Hic ille aethereo queritur sua vulnera regi
  - … 詩人は同様の事柄について上で用いた 471 行を繰り返している。
- [3] 536 Hic ille aethereo queritur sua uulnera regi
- [4] 536 Hic ille aethereo queritur sua vulnera regi
- [6] 536 hic ille aethereo queritur sua vulnera regi
  - regi (Iuppiter; ユピテル): aethereo . . . regi 536

537 saucius et magni genitoris iurgia suffert.
- [2] 537 Saucius , et magni genitoris jurgia suffert.
  - *Jurg. suffert*（叱責を甘受する）。61 行および 104 行を参照。
- [3] 537 Saucius et magni genitoris iurgia suffert.
- [4] 537 Saucius et magni genitoris jurgia suffert.
- [6] 537 saucius et magni genitoris iurgia suffert.
  - genitoris (Iuppiter; ユピテル): magni genitoris 537

## Book 6

538 Interea magnis Acamantem uiribus Aiax
- [2] 538 VI. Interea magnis Acamantem viribus Ajax
  - ボンダムおよびファン・デル・デュッセンは前掲箇所で、ホメロスの VI, 8 に基づいて *Acamantem*（アカマスを）と読んでいる。…
- [3] 538 Interea magnis Acamantem uiribus Aiax
- [4] 538 Interea magnis Acamantem viribus Ajax
  - Acamantem (ACAMAS dux Thracum; アカマス、トラキア人の将): Acamantem:テラモンの子アイアスが彼を殺す
  - Ajax (AJAX Telamonis filius; アイアス、テラモンの子): — トラキア人の将アカマスを殺す
- [6] 538 interea magnis Acamantem viribus Aiax
  - Acamantem (Acamas 2; アカマス 2): -antem . . . テラモンの子アイアスが彼を殺す 538
  - Aiax (Aiax (Telamonius); アイアス（テラモンの子）): -ax 538. 799. 1009

539 interimit uastumque capit Menelaus Adrastum
- [2] 539 Interimit, vastumque capit Menelaus Adrastum,
  - … ホメロス（Iliad. VI, 37 以下）の記述のゆえである。ホメロスは、アドラストスが恐怖で取り乱した馬から投げ出され、近くに立っていたメネラオスに生け捕りにされて命乞いをし、はじめはそれを許されたものの、駆けつけてメネラオスを叱責したアガメムノンによって重傷を負わされたと伝えているからである。…この読みから、作者がここでアドラストスの哀れな命乞いを考慮したのではなく、ただ彼の転落と捕縛を表現しようとしたにすぎないことが理解されるであろう。…
- [3] 539 Interimit, uastumque capit Menelaus Adrastum
- [4] 539 Interimit, vastumque capit Menelaus Adrastum
  - Adrastum (ADRASTUS; アドラストス): Adrastum:メネラオスが巨大なアドラストスを捕らえる
  - Menelaus (MENELAUS; メネラオス): — アドラストスを捕らえる
- [6] 539 interimit, vastumque capit Menelaus Adrastum
  - Adrastum (Adrastus; アドラストス): vastumque capit Menelaus -um 539
  - Menelaus (Menelaus; メネラオス): Menelaus 283. 312. 339. 539

540 et rapit ad classes manibus post terga reuinctis,
- [2] 540 Et rapit ad classes manibus post terga revinctis,
- [3] 540 Et rapit ad classes manibus post terga reuinctis,
- [4] 540 Et rapit ad classes manibus post terga revinctis,
- [6] 540 et rapit ad classes manibus post terga revinctis,
  - （証言） *manibus — revinctis* = 『ベレンガリウスの事績』3, 115

541 ut ui deducat laetos ex hoste triumphos.
- [2] 541 Ut vivo ducat laetos ex hoste triumphos.
  - … なお作者はここで、過度の簡潔さによってホメロスの叙述を切り縮めてしまった。なぜなら、アドラストスが捕らえられ船へと連行されるよう命じられたことだけを語り、最も重大な点、すなわちメネラオスの寛容さを非難したアガメムノンによってアドラストスが殺害されたことを沈黙してしまったからである。
- [3] 541 Ut uiuo ducat laetos ex hoste triumphos.
- [4] 541 Ut vivo ducat laetos ex hoste triumphos.
- [6] 541 ut vivo ducat laetos ex hoste triumphos.

542 Incumbunt Danai, cedit Troiana iuuentus
- [2] 542 Incumbunt Danai, cedit Trojana juventus,
- [3] 542 Incumbunt Danai, cedit Troiana iuuentus
- [4] 542 Incumbunt Danai, cedit Trojana juventus
  - Danai (GRAI; ギリシア人): — 押し寄せる
  - Trojana (TROJANI; トロイア人): Trojana juventus:トロイアの若者たちが退く
- [6] 542 incumbunt Danai, cedit Troiana iuventus
  - Danai (Danai; ダナオイ): Danai 508. 542. 646. 679. 766. 802. 838. 960. 978. 1002
  - Troiana (Troianus; トロイアの): Troiana iuventus 542. 770

543 tergaque nuda tegit. Sensit Mauortius Hector
- [2] 543 Tergaque nuda tegit : seusit Mavortius Hector
  - *Tergaque nuda tegit*（そして無防備な背を覆う）。盾によってであろう、彼らがみすみす討ち取られぬように。Virg. Aen. XI, 630: « Bis rejecti armis respectant terga tegentes »（二度退けられ、武器で背を覆いつつ後方を振り返る）。
- [3] 543 Tergaque nuda tegit; sensit Mauortius Hector,
- [4] 543 Tergaque nuda tegit; sensit Mavortius Hector,
  - Hector (HECTOR; ヘクトル): — マウォルスのヘクトルは、神々がギリシア人のために戦っていることを悟る
- [6] 543 tergaque nuda tegit; sensit Mavortius Hector
  - Hector (Hector; ヘクトル): Mavortius -or 543. 797
  - Mavortius (Mavortius; マウォルスの): Mavortius Hector 543. 797

544 pro Danais pugnare deos ualidasque suorum
- [2] 544 Pro Danais pugnare Deos, validasque suorum
- [3] 544 Pro Danais pugnare deos ualidasque suorum
- [4] 544 Pro Danais pugnare deos validasque suorum
  - Danais (GRAI; ギリシア人): Pro Danais:ヘクトルは神々がダナオイのために戦っていることを悟る
- [6] 544 pro Danais pugnare deos validasque suorum
  - Danais (Danai; ダナオイ): pro -is 544

545 uirginis armigerae subduci numine uires
- [2] — Virginis armigerae subduci numine vires.
- [3] 545 Uirginis armigerae subduci numine uires,
- [4] 545 Virginis armigerae subduci numine vires,
  - Virginis (MINERVA; ミネルウァ): 神威
- [6] 545 virginis armigerae subduci numine vires,
  - armigerae (armigera; 武装した): virginis armigerae 400. 545:ミネルウァの

546 continuoque petit muros Hecubamque uocari
- [2] 546 Continuoque petit muros , Hecubamque vocari
- [3] 546 Continuoque petit muros Hecubamque uocari
- [4] 546 Continuoque petit muros Hecubamque vocari
  - Hecubam (HECUBA; ヘカベ): Hecubam:ヘクトルはヘカベを呼ぶよう命じる
- [6] 546 continuoque petit muros Hecabenque vocari
  - Hecaben (Hecabe; ヘカベ): Hecubam 546

547 imperat et diuae placari numina suadet.
- [2] 547 Imperat , et Divae placari numina suadet.
- [3] 547 Imperat et diuae placari numina suadet.
- [4] 547 Imperat et divae placari numina suadet.
- [6] 547 imperat et divae placari numina suadet.
  - divae (Diva; 女神): divae 547:ミネルウァ

548 Protinus armatas innuptae Palladis arces
- [2] 548 Protinus armatas innuptse Palladis arces
  - … ――*Innuptae Minervae*（純潔のミネルウァの）は Virgil. Aen. II, 31。
- [3] 548 Protinus elatas innuptae Palladis arces
- [4] 548 Protinus auratas innuptae Palladis arces
  - Palladis (MINERVA; ミネルウァ): トロイアの女たちは未婚のパラスの神殿へ上って行く
- [6] 548 protinus † armatas innuptae Pallados arces
  - Pallados (Pallas; パラス): innuptae -dos arces 548(両箇所とも -dis trad.)

549 Iliades subeunt: festis altaria sertis
- [2] 549 Iliades subeunt, festisque altaria sertis
  - *Altaria sertis*（祭壇を花輪で）。言うまでもなく神々を宥めるためである、とバルトは前掲の箇所で述べている。古代人は犠牲獣を用いるだけでなく、祭壇を、そして付け加えるなら神殿を取り巻くために花冠をも用いた。Virg. Aen. II, 249: « Nos delubra Deum ... festa velamus fronde per urbem »；同 IV, 202: « variis florentia limina sertis »；同 Georg. IV, 276: « Saepe Deum nexis ornatae torquibus arae »。
- [3] 549 Iliades subeunt: festis altaria sertis
- [4] 549 Iliades subeunt : festis altaria sertis
  - Iliades (ILIADES; イリアデス): ミネルウァの神殿へ上って行く
- [6] 549 Iliades subeunt: festis altaria sertis
  - Iliades (Iliades; イリアデス): Iliades 549

550 exornant caeduntque sacras ex more bidentes.
- [2] 550 Exornant, caeduotque sacras de more bidentes.
- [3] 550 Exornant caeduntque sacras ex more bidentes.
- [4] 550 Exornant caeduntque sacras de more bidentes.
- [6] 550 exornant caeduntque sacras ex more bidentes.

551 Dumque preces Hecube supplex ad templa Mineruae
- [2] 551 Duroque preces Hecube supplex ad templa Minervae
- [3] 551 Dumque preces Hecube supplex ad templa Mineruae
- [4] 551 Dumque preces Hecube supplex ad templa Minervae
  - Hecube (HECUBA; ヘカベ): Hecube:嘆願者としてミネルウァの神殿へ
  - Minervae (MINERVA; ミネルウァ): Minervae:ヘカベは嘆願者としてミネルウァの神殿に来る
- [6] 551 dumque preces Hecabe supplex ad templa Minervae
  - Hecabe (Hecabe; ヘカベ): Hecabē (-cuba trad.) . . . genetrix 551
  - Minervae (Minerva; ミネルウァ): ad templa Minervae 551

552 pro caris genetrix natis et coniuge fundit,
- [2] 552 Pro charis genitrix natis et conjuge fundit,
- [3] 552 Pro caris genetrix natis et coniuge fundit,
- [4] 552 Pro caris genetrix natis et conjuge fundit,
- [6] 552 pro caris genetrix natis et coniuge fundit,
  - coniuge (Priamus; プリアモス): coniuge 552 を参照

553 interea Glaucus stricto decernere ferro
- [2] 553 Interea Glaucus stricto contendere ferro
- [3] 553 Interea Glaucus stricto decernere ferro
- [4] 553 Interea Glaucus stricto decernere ferro
  - Glaucus (GLAUCUS Lyciorum dux; グラウコス、リュキア人の将): — ディオメデスと戦おうとする
- [6] 553 interea Glaucus stricto decernere ferro
  - Glaucus (Glaucus; グラウコス): -us 553:トロイア側のリュキア人の将

554 cum Diomede parat nomenque genusque roganti
- [2] 554 Cum Diomede parat, nomenque genusque roganti,
- [3] 554 Cum Diomede parat nomenque genusque roganti,
- [4] 554 Cum Diomede parat nomenque genusque roganti,
  - Diomede (DIOMEDES; ディオメデス): Cum Diomede:ディオメデスと戦おうとするグラウコス
- [6] 554 cum Diomede parat nomenque genusque roganti
  - Diomede (Diomedes; ディオメデス): cum -dĕ 554

555 qui sit et unde ferat, magnis cum uiribus hastam
- [2] 555 Quis sit, et unde ferat, magnis cum viribus hastam
  - *Et unde ferat*（そしてどこから携えてきたのか）、すなわち武器を。…
- [3] 555 Qui sit et unde, ferus magnis cum uiribus hastam
- [4] 555 Quis sit et unde satus, magnis cum viribus hastam
- [6] 555 qui sit et unde ferat, magnis cum viribus hastam

556 mittere temptabat; temptanti Aetolius heros:
- [2] 556 Mittere tentabat ; tentanti Aetolius heros,
- [3] 556 Mittere temptabat, temptanti Aetolius heros
- [4] 556 Mittere temptabat, temptanti Aetolius heros
  - Aetolius (DIOMEDES; ディオメデス): Aetolius heros:グラウコスに呼びかける
- [6] 556 mittere temptabat; temptanti Aetolius heros
  - Aetolius (Aetolius; アイトリアの): Aetolius heros 556. 698:ディオメデス

557 "Quo ruis?" - exclamat - "quae te, scelerate, furentem
- [2] 557 cc Quo ruis! exclamat; quae te, scelerate, furentem
  - *Te, scelerate*（汝、悪漢よ）: これはホメロスの Iliad. VI, 123 以下のディオメデスの穏やかな弁舌に比して確かに厳しすぎる。…――しかしバルトは Adv. XXV, 15 で、*sceleratus* はしばしば「厄介な、過酷な（molestus）」や「不敬な」の意で用いられると注意を促している。実際ウェルギリウスも « sceleratum frigus »（酷い寒さ）と言い、ルティリウスも « Obruerint citius scelerata oblivia solem »（忌まわしき忘却のほうが早く太陽を覆い尽くそう）と述べている。パリ編者。
- [3] 557 'Quo ruis?' exclamat, 'quae te, scelerate, furentem
- [4] 557 « Quo ruis? » exclamat « quae te, scelerate, furentem
- [6] 557 'quo ruis?' exclamat 'quae te, scelerate, furentem

558 mens agit imparibus mecum concurrere telis?
- [2] 558 Mens agit imparibus mecum concurrere telis?
- [3] 558 Mens agit inparibus mecum concurrere telis?
- [4] 558 Mens agit imparibus mecum concurrere telis?
- [6] 558 mens agit inparibus mecum concurrere telis?

559 Hospitis arma uides, Veneris qui uulnere dextram
- [2] 559 Hospitis arma vides, Veneris qui vulnere dextram
  - *Veneris quae vulnere dex-*
  - **(cont.)** （前頁からの続き）-*tram* をすべての本が与えている。バルトは Adv. p. 2807 で、*dextram*（右手）という語を次のように反復して解すべきであると説いている: *Vides dextram, quae Veneris dextram vulneravit*（汝は見ている、ウェヌスの右手を傷つけた右手を）。そして、ある語が同じ格配置で二つの事柄に適合し得るとき、それを一度だけ置き、しかも両方の箇所に適用されねばならないようにする、詩人たちに慣用の修辞法であるとする。…
- [3] 559 Hospitis arma uides, Ueneris qui uulnere dextram
- [4] 559 Hospitis arma vides, Veneris qui vulnere dextram
  - Veneris (VENUS; ウェヌス): — ディオメデスがウェヌスの右手を傷つける
- [6] 559 hospitis arma vides, Veneris qui vulnere dextram
  - qui (Diomedes; ディオメデス): 584 行:qui . . . manum Veneris violavit(559 を参照)
  - Veneris (Venus; ウェヌス): -eris 559. 584

560 perculit et summo pupugit certamine Martem.
- [2] 560 Perculit, et summo repulit certamine Martem.
  - … ――しかしこの語は、同様の複合語 *repulit*, *recidit* と同じく、優れた詩人たちにおいては第一音節を長くして用いられるのが通例である。…
- [3] 560 Perculit et summo pupugit certamine Martem.
- [4] 560 Perculit et summo pupugit certamine Martem.
  - Martem (MARS; マルス): — ディオメデスはマルスを突いた
- [6] 560 perculit et summo pupugit certamine Martem.
  - Martem (Mars; マルス): Diomedes pupugit . . . Martem 560

561 Pone truces animos infestaque tela coerce."
- [2] 561 Pone truces animos, infestaque tela coerce».
- [3] 561 Pone truces animos infestaque tela coerce'.
- [4] 561 Pone truces animos infestaque tela coerce ».
- [6] 561 pone truces animos infestaque tela coerce'.

562 Post haec inter se posito certamine pugnae
- [2] 562 Post hsec inter se posito certamine pugnae
- [3] 562 Post haec inter se posito certamine pugnae
- [4] 562 Post haec inter se posito certamine pugnae
- [6] 562 post haec inter se posito certamine pugnae

563 commutant clipeos inimicaque proelia linquunt.
- [2] 563 Commutant clypeos, inimicaque praelia linquunt.
- [3] 563 Commutant clipeos inimicaque praelia lincunt.
- [4] 563 Commutant clipeos inimicaque proelia lincunt.
- [6] 563 commutant clipeos inimicaque proelia linquunt.

## Book 7

564 Colloquium petit interea fidissima coniunx
- [2] 564 Colloquium petit interea fidissima conjux.
- [3] 564 Colloquium petit interea fidissima coniunx
- [4] 564 Colloquium petit interea fidissima conjunx
  - Andromache (ANDROMACHE; アンドロマケ): ヘクトルのいと忠実な妻、彼と語り合うことを求める
- [6] 564 colloquium petit interea fidissima coniunx

565 Hectoris Andromache paruumque ad pectora natum
- [2] 565 Hectoris Andromache, parvumque ad pectora natum
  - *Ad pectora natum tenet*（子を胸に抱き寄せる）。Virg. Aen. VII, 318: « Et trepidae matres pressere ad pectora natos »。
- [3] 565 Hectoris Andromache paruumque ad pectora natum
- [4] 565 Hectoris Andromache parvumque ad pectora natum
  - Astyanacta (ASTYANAX; アステュアナクス): Astyanacta:アンドロマケが幼いアステュアナクスを抱く
  - Hectoris (HECTOR; ヘクトル): — その妻アンドロマケ
- [6] 565 Hectoris Andromache parvumque a pectore natum
  - Andromache (Andromache; アンドロマケ): fidissima coniunx . . . Andromachē 565
  - natum (Astyanax; アステュアナクス): parvum . . . natum 565 を参照
  - Hectoris (Hector; ヘクトル): -oris 232. 565. 1006. 1040

566 Astyanacta tenet, cuius dum maximus heros
- [2] 566 Astyanacta tenet, cujus dum maximus heros
- [3] 566 Astyanacta tenet; cuius dum maximus heros
- [4] 566 Astyanacta tenet ; cujus dum maximus heros
- [6] 566 Astyanacta tenet; cuius dum maximus heros
  - Astyanacta (Astyanax; アステュアナクス): Andromache parvum . . . Astyanacta tenet 566
  - heros (Hector; ヘクトル): maximus heros 566

567 oscula parua petit, subito perterritus infans
- [2] 567 Oscula parva petit, subito perterritus infans •
- [3] 567 Oscula cara petit, subito perterritus infans
- [4] 567 Oscula grata petit, subito perterritus infans
- [6] 567 oscula parva petit, subito perterritus infans
  - infans (Astyanax; アステュアナクス): infans 567. 571

568 conuertit timidos materna ad pectora uultus
- [2] 568 Convertit timidos materna ad pectora vultus,
- [3] 568 Conuertit timidos materna ad pectora uultus
- [4] 568 Convertit timidos materna ad pectora vultus
- [6] 568 convertit timidos materna ad pectora vultus
  - materna (Andromache; アンドロマケ): materna ad pectora 568 を参照

569 terribilemque fugit galeam cristamque comantem.
- [2] 569 Terribilemque fugit galeam , cristamque micantem.
  - … 詩人たちにおいて *micare* はしばしば「震える、揺らめく」と同じ意味だからである。実際、兜の前立が幼子を何よりも怖がらせたのは、それが幼子の顔の前で激しく揺れ動き、頷くように揺れたからであった。Calp. Ecl. II, 26 に *manus jactare micantes*（素早く動く両手を振る）とあるのを見た。Ovid. Her. V, 37: « Attoniti micuere sinus »；同 Met. IX, 37: « Et modo cervicem, modo crura micantia captat »。
- [3] 569 Terribilemque fugit galeam cristasque comantes.
- [4] 569 Terribilemque fugit galeam cristamque micantem.
- [6] 569 terribilemque fugit galeam cristamque comantem.

570 Vtque caput iuuenis posito detexerat aere,
- [2] 570 Utque caput juvenis posito detexerat aere ,
  - *Juvenis*（若者）はいかなる戦士についても言われるが、ここではヘクトルを指す。――*Posito aere*（青銅を脱ぎ置いて）は、青銅の兜を脱ぎ置いて。
- [3] 570 Utque caput iuuenis posito detexerat aere,
- [4] 570 Utque caput juvenis posito detexerat aere,
- [6] 570 utque caput iuvenis posito detexerat aere,
  - iuvenis (Hector; ヘクトル): iuvenis 570

571 protinus infantem geminis amplectitur ulnis
- [2] 571 Protinus infantem geminis amplectitur ulnis,
- [3] 571 Protinus infantem geminis amplectitur ulnis
- [4] 571 Protinus infantem geminis amplectitur ulnis
- [6] 571 protinus infantem geminis amplectitur ulnis
  - infantem (Astyanax; アステュアナクス): infans 567. 571

572 attollensque manus: "Precor, o pater optime" - dixit -
- [2] 572 AttoUensque manus : «Precor, o pater optime, dixit.
- [3] 572 Attollensque manus 'precor, o pater optime' dixit,
- [4] 572 Attollensque manus « Precor, o pater optime » dixit,
  - pater (JUPPITER; ユピテル): 呼格:最善なる者よ(ヘクトルが祈る)
- [6] 572 attollensque manus 'precor, o pater optime' dixit,
  - pater (Iuppiter; ユピテル): o pater optime 572

573 "ut meus hic, pro quo tua numina, natus, adoro,
- [2] 573 Ut meus hic, pro quo tua numina, natus, adoro,
- [3] 573 'Ut meus hic, pro quo tua numina natus adoro,
- [4] 573 Ut meus hic, pro quo tua numina natus adoro,
- [6] 573 'ut meus hic, pro quo tua numina, natus, adoro,
  - natus (Astyanax; アステュアナクス): meus . . . natus 573

574 uirtutes patrias primis imitetur ab annis."
- [2] 574 Virtutes patrias primis imitetur ab annis».
  - … しかし私は、息子について語る父ヘクトルの人物像には、*miretur* と言った場合よりも *imitetur* という語のほうが適していると考える。父が自らについて語る際に称賛を求めるのはあまりに自慢たらしく響く。だが息子が己を見習うように求めることこそは、父にふさわしい訓戒である。さらに彼が *patrias virtutes*（父の美徳）を付け加えている以上、*imitetur* という語は必須である。美徳は見習うべきものであり、美徳のゆえに称賛されるのはむしろ人格である。作者はむしろ、アイネイアスが息子を励ますウェルギリウスの格言（Aen. XII, 435: « Disce, puer, virtutem ex me, verumque laborem, Fortunam ex aliis »［子よ、美徳と真の労苦を余より学べ、幸運は他者より学べ］）を念頭に置いていた可能性が高い。…
- [3] 574 Uirtutes patrias primis imitetur ab annis'.
- [4] 574 Virtutes patrias primis imitetur ab annis ».
- [6] 574 virtutes patrias primis imitetur ab annis'.

575 Haec ait et portis acies petit acer apertis,
- [2] 575 VII. Haec ait, et portis acies petit acer apertis :
- [3] 575 Haec ait et portis acies petit acer apertis;
- [4] 575 Haec ait, et portis acies petit acer apertis;
- [6] 575 haec ait et portis acies petit acer apertis;
  - portis (Troia; トロイア): portis 227. 575

576 una deinde Paris. Postquam in certamina uentumst,
- [2] 576 Una deinde Paris: postquam ad certamina ventum est,
- [3] 576 Una deinde Paris. postquam in certamina uentum est,
- [4] 576 Una deinde Paris. Postquam ad certamina ventum est,
  - Paris (PARIS; パリス): — ヘクトルとともに戦列を目指す
- [6] 576 una deinde Paris. postquam in certamina ventum est,
  - Paris (Paris; パリス): Paris 576. 756

577 protinus in medium procedit maximus Hector
- [2] 577 Protinus in medium procedit maximus Hector,
- [3] 577 Protinus in medium procedit maximus Hector
- [4] 577 Protinus in medium procedit maximus Hector
  - Hector (HECTOR; ヘクトル): — 最も偉大な者、ギリシアの将たちに挑む
- [6] 577 protinus in medium procedit maximus Hector
  - Hector (Hector; ヘクトル): maximus -or 577. 636

578 Graiorumque duces inuictis prouocat armis.
- [2] 578 Graiorumque duces invictis provocat armis.
- [3] 578 Graiorumque duces inuictis prouocat armis.
- [4] 578 Grajorumque duces invictis provocat armis.
  - Grajorum (GRAI; ギリシア人): — ヘクトルは彼らの将たちに挑む
- [6] 578 Graiorumque duces invictis provocat armis.
  - Graiorum (Graius; ギリシアの): -orum . . . duces 578

579 Nec mora: continuo fraudis commentor Vlixes
- [2] 579 Nec mora, continuo fraudis commentor Ulysses,
  - *Fraudis commentor*（詐術の考案者）。ホメロス風の手法で 527 行から繰り返した。
- [3] 579 Nec mora: continuo fraudis commentor Ulixes
- [4] 579 Nec mora : continuo fraudis commentor Ulixes
  - Ulixes (ULIXES; ウリクセス): — 欺瞞の考案者、ヘクトルがギリシアの将たちに武器で挑むと、他の者たちとともに進み出る
- [6] 579 nec mora: continuo fraudis commentor Vlixes
  - Vlixes (Vlixes; ウリクセス): fraudis . . . commentor -es 527. 579

580 et ferus Idomeneus et notus gente paterna
- [2] 580 Et ferus Idomeneus, et notus gente paterna
- [3] 580 Et ferus Idomeneus et notus gente paterna
- [4] 580 Et ferus Idomeneus et notus gente paterna
  - Idomeneus (IDOMENEUS; イドメネウス): — 猛き者、ヘクトルがギリシアの将たちに挑むと進み出る
  - Meriones (MERIONES; メリオネス): — 父祖の家柄で知られ、他の者たちとともに戦いに進み出る
- [6] 580 et ferus Idomeneus et iunctus gente paterna
  - Idomeneus (Idomeneus; イドメネウス): ferus -eus 580

581 Meriones Graiumque simul dux acer Atrides
- [2] 581 Meriones, Graiumque simul dux acer Atrides,
- [3] 581 Meriones Graiumque simul dux acer Atrides
- [4] 581 Meriones Grajumque simul dux acer Atrides
  - Atrides (AGAMEMNON; アガメムノン): — ギリシア人の猛き将、ヘクトルがギリシアの将たちに武器で挑むと、進み出る
  - Grajum (GRAI; ギリシア人): — ギリシア人の将、アガメムノン
- [6] 581 Meriones Graiumque simul dux acer Atrides
  - Atrides (Atrides (Agamemno); アトリデス（アガメムノン）): Graium . . . dux acer -es 581
  - Graium (Graius; ギリシアの): -um . . . dux 581
  - Meriones (Meriones; メリオネス): Idomeneus et *iunctus gente paterna -nes 581

582 Aiacesque duo <et> claris speciosus in armis
- [2] 582 Ajacesque duo clari , speciosus in armis
- [3] 582 Aiacesque duo clari et speciosus in armis
- [4] 582 Ajacesque duo, claris speciosus in armis
  - Ajaces (AJACES; アイアス二人): 二人の
  - Eurypylus (EURYPYLUS; エウリュピュロス): — 名高い武具で見事な者、他の者たちとともに進み出る
- [6] 582 Aiacesque duo \<et> claris speciosus in armis
  - Aiaces (Aiaces; アイアス二人): Aiacesque duo 582

583 Eurypylus magnoque Thoas Andraemone natus
- [2] 583 Eurypylus, magnoque Thoas Andraemone natus,
- [3] 583 Eurypylus magnoque Thoas Andraemone natus
- [4] 583 Eurypylus magnoque Thoas Andraemone natus
  - Andraemone (ANDRAEMO; アンドライモン): — 偉大な[アンドライモン]の子トアス
  - Thoas (THOAS; トアス): — 偉大なアンドライモンの子、ギリシアの他の将たちとともに進み出る
- [6] 583 Eurypylus magnoque Thoas Andraemone natus
  - Andraemone (Andraemon; アンドライモン): Thoas Andraemone natus 202. 583
  - Eurypylus (Eurypylus; エウリュピュロス): claris speciosus in armis -us 583
  - Thoas (Thoas; トアス): magno . . . Thoas Andraemone natus 583

584 quique manum Veneris uiolauit uulnere tristi
- [2] 584 Quique manum Veneris violavit vulnere tristi,
- [3] 584 Quique manum Ueneris uiolauit uulnere tristi
- [4] 584 Quique manum Veneris violavit vulnere tristi
  - Veneris (VENUS; ウェヌス): — 同じ者が彼女の手を傷つけた
- [6] 584 quique manum Veneris violavit vulnere tristi
  - qui (Diomedes; ディオメデス): 584 行:qui . . . manum Veneris violavit(559 を参照)
  - Veneris (Venus; ウェヌス): -eris 559. 584

585 procedunt; aberat nam Troum terror Achilles
- [2] 585 Procedunt : aberat nam Troum terror Achilles,
- [3] 585 Procedunt; aberat nam Troum terror Achilles
- [4] 585 Procedunt; aberat nam Troum terror Achilles
  - Achilles (ACHILLES; アキレウス): — トロイア人の恐怖、戦いから離れ、竪琴で恋心を慰める
  - Troum (TROJANI; トロイア人): — トロイア人の恐怖、アキレウス
- [6] 585 procedunt; aberat nam Troum terror Achilles
  - Achilles (Achilles; アキレウス): Troum terror -es 585
  - Troum (Tros; トロイア人): Troum terror Achilles 585

586 et cithara dulci durum lenibat amorem.
- [2] 586 Et dulci cithara dirum lenibat amorem.
  - … というのも、われらの詩人自身が上掲の 25 行で *ferum amorem*（野蛮な愛）と述べており、下掲の 641 行でもほぼ同様の言回しを用いているからである: *Praedaque, quae duros Menelai mulceat ignes*（メネラオスの激しき情火を和らげる戦利品）。そしてここでは、ウェルギリウスが Georg. IV, 464 でオルペウスについて « Ipse cava solans aegrum testudine amorem »（彼自ら中空の亀甲（竪琴）にて病める愛を慰めつつ）と述べたのを模倣したように思われる。
- [3] 586 Et cithara dulci durum lenibat amorem.
- [4] 586 Et cithara dulci durum lenibat amorem.
- [6] 586 et cithara dulci † divum lenibat amores.
  - amores (Briseis; ブリセイス): amores 586

586a
- [2] [587] [Sortes miserunt , quis eonim in bella valeret]
- [3] —
- [4] —
- [6] —

587 Ergo ubi deiectis auratam regis Atridae
- [2] 588 Ergo ubi dejectis auratam regis Atridae
  - *Ergo ubi dejectis*（それゆえ投げ入れられた［籤］において……）。Virg. Aen. V, 490: « Convenere viri, dejectamque aerea sortem Accepit galea »（男たちは集い、投げ入れられた籤を青銅の兜が受けた）から取られた。
- [3] 587 Ergo ubi deiectis auratam regis Atridae
- [4] 587 Ergo ubi dejectis auratam regis Atridae
  - Atridae (AGAMEMNON; アガメムノン): — 王の兜の中に籤が投げ入れられる
- [6] 587 ergo ubi deiectis auratam regis Atridae
  - Atridae (Atrides (Agamemno); アトリデス（アガメムノン）): regis -dae 587

588 sortibus in galeam magnus processerat Aiax,
- [2] 589 Sortibus in galeam , magnus processerat Ajax ,
- [3] 588 Sortibus in galeam magnus processerat Aiax,
- [4] 588 Sortibus in galeam magnus processerat Ajax,
  - Ajax (AJAX Telamonis filius; アイアス、テラモンの子): — 偉大なる者、アガメムノンの兜に籤が投げ入れられると進み出る
- [6] 588 sortibus in galeam magnus processerat Aiax,
  - Aiax (Aiax (Telamonius); アイアス（テラモンの子）): magnus . . . -ax 588

588a
- [2] 590 Concurrunt armis Ajax crudelis et Hector.
- [3] —
- [4] —
- [6] —

589 principio iactis committunt proelia telis:
- [2] 591 Principio jactis committunt praelia telis,
- [3] 589 Principio iactis committunt praelia telis,
- [4] 589 Principio jactis committunt proelia telis,
- [6] 589 principio iactis committunt proelia telis:

590 mox rigidos stringunt enses et fortibus armis
- [2] 592 Mox rigidos stringunt enses , et fortibus armis
- [3] 590 Mox rigidos stringunt enses et fortibus armis
- [4] 590 Mox rigidos stringunt enses et fortibus armis
- [6] 590 mox rigidos stringunt enses et fortibus armis

591 decernunt partesque oculis rimantur apertas
- [2] 593 Decernunt, partesque oculis rimantur apertas;
  - … われらの詩人自身がこの行の意味を下掲の 605 行で明らかにしている: « quaque patebat Nuda viri cervix, fulgentem dirigit ensem »（そして男のむき出しの首筋が露出していた箇所へ、輝く剣を向ける）。同様の趣旨で Virgil. Aeneid. XII, 920: « telum Aeneas fatale coruscat, Sortitus fortunam oculis »。――キケロは『ウェッレース弾劾演説』V (VII), 71 で、戦う者たちのこの習慣に言及している: « Si ullum locum aperuerimus suspicioni aut crimini, accipiendum est statim vulnus »（もし疑念や告発に少しでも隙を見せるなら、直ちに傷を受けねばならない）。パリ編者。
- [3] 591 Decernunt partesque oculis rimantur apertas
- [4] 591 Decernunt partesque oculis rimantur apertas
- [6] 591 decernunt partesque oculis rimantur apertas

592 et modo terga petunt, duros modo fortibus ictus
- [2] 594 Et modo terga petunt, duros modo fortibus ictus
- [3] 592 Et modo terga petunt, duros modo fortibus ictus
- [4] 592 Et modo terga petunt, duros modo fortibus ictus
- [6] 592 et modo terga petunt, duros modo fortibus ictus

593 depellunt clipeis; ingens ad sidera clamor
- [2] 595 Depellunt clypeis : ingens ad sidera clamor
- [3] 593 Depellunt clipeis; ingens ad sidera clamor
- [4] 593 Depellunt clipeis; ingens ad sidera clamor
- [6] 593 depellunt clipeis; ingens ad sidera clamor

594 tollitur et uastis impletur uocibus aer.
- [2] 596 Tollitur, et vastis impletur vocibus aether.
- [3] 594 Tollitur et uastis inpletur uocibus aether.
- [4] 594 Tollitur et vastis impletur vocibus aether.
- [6] 594 tollitur et vastis impletur vocibus aer.

595 Non sic saetigeri exacuunt feruoribus iras
- [2] 598 Non sic setigeri exacuunt fervoribus iras,
- [3] 595 Non sic setigeri exacuunt feruoribus iras
- [4] 595 Non sic setigeri exacuunt fervoribus iras
- [6] 595 non sic saetigeri exacuunt fervoribus iras

596 pectoribusque petunt uastis, modo dentibus uncis
- [2] 599 Pectoribusque premunt vastis, modo dentibus uncis
- [3] 596 Pectoribusque fremunt uastis, modo dentibus uncis
- [4] 596 Pectoribusque fremunt vastis, mox dentibus uncis
- [6] 596 pectoribusque petunt vastis, modo dentibus uncis

597 alterni librant gladios et uulnera miscent.
- [2] [597] [Alterni vibrant gladios, et vulnera miscent]
- [3] 597 Alterni librant cladis et uulnera miscent:
- [4] 597 below Alterni librant gladios et vulnera miscent
- [6] 597 alterni librant gladios et vulnera miscent.

598 fortia terga premunt spumantque per ora uicissim;
- [2] 600 Fortia terga petunt, spumantque per ora vicissim :
  - … 野猪の背がなぜ *dura* と呼ばれるのかは、Virg. Georg. III, 256 が説明している: « fricat arbore costas, Atque hinc atque illinc humeros ad vulnera durat »（木に肋骨をこすりつけ、傷口に対抗してあちこち肩を硬く鍛える）。これゆえオリュンピウス［ネメシアヌス］の Laud. Hercul. 110 において、猪は « duratus armos scopulis »（岩で肩を硬く鍛えた）と呼ばれている。
- [3] 598 Fortia terga tremunt spumantque fera ora uicissim,
- [4] 598 Fortia terga petunt spumantque per ora vicissim,
- [6] 598 fortia terga premunt spumantque per ora vicissim

599 fumiferae nubes concretaque fulgura et ignes
- [2] 601 Fumiferse nubes, concretaque fulgura, et ignes
  - … ウェルギリウスは Aen. IX, 522 で « Fumiferos ignes » と呼び、オウィディウスは Metam. VII, 114 で « fumificos mugitus » と呼んでいる。…しかしバルトは前掲の箇所で、作者が野猪から稲妻と火が吐き出されると述べているのは粗野な表現であると注記している。確かに詩人たちによって馬や雄牛に火が帰せられることは通例であり（Nemes. Cyneg. 255 およびペトロニウスの妖術師についての詩 11 行を参照）、野猪にも稲妻が帰せられるが、彼らはわれらの詩人よりも節度をもってそれを行っている。Ovidius, Met. VIII, 289、カリュドンの猪について: « Fulmen ab ore venit, frondes adflatibus ardent »（口より稲妻が出で、その息吹で木の葉が燃え上がる）；同 X, 550: « Fulmen habent acres in aduncis dentibus apri »（獰猛なる猪は鉤形の牙に稲妻を宿す）。
- [3] 599 Fumiferae nubes concrescunt, fulgura et ignes
- [4] 599 Fumiferae nubes et crebri fulminis ignes
- [6] 599 fumiferae nubes concretaque fulgura et ignes

600 iactantur magnoque implentur murmure siluae.
- [2] 602 Jactantur , magnoque implentur murmure silvae :
- [3] 600 Iactantur magnoque inplentur murmure siluae.
- [4] 600 Jactantur magnoque implentur murmure silvae.
- [6] 600 iactantur magnoque implentur murmure silvae:

601 Tales Priamides ardorque Aiacis in armis
- [2] [603] [Talis Priamides, simul Ajax fortis in armis]
- [3] [601] [Talis Priamides similisque Eacides armis.]
- [4] 601 below Talis Priamides similisque Aeacides armis
  - Aeacides (ACHILLES; アキレウス): [Aeacides]
  - Priamides (HECTOR; ヘクトル): Priamides [—]
- [6] 601 tales Priamides ardorque Aiacis in armis
  - Aiacis (Aiax (Telamonius); アイアス（テラモンの子）): ardorque -acis 601
  - Priamides (Priamides; プリアミデス): Priamides 601. 610. 660. 988

602 Tandem animis teloque furens Telamonius Aiax
- [2] 604 Tandem animis armisque furens Telamonius Ajax
- [3] 602 Tandem animis armisque furens Telamonius Aiax
- [4] 602 Tandem animis armisque furens Telamonius Ajax
  - Ajax (AJAX Telamonis filius; アイアス、テラモンの子): — テラモンの子、心と武器で荒れ狂い、ヘクトルに向かう
- [6] 602 tandem animis teloque furens Telamonius Aiax
  - Aiax (Aiax (Telamonius); アイアス（テラモンの子）): Telamonius -ax 205. 363. 602. 623. 787. 836
  - Telamonius (Telamonius; テラモンの): Telamonius Aiax 205. 363. 602. 623. 787. 836

603 insignem bello petit Hectora, quaque patebat
- [2] 605 Insignem bello petit Hectora, quaque patebat
- [3] 603 Insignem bello petit Hectora, quaque patescit
- [4] 603 Insignem bello petit Hectora, quaque patescit
  - Hectora (HECTOR; ヘクトル): Hectora:テラモンの子アイアスが戦で名高いヘクトルに向かう
- [6] 603 insignem bello petit Hectora, quaque patebat
  - Hectora (Hector; ヘクトル): insignem bello . . . -ora 603

604 nuda uiri ceruix, fulgentem derigit ensem.
- [2] 606 Nuda viri cervix , fulgentem dirigit ensem.
- [3] 604 Nuda uiri ceruix, fulgentem derigit hastam:
- [4] 604 Nuda viri cervix, fulgentem derigit hastam :
- [6] 604 nuda viri cervix, fulgentem derigit ensem:

605 Ille ictum celeri praeuidit callidus astu
- [2] 607 Ille ictum celeri praevidit callidus astu ,
- [3] 605 Ille ictum celeri praeuidit callidus actu
- [4] 605 Ille ictum celeri praevidit callidus astu
- [6] 605 ille ictum celeri praevidit callidus astu

606 tergaque summisit ferrumque umbone repellit.
- [2] 608 Tergaque submisit, ferrumque umbone recepit ,
- [3] 606 Tergaque summisit ferrumque umbone repellit.
- [4] 606 Tergaque summisit ferrumque umbone repellit.
- [6] 606 tergaque summisit ferrumque umbone repellit.

607 Sed leuis extremas clipei perlabitur oras
- [2] 609 Sed levis extremas clypei perlabitur oras
- [3] 607 Sed leuis extremas clipei perlabitur oras
- [4] 607 Sed levis extremas clipei perlabitur oras
- [6] 607 sed levis extremas clipei perlabitur oras

608 ensis et exiguo ceruicem uulnere libat.
- [2] 610 Ensis, et exiguo cervicem vulnere libat.
- [3] 608 Cuspis et exiguo ceruicem uulnere libat.
- [4] 608 Cuspis et exiguo cervicem vulnere libat.
- [6] 608 ensis et exiguo cervicem vulnere libat.

609 Acrius impugnans rursus consurgit in hostem
- [2] 611 Acrius adversum rursus consurgit in hostem
- [3] 609 Acrius inpugnans rursus consurgit in hostem
- [4] 609 Acrius impugnans rursus consurgit in hostem
- [6] 609 acrius impugnans rursus consurgit in hostem

610 Priamides nec iam ferro Telamone creatum,
- [2] 612 Priamides, nec jam ferro Telamone creatum,
- [3] 610 Priamides nec iam ferro Telamone creatum,
- [4] 610 Priamides nec jam ferro Telamone creatum,
  - Telamone (AJAX Telamonis filius; アイアス、テラモンの子): Telamone creatus:ヘクトルはテラモンの子に石で向かう
  - Priamides (HECTOR; ヘクトル): — アイアスに対して戦う
- [6] 610 Priamides nec iam ferro Telamone creatum,
  - Priamides (Priamides; プリアミデス): Priamides 601. 610. 660. 988
  - Telamone (Telamon; テラモン): -one creatum 610. 624

611 sed magno saxi iactu petit. At ferus Aiax
- [2] 613 Sed magno saxi jactu petit : at ferus Ajax
- [3] 611 Sed magno saxi iactu petit; at ferus Aiax
- [4] 611 Sed magno saxi jactu petit; at ferus Ajax
  - Ajax (AJAX Telamonis filius; アイアス、テラモンの子): — 猛々しく、ヘクトルが投げた石を盾で撥ね返した
- [6] 611 sed magno saxi iactu petit; at ferus Aiax
  - Aiax (Aiax (Telamonius); アイアス（テラモンの子）): ferus -ax 611

612 ingentem clipeo septemplice reppulit ictum
- [2] 614 Ingentem clypeo septemplice depulit ictum ,
  - … *Clypeo septemplice*（七重の盾で）はオウィディウスに倣ったものであり、彼は Met. XIII, 2 で « clypei dominus septemplicis Ajax »（七重の盾の主アイアス）といい、また同書 346 行で « frustra Telamone creatus Gestasset laeva taurorum tergora septem »（テラモンの子は無駄に左手に七重の牛革を帯びていたことになろう）と述べている。ウェルギリウスは Aen. XII, 925 でトゥルヌスについてこう述べている: « orasque recludit Loricae, et clypei extremos septemplicis orbes »（胸甲の縁を切り開き、七重の盾の最外周の輪を貫く）。
- [3] 612 Ingentem clipeo septemplice reppulit ictum
- [4] 612 Ingentem clipeo septemplice reppulit ictum
- [6] 612 ingentem clipeo septemplice reppulit ictum

613 et iuuenem saxo percussum sternit eodem.
- [2] 615 Et juvenem saxo percussum sternit codem.
- [3] 613 Et iuuenem saxo percussum sternit eodem.
- [4] 613 Et juvenem saxo percussum sternit eodem.
- [6] 613 et iuvenem saxo percussum sternit eodem.

614 Quem leuat exceptum Grais inimicus Apollo
- [2] 616 Quem levat exceptum Graiis inimicus Apollo,
- [3] 614 Quem leuat exceptum Grais inimicus Apollo,
- [4] 614 Quem levat exceptum Grais inimicus Apollo,
  - Apollo (APOLLO; アポロ): — ギリシア人に敵意を抱き、アイアスがヘクトルを打つ石を軽くする
  - Grais (GRAI; ギリシア人): — ギリシア人に敵意を抱くアポロ
- [6] 614 quem levat exceptum Grais inimicus Apollo
  - Apollo (Apollo; アポロ): Grais inimicus -o 614
  - Grais (Graius; ギリシアの): Grais 2. 277. 614

615 integratque animum; iam rursus ad arma coibant
- [2] 617 Integratque animum : jam rursus ad arma coibant,
  - **(cont.)** （前頁からの続き）*Integrare*（新たにする）は、バルトの指摘（*Adv.* p. 2807）によれば、元の完全な状態に戻すこと（*in integrum*）、更新することを実に見事に意味している。上の 101 行で彼が « Et Troum renovare velis in praelia vires »（そして戦いへ向けてトロイア勢の力を一新させようと欲する）と言ったのと同様である。Statius, *Theb.* VIII, 657: « bellum integrabat Enyo »。Seneca, *Medea*, v. 672: « semet dolor Accendit ipse, vimque praeteritam integrat »。
- [3] 615 Integrat atque animum; iam rursus ad arma coibant
- [4] 615 Integrat atque animum ; jam rursus ad arma coibant
- [6] 615 integratque animum; iam rursus ad arma coibant.

616 stringebantque iterum gladios, cum fessus in undas
- [2] 618 Stringebantque iteruni gladios , quum fessus in undas
- [3] 616 Stringebantque iterum gladios, cum fessus in undas
- [4] 616 Stringebantque iterum gladios, cum fessus in undas
  - Titan (TITAN; ティタン): — 疲れて、火を運ぶ戦車を波に沈め始めたとき
- [6] 616 stringebant iterum gladios, cum fessus in undas

617 coeperat igniferos Titan immergere currus
- [2] 619 Coeperat igniferos Titan immergere currus ,
- [3] 617 Coeperat igniferos Titan inmergere currus
- [4] 617 Coeperat igniferos Titan immergere currus
- [6] 617 coeperat igniferos Titan immergere currus
  - Titan (Titan; ティタン): fessus in undas coeperat igniferos -an immergere currus 617

618 noxque subire polum: iuxta mittuntur, utrosque
- [2] 620 Noxque subire polum : juxta mittuntur, utrosque
- [3] 618 Noxque subire polum: iuxta mittuntur, utrosque
- [4] 618 Noxque subire polum : juxta mittuntur utrimque
- [6] 618 noxque subire polum: iuxta mittuntur, utrosque

619 qui dirimant a caede uiros, nec segnius illi
- [2] 621 Qui dirimaut a caede viros, nec segnius illi
- [3] 619 Qui dirimant a caede uiros; nec segnius illi
- [4] 619 Qui dirimant a caede viros; nec segnius illi
- [6] 619 qui dirimant a caede viros; nec segnius illi

620 deponunt animos. Tunc bello maximus Hector:
- [2] 622 Deponunt animos : tum bello maximus Hector :
- [3] 620 Deponunt animos. tum bello maximus Hector
- [4] 620 Deponunt animos. Tum bello maximus Hector
  - Hector (HECTOR; ヘクトル): — 戦において最も偉大な者、アイアスに呼びかける
- [6] 620 deponunt animos. tum bello maximus Hector
  - Hector (Hector; ヘクトル): bello maximus -or 620. 832

621 "Quae te terra uirum, qui te genuere parentes?
- [2] 623 «Quae te terra virum, qui te genuere parentes?
  - … Virg. *Aen.* I, 606: « qui tanti talem genuere parentes »。
- [3] [621] ['Quae te terra uirum, qui te genuere parentes?
- [4] 621 below « Quae te terra virum, qui te genuere parentes?
- [6] 621 'quae te terra virum, qui te genuere parentes?

622 Viribus es proles generosa atque inclita" - dixit.
- [2] 624 Viribus es proles generosa atque inclyta?» dixit.
- [3] 622 Uiribus es proles generosa atque inclita' dixit.
- [4] 622 below Viribus es proles generosa atque inclita » dixit.
- [6] 622 viribus es proles generosa atque inclita' dixit.

623 At contra se ferre parat Telamonius Aiax:
- [2] 625 ContrahaBC dicta referre paratTelamoniusAjax:
- [3] 623 At contra referre parat Telamonius Aiax
- [4] 623 below At contra referre parat Telamonius Ajax :
  - Ajax (AJAX Telamonis filius; アイアス、テラモンの子): [— テラモンの子がヘクトルに答える]
- [6] 623 at contra se ferre parat Telamonius Aiax:
  - … ウェルギリウス『アエネーイス』5, 372 を参照
  - Aiax (Aiax (Telamonius); アイアス（テラモンの子）): Telamonius -ax 205. 363. 602. 623. 787. 836
  - Telamonius (Telamonius; テラモンの): Telamonius Aiax 205. 363. 602. 623. 787. 836

624 "Hesiona de matre uides Telamone creatum,
- [2] 626 «Hesiona de matre vides Telamone creatum,
- [3] 624 'Hesione de matre uides Telamone creatum;
- [4] 624 below « Hesione de matre vides Telamone creatum;
  - Telamone (AJAX Telamonis filius; アイアス、テラモンの子): — [汝は見る(彼は自らについて語る)]
  - Hesione (HESIONA; ヘシオネ): [Hesione 奪格:母ヘシオネから生まれたテラモンの子]
- [6] 624 'Hesiona de matre vides Telamone creatum,
  - Hesiona (Hesione; ヘシオネ): -na de matre . . . Telamone creatum Aiacem 624
  - Telamone (Telamon; テラモン): -one creatum 610. 624

625 nobilis est domus et fama generosa propago."
- [2] 627 Nobilis illa domus fama, et generosa propago».
- [3] 625 Nobilis est domus et fama generosa propago'.
- [4] 625 below Nobilis est domus et fama generosa propago ».
- [6] 625 nobilis est domus et fama generosa propago'.

626 Hector, ut Hesionae nomen casusque recordans:
- [2] 628 Hector ut Hesjpnae nomen casusque recordat,
  - … また *recordat*［能動態］は、古風な動詞の形式を時折用いることが多くの用例から知られているこの三流詩人にふさわしいからである。――上の 456 行の注、およびネメシアヌスの『鳥刺し考』(*De Aucupio*) 断片への注を参照されたい。パリ編者。――なお、ここで言及されているヘシオネは、トロイア王ラオメドンの娘であり、海獣に差し出されていたところをヘラクレスによって救出された。その後トロイアが陥落した際、ヘラクレスは最初に城壁をよじ登ったテラモンに彼女を妻として与えた。Ovid. *Metam.* XI, 216 以下。
- [3] 626 Hector ut Hesionae nomen casusque recordat]
- [4] 626 below Hector ut Hesionae nomen casusque recordat :
  - Hector (HECTOR; ヘクトル): [— アイアスに呼びかける]
  - Hesionae (HESIONA; ヘシオネ): [ヘシオネの名]
- [6] 626 Hector, ut Hesionae nomen casusque recordans,
  - Hector (Hector; ヘクトル): Hector 256. 277. 491. 626. 677. 774. 959. 967. 979. 996. 1051
  - Hesionae (Hesione; ヘシオネ): Hesionae nomen 626

627 "Absistamus" - ait - "sanguis communis utriquest",
- [2] 629 ff Absistamus, ait, sanguis communis utrique»;
- [3] 627 'Absistamus' ait, 'nam uis communis utrique est';
- [4] 627 « Absistamus » ait, « nam vis communis utrique »;
- [6] 627 'absistamus' ait, 'sanguis communis utrique est'

628 et prior Aeaciden aurato munerat ense
- [2] 630 Ajacemque prior aurato munerat ense,
- [3] 628 Et prior Aiacem deaurato munerat ense
- [4] 628 Et prior Ajacem fulgenti munerat ense
  - Ajacem (AJAX Telamonis filius; アイアス、テラモンの子): — ヘクトルはアイアスに輝く剣を贈る
- [6] 628 et prior Aeaciden aurato munerat ense
  - Aeaciden (Aeacides (Aiax Telamonius); アエアキデス（テラモンの子アイアス）): -dēn *628
  - Aeaciden (Aiax (Telamonius); アイアス（テラモンの子）): -acem は Aeaciden 368. 628 を参照

629 inque uicem, quo se bellator cinxerat Aiax,
- [2] 631 Inque vicem , quo se bellator cinxerat Ajax ,
- [3] 629 Inque uicem, quo se bellator cinxerat Aiax,
- [4] 629 Inque vicem, quo se bellator cinxerat Ajax,
  - Ajax (AJAX Telamonis filius; アイアス、テラモンの子): — 戦士、ヘクトルは彼が締めていた帯を受け取る
- [6] 629 inque vicem, quo se bellator cinxerat Aiax,
  - Aiax (Aiax (Telamonius); アイアス（テラモンの子）): bellator . . . -ax 629

630 accipit insignem uario caelamine balteum.
- [2] 632 Accipit insignem vario caelamine balteum.
  - **(cont.)** … 作者は Virg. *Aen.* X, 496: « rapiens immania pondera baltei » の例に倣って *balteum* を2音節［連形］とした。Ovid. *Met.* XIII, 291 は *caelamina clypei*（盾の彫刻）と言っている。
- [3] 630 Accipit insignem uario caelamine balteum.
- [4] 630 Accipit insignem vario caelamine balteum.
- [6] 630 accipit insignem vario caelamine balteum.

631 Post haec extemplo Graium Troumque cateruae
- [2] 633 Post Iioc extemplo Troum Danaumque catervse
- [3] 631 Post haec extemplo Troum Danaumque cateruae
- [4] 631 Post haec extemplo Danaum Troumque catervae
  - Danaum (GRAI; ギリシア人): — ダナオイとトロイア人の部隊が退く
  - Troum (TROJANI; トロイア人): — トロイア人とダナオイの部隊が退く
- [6] 631 post haec extemplo Troum Danaumque catervae
  - Danaum (Danai; ダナオイ): -um(属格):19. 50. 67. 124. 153. 251. 268. 357. 389. 496. 631. 686. 691. 698. 705. 743. 747. 794. 1025
  - Troum (Tros; トロイア人): Troum 102. 281. 339. 357. 438. 631. 641. 701. 963

632 discedunt caelumque tegit nox atra tenebris.
- [2] 634 Discedunt, caeiumque tegit nox atra tenebris.
- [3] 632 Discedunt, caelumque tegit nox atra tenebris.
- [4] 632 Discedunt, caelumque tegit nox atra tenebris.
- [6] 632 discedunt caelumque tegit nox atra tenebris.

633 Implentur dapibus largis Bacchique liquore
- [2] 635 Implentur dapibus largis Bacchique liquore,
- [3] 633 Inplentur dapibus largis Bacchique liquore
- [4] 633 Implentur dapibus largis Bacchique liquore
  - Bacchi (BACCHUS; バックス): Bacchi liquor:バックスの液
- [6] 633 implentur dapibus largis Bacchique liquore
  - Bacchi (Bacchus; バックス): Bacchi . . . liquore 633

634 atque auidi placido tradunt sua corpora somno.
- [2] 636 Atque avidi placido tradunt sua corpora somno.
- [3] 634 Atque auidi placido tradunt sua corpora somno.
- [4] 634 Atque avidi placido tradunt sua corpora somno.
- [6] 634 atque avidi placido tradunt sua corpora somno.

635 Postera cum primum stellas Aurora fugarat,
- [2] 637 Postera quum primum stellas Aurora fugarat ,
  - … ボンダムは、作者がこの行で同様にオウィディウスに倣ったと考えている。*Met.* XV, 665: « Postera sidereos Aurora fugaverat ignes »、および *Met.* IV, 81: « Postera nocturnos Aurora removerat ignes »。――またウェルギリウスの箇所 *Aeneid* III, 521 も援用できよう: « Jamque rubescebat stellis Aurora fugatis »。パリ編者。――しかし私としては、むしろウェルギリウスの *Aen.* V, 42: « Postera quum primo stellas Oriente fugarat Clara dies, socios in coetum litore ab omni Advocat Aeneas » がここで採用されたと見る。…
- [3] 635 Postera cum primum stellas Aurora fugarat,
  - : 『ベレンガリウスの事績』III 90 参照
- [4] 635 Postera cum primum stellas Aurora fugarat,
  - Aurora (AURORA; アウロラ): 星々を追い払う
- [6] 635 postera cum primum stellas Aurora fugarat,
  - （証言） = 『ベレンガリウスの事績』3, 90 (*fugaret*)
  - Aurora (Aurora; アウロラ): stellas Aurora fugarat 635

636 in coetum uenere Phryges. Tunc maximus Hector
- [2] 638 In coetum venere Phryges, tum maximus Hector
- [3] 636 In coetum uenere Phryges; tum maximus Hector
- [4] 636 In coetum venere Phryges; tum maximus Hector
  - Hector (HECTOR; ヘクトル): — 最も偉大な者、仲間たちとともに昨日の死者たちを思い起こす
  - Phryges (TROJANI; トロイア人): — 集会に来る
- [6] 636 in coetum venere Phryges; tunc maximus Hector
  - Hector (Hector; ヘクトル): maximus -or 577. 636
  - Phryges (Phryges; プリュギア人): Phryges 401. 493. 636. 682. 762. 803

637 cum sociis memorans hesternae funera caedis
- [2] 639 Cum sociis, raemorans hesternae funera caedis ,
- [3] 637 Cum sociis memorans hesternae funera caedis
- [4] 637 Cum sociis memorans hesternae funera caedis
- [6] 637 cum sociis memorans hesternae funera caedis

638 suadet ut inuictis Helene reddatur Achiuis
- [2] 640 Suadet ut invictis Helene reddatur Achivis,
- [3] 638 Suadet ut inuictis Helene reddatur Achiuis
- [4] 638 Suadet ut invictis Helene reddatur Achivis
  - Achivis (GRAI; ギリシア人): — ヘクトルは、ヘレネを不敗のアカイア人に返すよう勧める
  - Helene (HELENA; ヘレネ): Helene:ヘクトルは、ヘレネをギリシア人に返すよう勧める
- [6] 638 suadet ut invictis Helene reddatur Achivis
  - Achivis (Achivi; アカイア人): invictis . . . -is 638
  - Helene (Helene; ヘレネ): Helenē 638

639 praedaque quae duros Menelai mulceat ignes
- [2] 641 Praedaque, quae duros Menelai mulceat ignes;
- [3] 639 Praedaque quae duros Menelai mulceat ignes;
- [4] 639 Praedaque quae duros Menelai mulceat ignes.
  - Menelai (MENELAUS; メネラオス): — メネラオスの激しい炎を和らげる戦利品
- [6] 639 praedaque quae duros Menelai mulceat ignes
  - Menelai (Menelaus; メネラオス): -lai 519. 639

640 idque placet cunctis. Tunc saeuo missus Atridae
- [2] 642 Idque placet cunctis ; tum saevo missus Atridae
- [3] 640 Idque placet cunctis. tum saeuo missus Atridae
- [4] 640 Idque placet cunctis. Tum saevo missus Atridae
  - Atridae (MENELAUS; メネラオス): Atridae:イダイオスが残忍なアトレウスの子のもとへ送られる
- [6] 640 idque placet cunctis. tum saevo missus Atridae
  - Atridae (Atrides (Agamemno); アトリデス（アガメムノン）): saevo . . . -dae 640

641 pertulit Idaeus Troum mandata; neque ille
- [2] 643 Pertulit Idaeus Troum mandata, neque ille
- [3] 641 Pertulit Idaeus Troum mandata; neque ille
- [4] 641 Pertulit Idaeus Troum mandata, neque ille
  - Idaeus (IDAEUS Trojanorum praeco; イダイオス、トロイア人の伝令): — トロイア人の伝言をアガメムノンに伝える
  - Troum (TROJANI; トロイア人): — イダイオスがトロイア人の伝言をアガメムノンに伝える
- [6] 641 pertulit Idaeus Troum mandata; neque ille
  - Idaeus (Idaeus 2; イダイオス 2): Idaeus 641
  - Troum (Tros; トロイア人): Troum 102. 281. 339. 357. 438. 631. 641. 701. 963

642 aut animum praedae aut dictis accommodat aures,
- [2] 644 Aut animum praedae, aut dictis accommodat aures,
- [3] 642 Aut animum praedae aut dictis accommodat aures,
- [4] 642 Aut animum praedae aut dictis accommodat aures,
- [6] 642 aut animum praedae aut dictis accommodat aures,

643 ultro etiam castris Idaeum excedere iussit.
- [2] 645 Ultro etiam castris Idaeum excedere jussit.
- [3] 643 Ultro etiam castris Idaeum excedere iussit.
- [4] 643 Ultro etiam castris Idaeum excedere jussit.
  - Idaeum (IDAEUS Trojanorum praeco; イダイオス、トロイア人の伝令): Idaeum:アガメムノンはイダイオスに陣営から去るよう命じる
- [6] 643 ultro etiam castris Idaeum excedere iussit.
  - Idaeum (Idaeus 2; イダイオス 2): -um 643:トロイア人の伝令

644 Paruit is monitis iterumque ad castra reuersus
- [2] 646 Paruit hic monitis, iterumque ad castra reversus
- [3] 644 Paruit is monitis iterumque ad castra reuersus
- [4] 644 Paruit is monitis iterumque ad castra reversus
  - Troica (TROICUS; トロイアの): ad Troica castra:トロイアの陣営へ
- [6] 644 paruit is monitis iterumque ad castra reversus

645 Troiae contemptum duro se reddit ab hoste.
- [2] 647 Trojae, contemptum duro se reddit ab hoste.
  - … また、すでに再び引き返してそこに居るのだから *se reddit*（身を戻す）はおかしい、と不審に思うべきではない。そのような冗語（プレオナスムス）は優れた作家にも頻出するからである。Suetonius, *Jul.* 2: « intra paucos rursus dies repetita Bithynia »。Plautus, *Poenulus* 序幕 79: « Revertor rursus denuo Carthaginem »。
- [3] 645 Troica contemptum duro se reddit ab hoste.
- [4] 645 Troica contemptum duro se reddit ab hoste.
- [6] 645 Troiae contemptum duro se reddit ab hoste.
  - Troiae (Troicus; トロイアの): castra . . . Troica(異読 Troiae)645

646 Interea Danai confusi caede suorum
- [2] 648 Interea Danai conflisi caede suorum
  - … 後代ラテン語の著述家たちは、心を取り乱すこと（*perturbari animo*）の意で *confundi* と言う。Juvenal. *Sat.* III, 1: « Quamvis digressu veteris confusus amici »。Plinius, *Epist.* V, 5, 1: « qui nuntius gravi me dolore confudit »。同 *Paneg.* 86: « Quam ego audio confusionem tuam fuisse, quum digredientem prosequereris »。以下の 681 行で、われらの詩人は « Danai turbati caede suorum » と述べている。
- [3] 646 Interea Danai confusa caede suorum
- [4] 646 Interea Danai confusa caede suorum
  - Danai (GRAI; ギリシア人): — 火葬の薪を積む
- [6] 646 interea Danai confusi caede suorum
  - confusi … だが 679行および H 426 を参照; confusi は「悲嘆にくれた」の意
  - Danai (Danai; ダナオイ): Danai 508. 542. 646. 679. 766. 802. 838. 960. 978. 1002

647 ingentes struxere pyras collectaque passim
- [2] 649 Ingentes struxere pyras, colleetaque passim
- [3] 647 Ingentes struxere pyras collectaque passim
- [4] 647 Ingentes struxere pyras collectaque passim
- [6] 647 ingentes struxere pyras collectaque passim

648 fortia tradiderunt sociorum corpora flammis.
- [2] 650 Fortia tradiderunt sociorum corpora flammis.
- [3] 648 Fortia tradiderunt sociorum corpora flammis;
- [4] 648 Fortia tradiderunt sociorum corpora flammis;
- [6] 648 fortia tradiderunt sociorum corpora flammis;

649 Tum renouant fossas et uallum robore cingunt.
- [2] 651 Tjjm renovant fossas, et vallum robore cingunt.
  - … バルトの注記によれば、*robur*（オーク材・堅木）は木の柵、オークの囲壁を指す。そしてわれらの詩人は、683 行や 764 行のように、しばしばこのようなオーク材の堡塁（vallum）に言及している。
- [3] 649 Tum renouant fossas et uallum robore cingunt.
- [4] 649 Tum renovant fossas et vallum robore cingunt.
- [6] 649 tum renovant vires et vallum robore cingunt.

## Book 8

650 Vt nitidum Titan radiis patefecerat orbem,
- [2] 652 VIII. Ut nitidum Titan radiis patefecerat orbem ,
  - … ボンダムは前掲書で、この行が Ovid. *Met.* IX, 796: « Postera lux radiis totum patefecerat orbem » から形作られたと指摘している。Virg. *Aen.* IV, 118: « ubi ortus Extulerit Titan radiisque retexerit orbem » も同様である。
- [3] 650 Ut nitidum Titan radiis patefecerat orbem,
- [4] 650 Ut nitidum Titan radiis patefecerat orbem,
  - Titan (TITAN; ティタン): — 光線で輝く円盤をあらわにしたとき
- [6] 650 ut nitidum Titan radiis patefecerat orbem,
  - Titan (Titan; ティタン): nitidum -an radiis patefecerat orbem 650

651 conuocat in coetum superos Iouis et monet, armis
- [2] 653 Convocat in coetum Superos Jovis, et mouet onmes,
- [3] 651 Conuocat in coetum superos Iouis et monet omnis,
- [4] 651 Convocat in coetum superos Jovis et monet omnes,
  - Jovis (JUPPITER; ユピテル): Jovis 主格:天上の神々を集会に呼び集める
- [6] 651 convocat in coetum superos Iovis et monet, armis
  - Iovis (Iuppiter; ユピテル): 主格:Iovis 651

652 ne contra sua dicta uelint contendere diui.
- [2] 654 Ne contra sua dicta velint contendere Divi.
- [3] 652 Ne contra sua dicta uelint contendere diui.
- [4] 652 Ne contra sua dicta velint contendere divi.
- [6] 652 ne contra sua dicta velint contendere divi.

653 Ipse per aetherias caeli delabitur auras
- [2] 655 Ipse per aethereas caeli delabitur auras,
- [3] 653 Ipse per aethereas caeli delabitur auras
- [4] 653 Ipse per aethereas caeli delabitur auras
- [6] 653 ipse per aethereas caeli delabitur auras

654 umbrosisque simul consedit montibus Idae.
- [2] 656 Umbrosisque simul consedit montibus Idae :
- [3] 654 Umbrosisque simul consedit montibus Idae;
- [4] 654 Umbrosisque simul consedit montibus Idae;
  - Idae (IDA; イダ): Idae:ユピテルはイダの木陰多い山々に座る
- [6] 654 umbrosisque simul consedit montibus Idae:
  - Idae (Ida; イダ): umbrosis . . . montibus Idae 654

655 Inde acies uidet Iliacas dextraque potenti
- [2] 657 Inde acies videt Iliacas, dextraqiie potenti
- [3] 655 Inde acies uidet Iliacas dextraque potenti
- [4] 655 Inde acies videt Iliacas dextraque potenti
  - Iliacas (ILIACUS; イリオンの): Iliacas acies:イリオンの戦列
- [6] 655 inde acies videt Iliacas dextraque potenti
  - Iliacas (Iliacus; イリオンの): acies . . . -cas 655

656 sustinet auratas aequato pondere lances
- [2] 658 Sustinet auratas aequato pondere lances,
- [3] 656 Sustinet auratas aequato pondere lances
- [4] 656 Sustinet auratas aequato pondere lances
- [6] 656 sustinet auratas aequato pondere lances

657 fataque dura Phrygum casusque expendit Achiuum
- [2] 659 Fataque dura Phryguin , casusque expendit Achivum ,
- [3] 657 Fataque dura Phrygum casusque expendit Achiuum
- [4] 657 Fataque dura Phrygum casusque expendit Achivum
  - Achivum (GRAI; ギリシア人): — ユピテルはアカイア人とプリュギア人の運命を量る
  - Phrygum (TROJANI; トロイア人): — ユピテルはプリュギア人の過酷な運命とギリシア人の運命を量る
- [6] 657 fataque dura Phrygum casusque expendit Achivum
  - Achivum (Achivi; アカイア人): -um 506. 657
  - Phrygum (Phryges; プリュギア人): fata . . . -um 657

658 et Graium clades grauibus praeponderat armis.
- [2] 660 Et Graium clades gravibus praeponderat armis.
- [3] 658 Et Graium clades grauibus praeponderat armis.
- [4] 658 Et Grajum clades gravibus praeponderat armis.
  - Grajum (GRAI; ギリシア人): — ユピテルが量ると、ギリシア人の災厄のほうが重い
- [6] 658 et Graium clades gravibus praeponderat armis.
  - Graium (Graius; ギリシアの): -um clades 658

659 Interea Danaos ingenti concitus ira
- [2] 661 Interea Danaos ingenti conciius ira
- [3] 659 Interea Danaos ingenti concitus ira
- [4] 659 Interea Danaos, ingenti concitus ira,
  - Danaos (GRAI; ギリシア人): — ヘクトルはダナオイに襲いかかる
- [6] 659 interea Danaos ingenti concitus ira
  - Danaos (Danai; ダナオイ): -os 45. 492. 659. 808. 912. 950. 1001

660 Priamides agit et totis grauis imminet armis
- [2] 662 Prlamides agit, et totis gravis imminet armis,
- [3] 660 Priamides agit et totis grauis imminet aruis,
- [4] 660 Priamides agit et gradiens supereminet omnes,
  - gradiens supereminet omnes 筆者（『アエネーイス』I, 501 を参照）…［armis は両肩について解されるべきと思われる……サンテンは Totis armis を「全軍」の意味に解した、クーテン］…
  - Priamides (HECTOR; ヘクトル): — プリュギアのただ一つの誉れ、怒って戦う
- [6] 660 Priamides agit et totis gravis imminet armis,
  - … armis … すなわち軍勢; 例えばオウィディウス『変身物語』7, 865 を参照
  - Priamides (Priamides; プリアミデス): Priamides 601. 610. 660. 988

661 unum quippe decus Phrygiae. Turbantur Achiui
- [2] 663 Unum quippe decus Phrygiae : turbantur Achivi,
- [3] 661 Unum quippe decus Phrygiae; turbantur Achiui
- [4] 661 Unum quippe decus Phrygiae; turbantur Achivi
  - Achivi (GRAI; ギリシア人): Achivi 主格:混乱に陥る
  - Phrygiae (PHRYGIA; プリュギア): Phrygiae unum decus:プリュギアのただ一つの誉れ(ヘクトル)
- [6] 661 unum quippe decus Phrygiae; turbantur Achivi
  - Achivi (Achivi; アカイア人): 661
  - decus (Hector; ヘクトル): unum . . . decus Phrygiae 661
  - Phrygiae (Phrygia; プリュギア): unum . . . decus Phrygiae、ヘクトル:661

662 Doricaque ingenti complentur castra tumultu.
- [2] 664 Doricaque ingenti complentur castra tumultu.
- [3] 662 Doricaque ingenti complentur castra tumultu.
- [4] 662 Doricaque ingenti complentur castra tumultu.
  - Dorica (DORICUS; ドリスの): Dorica castra:ドリスの陣営
- [6] 662 Doricaque ingenti complentur castra tumultu.
  - Dorica (Doricus; ドリスの): -ca . . . castra 662

663 Hortatur socios muris inclusus Atrides
- [2] 665 Hortatur socios muris inciusus Atrides,
- [3] 663 Hortatur socios muris inclusus Atrides
- [4] 663 Hortatur socios muris inclusus Atrides
  - Atrides (AGAMEMNON; アガメムノン): — 仲間たちを励ます
- [6] 663 hortatur socios murisque inclusus Atrides
  - Atrides (Atrides (Agamemno); アトリデス（アガメムノン）): -es 24. 510(?) 663

664 languentesque animos iuuenum in certamina firmat.
- [2] 666 Languentesque animos juvenum in certamina firmat.
- [3] 664 Languentesque animos iuuenum in certamina firmat.
- [4] 664 Languentesque animos juvenum in certamina firmat.
- [6] 664 languentes animos iuvenum in certamina firmat.

665 Princeps Tydides fulgens ardentibus armis
- [2] 667 Princeps Tydides ardentibus emicat armis,
  - *Ardentibus armis*。上の 394 行で *flagrantia arma* と言ったのと同様である。パリ編者。
- [3] 665 Princeps Tydides ardentibus emicat armis,
- [4] 665 Princeps Tydides ardentibus emicat armis,
  - Tydides (DIOMEDES; ディオメデス): — 将として、燃える武具で躍り出る
- [6] 665 princeps Tydides ardentibus emicat armis
  - Tydides (Tydides; テュディデス): Tydides 390. 408. 530. 665. 1008

666 per medios hostes immani pondere fertur.
- [2] 668 Per mediosquc hostes immani turbine fertur.
- [3] 666 Per mediosque hostes inmani turbine fertur.
- [4] 666 Per mediosque hostes immani turbine fertur.
- [6] 666 per medios\<que> hostes immani turbine fertur.

667 Hic illi occurrit fatis Agelaus iniquis,
- [2] 669 Hic illi occurrit fatis Agelaus iniquis
  - … この箇所にはプラドモンの子アゲラオス（Agelaus Phradmonides）が置かれるべきである。ホメロス（*Iliad* VIII, 258）は、彼がディオメデスによって槍で背中から胸へと刺し通されたと伝えている。
- [3] 667 Hic illi occurrit fatis Agelaus iniquis,
- [4] 667 Hic illi occurrit fatis Agelaus iniquis,
  - **667, 672** Agelaus, Gorgythiona …（『イリアス』VIII, 257 および 302）。
  - Agelaus (AGELAUS; アゲラオス): ディオメデスに立ち向かう
- [6] 667 hic illi occurrit fatis Agelaus iniquis,
  - Agelaus (Agelaus; アゲラオス): Agelaus 667:トロイア人、プラドモンの子

668 telum immane manu quatiens, quem maximus heros
- [2] 670 Telum immane manu quatiens, quem maximus heros,
- [3] 668 Telum inmane manu quatiens, quem maximus heros
- [4] 668 Telum immane manu quatiens, quem maximus heros
- [6] 668 telum immane manu quatiens, quem maximus heros
  - heros (Diomedes; ディオメデス): 668 maximus heros

669 occupat et duro medium transuerberat ense.
- [2] 671 Occupat , et duro medium transverberat ense.
  - … ホメロスに従えば、ここでは *ense*（剣）ではなく *hasta*（槍）と言われるべきであり、…
- [3] 669 Occupat et duro medium transuerberat ense.
- [4] 669 Occupat et duro medium transverberat ense.
- [6] 669 occupat et duro medium transverberat ense.

670 Hinc Phrygas Aiacis uastis protectus in armis
- [2] 672 Hinc Phrygas Ajacis vastis protectus in armis
  - … テウクロスがアイアスの盾に守られながら多くのトロイア勢を矢で射殺したと伝えている（*Iliad* VIII, 266: Τεῦκρος δ᾽ εἴνατος ἦλθε, παλίντονα τόξα τιταίνων. Στῆ δ᾽ ἄρ᾽ ὑπ᾽ Αἴαντος σάκεϊ Τελαμωνιάδαο；および 272 行: ὁ δέ μιν σάκεϊ κρύπτασκε φαεινῷ）。…
- [3] 670 Hinc Phrygas Aiacis uastis protectus in armis
- [4] 670 Hinc Phrygas Ajacis vastis protectus in armis
  - Ajacis (AJAX Telamonis filius; アイアス、テラモンの子): In Ajacis armis:アイアスの武具に守られて、テウクロスはトロイア人を追い立てる
  - Teucer (TEUCER; テウクロス): アイアスの盾の下に立ってトロイア人を追い立てる
  - Phrygas (TROJANI; トロイア人): — テウクロスはアイアスの盾の下に立ってプリュギア人を追い立てる
- [6] 670 hinc Phrygas Aiacis vastis protectus in armis
  - Aiacis (Aiax (Telamonius); アイアス（テラモンの子）): -acis 670
  - Phrygas (Phryges; プリュギア人): -as (-es trad.) . . . Teucer agit 670

671 Teucer agit spargitque leues in terga sagittas.
- [2] 673 Teucer agit , spargitque leves in terga sagittas :
- [3] 671 Teucer agit spargitque leues in terga sagittas.
- [4] 671 Teucer agit spargitque leves in terga sagittas.
- [6] 671 Teucer agit spargitque leves in terga sagittas.
  - Teucer (Teucer; テウクロス): Teucer 671

672 Gorgythiona ferum letali uulnere fundit;
- [2] 674 Gorgythiona ferum letali vulnere fundit.
  - … Hom. *Iliad* VIII, 302 に基づいて *Gorgythiona*（ゴルギュティオン）と読まれるべきである …
- [3] 672 Gorgythiona ferum letali uulnere fundit,
- [4] 672 Gorgythiona ferum letali vulnere fundit,
  - Gorgythiona (GORGYTHION; ゴルギュティオン): Gorgythiona:テウクロスが猛きゴルギュティオンを殺す
- [6] 672 Gorgythiona ferum letali vulnere fundit,
  - Gorgythiona (Gorgythion; ゴルギュティオン): *Gorgythiona ferum 672:プリアモスの子

673 mox alias acies petit aurigamque superbi
- [2] 675 Mox alias acies petit, aurigamque superbi
- [3] 673 Mox alias acies petit aurigamque superbi
- [4] 673 Mox alias acies petit aurigamque superbi
  - Hectoris (HECTOR; ヘクトル): — テウクロスは驕れるヘクトルの御者を斬り倒す
- [6] 673 mox alias acies petit aurigamque superbi
  - aurigam (Archeptolemus; アルケプトレモス): aurigam . . . Hectoris 673

674 Hectoris obtruncat, quem saxo Troius heros
- [2] 676 Hectoris obtruncat, quem saxo Troius heros
  - *Quem*（彼を）、すなわちテウクロス。パリ編者。
- [3] 674 Hectoris obtruncat. quem saxo Troius heros
- [4] 674 Hectoris obtruncat. Quem saxo Troius heros
  - Troius (HECTOR; ヘクトル): Troius heros:トロイアの英雄が石でテウクロスを倒す
- [6] 674 Hectoris obtruncat. quem saxo Troius heros
  - Hectoris (Hector; ヘクトル): superbi -oris 674
  - Troius (Troius; トロイアの): Troius heros、ヘクトル:674

675 occupat excussoque incautum proterit arcu.
- [2] 677 Occupat, excussoque incautum proterit arcu.
  - … *excusso arcu*（弓を打ち落とされて）によって、ヘクトルが投じた石の打撃でテウクロスの手から弓が叩き落とされたことが意味されている。
- [3] 675 Occupat excussoque extentum proterit arcu:
- [4] 675 Occupat excussoque incautum proterit arcu :
- [6] 675 occupat excussoque incautum proterit arcu:

676 Ast illum fidi rapiunt de caede sodales
- [2] 678 Ast illum fidi rapiunt de caede sodales,
  - … オウィディウスにその言い回しがある（*Her.* VI, 135: « Prodidit illa patrem: rapui de caede Thoanta »）。
- [3] 676 Ast illum fidi rapiunt de caede sodales
- [4] 676 Ast illum fidi rapiunt de caede sodales
- [6] 676 ast illum fidi rapiunt de caede sodales

677 prostratumque leuant. Ruit undique turbidus Hector
- [2] 679 Prostratumque levant: ruit undique turbidus Heclor,
- [3] 677 Prostratumque leuant. ruit undique turbidus Hector
- [4] 677 Prostratumque levant. Ruit undique turbidus Hector
  - Hector (HECTOR; ヘクトル): — 荒れ狂って突進する
- [6] 677 prostratumque levant. ruit undique turbidus Hector
  - Hector (Hector; ヘクトル): Hector 256. 277. 491. 626. 677. 774. 959. 967. 979. 996. 1051

678 aduersasque acies infesta cuspide terret.
- [2] 680 Adversasque acies infesta cuspide terret.
- [3] 678 Aduersaque acies inuersas cuspide terret.
- [4] 678 Adversasque acies infesta cuspide terret.
- [6] 678 adversasque acies infesta cuspide terret.

679 Se rursus Danai turbati caede suorum
- [2] 681 Sed rursus Danai turbati caede suorum
- [3] 679 Sic rursus Danai turbati caede suorum
- [4] 679 Sic rursus Danai turbati caede suorum
  - Danai (GRAI; ギリシア人): — 逃げ込む
- [6] 679 se rursus Danai turbati caede suorum
  - Danai (Danai; ダナオイ): Danai 508. 542. 646. 679. 766. 802. 838. 960. 978. 1002

680 conuertunt iterumque leues in castra cateruae
- [2] 682 Concurrunt , iterumque leves in castra catervae
- [3] 680 Conuertunt, iterumque leues in castra cateruae
- [4] 680 Convertunt, iterumque leves in castra catervae
- [6] 680 convertunt, iterumque leves in castra catervae

681 confugiunt portasque obiecto robore firmant.
- [2] 683 Confugiunt , portasque objecto robore firmant.
  - *Objecto robore*（オークの横木を差し渡して）、すなわちオーク材のかんぬき（pessulus）を差し渡して。この行全体が以下の 935 行で再び現れる。762 行も比較されたい。
- [3] 681 Confugiunt portasque obiecto robore firmant.
- [4] 681 Confugiunt portasque objecto robore firmant.
- [6] 681 confugiunt portasque obiecto robore firmant.

682 At Phryges obsidunt inclusos aggere Graios
- [2] 684 At Phryges obsidunt inclusos aggere Graios,
- [3] 682 At Phryges obsidunt inclusos aggere Graios
- [4] 682 At Phryges obsidunt inclusos aggere Grajos
  - Grajos (GRAI; ギリシア人): Grajos:トロイア人は塁壁の内に閉じ込められたギリシア人を包囲する
  - Phryges (TROJANI; トロイア人): — 塁壁の内に閉じ込められたギリシア人を包囲する
- [6] 682 at Phryges obsidunt inclusos aggere Graios
  - Graios (Graius; ギリシアの): Graios 682. 755. 763
  - Phryges (Phryges; プリュギア人): Phryges 401. 493. 636. 682. 762. 803

683 excubituque premunt muros flammisque coronant.
- [2] 685 Excubiisque premunt muros, flammisque coronant.
  - … というのもウェルギリウスの *Aen.* IX, 160 に « Interea vigilum excubiis obsidere portas Cura datur Messapo, et moenia cingere flammis »（すなわち見張りの篝火で）、また同 380 行に « omnemque aditum custode coronant » とあるからである。
- [3] 683 Excubituque premunt muros flammisque coronant.
- [4] 683 Excubituque premunt muros flammisque coronant.
- [6] 683 excubituque premunt muros flammisque coronant.

684 Cetera per campos sternunt sua corpora pubes
- [2] 686 Caetera per campos sternit sua corpora pubes,
- [3] 684 Cetera per campos sternunt sua corpora pubes
- [4] 684 Cetera per campos sternunt sua corpora pubes
- [6] 684 cetera per campos sternunt sua corpora pubes

685 indulgentque mero curas<que> animosque resoluunt.
- [2] 687 Indulgentque mero, curas animosque resolvunt.
- [3] 685 Indulgentque mero curasque animosque resoluunt.
- [4] 685 Indulgentque mero, curis animosque resolvunt.
- [6] 685 indulgentque mero curas\<que> animosque resolvunt.

## Book 9

686 Attoniti Danaum proceres discrimine tanto
- [2] 688 IX. Atfoniti Danaum proceres discrimine tanto
- [3] 686 Attoniti Danaum proceres discrimine tanto
- [4] 686 Attoniti Danaum proceres discrimine tanto
  - Danaum (GRAI; ギリシア人): — 首領たち
- [6] 686 attoniti Danaum proceres discrimine tanto
  - Danaum (Danai; ダナオイ): -um(属格):19. 50. 67. 124. 153. 251. 268. 357. 389. 496. 631. 686. 691. 698. 705. 743. 747. 794. 1025

687 nec dapibus releuant animos nec corpora curant,
- [2] 689 Nec dapibus relevant animos, nec corpora curant,
- [3] 687 Nec dapibus releuant animos nec corpora curant,
- [4] 687 Nec dapibus relevant animos nec corpora curant,
- [6] 687 nec dapibus relevant animos nec corpora curant,

688 sed miseri sua fata gemunt. Mox Nestore pulsi
- [2] 690 Sed miseri sua fata gemunt : mox hoste repulso
- [3] 688 Sed miseri sua fata gemunt. *tamen hoste repulso*
- [4] 688 Sed miseri sua fata gemunt. Jam, nocte recepti,
- [6] 688 sed miseri sua fata gemunt. mox † hoste repulso

689 legatos mittunt dextramque hortantur Achillis,
- [2] 691 Legatos mittunt, dextramque hortantur Achillis,
  - *Dextramque hortantur Achillis*（そしてアキレウスの右手を促す／求める）。バルトは 2807 頁で、この箇所において「右手」（*dextram*）が信義（*fides*）を意味していると指摘し、さらに古代人の多くの箇所を引いて、友情、好意、および寛容の証として右手がお互いに交わされたこと、同様に右手を差し出すことによって相互の約束が取り交わされ、和平が成立し、同盟が結ばれたことを論証している。これらはすべて周知の事柄であり、ここで繰り返すには長すぎる。一、二の例を挙げておこう。Valer. Flacc. II, 639（キュジコスについて）: « Ut videt, ipse ultro primus procurrit ad undas, Miraturque viros, dextraque amplexus et haerens Incipit »。同書第3巻 14: « manibusque datis junxere nepotes »、すなわちすべての子孫にわたる永久の同盟を結んだ（ただしグロノウィウスはそこで *penates* を採ろうとしている）。プロスペル『恩知らずについて』(*De Ingratis*): « An dextram, pacis palmam, dare te pudet hosti »。われらのホメロス模倣者のこの箇所においては、私の意見の趣くところでは、右手によってアキレウスの信義や友情だけでなく、彼の武勇や軍事的武力も示されている。
- [3] 689 Legatos mittunt dextramque hortantur Achillis,
- [4] 689 Legatos mittunt dextramque hortantur Achillis,
  - Achillis (ACHILLES; アキレウス): — ギリシアの使節たちは、助けをもたらすよう彼の右手に促すが無駄である
- [6] 689 legatos mittunt dextramque hortantur Achillis,
  - Achillis (Achilles; アキレウス): -is 54. 689. 719. 806

690 ut ferat auxilium miseris. Thetideius heros
- [2] 692 Ut ferat auxilium miseris. Thetideius heros
  - … ファン・デル・デュッセンは 36 頁で *Thetideius*（すなわちテティスの子）と読まれるべきであると見抜き、それはわれらの詩人の他の箇所（897、943、962 行など）でも正しく置かれている。…
- [3] 690 Ut ferat auxilium miseris. Thetideius heros
- [4] 690 Ut ferat auxilium miseris. Thetideius heros
  - Thetideius (ACHILLES; アキレウス): Thetideius heros:ギリシア人の嘆願をはねつける
- [6] 690 ut ferat auxilium miseris. Thetideius heros
  - Thetideius (Thetideius; テティスの子): Thetideius heros 690. 892:アキレウス

691 nec Danaum capit aure preces nec munera regis
- [2] 693 Nec Danaum capit aure preces, nec munera regis
- [3] 691 Nec Danaum capit aure preces nec munera regis
- [4] 691 Nec Danaum capit aure preces nec munera regis
  - Danaum (GRAI; ギリシア人): — アキレウスはダナオイの嘆願を退ける
- [6] 691 nec Danaum capit aure preces nec munera regis
  - regis (Agamemnon; アガメムノン): rex 58. 134. 691
  - Danaum (Danai; ダナオイ): -um(属格):19. 50. 67. 124. 153. 251. 268. 357. 389. 496. 631. 686. 691. 698. 705. 743. 747. 794. 1025

692 ulla referre cupit; non illum redditus ignis
- [2] 694 Ulla referre cupit : neque enim illum rcdditus ignis
- [3] 692 Ulla referre cupit; non illum redditus ignis
- [4] 692 Ulla referre cupit; non illum redditus ignis
- [6] 692 ulla referre cupit; non illum redditus ignis
  - ignis (Briseis; ブリセイス): redditus ignis 692

693 aut intacta suo Briseis corpore mouit.
- [2] 695 Aut infacta suo Briseis corpore movit.
- [3] 693 Aut intacta suo Briseis corpore mouit:
- [4] 693 Atque intacta suo Briseis corpore movit:
  - Briseis (BRISEIS; ブリセイス): たとえ手つかずのまま返されても、アキレウスを動かさない
- [6] 693 aut intacta suo Briseis corpore movit:
  - Briseis (Briseis; ブリセイス): intacta . . . Briseis 693

694 Irrita legati referunt responsa Pelasgis
- [2] 696 Irrita lcgati referunt responsa Pelasgis :
- [3] 694 Irrita legati referunt responsa Pelasgis.
- [4] 694 Irrita legati referunt responsa Pelasgis.
  - Pelasgis (GRAI; ギリシア人): Pelasgis:使節たちはペラスゴイにアキレウスの返答を伝える
- [6] 694 irrita legati referunt responsa Pelasgis
  - Pelasgis (Pelasgi; ペラスゴイ): -gis 694

695 et dapibus curant animos lenique sopore.
- [2] 697 Hinc dapibus curant animos lenique sopore.
- [3] [695] [Et dapibus curant animos lenique sopore.]
- [4] 695 below Et dapibus curant animos lenique sopore
- [6] 695 et dapibus curant animos lenique sopore.

## Book 10

696 Alterius tenebrae tarde labentibus astris
- [2] 698 X. Altera transierat tarde labentibus astris.
  - … ここでは、ホメロスから明らかなように、別の夜ではなくまさに同じ夜に行われた新たな出来事の叙-
  - **(cont.)** （前頁からの続き）―が始まり、後続の行で *pars tertia noctis*（夜の第三の部分）が付け加えられているからには、流布本が直前の *lenique sopore* と結びつけているように見える *alterius noctis*（別の夜の）は、ここに位置を占めることができない。むしろ作者は、上に述べられた事柄が起きたその夜の、まもなく第三の部分を付け加えることになる第二の部分（もうひとつの部分）を意味しようとしたのである。…
- [3] 696 Ulterius tenebrae tarde labentibus astris
- [4] 696 Ulterius tenebrae tarde labentibus astris [696]
- [6] 696 alterius tenebrae tarde labentibus astris

697 restabatque super tacitae pars tertia noctis,
- [2] 699 Restabatque super tacitae pars tertia noctis;
  - … これが翻訳元のホメロスの詩行（*Iliad* X, 252: Ἄστρα δὲ δὴ προβέβηκε· παρῴχηκεν δὲ πλέων νὺξ Τῶν δύο μοιράων, τριτάτη δ᾽ ἔτι μοῖρα λέλειπται）によっても裏づけられている。
- [3] 697 Restabatque super tacitae pars tertia noctis,
- [4] 697 Restabatque super tacitae pars tertia noctis,
- [6] 697 restabatque super tacitae pars tertia noctis,

698 cum Danaum iussu castris Aetolius heros
- [2] 700 Quum Danaum jussu castris Aetolius heros
- [3] 698 Cum Danaum iussu castris Aetolius heros
- [4] 698 Cum Danaum jussu castris Aetolius heros
  - Aetolius (DIOMEDES; ディオメデス): — ウリクセスとともに陣営を出る
  - Danaum (GRAI; ギリシア人): — ダナオイの命により、ディオメデスはウリクセスとともに陣営を出る
- [6] 698 cum Danaum iussu castris Aetolius heros
  - Aetolius (Aetolius; アイトリアの): Aetolius heros 556. 698:ディオメデス
  - Danaum (Danai; ダナオイ): -um(属格):19. 50. 67. 124. 153. 251. 268. 357. 389. 496. 631. 686. 691. 698. 705. 743. 747. 794. 1025

699 egreditur sociumque sibi delegit Vlixem,
- [2] 701 Egreditur, sociumque sibi delegit Ulyssem,
- [3] 699 Egreditur sociumque sibi delegit Ulixem,
- [4] 699 Egreditur sociumque sibi delegit Ulixem,
  - Ulixem (ULIXES; ウリクセス): Ulixem:ディオメデスはウリクセスを自らの仲間に選ぶ
- [6] 699 egreditur sociumque sibi delegit Vlixem,
  - Vlixem (Vlixes; ウリクセス): -xem 699

700 qui secum tacitae sublustri noctis in umbra
- [2] 702 Qui secum tacito sublustri noctis in umbra
  - … Virg. Aen. IX, 373: « sublustri noctis in umbra »。
- [3] 700 Qui secum tutae sublustri noctis in umbra
- [4] 700 Qui secum tacitae sublustri noctis in umbra
- [6] 700 qui secum tacitae sublustri noctis in umbra
  - sublustri … (ウェルギリウス『アエネーイス』9, 373 を参照) …

701 scrutetur studio quae sit fiducia Troum
- [2] 703 Scrutetur studio, quae sit fiducia Troum,
- [3] 701 Scrutetur studio, quae sit fiducia Troum
- [4] 701 Scrutetur studio, quae sit fiducia Troum
  - Troum (TROJANI; トロイア人): — トロイア人の自信がどのようなものか
- [6] 701 scrutetur studio, quae sit fiducia Troum
  - Troum (Tros; トロイア人): Troum 102. 281. 339. 357. 438. 631. 641. 701. 963

702 quidue agitent quantasue parent in proelia uires.
- [2] 704 Quidve agitent, quantasve parent in praelia vires.
- [3] 702 Quidue agitent quantasue parent in praelia uires.
- [4] 702 Quidve agitent quantasve parent in proelia vires.
- [6] 702 quidve agitent quantasve parent in proelia vires.

703 Dumque iter horrendum loca pernoctata pauentes
- [2] 705 Dumque iter horrendum loca per secreta vagantes
- [3] 703 Dumque iter horrendum loca per `non nota pauentes
- [4] 703 Dumque iter horrendum loca per non tuta paventes
- [6] 703 dumque iter horrendum loca pernoctata paventes

704 carpebant, uenit ecce Dolon, quem Troia pubes
- [2] 706 Carpebant, venit ecce Dolon, quem Troica pubes
- [3] 704 Carpebant, uenit ecce Dolon, quem Troia pubes
- [4] 704 Carpebant, venit ecce Dolon, quem Troia pubes
  - Dolon (DOLON; ドロン): 夜にディオメデスとウリクセスに出会う
  - Troia (TROJANI; トロイア人): Troia pubes:トロイアの若者たちは、ギリシア人の力を偵察させるためにドロンを送っていた
- [6] 704 carpebant, venit ecce Dolon, quem Troia pubes
  - Dolon (Dolon; ドロン): *Dolon 704
  - Troia (Troius; トロイアの): Troia pubes 704

705 miserat, ut Danaum sollerti pectore uires
- [2] 707 Miserat, ut Danaum solerti pectore vires
- [3] 705 Miserat, ut Danaum sollerti pectore uires
- [4] 705 Miserat, ut Danaum sollerti pectore vires
  - Danaum (GRAI; ギリシア人): — 力
- [6] 705 miserat, ut Danaum sollerti pectore vires
  - Danaum (Danai; ダナオイ): -um(属格):19. 50. 67. 124. 153. 251. 268. 357. 389. 496. 631. 686. 691. 698. 705. 743. 747. 794. 1025

706 perspiceret sensusque ducum plebisque referret.
- [2] 708 Perspicerel, sensusque ducum plebisque referret.
  - … ――バルトの注記（2808 頁）によれば、*sensus* とは計画・思慮（*consilia*）、判断力（*judicium*）のことである。クラウディアヌスにおいてもしばしば同様であり、例えば de III Cons. Honor. 187: « non corrumpentia sensus Dona valent »。同 de IV Cons. Hon. 300: « nec sic inflectere sensus Humanos edicta valent, ut vita regentis ». 同 de Laud. Stilich. III, 10: « magnanimum pectus, quo frena reguntur Imperii, cujus libratur sensibus orbis »。
- [3] 706 Perspiceret sensusque ducum plebisque referret.
- [4] 706 Perspiceret sensusque ducum plebisque referret.
- [6] 706 perspiceret sensusque ducum plebisque referret.

707 Quem procul ut uidit socius Diomedis Vlixes,
- [2] 709 Quem procul ut vidit socius Diomedis Ulysses,
- [3] 707 Quem procul ut uidit socius Diomedis Ulixes,
- [4] 707 Quem procul ut vidit socius Diomedis Ulixes,
  - Diomedis (DIOMEDES; ディオメデス): Diomedis socius:ディオメデスの仲間、ウリクセス
  - Ulixes (ULIXES; ウリクセス): — ドロンを見つける
- [6] 707 quem procul ut vidit socius Diomedis Vlixes,
  - Diomedis (Diomedes; ディオメデス): socius Diomedis 707
  - Vlixes (Vlixes; ウリクセス): Vlixes 707

708 abdiderant occultantes sua corpora furtim
- [2] 710 Abdiderunt occultantcs sua corpora furtim
- [3] 708 Abdiderunt occultantes sua corpora furtim
- [4] 708 Abdiderunt occultantes sua corpora furtim
- [6] 708 abdiderant occultantes sua corpora furtim

709 post densos frutices, dum spe percussus inani
- [2] 711 Post densos frutices, durn spe percussus inani
  - … 最も適切なのは、流布本および G. 2 に見出される *spe percussus inani*（空しい希望に打たれて）である。キケロも同様に述べている（Tusc. V, 11: « quodcumque nostros animos probabilitate percussit, id dicimus »）。――しかし私には、人が希望に打たれる（*spe percuti*）と言われうるとはほとんど思われない。パリ編者。
- [3] 709 Post densos frutices, dum spe percussus inani
- [4] 709 Post densos fructices, dum spe percussus inani
- [6] 709 post densos frutices, dum spe percussus inani

710 Tros Eumediades cursu praecederet illos,
- [2] 712 Tros Eumedides cursu praecederet illos,
  - … これはエウメデスの子ドロンを指し、Hom. Il. X, 314 および Virg. Aen. XII, 346 の双方から取られたものである。…
- [3] 710 Tros Eumediades cursu praecederet illos,
- [4] 710 Tros Eumediades cursu praecederet illos,
  - … Eumedides シュラーダー（『イリアス』X, 314）。
  - Eumediades (DOLON; ドロン): Tros Eumediades:エウメデスの子なるトロイア人が走って彼らより先を行く
- [6] 710 Tros Eumediades cursu praecederet illos,
  - Eumediades (Eumediades; エウメディアデス): Tros *Eumediades 710:ドロン
  - Tros (Tros; トロイア人): Tros (troius trad.) Eumediades、ドロン:710

711 ne facile oppressus gressum in sua castra referret.
- [2] 713 Ne facile, oppressus, gressum in sua castra referret
- [3] 711 Ne facile oppressus gressum in sua castra referret.
- [4] 711 Ne facile oppressus gressum in sua castra referret.
- [6] 711 ne facile oppressus gressum in sua castra referret.

712 Post, ubi transierat fidens animoque manuque,
- [2] 714 Post ubi transierat fidens animoque mauuque,
  - *Fidens animo*（心に確信を抱いて）。ウェルギリウスの表現、Aen. II, 61。
- [3] 712 Post ubi transierat fidens animoque manuque,
- [4] 712 Post ubi transierat fidens animoque manuque,
- [6] 712 post ubi transierat fidens animoque manuque,
  - fidens … ウェルギリウス『アエネーイス』2, 61 を参照

713 prosiluere uiri iuuenemque euadere cursu
- [2] 715 Prosiluere viri, juveuemque evadere cursu
- [3] 713 Prosiluere uiri iuuenemque euadere cursu
- [4] 713 Prosiluere viri juvenemque evadere cursu
- [6] 713 prosiluere viri iuvenemque evadere cursu

714 conantem capiunt ferroque manuque minantur.
- [2] 716 Conantem capiunt, ferroque manuque minantur
- [3] 714 Conantem capiunt ferroque manuque minantur.
- [4] 714 Conantem capiunt ferroque manuque minantur.
- [6] 714 conantem capiunt ferroque manuque minantur.

715 Ille timore pauens: "Vitam concedite" - dixit -,
- [2] 717 Ille timore pavens, ccYitam concedite, dixit,
- [3] 715 Ille timore pauens 'uitam concedite' dixit:
- [4] 715 Ille, timore pavens, « Vitam concedite » dixit
- [6] 715 ille timore pavens 'vitam concedite' dixit,

716 "hoc unum satis est; quodsi perstatis in ira,
- [2] 718 Hoc unum satis est : quod si perstatis in ira,
  - *Perstatis in ira*（汝らは怒りに固執する）。Ovidius, Pont. I, 4, 44: « Perstiterit laesi si gravis ira Dei »。
- [3] 716 'Hoc unum satis est; quodsin perstatis in ira,
- [4] 716 « Hoc unum satis est; quodsi perstatis in ira,
- [6] 716 'hoc unum satis est; quod si perstatis in ira,

717 quanta ex morte mea capietis praemia laudis?
- [2] 719 Quanta ex morte mea capietis praemia laudis?
- [3] 717 Quanta ex morte mea capietis praemia laudis?
- [4] 717 Quanta ex morte mea capietis praemia laudis ?
- [6] 717 quanta ex morte mea capietis praemia laudis?

718 At si cur ueniam tacitis exquiritis umbris:
- [2] 720 At si, cur veniam tacitis, exquiritis, umbris,
- [3] 718 At si cur ueniam tacitis exquiritis umbris:
- [4] 718 At si cur veniam tacitis exquiritis umbris :
- [6] 718 at si cur veniam tacitis exquiritis umbris:

719 maxima Troia mihi currum promisit Achillis
- [2] 721 Maxima Troja mihi currum promisit Achillis,
  - … このことをドロン自身がホメロスの Iliad. X, 392 でウリクセスに語っている。Virg. Aen. XII, 349 にドロンについて次のようにある: « Qui quondam, castra ut Danaum speculator adiret, Ausus Pelidae pretium sibi poscere currus »。Ovid. in Ib. 629: « Qualis equos pacto, quos fortis agebat Achilles, Acta Phrygi timido est, nox tibi talis eat »。『ラテン詩選』(*Anthol. Lat.*) I, 95 のドロンに関するエピグラム: « Praemia magna Dolon, currum dum poscit Achillis, Prodidit ipse cadens munera magna Dolon »。
- [3] 719 Maxima Troia mihi currum promisit Achillis,
- [4] 719 Maxima Troja mihi currum promisit Achillis,
  - Achillis (ACHILLES; アキレウス): — ドロンは、アキレウスの戦車がトロイア人から自分に約束されたと語る
  - Troja (TROJA; トロイア): — 最も偉大な都、ドロンにアキレウスの戦車を約束していた
- [6] 719 maxima Troia mihi currum promisit Achillis,
  - Achillis (Achilles; アキレウス): -is 54. 689. 719. 806
  - Troia (Troia; トロイア): maxima -ia 719

720 si uestras cepisset opes. Haec dona secutus
- [2] 722 Si vestras cepisset opes : haec dona sequutus
- [3] 720 Si uestras cepisset opes. haec dona secutus
- [4] 720 Si vestras cepisset opes. Haec dona secutus
- [6] 720 si vestras cepisset opes. haec dona secutus

721 in dubios casus, coram quod cernitis ipsi,
- [2] 723 In dubios casus, coram quos cernitis ipsi,
- [3] 721 In dubios casus, coram quod cernitis ipsi,
- [4] 721 In dubios casus, coram quod cernitis ipsi,
- [6] 721 in dubios casus, coram quod cernitis ipsi,

722 infelix cecidi. Nunc uos per numina diuum,
- [2] 724 Infelix cecidi : nunc vos per numina Divum,
- [3] 722 Infelix cecidi. nunc uos per numina diuum,
- [4] 722 Infelix cecidi. Nunc vos per numina divum,
- [6] 722 infelix cecidi. nunc vos per numina divum,

723 per mare, per Ditis fluctus obtestor opaci,
- [2] 725 Per mare, per Ditis fluctus obtestor opaci,
  - *Per Ditis fluctus*（ディスの波にかけて）、ステュクスにかけて、あるいは冥府の河川にかけて。オウィディウスの Met. I, 187 でユピテルが誓っているのと同様である。Virg. Cul. 371 では « Lacus Ditis opacos » と言われている。これは嘆願の定型句であり、Ovid. Trist. II, 53 の誓約の句 « Per mare, per terras, per tertia numina juro » と同類のものである。
- [3] 723 Per mare, per Ditis fluctus obtestor opaci,
- [4] 723 Per mare, per Ditis fluctus obtestor opaci,
  - Ditis (DIS; ディス): per Ditis opaci fluctus:暗きディスの波にかけて(ドロンが嘆願者として語る)
- [6] 723 per mare, per Ditis fluctus obtestor opaci,
  - Ditis (Dis; ディス): per Ditis fluctus obtestor opaci 723

724 ne rapere hanc animam crudeli caede uelitis.
- [2] 726 Ne rapere hanc animam crudeli caede velitis.
  - *Ne rapere hanc*（これを奪い去らぬように）。オウィディウスは Met. VI, 540 で « eripere animam »（命を奪う）と言っている。
- [3] 724 Ne rapere hanc animam crudeli caede uelitis.
- [4] 724 Ne rapere hanc animam crudeli caede velitis.
- [6] 724 ne rapere hanc animam crudeli caede velitis.

725 Haec pro concessa referetis dona salute:
- [2] 727 Haec pro concessa referetis dona salute,
- [3] 725 Haec pro concessa referetis dona salute:
- [4] 725 Haec pro concessa referetis dona salute :
- [6] 725 haec pro concessa referetis dona salute:

726 consilium Priami regis remque ordine gentis
- [2] 728 G)nsilium Priami regis, remque ordine gentis
- [3] 726 Consilium Priami totam remque ordine gentis
- [4] 726 Consilium Priami remque omnem ex ordine gentis
  - Priami (PRIAMUS; プリアモス): Priami:プリアモスの計画を明かそう(ドロンが語る)
  - Phrygiae (TROJANI; トロイア人): Phrygia gens Phrygiae gentis:プリュギアの民の事情をすべて明かそう(ドロンが語る)
- [6] 726 consilium Priami regis remque ordine gentis
  - Priami (Priamus; プリアモス): -mi regis 726

727 expediam Phrygiae." Postquam quid Troia pararet
- [2] 729 Expediam Phrygiae ». Postquam quid Troja pararet
  - … バルトは『雑考』(*Adv.*) LVIII, 14, p. 2752 で、トロイアの首領たちの代わりに *Troja* と言うのはあまり美しくないと述べている。しかしながら、これらの語はオウィディウスの Met. XIII, 244 から借用されたものであり、そこではウリクセスが同じ出来事を次のように詳述している: « Ausum eadem, quae nos, Phrygia de gente Dolona Interimo; non ante tamen, quam cuncta coegi Prodere, et edidici, quid perfida Troja pararet. Omnia cognoram »。
- [3] 727 Expediam Phrygiae'. postquam quid Troia pararet
- [4] 727 Expediam Phrygiae ». Postquam quid Troja pararet
  - Troja (TROJA; トロイア): — トロイアが何を準備していたか
- [6] 727 expediam Phrygiae'. postquam quid Troia pararet
  - Phrygiae (Phrygius; プリュギアの): gentis . . . Phrygiae 727
  - Troia (Troia; トロイア): Troia 727. 1016

728 cognouere uiri, fauces mucrone recluso
- [2] 730 G)gnovere viri, fauces mucrone reclusas
  - … というのも、私は *fauces mucrone reclusas*（あるいは *revulsas*）*detrudunt* という言い回しが、ドロンの首が喉を切り裂かれて胴体から切り落とされたことを意味すると考えるからである。ホメロスが彼が斬首された次第を伝えている通りである（Iliad. X, 455 以下）。――同様にユウェナリスは Sat. IV で *jugulos aperire*（喉を切り開く）と言った。また Horat. Epod. XVII, 71: « Modo ense pectus Norico recludere »。パリ編者。…
- [3] 728 Cognouere uiri, fauces mucrone recluso
- [4] 728 Cognovere viri, fauces mucrone recluso
- [6] 728 cognovere viri, fauces mucrone recluso

729 detrudunt iuuenis. Post haec tentoria Rhesi
- [2] 731 Detrudunt juvenis. Post haec tentoria Rhesi
  - … ――また動詞 *Detrudunt* は Virg. Aen. IX, 496 から繰り返されたものと思われる: « tuo-
  - **(cont.)** （前頁からの続き）-que Invisum hoc detrude caput sub Tartara telo »。パリ編者。…
- [3] 729 Pertundunt iuueni: post haec tentoria Rhesi
- [4] 729 Diffindunt juveni : post haec tentoria Rhesi
  - Rhesi (RHESUS; レソス): Rhesi:ウリクセスとディオメデスがレソスの天幕を奪い、彼を殺す
- [6] 729 † detrudunt iuvenis: post haec tentoria Rhesi
  - Rhesi (Rhesus; レソス): tentoria Rhesi 729

730 intrant atque ipsum somno uinoque sepultum
- [2] 732 Intravit , atque ipsum somno vinoque sepultum
- [3] 730 Intrant atque ipsum somno uinoque sepultum
- [4] 730 Intrant atque ipsum somno vinoque sepultum
- [6] 730 intrant atque ipsum somno vinoque sepultum

731 obtruncant spoliantque uirum fusosque per herbam
- [2] 733 Obtruncant, spoliantque viros, fusosque per herbam
- [3] 731 Obtruncant spoliantque armis fusosque per herbam
- [4] 731 Obtruncant, spoliantque virum, fusosque per herbam
- [6] 731 obtruncant spoliantque virum fusosque per herbam
  - virum (Rhesus; レソス): ipsum . . . virum 731 を参照

732 exanimant socios. Tum tristi caede peracta
- [2] 734 Exaniinant socios : tam tristi caede peracta
  - *Exanimant* が能動態の形で、刃物で切り殺す・殺害するという意味で用いられるのは、より優れた著述家たちの間では極めて稀であると私は考える。…
- [3] 732 Exanimant socios; tum tristi caede peracta
- [4] 732 Exanimant socios; tristi tum caede peracta
- [6] 732 exanimant socios; tum tristi caede peracta

733 praeda umeros onerant, multo et candore nitentes
- [2] 735 Praeda humeros onerant, multo candore nitentes
  - *Candore nitentes*（白さに輝く）。同様に Virg. Aen. XII, 84: « Qui candore nives anteirent, cursibus auras »。
- [3] 733 Praeda umeros onerant, multo candore nitentes
- [4] 733 Praeda umeros onerant, multo candore nitentes
- [6] 733 praeda umeros onerant, multo et candore nitentes

733a
- [2] [736] [Rhesi ventigenas secum adduxere jugales]
- [3] —
- [4] —
- [6] —

734 Thracas equos rapiunt, quos nec praecederet Eurus
- [2] 737 Thracis equos rapiunt, quos nec prsecederet Eurus,
  - … 詩人たちは俊足をとりわけ東風（エウルス）に比べるのが常だからである。Virg. Aen. VIII, 223 および Horat. Carm. II, 16, 24 を見よ。また学者たちは Virg. I, 317 において *Hebrus* の代わりに *Eurus* を置くことを欲している。…
- [3] 734 Thracas equos rapiunt, quos nec praecederet Eurus
- [4] 734 Thracas equos rapiunt, quos nec praecederet Eurus
  - Eurus (EURUS; エウルス): レソスの馬より先を行くことはないであろう
  - Thracas (THRAX; トラキアの): 形容詞:Thracas equos、トラキアの馬
- [6] 734 Thraecis equos rapiunt, quos nec praecederet Eurus
  - … オウィディウス『変身物語』9, 194 を参照 …
  - Eurus (Eurus; エウルス): Eurus 734:風
  - Thraecis (Rhesus; レソス): Thraecis 734
  - Thraecis (Thraex; トラキアの): Thraecis (-es trad.; -ăs 推測) equos 734:レソスの

735 nec posset uolucri cursu superare sagitta.
- [2] 738 Nec posset volucri cursu superare sagitta.
  - … 同様に Virgilius, Aen. V, 242: « illa Noto citius volucrique sagitta Ad terram fugit »。
- [3] 735 Nec posset uolucri cursu superare sagitta.
- [4] 735 Nec posset volucri cursu superare sagitta.
- [6] 735 nec posset volucri cursu superare sagitta.

736 Inde iterum Argolicas primae sub tempore lucis
- [2] 739 Inde iterum Argolicas primae sub tempore lucis
- [3] 736 Inde iterum Argolicas primae sub tempore lucis
- [4] 736 Inde iterum Argolicas primae sub tempore lucis
  - Argolicas (ARGOLICUS; アルゴスの): Argolicas classes
- [6] 736 inde iterum Argolicas primae sub tempore lucis
  - Argolicas (Argolicus; アルゴスの): -as . . . classes 736

737 ad classes redeunt, quos Nestoris accipit aetas
- [2] 740 Ad classes redeunt, quos Nestoris accipit setas,
  - *Nestoris accipit aetas*（ネストルの齢が受け入れる）、すなわち、老いたネストルが彼らの到着を真っ先に察知し、喜んで迎えるということである。これはホメロス X, 532 から理解できる。別の箇所、131 行において、われらの詩人は助言を与えることが話題となっている文脈で抽象表現 *prudentia Nestoris*（ネストルの思慮）を用いているが、ここでは老齢そのもののみを考慮して *aetas Nestoris*（ネストルの齢）という言葉を用いている。なぜなら、若者たちの徳と善-
  - **(cont.)** （前頁からの続き）-行を見守り、称賛することは、とりわけ老人たちに相応しいからである。
- [3] 737 Ad classes redeunt, quos Nestoris excipit aetas
- [4] 737 Ad classes redeunt, quos Nestoris excipit aetas
  - Nestoris (NESTOR; ネストル): — 彼の老いが、ドロンを殺して陣営に戻るディオメデスとウリクセスを迎える
- [6] 737 ad classes redeunt; quos Nestoris accipit aetas
  - accipit (すなわち聞く) …
  - Nestoris (Nestor; ネストル): -oris aetas 154. 737

738 ac recipit portis. Postquam sua castra tenebant,
- [2] 741 Ac recipit portis : postquam sua castra tenebant,
- [3] 738 Ac recipit portis. postquam sua castra tenebant,
- [4] 738 Ac recipit portis. Postquam sua castra tenebant,
- [6] 738 ac recipit portis. postquam sua castra tenebant,

739 facta duci referunt: laudat Pelopeius heros,
- [2] 742 Facta duci referunt; laudat Pelopeius heros,
- [3] 739 Facta duci referunt: laudat Pelopeius heros,
- [4] 739 Facta duci referunt : laudat Pelopeius heros,
  - Pelopeius (AGAMEMNON; アガメムノン): — ウリクセスとディオメデスの武勇を称える
- [6] 739 facta duci referunt: laudat Pelopeius heros,
  - duci (Agamemnon; アガメムノン): dux 134. 156. 739
  - Pelopeius (Pelopeius; ペロプス家の): Pelopeius heros 131. 739:アガメムノン

740 fessaque iucundae tradunt sua membra quieti.
- [2] 743 Fessaque jucundae tradunt sua membra quieti.
- [3] 740 Fessaque iocundae tradunt sua membra quieti.
- [4] 740 Fessaque jocundae tradunt sua membra quieti.
- [6] 740 fessaque iucundae tradunt sua membra quieti.

## Book 11

741 Lux exorta uiros in pristina bella remisit,
- [2] 744 XI. Lux exorta viros in pristina bella remisit,
- [3] 741 Lux exorta uiros in pristina bella remisit,
- [4] 741 Lux exorta viros in pristina bella remisit,
- [6] 741 lux exorta viros in pristina bella remisit,

742 instaurantque animos recreato milite pugnae
- [2] 745 Instaurantque animos recreato milite pugnae
- [3] 742 Instaurantque animos recreato milite pugnae
- [4] 742 Instaurantque animos recreato milite pugnae
- [6] 742 instaurantque animos recreato milite pugnae

743 Dardanidum Danaumque duces: uolat undique nubes
- [2] 746 Dardanidum Danaumque duces : volat undique nubes
  - … ――*Nubem telorum*（投槍の雲）という表現は、私の記憶が正しければ、マロー（ウェルギリウス）は事前の直喩による場合（Aen. XI［正しくは X］, 808: « sic obrutus undique telis Aeneas nubem belli, dum detonet, omnem Sustinet »）を除いて用いていない。――しかしマリウス・ウィクトルは carm. ad Salmon. 16 行で *densam telorum nubem* と言っている。本著作集第2巻…を見よ。
- [3] 743 Dardanidum Danaumque duces: uolat undique nubes
- [4] 743 Dardanidum Danaumque duces : volat undique nubes
  - Danaum (GRAI; ギリシア人): — 将たち
  - Dardanidum (TROJANI; トロイア人): Dardanidae Dardanidum duces:ダルダニデスたちの将たち
- [6] 743 Dardanidum Danaumque duces: volat undique nubes
  - Danaum (Danai; ダナオイ): -um(属格):19. 50. 67. 124. 153. 251. 268. 357. 389. 496. 631. 686. 691. 698. 705. 743. 747. 794. 1025
  - Dardanidum (Dardanides; ダルダニデス): -dum . . . duces 743:トロイア人の

744 telorum et ferro ferrum sonat, undique mixtis
- [2] 747 Telorum , et ferro ferrum sonat : undique mixtis
- [3] 744 Telorum et ferro ferrum sonat, undique flictu
  - … et ferrum から 746 の acies までの語句を『ベレンガリウスの事績』II 272–74 が有する …
- [4] 744 Telorum, ferro ferrum sonat, undique mixtis
- [6] 744 telorum et ferro ferrum sonat, undique mixtis
  - （証言） *ferrum* — 746 *acies* = 『ベレンガリウスの事績』2, 272–4 (745 *stridunt*)

745 inter se strident mucronibus: instat utrimque
- [2] 748 Inter se strident mucronibus, instat utriroque
- [3] 745 Inter se strident mucrones: instat utrimque
- [4] 745 Inter se strident mucronibus : instat utrimque
- [6] 745 inter se strident mucronibus: instat utrimque

746 densa acies mixtusque fluit cum sanguine sudor.
- [2] 749 Densa acies, mixtusque fluit cum sanguine sudor.
- [3] 746 Densa acies, mixtusque fluit cum sanguine sudor.
- [4] 746 Densa acies, mixtusque fluit cum sanguine sudor.
- [6] 746 densa acies mixtusque fluit cum sanguine sudor.

747 Tandem feruenti Danaum rex concitus ira
- [2] 750 Tandem ferventi Danaum rex concitus ira
- [3] 747 Tandem feruenti Danaum rex concitus ira
- [4] 747 Tandem ferventi Danaum rex concitus ira
  - Danaum (AGAMEMNON; アガメムノン): — アンティポスを傷つける
  - Danaum (GRAI; ギリシア人): — 王(アガメムノン)
- [6] 747 tandem ferventi Danaum rex concitus ira
  - rex (Agamemnon; アガメムノン): Danaum rex 747
  - Danaum (Danai; ダナオイ): -um(属格):19. 50. 67. 124. 153. 251. 268. 357. 389. 496. 631. 686. 691. 698. 705. 743. 747. 794. 1025

748 Antiphon ingenti prostratum uulnere fundit
- [2] 751 Antiphonem iagenti prostratum vulnere fundit,
  - … ホメロス（Il. XI, 101）では、プリアモスの息子たちであるアンティポスとイソスがアガメムノンによって討ち取られたと私は読んでいる。われらのホメロス詩人が彼を指そうとしたのか、それとも別人なのか、私には依然として疑わしい。…
- [3] 748 Antiphon ingenti prostratum uulnere fudit
- [4] 748 Antiphon ingenti prostratum vulnere fudit
  - Antiphon (ANTIPHUS Priami filius; アンティポス、プリアモスの子): Antiphon:アガメムノンが彼を傷つける
- [6] 748 Antiphon ingenti prostratum vulnere fudit
  - Antiphon (Antiphus 3; アンティポス 3): -ŏn 748:プリアモスの子

749 Pisandrumque simul fratremque ad bella ruentem
- [2] 752 Pisandrumque simul , fratremque ad bella ruentem
  - … ホメロスの Iliad. XI, 122 行に基づき *Pisandrum* および *Hippolochum* を置くべきであることは明白であり、…
- [3] 749 Pisandrumque simul fratremque ad bella ruentem
- [4] 749 Pisandrumque simul fratremque ad bella ruentem
  - **749, 750** Pisandrum, Hippolochum …（『イーリアス』XI, 122）。
  - Hippolochum (HIPPOLOCHUS; ヒッポロコス): Hippolochum:アガメムノンは戦いへ突進するヒッポロコスを斬り殺す
  - Pisandrum (PISANDER; ペイサンドロス): Pisandrum:アガメムノンがペイサンドロスを斬り殺す
- [6] 749 Pisandrumque simul fratremque ad bella ruentem
  - Pisandrum (Pisander; ペイサンドロス): *Pisandrum (tess- trad.) 749:アンティマコスの子

750 Hippolochum; post hos gladio petit Iphidamanta.
- [2] 753 Hippolochum , post hos gladio petit Iphidamanta :
  - … ホメロスの Iliad. XI, 221 に基づき、アンテノルの息子 *Iphidamanta* をここに復元すべきである…。
- [3] 750 Hippolochum; post hos gladio petit Iphidamanta.
- [4] 750 Hippolochum ; post hos gladio petit Iphidamanta.
  - Iphidamanta (IPHIDAMAS; イピダマス): Iphidamanta:アガメムノンがイピダマスを殺す
- [6] 750 Hippolochum; post hos gladio petit Iphidamanta.
  - Hippolochum (Hippolochus; ヒッポロコス): Pisandrum . . . fratremque . . . *Hippolochum 750:アンティマコスの子ら
  - Iphidamanta (Iphidamas; イピダマス): *Iphidamanta (amphi- trad.) 750:アンテノルの子

751 Hic frater dextram iaculo ferit; ille dolore
- [2] 754 Hinc frater regis dextram ferit , ille dolore
  - … ホメロスの記述（Iliad. XI, 231 以下）によれば、事の次第は次のよう
  - **(cont.)** （前頁からの続き）―であった。アガメムノンがイピダマスを討ち取った後、その兄コオンは弟の死を激しく悲しみ、折しもアガメムノンの傍らに立っていたが、槍でアガメムノンの腕の真ん中を突いた。しかし弟の遺体を引きずり出そうとしていたコオンを、間もなくアガメムノンは討ち取った。…というのも、付け加えられた *gladio*（剣で）は余計であり、槍で突いたと記すホメロスに反しているからである。
- [3] 751 Hic regis dextram frater ferit; ille dolore
- [4] 751 Hic regis dextram frater ferit; ille dolore
- [6] 751 hic frater dextram iaculo ferit; ille dolore
  - frater (Coon; コオン): (Coon)、アンテノルの子:frater 751

752 acrior accepto fugientem Antenore natum
- [2] 755 Acrior acoepto fugientem Antenore natum
  - *Antenore natum*（アンテノルの子）。すなわちイピダマスの兄コオンのこと。
- [3] 752 Acrior accepto fugientem Antenore natum
- [4] 752 Acrior accepto fugientem Antenore natum
  - Antenore (ANTENOR; アンテノル): — アガメムノンはその息子(コオン)を追って傷つける
- [6] 752 acrior accepto fugientem Antenore natum
  - Antenore (Antenor 2; アンテノル 2): Antenore natum 752:トラキア人コオン

753 persequitur traxitque ferox cum uulnere poenas.
- [2] 756 Persequitur, traxitque ferox cum vulnere pccnas.
  - *Traxitque ferox cum vulnere poenas*。すなわち、アガメムノンは傷を負っていたにもかかわらず、猛々しくコオンに対する復讐を続け、あるいは科し進めたということである。ヘルムシュテット写本（H.）は *Traxit ... graves cum sanguine poenas* とする。彼はこの言い回しをウェルギリウスの Aen. V, 785: « Non media de gente Phrygum exedisse nefandis Urbem odiis satis est, poenam traxisse per omnes Relliquias » から取ったと思われる。
- [3] 753 Persequitur traxitque ferox cum uulnere poenas.
- [4] 753 Persequitur traxitque ferox cum vulnere poenas.
- [6] 753 persequitur traxitque ferox cum vulnere poenas.

754 Hector tunc pugnae subit acri concitus ira
- [2] 757 Hector tunc pugnae subit acri concitus ira
- [3] 754 Hector tum pugnae subit acri concitus ira
- [4] 754 Hector tum pugnae subit acri concitus ira
  - Hector (HECTOR; ヘクトル): — プリアモスの子、怒って激しい戦いに入る
- [6] 754 Hector tum pugnae subit acri concitus ira
  - Hector (Hector; ヘクトル): -or . . . Priamides 754
  - Priamides (Priamides; プリアミデス): Hector -es 754:ヘクトル

755 Priamides et percussos agit undique Graios;
- [2] 758 Priamides, mox perculsos agit undique Graios,
- [3] 755 Priamides et percussos agit undique Graios;
- [4] 755 Priamides et percussos agit undique Grajos;
  - Grajos (GRAI; ギリシア人): — ヘクトルはギリシア人を四方から追い立てる
- [6] 755 Priamides et percussos agit undique Graios;
  - Graios (Graius; ギリシアの): Graios 682. 755. 763

756 nec Paris hostiles cessat prosternere turmas
- [2] 759 Nec Paris hostiles cessat prosternere turmas,
- [3] 756 Nec Paris hostiles cessat prosternere turmas
- [4] 756 Nec Paris hostiles cessat prosternere turmas
  - Paris (PARIS; パリス): — 敵の部隊を打ち倒す
- [6] 756 nec Paris hostiles cessat prosternere turmas
  - Paris (Paris; パリス): Paris 576. 756

757 Eurypylique femur contento uulnerat arcu.
- [2] 760 Eurypylique femur contento vulnerat arcu.
- [3] 757 Eurypylique femur contento uulnerat arcu.
- [4] 757 Eurypylique femur contento vulnerat arcu.
  - Eurypyli (EURYPYLUS; エウリュピュロス): Eurypyli:パリスがエウリュピュロスの腿を傷つける
- [6] 757 Eurypylique femur contento vulnerat arcu.
  - Eurypyli (Eurypylus; エウリュピュロス): -li 757

## Book 12

758 Incumbunt Troes, fugiunt in castra Pelasgi
- [2] 761 XII. Incumbunt Troes, fugiunt in castra Pelasgi
- [3] 758 Incumbunt Troes, fugiunt in castra Pelasgi
- [4] 758 Incumbunt Troes, fugiunt in castra Pelasgi
  - Pelasgi (GRAI; ギリシア人): Pelasgi 主格:陣営に逃げ込む
  - Troes (TROJANI; トロイア人): Troes:トロイア人が押し寄せ、ギリシア人が逃げる
- [6] 758 incumbunt Troes, fugiunt in castra Pelasgi
  - Pelasgi (Pelasgi; ペラスゴイ): Pelasgi 758. 769
  - Troes (Tros; トロイア人): Troes 758. 767. 928. 978. 1002、いずれも子音の前または最後の不定の位置で

759 uiribus exhaustis et uastis undique firmant
- [2] 762 Yiribus exhaustis, et vastis undique firmant
  - *Firmant Obicibus*（閂で固める）。上の 683 行の « portas objecto robore firmant » と同様。
- [3] 759 Uiribus exhaustis et uastis undique firmant
- [4] 759 Viribus exhaustis et vastis undique firmant
- [6] 759 viribus exhaustis et vastis undique firmant

760 obicibus muros. Tum saxo Martius Hector
- [2] 763 Obicibus muros ; tum saxo Martius Hector
  - … バルトは『テーバイド』第1行への注記において、この行と次の行で、作者が文字 a と r を頻繁に結びつけることによって、恐ろしい事象にふさわしい音の粗々しさを意図したと指摘している。
- [3] 760 Obicibus muros, tum saxo Martius Hector
- [4] 760 Obicibus muros. Tum saxo Martius Hector
  - Hector (HECTOR; ヘクトル): — 好戦的なヘクトルが石で敵陣の門を打ち破る
- [6] 760 obicibus muros; tum saxo Martius Hector
  - Hector (Hector; ヘクトル): Martius -or 760
  - Martius (Martius; 好戦的な): Martius Hector 760

761 perfringit portas ferrataque robora laxat.
- [2] 764 Perfringit portas, ferrataque robora laxat.
- [3] 761 Perfringit portas ferrataque robora laxat.
- [4] 761 Perfringit portas ferrataque robora laxat.
- [6] 761 perfringit portas ferrataque robora laxat.

762 Irrumpunt aditus Phryges atque in limine primo
- [2] 765 Irrumpunt aditus Phryges, atque in limine primo
- [3] 762 Inrumpunt aditus Phryges atque in limine primo
- [4] 762 Irrumpunt aditus Phryges atque in limine primo
  - Phryges (TROJANI; トロイア人): — 敵陣の入口に突入する
- [6] 762 inrumpunt aditus Phryges atque in limine primo
  - Phryges (Phryges; プリュギア人): Phryges 401. 493. 636. 682. 762. 803

763 restantes sternunt Graios ualloque cateruas
- [2] 766 Restantes sternunt Graios, valloque catervas
- [3] 763 Restantes sternunt Graios ualloque cateruas
- [4] 763 Restantes sternunt Grajos valloque catervas
  - Grajos (GRAI; ギリシア人): — トロイア人はギリシア人を打ち倒す
- [6] 763 restantes sternunt Graios valloque catervas
  - Graios (Graius; ギリシアの): Graios 682. 755. 763

764 deturbant, alii scalas in moenia poscunt
- [2] 767 Deturbant, alii scalas in moenia ponunt,
- [3] 764 Deturbant, alii scalas in moenia poscunt
- [4] 764 Deturbant, alti scalas in moenia poscunt
- [6] 764 deturbant, alii scalas in moenia poscunt

765 et iaciunt ignes: auget uictoria uires.
- [2] 768 Et jaciunt ignes : prsebet victoria vires.
- [3] 765 Et iaciunt ignes: praebet uictoria uires.
- [4] 765 Et jaciunt ignes : praebet victoria vires.
- [6] 765 et iaciunt ignes: auget victoria vires.

766 De muris pugnant Danai turresque per altas.
- [2] 769 De muris pugnant Danai, turresque per altas
- [3] 766 De muris pugnant Danai turresque per altas
- [4] 766 De muris pugnant Danai turresque per altas
  - Danai (GRAI; ギリシア人): — 城壁から戦う
- [6] 766 de muris pugnant Danai † puppesque per altas:
  - Danai (Danai; ダナオイ): Danai 508. 542. 646. 679. 766. 802. 838. 960. 978. 1002

767 Saxa uolant, subeunt acta testudine Troes
- [2] 770 Saxa volant; subeunt acta testudine Troes,
  - … 実にウェルギリウスの模倣もこれを示唆している。Aen. II, 441: « obsessumque acta testudine limen »；また IX, 505: « Accelerant acta pariter testudine Volsci »。
- [3] 767 Saxa uolant, subeunt acta testudine Troes
- [4] 767 Saxa volant, subeunt acta testudine Troes
  - Troes (TROJANI; トロイア人): — 亀甲隊形を組んで進む
- [6] 767 saxa volant, subeunt acta testudine Troes
  - acta … (ウェルギリウス『アエネーイス』2, 441; 9, 505 より) …
  - Troes (Tros; トロイア人): Troes 758. 767. 928. 978. 1002、いずれも子音の前または最後の不定の位置で

768 ascenduntque aditus et portis uiribus instant.
- [2] 771 Ascenduntque aditus , et totis viribus instant.
- [3] 768 Ascenduntque aditus et totis uiribus instant.
- [4] 768 Ascenduntque aditus et totis viribus instant.
- [6] 768 ascenduntque aditus et postes viribus intrant.

769 Turbati fugiunt omnes iam castra Pelasgi
- [2] 772 Turbati fugiunt linquentes castra Pelasgi,
- [3] 769 Turbati fugiunt omnes iam castra Pelasgi
- [4] 769 Turbati fugiunt omnes, en, castra Pelasgi
  - Pelasgi (GRAI; ギリシア人): — 皆混乱して逃げる
- [6] 769 turbati fugiunt omnes † in castra Pelasgi
  - Pelasgi (Pelasgi; ペラスゴイ): Pelasgi 758. 769

770 et scandunt puppes. Vrget Troiana iuuentus
- [2] 773 Et scandunt puppes; urget Trojana juventus ,
- [3] 770 Et scandunt puppes; urguet Troiana iuuentus
- [4] 770 Et scandunt puppes ; urguet Trojana juventus
  - Trojana (TROJANI; トロイア人): — ギリシア人に迫る
- [6] 770 et scandunt puppes; instat Troiana iuventus
  - Troiana (Troianus; トロイアの): Troiana iuventus 542. 770

771 telaque crebra iacit: resonat clamoribus aether.
- [2] 774 Telaque crebra jacit: resonat clamoribus aether.
- [3] 771 Telaque crebra iacit: resonat clamoribus aether.
- [4] 771 Telaque crebra jacit : resonat clamoribus aether.
- [6] 771 telaque crebra iacit: resonat clamoribus aether.

## Book 13

772 Neptunus uires Danais animumque ministrat:
- [2] 775 XIII. Neptunus vires Danais animumque ministrat :
- [3] 772 Neptunus uires Danais animumque ministrat.
- [4] 772 Neptunus vires Danais animumque ministrat.
  - Danais (GRAI; ギリシア人): Danais:ネプトゥヌスがダナオイに力を与える
  - Neptunus (NEPTUNUS; ネプトゥヌス): ギリシア人に勇気と力を与える
- [6] 772 Neptunus vires Danais animumque ministrat:
  - Danais (Danai; ダナオイ): -is 772
  - Neptunus (Neptunus; ネプトゥヌス): Neptunus 772

773 pugna ingens oritur, furit istinc hostis et illinc.
- [2] 776 Pugna ingens oritur; furit istinc hostis et illinc,
- [3] 773 Pugna ingens oritur, furit istinc hostis et illinc,
- [4] 773 Pugna ingens oritur, furit istinc hostis et illinc.
- [6] 773 pugna ingens oritur, furit istinc hostis et illinc.

774 Idomenei dextra cadit Asius; Hector atrocem
- [2] 777 Idoraenei dextra cadit Asius; Hector atrocem
  - … 確かに、ここでアシオスが最初に、ヘクトルによって討たれるアムピマコスよりも前に名指されているが、ホメロスによれば彼が討たれたのはアムピマコスよりずっと後のことである（Iliad. XIII, 384）。また、われらの詩人はこの戦列におけるイドメネウスの武勲を黙殺しているわけではなく、すぐ後にアンキセスの娘婿アルカトオスが彼によって討たれたことを記しており、この討ち取りはアシオスのそれよりも記憶されるべきものであった。…
- [3] 774 Dextraque Idomenei cadit Asius; Hector atrocem
- [4] 774 Idomenei dextra cadit Asius; Hector atrocem
  - Amphimachum (AMPHIMACHUS princeps Epeorum; アムピマコス、エペイオス人の将): Amphimachum:ヘクトルが猛きアムピマコスを斬り倒す
  - Asius (ASIUS Hyrtaci filius; アシオス、ヒュルタコスの子): — イドメネウスの右手に倒れる
  - Hector (HECTOR; ヘクトル): — アムピマコスを斬り倒す
  - Idomenei (IDOMENEUS; イドメネウス): Idomenei:アシオスはイドメネウスの右手に倒れる
- [6] 774 Idomenei dextra cadit Asius; Hector atrocem
  - Asius (Asius; アシオス): Asius 240. 774:ヒュルタコスの子、トロイア側
  - Hector (Hector; ヘクトル): Hector 256. 277. 491. 626. 677. 774. 959. 967. 979. 996. 1051
  - Idomenei (Idomeneus; イドメネウス): -nei dextrā 774

775 Amphimachum obtruncat nec non occumbit in armis
- [2] 778 Amphimachum obtrmrcat; nec non occumbit in armis
- [3] 775 Amphimachum obtruncat, necnon occumbit in armis
- [4] 775 Amphimachum obtruncat, nec non occumbit in armis
- [6] 775 Amphimachum obtruncat nec non occumbit in armis
  - Amphimachum (Amphimachus 1; アムピマコス 1): Hector atrocem -um obtruncat 775

776 Anchisae gener Alcathous, quem fuderat ense
- [2] 779 Anchisae gener Alcathous, quem fnderat ense
  - … ドルピウスとファン・デル・デュッセンはホメロスに基づいてこれに代えて正しく *Alcathous*（アルカトオス）を復元している。…
- [3] 776 Anchisae gener Alcathous, quem fuderat ense
- [4] 776 Anchisae gener Alcathous, quem fuderat ense
  - Alcathous (ALCATHOUS; アルカトオス): アンキセスの婿、殺される
- [6] 776 Anchisae gener Alcathous, quem fuderat ense
  - Alcathous (Alcathous; アルカトオス): Anchisae gener Alcathous 776
  - Anchisae (Anchises; アンキセス): Anchisae gener Alcathous 776

777 magnanimus ductor Rhytieus. Tunc feruidus hasta
- [2] 780 Magnanimus dactor Cretum; tunc fervidas hasta
  - … アルカトオスを討ったイドメネウスは、ホメロスによってクレタ人の指導者と呼ばれている（Il. XIII, 221, 259, 274、その他）。…
- [3] 777 Magnanimus ductor Rhythieus; tum feruidus hasta
- [4] 777 Magnanimus ductor Rhythieus; tum fervidus hasta
  - Rhythieus (IDOMENEUS; イドメネウス): Ductor Rhythieus:心大いなる将リュティエウスがアルカトオスを殺す
- [6] 777 magnanimus ductor Rhytieus; tum fervidus hasta
  - Rhytieus (Rhytieus; リュティエウス): magnanimus ductor Rhytieus 777:イドメネウス

778 Deiphobus ferit Ascalaphum mergitque sub undas.
- [2] 781 Deiphobus ferit Ascalaphum , mergitque sub umbras.
- [3] 778 Deiphobus ferit Ascalaphum mergitque sub umbras.
- [4] 778 Deiphobus ferit Ascalaphum mergitque sub umbras.
  - Ascalaphum (ASCALAPHUS; アスカラポス): Ascalaphum:デイポボスが彼を殺す
  - Deiphobus (DEIPHOBUS; デイポボス): — アスカラポスを斬り殺す
- [6] 778 Deiphobus ferit Ascalaphum mergitque sub umbras.
  - Ascalaphum (Ascalaphus; アスカラポス): -um 778
  - Deiphobus (Deiphobus; デイポボス): fervidus . . . -us 778

## Book 14

779 Hector ubique ferus uiolento pectore saeuit,
- [2] 782 XIV. Hector ubique ferox violento pectore saevit,
- [3] 779 Hector ubique ferox uiolento pectore saeuit,
- [4] 779 Hector ubique ferox violento pectore saevit,
  - Hector (HECTOR; ヘクトル): — 猛き者、激しい心で荒れ狂う
- [6] 779 Hector ubique ferox violento pectore saevit,
  - Hector (Hector; ヘクトル): -or . . . ferox 779

780 quem saxo ingenti percussum maximus Aiax
- [2] 783 Quem saxo ingenti percussum maximus Ajax
- [3] 780 Quem saxo ingenti percussum maximus Aiax
- [4] 780 Quem saxo ingenti percussum maximus Ajax
  - Ajax (AJAX Telamonis filius; アイアス、テラモンの子): — 最も偉大な者、石でヘクトルを打つ
- [6] 780 quem saxo ingenti percussum maximus Aiax
  - Aiax (Aiax (Telamonius); アイアス（テラモンの子）): maximus -ax 780

781 depulit et toto prostratum corpore fudit.
- [2] 784 Depulit, et toto prostratum corpore fudit.
- [3] 781 Reppulit et toto prostratum corpore fudit.
- [4] 781 Reppulit et toto prostratum corpore fudit.
- [6] 781 depulit et toto prostratum corpore fudit.

782 Concurrit Troiana manus iuuenemque uomentem
- [2] 785 Concurrit Trojana manus , juvenemque vomentem
- [3] 782 Concurrit Troiana manus iuuenemque uomentem
- [4] 782 Concurrit Trojana manus juvenemque vomentem
  - Trojana (TROJANI; トロイア人): Trojana manus:トロイアの一団が駆け集まる
- [6] 782 concurrit Troiana manus iuvenemque vomentem
  - Troiana (Troianus; トロイアの): -na manus 782

783 sanguineos fluctus Xanthi lauere fluentis.
- [2] 786 Sanguineos flactus Xanthi lavere fluento.
- [3] 783 Sanguineos fluctus Xanthi lauere fluento.
- [4] 783 Sanguineos fluctus Xanthi lavere fluento.
  - Xanthi (XANTHUS fluvius; クサントス、河): Xanthi:トロイア人は傷ついたヘクトルをクサントスの波で洗う
- [6] 783 sanguineos fluctus Xanthi lavere fluentis.
  - … ウェルギリウス『アエネーイス』4, 143 を参照
  - Xanthi (Xanthus (fluvius); クサントス(河)): Xanthi . . . fluentis 783

784 Inde iterum ad pugnam redeunt; fit maxima caedes
- [2] 787 Inde iterum ad pugnam redeunt, fit maxima caedes
- [3] 784 Inde iterum ad pugnam redeunt, fit maxima caedes
- [4] 784 Inde iterum ad pugnam redeunt, fit maxima caedes
- [6] 784 inde iterum ad pugnam redeunt, fit maxima caedes

785 amborum et manat tellus infecta cruore.
- [2] 788 Amborum , et manat teUus infecta cruore.
- [3] 785 Amborum, et manat tellus infecta cruore.
- [4] 785 Amborum, et manat tellus infecta cruore.
- [6] 785 amborum et manat tellus infecta cruore.

786 Polydamas ualido Prothoenora percutit ictu,
- [2] 789 Polydamas valido Profhoenora percutit ictu,
- [3] 786 Polydamas ualido Prothoenora percutit ictu,
- [4] 786 Polydamas valido Prothoenora percutit ictu,
  - Polydamas (POLYDAMAS; ポリュダマス): プロトエノルを殺す
  - Prothoenora (PROTHOENOR; プロトエノル): Prothoenora:ポリュダマスがプロトエノルを殺す
- [6] 786 Polydamas valido Prothoënora percutit ictu,
  - Polydamas (Polydamas; ポリュダマス): Polydamas 786:パントオスの子
  - Prothoënora (Prothoenor; プロトエノル): -ora 786

787 Archelochumque Antenoriden Telamonius Aiax,
- [2] 790 Archelochumque Antenoriden Teiamonius Ajax,
- [3] 787 Archilochumque Antenoriden Telamonius Aiax,
- [4] 787 Archilochumque Antenoriden Telamonius Ajax,
  - Archilocum …（『イーリアス』XIV, 462 以下）。
  - Ajax (AJAX Telamonis filius; アイアス、テラモンの子): — テラモンの子がアルケロコスを打つ
  - Archilochum (ARCHILOCHUS; アルケロコス): Archilochum:テラモンの子アイアスがアンテノルの子アルケロコスを殺す
- [6] 787 Archelochumque Antenoriden Telamonius Aiax,
  - Aiax (Aiax (Telamonius); アイアス（テラモンの子）): Telamonius -ax 205. 363. 602. 623. 787. 836
  - Antenoriden (Antenorides; アンテノリデス): Archelochum . . . Antenoriden 787
  - Archelochum (Archelochus; アルケロコス): -um . . . Antenoriden 787:トロイア人
  - Telamonius (Telamonius; テラモンの): Telamonius Aiax 205. 363. 602. 623. 787. 836

788 Boeotumque Acamas Promachum, quem sternit atrocis
- [2] 791 Bceotumque Acamas Promachum, quem sternit atrocem
- [3] 788 Boeotumque Acamas Promachum, quem sternit atrocis
- [4] 788 Boeotumque Acamas Promachum, quem sternit atrocis
  - Acamas (ACAMAS Antenoris filius; アカマス、アンテノルの子): — プロマコスを傷つける
  - Boeotum (BOEOTUS; ボイオティア人): Boeotum(Promachus を参照)
  - Promachum (PROMACHUS; プロマコス): Promachum:アンテノルの子アカマスがボイオティア人プロマコスを傷つける
- [6] 788 Boeotumque Acamas Promachum, quem sternit atrocis
  - Acamas (Acamas 1; アカマス 1): -as はプロマコスを殺した。そのアカマスを猛きペネレオスの右手が打ち倒す 788
  - Boeotum (Boeotus; ボイオティア人): Boeotum . . . Promachum 788
  - Promachum (Promachus; プロマコス): Boeotum . . . Promachum 788

789 Penelei dextra; inde cadit Priameia pubes
- [2] 792 Penelei dextra , inde cadit Priameia pubes.
- [3] 789 Penelei dextra; inde cadit Priameia pubes.
- [4] 789 Penelei dextra ; inde cadit Priameia pubes.
  - Penelei (PENELEUS; ペネレオス): Penelei:猛きペネレオスの右手がアンテノルの子アカマスを打ち倒す
  - Priameia (TROJANI; トロイア人): Priameia pubes:プリアモスの若者たちが倒れる
- [6] 789 Penelei dextra; inde cadit Priameia pubes
  - Penelei (Peneleos; ペネレオス): atrocis -lei 789:ボイオティア人の将
  - Priameia (Priameius; プリアモスの): -eia pubes 789. 837:トロイア人

## Book 15

790 acrius insurgunt Troes ad Achaica bella
- [2] 793 XV. Acrins insurgunt Troes ad Achaica bella,
  - … 作者の過度の簡潔さと叙述における貧弱な薄弱さのせいで、少し前には討たれ潰走していたトロイア勢が、なぜ今やより激しく立ち上がり、夥しい殺戮を行ってギリシア勢を自らの陣船へと追い詰めるのか、事態の急激な逆転がどこから生じたのかがこの箇所では理解できなくなっている。言うまでもなく、ホメロスが創作している諸原因、すなわち目を覚ましたユピテルがトロイア勢に勇気を取り戻させ、ネプトゥヌスにギリシア勢をもはや助けぬよう諫め、ヘクトルがアポロによって奮い立たされ、戦いを再開すべく新たな力を授けられたという事情を、少なくとも手短にでも触れるべきであった。もし作者が戦いや殺戮、突撃や潰走よりも、ホメロスのこれら詩的虚構をより注意深く伝えていたならば、詩としての魅力をより多く保ち、単なる実録（年代記）を語るだけに終わることはなかったであろう。
- [3] 790 Acrius adsurgunt Troes; at Achaica turba
- [4] 790 Acrius assurgunt Troes ; at Achaica turba
  - Achaica (GRAI; ギリシア人): Achaica turba:アカイアの群れが逃げる
  - Troes (TROJANI; トロイア人): — より激しく立ち上がる
- [6] 790 acrius insurgunt Troes ad Achaica bella,
  - Achaica (Achaicus; アカイアの): insurgunt Troes ad Achaica bella 790
  - Troes (Tros; トロイア人): Troēs ad 790

791 <>
- [2] 794 Instaurantque manus ; cedit Pelopeia virtus
- [3] [791] [Instaurantque manus, cedit Pelopea iuuentus]
- [4] 791 below Instaurantque manus, cedit Pelopea juventus
  - Pelopea (GRAI; ギリシア人): [Pelopea juventus:ペロプスの若者たちが退く]
- [6] —
  - — (Pelopeus; ペロプスの): [Pelopea iuventus 791]:ギリシア人

792 pulsa metu uallumque et muros aggere saeptos
- [2] 795 Pulsa metu, vallumque et muros aggere septos
- [3] 792 Pulsa metu uallumque et muros aggere saeptos
- [4] 792 Pulsa metu vallumque et muros aggere saeptos
- [6] 792 pulsa metu vallumque et muros aggere saeptos

793 transiliunt, alii fossas uoluuntur in ipsas.
- [2] 796 Transiliunt; alii fossas volvuntur in ipsas.
- [3] 793 Transiliunt, alii fossas uoluuntur in ipsas.
- [4] 793 Transiliunt, alii fossas volvuntur in ipsas.
- [6] 793 transiliunt, alii fossas volvuntur in ipsas.

794 Aduolat interea Danaum metus impiger Hector:
- [2] 797 Advolat interea Danaum metus, impiger Hector :
- [3] 794 Aduolat interea Danaum metus impiger Hector.
- [4] 794 Advolat interea Danaum metus impiger Hector.
  - Danaum (GRAI; ギリシア人): — ダナオイの恐怖、ヘクトル
  - Hector (HECTOR; ヘクトル): — ダナオイの恐怖、疲れを知らず、飛んで来てギリシア人を追い払う
- [6] 794 advolat interea Danaum metus impiger Hector:
  - Danaum (Danai; ダナオイ): -um(属格):19. 50. 67. 124. 153. 251. 268. 357. 389. 496. 631. 686. 691. 698. 705. 743. 747. 794. 1025
  - Hector (Hector; ヘクトル): Danaum metus, impiger -or 794

795 confugiunt iterum ad classes Agamemnonis alae
- [2] 798 Confugiunt iterum ad classes Agamemnonis alae,
- [3] 795 Confugiunt iterum ad classes Agamemnonis alae
- [4] 795 Confugiunt iterum ad classes Agamemnonis alae
  - Agamemnonis (AGAMEMNON; アガメムノン): — ヘクトルに押されて、彼の部隊は船へ逃げる
- [6] 795 confugiunt iterum ad classes Agamemnonis alae
  - Agamemnonis (Agamemnon; アガメムノン): -onis 121. 795

796 atque inde aduersis propellunt uiribus hostem.
- [2] 799 Atque inde adversis propellunt viribus hosiem.
- [3] 796 Atque inde aduersis propellunt uiribus hostem.
- [4] 796 Atque inde adversis propellunt viribus hostem.
- [6] 796 atque inde adversis propellunt viribus hostem.

797 Fit pugna ante rates, saeuit Mauortius Hector
- [2] 800 Fit pugna ante rates : SJBvit Mavortius Hector,
- [3] 797 Fit pugna ante rates; saeuit Mauortius Hector
- [4] 797 Fit pugna ante rates; saevit Mavortius Hector
  - Hector (HECTOR; ヘクトル): — マウォルスのヘクトルが荒れ狂い、ギリシア人の船を焼こうとする
- [6] 797 fit pugna ante rates; saevit Mavortius Hector
  - Hector (Hector; ヘクトル): Mavortius -or 543. 797
  - Mavortius (Mavortius; マウォルスの): Mavortius Hector 543. 797

798 et poscit flammas totamque incendere classem
- [2] 801 Et poscit flammas, totamque incendere classem
- [3] 798 Et poscit flammas totamque incendere classem
- [4] 798 Et poscit flammas totamque incendere classem
- [6] 798 et poscit flammas totamque incendere classem

799 apparat. Huic ualidis obsistit uiribus Aiax,
- [2] 802 Adparat : huic validis obsistit viribus Ajax
- [3] 799 Apparat: huic ualidis obsistere uiribus Aiax,
- [4] 799 Apparat; huic validis obsistit viribus Ajax,
  - Ajax (AJAX Telamonis filius; アイアス、テラモンの子): — ただ一人で船を守る
- [6] 799 apparat; huic validis obsistit viribus Aiax,
  - Aiax (Aiax (Telamonius); アイアス（テラモンの子）): -ax 538. 799. 1009

800 stans prima in puppi, clipeoque incendia saeua
- [2] 803 Stans prima in puppi , clypeoque incendia sseva
  - … ――*Incendia saeva Sustinet*（激しい火炎に耐える）。オウィディウスがアイアスの語り手を導入して次のように述べているのと同様である（Met. XIII, 7）: « non Hectoreis dubitavit cedere flammis Quas ego sustinui »。パリ編者。
- [3] 800 Stans prima in puppi, clipeoque incendia saeua
- [4] 800 Stans prima in puppi, clipeoque incendia saeva
- [6] 800 stans prima in puppi, clipeoque incendia saeva

801 sustinet et solus defendit mille carinas.
- [2] 804 Sustinet, et solus defendit mille carinas.
  - *Defendit mille carinas*（千隻の軍船を守る）。オウィディウスの前掲箇所において: « Nempe ego mille meo protexi pectore puppes »。
- [3] 801 Sustinet et solus defendit mille carinas.
- [4] 801 Sustinet et solus defendit mille carinas.
- [6] 801 sustinet et solus defendit mille carinas.

802 Hinc iaciunt Danai robustae cuspidis hastas,
- [2] 805 Hinc jaciunt Danai robustae cuspidis hastas,
- [3] 802 Hinc iaciunt Danai robustae cuspidis hastas,
- [4] 802 Hinc jaciunt Danai robustae cuspidis hastas,
  - Danai (GRAI; ギリシア人): — 槍を投げる
- [6] 802 hinc iaciunt Danai robustae cuspidis hastas,
  - Danai (Danai; ダナオイ): Danai 508. 542. 646. 679. 766. 802. 838. 960. 978. 1002

803 illinc ardentes taedas Phryges undique iactant;
- [2] 806 Illinc ardentes taedas Phryges undique jactant,
- [3] 803 Illinc ardentes taedas Phryges undique iactant:
- [4] 803 Illinc ardentes taedas Phryges undique jactant :
  - Phryges (TROJANI; トロイア人): — 燃える松明を投げる
- [6] 803 illinc ardentes taedas Phryges undique iactant:
  - Phryges (Phryges; プリュギア人): Phryges 401. 493. 636. 682. 762. 803

804 per uastos sudor pugnantum defluit artus.
- [2] 807 Per vastos sudor pugnantum defluit artus.
- [3] 804 Per uastos sudor pugnantum defluit artus.
- [4] 804 Sudor per vastos pugnantum defluit artus.
- [6] 804 per vastos sudor pugnantum defluit artus.

## Book 16

805 Non ualet ulterius cladem spectare suorum
- [2] 808 XVI. Non valet ulterius cladem spectare suorum
- [3] 805 Non ualet ulterius cladem spectare suorum
- [4] 805 Non valet ulterius cladem spectare suorum
- [6] 805 non valet ulterius cladem spectare suorum

806 Patroclus subitoque armis munitus Achillis
- [2] 809 Patroclus, subitoque armis munitus Achillis
- [3] 806 Patroclus subitoque armis munitus Achillis
- [4] 806 Patroclus subitoque armis munitus Achillis
  - Achillis (ACHILLES; アキレウス): — アキレウスの武具に守られたパトロクロス
  - Patroclus (PATROCLUS; パトロクロス): アキレウスの武具に守られて
- [6] 806 Patroclus subitoque armis munitus Achillis
  - Achillis (Achilles; アキレウス): -is 54. 689. 719. 806
  - Patroclus (Patroclus; パトロクロス): Patroclus 806. 827

807 prouolat et falsa conterret imagine Troas.
- [2] 810 Advolat, et falsa conterret imagine Troas.
- [3] 807 Prouolat et falsa conterret imagine Troas.
- [4] 807 Provolat et falsa conterret imagine Troas.
  - Troas (TROJANI; トロイア人): Troas:アキレウスの武具に守られたパトロクロスがトロイア人を恐れさせる
- [6] 807 provolat et falsa conterret imagine Troas.
  - Troas (Tros; トロイア人): Troas 807

808 Qui modo turbabant Danaos animoque fremebant,
- [2] 811 Qui modo turbabant Danaos, animoque fremebant,
- [3] 808 Qui modo turbabant Danaos animoque fremebant,
- [4] 808 Qui modo turbabant Danaos animisque fremebant,
  - Danaos (GRAI; ギリシア人): ついさっきまでダナオイを混乱させていたトロイア人が、今は逃げる
- [6] 808 qui modo turbabant Danaos animoque fremebant,
  - Danaos (Danai; ダナオイ): -os 45. 492. 659. 808. 912. 950. 1001

809 nunc trepidi fugiunt, fugientibus imminet ille
- [2] 812 Nunc trepidi fugiunt : fugientibus imminet ille,
- [3] 809 Nunc trepidi fugiunt: fugientibus imminet ille
- [4] 809 Nunc trepidi fugiunt : fugientibus imminet ille
- [6] 809 nunc trepidi fugiunt: fugientibus imminet ille
  - ille (Patroclus; パトロクロス): ille 809. 823 を参照

810 perturbatque ferox acies uastumque per agmen
- [2] 813 Perturbatque ferox aciem , vastumque per agmen
- [3] 810 Proturbatque ferox acies uastumque per agmen
- [4] 810 Proturbatque ferox acies vastumque per agmen
- [6] 810 perturbatque ferox acies vastumque per agmen

811 sternit et ingenti Sarpedona uulnere fundit
- [2] 814 Fertur, et ingenti Sarpedona vulnere fundit;
- [3] 811 Saeuit et ingenti Sarpedona uulnere fundit
- [4] 811 Saevit et ingenti Sarpedona vulnere fundit
  - Sarpedona (SARPEDON; サルペドン): Sarpedona:パトロクロスがサルペドンを殺す
- [6] 811 sternit et ingenti Sarpedona vulnere fundit
  - Sarpedona (Sarpedon; サルペドン): -dona 811

812 et nunc hos cursu nunc illos praeterit ardens
- [2] 815 Et nunc hos cursu y nunc illos praeterit ardens,
  - … この行において作者はウェルギリウス Aen. IV, 157: « jamque hos cursu, jam praeterit illos » を念頭に置いていたと思われる。
- [3] 812 Et nunc hos cursu nunc illos praeterit ardens
- [4] 812 Et nunc hos curru, nunc illos praeterit ardens
- [6] 812 et nunc hos cursu nunc illos praeterit ardens

813 proeliaque horrendi sub imagine uersat Achillis.
- [2] 816 Praeliaque horrendi sub imagine versat Achillis.'
- [3] 813 Praeliaque horrendi sub imagine uersat Achillis.
- [4] 813 Proeliaque horrendi sub imagine versat Achillis.
  - Achillis (ACHILLES; アキレウス): — パトロクロスは恐るべきアキレウスの姿で戦う
- [6] 813 proeliaque horrendi sub imagine versat Achillis.
  - Achillis (Achilles; アキレウス): horrendi . . . -is 813

814 Quem postquam socias miscentem caede cateruas
- [2] 817 Quem postquam socias miscentem csede catervas,
- [3] 814 Quem postquam socias miscentem caede cateruas
- [4] 814 Quem postquam socias miscentem caede catervas
- [6] 814 quem postquam socias miscentem caede catervas

815 turbantemque acies respexit feruidus Hector,
- [2] 818 Turbantemque acies conspexit fervidus Hector,
- [3] 815 Turbantemque acies respexit feruidus Hector,
- [4] 815 Turbantemque acies respexit fervidus Hector,
  - Hector (HECTOR; ヘクトル): — 燃え立つ者、アキレウスの姿で戦列を乱すパトロクロスを振り返る
- [6] 815 turbantemque acies respexit fervidus Hector,
  - Hector (Hector; ヘクトル): fervidus -or 815

816 tollit atrox animos uastisque immanis in armis
- [2] 819 Tollit atrox animos, vastisque immanis in armis
- [3] 816 Tollit atrox animos uastisque inmanis in armis
- [4] 816 Tollit atrox animos vastisque immanis in armis
- [6] 816 tollit atrox animos vastisque inmanis in armis

817 occurrit contra magnoque hunc increpat ore:
- [2] 820 Occurrit contra, magnoque hunc increpat ore :
- [3] 817 Occurrit contra magnoque haec increpat ore:
- [4] 817 Ocurrit contra magnoque haec increpat ore :
- [6] 817 occurrit contra magnoque hunc increpat ore:

818 "Huc, age, huc conuerte gradum, fortissime Achilles:
- [2] 821 «Huc, age, nunc converte gradum, fortissime Achilies,
- [3] 818 'Huc age nunc conuerte gradum, fortissime Achilles:
- [4] 818 « Huc age nunc converte gradum, fortissime Achilles :
  - Achilles (ACHILLES; アキレウス): 呼格:最も勇敢な者よ(ヘクトルが呼びかける)
- [6] 818 'huc age nunc converte gradum, fortissime Achilles:
  - Achilles (Achilles; アキレウス): 呼格:fortissime -es 818. 1028

819 iam nosces ultrix quid Troica dextera possit
- [2] 822 Jam nosces, ultrix quid Troica dextera possit,
- [3] 819 Iam nosces, ultrix quid Troica dextera possit
- [4] 819 Jam nosces, ultrix quid Troica dextera possit
  - Troica (TROICUS; トロイアの): Troica dextera:トロイアの右手(ヘクトルの手)
- [6] 819 iam nosces, ultrix quid Troica dextera possit
  - Troica (Troicus; トロイアの): Troica dextera、ヘクトルの:819

820 et quantum bello ualeat fortissimus Hector.
- [2] 823 Et quantum bello valeat fbrtissimus Hector.
- [3] 820 Et quantum in bello ualeat fortissimus Hector.
- [4] 820 Et quantum in bello valeat fortissimus Hector.
  - Hector (HECTOR; ヘクトル): — 最も勇敢な者、戦においてどれほど力があるか(自らについて語る)
- [6] 820 et quantum bello valeat fortissimus Hector.
  - Hector (Hector; ヘクトル): fortissimus -or 486. 820

821 Nam licet ipse suis Mauors te protegat armis,
- [2] 824 Nam licet ipse suis Mavors te protegat armis,
  - *Nam licet ipse*。バルトはこれらの行をきわめて美しいと称賛している（Adv. LIX, 15, p. 2808）。しかし実際のところ作者は、それらを自らの才能ではなく、ほとんど一語一語書き写したオウィディウスの才気に負っている（Metam. VIII, 394）: « Ipsa suis licet hunc Latonia protegat armis, Hunc tamen invita perimet mea dextra Diana »。
- [3] 821 Nam licet ipse suis Mauors te protegat armis,
- [4] 821 Nam licet ipse suis Mavors te protegat armis,
  - Mavors (MARS; マルス): — たとえ彼が汝を守ろうとも、汝は死ぬであろう(ヘクトルがパトロクロスに呼びかける)
- [6] 821 nam licet ipse suis Mavors te protegat armis,
  - Mavors (Mavors; マウォルス): ipse . . . Mavors 821

822 inuito tamen haec perimet te dextera Marte."
- [2] 825 Invito tamen haec perimet te dextera Marte ».
- [3] 822 Inuito tamen haec perimet te dextera Marte'.
- [4] 822 Invito tamen haec perimet te dextera Marte ».
  - Marte (MARS; マルス): Marte invito:マルスの意に反して、この右手が汝を滅ぼすであろう(ヘクトルが、アキレウスの武具をまとったパトロクロスに呼びかける)
- [6] 822 invito tamen haec perimet te dextera Marte'.
  - Marte (Mars; マルス): invito . . . Marte 822

823 Ille silet spernitque minas animosaque dicta,
- [2] 826 Ille silet , spernitque minas animosaque dicta ,
- [3] 823 Ille silet spernitque minas animosaque dicta,
- [4] 823 Ille silet spernitque minas animosaque dicta,
- [6] 823 ille silet spernitque minas animosaque dicta,
  - ille (Patroclus; パトロクロス): ille 809. 823 を参照

824 ut quem mentitur uerus credatur Achilles.
- [2] 827 Ut , quem mentitur, verus credatur Achilles.
- [3] 824 Ut quem mentitur uerus credatur Achilles,
- [4] 824 Ut quem mentitur verus credatur Achilles.
  - Achilles (ACHILLES; アキレウス): 主格、述語として:パトロクロスは、ヘクトルに本物のアキレウスと信じられるよう沈黙する
- [6] 824 ut quem mentitur verus credatur Achilles.
  - Achilles (Achilles; アキレウス): verus . . . -es 824

825 Tunc prior intorquet collectis uiribus hastam
- [2] 828 Tunc prior intorquet coliectis viribus hastam
- [3] 825 Tunc prior intorquet collectis uiribus hastam
- [4] 825 Tunc prior intorquet collectis viribus hastam
- [6] 825 tunc prior intorquet collectis viribus hastam

826 Dardanides, quam prolapsam celeri excipit ictu
- [2] 829 Dardanides, quam prolapsam celeri excipit ictu
- [3] 826 Dardanides, quam prolapsam celere excipit actu
- [4] 826 Dardanides, lapsam celeri quam decipit astu
  - Dardanides (HECTOR; ヘクトル): Dardanides:ダルダニデスが槍でパトロクロスに向かう
- [6] 826 Dardanides, quam prolapsam celeri excipit ictu
  - Dardanides (Dardanides; ダルダニデス): Dardanides 826:ヘクトル

827 Patroclus redditque uices et, mutua dona,
- [2] 830 Patroclus, redditque vices et mutua dona.
  - *Et mutua dona*（そして返礼の贈り物を）。これらの言葉についてバルトは Advers. LVIII, 14, p. 2752 で、打撃を贈り物と呼ぶのは作者特有の語法（idiotismus）であると指摘している。しかし実際にはウェルギリウスも同様に語っている（Aen. X, v. 881）: « Desine, jam venio moriturus, et haec tibi porto Dona prius »。――カトゥルスがカルウスへの諷刺詩［第 14 歌 20 行］で « Ac te his suppliciis remunerabor » と言い、ウァレリウス・フラックスが V, 550 で « Qui gemitus, irasque pares, et mutua Graiis dona ferant » と言っているのも同様である。すでにヨハンネス・シュラーダーが Observ. I, cap. 3, 35 頁でこのことを指摘していた。
  - **(cont.)** （前頁からの続き）同様に、*gratiam referre*（恩を返す）も悪い意味で復讐あるいは報復の意で用いられる。テレンティウス『宦官』V, 3, 2: « qui referam illi sacrilego gratiam »。パリ編者。
- [3] 827 Patroclus redditque uices et mutua dona;
- [4] 827 Patroclus redditque vices et mutua dona ;
  - Patroclus (PATROCLUS; パトロクロス): — ヘクトルの槍をかわす
- [6] 827 Patroclus redditque vices et mutua dona
  - Patroclus (Patroclus; パトロクロス): Patroclus 806. 827

827a
- [2] 831 Objicit et saxum multo cum pondere missum,
- [3] —
- [4] 827 bis Obicit et saxum magno cum robore missum
- [6] —

828 quod clipeo excussum uiridi tellure resedit.
- [2] 832 Quod clypeo excussum viridi tellure resediL
- [3] 828 Quod clipeo excussum uiridi tellure resedit.
- [4] 828 Quod clipeo excussum viridi tellure resedit.
- [6] 828 quod clipeo excussum viridi tellure resedit.

829 Tunc rigidos stringunt enses et comminus armis
- [2] 833 Tunc rigidos stringunt enses, et cominus arma
- [3] 829 Tunc rigidos stringunt enses et cominus arma
- [4] 829 Tunc rigidos stringunt enses et cominus arma
- [6] 829 tunc rigidos stringunt enses et comminus armis

830 inter se miscent, donec Troianus Apollo
- [2] 834 Inter se miscent, donec Trojanus Apollo
- [3] 830 Inter se miscent, donec Troianus Apollo
- [4] 830 Inter se miscent, donec Trojanus Apollo
  - Apollo (APOLLO; アポロ): — トロイアの[アポロ]が、アキレウスの姿で戦うパトロクロスを裸にする
- [6] 830 inter se miscent, donec Troianus Apollo
  - Apollo (Apollo; アポロ): Troianus -o 472. 830

831 mentitos uultus simulati pandit Achillis
- [2] 835 Mentitos vultus simulati pandit Acbillts,
- [3] 831 Mentitos uultus simulati pandit Achillis
- [4] 831 Mentitos vultus simulati pandit Achillis
  - Achillis (ACHILLES; アキレウス): — アポロが彼の偽りの顔をあらわにする
- [6] 831 mentitos vultus simulati pandit Achillis
  - Achillis (Achilles; アキレウス): simulati . . . -is(パトロクロスの)831
  - Achillis (Patroclus; パトロクロス): simulati . . . Achillis 831

832 denudatque uirum, quem bello maximus Hector
- [2] 836 Denudafque rirum : quem bello maximus Hector
- [3] 832 Denudatque uirum; quem bello maximus Hector
- [4] 832 Denudatque virum; quem bello maximus Hector
  - Hector (HECTOR; ヘクトル): — 戦において最も偉大な者、偽りの武具のパトロクロスを捕らえる
- [6] 832 denudatque virum; quem bello maximus Hector
  - Hector (Hector; ヘクトル): bello maximus -or 620. 832

833 pugnantem falsis postquam deprendit in armis,
- [2] 837 Pugnantem falsis postquam deprendit in armis,
- [3] 833 Pugnantem falsis postquam deprendit in armis,
- [4] 833 Pugnantem falsis postquam deprendit in armis,
- [6] 833 pugnantem falsis postquam deprendit in armis,

834 irruit et iuuenem nudato pectore ferro
- [2] 838 Irruit, et juvenem , nudato pectore , ferro
  - … すなわち、836 行で述べたように、アポロによって胸を剥き出しにされた後に、彼はその若者を剣で突き刺すのである。実際、ホメロスは武具がアポロによってパトロクロスから剥ぎ取られたと語るが、ホメロス受容者（われらの詩人）はホメロスを離れて、武具はヘクトルによって剥ぎ取られたと述べている。
- [3] 834 Irruit et iuuenem nudato pectore ferro
- [4] 834 Irruit et juvenem nudato pectore ferro
- [6] 834 irruit et iuvenem nudato pectore ferro
  - iuvenem (Patroclus; パトロクロス): iuvenem 834

835 traicit et uictor Vulcania detrahit arma.
- [2] 839 Trajicit, et victo Vulcania detrahit arma.
- [3] 835 Traicit et uicto Uulcania detrahit arma.
- [4] 835 Traicit et victo Vulcania detrahit arma.
  - Vulcania (VULCANIUS; ウルカヌスの): Vulcania arma:ウルカヌスの武具
- [6] 835 traicit et victor Vulcania detrahit arma.
  - Vulcania (Vulcanius; ウルカヌスの): Vulcania . . . arma、アキレウスの 835. 961

## Book 17

836 Vindicat exstincti corpus Telamonius Aiax
- [2] 840 XVII. Vindicat exstincti corpus Telamonius Ajax,
- [3] 836 Uindicat extincti corpus Telamonius Aiax
- [4] 836 Vindicat exstincti corpus Telamonius Ajax
  - Ajax (AJAX Telamonis filius; アイアス、テラモンの子): — テラモンの子がパトロクロスの亡骸を守り取る
- [6] 836 vindicat extincti corpus Telamonius Aiax
  - Aiax (Aiax (Telamonius); アイアス（テラモンの子）): Telamonius -ax 205. 363. 602. 623. 787. 836
  - extincti (Patroclus; パトロクロス): extincti 836
  - Telamonius (Telamonius; テラモンの): Telamonius Aiax 205. 363. 602. 623. 787. 836

837 oppositoque tegit clipeo. Priameia pubes
- [2] 841 Oppositoque tegit clypeo. Priameia pubes
- [3] 837 Oppositoque tegit clipeo. Priameia pubes
- [4] 837 Oppositoque tegit clipeo. Priameia pubes
  - Priameia (TROJANI; トロイア人): — 喜びに躍り上がる
- [6] 837 oppositoque tegit clipeo. Priameia pubes
  - Priameia (Priameius; プリアモスの): -eia pubes 789. 837:トロイア人

838 laetitia exsultat, Danai sua uulnera maerent.
- [2] 842 Laetitia exsultat; Danai sua funera moerent.
- [3] 838 Laetitia exultat, Danai sua funera maerent.
- [4] 838 Laetitia exsultat, Danai sua funera maerent.
  - Danai (GRAI; ギリシア人): — 自らの死者を悼む
- [6] 838 laetitia exultat, Danai sua funera maerent.
  - Danai (Danai; ダナオイ): Danai 508. 542. 646. 679. 766. 802. 838. 960. 978. 1002

## Book 18

839 Interea iuuenis tristi cum pube suorum
- [2] 843 Interea juvenis tristi cum pube suonim
- [3] 839 Interea iuuenis tristi cum pube suorum
- [4] 839 Interea juvenis tristi cum pube suorum
- [6] 839 interea iuvenis tristi cum pube suorum

840 Nestorides in castra ferunt miserabile corpus.
- [2] 844 Nestorides in castra refert miserabile corpus.
  - … なお、ここでも作者はホメロスとは異なって物語っている。というのも、ホメロスによればメネラオスとメリオネスがパトロクロスの遺体を陣営へと運び帰り、アンティロコスはその死の知らせをアキレウスのもとへ届けたにすぎないからである。
- [3] 840 Nestorides in castra ferunt miserabile corpus.
- [4] 840 Nestorides in castra ferunt miserabile corpus.
  - Nestorides (ANTILOCHUS; アンティロコス): Nestorides:パトロクロスの亡骸を陣営に運び帰る
- [6] 840 Nestorides in castra ferunt miserabile corpus.
  - Nestorides (Nestorides; ネストリデス): Nestorides 840:アンティロコス
  - corpus (Patroclus; パトロクロス): miserabile corpus 840

841 Tunc ut Pelidae aures diuerberat horror,
- [2] 845 XVIII. Tunc ut Pelidae rumor deverberataures,
  - **(cont.)** … バルトは『雑考』(*Advers.*) 2752 頁で、*diverberare aures rumorem*（噂が耳を打つ）をわれらの詩人特有の語法（イディオティスムス）と見なしている。しかしながら、他の作家たちも同様の表現を用いている。プラウトゥス『アンピトリュオ』I, 1, 177 において: « vox aures verberat »；またルカヌス VII, 25: « tuba verberat aures »。――本著作第2巻128頁でわれわれが引いたペトロニウスの断片において: « subitis rumoribus oppida pulsat »。パリ編者。――同人『サテュリコン』第68章: « nullus sonus unquam acidior percussit aures meas »。
- [3] 841 Hic Pelidae aures ut dirus uerberat horror,
- [4] 841 Hic ut Pelidae devenerat horror ad aures
  - Pelidae (ACHILLES; アキレウス): — その恐ろしい知らせ(パトロクロスの殺害)が彼の耳に届いていた
- [6] 841 tunc † ut Pelidis aures diverberat horror;
  - Pelidis (Pelides; ペリデス): -dae 841

842 palluit infelix iuuenis, calor ossa reliquit;
- [2] 846 Palluit infelix juvenis, caior ossa reliquit;
- [3] 842 Palluit infelix iuuenis; calor ossa reliquit,
- [4] 842 Palluit infelix juvenis; calor ossa reliquit,
- [6] 842 palluit infelix iuvenis, calor ossa reliquit.

843 membra simul lacrimans materno innectit amictu,
- [2] 847 Membra siimil lacrymans materno tersit amictu
  - … しかし「母の衣をもって（*materno amictu*）」、すなわち「母から授かった［衣をもって］」とわれらの詩人が言うのは、母親が出征する息子たちのために衣を織ったと述べる他の詩人たちの箇所に疑いなく由来している。例えばラウススについて Virgil. Aen. XI, 818；アテュスについて Statius, Theb. VIII, 566；アタランテの子パルテノパイオスについて同 IX, 691 に見られ、おそらくアキレウスについてもどこかで同様のことが言われているのであろう。しかしこの箇所においてホメロスは母の衣に言及していない。
- [3] [843] [Membra simul lacrimans materno nectit amictu
- [4] 843 below Membra simul lacrimans materno nectit amictu
- [6] 843 membra simul lacrimans materno † nectit amictu,
  - membra (Patroclus; パトロクロス): membra 843
  - materno (Thetis; テティス): materno . . . amictu 843

844 deflens Aeacides tristi de caede sodalis;
- [2] 848 Deflens Aeacides tristi de caede sodatis,
  - … 前掲箇所のバルトが *deflere de caede* を作者特有の語法、それどころか極めて異例な言いまわしと見なしているのに対し、全面的に同意すべきかどうか私には分からない。*deflere* は、*declamare*（大声で演説する）、*defatigare*（疲れ果てさせる）、*detonare*（雷鳴を轟かせ尽くす）などが言われるのと同様に、おびただしく泣き、泣くことによって悲しみを満たすという意味で解されるべきである。また *de caede* は *ob* または *propter caedem*（殺戮のゆえに）の代わりに置かれている。…
- [3] 844 Deflens Aeacides tristi de caede sodalis.]
- [4] 844 below Deflens Aeacides tristi de caede sodalis.
  - Aeacides (ACHILLES; アキレウス): — [パトロクロスの殺害を嘆く]
- [6] [844] [deflens Aeacides tristi de caede sodalis]
  - Aeacides (Aeacides (Achilles); アエアキデス（アキレウス）): ferus -es 74. [844]
  - sodalis (Patroclus; パトロクロス): [sodalis 844]

845 unguibus ora secat comptosque in puluere crines
- [2] 849 Unguibns ora seeat, comptos in pulvere crines
  - … 喪に服して自らに塵を振りかける習俗は、聖書から知られるようにユダヤ人だけでなく、実例は稀であるとはいえギリシア人やローマ人にも行われていたことを、ベルナルティウスが Stat. Theb. III, 50 への注で指摘している。スタティウスはしばしばこれに触れており、とりわけ Theb. VI, 30: « sed et ipse exsutus honore Vittarum nexu genitor, squallentiaque ora Sparsus, et incultam ferali pulvere barbam »。――またフォス版の Catullus in Epithal. Pel. 183 頁を参照せよ: « Canitiem terra atque infuso pulvere foedans »。パリ編者。――われらの詩人はまた、古代人の慣習に従って動詞 *deformat*（姿を損なう、汚す）を用いている。古代人はこのように塵を浴びた者を好んで *informes*（無残な姿の、醜悪な）と呼んだからである。スタティウスの前掲箇所: « haustaque informis arena Questibus implet agros »。そしてコルネリウス・セウェルス「キケロの死について」16 行: « Informes vultus sparsamque cruore nefando Canitiem »。
- [3] 845 Unguibus ora secat, comptos dein puluere crines
- [4] 845 Unguibus ora secat, comptos in pulvere crines
- [6] 845 unguibus ora secat comptosque in pulvere crines
  - … ウェルギリウス『アエネーイス』12, 99 を参照 …

846 deformat, scindit firmo de pectore uestes
- [2] 850 Deformat, scindit filrmas de pectore vestes,
  - *Scindit de pectore vestes*（胸から衣服を引き裂く）。喪において衣服を裂-
  - **(cont.)** （前頁からの続き）-くという万民共通のこの習俗を、バルトは注釈の多くの箇所で、とりわけスタティウスの次の箇所（Theb. IX, 353）への注で論証した: « Exsiliit furibunda comis, ac verbere crebro Oraque, pectoraque, et viridem scidit horrida vestem »。同人の Stat. Silv. II, 1, 171 への注記と比較せよ。また Sil. Ital. XIII, 389 を付け加えることができる: « Pulsato lacerat violenter pectore amictus »。
- [3] 846 Deformat scinditque suas de pectore uestes
- [4] 846 Deformat scinditque suas de pectore vestes
- [6] 846 deformat: scindit † firmas de pectore vestes

847 et super exstincti prostratus membra sodalis
- [2] 851 Et super exstincti prostratus membra sodalis,
- [3] 847 Et super extincti prostratus membra sodalis
- [4] 847 Et super exstincti prostratus membra sodalis
- [6] 847 et super extincti prostratus membra sodalis
  - sodalis (Patroclus; パトロクロス): extincti . . . sodalis 847

848 crudeles fundit questus atque oscula figit.
- [2] 852 Crudeles fundit questus, atque oscula figit.
- [3] 848 Crudeles fundit questus atque oscula figit.
- [4] 848 Crudeles fundit questus atque oscula figit.
- [6] 848 crudeles fundit questus atque oscula figit.

849 Mox ubi depositi gemitus lacrimaeque quierunt:
- [2] 853 Mox ubi depulsi gemitus, lacrymaeque quierunt,
- [3] 849 Mox ubi depositi gemitus lacrimaeque quierunt,
- [4] 849 Mox ubi depositi gemitus lacrimaeque quierunt,
- [6] 849 mox ubi depositi gemitus lacrimaeque quierunt,

849a
- [2] [854] [Tristis ait, jam jamque meo cruciabere ferro]
- [3] —
- [4] —
- [6] —

850 "Non impune mei laetabere caede sodalis,
- [2] 855 «Non impune mei laetabere caede sodalis,
- [3] 850 'Non inpune mei laetabere caede sodalis,
- [4] 850 « Non impune mei laetabere caede sodalis,
- [6] 850 'non impune mei laetabere caede sodalis,
  - sodalis (Patroclus; パトロクロス): mei sodalis 850

851 Hector" - ait - "magnoque meo, uiolente, dolori
- [2] 856 Hector , ait, magnasque meo, violente, dolori
  - … なお、バルトは Adv. 2753 頁で、作者は *violentus*（狂暴な男）を罵詈や非難の意で受け取らせようとしたのであり、それゆえそのような語が本来あるべき適切さを欠いて濫用されるようになった時代に書いたように見える、と考えている。しかし私は、ここで罵詈や非難を探し求めるのは無駄であると考える。むしろ大胆不敵で無謀であり、己の力を悪用する者が *violentus* として叱責されているのである。確かに、ここで作者が追随したと思われるオウィディウスも Met. IX, 121 で同様に述べている: « Quo te fiducia, clamat, Vana pedum, violente, rapit »。――ティブルスもマルス自身について IV, 2, 3 で同様に述べている: « at tu, violente, caveto Ne tibi miranti turpiter arma cadant »。そしてオウィディウス『イービス』20 行: « At tibi, calcasti qui me, violente, jacentem »。パリ編者。
- [3] 851 Hector' ait, 'magnoque meo, uiolente, dolori
- [4] 851 Hector, » ait « magnasque meo, violente, dolori
  - Hector (HECTOR; ヘクトル): 呼格:乱暴な者よ(アキレウスがパトロクロスの殺害について)
- [6] 851 Hector' ait, 'magnoque meo, violente, dolori
  - Hector (Hector; ヘクトル): 呼格:-or . . . violente 851

852 persolues poenas atque istis uictor in armis,
- [2] 857 Persolves poenas, atque istis victor in armis,
- [3] 852 Persolues poenas atque istis uictor in armis,
- [4] 852 Persolves poenas atque istis victor in armis,
- [6] 852 persolves poenas atque istis, victor, in armis,
  - … 私は倒置法(ヒュペルバトン)をコンマで示した

853 in quibus exsultas, fuso moriere cruore."
- [2] 858 In quibus exsultas, fuso moriere cruore ».
- [3] 853 In quibus exultas, fuso moriere cruore.'
- [4] 853 In quibus exsultas, fuso moriere cruore ».
- [6] 853 in quibus exultas, fuso moriere cruore.'

854 Post haec accensus furiis decurrit ad aequor
- [2] 859 Post haec accensus furiis decurrit ad aequor.
  - … *Accensus furiis*（狂乱に燃え上がり）は Virgil. Aen. XII, 946。
- [3] 854 Post haec accensus furiis decurrit ad aequor
- [4] 854 Post haec accensus furiis decurrit ad aequor
- [6] 854 post haec accensus furiis decurrit ad aequor

855 fortiaque arma Thetin supplex rogat: illa relictis
- [2] 860 Fortiaque arma Thetin supplex rogat : illa relictis
- [3] 855 Fortiaque arma Thetin supplex rogat: illa relictis
- [4] 855 Fortiaque arma Thetin supplex rogat : illa relictis
  - Thetin (THETIS; テティス): Thetin:アキレウスはテティスに強い武具を求める
- [6] 855 fortiaque arma Thetin supplex rogat: illa relictis
  - Thetin (Thetis; テティス): Thetin 855

856 fluctibus auxilium Vulcani protinus orat.
- [2] 861 Fluctibus, auxiiiuin Vulcani protinus orat,
- [3] 856 Fluctibus auxilium Uulcani protinus orat.
- [4] 856 Fluctibus auxilium Vulcani protinus orat.
  - Vulcani (VULCANUS; ウルカヌス): Vulcani:テティスはウルカヌスの助けを乞う
- [6] 856 fluctibus auxilium Vulcani protinus orat.
  - Vulcani (Vulcanus; ウルカヌス): Vulcani 856

857 Excitat Aetnaeos calidis fornacibus ignes
- [2] 862 Excitat Aetnaeos calidis fornacibus ignes
  - ここでラテン・ホメロス作者は、エトナの火炎やその中にあるウルカヌスの鍛冶場を知らないホメロスではなく、ウェルギリウス（Aen. VIII, 419 以下）を模倣して *Aetnaeos ignes*（エトナの業火）と名指している。同様にレポシアヌス『マルスとウェヌスの情事』163 行で、ウルカヌスは密通者を縛り上げる鎖を鍛えるために « Antra furens Aetnaea petit »（怒りに狂いてエトナの洞窟へと向かう）。
- [3] 857 Excitat Aetnaeos calidis fornacibus ignes
- [4] 857 Excitat Aetnaeos calidis fornacibus ignes
  - Aetnaeos (AETNAEUS; エトナの): Aetnaeos ignes
- [6] 857 excitat Aetnaeos calidis fornacibus ignes
  - Aetnaeos (Aetnaeus; エトナの): Aetnaeos . . . ignes、ウルカヌスの 857

858 Mulciber et ualidis fuluum domat ictibus aurum.
- [2] 863 Mulciber, et validis fulvum domat ignibus aurum.
- [3] 858 Mulciber et ualidis fuluum domat ictibus aurum.
- [4] 858 Mulciber et validis fulvum domat ictibus aurum.
  - Mulciber (VULCANUS; ウルカヌス): Mulciber:エトナの火を掻き立てる
- [6] 858 Mulciber et validis fulvum domat ictibus aurum.

859 Mox effecta refert diuinis artibus arma.
- [2] 864 Mox effecta refert divinis artibus arma,
- [3] 859 Mox effecta refert diuinis artibus arma;
- [4] 859 Mox effecta refert divinis artibus arma
- [6] 859 mox effecta refert divinis artibus arma,
  - artibus (Vulcanus; ウルカヌス): divinis artibus 859

860 Euolat inde Thetis; quae postquam magnus Achilles
- [2] 865 Et donat Thetidi : quae postquam magnus Achilles
  - … *Evolat ad Thetidem*（テティスのもとへ飛び去る）とするが、これはホメーロスによって足萎えと描かれているウゥルカーヌスには全くそぐわない。――そしてそれゆえに彼はカトゥッルス（Carm. 31）によって「鈍足の神（*tardipes Deus*）」と呼ばれている。パリ編者。…
- [3] 860 Euolat inde Thetis. quae postquam magnus Achilles
- [4] 860 Et donat Thetidi. Quae postquam magnus Achilles
  - Achilles (ACHILLES; アキレウス): — 偉大なる者、ウルカヌスの武具をまとう
  - Thetidi (THETIS; テティス): Thetidi:ウルカヌスがテティスに武具を贈る
- [6] 860 evolat et Thetis. . . . . . . . . . . . .
- [6] 860 . . . . . . . quae postquam magnus Achilles
  - Achilles (Achilles; アキレウス): magnus -es 860. 995
  - Thetis (Thetis; テティス): Thetis 83. 860

861 induit, in clipeum uultus conuertit atroces.
- [2] 866 Induit, in clypeum vultus convertit atroces.
- [3] 861 Induit, in clipeum uultus conuertit atroces.
- [4] 861 Induit, in clipeum vultus convertit atroces.
- [6] 861 induit, in clipeum vultus convertit atroces.

862 Illic Ignipotens mundi caelauerat arcem
- [2] 867 Iliic Ignipotens mundi caeiaverat axem,
  - *Illic Ignipotens*、すなわちウルカヌス。105 行への注で述べたところを見よ。…作者は Ovid. Metam. XIII, 110: « Nec clypeus vasti caelatus imagine mundi » を念頭に置いているように思われる。…
- [3] 862 Illic Ignipotens mundi caelauerat arcem
- [4] 862 Illic Ignipotens mundi caelaverat arcem
  - Ignipotens (VULCANUS; ウルカヌス): Ignipotens:火の主が盾に世界を彫り刻んでいた
- [6] 862 illic Ignipotens mundi caelaverat arcem
  - Ignipotens (Ignipotens; イグニポテンス): Ignipotens 862

863 sideraque et liquidis redimitas undique nymphis
- [2] 868 Sideraque, et [liquidas redimitas undique Nymphas.
- [3] 863 Sideraque et liquido redimitum lumine Olympum,
- [4] 863 below Sideraque et liquidas redimitas undique Nymphas
- [6] 863 sideraque et liquidis redimitas undique nymphas
  - nymphas (nympha; ニンフ): nymphas 863(?)

864 Oceani terras et cinctum Nerea circum
- [2] 870 Oceanum ] terras , et euntem Nerea circum ,
  - … われらの詩人が疑いなく念頭に置いたオウィディウスの Met. II, 6 に次のようにあるのと同様である: « Aequora caelarat medias cingentia terras »。プリスキアヌス『周航記』の冒頭: « Oceanum, tellus quo cingitur aequore tota »。またわれわれがルキリウスの『エトナ』93 行への注で述べたところと比較せよ。…しかしながら *cinctus circum* は作者によって意味を変えて *circumductus*（巡らされた）あるいは *circumfusus*（周りに注がれた）の代わりに置かれた可能性もあり、したがって *cinctum* に
  - **(cont.)** （前頁からの続き）おそらく *ductum* や *fusum* を代入することもできよう。Ovid. Met. I, 12: « Et circumfuso pendebat in aere tellus »。――動詞 *cingere* は詩人たちによって、*circumducere*（巡らす）、*circum adponere*（周囲に配する）あるいは *adjungere*（周囲に添える）の意で時折用いられるようである。シリウス VIII, 617: « Non totidem Ilva viros, sed lectos cingere ferrum »；もっともそこでは *gignere ferrum* あるいは *stringere* と読むのを好む者もいる。しかしポムポニウス・メラはまさにわれらの詩人と同じように *cingere* を用いたように見受けられる（第3巻第1章）: « Restat ille circuitus, quem, ut initio diximus, cingit Oceanus »、すなわち「巡らしている（*circumducit*）」。…
- [3] 864 Omnes et terras et cinctum Nerea circum;
- [4] 864 below Oceanum terris et cinctum Nerea circum.
  - Nerea (NEREUS; ネレウス): [ウルカヌスはアキレウスの盾にネレウスを作っていた]
  - Oceanum (OCEANUS; オケアヌス): [—]
- [6] 864 Oceanum terris et cinctum Nerea circum
  - Nerea (Nereus; ネレウス): Nerea 864
  - Oceanum (Oceanus; オケアヌス): Oceanum(?) 864

865 astrorumque uices dimensaque tempora noctis,
- [2] 871 Annorumque vices, dimensaque tempora noclis,
- [3] 865 Astrorumque uices dimensaque tempora noctis,
  - **865—67** 『ベレンガリウスの事績』I 108–110 が有する
- [4] 865 Astrorumque vices dimensaque tempora noctis,
- [6] 865 annorumque vices dimensaque tempora noctis,
  - **865—867** （証言） = 『ベレンガリウスの事績』1, 108–110

866 quattuor et mundi partes, quantum Arctos ab Austro
- [2] 872 Quattuor et mundi partes, quanturo Arctos ab Austro,
- [3] 866 Quattuor et mundi partes, quantum Arctus ab Austro
- [4] 866 Quattuor et mundi partes, quantum Arctus ab Austro
  - Arctus (ARCTUS; アルクトス)
  - Austro (AUSTER; アウステル): ab Austro:アルクトスはアウステルから遠く離れている
- [6] 866 quattuor et mundi partes, quantum Arctos ab Austro
  - Arctos (Arctos; アルクトス): Arctos 866:天の一領域
  - Austro (Auster; アウステル): quantum Arctos ab Austro . . . distaret 866
  - occasus (occasus; 日没): [太陽の]沈む領域:866
  - ortu (ortus; 日の出): [太陽の]昇る領域:866

867 et quantum occasus roseo distaret ab ortu,
- [2] 873 Et quantum Occasus roseo distaret ab Ortu:
- [3] 867 Et quantum occasus roseo distaret ab ortu,
- [4] 867 Et quantum occasus roseo distaret ab ortu,
- [6] 867 et quantum occasus roseo distaret ab ortu,

868 Lucifer unde suis, unde Hesperus unus uterque
- [2] 874 Lucifer unde suis, unde Hesperus, unus uterque,
  - … 詩人たちはルキフェル（明けの明星）とヘスペルス（宵の明星）を名前の上では区別するが、同一の星と認めているからである。――本著作第2巻232頁以下の『マエケナス哀歌』補論、129-132行に対するわれわれの注を参照せよ。パリ編者。――セネカは『ヒッポリュトス』750行でこれを明瞭に示している: « Qualis est primas referens tenebras Nuntius noctis, modo lotus undis Hesperus, pulsis iterum tenebris Lucifer idem »。同一の星であることを示すため、別のものとして現れるときには早馬を乗り換える（または軽業師のように馬を乗り移る）のだと詩人たちは言う。スタティウスは Theb. VI, 237 で雄弁に語っている: « Roscida jam novies caelo dimiserat astra Lucifer, et totidem Lunae praevenerat ignes Mutato nocturnus equo; nec conscia fallit Sidera, et alterno deprenditur unus in ortu »。したがって、ルキフェルとヘスペルスは乗り換えた馬によって見分けられるため、われらの詩人は両者がそれぞれの馬で昇る（*suis equis*）と述べているのである。もっとも他の諸本、とりわけライプツィヒ版や G. 2 は *aquis*（水から）と書いており、高名なアントン・デ・ローイ（99頁）もそれを好んでいるが。なお、私はルキリウスの『エトナ』の中に、われらの詩人がここで暗示していると思われる詩行が読まれることに気づいた。なぜならその 168 行に: « Hinc furtim Borea atque Noto, nunc unus uterque »；また 239 行に: « Lucifer unde micet, quave Hesperus, unde Bootes » とあるからである。ルキリウスのもう一つの類似の箇所を次の行の注で挙げる。ここから、われらの作者がルキリウスを読んでいたという論拠を容易に引き出すことができよう。
- [3] 868 Lucifer unde suis, unde Hesperus unus uterque
- [4] 868 Lucifer unde suis, unde Hesperus unus uterque
  - Hesperus (HESPERUS; ヘスペルス): 昇る
  - Lucifer (LUCIFER; ルキフェル)
- [6] 868 Lucifer unde suis, unde Hesperus unus uterque
  - Hesperus (Hesperus; ヘスペルス): Lucifer . . . Hesperus, unus uterque 868
  - Lucifer (Lucifer; ルキフェル): Lucifer 868

869 exoreretur equis, et quantum in orbe mearet
- [2] 875 Exoreretur equis ; quantus Sol orbe mearet ,
  - **(cont.)** … というのも、ルキフェルとヘスペルス、次いで月が名指されながら、なぜ特に名指されるべきであり、引用したルキリウスの詩行や、作者がこの箇所で忠実に表現しているホメロス自身（Il. XVIII, 484）においてなされているように月と結合されるべき太陽について沈黙しているのか。…
- [3] 869 Exoreretur equis, et quantus in orbe mearet
- [4] 869 Exoreretur equis, et quantus in orbe mearet
- [6] 869 exoreretur equis, et quantus in orbe mearet

869a
- [2] —
- [3] —
- [4] 869 bis \<Sol. . . . . . . . . . . . . . >
- [6] —

870 Luna caua et nitida lustraret lampade caelum;
- [2] 876 Quantum et Luna cava lustraret lampade terras.
- [3] 870 Luna caua et nitida lustraret lampade caelum;
- [4] 870 Luna cava et nitida lustraret lampade caelum;
- [6] 870 Luna cava et nitida lustraret lampade caelum;
  - Luna (Luna; ルナ): Luna cava 870

871 addideratque fretis sua numina: Nerea magnum
- [2] 877 Addideratque freto sua numina, Nerea magnum,
- [3] 871 Addideratque fretis sua numina, Nerea magnum
- [4] 871 Addideratque fretis sua numina, Nerea magnum
  - Nerea (NEREUS; ネレウス): — 同じ盾に、偉大な者として
- [6] 871 addideratque fretis sua numina: Nerea magnum
  - Nerea (Nereus; ネレウス): -a magnum 871

872 Oceanumque senem nec eundem Protea semper,
- [2] 878 Oceanumque senem , nec eumdem Protea semper,
- [3] 872 Oceanumque senem nec eundem Protea semper,
- [4] 872 Oceanumque senem nec eundem Protea semper,
  - Oceanum (OCEANUS; オケアヌス): Oceanum senem:ウルカヌスはアキレウスの盾に老オケアヌスを作っていた
  - Protea (PROTEUS; プロテウス): Protea:常に同じ姿ではないプロテウス(ウルカヌスがアキレウスの盾に作っていた)
- [6] 872 Oceanumque senem nec eundem Protea semper,
  - Oceanum (Oceanus; オケアヌス): -um . . . senem 872
  - Protea (Proteus; プロテウス): nec eundem Protea semper 872

873 Tritonasque feros et amantem Dorida fluctus;
- [2] 879 Tritonesque feros, et amantem Dorida fluctus.
  - *Tritonesque feros*（そして野性的なトリトンたち）。彼らが *feri*（野獣のような）と呼ばれるのは、体の一部が怪獣のようであり、足の代わりに魚の尾を持っているからである。クラウディアヌスも『ホノリウスの婚礼』138 および 145 行でトリトンを *ferus* および *semifer*（半獣の）と呼んでいる。…
- [3] 874 Tritonesque feros et amantem Dorida fluctus;
- [4] 873 Tritonesque feros et amantem Dorida fluctus;
  - Dorida (DORIS; ドリス): Dorida:波を愛するドリス
  - Tritones (TRITONES; トリトンたち): Tritones feros:ウルカヌスが盾に猛きトリトンたちを作っていた
- [6] 873 Tritonasque feros et amantem Dorida fluctus;
  - Dorida (Doris; ドリス): amantem Dorida fluctus 873
  - Tritonas (Triton; トリトン): Tritonas (-es trad.) . . . feros 873

874 fecerat et liquidas mira Nereidas arte.
- [2] 869 Fecerat et mira liquidas Nereidas arte,
- [3] 873 Fecerat et liquidas mira Nereidas arte
- [4] 863 bis below Fecerat et mira liquidas Nereidas arte
- [4] 874 Fecerat et liquidas mira Nereidas arte
  - Nereidas (NEREIDES; ネレイスたち): Nereidas:ウルカヌスはアキレウスの盾にネレイスたちを作っていた
  - Nereidas (NEREIDES; ネレイスたち): [および]
- [6] [874] [fecerat et mire liquidas Nereidos arces]
- [6] 874 fecerat et liquidas mira Nereidas arte.
  - Nereidas (Nereis; ネレイス): liquidas . . . Nereidas 874

875 Terra gerit siluas horrendaque monstra ferarum
- [2] 880 Terra gerit sihras, horrendaque monstra ferarum,
  - *Terra gerit silvas*（大地は森を宿す）。この行および次の行において、作者はオウィディウスの次の詩行（Met. II, 15）を念頭に置き、ほぼそのまま表現したように見受けられる: « Terra viros, urbesque gerit, silvasque, ferasque, Fluminaque, et Nymphas, et caetera numina ruris »。
- [3] 875 Terra gerit siluas horrendaque monstra ferarum
- [4] 875 Terra gerit silvas horrendaque monstra ferarum
- [6] 875 terra gerit silvas horrendaque monstra ferarum

876 fluminaque et montes cumque altis oppida muris,
- [2] 881 Fluniinaque et montes, cumque aitis oppida muris,
- [3] 876 Fluminaque et montes cumque altis oppida muris,
- [4] 876 Fluminaque et montes cumque altis oppida muris,
- [6] 876 fluminaque et montes cumque altis oppida muris,

877 in quibus exercent leges annosaque iura
- [2] 882 In quibus exercent leges animosaque jura
  - *Animosaque jura*（そして気脈あふれる法）。バルトは Adv. 2809 頁で、これが極めて巧みに言われていると考えている。法ははるかに強大な悪徳に立ち向かうものだからである。
- [3] 877 In quibus exercent leges annosaque iura
- [4] 877 In quibus exercent leges animosaque jura
- [6] 877 in quibus exercent leges annosaque iura

878 certantes populi; sedet illic aequus utrisque
- [2] 883 Certantes populi : sedet illic sequus utrique
  - … 諸刊本では *utrique* であり、すなわち個々の訴訟における原告と被告の双方に対して、ということである。
- [3] 878 Certantes populi; sedet illic aequus utrisque
- [4] 878 Certantes populi; sedet illic aequus utrisque
- [6] 878 certantes populi; sedet illic aequus utrisque

879 iudex et litem discernit fronte serena.
- [2] 884 Judex, et litem discernit fromte severa.
- [3] 879 Iudex et litem discernit fronte serena.
- [4] 879 Judex et litem discernit fronte serena.
- [6] 879 iudex et litem discernit fronte severa.

880 Parte alia castae resonant Paeana puellae
- [2] 885 Parte alia castae resonant Paeana puellae ,
- [3] 880 Parte alia resonant castae paeana puellae
  - **880—83** , 85, 88 『ベレンガリウスの事績』I 64–69 が有する（880 は変更なし）
- [4] 880 Parte alia resonant castae paeana puellae
- [6] 880 parte alia castae resonant Paeana puellae
  - （証言） *puellae* — 883 『ベレンガリウスの事績』1, 64–67 に採録
  - puellae (Musa; ムーサ): castae . . . puellae 880
  - Paeana (Paean; パエアン): resonant Paeana puellae 880

881 dantque choros molles et tympana dextera pulsat;
- [2] 886 Dantque choros molles: haec dextra tympana pulsat,
- [3] 881 Dantque choros molles; haec dextra tympana pulsat,
- [4] 881 Dantque choros molles; haec dextra tympana pulsat,
- [6] 881 dantque choros molles et tympana dextera pulsat:

882 ille lyrae graciles extenso pollice chordas
- [2] 887 Illa lyrae graciles extenso pollice chordas
- [3] 882 Illa lyrae graciles extenso pollice chordas
- [4] 882 Illa lyrae graciles extenso pollice chordas
- [6] 882 ille lyrae graciles extenso pollice chordas

883 percurrit septemque modos modulatur auenis:
- [2] 888 Percurrit , septemque modos modulatur avenis.
- [3] 883 Percurrit septemque modis modulatur amoenis
- [4] 883 Percurrit septemque modis modulatur amoenis
- [6] 883 percurrit septemque modos modulatur avenis:

884 carmina componunt mundi resonantia motum.
- [2] 889 Carmina componunt mundi resonantia motum :
  - … 作者は天体の調和（ハーモニー）に関する古代人の見解に触れており、これについてはアウグスティヌスに宛てたリケンティウスの詩の冒頭で論じた。
- [3] 884 Stamina compositum mundi resonantia motum.
- [4] 884 Stamina compositum mundi resonantia motum.
- [6] 884 carmina componunt mundi resonantia motum.

885 Rura colunt alii, sulcant grauia arua iuuenci
- [2] 890 Rura colunt alii, sulcant gravia arva juvenci,
- [3] 885 Rura colunt alii, sulcant grauia arua iuuenci
- [4] 885 Rura colunt alii, sulcant gravia arva juvenci
- [6] 885 rura colunt alii, sulcant gravia arva iuvenci
  - （証言） = 『ベレンガリウスの事績』1, 68

886 maturasque metit robustus messor aristas
- [2] 891 Maturasque metit robustus messor aristas,
- [3] 886 Maturasque metit robustus messor aristas
- [4] 886 Maturasque metit robustus messor aristas
- [6] 886 maturasque metit robustus messor aristas

887 et gaudet pressis immundus uinitor uuis;
- [2] 892 Et gaudet pressis immundus vinitor uvis.
- [3] 887 Et gaudet pressis inmundus uinitor uuis;
- [4] 887 Et gaudet pressis immundus vinitor uvis;
- [6] 887 et gaudet pressis immundus vinitor uvis;

888 tondent prata greges, pendent in rupe capellae.
- [2] 893 Tondent prata greges , pendent in rupe capellae.
- [3] 888 Tondent prata greges, pendent in rupe capellae.
- [4] 888 Tondent prata greges, pendent in rupe capellae.
- [6] 888 tondent prata greges, pendent in rupe capellae.
  - （証言） = 『ベレンガリウスの事績』1, 69 (*pendentque*)

889 Haec inter mediis stabat Mars aureus armis,
- [2] 894 Hic intermedius stabat Mars aureus armis,
  - … これらの行で提示されている図像それ自体については、本篇末尾の第三補論（Excursus III）を見よ。
- [3] 889 Haec inter mediis stabat Mars aureus armis,
- [4] 889 Haec inter nitidis stabat Mars aureus armis,
  - Mars (MARS; マルス): — 黄金の者、アキレウスの盾の上に立っていた
- [6] 889 haec inter mediis stabat Mars aureus armis,
  - … armis Ω すなわち盾の上に
  - Mars (Mars; マルス): Mars aureus in medio Achillis clipeo 889

890 quem diua poesis reliquae* circaque sedebant
- [2] 895 Diva potens Atropos circa, reliquaeque sedebant
- [3] 890 Post quem diua potens belli; circaque sedebant
- [4] 890 Post quem diva potens belli; circaque sedebant
- [6] 890 quem diva † poesis † reliquae circaque sedebant

891 anguineis maestae Clotho Lachesisque capillis.
- [2] 896 Sanguineis moestae Clotho Lachesisque capiUis.
  - … ［作者が］暗示（仄めかし）をした［と思われるのは］―
  - **(cont.)** （前頁からの続き）ウェルギリウスの半行（*Aen.* III, 64: « Caeruleis maestae vittis »）をほのめかしているように思われる。――また運命の女神たち（パルカたち）について、カトゥルスは『ペレウスの祝婚歌』(*Epithal. Pel.*) p. 186 Voss. で次のように述べている: « At roseae niveo residebant vertice vittae »。パリ編者。
- [3] 891 Sanguineis maestae Clotho Lachesisque quasillis.
- [4] 891 Sanguineis maestae Clotho Lachesisque quasillis.
  - Clotho (CLOTHO; クロト): (アキレウスの盾の上に)
  - Lachesis (LACHESIS; ラケシス): (アキレウスの盾の上に)
- [6] 891 anguineis maestae Clotho Lachesisque capillis.
  - Clotho (Clotho; クロト): Clotho 891
  - Lachesis (Lachesis; ラケシス): Lachesis 891

## Book 19

892 Talibus ornatus donis Thetideius heros
- [2] 897 XIX et XX. Talibus ornatus donis Thetideius heros
- [3] 892 Talibus ornatus donis Thetideius heros
- [4] 892 Talibus ornatus donis Thetideius heros
  - Thetideius (ACHILLES; アキレウス): — ウルカヌスの武具で飾られて
- [6] 892 talibus ornatus donis Thetideius heros
  - Thetideius (Thetideius; テティスの子): Thetideius heros 690. 892:アキレウス

893 in medias acies immani turbine fertur,
- [2] 898 In medias acies iminani turbine fertur.
- [3] 893 In medias acies inmani turbine fertur,
- [4] 893 In medias acies immani turbine fertur,
- [6] 893 in medias acies immani turbine fertur,

894 cui uires praebet casta cum Pallade Iuno
- [2] 899 Cui vires praebet casta cum Pallade Juno,
- [3] 894 Cui uires praebet cum casta Pallade Iuno
- [4] 894 Cui vires praebet casta cum Pallade Juno
  - Juno (JUNO; ユノー): — ミネルウァとともにアキレウスに力を与える
  - Pallade (MINERVA; ミネルウァ): 貞潔なパラスとともにユノーがアキレウスに力を与える
- [6] 894 cui vires praebet casta cum Pallade Iuno
  - Iuno (Iuno; ユノー): Iuno 98. 894
  - Pallade (Pallas; パラス): casta cum -de 532. 894

895 dantque animos iuueni. Vidit Cythereius heros
- [2] 900 Dantque animos juveni : videt hunc Cytbereiusherosgoo
- [3] 895 Dantque animos iuueni; contra Cythereius heros
- [4] 895 Dantque animos juveni ; contra Cythereius heros
  - Cythereius (AENEAS; アイネイアス): Cythereius heros:アキレウスに立ち向かい、ネプトゥヌスに救われる
- [6] 895 dantque animos iuveni: vidit Cythereius heros
  - Cythereius (Cythereius; キュテラの): Cythereius heros 895:アイネイアス

896 occurritque uiro, sed non cum uiribus aequis
- [2] 901 Occurritque viro, sed non cum viribus aequis,
  - … 同様にマロー（ウェルギリウス）の Aen. V, 809 で、ネプトゥヌスが次のように述べている: « Pelidae forti Congressum Aeneam, nec Dis, nec viribus aequis »。
- [3] 896 Occurrit feruens; sed enim non uiribus aequis,
- [4] 896 Occurrit fortis, sed enim non viribus aequis,
- [6] 896 occurritque viro, sed non cum viribus aequis

897 Aeacidae nec compar erat, tamen ira coegit
- [2] 902 Aeacidae nec compar erat; tamen ira coegit
  - … だがバルトはこの箇所について『雑考』(*Adv.*) p. 2809 で、作者が後代のラテン語の慣習に従って *compar* の音節を短縮したのだと指摘している。プルデンティウスが『ロマヌス歌』で « Meatus unus impar ad laudes Dei » としているのと同様である。アウィアヌスも二箇所で同様にこの音節を短縮している。すなわち寓話第 11 篇 5 行: « Dispar erat fragili et solidae concordia motus »、および寓話第 18 篇 10 行: « Tantorum solus viribus impar erat »。
- [3] 897 Aeacidae nec erat conpar; tamen ira coegit
- [4] 897 Aeacidae nec erat compar; tamen ira coegit
  - Aeacidae (ACHILLES; アキレウス): Aeacidae:アイネイアスはアエアキデスに匹敵しなかった
- [6] 897 Aeacidae nec † corpus erat, tamen ira coegit
  - Aeacidae (Aeacides (Achilles); アエアキデス（アキレウス）): -dae 897

898 conferre inuictis iuuenem cum uiribus arma.
- [2] 903 Conferre invictis juvenem cum viribus arma.
- [3] 898 Conferre inuictis iuuenem cum uiribus arma.
- [4] 898 Conferre invictis juvenem cum viribus arma.
- [6] 898 conferre invictis iuvenem cum viribus arma.

899 Quem nisi seruasset magnarum rector aquarum,
- [2] 904 Quem nisi servasset magnarum rector aquarum,
  - *Rector aquarum*（水の支配者）、すなわちネプトゥヌス。アイネイアスがアキレウスと交戦した際に、彼によって救われ戦いから救出されたことは、ホメロスが『イリアス』XX, 325 以下で語り、ウェルギリウスの Aen. V, 804 以下でもネプトゥヌス自身が誇らしげに語っている。
- [3] 899 Quem nisi seruasset magnarum rector aquarum,
- [4] 899 Quem nisi servasset magnarum rector aquarum,
- [6] 899 quem nisi servasset magnarum rector aquarum,
  - rector (Neptunus; ネプトゥヌス): magnarum rector aquarum 899 を参照

900 ut profugus laetis Troiam repararet in aruis
- [2] 905 Ut profugus Latiis Trojam repararet in arvis,
  - … ウェルギリウスも、トロイアがラティウムにもたらされた（Aeneid. I, 6）、トロイアがイタリアで再建されるべきである（Aen. III, 504）、イリオンがイタリアへ運ばれる（Aen. I, 68）と言う際に、このようにしばしば述べている。そしてオウィディウスも、まったくわれらの詩人と同様に、Fast. IV, 251 で歌っている: « Quum Trojam Aeneas Italos portaret in agros »。――われらのオウィディウス版第 6 巻 p. 251 を参照。パリ編者。
- [3] 900 Ut profugus laetis Troiam repararet in aruis
- [4] 900 Ut profugus Latiis Trojam repararet in arvis
  - Latiis (LATIUS; ラティウムの): Latiis in arvis:ラティウムの野に
  - Trojam (TROJA; トロイア): — ラティウムの野に再建されたトロイア
- [6] 900 ut profugus Latiis Troiam repararet in arvis
  - profugus (Aeneas; アイネイアス): profugus 900
  - Latiis (Latius; ラティウムの): *Latiis (laetis trad.) . . . in arvis 900
  - Troiam (Troia; トロイア): Latiis -iam repararet in arvis 900

901 Augustumque genus claris submitteret astris,
- [2] 906 Augustumque genus cseli submitteret astris , '
  - … *Submitteret astris* は、ここから「星々へと送り出す」、あるいは「名声と栄光によって星々へと導く」と解釈することもできるが、私はむしろ、アウグストゥスの血統を生命の中へ、天の下へと生み出すことを意味すると解釈したい。ウェルギリウスが Aeneid. VI, 790 でアウグストゥスの血統について次のように述べているのと同様である: « Hic Caesar et omnis Iuli Progenies, magnum caeli ventura sub axem »。…なお、バルトは前掲箇所でこの詩行から、この詩がローマ人によって、そしてローマが君臨するアウグストゥスたちの下でなお繁栄していた時代に書かれたものであると、正当にも推論している。――バルトのこの見解は、ヴェルンスドルフが『イリアス梗概』序論（*Prooemium*）の冒頭で報告している。パリ編者。
- [3] 901 Augustumque genus claris submitteret astris,
- [4] 901 Augustumque genus claris submitteret astris,
  - Augustum (AUGUSTUM; アウグストゥスの): genus(アウグストゥスの一族)
- [6] 901 Augustumque genus claris submitteret astris,
  - Augustum (Augustus; アウグストゥスの): Augustum . . . genus 901:ユリウス家

902 non clarae gentis nobis mansisset origo.
- [2] 907 Non clarae gentis nobis mansisset origo.
  - … なお、ユリウス氏族が卓越して（κατ᾽ ἐξοχὴν）*clara*（輝かしい）と呼ばれたのは、ホラティウスやウェルギリウスが言う「ユリウスの星（カエサルの彗星）」あるいは「ディオネの星」の出現によって、ひときわ明示されたと考えられていたからである。――われらの詩人は、ウェルギリウスの流儀に倣ってアイネイアスをユリウス氏族の始祖と呼んでいる。ウェルギリウスは Aeneid. XII, v. 166 で « Hinc pater Aeneas Romanae stirpis origo » と歌い、また Aen. I, 286 では « Nascetur pulchra Trojanus origine Caesar Julius, a magno demissum nomen Iulo » と歌っている。
- [3] 902 Non carae gentis nobis mansisset origo.
- [4] 902 Non pulcrae gentis nobis mansisset origo.
- [6] 902 non clarae gentis nobis mansisset origo.
  - gentis (Augustus; アウグストゥスの): clarae gentis 902 を参照

903 Inde agit Aeacides infesta cuspide Teucros
- [2] 908 Inde agit Aeacides infesta cuspide Teucros,
- [3] 903 Inde agit Aeacides infesta cuspide Teucros
- [4] 903 Inde agit Aeacides infesta cuspide Teucros
  - Aeacides (ACHILLES; アキレウス): — 槍でトロイア人を追い立てる
  - Teucros (TROJANI; トロイア人): Teucros:アキレウスは槍でテウクロイを追い立てる
- [6] 903 inde agit Aeacides infesta cuspide Teucros
  - Aeacides (Aeacides (Achilles); アエアキデス（アキレウス）): -ēs 903
  - Teucros (Teucri; テウクロイ): -os 424. 903

904 ingentemque modum prosternit caede uirorum,
- [2] 909 Ingentemque manum prosternit caede virorum,
  - … *modus* はしばしばいかなる大きさや尺度に対しても用いられる語であり、ホラティウスが Sat. II, 2, 36 で « Scilicet illis Majorem natura modum dedit »、同 II, 6, 1 で « modus agri non ita magnus » としているのと同様である。
- [3] 904 Ingentemque modum prosternit caede uirorum,
- [4] 904 Ingentemque modum prosternit caede virorum,
- [6] 904 ingentemque modum prosternit caede virorum,

905 sanguinis Hectorei sitiens. At Dardana pubes
- [2] 910 Sanguinis Hectorei sitiens : at Dardana pubes
- [3] 905 Sanguinis Hectorei sitiens; at Dardana pubes
- [4] 905 Sanguinis Hectorei sitiens; at Dardana pubes
  - Hectorei (HECTOREUS; ヘクトルの): Hectorei sanguinis
  - Dardana (TROJANI; トロイア人): Dardana pubes:ダルダニアの若者たちがクサントスへ逃げ込む
- [6] 905 sanguinis Hectorei sitiens; at Dardana pubes
  - Dardana (Dardanus; ダルダニアの): Dardana pubes 905
  - Hectorei (Hectoreus; ヘクトルの): sanguinis Hectorei 905

906 confugit ad Xanthi rapidos perterrita fluctus
- [2] 911 XXI. Confugit ad Xanthi rapidos perterrita fluctus ,
- [3] 906 Confugit ad Xanthi rapidos perterrita fluctus
- [4] 906 Confugit ad Xanthi rapidos perterrita fluctus
  - Xanthi (XANTHUS fluvius; クサントス、河): トロイア人はクサントスの波へ逃げる
- [6] 906 confugit ad Xanthi rapidos perterrita fluctus
  - Xanthi (Xanthus (fluvius); クサントス(河)): ad -i fluctus 906

907 auxiliumque petit diuini fluminis; ille
- [2] 912 Auxiliumque petit divini fluminis : ille
- [3] 907 Auxiliumque petit diuini fluminis; ille
- [4] 907 Auxiliumque petit divini fluminis; ille
- [6] 907 auxiliumque petit divini fluminis; ille
  - fluminis (Xanthus (fluvius); クサントス(河)): divini fluminis 907 を参照

908 instat et in mediis pugnatur gurgitis undis.
- [2] 913 Instat, et in mediis pugnatur gurgitis undis;
- [3] 908 Instat et in mediis bellatur gurgitis undis.
- [4] 908 Instat et in mediis bellatur gurgitis undis.
- [6] 908 instat et in mediis bellatur gurgitis undis.

909 Ira dabat uires; stringuntur sanguine ripae
- [2] 914 Ira dabat vires, stringuntur sanguine ripae,
- [3] 909 Ira dabat uires; stringuntur sanguine ripae
- [4] 909 Ira dabat vires; stringuntur sanguine ripae
- [6] 909 ira dabat vires; stringuntur sanguine ripae
  - … stringuntur … ウェルギリウス『アエネーイス』8, 62 を参照

910 sparsaque per totos uoluuntur corpora fluctus.
- [2] 915 Sparsaque per totos volvuntur corpora fiuctus.
- [3] 910 Sparsaque per totos uoluuntur corpora fluctus.
- [4] 910 Sparsaque per totos volvuntur corpora fluctus.
- [6] 910 sparsaque per totos volvuntur corpora fluctus.

## Book 20

911 At Venus et Phrygiae gentis tutator Apollo
- [2] 916 At Venus et Phrygiae gentis tutator Apollo
- [3] 911 At Uenus et Phrygiae gentis tutator Apollo
- [4] 911 At Venus et Phrygiae gentis tutator Apollo
  - Apollo (APOLLO; アポロ): — プリュギアの民の守護者、ウェヌスとともに、ギリシア人に向けてクサントスの波を立ち上がらせる
  - Phrygiae (TROJANI; トロイア人): — その守護者アポロ
  - Venus (VENUS; ウェヌス): — とアポロがギリシア人に向けてクサントスの波を立ち上がらせる
- [6] 911 at Venus et Phrygiae gentis tutator Apollo
  - Apollo (Apollo; アポロ): Phrygiae gentis tutator -o 911
  - Phrygiae (Phrygius; プリュギアの): -iae gentis 911
  - Venus (Venus; ウェヌス): Venus 315. 464. 911

912 cogunt in Danaos Xanthi consurgere fluctus,
- [2] 917 Cogunt in Danaos Xanthi consurgere fluctus ,
- [3] 912 Cogunt in Danaos Xanthi consurgere fluctus,
- [4] 912 Cogunt in Danaos Xanthi consurgere fluctus,
  - Danaos (GRAI; ギリシア人): ダナオイに向けて、ウェヌスとアポロがクサントスの波を立ち上がらせる
  - Xanthi (XANTHUS fluvius; クサントス、河): — アポロとウェヌスがギリシア人に向けてクサントスの波を立ち上がらせる
- [6] 912 cogunt in Danaos Xanthi consurgere fluctus,
  - Danaos (Danai; ダナオイ): -os 45. 492. 659. 808. 912. 950. 1001
  - Xanthi (Xanthus (fluvius); クサントス(河)): -i . . . fluctus 912

913 ut fera terribili miscentem proelia dextra
- [2] 918 Ut fera terribili miscentem praelia dextra
- [3] 913 Ut fera terribili miscentem praelia dextra
- [4] 913 Ut fera terribili miscentem proelia dextra
- [6] 913 ut fera terribili miscentem proelia dextra

914 obruat Aeaciden; qui protinus undique totis
- [2] 919 Obruat ,acidem, qui protinus undique totis
- [3] 914 Obruat Aeaciden: qui protinus undique totis
- [4] 914 Obruat Aeaciden : qui protinus undique totis
  - Aeaciden (ACHILLES; アキレウス): Aeaciden:クサントスがアエアキデスを圧倒するように
- [6] 914 obruat Aeaciden: qui protinus undique totis
  - Aeaciden (Aeacides (Achilles); アエアキデス（アキレウス）): -den 914

915 exspatiatur aquis et uasto gurgite praeceps
- [2] 920 Impediatur aquis : sed vasto gurgite praaceps
- [3] 915 Expatiatur aquis et uasto gurgite praeceps
- [4] 915 Exspatiatur aquis et vasto gurgite praeceps
- [6] 915 expatiatur aquis et vasto gurgite praeceps
  - Expatiatur … (オウィディウス『変身物語』1, 285 を参照) …

916 uoluitur atque uirum torrentibus impedit undis
- [2] 921 Yolvitur, atque virum torrentibus impedit undis,
- [3] 916 Uoluitur atque uirum torrentibus inpedit undis
- [4] 916 Volvitur atque virum torrentibus impedit undis
- [6] 916 volvitur atque virum torrentibus inpedit undis

917 praetardatque gradus. Ille omni corpore saeuas
- [2] 922 Praetardatque gradus : ille omni corpore saevas
  - … スタティウス『テーバイス』II, 671: « Tardatique gradus »。もっとも、動詞 *praetardo* は辞書に見当たらないようである。
- [3] 917 Praetardatque gradus; ille omni corpore saeuas
- [4] 917 Praetardatque gradus; ille omni corpore saevas
- [6] 917 praetardatque gradus; ille omni corpore saevas

918 contra pugnat aquas aduersaque flumina rumpit
- [2] 923 Contra pugnat aquas , adversaque flumina rumpit ,
- [3] 918 Contra pugnat aquas aduersaque flumina rumpit
- [4] 918 Contra pugnat aquas adversaque flumina rumpit
- [6] 918 contra pugnat aquas adversaque flumina rumpit

919 et modo disiectos umeris modo pectore uasto
- [2] 924 Et modo disjectos humeris, modo pectore vasto
- [3] 919 Et modo disiectos umeris modo pectore uasto
- [4] 919 Et modo disjectos umeris modo pectore vasto
- [6] 919 et modo disiectos umeris modo pectore vasto

920 propellit fluctus. Quem longe prouida Iuno
- [2] 925 Propellit fluctus, quem longe provida Juno
- [3] 920 Propellit fluctus. quem longe prouida Iuno
- [4] 920 Propellit fluctus. Quem longe provida Juno
  - Juno (JUNO; ユノー): — 遠くまで見通す者、クサントスの波と戦うアキレウスを守る
- [6] 920 propellit fluctus. quem longe provida Iuno
  - Iuno (Iuno; ユノー): longe provida -o 920

921 asseruit, rapidae quia cederet, ignibus, undae,
- [2] 926 Adseruit, rapidae ne cederet ictibus undae:
  - … すなわち、支えた、力づけたということである。G. 2 は *Imbribus*, *ignibus*, *fluctibus undae* を掲げる。なおユノーがアキレウスを助けたのは、彼の救援のためにウルカヌスを奮起させ、河の堤と平野を焼き払わせたことによる。
- [3] 921 Asseruit, rabidae qua cederet ictibus undae.
- [4] 921 Asseruit, rabidaene cederet ignibus undae.
  - … 筆者としてはクーテンの提案に従って ignibus を保持した。『イリアス』XXI, 342, 356, 361, 365 を参照。…
- [6] 921 asseruit, rapidae quia cederet, ignibus, undae,
  - … ignibus は asseruit と結びつけるべし (Thesaurus II p. 864 を参照)。倒置法については 573行 natus, 852行 uictor を参照

922 sanctaque pugnarunt inter se numina diuum.
- [2] 927 Sanctaque pugnarunt inter se numina Divum.
  - … この詩行において作者は、ホメロスの『イリアス』XXI, vv. 385–515 で神々と女神たちがトロイア勢を巡って戦う争いや戦闘――マルスとミネルウァ、ネプトゥヌスとアポロ、ユノーとディアナ――について、いかにもあまりに簡潔にしか触れていない。
- [3] 922 Sanctaque pugnarunt inter se numina diuum.
- [4] 922 Sanctaque pugnarunt inter se numina divum.
- [6] 922 sanctaque pugnarunt inter se numina divum.

923 Rursus agit Phrygias ingenti caede cateruas
- [2] 928 Rursus agit Phrygias ingenti caede catervas
- [3] 923 Rursus agit Phrygias ingenti caede cateruas
- [4] 923 Rursus agit Phrygias ingenti caede catervas
  - Phrygias (TROJANI; トロイア人): Phrygiae catervae Phrygias catervas:アキレウスはプリュギアの部隊を大殺戮で追い立てる
- [6] 923 rursus agit Phrygias ingenti caede catervas
  - Phrygias (Phrygius; プリュギアの): -ias . . . catervas 923

924 horridus Aeacides bellique ardore resumpto
- [2] 929 Horridus Aeacides, bellique ardore resumpto
- [3] 924 Horridus Aeacides bellique ardore resumpto
- [4] 924 Horridus Aeacides bellique ardore resumpto
  - Aeacides (ACHILLES; アキレウス): — 恐るべき者、再びトロイア人を追い立てる
- [6] 924 horridus Aeacides bellique ardore resumpto
  - Aeacides (Aeacides (Achilles); アエアキデス（アキレウス）): horridus -es 924

925 funereas acies horrendaque proelia miscet.
- [2] 930 Funereas acies borrendaque praelia miscet.
- [3] 925 Funereas acies horrendaque praelia miscet.
- [4] 925 Funereas acies horrendaque proelia miscet.
- [6] 925 funereas acies horrendaque proelia miscet,

926 Non illum uis ulla mouet, non saeua fatigant
- [2] 931 Non illum vis ulla tenet , non saeva fatigant
- [3] 926 Non illum uis ulla mouet; non saeua fatigat
- [4] 926 Non illum vis ulla movet; non saeva fatigat
- [6] 926 non illum vis ulla movet, non saeva fatigant

927 pectora bellando; uires successus adauget.
- [2] 932 Pectora pugnando; vires successus adauget.
  - … *Vires successus adauget*（成功が力を増す）は、作者が上の 494 行および 768 行で *geminat victoria vires*（勝利が力を倍加させる）と述べたのと同じことである。
- [3] 927 Pectora pugnando; uires successus adauget.
- [4] 927 Pectora pugnando; vires successus adauget.
- [6] 927 pectora bellando; vires successus adauget.

928 Percussi dubitant trepida formidine Troes
- [2] 933 Perculsi dubitant trepida. formidine Troes,
- [3] 928 Percussi dubitant trepida formidine Troes
- [4] 928 Percussi dubitant trepida formidine Troes
  - Troes (TROJANI; トロイア人): — 恐怖でためらう
- [6] 928 percussi dubitant trepida formidine Troes
  - Troes (Tros; トロイア人): Troes 758. 767. 928. 978. 1002、いずれも子音の前または最後の不定の位置で

929 atque intra muros exhausta paene salute
- [2] 934 Atque intra muros exhausta paene salute
  - … ――*Exhausta paene salute*（安全［救い］がほとんど尽き果てて）、すなわち、彼らがほとんど滅びかけ、安全への希望のほぼすべてが消え失せていたとき。ウェルギリウスでは « absumpta salus »（奪い去られた救い、Aen. I, 555）と言われている。
- [3] 929 Aut intra muros exhausta paene salute
- [4] 929 Atque intra muros exhausta paene salute
- [6] 929 atque intra muros exhausta paene salute

930 confugiunt portasque obiecto robore firmant.
- [2] 935 Confugiunt, portasque objecto robore firmant.
  - 683 行を見よ。パリ編者。
- [3] 930 Defugiunt portasque obiecto robore firmant.
- [4] 930 Confugiunt portasque objecto robore firmant.
- [6] 930 confugiunt portasque obiecto robore firmant.

## Book 21

931 Vnus tota salus in quo Troiana manebat
- [2] 936 XXII. Unus, tota salus in quo Trojana manebat,
- [3] 931 Unus tota salus in quo Troiana manebat
- [4] 931 Unus tota salus in quo Trojana manebat
  - Trojana (TROJANUS; トロイアの): salus Trojana:トロイアの救い
- [6] 931 unus tota salus in quo Troiana manebat
  - Troiana (Troianus; トロイアの): salus -na 931

932 Hector adest, quem non durae timor undique mortis,
- [2] 937 Hector adest, quem non durae timor undique mortis»,
- [3] 932 Hector adest, quem non durae timor undique mortis
- [4] 932 Hector adest, quem non durae timor undique mortis
  - Hector (HECTOR; ヘクトル): — そこにいる、トロイアの救いがその身にのみかかっていた者
- [6] 932 Hector adest, quem non durae timor undique mortis,
  - Hector (Hector; ヘクトル): unus tota salus in quo Troiana manebat -or 932

933 non patriae tenuere preces, quin obuius iret
- [2] 938 Nec patriae tenuere preces, c[uin obvius iret,
- [3] 933 Nec patriae tenuere preces, quin obuius iret
- [4] 933 Nec patriae tenuere preces, quin obvius iret
- [6] 933 non patriae tenuere preces, quin obvius iret

934 et contra magnum contendere uellet Achillem.
- [2] 939 Et contra magnum contendere vellet Achillem.
- [3] 934 Et contra magnum contendere uellet Achillem.
- [4] 934 Et contra magnum vellet contendere Achillem.
  - Achillem (ACHILLES; アキレウス): 偉大なアキレウスに対してヘクトルは戦おうとする
- [6] 934 et contra magnum contendere vellet Achillem.
  - Achillem (Achilles; アキレウス): magnum . . . -em 60. 72. 934

935 Quem procul ut uidit tectum caelestibus armis,
- [2] 941 Quem procul ut vidit tectum caelestibus armis,
  - … したがって *in caelestibus armis*（天上の武具を身にまとって）はウルカヌスによって鍛造されたアキレウスの武具と理解すべきであり、マロ（ウェルギリウス）が Aen. XII, 167 でアイネイアスについて « Sidereo flagrans clypeo et caelestibus armis » と述べているのと同様である。そしてヘクトルが
  - **(cont.)** （前頁からの続き）武具に輝くアキレウスを見て恐怖を抱いたことは、ホメロスが『イリアス』XXII, 136 で伝えている。
- [3] 935 Quem procul ut uidit tectum caelestibus armis,
- [4] 935 Quem procul ut vidit tectum caelestibus armis,
- [6] 935 quem procul ut vidit tectum caelestibus armis,

936 ante oculos subito uisa est Tritonia Pallas
- [2] [940] [Ante oculos subito visa est Tritonia Pallas]
  - … そして彼の主張が正しいことは、ホメロスを調べれば容易に理解される。ホメロスは、作者が 952 行で伝えているもの以外のパラスの顕現を伝えていないからである。…
- [3] [936] [Ante oculos subito uisa est Tritonia Pallas]
- [4] 936 below Ante oculos subito visa est Tritonia Pallas
  - Pallas (MINERVA; ミネルウァ): [— トリトニアが突然ヘクトルの目の前に現れる]
- [6] [936] [ante oculos subito visa est Tritonia Pallas]
  - Pallas (Pallas; パラス): [Tritonia -as 936]
  - Tritonia (Tritonia; トリトニア): [-ia Pallas 936]

937 pertimuit clausisque fugit sua moenia circum
- [2] 942 Pertimuit, clausisque fugit sua moenia circum
- [3] 937 Praemetuit clausisque fugit sua moenia circum
- [4] 937 Praemetuit clausisque fugit sua moenia circum
- [6] 937 pertimuit clausisque fugit sua moenia circum

938 infelix portis, sequitur Nereius heros:
- [2] 943 Infelix portis : sequitur Nereius heros.
  - … 下の 980 行でも彼は同様に *Nereius* と呼ばれており、サレイウス［・バッスス］も『ピーソーへの詩』(*Carm. in Pis.*) 164 行でその名を用いている。…
- [3] 938 Infelix portis; sequitur Nereius heros.
- [4] 938 Infelix portis; sequitur Nereius heros.
  - Nereius (ACHILLES; アキレウス): Nereius heros:恐れるヘクトルを追う
- [6] 938 infelix portis; sequitur Nereius heros.
  - Nereius (Nereius; ネレウスの): Nereius heros 938. 975:アキレウス

939 in somnis ueluti, cum pectora terruit ira,
- [2] 944 In somnis veluti , quum pectora terruit ira ,
  - … この詩行は、諸刊本にあるのとは異なって句読点を打ち、後続の行と結びつけられるべきものであり、夢を見ている者たちとの比喩を含んでいる。これはホメロス（『イリアス』XXII, 199 以下）およびウェルギリウス（Aen. XII, 908）が用いたもので、走って他者に追いつくか、あるいは他者から逃げているように思えるのに、眠りに圧迫されて気だるく何も果たせない夢想者のことである。われらの詩人は両者の箇所を念頭に置き、一部を模倣しようとしたように思われるが、成功していない。
- [3] 939 In somnis ueluti, cum pectora terret imago,
- [4] 939 In somnis veluti, cum pectora terruit ira,
- [6] 939 in somnis veluti, cum pectora terruit ira,

940 hic cursu super insequitur, fugere ille uidetur,
- [2] 945 Hic cursu super insequitur, fugere ille videtur,
- [3] 940 Hic cursu super insequitur, fugere ille uidetur,
- [4] 940 Hic cursu super insequitur, fugere ille videtur,
- [6] 940 hic cursu super insequitur, fugere ille videtur,

941 festinantque ambo, gressum labor ipse moratur,
- [2] 946 Festinantque ambo; gressum labor ipse moratur.
  - … 作者は同じ比喩におけるマロ（ウェルギリウス）の思想（Aeneid. XII, 909: « nequidquam avidos extendere cursus Velle videmur, et in mediis conatibus aegri Succidimus »）を表現しようとしたものと思われる。
- [3] 941 Festinantque ambo; gressum labor ipse moratur:
- [4] 941 Festinantque ambo; gressum labor ipse moratur.
- [6] 941 festinantque ambo, gressum labor ipse moratur:

942 alternis poterant insistere coepta periclis,
- [2] 947 Alternis poterant insistere coepta periciis,
  - … *Insistere coepta* はここでは逃走を追撃すること、走って追いつめようとすることを意味し、ウェルギリウスが Georg. III, 164 で *viam insistere*（道を進む）と言ったのと同様である。…
- [3] 942 Alternis poterant insistere coepta periclis,
- [4] 942 below Alternis poterant insistere coepta periclis
- [6] 942 alternis poterant insistere coepta periclis,
  - … 私は次のように解する: ヘクトルもアキレウスも命の危機に瀕していた

943 nec requies aderat, timor undique concitat iras.
- [2] 948 Nec requies aderat, timor undique concitat iras.
  - … というのも、双方の英雄が相手に打ち負かされるのを恐れるあまり、この恐れが彼らの怒りを研ぎ澄まし、抗争を高めるからである。…そしておそらくわれらの詩人は、オウィディウスが Metam. I, 539 で描写した、アポロに追われるダプネの逃走を念頭に置いていたのであろう: « Sic Deus et virgo
  - **(cont.)** （前頁からの続き）est: hic spe celer, illa timore. Qui tamen insequitur, pennis adjutus amoris Ocior est, requiemque negat, tergoque fugacis Imminet »。
- [3] 943 Nec requies aderat: timor hinc, hinc concitat ira.
- [4] 943 Nec requies aderat : timor undique concitat ira.
- [6] 943 nec requies aderat: timor † undique concitat iras.

## Book 22

944 Spectant de muris miseri sua fata parentes
- [2] 949 Spectant de muris miseri sua fata parentes ,
- [3] 944 Spectant de muris miseri sua fata parentes
- [4] 944 Spectant de muris miseri sua fata parentes
- [6] 944 spectant de muris miseri sua fata parentes
  - parentes (Hecabe; ヘカベ): parentes 944 を参照
  - parentes (Priamus; プリアモス): parentes 944

945 pallentemque uident supremo tempore natum
- [2] 950 Pallentemque vident supremo tempore natum,
- [3] 945 Pallentesque uident tum primum cedere natum,
- [4] 945 Pallentemque vident extremo tempore natum,
- [6] 945 pallentemque vident supremo tempore natum
  - natum (Hector; ヘクトル): natum 945. 1033. 1036

946 quem iam summa dies suprema luce premebat.
- [2] 951 Quem jam summa dies extrema luce premebat.
  - … しかしこれは同語反復的（ταυτολόγως）であり、あまり優雅ではない。とりわけ *suprema* という語が二度置かれている点においてである。…
- [3] 946 Quem iam summa dies suprema luce premebat.
- [4] 946 Quem jam summa dies suprema luce premebat.
- [6] [946] [quem iam summa dies suprema luce premebat].

947 Huic subito ante oculos similis Tritonia fratri
- [2] 952 Hinc subito ante oculos similis Tritouia fratri
- [3] 947 Huic subito ante oculos similis Tritonia fratri
- [4] 947 Huic subito ante oculos similis Tritonia fratri
  - Tritonia (MINERVA; ミネルウァ): Tritonia:デイポボスの顔と武具をまとって、ヘクトルを欺く
- [6] 947 huic subito ante oculos similis Tritonia fratri
  - fratri (Deiphobus; デイポボス): fratri 947 を参照
  - Tritonia (Tritonia; トリトニア): Tritonia 947

948 occurrens iuuenem simulato decipit ore;
- [2] 953 Occurrens juvenem simulato decipit ore.
- [3] 948 Occurrens iuuenem simulato decipit ore.
- [4] 948 Occurrens juvenem simulato decipit ore :
- [6] 948 occurrens iuvenem simulato decipit ore,

949 nam cum Deiphobi tutum se credidit armis,
- [2] 954 'Ham dum Deiphobi tutum se credidit armis,
- [3] 949 Nam dum Deiphobi tutum se credidit armis,
- [4] 949 Nam dum Deiphobi tutum se credidit armis,
  - Deiphobi (DEIPHOBUS; デイポボス): Deiphobi:ミネルウァはデイポボスの姿をとる
- [6] 949 nam cum Deiphobi tutum se credidit armis,
  - Deiphobi (Deiphobus; デイポボス): -bi 949:プリアモスの子

950 transtulit ad Danaos iterum sua numina Pallas.
- [2] 955 Transtulit ad Danaos iterum sua numina Pallas.
- [3] 950 Transtulit ad Danaos iterum sua numina Pallas.
- [4] 950 Transtulit ad Danaos iterum sua numina Pallas.
  - Danaos (GRAI; ギリシア人): ダナオイのほうへ、ミネルウァが自らの神威を移す
  - Pallas (MINERVA; ミネルウァ): — ギリシア人のほうへ神威を移す
- [6] 950 transtulit ad Danaos iterum sua numina Pallas.
  - Danaos (Danai; ダナオイ): -os 45. 492. 659. 808. 912. 950. 1001
  - Pallas (Pallas; パラス): Pallas 950

951 Concurrunt iactis inter se comminus hastis
- [2] 956 Concurrunt jactis inter se cominus hastis
- [3] 951 Concurrunt iactis inter se cominus hastis
- [4] 951 Concurrunt jactis inter se cominus hastis
- [6] 951 concurrunt iactis inter se comminus hastis

952 inuicti iuuenes: hic uastis intonat armis,
- [2] 957 Invicti juvenes : hic vastis intonat armis;
  - *Intonat armis*（武具を轟かせる）はウェルギリウスの表現である（Aen. XII, 700）。
- [3] 952 Inuicti iuuenes: hic uastis intonat armis,
- [4] 952 Invicti juvenes : hic vastis intonat armis,
- [6] 952 invicti iuvenes: hic vastis intonat armis,

953 ille hostem ualidum nequiquam umbone repellit
- [2] 958 Ille hostem validum nequidquam umbone repellit,
  - *Nequidquam umbone repellit*（盾の突起で空しく押し返す）。Virg. Aeneid. II, 545: « rauco quod protinus aere repulsum, Et summo clypei nequidquam umbone pependit » と同様である。
- [3] 953 Ille hostem ualidum nequicquam umbone repellit;
- [4] 953 Ille hastam valido nequicquam umbone repellit
- [6] 953 ille hostem validum nequiquam umbone repellit

954 alternisque ferox mutat congressibus ictus.
- [2] 959 Altemisque ferox mutat congressibus ictus.
  - *Mutat congressibus ictus*（組み打ちにおいて打撃を変化させる）、すなわち、組み合いながら打撃をあれこれと違った仕方で繰り出す。これはナソ（オウィディウス）が Metam. IX, 42 で次のように述べている交互の組み打ちのことである: « Digredimur paullum, rursumque ad bella coimus »。…
- [3] 954 Alternisque feros uitant congressibus ictus.
- [4] 954 Alternisque feros mutant congressibus ictus.
- [6] 954 alternisque ferox mutat congressibus ictus.

955 Sudor agit riuos, ensem terit horridus ensis
- [2] 960 Sudor agit rivos, ensem terit horridus ensis,
  - *Sudor agit rivos*（汗が川をなす）。Virgil. Aen. V, 200: « sudor fluit undique rivis »、および 807 行を見よ。
- [3] 955 Sudor agit riuos, ensem terit horridus ensis,
- [4] 955 Sudor agit rivos, ensem terit horridus ensis,
- [6] 955 sudor agit rivos, ensem terit horridus ensis.

956 collatusque haeret pede pes et dextera dextrae.
- [2] 961 Collatusque haeret pede pes, et dextera dextrae.
  - *Collatusque haeret*（身を寄せ合って離れない）。Virg. Aen. X, 361: « Concurrunt, haeret pede pes, densusque viro vir »。しかし詩人はむしろオウィディウスの Metam. IX, 44 を念頭に置いていた: « eratque Cum pede pes junctus: totoque ego pectore pronus Et digitos digitis, et frontem fronte premebam »。…
- [3] 956 Conlatusque haeret pede pes et dextera dextrae.
- [4] 956 Collatusque haeret pede pes et dextera dextrae.
- [6] 956 collatusque haeret pede pes et dextera dextrae.

956a
- [2] 962 Interea validam Thetideius extulit hastam ,
- [3] —
- [4] —
- [6] —

957 Hastam iam manibus saeuus librabat Achilles
- [2] —
- [3] 957 Hastam iam manibus saeuus librabat Achilles
- [4] 957 Hastam jam manibus saevus librabat Achilles
  - Achilles (ACHILLES; アキレウス): — 残忍なる者、ヘクトルに向けて槍を構える
- [6] 958 hastam iam manibus saevus librabat Achilles
  - Achilles (Achilles; アキレウス): saevus . . . -es 958

958 inque uirum magnis emissam uiribus egit,
- [2] 963 Inque virum magnis emissam viribus egit;
- [3] 958 Inque uirum magnis emissam uiribus egit;
- [4] 958 Inque virum magnis emissam viribus egit;
- [6] 957 inque virum magnis emissam viribus egit;

959 quam praeterlapsam uitauit callidus Hector.
- [2] 964 Quam praeterlapsam vitavit callidus Hector :
- [3] 959 Quam praeterlapsam uitauit callidus Hector.
- [4] 959 Quam praeterlapsam vitavit callidus Hector.
  - Hector (HECTOR; ヘクトル): — 狡猾な者、アキレウスの槍を避ける
- [6] 959 quam praeterlapsam vitavit callidus Hector.
  - Hector (Hector; ヘクトル): Hector 256. 277. 491. 626. 677. 774. 959. 967. 979. 996. 1051

960 Exclamant Danai. Contra Priameius heros
- [2] 965 Exclamant Danai. Contra Priameius heros
- [3] 960 Exclamant Danai. contra Priameius heros
- [4] 960 Exclamant Danai. Contra Priameius heros
  - Danai (GRAI; ギリシア人): — アキレウスの槍がヘクトルに避けられると叫ぶ
  - Priameius (HECTOR; ヘクトル): Priameius heros:プリアモスの子なる英雄がアキレウスに向けて投げ槍を投げる
- [6] 960 exclamant Danai. contra Priameius heros
  - Danai (Danai; ダナオイ): Danai 508. 542. 646. 679. 766. 802. 838. 960. 978. 1002
  - Priameius (Priameius; プリアモスの): Priameius heros:パリス 271、ヘクトル 960

961 uibratum iaculum Vulcania torquet in arma.
- [2] 966 Vibratum jaculum Vulcania torquet in arma ,
- [3] 961 Libratum iaculum Uulcania torquet in arma.
- [4] 961 Libratum jaculum Vulcania torquet in arma.
  - Vulcania (VULCANIUS; ウルカヌスの): Vulcania arma:ウルカヌスの武具
- [6] 961 vibratum iaculum Vulcania torquet in arma.
  - Vulcania (Vulcanius; ウルカヌスの): Vulcania . . . arma、アキレウスの 835. 961

962 Nec successus adest: nam duro inflectitur auro
- [2] 967 Nec successus adest, nam duro inflectitur auro :
  - … なぜならここではウルカヌス作の武具のことが論じられており、それが黄金で鍛造されたと、われらの詩人は上の 863 行で述べているからである。また古代の英雄たちが黄金を彫り施した盾を携えることも稀ではない。Ovid. Metam. VIII, vs. 26: « Seu sumpserat auro Fulgentem clypeum, clypeum sumpsisse decebat »。
- [3] 962 Nec successus adest; nam duro inflectitur auro
- [4] 962 Nec successus adest; nam duro inflectitur auro;
- [6] 962 nec successus adest, nam duro inflectitur auro

963 dissiluitque mucro. Gemuerunt agmina Troum.
- [2] 968 Dissiluit mucro : gemuerunt agmina Troum.
  - … これは幾分唐突に見え、何か行が脱落したのではないかと疑われるほどである。というのも、直前では投げられた槍のことが語られていたのに、ここでは *mucro*、すなわち剣の切先のことが語られているからである。そして *Dissiluit* において作者は、Virg. Aen. XII, 739 でトゥルヌスに起こったこと、すなわち « postquam arma Dei ad Vulcania ventum est, Mortalis mucro, glacies ceu futilis, ictu Dissiluit » を表現しているかのように見える。しかしここで、黄金によって曲げられた（すなわち、刃こぼれした、あるいは逸らされた）切先は、砕け散った（粉々に散った）とは言えず、むしろ落ちた（*decidisse*）と言うべきである。…
- [3] 963 Desiliitque mucro; gemuerunt agmina Troum.
- [4] 963 Desiluit mucro; gemuerunt agmina Troum.
  - Troum (TROJANI; トロイア人): — トロイア人の隊列が呻いた
- [6] 963 dissiluit\<que> mucro: gemuerunt agmina Troum.
  - Troum (Tros; トロイア人): Troum 102. 281. 339. 357. 438. 631. 641. 701. 963

964 Concurrunt iterum collatis fortiter armis
- [2] 969 Concurrunt iterum collatis fortiter armis,
- [3] 964 Concurrunt iterum collatis fortiter armis
- [4] 964 Concurrunt iterum collatis fortiter armis
- [6] 964 concurrunt iterum collatis fortiter armis

965 inque uicem duros euitant comminus enses.
- [2] 970 Inque vicem duros evitant cominus enses.
  - … これを「剣を手に対峙した両者は、互いに一撃を躱し合い傷を負わないよう、長い間激しく切り結ぶ」と解釈する。実際、その後ヘクトルは再び退却して逃亡するからである。…
  - **(cont.)** … ――*Mutare ictus*（打撃を交わす）または *commutare enses*（剣を交わす）という表現は、クラウディアヌスの『ホノリウスとマリアの婚礼について』(*de Nupt. Hon. et Mar.*) 86行における « permutare radios »（光線を交わす）と同様の理路で言われていると思われる。すなわち、互いに交錯する一撃を繰り出し、また打ち返すということである。剣も光線も同様に互いを掠め、また掠められ、閃いては打ち返し合い、それゆえに「交換される」のである。パリ編者。
- [3] 965 Inque uicem duros euitant cominus enses.
- [4] 965 Inque vicem duros evitant cominus enses.
- [6] 965 inque vicem duros evitant comminus enses.

966 Nec sufferre ualet ultra sortemque supremam
- [2] 971 Nec sufferre valet ultra , sortemque supremam
- [3] 966 Nec suffere ualet ultra iam sorte suprema
- [4] 966 Nec sufferre valet ultra sortemque supremam
- [6] 966 nec sufferre valet ultra iam sorte suprema

967 stantemque Aeaciden defectis uiribus Hector.
- [2] 972 Horruit instantem defectis viribus Hector.
- [3] 967 Instantem Aeacidem defectus uiribus Hector;
- [4] 967 Horruit instantem defectus viribus Hector;
  - Hector (HECTOR; ヘクトル): — 力尽き、アキレウスが迫る中で
- [6] 967 instantem Aeaciden defectis viribus Hector;
  - Hector (Hector; ヘクトル): Hector 256. 277. 491. 626. 677. 774. 959. 967. 979. 996. 1051

968 Dumque retro cedit fraternaque rebus in artis
- [2] 973 Damque retro cedit, fraternaque rebus in arctis
- [3] 968 Dumque retrocedit fraternaque rebus in artis
- [4] 968 Dumque retrocedit fraternaque rebus in artis
- [6] 968 dumque retro cedit fraternaque rebus in artis
  - fraterna (Deiphobus; デイポボス): fraterna . . . auxilia 968

969 respicit auxilia et nullam uidet esse salutem,
- [2] 974 Respicit auxilia, et nullam videt esse salutem,
- [3] 969 Respicit auxilia et nullam uidet esse salutem,
- [4] 969 Respicit auxilia et nullam videt esse salutem,
- [6] 969 respicit auxilia et nullam videt esse salutem,

970 sensit adesse dolos. Quid agat? quae numina supplex
- [2] 975 Sensit adesse dolos : quid agat?qu» numina supplex
  - … ――*quid agat?*（彼はいかにすべきか？）という定型表現については、本著作第2巻、哀歌第12歌37行、301頁の注記を参照すべきである。そして、ここで *quae numina supplex Invocet?*（伏して願うにいかなる神々に祈るべきか？）と言われているのと同様に、上掲のレポシアヌス145行でも « Quod numen poscat? » とある。パリ編者。
- [3] 970 Sensit adesse dolos: quid agat? quae numina supplex
- [4] 970 Sensit adesse dolos : quid agat? quae numina supplex
- [6] 970 sensit adesse dolos: quid agat? quae numina supplex

971 inuocet? et toto languescunt corpore uires
- [2] 976 Invocet? et toto languescunt corpore vires
- [3] 971 Inuocet? et toto languescunt corpore uires
- [4] 971 Invocet? en toto languescunt corpore vires
- [6] 971 invocet? et toto languescunt corpore vires

972 auxiliumque negant; retinet uix dextera ferrum,
- [2] 977 Auxiliumque negant; retinet vix dextera ferrum,
- [3] 972 Auxiliumque negant; retinet uix dextera ferrum,
- [4] 972 Auxiliumque negant; retinet vix dextera ferrum.
- [6] 972 auxiliumque negant; retinet vix dextera ferrum,

973 nox oculos inimica tegit nec subuenit ullum
- [2] 978 Nox oculos inimica tegit, nec subvenit ullum
- [3] 973 Nox oculos inimica tegit nec subuenit ullum
- [4] 973 Nox oculos inimica tegit nec subvenit ullum
- [6] 973 nox oculos inimica tegit nec subvenit ullum

974 defesso auxilium; pugnat moriturus et alto
- [2] 979 Defesso auxilium : pugnat moriturus et altos
- [3] 974 Defesso auxilium; pugnat moriturus et altos
- [4] 974 Defesso auxilium; pugnat moriturus et alto
- [6] 974 defesso auxilium; pugnat moriturus et alto
  - … alto … ウェルギリウス『アエネーイス』10, 464 を参照

975 corde premit gemitus. Instat Nereius heros
- [2] 980 Corde premit gemitus : instat Nereius heros,
- [3] 975 Corde petit gemitus. instat Nereius heros
- [4] 975 Corde trahit gemitus. Instat Nereius heros
  - Nereius (ACHILLES; アキレウス): — ヘクトルに迫る
- [6] 975 corde premit gemitus. instat Nereius heros
  - Nereius (Nereius; ネレウスの): Nereius heros 938. 975:アキレウス

976 turbatumque premit procul undique; tunc iacit hastam
- [2] 981 Turbatumqueprocul premit undique; tunc jacit hastam,
  - … ここでは、他所なら *proturbatum*（遠くへ追い立てられた）と言うべきところを *turbatum procul*（混乱のうちに遠くへ追いやられた）と述べている。
- [3] 976 Turbatumque premit procul undique, tum iacit hastam
- [4] 976 Turbatumque premit procul undique, tum jacit hastam
- [6] 976 turbatumque premit procul undique, tunc iacit hastam

977 et medias rigida transfixit cuspide fauces.
- [2] 982 Et medias rigida transfixit cuspide fauces.
- [3] 977 Et medias rigida transfixit cuspide fauces.
- [4] 977 Et medias rigida transfixit cuspide fauces.
- [6] 977 et medias rigida transfixit cuspide fauces.

978 Exsultant Danai, Troes sua uulnera deflent.
- [2] 983 Exsultant Danai, Troes sua funera deflent.
- [3] 978 Exultant Danai, Troes sua funera maerent.
- [4] 978 Exsultant Danai, Troes sua funera maerent.
  - Danai (GRAI; ギリシア人): — ヘクトルが殺されると歓喜する
  - Troes (TROJANI; トロイア人): — 自らの死者を悼む
- [6] 978 exultant Danai, Troes sua vulnera deflent.
  - Danai (Danai; ダナオイ): Danai 508. 542. 646. 679. 766. 802. 838. 960. 978. 1002
  - Troes (Tros; トロイア人): Troes 758. 767. 928. 978. 1002、いずれも子音の前または最後の不定の位置で

979 Tunc sic amissis infelix uiribus Hector:
- [2] 984 Tum sic amissis infelix viribus Hector :
- [3] 979 Tum sic amissis infelix uiribus Hector
- [4] 979 Tum sic amissis infelix viribus Hector :
  - Hector (HECTOR; ヘクトル): — 不幸な者、力を失い、アキレウスに嘆願する
- [6] 979 tunc sic amissis infelix viribus Hector
  - Hector (Hector; ヘクトル): Hector 256. 277. 491. 626. 677. 774. 959. 967. 979. 996. 1051

980 "En concede meos miseris genitoribus artus,
- [2] 985 « En concede meos miseris genitoribus artus ,
- [3] 980 'En concede meos miseris genitoribus artus,
- [4] 980 « En concede meos miseris genitoribus artus,
- [6] 980 'en concede meos miseris genitoribus artus,
  - genitoribus (Hecabe; ヘカベ): miseris genitoribus 980
  - genitoribus (Priamus; プリアモス): miseris genitoribus 980

981 quos pater infelix multo mercabitur auro:
- [2] 986 Quos pater infelix multo mercabitur auro :
- [3] 981 Quos pater infelix multo mercabitur auro:
- [4] 981 Quos pater infelix multo mercabitur auro.
- [6] 981 quos pater infelix multo mercabitur auro:
  - pater (Priamus; プリアモス): pater infelix 981

982 dona feres uictor. Priami nunc filius orat,
- [2] 987 Dona feres victor. Priami nunc filius orat,
  - … 後続の *Te Priamus* にも同時に係ることになって、見事な漸層法（グラダーティオー）をなしている。
- [3] 982 Dona feres uictor. Priami nunc filius orat
- [4] 982 Dona feres victor. Priami nunc filius orat,
  - Priami (HECTOR; ヘクトル): Priami filius:かの将の中の将(死に際して自らについて語る)
  - Priami (PRIAMUS; プリアモス): — 子
- [6] 982 dona feres victor. Priami nunc filius orat
  - filius (Hector; ヘクトル): Priami . . . filius . . . dux ille ducum, quem Graecia solum pertimuit 982
  - Priami (Priamus; プリアモス): -mi . . . filius 982

983 te Priamus, dux ille ducum, quem Graecia solum
- [2] 988 Te Priamus, dux ille ducum, quem Graecia solum
- [3] 983 Te primus, dux ille ducum, quem Graecia solum
- [4] 983 Te Priami, dux ille ducum, quem Graecia solum
  - Graecia (GRAECIA; ギリシア): — ヘクトルただ一人を恐れていた
- [6] 983 te primum, dux ille ducum, quem Graecia solum
  - Graecia (Graecia; ギリシア): -a 983
  - — (Priamus; プリアモス): Priamus 278 [983] 1046

984 pertimuit: si, nec precibus nec munere uictus,
- [2] 989 Pertimuit : si nec precibus, nec munere victus,
- [3] 984 Pertimuit: si nec precibus nec uulnere uicti
- [4] 984 Pertimuit : si nec precibus nec vulnere victi
- [6] 984 pertimuit: si, nec precibus nec munere victus,

985 nec lacrimis miseri nec clara gente moueris,
- [2] 990 Nec lacrymis miseri, nec clara gente moveris,
- [3] 985 Nec lacrimis miseri nec clara gente moueris,
- [4] 985 Nec lacrimis miseri nec clara gente moveris,
- [6] 985 nec lacrimis miseri nec clara gente moveris,

986 afflicti miserere patris: moueat tua Peleus
- [2] 991 Adflicti miserere patris : moveat tua Peleus
- [3] 986 Afflicti miserere patris, moueat tua Peleus
- [4] 986 Afflicti miserere patris, moveat tua Peleus
  - Peleus (PELEUS; ペレウス): プリアモスのためにペレウスがアキレウスを動かさんことを(ヘクトルが死に際して呼びかける)
- [6] 986 afflicti miserere patris: moveat tua Peleus
  - Peleus (Peleus; ペレウス): Peleus 986:アキレウスの父
  - patris (Priamus; プリアモス): afflicti . . . patris 986. 1032

987 pectora pro Priamo, pro nostro corpore Pyrrhus."
- [2] 992 Pectora pro Priamo , pro nostro corpore Pyrrhus ».
  - … というのも、われらの詩人は子の代わりに *corpus* を置くのを常としているからである。89行を見よ。
- [3] 987 Pectora pro Priamo, pro nostro corpore Pyrrhus.'
- [4] 987 Pectora pro Priamo, pro nostro corpore Pyrrhus ».
  - Priamo (PRIAMUS; プリアモス): Pro Priamo:プリアモスのためにペレウスがアキレウスを動かさんことを(ヘクトルが語る)
  - Pyrrhus (PYRRHUS; ピュロス): ヘクトルのためにピュロスがアキレウスを動かさんことを
- [6] 987 pectora pro Priamo, pro nostro pignore Pyrrhus.'
  - Priamo (Priamus; プリアモス): pro -mo 987
  - Pyrrhus (Pyrrhus; ピュロス): Pyrrhus 987:アキレウスの子

988 Talia Priamides. Quem contra durus Achilles:
- [2] 993 Talia Priamides , contra quem durus Achilles :
- [3] 988 Talia Priamides; contra quem durus Achilles
- [4] 988 Talia Priamides; contra quem durus Achilles :
  - Achilles (ACHILLES; アキレウス): — 無情なる者、ヘクトルの嘆願を退ける
  - Priamides (HECTOR; ヘクトル): — このように語った(アキレウスに、死に際して)
- [6] 988 talia Priamides; quem contra durus Achilles
  - Achilles (Achilles; アキレウス): -es 211. 988. 997. 1014. 1043
  - Priamides (Priamides; プリアミデス): Priamides 601. 610. 660. 988

989 "Quid mea supplicibus temptas inflectere dictis
- [2] 994 a Quid mea supplicibus tentas inflectere dictis
- [3] 989 'Quid mea supplicibus temptas inflectere dictis
- [4] 989 « Quid mea supplicibus temptas inflectere dictis
- [6] 989 'quid mea supplicibus temptas inflectere dictis

990 pectora, quem possem direptum more ferarum,
- [2] 995 PectoraPquem possem discerptum more ferarum,
  - … これがホメロスの言葉 Iliad. XXII, 346 に合致すると考えている。メラニッポスの頭部と脳を噛み砕いたテュデウスの例（スタ-
  - **(cont.)** （前頁からの続き）-ティウスが Theb. VIII, 755 以下で伝えている）に倣って、バルトは前掲箇所でこの言語に絶する残虐行為の事例を歴史から数多く集めている。…
- [3] 990 Pectora, quem possem discerptum more ferarum,
- [4] 990 Pectora, quem possem discerptum more ferarum,
- [6] 990 pectora, quem possem direptum more ferarum,

991 si sineret natura, meis absumere malis?
- [2] 996 Si sineret natura, nieis absumere malis.
- [3] 991 Si sineret natura, meis absumere malis?
- [4] 991 Si sineret natura, meis absumere malis?
- [6] 991 si sineret natura, meis absumere malis?

992 Te uero tristesque ferae cunctaeque uolucres
- [2] 997 Te vero tristesque ferae cunctaeque volucres
- [3] 992 Te uero tristesque ferae cunctaequae uolucres
- [4] 992 Te vero tristesque ferae cunctaeque volucres
- [6] 992 te vero tristesque ferae cunctaeque volucres

993 diripient, auidosque canes tua uiscera pascent.
- [2] 998 Diripient , avidique canes tua viscera pascent.
  - … そして確かに、*pascere* が能動の意味で *vorare*（貪り食う）の意に用いられる例は優れた作家においては滅多に見出されないが、複合動詞 *depascere* は Colum. VII, 5 に見出され、また本作のような作家においては、すべての語を最善の語法に厳格に合わせることは到底できない。したがって、ここでは判断を保留すべきである（*ampliandum*）と考える。
- [3] 993 Diripient, auidosque canes tua uiscera pascent.
- [4] 993 Diripient, avidosque canes tua viscera pascent.
- [6] 993 diripient, avidique canes tua viscera pascent.

994 Haec ex te capient Patrocli gaudia manes,
- [2] 999 Haeo ex te capient Patrocli gaudia Manes,
- [3] 994 Haec ex te capient Patrocli gaudia manes,
- [4] 994 Haec ex te capient Patrocli gaudia manes,
  - Patrocli (PATROCLUS; パトロクロス): Patrocli manes:パトロクロスの霊
- [6] 994 haec ex te capient Patrocli gaudia manes,
  - Patrocli (Patroclus; パトロクロス): -cli . . . manes 994

995 si sapiunt umbrae." Dum talia magnus Achilles
- [2] 1000 Si capiunt umbrae». Dum talia magnus Achilles
  - … おそらくこれはウェルギリウスの Georg. IV, 489 のあの句から模取されたものであろう：« Ignoscenda quidem, scirent si ignoscere Manes »。またカルプルニウス VIII, 38：« Si sentire datur post fata quietis »。
- [3] 995 Si capiunt umbrae.' dum talia magnus Achilles
- [4] 995 Si capiunt umbrae ». Dum talia magnus Achilles
  - Achilles (ACHILLES; アキレウス): — 偉大なる者が語る間に、ヘクトルは魂を返す
- [6] 995 si capiunt umbrae.' dum talia magnus Achilles
  - Achilles (Achilles; アキレウス): magnus -es 860. 995

996 ore truci iactat, uitam miserabilis Hector
- [2] 1001 Ore truci jactat, vitam miserabilis Hector
- [3] 996 Ore truci iactat, uitam miserabilis Hector
- [4] 996 Ore truci jactat, vitam miserabilis Hector
  - Hector (HECTOR; ヘクトル): — 哀れな者、命を返す
- [6] 996 ore truci iactat, vitam miserabilis Hector
  - Hector (Hector; ヘクトル): Hector 256. 277. 491. 626. 677. 774. 959. 967. 979. 996. 1051

997 reddidit. Hunc animi nondum satiatus Achilles
- [2] 1002 Reddidit : hunc animo nondum satiatus Achilles
  - … *nondum satiatus*（いまだ満ち足りず）という言葉に接して、私は Anthol. Lat. 第1巻94に収められ、『ヘクトルの引きずりについて』と題されたエピグラムを思い起こす：« Funere turbat equos necdum satiatus Achilles, Hector et exanimis funere turbat equos »。このエピグラムにおいて私は *turbat*（かき乱す／怯えさせる）という語に違和感を覚えるが、われらの要約者（エピトマートル）と照らし合わせるならば、誰もがこれが誤って用いられていると考えるであろう。なぜならわれらの詩人は1005行で、アキレウスの馬たちが取り乱したり怯えたりしたのではなく、むしろヘクトルの遺骸によってより誇らしげに、より高く歩みを進めたと述べているからである。それゆえおそらく *turbat* の代わりに、Statius, Achill. I, 88: « modo crassa exire vetabit (Achilles) Flamina, et Hectoreo tardabit funere currus » の例に倣って、*tardat*（遅らせる）と読むべきかもしれない。
- [3] 997 Reddidit. hunc animi nondum satiatus Achilles
- [4] 997 Reddidit. Hunc animi nondum satiatus Achilles
  - Achilles (ACHILLES; アキレウス): — まだ飽き足らず、ヘクトルの手足を戦車に縛りつける
- [6] 997 reddidit. hunc animi nondum satiatus Achilles
  - Achilles (Achilles; アキレウス): -es 211. 988. 997. 1014. 1043

998 deligat ad currum pedibusque exsanguia membra
- [2] 1003 Deligat ad currum , pedibusque exsanguia membra
- [3] 998 Deligat ad currum pedibusque exsanguia membra
- [4] 998 Deligat ad currum pedibusque exsanguia membra
- [6] 998 deligat ad currum pedibusque exsanguia membra

999 ter circum muros uictor trahit; altius ipsos
- [2] 1004 Ter circum ihuros victor trahit : altius ipsos
  - *Ter circum muros victor trahit*（勝者は三度城壁の周りを引きずり回す）。ここでわれらの作者は再び、ホメロスその人からではなく、Aen. I, 483 で « Ter circum Iliacos raptaverat Hectora muros » と述べたウェルギリウスに依拠してホメロスを再現している。しかしホメロス自身は、戦車に結びつけられたヘクトルがアキレウスによって引きずり回されたのは、トロイアの城壁の周りではなく、パトロクロスの塚の周りを三度であったと記している。他の古代ギリシアおよびラテンの詩人たちも城壁の周りを引きずられたと伝えているが、「3度」という数については沈黙している。Ovid. Metam. XII, 591 および in Ib. 336 を見よ。ピエール・ベールは『歴史批評辞典』(*Diction.*) の項目
  - **(cont.)** （前頁からの続き）「アキレウス」（*Achille*）、注 H において、ウェルギリウス以後の詩人の中でこれを伝えているのは唯一『イリアス・ラティナ』の作者のみであると指摘し、さらにアウソニウスもホメロス『イリアス』第22巻の要約（ペリオカ）で同じことを行っており、そのためにマリアンジェロ［・アックルシオ］から非難されたと付言している。このような特異な点におけるアウソニウスとわれらのホメロス詩人との一致は、仮にこの要約詩（エピトメー）の作者がアウソニウス自身でないとしても、少なくとも『ペリオカ』の作者と同一人物であると推測させ得るほどのものである（もっとも『ペリオカ』がアウソニウスに帰属されること自体、それほど確実というわけではないが）。
- [3] 999 Ter circum muros uictor trahit: altior ipsos
- [4] 999 Ter circum muros victor trahit : altior ipsos
- [6] 999 ter circum muros victor trahit: altius ipsos
  - muros (Troia; トロイア): muros 999

1000 fert domini successus equos. Tum maximus heros
- [2] 1005 Fert domini successus equos : tunc maximus heros
  - *Fert domini successus equos*（主人の成功が馬たちを高揚させる）。バルトは『雑考』(*Adv.*) 2809 頁で、これは見事に、またホメロス風に表現されていると考えている。というのも詩人たちは英雄の馬たちを、ある種の未来の予兆を知るものとするからである。バルトは Stat. Theb. I, 275、および『プロセルピナの略奪』(*de Raptu Proserp.*) 第1巻の最終行への注でも同様のことを記している。クラウディアヌスの de Cons. Olybr. 4行の次の句にも同様の言いまわしが見られる：« Blandius elato surgant temone jugales »。…
- [3] 1000 Fert domini successus equos. tum maximus heros
- [4] 1000 Fert domini successus equos. Tum maximus heros
- [6] 1000 fert domini successus equos. tum maximus heros
  - heros (Achilles; アキレウス): maximus heros 1000

1001 detulit ad Danaos foedatum puluere corpus.
- [2] 1006 Detulit ad Danaos foedatum pulvere corpus.
- [3] 1001 Detulit ad Danaos foedatum puluere corpus.
- [4] 1001 Detulit ad Danaos foedatum pulvere corpus.
  - Danaos (GRAI; ギリシア人): ダナオイのもとへ、アキレウスがヘクトルの亡骸を運ぶ
- [6] 1001 detulit ad Danaos foedatum pulvere corpus.
  - Danaos (Danai; ダナオイ): -os 45. 492. 659. 808. 912. 950. 1001
  - corpus (Hector; ヘクトル): corpus 1001

1002 Laetantur Danai, plangunt sua uulnera Troes
- [2] 1007 Laetantur Danai; plangunt sua funera Troes,
- [3] 1002 Laetantur Danai, plangunt sua uulnera Troes
- [4] 1002 Laetantur Danai, plangunt sua funera Troes.
  - Danai (GRAI; ギリシア人): — 喜ぶ
  - Troes (TROJANI; トロイア人): — 自らの傷を嘆く
- [6] 1002 laetantur Danai, plangunt sua funera Troes
  - Danai (Danai; ダナオイ): Danai 508. 542. 646. 679. 766. 802. 838. 960. 978. 1002
  - Troes (Tros; トロイア人): Troes 758. 767. 928. 978. 1002、いずれも子音の前または最後の不定の位置で

1003 et pariter captos deflent cum funere muros.
- [2] 1008 Et pariter captos deflent cum fiinere muros.
- [3] 1003 Et pariter corpus deflent cum funere raptum.
- [4] 1003 below Et pariter raptum deflent cum funere corpus
- [6] 1003 et pariter captos deflent cum funere muros.

## Book 23

1004 Interea uictor defleti corpus amici
- [2] 1009 XXIII. Interea victor defleti corpus amici
- [3] 1004 Interea uictor defleti corpus amici
- [4] 1004 Interea victor defleti corpus amici
- [6] 1004 interea victor defleti corpus amici
  - amici (Patroclus; パトロクロス): defleti . . . amici 1004

1005 funerat Aeacides pompasque ad funera ducit.
- [2] 1010 Funerat Aeacides, pompasque ad funera ducit.
  - *Pompasque ad funera ducit*（葬礼へと行列を導く）。Virg. Georg. III, 22: « solennes ducere pompas Ad delubra juvat »。
- [3] 1005 Funerat Aeacides pompasque ac munera ducit.
- [4] 1005 Funerat Aeacides pompasque ac munera ducit.
  - Aeacides (ACHILLES; アキレウス): — パトロクロスの亡骸の葬儀を行う
- [6] 1005 funerat Aeacides pompasque ad funera ducit.
  - ad funera … ウェルギリウス『農耕詩』3, 22 を参照
  - Aeacides (Aeacides (Achilles); アエアキデス（アキレウス）): victor . . . -es 1005. 1026

1006 Tum circa tumulum miseros rapit Hectoris artus
- [2] 1011 Ter circa tumulum miseros rapit Hectoris artus,
  - ここでは確かに、流布本の読異はヘクトルの四肢がパトロクロスの塚の周りを三度引きずり回されたと述べており、ホメロス自身も Iliad. XXIV, 16 でそう述べている。…なぜなら、後代の詩人たちがウェルギリウスに従って、ホメロスの伝えるパトロクロスの塚の周りの3度の引きずり回しから、トロイアの城壁の周りの同数の引きずり回しを作り出した可能性が高いからである。われらの詩人は上にすでにそれを述べている以上、この箇所で再びそれを示したとは考えられないからである。
- [3] 1006 Ter circa tumulum miseros rapit Hectoris artus
- [4] 1006 Ter circa tumulum miseros rapit Hectoris artus
  - Hectoris (HECTOR; ヘクトル): — アキレウスはヘクトルの哀れな手足をパトロクロスの墓の周りに三度引きずる
- [6] 1006 ter circa tumulum miseros rapit Hectoris artus
  - Hectoris (Hector; ヘクトル): -oris 232. 565. 1006. 1040

1007 et uapido cineri ludorum indicit honores.
- [2] 1012 Et varios cineri ludorum indicit honores.
- [3] 1007 Et uarios cineri ludorum indicit honores.
- [4] 1007 Et varios cineri ludorum indicit honores.
- [6] 1007 et vapido cineri ludorum indicit honores.

1008 Tydides *tyrsin* cursu pedibusque ferocem
- [2] 1013 Tydides circi cursu, pedibusque ferorum
  - **(cont.)** … ここで論じられているのは戦車競走（競馬）のことであり、そこではディオメデスがメリオネスを破ったのだが、ここではメリオネスが足において獰猛（*pedibus ferox*）、あるいは…敏捷（*velox*）と不条理にも言われている。…――詩人たちによって競馬場（ヒッポドロモス）について *circus* が用いられることは、シュラーダーが『校訂考』(*Emend.*) 第8章 160 頁で指摘している。パリ編者。――*equorum*（馬たちの）の代わりに *ferorum*（野獣たちの／猛獣たちの）と言ったのは、Virg. Aen. II, 51、V, 818；Manilius 第5巻 76行（競技場の御者自身について：« Aut quum laxato fregerunt cardine claustra, Exagitare feros, pronumque anteire volantes »）の例に倣ったものである。さらにペトロニウス 89章『トローイアの陥落』(*Trojae halosis*) 12行、およびディオメデスの *feros*、すなわち馬たちと述べているアウソニウスの Epist. 24, 17 を加えよ。…
- [3] 1008 Tydides cunctos curru pedibusque feroces
- [4] 1008 Tydides cunctos curru pedibusque ferorum
  - Tydides (DIOMEDES; ディオメデス): — <心大いなる者>、戦車ですべての者に勝つ
- [6] 1008 Tydides † tyrsin cursu pedibusque ferocem
  - tyrsin (Tros; トロイア人): (Trosin equis? 1008)
  - Tydides (Tydides; テュディデス): Tydides 390. 408. 530. 665. 1008

1009 Merionem superat; luctando uincitur Aiax
- [2] 1014 Merionem superat: luctando vincitur Ajax,
- [3] 1009 Aeolides superat; luctando uincitur Aiax,
- [4] 1009 Magnanimus superat; luctando vincitur Ajax
  - Ajax (AJAX Telamonis filius; アイアス、テラモンの子): — 相撲で負ける(アキレウスがパトロクロスの亡骸の葬儀を行う間に)
- [6] 1009 Merionem superat; luctando vincitur Aiax,
  - Aiax (Aiax (Telamonius); アイアス（テラモンの子）): -ax 538. 799. 1009
  - Merionem (Meriones; メリオネス): -em 1009(?)

1010 cuius decepit uires Laertius astu;
- [2] 1015 Cujus decepit vires Laertius astu :
- [3] 1010 Cuius decepit uires Laertius astu;
- [4] 1010 Cujus decepit vires Laertius astu;
  - Laertius (ULIXES; ウリクセス): Laertius:ラエルテスの子が葬送競技で相撲においてアイアスに勝つ
- [6] 1010 cuius decepit vires Laertius astus;
  - Laertius (Laertius; ラエルテスの): Laertius astus 1010:ウリクセス

1011 caestibus aduersis cunctos superauit Epeos
- [2] 1016 Caestibus adversis cunctos superavit Epeus ,
  - *Superavit Epeus*（エペイオスが打ち勝った）：ドルプとファン・デル・デュッセンはこのように校訂しており、ホメロスも Iliad. XXIII, 665 でそう教えている。…
- [3] 1011 Caestibus aduersos cunctos superauit Epeos
- [4] 1011 Caestibus adversos cunctos superavit Epeus
  - Epeus (EPEUS; エペイオス): 拳闘の籠手ですべての者に勝つ
- [6] 1011 caestibus adversos cunctos superavit Epeos
  - Epeos (Epeos; エペイオス): caestibus . . . cunctos superavit *Epeos 1011

1012 et disco forti Polypoetes depulit omnes
- [2] 1017 Et disco fortis Polypoetes depulit omnes ,
  - *Fortis Polypoetes*（勇敢なるポリュポイテース）：ホメロス Iliad. XXIII, 836 に拠ってこのように書くべきである。…
- [3] 1012 Et disco fortis Polypoetes depulit omnes
- [4] 1012 Et disco fortis Polypoetes depulit omnes
  - Polypoetes (POLYPOETES; ポリュポイテス): — 葬送競技で円盤においてすべての者に勝つ
- [6] 1012 et disco forti Polypoetes depulit omnes
  - Polypoetes (Polypoetes; ポリュポイテス): *Polypoetes 182. 1012:ヒッポダメイアの子

1013 Merionesque arcu. Tandem certamine misso
- [2] 1018 Merionesque arcu : tandem certamine misso
- [3] 1013 Merionesque arcu; tandem certamine misso
- [4] 1013 Merionesque arcu ; tandem certamine misso
  - Meriones (MERIONES; メリオネス): — 葬送競技で弓においてすべての者に勝つ
- [6] 1013 Merionesque arcu; tandem certamine misso
  - Meriones (Meriones; メリオネス): -nes *432. 1013

1014 in sua castra redit turbis comitatus Achilles.
- [2] 1019 In sua castra redit turbis comitatus Achilles.
- [3] 1014 In sua castra redit turbis comitatus Achilles.
- [4] 1014 In sua castra redit turbis comitatus Achilles.
  - Achilles (ACHILLES; アキレウス): — 陣営に戻る
- [6] 1014 in sua castra redit turbis comitatus Achilles.
  - Achilles (Achilles; アキレウス): -es 211. 988. 997. 1014. 1043

## Book 24

1015 Flent miseri amissum Phryges Hectora totaque maesto
- [2] 1020 XXIV. Flent miseri amissum PhrygesHectora,totaque moesto
- [3] 1015 Flent miseri amissum Phryges Hectora, totaque maesto
- [4] 1015 Flent miseri amissum Phryges Hectora, totaque maesto
  - Hectora (HECTOR; ヘクトル): — トロイア人は失われたヘクトルを悼んで泣く
  - Phryges (TROJANI; トロイア人): — 失われたヘクトルを悼んで泣く
- [6] 1015 flent miseri amissum Phryges Hectora, totaque maesto
  - Hectora (Hector; ヘクトル): -oră 1015
  - Phryges (Phryges; プリュギア人): miseri . . . -es 1015

1016 Troia sonat planctu; fundit miseranda querelas
- [2] 1021 Troja sonat planctu; fundit miseranda querelas i«at
  - *Miseranda querelas Infelix*（哀れにも悲嘆に暮れる不幸な女）。われらの詩人は、一方が副詞的に解釈されるべき場合に形容語句（エピテトン）を重ねるのを常としており、ここでの *miseranda* はすなわち *miserandum in modum*（哀れを誘うように）の意である。同様の用法は1026行でも再び現れる。
- [3] 1016 Troia sonat planctu; fundit miseranda querellas
- [4] 1016 Troja sonat planctu; fundit miseranda querellas
  - Troja (TROJA; トロイア): — ヘクトルを失って嘆きの声に響く
- [6] 1016 Troia sonat planctu; fundit miseranda querellas
  - Troia (Troia; トロイア): Troia 727. 1016

1017 infelix Hecube saeuisque arat unguibus ora
- [2] 1022 Infelix Hecube, saevisque arat unguibus ora,
- [3] 1017 Infelix Hecube saeuisque arat unguibus ora;
- [4] 1017 Infelix Hecube saevisque arat unguibus ora;
  - Hecube (HECUBA; ヘカベ): — 不幸な者、ヘクトルが死ぬと嘆く
- [6] 1017 infelix Hecabe saevisque arat unguibus ora
  - Hecabe (Hecabe; ヘカベ): infelix -be (-cuba trad.) 1017

1018 Andromacheque suas scindit de pectore uestes,
- [2] 1023 Andromacheque suas scindit de pectore vestes,
  - *De pectore vestes*（胸から衣服を）。850行を見よ。
- [3] 1018 Andromacheque suas scindit de pectore uestes,
- [4] 1018 Andromacheque suas scindit de pectore vestes,
  - Andromache (ANDROMACHE; アンドロマケ): — ヘクトルが殺されると、衣を引き裂く
- [6] 1018 Andromacheque suas scindit de pectore vestes,
  - Andromache (Andromache; アンドロマケ): -ē 1018. 1058

1019 heu tanto spoliata uiro. Ruit omnis in uno
- [2] 1024 Heu! tanto spoliata viro:ruit omnis in uno
  - *Tanto spoliata viro*（これほど偉大な夫を奪われ）。Ovid. Met. XIV, 839: « Praecipuum matrona decus, dignissima tanti Ante fuisse viri conjux » とあるのと同様である。
- [3] 1019 Heu tanto spoliata uiro! ruit omnis in uno
- [4] 1019 Heu tanto spoliata viro ! Ruit omnis in uno
- [6] 1019 heu tanto spoliata viro. ruit omnis in uno

1020 Hectore causa Phrygum, ruit hoc defensa senectus
- [2] 1025 Hectore caussa Phrygum, cecidit defessa senectus
  - *In uno Hectore caussa Phrygum*（ヘクトル一人のうちにプリュギア人の大義／命運がある）：ペンタディウスの『ヘクトルの塚にて』(*in tumulo Hect.*) に « Occubuere simul spesque salusque Phrygum » とあり、またアウソニウスの『英雄たちの墓碑銘』(*Epitaph. Her.*) XIV に « Hectoris hic tumulus, cum quo sua Troja sepulta est. Conduntur pariter, qui periere simul » とあるのと同様である。1045行および1059行を参照。…
- [3] 1020 Hectore causa Phrygum, ruit et defessa senectus
- [4] 1020 Hectore causa Phrygum, ruit et defessa senectus
  - Hectore (HECTOR; ヘクトル): In uno Hectore:ヘクトルただ一人においてトロイアの命運が倒れる
  - patris (PRIAMUS; プリアモス): また「打ちひしがれた父の、疲れ果てた哀れむべき老い」(ヘクトルを失って)
  - Phrygum (TROJANI; トロイア人): — プリュギア人の命運のすべてがヘクトルただ一人において倒れる
- [6] 1020 Hectore causa Phrygum, ruit hoc defensa senectus
  - Hectore (Hector; ヘクトル): ruit omnis in uno -ore causa Phrygum 1020
  - Phrygum (Phryges; プリュギア人): causa -um 1020

1021 afflicti miseranda patris, quem nec sua coniunx
- [2] 1026 Adflicti miseranda patris, quem nec sua conjux
- [3] 1021 Afflicti miseranda patris, quem nec sua coniunx
- [4] 1021 Afflicti miseranda patris, quem nec sua conjunx
- [6] 1021 afflicti miseranda patris. quem nec sua coniunx
  - coniunx (Hecabe; ヘカベ): coniunx 1021
  - patris (Priamus; プリアモス): senectus afflicti miseranda patris 1021

1022 turbaque natorum nec magni gloria regni
- [2] 1027 Turbaque natorum , nec magni gloria regni
- [3] 1022 Turbaque natorum nec magni gloria regni
- [4] 1022 Turbaque natorum nec magni gloria regni
- [6] 1022 turbaque natorum nec magni gloria regni

1023 oblitum tenuit uitae, quin iret inermis
- [2] 1028 Oblitum tenuit vitae, quin iret inermis,
  - … 作者は上の 938 行でも同一の構文を用いている。
- [3] 1023 Oblitum tenuit uitae, quin iret inermis
- [4] 1023 Oblitum tenuit vitae, quin iret inermis
- [6] 1023 oblitum tenuit uitae, quin iret inermis

1024 et solum inuicti castris se redderet hostis.
- [2] 1029 Et solum invicti castris se redderet hostis.
- [3] 1024 Et solum inuicti castris se redderet hostis.
- [4] 1024 Et solum invicti castris se redderet hostis.
- [6] 1024 et solum invicti castris se redderet hostis.
  - hostis (Achilles; アキレウス): invicti . . . hostis 1024

1025 Mirantur Danaum proceres, miratur et ipse
- [2] 1030 Mirantur Danaum proceres, miratur et ipse
- [3] 1025 Mirantur Danaum proceres, miratur et ipse
- [4] 1025 Mirantur Danaum proceres, miratur et ipse
  - Danaum (GRAI; ギリシア人): — 首領たち
- [6] 1025 mirantur Danaum proceres, miratur et ipse
  - Danaum (Danai; ダナオイ): -um(属格):19. 50. 67. 124. 153. 251. 268. 357. 389. 496. 631. 686. 691. 698. 705. 743. 747. 794. 1025

1026 Aeacides animum miseri senis; ille trementes
- [2] 1031 Aeacides animum miseri senis : ille trementes
- [3] 1026 Aeacides animum miseri senis; ille trementes
- [4] 1026 Aeacides animum miseri senis; ille trementes
  - Aeacides (ACHILLES; アキレウス): — 哀れなプリアモスの心に驚く
- [6] 1026 Aeacides animum miseri senis; ille trementes
  - Aeacides (Aeacides (Achilles); アエアキデス（アキレウス）): victor . . . -es 1005. 1026
  - senis (Priamus; プリアモス): miseri senis 1026

1027 affusus genibus tendens ad sidera palmas
- [2] 1032 Adfusus genibus tendensad sidera palmas,
- [3] 1027 Affusus genibus tendens ad sidera palmas
- [4] 1027 Affusus genibus tendens ad sidera palmas
- [6] 1027 affusus genibus tendens ad sidera palmas

1028 haec ait: "O Graiae gentis fortissime Achilles,
- [2] 1033 Haec ait : «O Graiae gentis fortissime Achilles,
  - … ホメロスにおいて（Iliad. XXIV, 486 以下）、プリアモスの演説はラテン語ホメーリストにおけるこの演説とはまったく異なっており、ラテン語詩人はこの箇所でも他の箇所と同様に自ら詩人たらんとしたのである。しかし私の考えでは、ホメロスのあの神的な Μνῆσαι πατρὸς σοῖο（汝の父を思い起こされよ）には遠く及ばない。
- [3] 1028 Haec ait 'o Graiae gentis fortissime Achilles,
- [4] 1028 Haec ait : « O Grajae gentis fortissime Achilles,
  - Achilles (ACHILLES; アキレウス): — ギリシアの民の最も勇敢な者よ(プリアモスが呼びかける)
  - Grajae (GRAI; ギリシア人): Graja gens Grajae gentis:ギリシアの民の最も勇敢な者、アキレウスよ
- [6] 1028 haec ait 'o Graiae gentis fortissime Achilles,
  - Achilles (Achilles; アキレウス): 呼格:fortissime -es 818. 1028
  - Graiae (Graius; ギリシアの): Graiae gentis 1028

1029 o regnis inimice meis, te Dardana solum
- [2] 1034 O regnis inimice meis, te Dardana solum
- [3] 1029 O regnis inimice meis, te Dardana solum
- [4] 1029 O regnis inimice meis, te Dardana solum
  - Dardana (TROJANI; トロイア人): — 汝ただ一人に震える(プリアモスがアキレウスに呼びかける)
- [6] 1029 o regnis inimice meis, te Dardana solum
  - Dardana (Dardanus; ダルダニアの): -na . . . pubes 1029

1030 uicta tremit pubes, te sensit nostra senectus
- [2] 1035 Victa tremit pubes, te sensit nostra senectus
- [3] 1030 Uicta tremit pubes, te sensit nostra senectus
- [4] 1030 Victa tremit pubes, te sensit nostra senectus
- [6] 1030 victa tremit pubes, te sensit nostra senectus
  - senectus (Priamus; プリアモス): nostra senectus 1030

1031 crudelem nimium. Nunc sis mitissimus oro
- [2] 1036 Crudelem niinium : nunc sis mitissimus oro,
- [3] 1031 Crudelem nimium: nunc sis mitis semel, oro,
- [4] 1031 Crudelem nimium : nunc sis mihi mitior, oro,
- [6] 1031 crudelem nimium: nunc sis mitissimus, oro,
  - … mitissimus … だがオウィディウス『変身物語』14, 587 を参照

1032 et patris afflicti genibus miserere precantis
- [2] 1037 Et patris adflicti genibus miserere precantis,
  - … 私は何も改めるべきではないと考え、バルト（スタティウス註釈、第3巻394頁）とともに、*adflicti genibus* を「あなたの膝元に打ちつけられた、あたかも何らかの力で押しつけられた」と説明する。スエトニウスの Jul. 20 に « ad genua accidere »（膝元に倒れ伏す）と読まれるのと同様である。
- [3] 1032 Et patris afflicti genibus miserere precantis
- [4] 1032 Et patris afflicti genibus miserere precantis
- [6] 1032 et patris afflicti genibus miserere precantis
  - patris (Priamus; プリアモス): afflicti . . . patris 986. 1032

1033 donaque quae porto miseri pro corpore nati
- [2] 1038 Donaque, quae porto miseri pro corpore nati,
- [3] 1033 Donaque quae porto miseri pro corpore nati
- [4] 1033 Donaque quae porto miseri pro corpore nati
- [6] 1033 donaque quae porto miseri pro corpore nati
  - nati (Hector; ヘクトル): natum 945. 1033. 1036

1034 accipias; si nec precibus nec flecteris auro,
- [2] 1039 Accipias : sin nec precibus, nec flecteris auro,
- [3] 1034 Accipias; si nec precibus nec flecteris auro,
- [4] 1034 Accipias ; si nec precibus nec flecteris auro,
- [6] 1034 accipias; si nec precibus nec flecteris auro,

1035 in senis extremis tua dextera saeuiat annis:
- [2] 1040 In senis extremos tua dextera saeviat annos :
- [3] 1035 In senis extremis tua dextera saeuiat annis:
- [4] 1035 In senis extremis tua dextera saeviat annis :
- [6] 1035 in senis extremis tua dextera saeviat annis:
  - senis (Priamus; プリアモス): senis 1035

1036 saltem saeua pater comitabor funera nati!
- [2] 1041 Saltem saeva pater comitabor funera nati.
- [3] 1036 Saltim scaeua pater comitabor funera nati.
- [4] 1036 Saltim saeva pater comitabor funera nati.
- [6] 1036 saltem saeva pater comitabor funera nati.
  - nati (Hector; ヘクトル): natum 945. 1033. 1036
  - pater (Priamus; プリアモス): pater 1036

1037 Nec uitam mihi nec magnos *concedere* honores,
- [2] 1042 Non vitam mihi, nec magnos concedere honores.
  - **(cont.)** … 作者は、殺されたパラスの父が Virg. Aeneid. XI, 180 で語る言葉からこれを創作したように思われる: « Non vitae gaudia quaero, Nec fas, sed nato Manes perferre sub imos »。
- [3] 1037 Non uitam mihi nec magnos concede fauores,
- [4] 1037 Non vitam mihi nec magnos concedere honores,
- [6] 1037 nec vitam mihi nec magnos concedere honores

1038 sed funus crudele meum! Miserere parentis
- [2] 1043 Sed funus crudele peto : miserere parentis ,
  - … オウィディウスの Met. IX, 179 にも類似の思想がある: « diris cruciatibus aegram Invisamque animam, natamque laboribus aufer, Mors mihi munus erit »。…
- [3] 1038 Sed funus crudele mei: miserere parentis
- [4] 1038 Sed funus crudele peto : miserere parentis
- [6] 1038 sed funus crudele meum: miserere parentis
  - funus (Hector; ヘクトル): funus 1038
  - parentis (Priamus; プリアモス): parentis 225. 1038. 1044

1039 et pater esse meo mitis de corpore disce.
- [2] 1044 Et pater esse meo mitis de funere disce.
  - … バルトは『雑考』(*Adv.*) 2810 頁で流布本の *de funere* に固執し、プリアモスが息子の殺害後に自らを屍（*funus*）と呼んでいると考え、それはウェルギリウスが『キリス』(*Ciris*) においてある老女を骸（*cadaver*）と呼んだのと同様であるとする。…
- [3] 1039 Et pater esse meo mitis de uulnere disce.
- [4] 1039 Et pater esse meo mitis de vulnere disce.
- [6] 1039 et pater esse meo mitis de corpore disce.

1040 Hectoris interitu uicisti Dardana regna,
- [2] 1045 Hectoris interitu vicisti Dardana regna,
- [3] 1040 Hectoris interitu uicisti Dardana regna,
- [4] 1040 Hectoris interitu vicisti Dardana regna,
  - Dardana (DARDANUS; ダルダニアの): Dardana regna:汝はダルダニアの王国を征服した(プリアモスがアキレウスに)
  - Hectoris (HECTOR; ヘクトル): — ヘクトルの死によって征服されたトロイア
- [6] 1040 Hectoris interitu vicisti Dardana regna,
  - Dardana (Dardanus; ダルダニアの): -na regna 1040:トロイアの
  - Hectoris (Hector; ヘクトル): -oris 232. 565. 1006. 1040

1041 uicisti Priamum: sortis reminiscere uictor
- [2] 1046 Yicisti Priamum : sortis reminiscere victor
  - *Sortis reminiscere victor Humanae*（勝者よ、人の身の運命を思い起こせ）。この思想が、われらの作者の他の多くの箇所と同様に、オウィディウスの Trist. III, 11, 67 の言葉をほのめかしていることは明白である: « Humanaeque memor sortis, quae tollit eosdem, Et premit, incertas ipse verere vices »。オウィディウスから借用されたこの同じ言葉を、アウソニウスが『イリアス摘要』第24巻で用いている。ユピテルはテティスを息子のもとへ遣わし、死者に対して荒れ狂うのをやめ、息絶えた敵において人間の運命を畏れよという指示を与える。この末尾の語句は誤脱または不完全に見えるが、オウィディウスの言葉から補って *fatique hominum vices ... vereatur* と校訂するのが最善である。実に、われらの作者とアウソニウスがここで提示しているような思想は、マリアンゲルスとウィネトゥスがかつてアウソニウス註釈で指摘したように、ホメロスにはまったく見られない。ホメロスからの離脱においても、オウィディウスの思想の採用においても、両者の一致は実に注目に値し、おそらく両作品の作者が同一人物ではないかという疑いを抱かせるに足るものである。
- [3] 1041 Uicisti Priamum: sortis reminiscere uictor
- [4] 1041 Vicisti Priamum : sortis reminiscere victor
  - Priamum (PRIAMUS; プリアモス): Priamum:汝はプリアモスを征服した(アキレウスに向かって自らについて語る)
- [6] 1041 vicisti Priamum: sortis reminiscere victor
  - Priamum (Priamus; プリアモス): vicisti -mum 1041

1042 humanae uariosque ducum tu respice casus."
- [2] 1047 Humanae, variosque dticum tu respice casus».
- [3] 1042 Humanae uariosque ducum tu respice casus'.
- [4] 1042 Humanae variosque ducum tu respice casus ».
- [6] 1042 humanae variosque ducum tu respice casus'.

1043 His tandem precibus grandaeuum motus Achilles
- [2] 1048 His tandem precibus grandaevum motus Achilles
- [3] 1043 His tandem precibus grandaeuum motus Achilles
- [4] 1043 His tandem precibus grandaevum motus Achilles
  - Achilles (ACHILLES; アキレウス): — プリアモスの嘆願に動かされ、息子の亡骸を返す
- [6] 1043 his tandem precibus grandaevum motus Achilles
  - Achilles (Achilles; アキレウス): -es 211. 988. 997. 1014. 1043
  - grandaevum (Priamus; プリアモス): grandaevum 1043

1044 alleuat a terra corpusque exsangue parenti
- [2] 1049 Adlevat a terra , corpusque exsangue parenti
- [3] 1044 Alleuat a terra corpusque exsangue parenti
- [4] 1044 Allevat a terra corpusque exsangue parenti
  - Hectoreum (HECTOREUS; ヘクトルの): Hectoreum corpus
- [6] 1044 allevat a terra corpusque exsangue parenti
  - parenti (Priamus; プリアモス): parentis 225. 1038. 1044

1045 reddidit Hectoreum. Post haec sua dona reportat
- [2] 1050 Reddidit Hectoreuin : post haec sua dona reportat
  - *Post haec sua dona reportat*（こののちプリアモスは自らの賜物を持ち帰る）。バルトはスタティウス註釈の前掲箇所で、この語句が健全であるか疑っている。というのも、ホメロスにおいてアキレウスが運ばれてきた贈り物をプリアモスに返還したなどということは決してなく、それどころか贈り物ゆえにヘクトルの遺体を返還するのだと公言しているからである。そこでバルトは *sua dona reportat Achilles, It patriam Priamus*（アキレウスは自らの贈り物を持ち去り、プリアモスは祖国へと向かう）と書くことを欲している。しかし私は、その点にこだわる必要はないと考え、*dona*（賜物）によって、プリアモスに与えられたヘクトルの遺体そのものが意味されていると解する。
- [3] 1045 Reddidit Hectoreum, post haec sua dona reportat.
- [4] 1045 Reddidit Hectoreum, post haec sua dona reportat.
- [6] 1045 reddidit Hectoreum. post haec sua dona reportat
  - … dona すなわちヘクトルの遺体
  - Hectoreum (Hectoreus; ヘクトルの): corpus . . . -eum 1045

1046 in patriam Priamus tristesque ex more suorum
- [2] 1051 In patriam Priamus , tristesque ex more suorum
- [3] 1046 It patriam Priamus tristisque ex more suorum
- [4] 1046 Jamque redit Priamus tristesque ex more suorum
  - Priamus (PRIAMUS; プリアモス): — アキレウスがヘクトルの亡骸を返した後、陣営に戻る
- [6] 1046 in patriam Priamus tristesque ex more suorum
  - Priamus (Priamus; プリアモス): Priamus 278 [983] 1046

1047 apparat exsequias extremaque funera ducit.
- [2] 1052 Comparat exsequias , supremaque funera ducit.
- [3] 1047 Comparat exequias supremaque funera ducit.
- [4] 1047 Comparat exsequias supremaque funera ducit.
- [6] 1047 apparat exequias supremaque funera ducit.

1048 Tum pyra construitur, qua bis sex corpora Graium
- [2] 1053 Tunc pyra construitur, quo bis sex corpora Graium
  - … しかしバルトはスタティウス註釈、第3巻395頁でルタティウスの読異に異議を唱え、ヘクトルとともに火葬されたのは断じてトロイア人の遺体であって、ギリシア人のものではないと主張している。彼が考えるには、古代人においては敵が同一の火葬塚に葬られることのないよう厳重な宗教的配慮がなされていたこと、ギリシア人が埋葬のために自軍の遺体をきわめて熱心に回収したことは明白であるからプリアモスの手元にギリシア人の遺体は存在しなかったこと、さらに生きた虜囚を犠牲にすることは恩知らずのプリアモスに対するアキレウスの激しい怒りを招く大きな危険なしにはあり得なかったこと、がその理由である。そして実に、作者はこの件においてヘクトルの葬儀に関するホメロスの記述から離脱しており、パトロクロスの火葬塚に関するホメロスの別の記述（Il. XXIII, 171）や、パラスに捧げられた追悼供儀に関するマロの記述（Aen. XI, 80 以下）に合わせて自らの物語を構成したように思われる。しかしながら、最善の諸写本によって裏づけられている *corpora Graium* という読みは、バルトによって決して退けられるべきではなく、もしそこに何らかの誤りがあるとしても、それは写字生たちの誤りではなく作者自身の過誤である。またバルトが *Troum* と読むべきだとする論拠のすべてに私が賛同できるわけでもない。――*corpora Graium* という読みは、シュラーダーによっても擁護されている（『考察集』第1巻第5章61頁）。パリ編者。
- [3] 1048 Tum pyra construitur, quo bis sex corpora Graium
  - **1048—51** Lactantius が Statius Theb. VI 121 への注で引用（「ホメロスはヘクトルの葬儀において言う」）
- [4] 1048 Tum pyra construitur, quo bis sex corpora Grajum
  - Grajum (GRAI; ギリシア人): — ギリシア人の六つの亡骸がヘクトルの火葬の薪に載せられる
- [6] 1048 tum pyra construitur, qua bis sex corpora Graium
  - **1048/50** （証言） この事柄についてラクタンティウスがスタティウス『テーバイデ』6, 121 の註解で引用 …
  - Graium (Graius; ギリシアの): corpora -um 1048

1049 quadrupedesque adduntur equi currusque tubaeque
- [2] 1054 Quadrupedesque adduntur equi, currusque, tubaeque.
  - … ――火葬塚に戦車やラッパが加えられたと付け加えている点については、ホメロスにはまったく見られないものであり、おそらくウェルギリウスから不適切に借-
  - **(cont.)** （前頁からの続き）-用されたものであろう。ウェルギリウスはミセヌスの墓について Aen. VI, 232 で次のように述べている: « Imponit suaque arma viro, remumque, tubamque »。しかしウィクトルは『ローマ民族起源論』第9章において、ウェルギリウスのその箇所を引用しつつ、ホメロスによればトロイア時代にはラッパの使用は知られていなかったと指摘している。
- [3] 1049 Quadrupedesque adduntur equi currusque tubaeque
- [4] 1049 Quadrupedesque adduntur equi currusque tubaeque
- [6] 1049 quadrupedesque adduntur equi currusque tubaeque

1050 et clipei galeaeque cauae argutaque tela.
- [2] 1055 Et clypei, galeaBque.graves, Argivaque tela.
- [3] 1050 Et clipei galeaeque ocreaeque Argiuaque tela.
- [4] 1050 Et clipei galeaeque cavae Argivaque tela.
  - Argiva (ARGIVUS; アルゴスの): Argivaque tela(主格)
- [6] 1050 cumque cavis galeis clipeique Argivaque tela.
  - Argiva (Argivus; アルゴスの): Argiva . . . tela 1050

1051 Haec super ingenti gemitu componitur Hector:
- [2] 1056 Haec super ingenti gemitu componitur Hector.
- [3] 1051 Haec super ingenti gemitu componitur Hector:
- [4] 1051 Haec super ingenti gemitu componitur Hector :
  - Hector (HECTOR; ヘクトル): — 火葬の薪に横たえられる
- [6] 1051 haec super ingenti gemitu componitur Hector:
  - Hector (Hector; ヘクトル): Hector 256. 277. 491. 626. 677. 774. 959. 967. 979. 996. 1051

1052 stant circum Iliades matres manibusque decoros
- [2] 1057 Stant circum Uiades matres, manibusque decoros
  - *Stant circum Iliades*（トロイアの女たちが周りに立つ）。ウェルギリウスはポリュドロスとパラスの葬儀においてこの慣習が遵守されたことを、Aen. III, 65 および XI, 35 の次の行で示している: *Stant circum Iliades crinem de more solutae*。したがって、われらの詩人が用いる *abrumpere crines*（髪を引きちぎる）は、ウェルギリウスの *solvere crines*（髪を解く）と同じ意味である。
- [3] 1052 Stant circum Iliades matres manibusque decoros
- [4] 1052 Stant circum Iliades matres manibusque decoros
  - Iliades (ILIADES; イリアデス): — イリオンの母たちがヘクトルの亡骸の周りに立つ
- [6] 1052 stant circum Iliades matres manibusque decoros
  - Iliades (Iliades; イリアデス): -des matres 1052

1053 abrumpunt crines laniataque pectora plangunt:
- [2] 1058 Abrumpunt crines, laniataque pectora tundunt :
- [3] 1053 Corrumpunt crines laniataque pectora plangunt
- [4] 1053 Abscindunt crines laniataque pectora plangunt.
- [6] 1053 abrumpunt crines laniataque pectora plangunt:

1054 illo namque rogo natorum funera cernunt.
- [2] 1059 Illo namque rogo natorum funera cernunt.
- [3] 1054 (Illo namque rogo natorum funera cernunt),
- [4] 1054 below Illo namque rogo natorum funera cernunt
- [6] 1054 illo namque rogo natorum funera cernunt.

1055 Tollitur et iuuenum magno cum murmure clamor
- [2] 1060 ToUitur et juvenum magno cum murmure clamor
- [3] 1055 Tollitur et iuuenum magno cum murmure clamor
- [4] 1055 Tollitur et juvenum magno cum murmure clamor
- [6] 1055 tollitur et iuvenum magno cum murmure clamor

1056 flebilis: ardebat flamma namque Ilion illa.
- [2] 1061 Flebilis , ardebat fiamma namque Ilion illa.
  - *Flamma namque Ilion illa*（実にイリオンはその炎によって燃えていた）。338 行を参照。
- [3] 1056 Flebilis: ardebat flamma namque Ilion illa.
- [4] 1056 Flebilis : ardebat flamma namque Ilion illa.
  - Ilion (TROJA; トロイア): — ヘクトルの亡骸が燃えた炎
- [6] 1056 flebilis: ardebat flamma namque Ilion illa.
  - Ilion (Ilion; イリオン): Ilĭŏn 153. 1056

1057 Inter quos gemitus laniato pectore coniunx
- [2] 1062 Inter quos gemitus laniato corpore conjux
- [3] 1057 Inter quos gemitus laniato corpore coniunx
- [4] 1057 Inter quos gemitus laniato corpore conjunx
- [6] 1057 inter quos gemitus laniato pectore coniunx

1058 prouolat Andromache mediosque immittere in ignes
- [2] 1063 Advolat Andromache , mediosque immittere in ignes
- [3] 1058 Prouolat Andromache mediosque inmittere in ignes
- [4] 1058 Provolat Andromache mediosque immittere in ignes
  - Andromache (ANDROMACHE; アンドロマケ): — ヘクトルの亡骸が損なわれると、走り出て嘆く
- [6] 1058 provolat Andromache mediosque inmittere in ignes
  - Andromache (Andromache; アンドロマケ): -ē 1018. 1058

1059 se cupit Astyanacta tenens, quam iussa suarum
- [2] 1064 Se cupit, Astyanacta tenens, quam jussa suorum
- [3] 1059 Se cupit Astyanacta tenens, quam maesta suarum
- [4] 1059 Se cupit Astyanacta tenens, quam maesta suarum
  - Astyanacta (ASTYANAX; アステュアナクス): — 彼を抱くアンドロマケ
- [6] 1059 se cupit Astyanacta tenens, quam iussa suorum
  - Astyanacta (Astyanax; アステュアナクス): Andromache . . . -cta tenens 1059

1060 turba rapit. Contra tamen omnibus usque resistit,
- [2] 1065 Tristis turba rapit : contra tamen usque resistit,
- [3] 1060 Turba rapit comitum; contra tamen usque resistit,
- [4] 1060 Turba rapit; contra tantum tamen illa resistit,
- [6] 1060 turba rapit; contra tamen omnibus usque resistit,

1061 donec collapsae ceciderunt robora flammae
- [2] 1066 Donec collapsae ceciderunt robora flammae,
  - … Virg. Aen. VI, 226: « Postquam collapsi cineres, et flamma quievit »。われらの詩人が *robora flammae*（炎の威力／樫材）と呼んでいる表現を、他の誰かが用いたかどうか私は知らない。しかし *robora* は、火葬塚に組み上げられ、火によって焼き尽くされて灰へと崩れ落ちた樫材のことと理解することもできる。マロがミセヌスの火葬塚について Aen. VI, 213 で次のように述べているのと同様である: « pinguem taedis et robore secto Ingentem struxere pyram »。
- [3] 1061 Donec conlapsae ceciderunt robora flammae
- [4] 1061 Donec collapsae ceciderunt robora flammae
- [6] 1061 donec conlapsae ceciderunt robora flammae

1062 inque leues abiit tantus dux ille fauillas.
- [2] 1067 Inque leves abiit tantus dux ille favillas.
- [3] 1062 Inque leues abiit tantus dux ille fauillas.
- [4] 1062 Inque leves abiit tantus dux ille favillas.
- [6] 1062 inque leves abiit tantus dux ille favillas.
  - dux (Hector; ヘクトル): tantus dux 1062

1063 Sed iam siste gradum finemque impone labori,
- [2] 1068 Sed jam siste gradum, (inemque impone iabori,
  - … ――シドニウス・アポリナリスも同様に歌っている（Carm. 2）: « Siste, Camena, modos tenues, portumque petenti Jam placido sedeat mihi carminis anchora fundo »。パリ編者。
- [3] 1063 Sed iam siste gradum finemque inpone labori,
- [4] 1063 Sed jam siste gradum finemque impone labori,
- [6] 1063 Sed iam siste gradum finemque inpone labori,

1064 Calliope, uatisque tui moderare carinam,
- [2] 1069 Calliope, vatisque tui moderare cariDatn,
  - *Calliope*。作者がここでホメロスの詩行の外側において自らのためにムーサに語りかけていることは、彼がホメロスの『イリアス』をラテン語に要約するにあたり、自身の才知と詩人としての務めの双方を発揮したことを示そうとしているように思われる。私はそのことを彼から全面的に否定しようとは思わない。――*Moderare carinam*（船の舵を取れ）。詩人たちが自らの作品を航海になぞらえ、あるいは戦車や四頭立ての二輪戦車になぞらえるのは、実に通例のことであり、スタティウス（Silv. IV, 4, 99）、ネメシアヌス（Cyneg. 59）、クラウディアヌス（『プロセルピナ略奪』第1巻序文）などによってもなされている。しかし、ここでエピローグのほぼ全体を占めている航海の寓意は、この詩の作者が、『ラテン詩文選』(*Anthol. Lat.*) 第3巻エピグラム62に収められ、われわれがこの詩に関する証言集（『テスティモニア』）にも収録した、あの航海に関するエピグラムの作者と同一人物である可能性を少なからず高めている。そのエピグラムにおいて作者は、海辺の別荘で『イリアス』すなわちトロイア戦争を描き記したと述べ、同時に海の危険と田園の平穏とを対比しているのである。この問題については、われわれは序論（『プロエミウム』）においてさらに詳述した。
- [3] 1064 Calliope, uatisque tui moderare carinam,
- [4] 1064 Calliope, vatisque tui moderare carinam,
  - Calliope (CALLIOPE; カリオペー): 呼格(われらの詩人が祈る)
- [6] 1064 Calliope, vatisque tui moderare carinam,
  - vatis (Baebius; バエビウス): vatis 1064. 1070 を参照
  - Calliope (Calliope; カリオペー): Calliope 呼格 1064

1065 Remis quem cernis stringentem litora paucis,
- [2] 1070 Quem cernis paucis stringentem litora remis.
  - … ――*Paucis remis*（わずかな櫂で）とは、少数の櫂を用いる小さな小舟で、の意である。オリュンピウス『狩猟詩』(*Cyneg.*) 59: « Dum non magna ratis vicinis sueta moveri Litoribus, tutosque sinus percurrere remis »。――またクラウディアヌス前掲箇所（本叢書版第2巻182頁以下、パリ編者）: « Qui dubiis ausus committere flatibus alnum, Quas natura negat, praebuit arte vias, Tranquillis primum trepidus se credidit undis, Litora securo tramite summa legens »。パリ編者。
- [3] 1065 Remis quam cernis stringentem litora paucis.
- [4] 1065 Raris quam cernis stringentem litora remis,
- [6] 1065 Remis quem cernis stringentem litora paucis.

1066 Iamque tenet portum metamque potentis Homeri.
- [2] 1071 Jamque tenens portum metamque patentis Homeri ,
  - … というのも、詩人はホメーロスの大作を広漠たる外海のように今や測り終えた、と言おうとしているからである。ホラティウスの Carm. II, 16, 1: *in patenti Prensus Aegaeo*（広大なるエーゲ海で捕らえられし者）。――また動詞 *patefecit* は、サレイウス・バッスス『ピソーへの詩』(*Carm. ad Pisonem*) 230 行において、別の注目すべき意味で現れている: « Ausoniamque chelyn gracilis patefecit Horati »。そこで動詞 *patefacere* を「高名にする、世の名声に示す」と正しく解釈できたとすれば、ここでは *patentis Homeri* を「名声が万人にあまねく知れ渡った名高い、誉れ高き詩人の」と解釈することもあながち不当ではあるまい。本巻の前掲箇所註釈（265頁以下）を参照されたい。もっとも私はこの所見をいわば余剰のものとして付け加えるのであり、そのためにヴェルンスドルフの解釈を捨てるべきだとは考えていない。パリ編者。
- [3] 1066 Iamque tenens portum metamque potentis Homeri,
- [4] 1066 Iamque tenens portum metamque potentis Homeri,
  - Homeri (HOMERUS; ホメロス): Homeri:カリオペーはわれらの詩人とともに、力強きホメロスの折り返し点に達する
- [6] 1066 Iamque tenet portum metamque potentis Homeri:
  - Homeri (Homerus; ホメロス): metam . . . potentis Homeri 1066

1067 Pieridum comitata cohors, summitte rudentes
- [2] 1072 Pieridum comitata cohors , submitte rudentes;
  - *Submitte rudentes*（索具を降ろせ）：帆を縮めて降ろせ、の意。ウェルギリウスが Georg. IV, 116 で次のように述べたのと同じである: « extremo ni jam sub fine laborum Vela traham, et terris festinem advertere proram »。またスタティウスが『テーバイス』の完成について Silv. IV, 4, 89 で述べているのと同様である: « Jam Sidonios emensa labores Thebais optato collegit carbasa portu »。
- [3] 1067 Pieridem comitata cohors, summitte rudentes;
- [4] 1067 Pieridum comitata cohors, summitte rudentes;
  - Pieridum (PIERIDES; ピエリデス): Pieridum cohors:ピエリデスの一団
- [6] 1067 Pieridum comitata cohors, summitte rudentes
  - Pieridum (Pieris; ピエリス): Pieridum . . . cohors 1067

1068 Sanctaque uirgineos lauro redimita capillos
- [2] 1073 Sanetaque virgineos lauro redimita capillos
  - *Sanctaque virgineos lauro redimita*（月桂樹で乙女の髪を飾られた聖なる者よ）。いつもの習いとして、作者はムーサたちの隊伍を二重の修飾辞で飾っている。――1021 行および 1026 行の注を参照。パリ編者。
- [3] 1068 Sanctaque uirgineos lauro redimita capillos,
- [4] 1068 Sanctaque virgineos lauro redimita capillos,
- [6] 1068 Sanctaque virgineos lauro redimita capillos

1069 Ipsa tuas depone lyras. Ades, inclita Pallas,
- [2] 1074 Ipsa tuas depone lyras : ades, inclyta Pallas,
  - われらの詩人が複数形で *lyras*（リラ琴）と言ったことについて、バルトは『雑考』(*Adv.*) LVIII, 14, 2753 頁で、これは正統なラテン語ではないと断定している。私としてはこれをにわかに断定することは控えたい。むしろ次の点に注意を促したい。すなわち *lyra* や *chelys* は常に抒情詩についてのみ用いられるわけではなく、他の詩、とりわけ叙事詩についても言われるということである。スタティウスの Silv. II, 2, 114 に見られる通りである: « Seu nostram quatit ille chelyn, seu dissona nectit Carmina »（彼は叙事詩のヘクサメトロスとエレゲイアの詩行を意味している）。――*adsis* の代わりに *Ades, inclyta Pallas*。パリ編者。
- [3] 1069 Ipsa, tuas depone lyras, ades, inclita Pallas,
  - Ipsa（= era、すなわち Calliope）…
- [4] 1069 Ipsa, tuas depone lyras, ades, inclita Pallas,
  - Pallas (MINERVA; ミネルウァ): 呼格:名高き者よ、来たれ(詩人が、道程を走り終えて女神に祈る)
- [6] 1069 Ipsa tuas depone lyras. ades, inclita Pallas,
  - Pallas (Pallas; パラス): 呼格:ades, inclita -as 1069

1070 Tuque faue cursu uatis iam, Phoebe, peracto.
- [2] 1075 Tuque fave, cursu vatis jam, Phoebe, peracto.
  - *Jam, Phoebe, peracto*（ポエブスよ、今や詩人の航海が終わりて）。これらの言葉によって、作者はポエブスを祈願した 164 行を振り返っているように思われる。パリ編者。
- [3] 1070 Tuque faue cursu uatis iam, Phoebe, peracto.
- [4] 1070 Tuque fave vati, cursu jam, Phoebe, peracto.
  - Phoebe (APOLLO; アポロ): Phoebus Phoebe(われらの詩人が、道程を終えて神に祈る)
- [6] 1070 Tuque fave cursu vatis iam, Phoebe, peracto.
  - vatis (Baebius; バエビウス): vatis 1064. 1070 を参照
  - Phoebe (Phoebus; ポエブス): Phoebĕ 1070
