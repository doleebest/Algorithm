SELECT 
    PT_NAME, 
    PT_NO, 
    GEND_CD, 
    AGE, 
    COALESCE(TLNO, 'NONE') AS TLNO
FROM 
    PATIENT
WHERE 
    AGE <= 12 and gend_cd = 'w'
ORDER BY 
    AGE DESC, 
    PT_NAME ASC;
