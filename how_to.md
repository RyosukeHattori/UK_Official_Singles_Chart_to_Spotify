# Spotifyが公開しているAPIを使用してUK Official Chart Top 100に対応したプレイリストを作ってみた

Sportifyとは世界中の音楽が聴き放題の神アプリです。
筆者は、通勤などの移動の際には必ずSportifyを使用して音楽を聞いています。
Sportifyのいい所は、プレイリストが豊富であり、
* Top Chartプレイリスト
* アーティスト別のプレイリスト    
* 好きなアーティストに関連する曲が含まれるプレイリスト
* 自分にオススメの曲で構成されたプレイリスト
などがあります。

また、SportifyはSHAZAMと連携することができ、SHAZAMした曲を1つのプレイリストにまとめることができます。

筆者はDJをしていますので、これらの機能があるSportifyをとても愛用しています。

こんな"最高の"Sportifyですが、一点だけ不満があります。
それは、Top Chartプレイリストの曲が日々更新されてしまうことです。
DJをしている私にとっては、どの月に何は流行っていたのかを知りたいので、1つのTop Chartプレイリストで中身の曲が変わるよりも、
1月のTop Chartプレイリスト、2月のTop Chartプレイリストなど月別で別れている方が望ましいです。

そこで、Spotifyが公開しているAPIを使用して月別のUK Official Chart Top 100プレイリストを作りました。
コードはhttps://github.com/RyosukeHattori/UK_Official_Singles_Chart_to_Spotifyです。

##Jupyter notebookを動かすには

notebookの2セル目の
```
with open("your_ID.txt") as f:
    l = f.readlines()
```
のyour_ID.txtには、Spotify for Developersにて、Spotify APIを使用するために必要なclient IDとclient secret、usernameをこの順に記入します。

これでとりあえず、動きます。

14セルで出力される"This is None Track"は生成するSpotifyのプレイリストに含むことができない曲です。
ここで出力される曲と15セルで出力される行番号がUK Official Chart Top 100のランキングに対応します。
つまり、14セル目で
```
this track is None:READY/FREDO FT SUMMER WALKER
this track is None:FRIDAY/RITON/NIGHTCRAWLERS/MUFASA
this track is None:LOVE NOT WAR (THE TAMPA BEAT)/JASON DERULO & NUKA
this track is None:BE THE ONE/RUDIMENTAL/MORGAN/DIGGA D/TIKE
this track is None:FOREVER YOUNG/BECKY HILL
```
と出力され、15セル目で
```
      id track artist
20  None  None   None
23  None  None   None
31  None  None   None
57  None  None   None
84  None  None   None
```
と、出力されたとすると
それは、
UK Official Chart Top 100に含まれる
20位のREADY/FREDO FT SUMMER WALKER
23位のFRIDAY/RITON/NIGHTCRAWLERS/MUFASA
：
：
84位のFOREVER YOUNG/BECKY HILL
がプレイリストから欠損していることを意味します。
これらの欠損した曲は手動で加えてください。
また、欠損が出ないようなプログラムの書き方を教えてください！！！










