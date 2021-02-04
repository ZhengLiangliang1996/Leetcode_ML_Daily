
# Write your MySQL query statement below
SELECT class 

FROM courses 

GROUP BY class 
# 5 students, these student should all be distinct 
# 里面有坑 有两个 A MATH
'''
比如
{"headers": {"courses": ["student", "class"]}, 
"rows": {"courses": [["A", "Math"], 
                     ["B", "English"], 
                     ["C", "Math"], 
                     ["D", "Biology"], 
                     ["E", "Math"], 
                     ["F", "Math"], 
                     ["A", "Math"]]}}
'''
HAVING COUNT(DISTINCT student) >= 5
