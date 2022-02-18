use `web-project-g17`;

create table if not exists cities
(
	city varchar(255) not null
		primary key
);

create table if not exists contacts
(
	id int auto_increment
		primary key,
	email varchar(255) not null,
	description text null,
	DT timestamp default CURRENT_TIMESTAMP not null
);

create table if not exists users
(
	email varchar(255) not null
		primary key,
	first_name varchar(255) null,
	last_name varchar(255) null,
	create_date timestamp default CURRENT_TIMESTAMP null,
	about_me text null,
	phone_number varchar(10) null,
	password varchar(120) not null,
	car_type varchar(100) null,
	car_color varchar(100) null
);

create table if not exists trips
(
	trip_id int auto_increment
		primary key,
	driver varchar(255) null,
	pick_up_date date not null,
	pick_up_time time not null,
	pick_up_city varchar(255) null,
	drop_city varchar(255) null,
	available_seats int null,
	price int not null,
	passengers int not null,
	constraint trips_ibfk_1
		foreign key (driver) references users (email)
);


create index driver
	on trips (driver);

create table if not exists tripuser
(
	trip int not null,
	user varchar(255) not null,
	seats_amount int null,
	primary key (trip, user),
	constraint fk_trip
		foreign key (trip) references trips (trip_id),
	constraint fk_user
		foreign key (user) references users (email)
);

