create table zoo (
    zname          text not null primary key,
    business_hours text,
    phone_number   integer,
    fax_number     integer,
    email          text,
    loc_city       text,
    loc_state      text,
    loc_zip        integer
);

create table employee (
    fname        text not null,
    minit        text,
    lname        text not null,
    eid          integer primary key autoincrement not null,
    phone_number integer,
    s_date       date not null,
    sex          text,
    age          integer,
    salary       text not null,
    zname        text REFERENCES zoo(zname),
    CONSTRAINT employee_k
);

create table manager (
    zoo_subsection text not null,
    eid integer    integer not null,
    CONSTRAINT k_manager
        FOREIGN KEY (eid)
        REFERENCES employee(eid)
);

create table caretaker (
    specialty text not null,
    eid       integer not null,
    zoo_subsection text not null REFERENCES manager(zoo_subsection),
    CONSTRAINT k_caretaker
        FOREIGN KEY (eid)
        REFERENCES employee(eid)
);

create table takes_care_of (
    eid integer not null REFERENCES caretaker(eid),
    aid integer not null REFERENCES animal(aid)
);

create table animal (
    aid              integer primary key autoincrement not null,
    cage_number      integer,
    biological_class text,
    species          text,
    feed_time        text,
    zoo_section      text,
    diet             text,
    zname            text REFERENCES zoo(zname)
);