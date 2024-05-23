-- Script that lists all Comedy shows in the database

SELECT shows.title
FROM tv_shows AS shows
INNER JOIN tv_show_genres AS genre ON shows.id = genre.show_id
INNER JOIN tv_genres AS tv_genre ON genre.genre_id = tv_genre.id
WHERE tv_genre.name = 'Comedy'
ORDER BY shows.title ASC;
