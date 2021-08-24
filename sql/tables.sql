create table program
(

	id_program integer, 
	program varchar(100) not null,
	
	primary key(id_program)

);

create table shell
(

	id_program integer,
	id_shell integer,
	
	command varchar(500) not null,
	connection char(3) not null,
    
	primary key(id_shell),
	foreign key (id_program) references program(id_program)

);

