clear all
set more off
capture log close

cd "/Users/andreaspetrou/OneDrive - University of Bristol/UoB/Year 3/Data Science/PROJECT/Final things"

log using merging.log, replace

import delimited distance.csv

br

save "/Users/andreaspetrou/OneDrive - University of Bristol/UoB/Year 3/Data Science/PROJECT/Final things/distance.dta", replace

clear

import delimited data_final.csv

br

save "/Users/andreaspetrou/OneDrive - University of Bristol/UoB/Year 3/Data Science/PROJECT/Final things/data_final.dta", replace

merge m:1 country using "/Users/andreaspetrou/OneDrive - University of Bristol/UoB/Year 3/Data Science/PROJECT/Final things/distance.dta", keepusing(country distance)

drop ïrank currency_symbol v4 local_price eur usd region areatype latitude longitude name gnipercapitacurrentusd gnipercapitagbp usdgbpaverageexcahngerate2019 carpricegnipercapita affortability

keep if _merge==3
drop _merge

br

save "/Users/andreaspetrou/OneDrive - University of Bristol/UoB/Year 3/Data Science/PROJECT/Final things/distance_price.dta", replace

list country gbp id distance

outsheet country gbp id distance using distance_price.csv , comma 

type distance_price.csv

capture log close
