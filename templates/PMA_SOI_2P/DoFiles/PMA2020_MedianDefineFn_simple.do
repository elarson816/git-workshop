/*
06/20/2014
written for PMA2020 two-pager

Three input parameters: file, variable, low bound of age
e.g.

pma2020mediansimple GHtab age1stmarriage 15

DHS uses this interpolation method to calculate the median for discrete variables
See page 16 of "Guide to DHS statistics" for details
*/

*arguments to input are 1 (dataset), 2 (variable name), 3 lower age bound
cap program drop pma2020mediansimple
program define pma2020mediansimple

use `1', clear
keep if FQ_age>=`3' //age range for the tabulation

gen one=1
drop if `2'==.
collapse (count) count=one [pweight=FQweight], by(`2')
sort  `2'
gen ctotal=sum(count)
egen total=sum(count)
gen cp=ctotal/total

keep if (cp <= 0.5 & cp[_n+1]>0.5) | (cp>0.5 & cp[_n-1]<=0.5)

local median=(0.5-cp[1])/(cp[2]-cp[1])*(`2'[2]-`2'[1])+`2'[1] +1

macro list _median

clear
set obs 1
gen median=`median'

end
