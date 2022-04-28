#file with all queries. instead of having them in their own file, just adding them here, and importing the relevant query in the relevant file.


queryCBT = '''select ec.FestivalYear,  ec.FestivalCode, ec.EntryTypeName, ec.MediaDescription, ec.CategoryDescription as "Category Description",
ED.Advertiser, ED.short as Shortlist, ed.EntryId as "All Entries", ed.product, ed.title,
ED.AwardCountCode as Winner, ED.PrizeCode, ED.CategoryCode as "Cat Code",  ed.CategorySubTypeID, ed.CatalogueNo,
cd.CompanyName, CD.NetworkCode, cd.NetworkName, CD.UltimateHoldingCompanyName,  
cd.Country, cd.GroupCompanyName, cd.coTown, cd.CompanyType, cd.RegionName,

sec.Sector_Name sector_name,
subSec.Sector_Name sub_sector_name,

tgg.Name as taggroupgroupname,
tg.Name TagGroupName,
t.Name tagname

from PublishedArchiveEntryData pED

inner Join ArchiveCompanyData as CD
	on pED.EntrantCompanyNo = CD.companyNo 
	and ped.Festivalyear = cd.ArchiveYear

inner join ArchiveEntryData ed
	on ed.EntryId = ped.entryid
	and ed.FestivalYear = ped.FestivalYear
	and ed.FestivalCode = ped.FestivalCode  COLLATE Latin1_General_CI_AI

left join ArchiveEntryCategories ec

	ON ec.FestivalCode = ped.FestivalCode COLLATE Latin1_General_CI_AI
	AND ec.FestivalYear = ped.FestivalYear
	AND ec.CategoryCode = ped.CategoryCode COLLATE Latin1_General_CI_AI
	AND ec.EntryTypeId = ped.EntryTypeId

left JOIN IAFF.DBO.ArchiveCampaignTags et 
	ON ped.FestivalYear = et.FestivalYear
	AND ped.FestivalCode = et.FestivalCode COLLATE Latin1_General_CI_AI
	AND ped.EntryId = et.EntryID

left JOIN IAFF.DBO.ArchiveTags t WITH (NOLOCK)
	ON et.TagID = t.TagId 
	AND et.FestivalCode  = t.FestivalCode 
	AND et.FestivalYear = t.FestivalYear 

left JOIN IAFF.DBO.ArchiveTagGroups tg WITH (NOLOCK)
	ON t.TagGroupID = tg.TagGroupID
	AND t.FestivalCode  = tg.FestivalCode 
	AND t.FestivalYear = tg.FestivalYear 
left join ArchiveTagGroupGroups tgg
    on tgg.TagGroupGroupID = tg.TagGroupGroupId
    and tgg.FestivalCode = tg.FestivalCode
    and tgg.FestivalYear = tg.FestivalYear

LEFT JOIN 
ArchiveEntrySector sec
	ON sec.FestivalYear = ed.FestivalYear
	AND sec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS 
	AND sec.Sector_ID = ed.sector_id
LEFT JOIN ArchiveEntrySector subSec
	ON subSec.FestivalYear = ed.FestivalYear
	AND subSec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS 
	AND subSec.Sector_ID = ed.sector_sub_id 	


where ec.EntryTypeName like '%creative bu%' 
and ec.FestivalYear in(2020,2021)
and ec.FestivalCode = 'CL'
'''

titaniumQuery = '''select 
pED.FestivalYear, pED.Advertiser, pED.short as Shortlist, PED.FestivalCode, PED.EntryTypeName, 
	PED.AwardCountCode as Winner, PED.PrizeCode, PED.CategoryCode, Ped.CategorySubTypeID, Ped.CatalogueNo, 
	ped.EntryId as "All Entries", ped.Product,ed.title,
	cd.CompanyName, CD.NetworkCode, cd.NetworkName, CD.UltimateHoldingCompanyName, cd.GroupCompanyName, 
	cd.Country, cd.GroupCompanyName, cd.coTown, cd.CompanyType, cd.RegionName,
	ec.MediaDescription, ec.CategoryDescription as "Category Description",
	sec.Sector_Name sector_name,
	subSec.Sector_Name sub_sector_name
from PublishedArchiveEntryData ped

left Join [ArchiveCompanyData] as CD
on ped.EntrantCompanyNo = CD.companyNo and ped.Festivalyear = cd.ArchiveYear


left join ArchiveEntryCategories as EC
	ON ec.FestivalCode = ped.FestivalCode COLLATE Latin1_General_CI_AI
	AND ec.FestivalYear = ped.FestivalYear
	AND ec.CategoryCode = ped.CategoryCode COLLATE Latin1_General_CI_AI
	AND ec.EntryTypeId = ped.EntryTypeId



left join ArchiveEntryData ed
	on ed.EntryId = ped.entryid
	and ed.FestivalYear = ped.FestivalYear
	and ed.FestivalCode = ped.FestivalCode  COLLATE Latin1_General_CI_AI

LEFT JOIN 
ArchiveEntrySector sec
	ON sec.FestivalYear = ed.FestivalYear
	AND sec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS 
	AND sec.Sector_ID = ed.sector_id
LEFT JOIN ArchiveEntrySector subSec
	ON subSec.FestivalYear = ed.FestivalYear
	AND subSec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS 
	AND subSec.Sector_ID = ed.sector_sub_id 	

	WHERE ED.FestivalYear >= 2017
	AND PED.EntryTypeName LIKE '%Titanium%' '''


sustainabilityQuery = '''select ec.FestivalYear,  ec.FestivalCode, ec.EntryTypeName, ec.MediaDescription, ec.CategoryDescription as "Category Description",
ED.Advertiser, ED.short as Shortlist, ed.EntryId as "All Entries", ed.Product, ed.title,
ED.AwardCountCode as Winner, ED.PrizeCode, ED.CategoryCode as "Cat Code",  ed.CategorySubTypeID, ed.CatalogueNo,
cd.CompanyName, CD.NetworkCode, cd.NetworkName, CD.UltimateHoldingCompanyName,  
cd.Country, cd.GroupCompanyName, cd.coTown, cd.CompanyType, cd.RegionName,

sec.Sector_Name sector_name,
subSec.Sector_Name sub_sector_name
,
tgg.Name as taggroupgroupname,
tg.Name TagGroupName,
t.Name tagname



from PublishedArchiveEntryData pED

inner Join ArchiveCompanyData as CD
	on pED.EntrantCompanyNo = CD.companyNo 
	and ped.Festivalyear = cd.ArchiveYear

inner join ArchiveEntryData ed
	on ed.EntryId = ped.entryid
	and ed.FestivalYear = ped.FestivalYear
	and ed.FestivalCode = ped.FestivalCode  COLLATE Latin1_General_CI_AI

left join ArchiveEntryCategories ec

	ON ec.FestivalCode = ped.FestivalCode COLLATE Latin1_General_CI_AI
	AND ec.FestivalYear = ped.FestivalYear
	AND ec.CategoryCode = ped.CategoryCode COLLATE Latin1_General_CI_AI
	AND ec.EntryTypeId = ped.EntryTypeId

left JOIN IAFF.DBO.ArchiveCampaignTags et 
	ON ped.FestivalYear = et.FestivalYear
	AND ped.FestivalCode = et.FestivalCode COLLATE Latin1_General_CI_AI
	AND ped.EntryId = et.EntryID

left JOIN IAFF.DBO.ArchiveTags t WITH (NOLOCK)
	ON et.TagID = t.TagId 
	AND et.FestivalCode  = t.FestivalCode 
	AND et.FestivalYear = t.FestivalYear 

left JOIN IAFF.DBO.ArchiveTagGroups tg WITH (NOLOCK)
	ON t.TagGroupID = tg.TagGroupID
	AND t.FestivalCode  = tg.FestivalCode 
	AND t.FestivalYear = tg.FestivalYear 
left join ArchiveTagGroupGroups tgg
    on tgg.TagGroupGroupID = tg.TagGroupGroupId
    and tgg.FestivalCode = tg.FestivalCode
    and tgg.FestivalYear = tg.FestivalYear

LEFT JOIN 
ArchiveEntrySector sec
	ON sec.FestivalYear = ed.FestivalYear
	AND sec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS 
	AND sec.Sector_ID = ed.sector_id
LEFT JOIN ArchiveEntrySector subSec
	ON subSec.FestivalYear = ed.FestivalYear
	AND subSec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS 
	AND subSec.Sector_ID = ed.sector_sub_id 	

Where
ec.FestivalYear >= 2018
and ec.FestivalCode = 'CL'
and ped.Cancelled <> 1
and ed.short = 1
'''

heinekenQuery = '''SELECT  ED.FestivalYear, ED.Advertiser, ED.short as Shortlist, ED.FestivalCode,ED.EntryTypeName, ed.Product,
	ED.AwardCountCode as Winner, ED.PrizeCode, ED.CategoryCode as "Cat Code",  ed.CategorySubTypeID, ed.CatalogueNo,
	 ed.EntryId as "All Entries",ed.Title,
	cd.CompanyName, CD.NetworkCode, cd.NetworkName, CD.UltimateHoldingCompanyName, 
	cd.Country, cd.GroupCompanyName, cd.coTown, cd.CompanyType, cd.RegionName,
	ed.sector_id, ed.sector_sub_id,
    sec.Sector_Name sector_name,
    subSec.Sector_Name sub_sector_name, 

	ec.MediaDescription, ec.CategoryDescription as "Category Description" 
	FROM ArchiveEntryData as ED
inner Join [ArchiveCompanyData] as CD
	on ED.EntrantCompanyNo = CD.companyNo
	and ed.Festivalyear = cd.ArchiveYear
inner join ArchiveEntryCategories as EC
	ON ec.FestivalCode = ed.FestivalCode COLLATE Latin1_General_CI_AI
	AND ec.FestivalYear = ed.FestivalYear
	AND ec.CategoryCode = ed.CategoryCode COLLATE Latin1_General_CI_AI
	AND ec.EntryTypeId = ed.EntryTypeId

LEFT JOIN 
ArchiveEntrySector sec
	ON sec.FestivalYear = ed.FestivalYear
	AND sec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS 
	AND sec.Sector_ID = ed.sector_id
LEFT JOIN ArchiveEntrySector subSec
	ON subSec.FestivalYear = ed.FestivalYear
	AND subSec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS 
	AND subSec.Sector_ID = ed.sector_sub_id 	

	where ed.FestivalYear >= 2011
	and ed.FestivalCode IN ('CL', 'LE', 'LI', 'LH')
	and	(ed.Advertiser like '%heinek%'
	or '.' + ed.Advertiser + '.' like '%[^a-z]%amstel[^a-z]%' 
	or (ed.Advertiser like 'Sol' or ed.Advertiser like 'cerveza sol' )
	or ed.Advertiser like '%Moretti%'
	or ed.Advertiser like '%Edelweiss%'
	--ciders
	or ed.Advertiser like '%Strongbow%'
	or ed.Advertiser like 'orchard thieve%'
	or ed.Advertiser like '%Stassen%'
	or ed.Advertiser like '%Old Mout%'
	--world beers
	or ed.Advertiser like '%Harar%'
	or ed.Advertiser like '%Windhoek%'
	or ed.Advertiser like '%Maltina%'
	or ed.Advertiser like '%Dos Equis%'
	or ed.Advertiser like '%Red Stripe%'

	or ed.Advertiser like '%bintang%'
	or ed.Advertiser like '%green sand%'
	or ed.Advertiser like '%South Pacific%' --gamwtoxristouli
	or ed.Advertiser like '%kingfischer%'

	or (ed.Advertiser like '%Gösser%' or  ed.Advertiser like '%Gosser%')
	or ed.Advertiser like '%Sagres%'

	or ed.Advertiser like '%Cruzcampo%'
	or ed.Advertiser like '%Desperados%'
	or ed.Advertiser like '%Soproni%'
	or (ed.Advertiser like '%Żywiec%' or  ed.Advertiser like '%Zywiec%')
	or ed.Advertiser like '%Beavertown%'


	or ed.Advertiser like '%Affligem%'
	or ed.Advertiser like '%Lagunitas%'
	or ed.Advertiser like '%Mort Subite%')
	and ed.Advertiser not like '%COLA%'
	and ed.Advertiser not like '%EDELWEISS AIR%'
	and ed.Advertiser not like '%CITY OF WINDHOEK%'
'''
TBWAQuery = """SELECT ED.FestivalYear, ED.Advertiser, ED.short as Shortlist, ED.FestivalCode,ED.EntryTypeName,
	ED.AwardCountCode as Winner, ED.PrizeCode, ED.CategoryCode,  ed.CategorySubTypeID, ed.entryId as "All Entries",
	cd.CompanyName, CD.NetworkCode, cd.NetworkName, CD.UltimateHoldingCompanyName, cd.GroupCompanyName, 
	cd.Country, cd.GroupCompanyName, cd.coTown, cd.RegionName,
	ec.MediaDescription, ec.CategoryDescription 
	
	FROM ArchiveEntryData as ED
	left Join [ArchiveCompanyData] as CD
	on ED.EntrantCompanyNo = CD.companyNo and ed.Festivalyear = cd.ArchiveYear
	left join ArchiveEntryCategories as EC
	ON ec.FestivalCode = ed.FestivalCode COLLATE Latin1_General_CI_AI
	AND ec.FestivalYear = ed.FestivalYear
	AND ec.CategoryCode = ed.CategoryCode COLLATE Latin1_General_CI_AI
	AND ec.EntryTypeId = ed.EntryTypeId

    where ed.FESTIVALCODE IN ('CL', 'LE', 'LI', 'LH')
    and ed.festivalyear in (2017,2018,2019)

--	and  ed.Cancelled <>1
--	and ed.AwardCountCode is not null"""


eurobest2021 ='''select
	cd.companyName, cd.companyNo, cd.CompanyType, cd.coTown, cd.Country, cd.GroupCompanyName, cd.NetworkName,
	cd.UltimateHoldingCompanyName, cd.RegionName,
	ED.FestivalYear, ED.Advertiser, ED.short as Shortlist, ED.FestivalCode, ED.EntryTypeName, 
	ED.AwardCountCode as Winner, ED.PrizeCode, ED.CategoryCode, ed.CategorySubTypeID, ed.CatalogueNo, 
	ed.EntryId as "All Entries", ed.Product,ed.title,
	ec.MediaDescription, ec.CategoryDescription as "Category Description",
	sec.Sector_Name sector_name,
	subSec.Sector_Name sub_sector_name,
	ped.Cancelled 


from publishedArchiveEntryData ped


left join ArchiveEntryData ed
on ped.festivalYear  = ed.FestivalYear and
ped.EntryId = ed.EntryId

left Join [ArchiveCompanyData] as CD
on ed.EntrantCompanyNo = CD.companyNo 
and ed.Festivalyear = cd.ArchiveYear


left join ArchiveEntryCategories as EC
	ON ec.FestivalCode = ed.FestivalCode COLLATE Latin1_General_CI_AI
	AND ec.FestivalYear = ed.FestivalYear
	AND ec.CategoryCode = ed.CategoryCode COLLATE Latin1_General_CI_AI
	AND ec.EntryTypeId = ed.EntryTypeId

	LEFT JOIN
ArchiveEntrySector sec
	ON sec.FestivalYear = ed.FestivalYear
	AND sec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS 
	AND sec.Sector_ID = ed.sector_id

LEFT JOIN ArchiveEntrySector subSec
	ON subSec.FestivalYear = ed.FestivalYear
	AND subSec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS 
	AND subSec.Sector_ID = ed.sector_sub_id 


where ed.FestivalCode ='eb'
and ed.FestivalYear = 2021
'''

ipgquery = '''
select  CD.UltimateHoldingCompanyName, count (cd.UltimateHoldingCompanyName) as count

	cd.companyName, cd.companyNo, cd.CompanyType, cd.coTown, cd.Country, cd.GroupCompanyName, cd.NetworkName,
	cd.UltimateHoldingCompanyName, cd.RegionName,
	ED.FestivalYear, ED.Advertiser, ED.short as Shortlist, ED.FestivalCode, ED.EntryTypeName, 
	ED.AwardCountCode as Winner, ED.PrizeCode, ED.CategoryCode, ed.CategorySubTypeID, ed.CatalogueNo, 
	ed.EntryId as "All Entries", ed.Product,ed.title, ed.HeaderCampaignId, ed.HeaderCampaignTitle,
	ec.MediaDescription, ec.CategoryDescription as "Category Description",
	sec.Sector_Name sector_name,
	subSec.Sector_Name sub_sector_name


from publishedArchiveEntryData ped


left join ArchiveEntryData ed
on ped.festivalYear  = ed.FestivalYear and
ped.EntryId = ed.EntryId

left Join [ArchiveCompanyData] as CD
on ed.EntrantCompanyNo = CD.companyNo 
and ed.Festivalyear = cd.ArchiveYear


left join ArchiveEntryCategories as EC
	ON ec.FestivalCode = ed.FestivalCode COLLATE Latin1_General_CI_AI
	AND ec.FestivalYear = ed.FestivalYear
	AND ec.CategoryCode = ed.CategoryCode COLLATE Latin1_General_CI_AI
	AND ec.EntryTypeId = ed.EntryTypeId

	LEFT JOIN
ArchiveEntrySector sec
	ON sec.FestivalYear = ed.FestivalYear
	AND sec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS 
	AND sec.Sector_ID = ed.sector_id

LEFT JOIN ArchiveEntrySector subSec
	ON subSec.FestivalYear = ed.FestivalYear
	AND subSec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS 
	AND subSec.Sector_ID = ed.sector_sub_id 

where ((cd.companyName like '%IPG%' or cd.NetworkName like '%IPG%' or cd.UltimateHoldingCompanyName like '%IPG%')
OR 
(cd.companyName like '%Interpublic Group%' or cd.NetworkName like '%Interpublic Group%' or cd.UltimateHoldingCompanyName like '%Interpublic Group%'))

--cd.companyName like '%FITCH%' or cd.NetworkName like '%FITCH%')
and ed.FestivalYear >= 2018
and ed.FestivalCode in ('CL', 'LE', 'LI', 'LH')
--and (cd.companyName not like 'wavemaker' and  cd.NetworkName not like 'wavemaker' )
--and ed.AwardCountCode is not null

group by cd.UltimateHoldingCompanyName
'''



