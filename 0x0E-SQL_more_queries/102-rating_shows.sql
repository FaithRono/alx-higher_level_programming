-- script that lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT tv_shows.title, SUM(tvshows_rate.rating) as rating
FROM tv_shows
JOIN tvshows_rate ON tv_shows.id = tvshows_rate.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;
