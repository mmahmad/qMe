-- DDL generated by Postico 1.5.8
-- Not all database features are supported. Do not use for backup.

-- Table Definition ----------------------------------------------

CREATE TABLE merchants_counters (
    counter_uuid text PRIMARY KEY,
    merchant_uuid text NOT NULL REFERENCES merchants(uuid) ON DELETE CASCADE ON UPDATE CASCADE,
    counter_identifier text,
    counter_sequence integer NOT NULL DEFAULT 0
);

-- Indices -------------------------------------------------------

CREATE UNIQUE INDEX merchants_counters_pkey ON merchants_counters(counter_uuid text_ops);