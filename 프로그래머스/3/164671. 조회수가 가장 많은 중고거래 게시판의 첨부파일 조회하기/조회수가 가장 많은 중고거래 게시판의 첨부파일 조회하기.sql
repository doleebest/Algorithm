SELECT CONCAT('/home/grep/src/', b.board_id, '/', f.file_id, f.file_name,  f.file_ext) AS FILE_PATH
FROM used_goods_board b
JOIN used_goods_file f ON b.board_id = f.board_id
WHERE b.board_id = (
    SELECT board_id
    FROM used_goods_board
    ORDER BY views DESC
    LIMIT 1
)
ORDER BY f.file_id DESC;
