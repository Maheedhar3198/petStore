from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"   # table name

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

engine = create_engine("sqlite:///test.db", echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


user1 = User(name="Alice", email="alice@example.com")
user2 = User(name="Bob", email="bob@example.com")

session.add_all([user1, user2])
session.commit()

all_users = session.query(User).all()
for u in all_users:
    print(u)
