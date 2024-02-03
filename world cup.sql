create database WC;
use WC;
select * from wc2023 ;
#Total no. of matches won by each team
SELECT distinct(`match winner`),count((`match winner`)) as mw FROM `wc`.`wc2023` group by `match winner` order by mw desc;

# Toss decisions
SELECT count(`Toss decision`), 
case
when count(`Toss decision`) =26 then 'Bowling'
when count(`Toss decision`) =22 then 'Batting'
else 'nowhere'
end as status
FROM `wc`.`wc2023` group by `Toss decision` ;


#Won by Runs or WIcket
SELECT count(`won by`),
case 
when  count(`won by`)=25 then'RUNS'
when count(`won by`)=23 then 'WICKETS'
else 'no'
end as staus1
FROM `wc`.`wc2023` group by `won by`;
#MoM winners
select count(MoM) as mm,MoM from wc2023 group by MoM order by mm desc limit 8;

#BEST STADIUM TO BAT FIRST
SELECT sum(`1st innings score`) as fis,sum(`2nd innings score`) as sis,Venue FROM `wc`.`wc2023`
GROUP BY Venue order by fis,sis ;


#BEST stadium to bowl first
SELECT sum(`1st innings wickets`) as fiw,sum(`2nd innings wickets`) as siw,Venue FROM `wc`.`wc2023`
GROUP BY Venue order by fiw,siw ;

#Average scores in both innings
SELECT round(avg(`1st innings score`),2) as afis,round(avg(`2nd innings score`),2) as asis,Venue FROM `wc`.`wc2023`
GROUP BY Venue order by afis,asis ;

#AVERAGE WICKETS IN BOTH INNINGS
SELECT ROUND(AVG(`1st innings wickets`),2) as Afiw,ROUND(AVG(`2nd innings wickets`),2) as Asiw,Venue FROM `wc`.`wc2023`
GROUP BY Venue order by Afiw,Asiw ;

#MoMs by each profile
SELECT count(`Profile`) as Total_MOMS,`Profile`FROM `wc`.`wc2023` group by `Profile`;

#Highest scorer in by matches
SELECT sum(`highest scorer2`) as hs,`highest scorer` FROM `wc`.`wc2023` group by `highest scorer` order by hs desc limit 6;
#BEST Bowler award in matches
SELECT count(`highest wickets`) as hw,`highest wickets` FROM `wc`.`wc2023` group by `highest wickets` order by hw desc limit 5;

# Match winners according to their venue
SELECT distinct(`match winner`),count(`match winner`),venue FROM `wc`.`wc2023` group by `match winner`,venue ;


