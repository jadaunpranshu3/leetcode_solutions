select  score,
    DENSE_rank() over(order by score desc)as 'rank'
from Scores;

