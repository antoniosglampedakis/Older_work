from imports import *

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DVLN2DDBS01\EC;'
                      'Database=IAFF;'
                      'Trusted_Connection=yes;')

# years = [2017, 2018, 2019]
# short = [1, 'any']
# prize = ['is nut null', 'any']

query2 = """SELECT ED.FestivalYear, ED.Advertiser, ED.short, ED.FestivalCode,ED.EntryTypeName,
	ED.AwardCountCode, ED.PrizeCode, ED.CategoryCode,  ed.CategorySubTypeID, ed.Cancelled,
	cd.CompanyName, CD.NetworkCode, cd.NetworkName, CD.UltimateHoldingCompanyName, cd.GroupCompanyName, cd.Country, cd.GroupCompanyName, cd.coTown,
	ec.MediaDescription, ec.CategoryDescription 
	FROM PublishedArchiveEntryData as ED
	inner Join [ArchiveCompanyData] as CD
	on ED.EntrantCompanyNo = CD.companyNo and ed.Festivalyear = cd.ArchiveYear
	inner join ArchiveEntryCategories as EC
	ON ec.FestivalCode = ed.FestivalCode COLLATE Latin1_General_CI_AI
	AND ec.FestivalYear = ed.FestivalYear
	AND ec.CategoryCode = ed.CategoryCode COLLATE Latin1_General_CI_AI
	AND ec.EntryTypeId = ed.EntryTypeId

        where ed.FestivalYear in (2017,2018,2019)
	and ed.FESTIVALCODE IN ('CL', 'LE', 'LI', 'LH')
	and CD.NetworkName like '%TBWA WORLDWIDE%'
--	and ed.AwardCountCode is not null"""
df = pd.read_sql(query2, conn)

#creative council process:
#get the data