# DROP TABLES

songplay_table_drop = "drop table if exists songplays;"
user_table_drop = "drop table if exists users;"
song_table_drop = "drop table if exists songs;"
artist_table_drop = "drop table if exists artists;"
time_table_drop = "drop table if exists time;"

# CREATE TABLES

songplay_table_create = ("""
create table if not exists songplays (
	songplay_id serial primary key,
	start_time bigint not null,
	user_id int,
	level varchar(10),
	song_id varchar(18),
	artist_id varchar(18),
	session_id int not null,
	location varchar(100),
	user_agent varchar(200)
);
""")

user_table_create = ("""
create table if not exists users (
	user_id int not null primary key,
	first_name varchar(15),
	last_name varchar(15),
	gender varchar(1),
	level varchar(5)
);

""")

song_table_create = ("""
create table if not exists songs (
	song_id varchar(18) not null primary key,
	title varchar(100) not null,
	artist_id varchar(18) not null,
	year int,
	duration numeric(10,5) not null
);
""")

artist_table_create = ("""
create table if not exists artists (
	artist_id varchar(18) not null primary key,
	name varchar(150) not null,
	location varchar(100),
	latitude numeric(8, 5),
	longitude numeric(8, 5)
);
""")

time_table_create = ("""
create table if not exists time (
	start_time bigint not null primary key,
	hour int not null,
	day int not null,
	weekofyear int not null,
	month int not null,
	year int not null,
	weekday int not null
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id)
DO NOTHING;
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id)
DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id)
DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time ("start_time", "hour", "day", "weekofyear", "month", "year", "weekday")
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time)
DO NOTHING;
""")

# FIND SONGS

song_select = ("""
select songs.song_id, artists.artist_id from songs
inner join artists on artists.artist_id = songs.artist_id
where title=%s and artists.name=%s and duration=%s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
