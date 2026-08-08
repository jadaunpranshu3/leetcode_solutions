select  MAX(num) as num FROM (
    select num from MyNumbers
    group by num
    having count(*)=1
)AS temp;
