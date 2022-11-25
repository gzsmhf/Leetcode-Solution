-- 执行用时：413 ms, 在所有 MySQL 提交中击败了81.25% 的用户
-- 内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户

select
    p.firstName,
    p.lastName,
    a.city,
    a.state
from
    Person as p
    left join Address as a on p.personId = a.personId