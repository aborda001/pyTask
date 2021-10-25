CREATE TABLE IF NOT EXISTS User (
	idUser INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	userName TEXT UNIQUE,
	password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Task (
	idTask INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	idUser INTEGER NOT NULL,
	description TEXT NOT NULL,
	status TEXT NOT NULL,
	foreign key (idUser) references User (idUser)
		on delete cascade
		on update cascade
);