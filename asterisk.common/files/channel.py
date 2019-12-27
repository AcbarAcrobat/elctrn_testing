# coding=utf-8


import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID

roles = {'None': 0, 'Conference': 1, 'MainUser': 2, 'FirstAnsweredUser': 3, 'Assistant': 4, 'PartialAssistant': 5,
         'Applicant': 6}
engine = create_engine('postgresql://postgres:1@192.168.3.20/PhoneSystemGateway')
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()


class Channel(Base):
    __tablename__ = 'channel'
    channel_id = Column(String, primary_key=True)
    call_id = Column(UUID(as_uuid=True))
    bridge_id = Column(UUID(as_uuid=True))
    line_id = Column(UUID(as_uuid=True))
    extension = Column(Integer)
    role = Column(Integer)

    def __init__(self, channel_id, call_id, bridge_id, line_id, extension, role):
        self.channel_id = channel_id
        self.call_id = call_id
        self.bridge_id = bridge_id
        self.line_id = line_id
        self.extension = extension
        self.role = role

    def __repr__(self):
        return "<Channel(channel_id={})>".format(self.channel_id)

# yum install python-sqlalchemy python-psycopg2
