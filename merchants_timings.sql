-- DDL generated by Postico 1.5.8
-- Not all database features are supported. Do not use for backup.

-- Table Definition ----------------------------------------------

CREATE TABLE merchants_timings (
    uuid text PRIMARY KEY REFERENCES merchants(uuid) ON DELETE CASCADE ON UPDATE CASCADE,
    saturday_start time without time zone,
    saturday_end time without time zone,
    sunday_start time without time zone,
    sunday_end time without time zone,
    monday_start time without time zone,
    monday_end time without time zone,
    tuesday_start time without time zone,
    tuesday_end time without time zone,
    wednesday_start time without time zone,
    wednesday_end time without time zone,
    thursday_start time without time zone,
    thursday_end time without time zone,
    friday_start time without time zone,
    friday_end time without time zone
);

-- Indices -------------------------------------------------------

CREATE UNIQUE INDEX merchants_timings_pkey ON merchants_timings(uuid text_ops);
