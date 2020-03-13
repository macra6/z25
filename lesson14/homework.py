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


class Test(BaseModel):
    __tablename__ = 'tests'

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    text = Column(String, nullable=False)


class Question(BaseModel):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    text = Column(String, nullable=False)


class TestQuestion(BaseModel):
    __tablename__ = 'tests_questions'
    __table_args__ = (UniqueConstraint('test_id', 'question_id'), )

    id = Column(Integer, primary_key=True)
    test_id = Column(ForeignKey('tests.id'), nullable=False)
    question_id = Column(ForeignKey('questions.id'), nullable=False)


class Answer(BaseModel):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    is_correct = Column(Boolean, default=False)
    question_id = Column(ForeignKey('questions.id'), nullable=False)


class UserAnswer(BaseModel):
    __tablename__ = 'users_answers'
    __table_args__ = (UniqueConstraint('tests_questions_id', 'user_id'),)

    id = Column(Integer, primary_key=True)
    tests_questions_id = Column(ForeignKey('tests_questions.id'), nullable=False)
    user_id = Column(ForeignKey('app_users.id'), nullable=False)
    answer_id = Column(ForeignKey('answers.id'), nullable=False)


BaseModel.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
