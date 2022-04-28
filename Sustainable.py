from imports import *
from statsForAward import *
from queries import sustainabilityQuery

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DVLN2DDBS01\EC;'
                      'Database=IAFF;'
                      'Trusted_Connection=yes;')


dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")

df = pd.read_sql(sustainabilityQuery, conn)
df["FestivalYear"] = df["FestivalYear"].replace(2020, 2021)
df["FestivalYear"] = df["FestivalYear"].replace(2021, '2021/2021')
dfSust = df[(df["Shortlist"] == 1) & (df["tagname"].astype(str) == "Sustainability")]
dfAll = df[df["Shortlist"] ==1].drop(["tagname", "TagGroupName","taggroupgroupname"], axis = 1).drop_duplicates()
dfSust  = dfSust.rename(columns ={"All Entries":"Sustainability Entries","Winner":"Sustainablility Winner"})


df.groupby("FestivalYear")["All Entries"].count()




writingFile = pd.ExcelWriter("sustainable{}.xlsx".format(dateTime), engine='xlsxwriter')


SustEntries = dfSust.groupby(["FestivalYear"])["Sustainability Entries"].count()
AllEntries =dfAll.groupby(["FestivalYear"])["All Entries"].count()

SustWinners = dfSust[dfSust["Sustainablility Winner"].notnull()].groupby(["FestivalYear"])["Sustainability Entries"].count()
AllWinners =dfAll[dfAll["Winner"].notnull()].groupby(["FestivalYear"])["All Entries"].count()
listOfDfs = [SustEntries,AllEntries,SustWinners,AllWinners]
allDfs = pd.DataFrame(listOfDfs)

allDfs.to_excel(writingFile,sheet_name= "Totals Per Year")

listOfColumns = ["RegionName", "sector_name", "sub_sector_name", "Country", "coTown",]


for column in listOfColumns:
    allStatsForSustainability(dfSust, dfAll, column, writingFile)

writingFile.save()



#\\\\
#
# df.groupby(["FestivalYear","Country"])["All Entries"].size().groupby("FestivalYear").size() \
#     .to_excel(writingFile, sheet_name="Entries per country Per Year")
# df[df['Winner'].notnull()].groupby(["FestivalYear","Country"])["All Entries"].size().groupby("FestivalYear").size() \
#     .to_excel(writingFile, sheet_name="Winners per country Per Year")
#
# df.groupby(["FestivalYear","sub_sector_name"])["All Entries"].size().groupby("FestivalYear").size()\
#     .to_excel(writingFile,sheet_name="Entries per sub sector Per Year")
# df[df['Winner'].notnull()].groupby(["FestivalYear","sub_sector_name"])["All Entries"].size().groupby("FestivalYear").size()\
#     .to_excel(writingFile,sheet_name="Winners per sub sector Per Year")
#
#
# df.groupby(["FestivalYear"])["All Entries"].count().to_excel(writingFile,sheet_name="Total Entries Per Year")
# df.groupby(["FestivalYear"])["Winner"].count().to_excel(writingFile,sheet_name="Total Winners Per Year")





