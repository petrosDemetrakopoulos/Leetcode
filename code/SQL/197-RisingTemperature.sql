SELECT wthr1.id
FROM weather Wthr1, Weather wthr2
WHERE wthr1.temperature > wthr2.temperature AND to_days(wthr1.recordDate) - to_days(wthr2.recordDate) = 1