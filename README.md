# crawl-stock

# 可惡，grs 好多錯的資料，不想改了，砍掉重練

<p>這是一個用來爬台灣股市的程式，用了 grs 套件。</p>

## 用法說明

### 更新股市資料庫

<code>python prune_unused_stocknumber.py</code>

<p>把新的<b>股市清單</b>貼到 stocknumber.csv 中後，用 prune_unused_stocknumber.py 把認購權證, 認售權證, 熊證, 牛證, 受益證券移除，約剩下 10% 的股票清單。<b>股市清單</b>規格可以參照 grs 原本的檔案</p>



###抓資料 and 更新資料
<code>python crawl.py</code>

1. <b>抓資料</b>：如果沒有資料的話，會去用二分搜尋法找出該股票有的最多月份（最多以 480 個月計）
2. <b>更新資料</b>：如果有資料的話，會抓最後一筆的時間，直接 append 上去，新 append 的資料<b>最多</b>跟就資料差三個月（預設不會三個月沒抓）

## 版本更新

###v1.2.0

1. 加了 validateData.py 可以驗證抓到的資料
2. crawl.py 後面可以加上從第幾號開始，抓到第幾號，比如說：

<code>python crawl.py 0050 4413</code>


###v1.1.0

1. 股票清單加了上櫃列表，2015/02/02 更新

###v1.0.0

1. 基礎陽春版

## 待更新功能
1. 抓系統時間，如果超過三個月還是可以更新
2. 加入基本 shell script
