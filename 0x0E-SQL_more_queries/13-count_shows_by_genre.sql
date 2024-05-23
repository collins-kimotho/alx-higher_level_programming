-- Script that lists all genres and number of shows linked to each
SELECT
	genres.name AS genre,
	COUNT(show_genres.show_id) AS number_of_shows
FROM
	tv_genres AS genres
	LEFT JOIN tv_show_genres AS show_genres ON genres.id = show_genres.genre_id
GROUP BY
	genres.name
HAVING
	number_of_shows > 0
ORDER BY
	number_of_shows DESC;
	
