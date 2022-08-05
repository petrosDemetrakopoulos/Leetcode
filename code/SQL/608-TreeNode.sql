SELECT DISTINCT t.id,CASE WHEN t.p_id IS null THEN 'Root' 
                         WHEN p.p_id IS null THEN 'Leaf' 
                         ELSE 'Inner' 
                    END AS type
FROM Tree t 
LEFT JOIN Tree p ON p.p_id = t.id 