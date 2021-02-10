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








