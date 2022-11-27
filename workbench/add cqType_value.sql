ALTER TABLE cqType ADD COLUMN cqType_value varchar(11) NOT NULL AFTER cqType_id;
UPDATE cqType SET cqType_value = '1' WHERE cqType_name = 'test';
UPDATE cqType SET cqType_value = '2' WHERE cqType_name = 'search';
ALTER TABLE cqType ADD UNIQUE(cqType_value);
