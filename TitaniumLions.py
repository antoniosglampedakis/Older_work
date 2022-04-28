from imports import *
from statsForAward import *
from queries import titaniumQuery

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DVLN2DDBS01\EC;'
                      'Database=IAFF;'
                      'Trusted_Connection=yes;')




df = pd.read_sql(titaniumQuery, conn)

dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")

writingFile = pd.ExcelWriter("Titanium{}.xlsx".format(dateTime), engine='xlsxwriter')

listOfColumns = ["RegionName", "sector_name", "sub_sector_name", "Country", "coTown",
                 "MediaDescription", "CompanyType","Category Description"
                ,"Advertiser", "Product"]


for column in listOfColumns:
    allStatsForColumnByYear (df,column, writingFile, True)



writingFile.save()

#
# awardsByRegion = df.groupby("RegionName")["AwardCountCode"].count().sort_values(ascending= False)
#
# awardsBySector = df.groupby("sector_name")["AwardCountCode"].count().sort_values(ascending= False)
#
# awardsBySubsector =  df.groupby("sub_sector_name")["AwardCountCode"].count().sort_values(ascending = False)
#
# awardsByCountry = df.groupby("Country")["AwardCountCode"].count().sort_values(ascending = False)
#
#
# #WRONG, some companies have the town in their name, not in the cotown
# awardsByTown = df.groupby("coTown")["AwardCountCode"].count().sort_values(ascending = False).head(20)
#
# awardsByFestivalYear = df.groupby("FestivalYear")["Advertiser"].count().sort_values(ascending = False).head(20)
#
# awardsByCategoryDescription = df.groupby("CategoryDescription")["AwardCountCode"].count().sort_values(ascending = False).head(20)
# participantsByCategoryDescription = df.groupby("CategoryDescription")["Advertiser"].count().sort_values(ascending = False).head(20)
#

categoryPercentage = df.groupby("CategoryDescription")["AwardCountCode"].count().sort_values(ascending = False).head(20) / \
 df.groupby("CategoryDescription")["Advertiser"].count().sort_values(ascending = False).head(20)