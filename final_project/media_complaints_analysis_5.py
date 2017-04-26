import psycopg2
import datetime

conn = psycopg2.connect(database="projectdatabase", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

now=datetime.datetime.now()


a="create table "
b="complaints_media_analysis_"
c=str(now.year)+now.strftime('%m')
c1 =str(now.year)
d=" as SELECT c.year_month, c.cleaned_company, c.complaints_count, sum(m.numsources) as mentions, avg (avgtone) as sentiment FROM ccdata_y"
d1="_update c join mediadata_"
d2="_update m on c.year_month = m.monthyear WHERE (m.sourceurl like  lower('%'||c.cleaned_company||'%') AND c.year_month = '"
e="') GROUP BY c.year_month, c.cleaned_company, c.complaints_count order by c.complaints_count DESC"
f="drop table if exists "

#Load 201601-201704 as base data
cur.execute(a+b+"201601"+d+"2016"+d1+"2016"+d2+"201601"+e)
cur.execute(a+b+"201602"+d+"2016"+d1+"2016"+d2+"201602"+e)
cur.execute(a+b+"201603"+d+"2016"+d1+"2016"+d2+"201603"+e)
cur.execute(a+b+"201604"+d+"2016"+d1+"2016"+d2+"201604"+e)
cur.execute(a+b+"201605"+d+"2016"+d1+"2016"+d2+"201605"+e)
cur.execute(a+b+"201606"+d+"2016"+d1+"2016"+d2+"201606"+e)
cur.execute(a+b+"201607"+d+"2016"+d1+"2016"+d2+"201607"+e)
cur.execute(a+b+"201608"+d+"2016"+d1+"2016"+d2+"201608"+e)
cur.execute(a+b+"201609"+d+"2016"+d1+"2016"+d2+"201609"+e)
cur.execute(a+b+"201610"+d+"2016"+d1+"2016"+d2+"201610"+e)
cur.execute(a+b+"201611"+d+"2016"+d1+"2016"+d2+"201611"+e)
cur.execute(a+b+"201612"+d+"2016"+d1+"2016"+d2+"201612"+e)
cur.execute(a+b+"201701"+d+"2017"+d1+"2017"+d2+"201701"+e)
cur.execute(a+b+"201702"+d+"2017"+d1+"2017"+d2+"201702"+e)
cur.execute(a+b+"201703"+d+"2017"+d1+"2017"+d2+"201703"+e)
cur.execute(a+b+"201704"+d+"2017"+d1+"2017"+d2+"201704"+e)
cur.execute("create table complaints_media_analysis_Combined as select * from (select * from complaints_media_analysis_201704 union select * from complaints_media_analysis_201703 union select * from complaints_media_analysis_201702 union select * from complaints_media_analysis_201701 union select * from complaints_media_analysis_201612 union select * from complaints_media_analysis_201611 union select * from complaints_media_analysis_201610 union select * from complaints_media_analysis_201609 union select * from complaints_media_analysis_201608 union select * from complaints_media_analysis_201607 union select * from complaints_media_analysis_201606 union select * from complaints_media_analysis_201605 union select * from complaints_media_analysis_201604 union select * from complaints_media_analysis_201603 union select * from complaints_media_analysis_201602 union select * from complaints_media_analysis_201601) u order by u.year_month")

#Load monthly data starting 201705
cur.execute(f+b+c)
cur.execute(a+b+c+d+c1+d1+c1+d2+c+e)
cur.execute("alter table complaints_media_analysis_Combined Rename to temp")
cur.execute("create table complaints_media_analysis_Combined as select * from (select * from complaints_media_analysis_201704 union select * from temp) u order by u.year_month")  
cur.execute("drop table if exists temp")

conn.commit()
cur.close()
conn.close()
