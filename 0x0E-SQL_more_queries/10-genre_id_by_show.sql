-- Script to list all shows in the database hbtn_0d_tvshows

-- All your SQL queries should have a comment just before (i.e. syntax above)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
