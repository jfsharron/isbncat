ALTER TABLE genre MODIFY COLUMN value int;
ALTER TABLE genre ADD UNIQUE (value);
ALTER TABLE isbn ADD CONSTRAINT FK_genreisbn FOREIGN KEY(genre) REFERENCES genre(value) ON DELETE CASCADE ON UPDATE CASCADE;