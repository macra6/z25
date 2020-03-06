CREATE TABLE my_user (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    email VARCHAR(60) NOT NULL UNIQUE,
    other VARCHAR(90)
);

CREATE TABLE answers (
    id SERIAL PRIMARY KEY;
    name REFERENCES my_user(name);
    question REFERENCES test_1(question);
    answers VARCHAR(120);
    correct BOOLEAN NOT NULL;
):

CREATE TABLE test_1(
    id SERIAL PRIMARY KEY;
    question VARCHAR(120) NOT NULL;
    answer VARCHAR(120) NOT NULL;
);

INSERT INTO my_user(name, email, other)
VALUES ('вася', 'вася@mail.com')

INSERT INTO test_1(question, answer)
VALUES ('1й вопрос', 'правильный ответ')
    ('2й вопрос', 'правильный ответ')
    ('3й вопрос', 'правильный ответ')
    ('4й вопрос', 'правильный ответ')
