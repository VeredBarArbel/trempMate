use `web-project-g17`;

insert into cities(city) value('Tel-Aviv');
insert into cities(city) value('Beer-Sheba');
insert into cities(city) value('Jerusalem');
insert into cities(city) value('Hadera');
insert into cities(city) value('Haifa');
insert into cities(city) value('Herzeliya');
insert into cities(city) value('Tel-mond');
insert into cities(city) value('Eilat');
insert into cities(city) value('Metula');

insert into users(email, first_name, last_name, about_me, phone_number, password, car_type, car_color)
values('barelbaz@gmail.com','Bar','Elbaz','student','0507889272','12345','kia','red');
insert into users(email, first_name, last_name, about_me, phone_number, password, car_type, car_color)
values('dana@gmail.com','dana','Rubin','student','0542338989','19908','toyota','black');
insert into users(email, first_name, last_name, about_me, phone_number, password, car_type, car_color)
values('hadas@gmail.com','hadas','gal','','0507834272','12345','toyota','blue');
insert into users(email, first_name, last_name, about_me, phone_number, password, car_type, car_color)
values('ran@gmail.com','Rar','Biran','','0507239272','12345','chevrolet','white');
insert into users(email, first_name, last_name, about_me, phone_number, password, car_type, car_color)
values('gal@gmail.com','gal','orad','','0502897877','12345','kia','black');
insert into users(email, first_name, last_name, about_me, phone_number, password, car_type, car_color)
values('shay@gmail.com','shai','Rad','','0502812345','889767','','');
insert into users(email, first_name, last_name, about_me, phone_number, password, car_type, car_color)
values('matan@gmail.com','matan','zarmon','','0502890897','55555','','');

insert into contacts(email, description) VALUES('gal@gmail.com','the driver didnt show up ');
insert into contacts(email, description) VALUES('shai@gmail.com','i have a problem in the app please conatact me ');
insert into contacts(email, description) VALUES('hadar@gmail.com','please contact me');
insert into contacts(email, description) VALUES('tal@gmail.com','hi please call me back i have a technical problem');

insert into trips(driver, pick_up_date, pick_up_time, pick_up_city, drop_city, available_seats, price, passengers) VALUES ('gal@gmail.com','2022-05-28','20:00','Jerusalem','Tel-Aviv','1','25','4');
insert into trips(driver, pick_up_date, pick_up_time, pick_up_city, drop_city, available_seats, price, passengers) VALUES ('ran@gmail.com','2022-02-25','16:00','Tel-Aviv','Hadera','2','25','3');
insert into trips(driver, pick_up_date, pick_up_time, pick_up_city, drop_city, available_seats, price, passengers) VALUES ('hadas@gmail.com','2022-02-20','17:00','Metula','Tel-Aviv','2','20','3');
insert into trips(driver, pick_up_date, pick_up_time, pick_up_city, drop_city, available_seats, price, passengers) VALUES ('gal@gmail.com','2022-02-22','18:00','Jerusalem','Eilat','2','50','3');

insert into tripuser(trip, user, seats_amount) VALUES ('1','gal@gmail.com','1');
insert into tripuser(trip, user, seats_amount) VALUES ('2','ran@gmail.com','1');
insert into tripuser(trip, user, seats_amount) VALUES ('3','dana@gmail.com','1');
insert into tripuser(trip, user, seats_amount) VALUES ('4','barelbaz@gmail.com','1');
insert into tripuser(trip, user, seats_amount) VALUES ('1','barelbaz@gmail.com','2');

