- Print prime numbers
https://www.hackerrank.com/challenges/print-prime-numbers/problem  
```sql
with recursive tmp(n) as (
    select 2
    union all
    select n + 1
    from tmp
    where n < 1000
)
select group_concat(t1.n separator '&')
from tmp as t1
where not exists (
    select * 
    from tmp as t2
    where t2.n <= sqrt(t1.n)
         and t1.n % t2.n = 0
)
```

- Calculate median
_re-visit_
https://www.hackerrank.com/challenges/weather-observation-station-20/problem
```sql
set @row := -1;

select round(avg(seq.lat_n), 4)
from (
    select (@row := @row + 1) as i_row, lat_n
    from station
    order by lat_n
) as seq
where seq.i_row in (ceil(@row / 2), floor(@row / 2))
```

- Draw The Triangle 1 (with recursive)
```sql
with recursive tmp(n) as (
    select 20
    union all
    select n - 1
    from tmp
    where n > 1
)
select repeat('* ', n)
from tmp
```

- Q176. Second Highest Salary  
_Beware of the null condition_  
https://leetcode.com/problems/second-highest-salary/submissions/
```sql
select max(salary) as SecondHighestSalary
from employee
where salary < (select max(salary) from employee)
```


- Q177. Nth Highest Salary
_similar to Q176_
https://leetcode.com/problems/nth-highest-salary/submissions/
```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
declare m int;
set m = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      
      select distinct salary
      from employee
      union all 
      select null as salary
      order by salary desc
      limit 1 offset m
      
  );
END
```


- Q626. Exchange Seats
_very interesting_
https://leetcode.com/problems/exchange-seats/submissions/
```sql
select row_number() over() as id, student
from seat as s
order by (s.id -1) div 2, s.id desc
```