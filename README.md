인공지능 과제 "12월1일~15일간의 제주입도 관광객 수를 가지고 휴일별 방문자 수 예측하기"

출처 : http://www.visitjeju.or.kr/web/bbs/bbsDtl.do?pageIndex=1&sBbsId=TOURSTATD&bbsId=TOURSTATD&noticeNum=2621&authNum=&sKeyOpt=1&sKey=



1.모듈 불러오기

<pre><code>from prediction_util import PredictionUtil as pu
import pandas as pd
</code></pre>

2.객체 만들기
<pre><code>gildong=pu()
</code></pre>

3.Date set 전처리 
<pre><code>gildong.read('jejuvisit2.csv')</code></pre>
