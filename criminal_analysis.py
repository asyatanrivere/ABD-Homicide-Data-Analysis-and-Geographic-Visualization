import pandas as pd

df=pd.read_csv("homicide-data.csv", encoding="latin-1")

print(df.head(10))
"""
          uid  reported_date   victim_last victim_first victim_race victim_age victim_sex         city state        lat         lon            disposition
0  Alb-000001       20100504        GARCIA         JUAN    Hispanic         78       Male  Albuquerque    NM  35.095788 -106.538555  Closed without arrest
1  Alb-000002       20100216       MONTOYA      CAMERON    Hispanic         17       Male  Albuquerque    NM  35.056810 -106.715321       Closed by arrest
2  Alb-000003       20100601   SATTERFIELD      VIVIANA       White         15     Female  Albuquerque    NM  35.086092 -106.695568  Closed without arrest
3  Alb-000004       20100101      MENDIOLA       CARLOS    Hispanic         32       Male  Albuquerque    NM  35.078493 -106.556094       Closed by arrest
4  Alb-000005       20100102          MULA       VIVIAN       White         72     Female  Albuquerque    NM  35.130357 -106.580986  Closed without arrest
5  Alb-000006       20100126          BOOK    GERALDINE       White         91     Female  Albuquerque    NM  35.151110 -106.537797         Open/No arrest
6  Alb-000007       20100127     MALDONADO        DAVID    Hispanic         52       Male  Albuquerque    NM  35.111785 -106.712614       Closed by arrest
7  Alb-000008       20100127     MALDONADO       CONNIE    Hispanic         52     Female  Albuquerque    NM  35.111785 -106.712614       Closed by arrest
8  Alb-000009       20100130  MARTIN-LEYVA      GUSTAVO       White         56       Male  Albuquerque    NM  35.075380 -106.553458         Open/No arrest
9  Alb-000010       20100210       HERRERA       ISRAEL    Hispanic         43       Male  Albuquerque    NM  35.065930 -106.572288         Open/No arrest
"""
print(df.describe())
"""
       reported_date           lat           lon
count   5.217900e+04  52119.000000  52119.000000
mean    2.013090e+07     37.026786    -91.471094
std     1.123420e+06      4.348647     13.746378
min     2.007010e+07     25.725214   -122.507779
25%     2.010032e+07     33.765203    -95.997198
50%     2.012122e+07     38.524973    -87.710286
75%     2.015091e+07     40.027627    -81.755909
max     2.015111e+08     45.051190    -71.011519"""
print("--------------------------------")
print(df.info())
"""
<class 'pandas.DataFrame'>
RangeIndex: 52179 entries, 0 to 52178
Data columns (total 12 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   uid            52179 non-null  str    
 1   reported_date  52179 non-null  int64     --> there is a null value
 2   victim_last    52178 non-null  str    
 3   victim_first   52179 non-null  str    
 4   victim_race    52179 non-null  str    
 5   victim_age     52179 non-null  str    
 6   victim_sex     52179 non-null  str    
 7   city           52179 non-null  str    
 8   state          52179 non-null  str    
 9   lat            52119 non-null  float64
 10  lon            52119 non-null  float64
 11  disposition    52179 non-null  str    
dtypes: float64(2), int64(1), str(9)
memory usage: 4.8 MB
None"""
print("--------------------------------")

df.duplicated().sum() # 0 --> no repeated rows
print(df.isnull().sum())
"""
uid               0
reported_date     0
victim_last       1
victim_first      0
victim_race       0
victim_age        0
victim_sex        0
city              0
state             0
lat              60
lon              60
disposition       0
dtype: int64
"""
print(df.columns)
"""
Index(['uid', 'reported_date', 'victim_last', 'victim_first', 'victim_race',
       'victim_age', 'victim_sex', 'city', 'state', 'lat', 'lon',
       'disposition'],
      dtype='str')
      """
df.dropna(subset=["victim_last","lat","lon"],inplace=True)
# now, there is no a row with null entry
print(df.dtypes)
"""
uid                  str
reported_date      int64
victim_last          str
victim_first         str
victim_race          str
victim_age           str      --> has to be int
victim_sex           str
city                 str
state                str
lat              float64
lon              float64
disposition          str
dtype: object"""

df["victim_age"]=pd.to_numeric(df["victim_age"],errors="coerce")
print(df["victim_age"].isnull().sum()) # 2997
df.dropna(subset=["victim_age"],inplace=True)
df["victim_age"]=df["victim_age"].astype(int)
df["reported_date"] = pd.to_datetime(df["reported_date"], format="%Y%m%d")

df["victim_last"]=df["victim_last"].str.title().str.strip()
df["victim_first"]=df["victim_first"].str.title().str.strip()
df["victim_race"]=df["victim_race"].str.title().str.strip()

df["victim_old"] = "Adult"  # default
df.loc[df["victim_age"] > 65, "victim_old"] = "Old"
df.loc[df["victim_age"] < 18, "victim_old"] = "Child"

df = df[df["victim_sex"].str.strip().str.lower() != "unknown"]
df = df[df["victim_race"].str.strip().str.lower() != "unknown"]

print(df.head(10))
df.dropna(subset="victim_sex",inplace=True)
print(f"Mean of victim's age: {df["victim_age"].mean()}")
# Mean of victim's age: 31.801368050324708

print(df["disposition"].value_counts())
"""
Closed by arrest         24136
Open/No arrest           22285
Closed without arrest     2700"""

print(df["victim_sex"].value_counts())
"""
victim_sex
Male      40402
Female     7097"""
print(df["victim_race"].value_counts())
"""
victim_race
Black       33062
Hispanic     6817
White        6258
Asian         676
Other         664
Name: count, dtype: int64"""
print(df["victim_old"].value_counts())
"""
victim_old
Adult    42292
Child     3916
Old       1269
Name: count, dtype: int64"""
print(df["city"].value_counts().sort_values())
"""
Name: count, dtype: int64
city
Tampa              198
Savannah           230
San Bernardino     274
Durham             276
Albuquerque        284
Denver             312
Richmond           316
Minneapolis        364
Sacramento         370
Long Beach         378
Omaha              402
Baton Rouge        423
Stockton           439
San Diego          450
Miami              462
Fresno             480
Buffalo            510
Fort Worth         549
Louisville         572
Tulsa              573
Boston             605
New York           622
Pittsburgh         628
Oklahoma City      653
Charlotte          661
San Francisco      663
Cincinnati         691
Nashville          755
Birmingham         785
San Antonio        825
Oakland            945
Atlanta            968
Columbus          1069
Milwaukee         1115
Jacksonville      1151
Las Vegas         1299
Washington        1308
Indianapolis      1321
New Orleans       1394
Memphis           1510
St. Louis         1661
Los Angeles       2196
Detroit           2496
Baltimore         2827
Houston           2908
Philadelphia      3036
Chicago           5523
Name: count, dtype: int64"""
print(df.groupby("city")["state"].value_counts().sort_values())
"""
city            state
Tulsa           AL          1
Tampa           FL        198
Savannah        GA        230
San Bernardino  CA        274
Durham          NC        276
Albuquerque     NM        284
Denver          CO        312
Richmond        VA        316
Minneapolis     MN        364
Sacramento      CA        370
Long Beach      CA        378
Omaha           NE        402
Baton Rouge     LA        423
Stockton        CA        439
San Diego       CA        450
Miami           FL        462
Fresno          CA        480
Buffalo         NY        510
Fort Worth      TX        549
Louisville      KY        572
Tulsa           OK        572
Boston          MA        605
New York        NY        622
Pittsburgh      PA        628
Oklahoma City   OK        653
Charlotte       NC        661
San Francisco   CA        663
Cincinnati      OH        691
Nashville       TN        755
Birmingham      AL        785
San Antonio     TX        825
Oakland         CA        945
Atlanta         GA        968
Columbus        OH       1069
Milwaukee       wI       1115
Jacksonville    FL       1151
Las Vegas       NV       1299
Washington      DC       1308
Indianapolis    IN       1321
New Orleans     LA       1394
Memphis         TN       1510
St. Louis       MO       1661
Los Angeles     CA       2196
Detroit         MI       2496
Baltimore       MD       2827
Houston         TX       2908
Philadelphia    PA       3036
Chicago         IL       5523
Name: count, dtype: int64"""
print(df.groupby("victim_race")["disposition"].value_counts().sort_values())
"""
victim_race  disposition          
Other        Closed without arrest       29
Asian        Closed without arrest       71
             Open/No arrest             201
Other        Open/No arrest             288
             Closed by arrest           347
Hispanic     Closed without arrest      397
Asian        Closed by arrest           404
White        Closed without arrest      598
Black        Closed without arrest     1480
White        Open/No arrest            1747
Hispanic     Open/No arrest            3140
             Closed by arrest          3280
White        Closed by arrest          3913
Black        Closed by arrest         15275
             Open/No arrest           16307
Name: count, dtype: int64"""

print(f"The age of the oldest victim: {df["victim_age"].max()}")
print(f"The age of the youngest victim: {df["victim_age"].min()}")

print(f"Mean of lat: {df["lat"].mean()}")
print(f"Mean of lon: {df["lon"].mean()}")

print(df.groupby("victim_race")["victim_old"].value_counts())
"""
victim_race  victim_old
Asian        Adult           562
             Child            63
             Old              51
Black        Adult         29808
             Child          2714
             Old             540
Hispanic     Adult          6001
             Child           703
             Old             113
Other        Adult           582
             Child            56
             Old              26
White        Adult          5339
             Old             539
             Child           380
Name: count, dtype: int64"""

#------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sb

race=df["victim_race"].value_counts()
plt.figure(figsize=(10,5))

sb.barplot(x=race.index,y=race.values)
plt.xlabel("Victim Race")
plt.ylabel("Number of Homicides")
plt.title("Distribution of Homicides by Race")

plt.savefig("images/homicides_by_race.png")
plt.show()

#------------------------------------------

victimsex=df["victim_sex"].value_counts()
plt.figure(figsize=(5,5))

sb.barplot(x=victimsex.index,y=victimsex.values)
plt.xlabel("Victim Sex")
plt.ylabel("Number of Homicides")
plt.title("Distribution of Homicides by Sex")

plt.savefig("images/homicides_by_sex.png")
plt.show()

#------------------------------------------

disposition=df["disposition"].value_counts()
plt.figure(figsize=(8,5))

sb.barplot(x=disposition.index,y=disposition.values)
plt.xlabel("Disposition")
plt.ylabel("Number of Homicides")
plt.title("Distribution of Disposition")

plt.savefig("images/homicides_by_disposition.png")
plt.show()

#------------------------------------------

age=df["victim_age"].value_counts()
plt.figure(figsize=(8,5))

sb.lineplot(x=age.index,y=age.values)
plt.xlabel("Age")
plt.ylabel("Number of Homicides")
plt.title("Distribution of Age")

plt.savefig("images/homicides_by_age.png")
plt.show()

#----------------------------------------------

df["reported_year"] = df["reported_date"].dt.year

yearly=df["reported_year"].value_counts()
plt.figure(figsize=(8,5))

sb.barplot(x=yearly.index,y=yearly.values)
plt.xlabel("Years")
plt.ylabel("Number of Homicides")
plt.title("Distribution of Year")

plt.savefig("images/homicides_by_year.png")
plt.show()

#---------------------------------------

city=df["city"].value_counts()
plt.figure(figsize=(10,15))

sb.barplot(y=city.index,x=city.values)
plt.ylabel("Cities")
plt.xlabel("Number of Homicides")
plt.title("Distribution of City")

plt.savefig("images/homicides_by_city.png")
plt.show()

#---------------------------------------

locations=pd.DataFrame(df,columns=["lat","lon"])
locations.to_csv("location.csv",index=False)
# we'll use that csv to point the locations on map
#---------------------------------------
racedis=df.groupby("victim_race")["disposition"].value_counts().reset_index(name="count")
sb.barplot(data=racedis,x="victim_race",y="count",hue="disposition")
plt.title("Disposition by Victim Race")
plt.xlabel("Victim Races")
plt.tight_layout()
plt.savefig("images/race_vs_disposition.png")
plt.show()
#---------------------------------------
agevssex = df.groupby("victim_age")["victim_sex"].value_counts().reset_index(name="count")
plt.figure(figsize=(12,6))
sb.lineplot(data=agevssex,x="victim_age",y="count",hue="victim_sex")
plt.title("Victim Age Distribution by Sex")
plt.xlabel("Victim Age")
plt.ylabel("Number of Victims")
plt.tight_layout()
plt.savefig("images/age_vs_sex.png")
plt.show()
