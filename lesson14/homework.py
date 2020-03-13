"""Описать таблицы из lesson12/homework.sql при помощи sqlalchemy"""

from sqlalchemy import (
    create_engine,
    MetaData,
    Column,
    ForeignKey,
    Boolean,
    Integer,
    String,
    UniqueConstraint
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine(
    'postgres://postgres:postgres@localhost:5432/sqlalchemy1'
)

metadata = MetaData()

BaseModel = declarative_base(bind=engine)


class User(BaseModel):
    __tablename__ = 'app_users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)

    def __repr__(self):
        return f'id: {self.id}, username: {self.username}\n'


class Tests(BaseModel):
    __tablename__ = 'tests'

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    text = Column(String, nullable=False)

    def __repr__(self):
        return f'id: {self.id} number: {self.number} text: {self.text}'


class Question(BaseModel):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    text = Column(String, nullable=False)

    def __repr__(self):
        return f'id: {self.id} number: {self.number} question: {self.text}'


class TestQuestion(BaseModel):
    __tablename__ = 'tests_questions'
    __table_args__ = (UniqueConstraint('test_id', 'question_id'), )

    id = Column(Integer, primary_key=True)
    test_id = Column(ForeignKey('tests.id'), nullable=False)
    question_id = Column(ForeignKey('questions.id'), nullable=False)

    def __repr__(self):
        return f'id: {self.id} test_id: {self.test_id} ' \
               f'question_id: {self.question_id}'


class Answer(BaseModel):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    is_correct = Column(Boolean, default=False)
    question_id = Column(ForeignKey('questions.id'), nullable=False)

    def __repr__(self):
        return f'id: {self.id} text: {self.text} is_correct: {self.is_correct}' \
               f'question_id:m{self.question_id}'


class UserAnswer(BaseModel):
    __tablename__ = 'users_answers'
    __table_args__ = (UniqueConstraint('tests_questions_id', 'user_id'),)

    id = Column(Integer, primary_key=True)
    tests_questions_id = Column(ForeignKey('tests_questions.id'), nullable=False)
    user_id = Column(ForeignKey('app_users.id'), nullable=False)
    answer_id = Column(ForeignKey('answers.id'), nullable=False)

    def __repr__(self):
        return f'id: {self.id} tests_questions_id: {self.tests_questions_id}' \
               f' user_id: {self.user_id} answer_id: {self.answer_id}'


BaseModel.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

users = User(username="victor")
session.add(users)
users = User(username="vlad")
session.add(users)

test = Tests(number=1, text="The first test")
session.add(test)
question = Question(number=1, text="The first question")
session.add(question)
testquestion = TestQuestion(test_id=1, question_id=1)
session.add(testquestion)

session.commit()

print(session.query(User).all())
print(session.query(Tests).all())
print(session.query(Question).all())
print(session.query(TestQuestion).all())
print(session.query(UserAnswer).all())
