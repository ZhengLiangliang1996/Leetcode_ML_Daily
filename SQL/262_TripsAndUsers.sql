# Write your MySQL query statement below
WITH 

CLIENT_UNBANNED AS (
    SELECT Users_Id
    FROM Users
    WHERE Banned = 'NO'
        AND Role = 'client'
),


#DRIVER_UNBANNED AS (
#    SELECT Users_Id
#    FROM Users
#    WHERE Banned = 'NO'
#        AND Role = 'driver'
#),

EXCLUDE AS (
    SELECT T.Id
        , T.Client_Id
        , T.Driver_Id
        , T.Status
        , T.Request_at
    
    FROM Trips T
    
    INNER JOIN CLIENT_UNBANNED CN
        ON CN.Users_Id = T.Client_Id
    
    #INNER JOIN DRIVER_UNBANNED DN 
       # ON DN.Users_Id = T.Driver_Id
)

SELECT Request_at AS Day
    , ROUND(SUM(CASE WHEN
                    status = 'cancelled_by_driver' OR status = 'cancelled_by_client' THEN 1 
                ELSE 0 
                END) / COUNT(Id), 2) as "Cancellation Rate"

FROM EXCLUDE

WHERE Request_at BETWEEN '2013-10-01' AND '2013-10-03'

GROUP BY 1

ORDER BY 1
