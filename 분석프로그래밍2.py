from pandas import Series, DataFrame #파이썬에서 pandas패키지의Series와 데이터프레임을 사용
import pandas as pd #pandas 패키지를 pd로 줄여서 사용
import numpy as np  #numpy패키지를 np로 줄여서 사용   



dc= pd.read_table('Data2_Clickstreams.tab', sep='\t', encoding='mbcs') # Data2_Clickstreams.tab파일을 읽어서 dc라는 변수에 저장한다.(encoding='mbcs'는 한글 파일을 읽기 위해서 쓴다.)
mu=dc[dc.ACT_NM=='동영상/비디오'] # ACT_NM에서 '동영상/비디오' 인것만 추출

mu['ym']=mu.TIME_ID.astype(str).str[:6] # TIME_ID를 문자열로 type 변환시키고 문자열을 0~5(연,월)까지 뽑은 것들을 mu의 'ym'에 저장
mu['h']=mu.TIME_ID.astype(str).str[8:10] #TIME_ID를 문자열로 type 변환시키고 문자열을 8~9(시간)까지 뽑은 것들을 mu의 'h'에 저장
mu['ymd']=mu.TIME_ID.astype(str).str[:8]  # TIME_ID를 문자열로 type 변환시키고 문자열을 0~7(연,월,일)까지 뽑은 것들을 mu의 'ymd'에 저장


ca=dc[dc.ACT_NM=='포털만화'] #ACT_NM에서 '포털만화'만 따로 추출하여 ca에 저장

ca['ym']=ca.TIME_ID.astype(str).str[:6] # TIME_ID를 문자열로 type 변환시키고 문자열을 0~5(연,월)까지 뽑은 것들을 ca의 'ym'에 저장

bi=mu[mu.SITE_NM=='비메오'] #SITE_NM에서 '비메오'인 것만 bi에 저장
 
yu=mu[mu.SITE_NM=='YouTube'] #SITE_NM에서 'YouTube'인 것만 yu에 저장

di=mu[mu.SITE_NM=='Dailymotion'] #SITE_NM에서 'Dailymotion'인 것만 di에 저장

#평균 체류시간 비교    


bis=bi[['ym','SITE_CNT','ST_TIME']] #비메오의 기간별 체류시간과 페이지뷰
biss=bis.groupby('ym',as_index=False).mean() #비메오의 기간별 체류시간과 페이지뷰의 평균

bb=pd.Series(biss.ST_TIME) #비메오의 체류시간과 페이지뷰를 plot하기 위해 시리즈로 만들기
bb.index=biss.ym #기간에 따른 체류시간을 나타내기 위해 index를 기간으로 바꾸기 


yus=yu[['ym','SITE_CNT','ST_TIME']] #youtube의 기간별 체류시간과 페이지뷰
yuss=yus.groupby('ym',as_index=False).mean() #youtube의 시간별 체류시간과 페이지뷰의 평균

yy=pd.Series(yuss.ST_TIME)#youtube의 체류시간과 페이지뷰를 plot하기 위해 시리즈로 만들기
yy.index=yuss.ym #기간에 따른 체류시간을 나타내기 위해 index를 기간으로바꾸기

dis=di[['ym','SITE_CNT','ST_TIME']]  #데일리모션의 기간별 체류시간과 페이지뷰
diss=dis.groupby('ym',as_index=False).mean() #데일리모션의 시간별 체류시간과 페이지뷰의 평균

dd=pd.Series(diss.ST_TIME) #데일리모션의 체류시간과 페이지뷰를 plot하기 위해 시리즈로 만들기
dd.index=diss.ym   #기간에 따른 체류시간을 나타내기 위해 index를 기간으로바꾸기

#그래프 그리기
%pylab inline 
plt.rc('font', family='Malgun Gothic') #폰트를 맑은 고딕으로 변경
plt.style.use('ggplot')   #ggplot 그래프 사용
yy.plot(color="r",label='YouTube') #yy의 plot을 색깔은 빨강색으로 하고 라벨을 'YouTube'로 하여 그려라
bb.plot(color="g",label='비메오') #bb의 plot을 색깔은 녹색으로 하고  라벨을 '비메오'로 하여 그려라
dd.plot(color='y',label='Dailymotion') #dd의 plot을 색깔은 노란색으로 하고 라벨을 'Dailymotion'로 하여 그려라
plt.legend(loc=1)   #오른쪽 맨위로 legend 설정
plt.xlabel('기간(월)') # x축의 라벨을 '기간(월)'로 설정
plt.ylabel('평균 체류시간(초)') #y축의 라벨을 '평균 체류시간(초)'로 설정
plt.title('평균 체류시간 비교') #plot 의 title을 '평균 체류시간 비교'로 설정
savefig('평균 체류시간.png') #그래프 저장하기


#평균 페이지뷰(1인당 페이지뷰)

bbp=pd.Series(biss.SITE_CNT) #비메오의 체류시간과 평균 페이지뷰를 plot하기 위해 시리즈로 만들기
bbp.index=biss.ym #평균 페이지뷰를 나타내기 위해 index를 기간으로바꾸기


yyp=pd.Series(yuss.SITE_CNT) #youtube의 체류시간과 페이지뷰를 plot하기 위해 시리즈로 만들기
yyp.index=yuss.ym #평균 페이지뷰를 나타내기 위해 index를 기간으로바꾸기


ddp=pd.Series(diss.SITE_CNT) #데일리모션의 체류시간과 페이지뷰를 plot하기 위해 시리즈로 만들기
ddp.index=diss.ym #평균 페이지뷰를 나타내기 위해 index를 기간으로바꾸기

yyp.plot(color="r",label='YouTube') #yyp의 plot을 색깔은 빨강색으로 하고 라벨을 'YouTube'로 하여 그려라
bbp.plot(color="g",label='비메오') #bbp의 plot을 색깔은 녹색으로 하고  라벨을 '비메오'로 하여 그려라
ddp.plot(color='y',label='Dailymotion') #ddp의 plot을 색깔은 노란색으로 하고 라벨을 'Dailymotion'로 하여 그려라
plt.legend(loc=1) #오른쪽 맨위로 legend 설정
plt.xlabel('기간(월)') #x축의 라벨을 '기간(월)'로 설정
plt.ylabel('페이지뷰') #y축의 라벨을 '페이지뷰'로 설정
plt.title('평균 페이지뷰 비교') #plot 의 title을 '평균 페이지뷰 비교'로 설정
savefig('평균 페이지뷰.png') #그래프 저장하기



#총체류시간 비교

bit=bis.groupby('ym',as_index=False).sum()  #비메오의 기간별 체류시간과 페이지뷰의 총합계
bits=pd.Series(bit.ST_TIME) #비메오의 기간별 총 체류시간과 페이지뷰를 plot하기 위해 시리즈로 만들기
bits.index=bit.ym #총 체류시간을 나타내기 위해 index를 기간으로바꾸기


yut=yus.groupby('ym',as_index=False).sum() #YouTube의 기간별 체류시간과 페이지뷰의 총합계
yuts=pd.Series(yut.ST_TIME) #YouTube의 기간별 총 체류시간과 페이지뷰를 plot하기 위해 시리즈로 만들기
yuts.index=yut.ym #총 체류시간을 나타내기 위해 index를 기간으로바꾸기


dit=dis.groupby('ym',as_index=False).sum() #Dailymotion의 기간별 체류시간과 페이지뷰의 총합계
dits=pd.Series(dit.ST_TIME) #Dailymotion의 기간별 총 체류시간과 페이지뷰를 plot하기 위해 시리즈로 만들기
dits.index=dit.ym #총 체류시간을 나타내기 위해 index를 기간으로바꾸기


yuts.plot(color="r",label='YouTube') #yuts의 plot을 색깔은 빨강색으로 하고 라벨을 'YouTube'로 하여 그려라
bits.plot(color="g",label='비메오') #bits plot을 색깔은 녹색으로 하고  라벨을 '비메오'로 하여 그려라
dits.plot(color='y',label='Dailymotion') #dits의 plot을 색깔은 노란색으로 하고 라벨을 'Dailymotion'로 하여 그려라
plt.legend(loc=1) #오른쪽 맨위로 legend 설정
plt.xlabel('기간(월)') #x축의 라벨을 '기간(월)'로 설정
plt.ylabel('체류시간(초)') #y축의 라벨을 '체류시간(초)'로 설정
plt.title('총 체류시간 비교') #plot 의 title을 '총 체류시간 비교'로 설정
savefig('총 체류시간.png') #그래프 저장하기

#총 페이지뷰 비교


bitc=pd.Series(bit.SITE_CNT) #비메오의 기간별 체류시간과 총 페이지뷰를 plot하기 위해 시리즈로 만들기
bitc.index=bit.ym #총 페이지뷰를 나타내기 위해 index를 기간으로바꾸기


yutc=pd.Series(yut.SITE_CNT) #YouTube의 기간별 체류시간과 총 페이지뷰를 plot하기 위해 시리즈로 만들기
yutc.index=yut.ym #총 페이지뷰를 나타내기 위해 index를 기간으로바꾸기


ditc=pd.Series(dit.SITE_CNT) #Dailymotion의 기간별 체류시간과 총 페이지뷰를 plot하기 위해 시리즈로 만들기
ditc.index=dit.ym #총 페이지뷰를 나타내기 위해 index를 기간으로바꾸기


yutc.plot(color="r",label='YouTube') #yutc의 plot을 색깔은 빨강색으로 하고 라벨을 'YouTube'로 하여 그려라
bitc.plot(color="g",label='비메오') #bitc plot을 색깔은 녹색으로 하고  라벨을 '비메오'로 하여 그려라
ditc.plot(color='y',label='Dailymotion') #ditc의 plot을 색깔은 노란색으로 하고 라벨을 'Dailymotion'로 하여 그려라
plt.legend(loc=1) #오른쪽 맨위로 legend 설정
plt.xlabel('기간(월)') #x축의 라벨을 '기간(월)'로 설정
plt.ylabel('페이지뷰') #y축의 라벨을 '페이지뷰'로 설정
plt.title('총 페이지뷰 비교') #plot 의 title을 '총 페이지뷰 비교'로 설정
savefig('총 페이지뷰.png') #그래프 저장하기

#파이차트
dp=pd.read_excel('Data1_Profiles.xlsx',encoding='mbcs') # Data1_Profiles파일 읽어오기
mb=pd.merge(bi,dp,on='CUS_ID')  #bi와 dp를 CUS_ID로 merge하기
my=pd.merge(yu,dp,on='CUS_ID') #yu와 dp를 CUS_ID로 merge하기
md=pd.merge(di,dp,on='CUS_ID') #di와 dp를 CUS_ID로 merge하기


mb['age']=pd.cut(mb.AGE, bins=[0, 20, 30, 40, 50,60, 80],right=False, labels=['10대 이하', '20대', '30대','40대','50대','60대 이상'])
#나이구간을 0~19,20~29,30~39,40~49,50~59,60~79으로 정하고 명칭을 '10대 이하', '20대', '30대','40대','50대','60대 이상'으로 설정
my['age']=pd.cut(my.AGE, bins=[0, 20, 30, 40, 50,60, 80],right=False, labels=['10대 이하', '20대', '30대','40대','50대','60대 이상'])
#나이구간을 0~19,20~29,30~39,40~49,50~59,60~79으로 정하고 명칭을 '10대 이하', '20대', '30대','40대','50대','60대 이상'으로 설정
md['age']=pd.cut(md.AGE, bins=[0, 20, 30, 40, 50,60, 80],right=False, labels=['10대 이하', '20대', '30대','40대','50대','60대 이상'])
#나이구간을 0~19,20~29,30~39,40~49,50~59,60~79으로 정하고 명칭을 '10대 이하', '20대', '30대','40대','50대','60대 이상'으로 설정


mbd=mb.drop_duplicates(['CUS_ID']) #방문중복제거
myd=my.drop_duplicates(['CUS_ID']) #방문중복제거
mdd=md.drop_duplicates(['CUS_ID']) #방문중복제거

mbdd = mbd.groupby('age').size() #비메오 나이대별 고객수
plt.style.use('ggplot') #pie 차트 이용하기 위하여 ggplot 사용
mbdd.plot(kind='pie',autopct='%1.1f%%',figsize=(6,6),shadow=True) #파이차트 그림자 설정 및 크기 설정
title("비메오 접속 연령대") #plot 의 title을 '비메오 접속 연령대'로 설정
savefig('비메오 파이차트.png') #그래프 저장하기

mydd = myd.groupby('age').size()  #유투브 나이대별 고개수
mydd.plot(kind='pie',autopct='%1.1f%%',figsize=(6,6),shadow=True) #파이차트 그림자 설정 및 크기 설정
title("YouTube 접속 연령대") #plot 의 title을 'YouTube 접속 연령대'로 설정
savefig('유툽 파이차트.png') #그래프 저장하기

mddd = mdd.groupby('age').size() #데일리모션 나이대별 고객수
mddd.plot(kind='pie',autopct='%1.1f%%',figsize=(6,6),shadow=True) #파이차트 그림자 설정 및 크기 설정
title("Dailymotion 접속 연령대") #plot 의 title을 'Dailymotion 접속 연령대'로 설정
savefig('데일리 파이차트.png') #그래프 저장하기


# 방문자수 분석


bid=pd.merge(bi,dp,on='CUS_ID') #비메오 데이터프레임과 고객정보 데이터프레임 merge
bids=bid[['CUS_ID','ym','GENDER','AGE']]# bids에 bid의 'CUS_ID','ym','GENDER','AGE'를 가져온다
bidsv=pd.pivot_table(bids,values='CUS_ID',index='ym',aggfunc=np.size,fill_value=0).reset_index() #월별 비메오 방문자수를 구하기 위해 고객의 크기를 값으로 설정하고 기간을 index로하여 피벗 테이블 생성
bidsvs=pd.Series(bidsv.CUS_ID) #bidsv의 고객정보의 데이터 프레임을 Series로 변환
bidsvs.index=bidsv.ym #월별 방문자 수를 나타내기 위해 index를 기간으로 바꾸기


yud=pd.merge(yu,dp,on='CUS_ID') #YouTube 데이터프레임과 고객정보 데이터프레임 merge
yuds=yud[['CUS_ID','ym','GENDER','AGE']] # yuds에 yud의 'CUS_ID','ym','GENDER','AGE'를 가져온다
yudsv=pd.pivot_table(yuds,values='CUS_ID',index='ym',aggfunc=np.size,fill_value=0).reset_index()#월별 유튜브 방문자수를 구하기 위해 고객의 크기를 값으로 설정하고 기간을 index로하여 피벗 테이블 생성
yudsvs=pd.Series(yudsv.CUS_ID) #yudsv의 고객정보의 데이터 프레임을 Series로 변환
yudsvs.index=bidsv.ym #월별 방문자 수를 나타내기 위해 index를 기간으로 바꾸기



did=pd.merge(di,dp,on='CUS_ID') #Dailymotion 데이터프레임과 고객정보 데이터프레임 merge
dids=did[['CUS_ID','ym','GENDER','AGE']] # dids에 did의 'CUS_ID','ym','GENDER','AGE'를 가져온다
didsv=pd.pivot_table(dids,values='CUS_ID',index='ym',aggfunc=np.size,fill_value=0).reset_index()#월별 Dailymotion 방문자수를 구하기 위해 고객의 크기를 값으로 설정하고 기간을 index로하여 피벗 테이블 생성
didsvs=pd.Series(didsv.CUS_ID) #didsv의 고객정보의 데이터 프레임을 Series로 변환
didsvs.index=didsv.ym #월별 방문자 수를 나타내기 위해 index를 기간으로 바꾸기


plt.style.use("ggplot") #ggplot 그래프 사용
bidsvs.plot(color="g",label='비메오') #bidsvs의 plot를 색깔은 녹색으로 하고  라벨을 '비메오'로 하여 그려라
yudsvs.plot(color='r',label='YouTube') #yudsvs의 plot을 색깔은 빨강색으로 하고 라벨을 'YouTube'로 하여 그려라
didsvs.plot(color='y',label='Dailymotion') #didsvs의 plot를 색깔은 노란색으로 하고  라벨을 'Dailymotion'로 하여 그려라
plt.legend(loc=1) #오른쪽 맨위로 legend 설정
plt.xlabel('기간(월)') #x축의 라벨을 '기간(월)'로 설정
plt.ylabel('방문자수') #y축의 라벨을 '방문자수'로 설정
plt.title('월별 방문자수') #plot 의 title을 '월별 방문자수'로 설정
savefig('월별 방문자수.png') #그래프 저장하기

#높은 방문자수가 있었던 달 분석

mbb=mb[(mb.ym=='201211')] #mb에서 방문자수가 높은연월인 201211을 구해서 mbb에 저장
abb=mb[(mb.ym=='201305')] #mb에서 방문자수가 높은연월인 201305를 구해서 abb에 저장

p=pd.concat([mbb,abb]) #mbb와 abb를 열로 하여 p에 저장
pp = pd.crosstab(p['ym'], p['GENDER'], values=p['CUS_ID'], aggfunc=np.size) #행이 연월이고 열이 성별인 교차테이블
ppp=pp.div(pp.sum(1),axis=0) # 비율을 구하기 위해 div함수를 취한다. 
pp.index.name=None #pp의 index 이름을 없앤다.
ppp.plot(kind='barh',sharey=True,stacked=True) # 누운 막대 그래프를 그리기 위하여 설정한다
savefig('두기간 성별 차이.png') #그래프 저장하기


pa = pd.crosstab(p['ym'], p['age'], values=p['CUS_ID'], aggfunc=np.size) #행이 연월이고 열이 나이대인 교차테이블
pap=pa.div(pa.sum(1),axis=0) # 비율을 구하기 위해 div함수를 취한다. 
pap.index.name=None #pap의 index 이름을 없앤다.
pap.plot(kind='barh',sharey=True,stacked=True) # 누운 막대 그래프를 그리기 위하여 설정한다
savefig('두기간 나이대 차이.png') #그래프 저장

#비메오 총페이지수 바그래프

bbit=bit  #bit와 똑같은 데이터프레임을 bbit에 설정
bbit.index=bbit.ym  #bitt의 인덱스를 날짜로 변경
bbit=bbit[['SITE_CNT']]  #페이지뷰 정보만 취하기
bbit.columns=['페이지뷰'] #열이름을 페이지뷰로 바꾸기



bbit.plot(kind='bar',figsize=(8,8),color='g',legend=False) # color를 녹색으로 설정하고 legend를 설정하지 않은 barplot을 그린다
plt.xlabel('기간(월)') #x축의 라벨을 '기간(월)'로 설정
plt.ylabel('페이지뷰') #y축의 라벨을 '페이지뷰'로 설정
plt.title('비메오 월별 페이지뷰') #plot 의 title을 '비메오 월별 페이지뷰'로 설정
savefig('비메오 월별 페이지뷰 막대.png') #그래프 저장하기


#방문자 깊이

#비메오
pbi=bi[['CUS_ID','SITE_CNT']] #비메오의 고객별 페이지뷰를 비교 하기 위하여 CUS_ID와 SITE_CNT를 따로 뽑아 설정한다.
pbi['방문자깊이']=pd.cut(pbi.SITE_CNT,bins=[1,2,11,51,200],right=False,labels=['뜨내기 방문자','정보탐색자','충성고객','VIP']) #페이지뷰별로 분류하기 위하여 페이지뷰 구간은 1,2~10,11~50,51~199로 설정하고 각각의 라벨을 '뜨내기 방문자','정보탐색자','충성고객','VIP로 분류한다.
pbii=pbi.groupby('방문자깊이').size() #방문자깊이별 고객수를 구하기 위해 방문자 깊이의 크기를 값으로 groupby한다.

pbii.plot(kind='pie',autopct='%1.1f%%',figsize=(6,6),shadow=True) #비율을 비교하기 위하여 파이 차트를 설정한다
title("페이지뷰별 비메오 방문자 구성비율") #plot 의 title을 "페이지뷰별 비메오 방문자 구성비율"'로 설정
savefig('비메오 방문자 깊이 파이차트.png') #그래프 저장


#YouTube

pyu=yu[['CUS_ID','SITE_CNT']]  #YouTube의 고객별 페이지뷰를 비교 하기 위하여 CUS_ID와 SITE_CNT를 따로 뽑아 설정한다.
pyu['방문자깊이']=pd.cut(pyu.SITE_CNT,bins=[1,2,11,51,200],right=False,labels=['뜨내기 방문자','정보탐색자','충성고객','VIP']) #페이지뷰별로 분류하기 위하여 페이지뷰 구간은 1,2~10,11~50,51~199로 설정하고 각각의 라벨을 '뜨내기 방문자','정보탐색자','충성고객','VIP로 분류한다.
pyuu=pyu.groupby('방문자깊이').size() #방문자깊이별 고객수를 구하기 위해 방문자 깊이의 크기를 값으로 groupby한다.

pyuu.plot(kind='pie',autopct='%1.1f%%',figsize=(6,6),shadow=True) #비율을 비교하기 위하여 파이 차트를 설정한다
title("페이지뷰별 YouTube 방문자 구성비율") #plot 의 title을 "페이지뷰별 YouTube 방문자 구성비율"'로 설정
savefig('유툽 방문자 깊이 파이차트.png') #그래프 저장



#데일리

pdi=di[['CUS_ID','SITE_CNT']] #Datilymotion의 고객별 페이지뷰를 비교 하기 위하여 CUS_ID와 SITE_CNT를 따로 뽑아 설정한다.
pdi['방문자깊이']=pd.cut(pdi.SITE_CNT,bins=[1,2,11,51,200],right=False,labels=['뜨내기 방문자','정보탐색자','충성고객','VIP']) #페이지뷰별로 분류하기 위하여 페이지뷰 구간은 1,2~10,11~50,51~199로 설정하고 각각의 라벨을 '뜨내기 방문자','정보탐색자','충성고객','VIP로 분류한다.
pdii=pdi.groupby('방문자깊이').size() #방문자깊이별 고객수를 구하기 위해 방문자 깊이의 크기를 값으로 groupby한다.


pdii.plot(kind='pie',autopct='%1.1f%%',figsize=(6,6),shadow=True) #비율을 비교하기 위하여 파이 차트를 설정한다
plt.title("페이지뷰별 Dailymotion 방문자 구성비율") #plot 의 title을 "페이지뷰별 Dailymotion 방문자 구성비율"'로 설정
savefig('데일리 방문자 깊이 파이차트.png')  #그래프 저장

#방문자 깊이 비율

apyu=yu[['CUS_ID','SITE_NM','SITE_CNT']] #apyu에 yu의 'CUS_ID','SITE_NM','SITE_CNT'저장
apbi=bi[['CUS_ID','SITE_NM','SITE_CNT']] #apbi에 bi의 'CUS_ID','SITE_NM','SITE_CNT'저장
apdi=di[['CUS_ID','SITE_NM','SITE_CNT']] #apdi에 di의 'CUS_ID','SITE_NM','SITE_CNT'저장

mg=pd.concat([apyu,apbi,apdi]) #apyu,apbi,apdi행 bind
mg['방문자깊이']=pd.cut(mg.SITE_CNT,bins=[1,2,11,51,200],right=False,labels=['뜨내기 방문자','정보탐색자','충성고객','VIP'])
# 페이지뷰를 1,2~10,11~50,51~199로 구간을 설정하고 이름을 각각 '뜨내기 방문자','정보탐색자','충성고객','VIP'으로 하라.
pmg= pd.crosstab(mg['SITE_NM'], mg['방문자깊이'], values=mg['CUS_ID'], aggfunc=np.size) #행이 사이트이름이고 열이 방문자깊인이 교차테이블을 만든다.
pmg.index.name=None #pmg의 index값의 이름을 없앤다.
ppmg=pmg.div(pmg.sum(1),axis=0)  # 비율을 구하기 위해 div함수를 취한다. 
ppmg.plot(kind='barh',sharey=True,stacked=True)  # 누운 막대 그래프를 그리기 위하여 설정한다 
plt.legend(loc=3) #왼쪽 하단으로 legend 설정
plt.title('페이지뷰별 방문자 비율') #plot 의 title을 '총 페이지뷰 비교'로 설정
savefig('페이지뷰별 방문자 비율.png') #그래프 저장하기




#산업군비교


#페이지뷰
cas=ca[['ym','SITE_CNT']] #cas에 포털만화의 ym','SITE_CNT' 저장
cat=cas.groupby('ym',as_index=False).sum() #'ym'을 기준으로 groupby 시키고 페이지뷰의 합을 계산한다.
cat.columns=['ym','포털만화'] #cat의 열이름을 'ym','포털만화'로 설정한다



mus=mu[['ym','SITE_CNT']] #mus에 동영상의 ym','SITE_CNT' 저장
mut=mus.groupby('ym',as_index=False).sum() #'ym'을 기준으로 groupby 시키고 페이지뷰의 합을 계산한다.
mut.columns=['ym','동영상'] #mut의 열이름을 'ym','동영상'으로 설정한다


cm=pd.merge(mut,cat,on='ym') #cm에 mut과 cat을 'ym'을 기준으로 merge
cm.index=cm.ym  #index값을 'ym'으로 설정
cm=cm[['동영상', '포털만화']] #cm 에서 '동영상'과 '포털만화'열만 가져온다

cm.plot(kind='bar',figsize=(8,8))  #barplot을 그리고 크기를 설정한다
plt.xlabel('기간(월)') #x축의 라벨을 '기간(월)'로 설정
plt.ylabel('페이지뷰') #y축의 라벨을 '페이지뷰'로 설정
plt.title('산업군 페이지뷰 비교') #plot 의 title을 '산업군 페이지뷰 비교'로 설정
savefig('산업군 페이지뷰 비교.png') #그래프 저장하기


#평균페이지뷰
mcat=cas.groupby('ym',as_index=False).mean() #'ym'을 기준으로 포털만화의 페이지뷰의 평균을 계산한다.
mcat.columns=['ym','포털만화'] #mcat의 열이름을 'ym','포털만화'로 설정한다

mmut=mus.groupby('ym',as_index=False).mean() #'ym'을 기준으로 동영상의 페이지뷰의 평균을 계산한다.
mmut.columns=['ym','동영상'] #mmut에서 열이름을 'ym','동영상'으로 설정한다

mcm=pd.merge(mmut,mcat,on='ym') #mcm에 mmut과 mcat을 'ym'을 기준으로 merge
mcm.index=mcm.ym #index값을 'ym'으로 설정
mcm=mcm[['동영상', '포털만화']] #mcm에서 동영상,포털판화열만 가져온다.

mcm.plot(kind='bar',figsize=(8,8))  #barplot을 그리고 크기를 설정한다
plt.xlabel('기간(월)') #x축의 라벨을 '기간(월)'로 설정
plt.ylabel('페이지뷰') #y축의 라벨을 '페이지뷰'로 설정
plt.title('산업군 평균 페이지뷰 비교') #plot 의 title을 '산업군 평균 페이지뷰 비교'로 설정
savefig('산업군 평균 페이지뷰 비교.png') #그래프 저장하기



#체류시간

cad=ca[['ym','ST_TIME']] #cad에 ca의 ym','ST_TIME' 저장
cadw=cad.groupby('ym',as_index=False).sum()  #'ym'을 기준으로 groupby 시키고 체류시간의  합을 계산한다.
cadw.columns=['ym','포털만화'] #cadw에서 'ym','포털만화'column만 설정한다


mud=mu[['ym','ST_TIME']] #mud에 mu의 ym','ST_TIME' 저장
mudw=mud.groupby('ym',as_index=False).sum()  #'ym'을 기준으로 groupby 시키고 체류시간의  합을 계산한다.
mudw.columns=['ym','동영상'] #mudw에서 'ym','포털만화'column만 설정한다


cmd=pd.merge(mudw,cadw,on='ym') #cmd에 mudw과 cadw을 'ym'을 기준으로 merge
cmd.index=cmd.ym #index값을 'ym'으로 설정
cmd=cmd[['동영상', '포털만화']]  #cm 에서 '동영상'과 '포털만화'만 column으로 설정

cmd.plot(kind='bar',figsize=(8,8)) #barplot을 그리고 크기를 설정한다
plt.xlabel('기간(월)')  #x축의 라벨을 '기간(월)'로 설정
plt.ylabel('페이지뷰') #y축의 라벨을 '페이지뷰'로 설정
plt.title('산업군 페이지뷰 비교') #plot 의 title을 '산업군 페이지뷰 비교'로 설정
savefig('산업군 체류시간 비교.png') #그래프 저장하기










#방문자수


cav=pd.pivot_table(ca,values='CUS_ID',index='ym',aggfunc=np.size,fill_value=0).reset_index() #index를 ym으로 값을 고객 아이디의 size로 설정하는 피벗테이블을 생성한다
cav.columns=['ym','포털만화'] #cav 에서 '동영상'과 '포털만화'만 column으로 설정


muv=pd.pivot_table(mu,values='CUS_ID',index='ym',aggfunc=np.size,fill_value=0).reset_index()#index를 ym으로 값을 고객 아이디의 size로 설정하는 피벗테이블을 생성한다
muv.columns=['ym','동영상'] #muv 에서 '동영상'과 '포털만화'만 column으로 설정


cmv=pd.merge(muv,cav,on='ym') #cmv에 muv과 cav를 'ym'을 기준으로 merge
cmv.index=cmv.ym #index값을 'ym'으로 설정
cmv=cmv[['동영상', '포털만화']] #cmv 에서 '동영상'과 '포털만화'만 column으로 설정


cmv.plot(kind='bar',figsize=(8,8)) #barplot을 그리고 크기를 설정한다
plt.xlabel('기간(월)')  #x축의 라벨을 '기간(월)'로 설정
plt.ylabel('방문자수') #y축의 라벨을 '페이지뷰'로 설정
plt.title('산업군 방문자수 비교') #plot 의 title을 '산업군 방문자수 비교'로 설정
savefig('산업군 방문자수 비교.png') #그래프 저장하기


#직업별




mp=pd.merge(mg,dp,on='CUS_ID') #mg와 dp를 CUS_ID를 기준으로 merge


mpp = pd.crosstab(mp['JOB'], mp['SITE_NM'], values=mp['CUS_ID'], aggfunc=np.size) #SITE_NM과 'JOB'을 CUS_ID값의 크기로 crosstab한다.
mpp.index.name = None #mpp의 index값 이름을 없앤다.

mpp[[0]].plot(kind='barh',sharey=True,color='y',figsize=(8,8)) # 데일리 모션의 누운 막대 그래프를 그리기 위하여 설정하고 색깔을 노란색으로 지정한다.
plt.title('직업별 Dailymotion 방문자수')  #plot 의 title을 '직업별 Dailymotion 방문자수'로 설정
savefig('직업별 데일 방문자수.png') #그래프 저장하기


mpp[[1]].plot(kind='barh',sharey=True,color='r',figsize=(8,8)) # 유투브의 누운 막대 그래프를 그리기 위하여 설정하고 색깔을 빨강색으로 지정한다.
plt.title('직업별 YouTube 방문자수') #plot 의 title을 '직업별 YouTube 방문자수'로 설정
savefig('직업별 유툽 방문자수.png') #그래프 저장하기


mpp[[2]].plot(kind='barh',sharey=True,color='g',figsize=(8,8)) # 비메오의 누운 막대 그래프를 그리기 위하여 설정하고 색깔을 녹색으로 지정한다.
plt.title('직업별 비메오 방문자수') #plot 의 title을 '직업별 비메오 방문자수'로 설정
savefig('직업별 비메오 방문자수.png') #그래프 저장하기


#daycov(팀 프로젝트 1결과 이용)


dc= pd.read_table('Data2_Clickstreams.tab', sep='\t', encoding='mbcs') # Data2_Clickstreams.tab파일을 읽어서 dc라는 변수에 저장한다.(encoding='mbcs'는 한글 파일을 읽기 위해서 쓴다.)
dc['ym']=dc.TIME_ID.astype(str).str[:8]#dc의 ym이라는 새로운 열에 연월일값을 저장한다., 
dayc=pd.pivot_table(dc,values='ST_TIME',index='CUS_ID',columns='ym',aggfunc=sum,fill_value=0).reset_index() #index를 고객아이디로 열을 기간으로 하고, 값이 체류시간의 합인 피벗 테이블을 생성하여 dayc에 생성한다.
dayc['DAYCOV']= dayc.ix[:,1:].std(axis=1)/dayc.ix[:,1:].mean(axis=1) #행별로 표준편차를 평균으로 나눠서 DAYCOV에 저장한다.
dayc1=dayc[['CUS_ID','DAYCOV']] #dayc에 CUS_ID와 DAYCOV 데이터 프레임만 따로 분류 
dayc1.columns.name=None  #dayc1의 열의 이름을 없앤다.




dmg=pd.merge(mg,dayc1,on='CUS_ID')  #mg와 dayc1을 CUS_ID를 기준으로 merge하여 dmg로 저장
ddmg=pd.pivot_table(dmg,values='DAYCOV',index='SITE_NM',aggfunc=mean).reset_index() #index를 사이트 이름을 index로 하고 값이 DAYCOV의 평균인 피벗 테이블을 생성하여 ddmg에 생성한다.
ddmg.index=ddmg.SITE_NM #ddmg의 index값을 사이트 이름으로 설정
ddmg.index.name=None #ddmg의 index이름을 없앤다
ddmg=ddmg[['DAYCOV']] #ddmg에서 DAYCOV만 사용하여 그래프를 그리기 위하여 따로 분류한다.


colors=['y','r','g'] #colors에 색깔을 노란색 빨강색, 녹색으로 설정하여 위에 누운막대 그래프에 넣기 위해 지정한다.
ddmg.plot(kind='barh',legend=False,color=colors) # 누운 막대 그래프를 그리기 위하여 설정하고 색깔을 지정한 colors으로 설정한다.
plt.title('사이트별 일일 변동계수') #plot 의 title을 '사이트별 일일 변동계수'로 설정
savefig('사이트별 일일 변동계수.png') #그래프 저장하기



#산업군


amu=pd.pivot_table(mu,values='CUS_ID',index='SITE_NM',aggfunc=np.size,fill_value=0).reset_index().sort_index(by='CUS_ID', ascending=False).head()#방문자수 기준으로 상위5개 뽑기
aamu=pd.concat([mu[mu.SITE_NM=='YouTube'],mu[mu.SITE_NM=='아프리카TV'],mu[mu.SITE_NM=='판도라TV'],mu[mu.SITE_NM=='pooq'],mu[mu.SITE_NM=='엠군']])#상위5개 동영상 사이트를 각각뽑은뒤 행bind

arm=aamu[['ym','SITE_CNT','ST_TIME']] #뽑은 데이터프레임에서 연월,페이지뷰,체류시간만 가져오기
armm=arm.groupby('ym',as_index=False).mean() #연월 기준 페이지뷰,체류시간의 평균
aam=pd.Series(armm.SITE_CNT)  #armm의 페이지뷰를 시리즈로 만들기
aam.index=armm.ym #aam시리즈의 index를 연월로 바꾸기


aam.plot(color='b',label='상위 5개') #amm데이터프레임 plot,색깔은 파란색,라벨은 상위5개로
bbp.plot(color='g',label='비메오')   #bbp데이터프레임 plot,색깔은 녹색,라벨은 비메오로
plt.xlabel('기간(월)') #x축 이름설정
plt.ylabel('페이지뷰')  #y축 이름설정
plt.legend(loc=9) #범례를 그래프 중앙 윗쪽에
plt.title('산업군 평균 페이지뷰 비교')#그래프 이름설정
savefig('산업군 평균 페이지뷰.png') #그래프 저장






