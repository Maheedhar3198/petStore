from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey, column
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class EmpDetails(Base):
    __tablename__ = 'EmpDetails'
    ID = Column(Integer, primary_key=True)
    Name = Column(String)
    email = Column(String)
    DOJ = Column(Date)
    EmpID = Column(Integer, unique=True)


class EmpSalary(Base):
    __tablename__ = 'EmpSalary'
    ID = Column(Integer, primary_key=True)
    Salary = Column(Float)
    EmpID = Column(Integer, ForeignKey('EmpDetails.EmpID'))

class ProjDetails(Base):
    __tablename__ = 'ProjDetails'
    ID = Column(Integer, primary_key=True)
    ProjID = Column(Integer)
    ProjName = Column(String)
    EmpID = Column(Integer)


class Insurance(Base):
    __tablename__ = 'Insurance'
    ID = Column(Integer, primary_key=True)
    InsuranceAmount = Column(Integer)
    EmpID = Column(Integer)



engine = create_engine("mysql+pymysql://root:Atmecs!1234@localhost:3306/employees")
Session = sessionmaker(bind=engine)
session = Session()

employees = (session.query(EmpDetails.Name).join(EmpSalary, EmpDetails.EmpID == EmpSalary.EmpID)
             .filter(EmpDetails.DOJ > datetime(2019, 12, 31))
             .filter(EmpSalary.Salary > 20000).all())

for emp in employees:
    print(emp.Name)


employeeID = (session.query(ProjDetails.EmpID).join(Insurance, ProjDetails.EmpID == Insurance.EmpID)
              .filter(ProjDetails.ProjName == "Google").filter(Insurance.InsuranceAmount > 100000).all())

for identity in employeeID:
    print(identity.EmpID)

names = (session.query(EmpDetails.Name).join(EmpSalary, EmpDetails.EmpID == EmpSalary.EmpID)
        .join(Insurance, EmpDetails.EmpID == Insurance.EmpID) .filter(EmpSalary.Salary > 20000)
        .filter(Insurance.InsuranceAmount > 100000).all())


for name in names:
    print(name.Name)