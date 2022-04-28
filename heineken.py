from imports import *
from statsForAward import *
from queries import heinekenQuery

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DVLN2DDBS01\EC;'
                      'Database=IAFF;'
                      'Trusted_Connection=yes;')


df = pd.read_sql(heinekenQuery, conn)
df["Category"] = df["Cat Code"].astype(str).str[0]


#% Heineken awards per region vs. awards in all categories since 2011
#awards per region
df.groupby("RegionName")["Winner"].count()/df.groupby("RegionName")["EntryTypeName"].count()


dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")

writingFile = pd.ExcelWriter("heineken{}.xlsx".format(dateTime), engine='xlsxwriter')

writingFilePerYear = pd.ExcelWriter("heinekenperYear{}.xlsx".format(dateTime), engine='xlsxwriter')
AllEntries =df.groupby(["FestivalYear"])["All Entries"].count()
AllWinners =df[df["Winner"].notnull()].groupby(["FestivalYear"])["Winner"].count()

AllShortlist =df[df["Shortlist"] ==1 ].groupby(["FestivalYear"])["Shortlist"].count()
listofdfs = [AllEntries,AllWinners,AllShortlist]
allDfs = pd.DataFrame(listofdfs)
allDfs.to_excel(writingFile,sheet_name= "Totals Per Year")

listOfColumns = ["RegionName", "sector_name", "sub_sector_name", "Country", "coTown",
                 ["Category","MediaDescription"], "CompanyType",["Cat Code","Category Description"]
                ,"Advertiser", "Product","Title","CompanyName","NetworkName",
                 "UltimateHoldingCompanyName","GroupCompanyName" , "Winner"]

listOfColumnsPerYear = ["RegionName", "sector_name", "sub_sector_name", "Country", "coTown",
                 "MediaDescription","Category", "CompanyType","Category Description"
                ,"Advertiser", "Product", "Title", "CompanyName","NetworkName",
                        "UltimateHoldingCompanyName","GroupCompanyName", "Winner"]

#
# for column in listOfColumns:
#     allStatsForColumn(df, column, writingFile)

for column in listOfColumnsPerYear:
    allStatsForColumbGroupedByYear(df,column,writingFilePerYear, True)
    allStatsForColumn(df, column, writingFile,True)

writingFile.save()
writingFilePerYear.save()