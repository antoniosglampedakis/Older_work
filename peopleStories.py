from imports import *


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DVLN2DDBS01\EC;'
                      'Database=IAFF;'
                      'Trusted_Connection=yes;')
query = '''SELECT ec.FestivalYear, ec.Name as CreditName, EC.Company, ec.CreditsId,
	ed.AwardCountCode, ed.Short, ed.CategoryCode, ed.CategorySubTypeID, ED.Advertiser,ED.EntryTypeName, ED.FestivalCode,
	cd.coTown,	cd.Country, cd.RegionName,  cd.companyNo



 FROM ArchiveEntryCredits EC
	inner join ArchiveEntryData ed
	on ed.FestivalYear = ec.FestivalYear and
	ed.FestivalCode = ec.FestivalCode and
	ed.EntryId = ec.EntryId
 	left join ArchiveEntryCategories as ECat
		ON ECat.FestivalCode = ed.FestivalCode COLLATE Latin1_General_CI_AI
		AND ECat.FestivalYear = ed.FestivalYear
		AND ECat.CategoryCode = ed.CategoryCode COLLATE Latin1_General_CI_AI
		AND ECat.EntryTypeId = ed.EntryTypeId

	left Join [ArchiveCompanyData] as CD
		on ED.EntrantCompanyNo = CD.companyNo 
		AND ed.Festivalyear = cd.ArchiveYear

	where ed.FestivalCode = 'eb'
 '''
df = pd.read_sql(query, conn)
#eurobest 2020
year = 2020
uniqueAwards =df.groupby("AwardCountCode")["AwardCountCode"].unique().index.values.tolist()
uniqueAwards.append("All")

#I want to find the first time awards in 2020.
#this means: from people who had an award in 2020
#not having an award in other years.
#this means the number of occurances for this award in previous years is 0

firstTimers = df[(df["FestivalYear"] == 2020 & df["AwardCountCode"]) & ()].drop_duplicates(["CreditName", "AwardCountCode"])