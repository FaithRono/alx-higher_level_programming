-- script that lists all genres in the database hbtn_0d_tvshows_rate
SELECT tv_genres.name, SUM(tvshows_rate.rating) as rating
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tvshows_rate ON tv_shows.id = tvshows_rate.show_id
GROUP BY tv_genres.id
ORDER BY rating DESC;
