인공지능 과제 "12월1일~15일간의 제주 입도 관광객 수 자료를 이용하여 일별 방문자 수 예측하기"


자료 출처 : 제주관광협회 http://www.visitjeju.or.kr/web/bbs/bbsDtl.do?pageIndex=1&sBbsId=TOURSTATD&bbsId=TOURSTATD&noticeNum=2621&authNum=&sKeyOpt=1&sKey=


1.모듈 불러오기

<pre><code>from prediction_util import PredictionUtil as pu
import pandas as pd
</code></pre>

2.객체 만들기
<pre><code>gildong=pu()
</code></pre>

3.Date set 전처리 
<pre><code>gildong.read('jejuvisit2.csv')</code></pre>
<img width="200" height="200" alt="데이터리드" src="https://user-images.githubusercontent.com/55755351/71154186-4e1d7b00-227e-11ea-87a0-04f395a0f53f.PNG">

date는 일자를, visit은 관광객 수, day는 요일, holiday 0은 평일, 1은 주말 및 휴일을 뜻합니다.



4.일자와 휴일, 관광객 간의 상호관계 확인
<pre><code>gildong.lmplot('date','visit','holiday')</code></pre>
<img width="521" alt="3 lm플롯" src="https://user-images.githubusercontent.com/55755351/71154643-52966380-227f-11ea-83a7-a56b2ed23468.PNG">


<pre><code>gildong.boxplot('day','visit')</code></pre>
<img width="806" alt="4박스플롯" src="https://user-images.githubusercontent.com/55755351/71154723-883b4c80-227f-11ea-9828-2064bab2acc3.PNG">
결과와 같이 월,목,일 항공권이 저렴한때 혹은 휴일 전후가 관광객 수가 많은것을 확인 할 수 있었습니다.


<pre><code>gildong.plot_3d('date','holiday','visit')</code></pre>
<img width="644" alt="5 3d플롯" src="https://user-images.githubusercontent.com/55755351/71154793-b4ef6400-227f-11ea-81fd-9314968d1397.PNG">


<pre><code>gildong.heatmap(['date','holiday','visit'])</code></pre>
<img width="741" alt="6 heat맵" src="https://user-images.githubusercontent.com/55755351/71154832-cb95bb00-227f-11ea-85b7-8a682235400a.PNG">


5.상관관계를 이용하여 제주에 입도하는 관광객 수 예측하기
<pre><code>gildong.run_all(['date'],'visit')</code></pre>
<img width="500" alt="런올!!!" src="https://user-images.githubusercontent.com/55755351/71154966-17486480-2280-11ea-887b-1ee96d877ce0.PNG">

예측의 결과로 decision_tree와 random_forest를 이용하는것이 인식률이 높은것을 확인할  있었습니다.
감사합니다.
