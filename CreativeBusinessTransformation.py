from imports import *
from statsForAward import *
from queries import queryCBT

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=iafsql;'
                      'Database=IAFF;'
                      'Trusted_Connection=yes;')

dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")
df = pd.read_sql(queryCBT, conn)

#getting the dataframe

dfshort = df[df["Shortlist"] ==1]
listOfGroups = dfshort[["taggroupgroupname", "TagGroupName", "tagname"]].drop_duplicates()#removing different entries
listOfGroups[["taggroupgroupname", "TagGroupName","tagname"]].nunique() #finding number of uniques

len(listOfGroups)

#this proves that each tagname is unique
#creating the series
list_of_tags = df.sort_values("All Entries").groupby("All Entries")["tagname"].apply(list)
list_of_entries = pd.Series(df.sort_values("All Entries")["All Entries"].dropna().unique().tolist())
list_of_group_tags = df.sort_values("All Entries").groupby("All Entries")["TagGroupName"].apply(list)

#creating the dataframe for proving the uniqueness of tags
dfclear = removeTags(df)
dfclear["listOfTags"]  = list_of_tags
dfclear["listOfGroupTags"]  = list_of_group_tags

writingFileFinal = pd.ExcelWriter("CBTTags{}.xlsx".format(dateTime), engine='xlsxwriter')

#Creating the final dataframe
final = createStatsCBTDf(df,dfclear, writingFileFinal)

writingFileFinal.save()


#number of tags importance?
tagsNumberpercentage =(dfshort[dfshort["Winner"].notnull()].groupby("All Entries")["tagname"].count().value_counts().sort_index()/ \
    dfshort.groupby("All Entries")["tagname"].count().value_counts().sort_index()).fillna(0).reset_index()
spearmanRcor = scipy.stats.spearmanr(tagsNumberpercentage["index"], tagsNumberpercentage["tagname"])
tagsNumberpercentage["tagname"].plot.bar()

hotdummystuff = pd.get_dummies( df["tagname"],prefix='TagName_')
linearRegressionModel = LinearRegression()
#linearRegressionModel.fit(hotdummystuff, df["Winner"])

#final shit before turning tags into a list!

dfshort.groupby("tagname").size().sort_values(ascending = False).head(20) #20 most common tags

df[df["Winner"].notnull()].groupby("tagname").size().sort_values(ascending = False).head(20) #20 most common éé

skatoulakia = df[df["Shortlist"]==1].groupby("tagname").size()  /  df.groupby("tagname").size()
print(skatoulakia.sort_values(ascending = False).head(20))

###Normalising the dataframe:
#columns we want to group
listOfTagColumns = ["tagname", "TagGroupName","taggroupgroupname"]
finalDf = pd.DataFrame()
for column in listOfTagColumns:
    finalDf[column]= df.groupby("All Entries")[column].apply(list)
    df = df.drop(column, axis =1)

df = df.drop_duplicates()
df = df.set_index("All Entries")
for column in finalDf:
    df[column] = finalDf[column]

df["Category"] = df["Cat Code"].astype(str).str[0]

df = df.reset_index()
####


#
#getting the graphs and excels:
#
#input for Award
dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")

writingFile = pd.ExcelWriter("CBT{}.xlsx".format(dateTime), engine='xlsxwriter')


listOfColumns = ["RegionName", "sector_name", "sub_sector_name", "Country", "coTown",
                 ["Category","MediaDescription"], "CompanyType",["Cat Code","Category Description"]]

for column in listOfColumns:
    allStatsForColumn(df, column, writingFile, True)

writingFile.save()
#writingFile.close()
#shortlisted stats



