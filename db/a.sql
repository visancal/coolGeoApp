create table paystats (
    id integer,
    postal_code_id integer,
    p_gender varchar(1),
    p_age varchar(10),
    p_month date,
    amount real,
    PRIMARY KEY (id)
);

create table postal_codes (
    id integer,
    code integer,
    the_geom geometry(Geometry,4326),
    PRIMARY KEY (id)
);

CREATE INDEX postal_codes_geom_idx
  ON postal_codes
  USING GIST (the_geom);