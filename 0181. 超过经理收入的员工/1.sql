-- 执行用时：396 ms, 在所有 MySQL 提交中击败了64.69% 的用户
-- 内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
select
    ee.name as Employee
from
    Employee as e
    inner join Employee as ee on e.id = ee.managerId
where
    ee.salary > e.salary