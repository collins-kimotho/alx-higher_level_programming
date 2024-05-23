-- Script that lists all shows and all genres linked to each show in the database hbtn_0d_tvshows
SELECT tv.title, tv_genre.name
FROM tv_shows AS tv
LEFT JOIN tv_show_genres AS tv_show_genre ON tv.id = tv_show_genre.show_id
LEFT JOIN tv_genres AS tv_genre ON tv_show_genre.genre_id = tv_genre.id
ORDER BY tv.title, tv_genre.name ASC;
