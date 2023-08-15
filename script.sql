-- RUN THIS SCRIPT IN POSTGRESQL
-- TERMINAL BEFORE EXECUTING THE PROJECT

CREATE DATABASE IF NOT EXISTS hamza_ai;

\c hamza_ai;

CREATE TABLE IF NOT EXISTS videos (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    url TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS transcriptions (
    id SERIAL PRIMARY KEY,
    video_id INT REFERENCES videos(id),
    text TEXT NOT NULL,
    start_time NUMERIC NOT NULL,
    duration NUMERIC NOT NULL
);
