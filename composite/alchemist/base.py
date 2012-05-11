from threading import local
import sqlalchemy as sqla
from sqlalchemy import orm
from sqlalchemy.ext import declarative
from zope.sqlalchemy import ZopeTransactionExtension
from zope.interface import classImplements
from .events import EventExtension
from .interfaces import IDeclarativeBase

_base = declarative.declarative_base()
classImplements(_base, IDeclarativeBase)

_zte = ZopeTransactionExtension()
_ev_ext = EventExtension()
_session = orm.scoped_session(orm.sessionmaker(extension=[_zte, _ev_ext]))
_session_maker = orm.sessionmaker()
_sa_session = local()

def get_base():
    """Return the central SQLAlchemy declarative base."""
    return _base

def reset_session():
    """Reset sqla session"""
    global _zte, _ev_ext, _session
    _zte = ZopeTransactionExtension()
    _ev_ext = EventExtension()
    _session = orm.scoped_session(orm.sessionmaker(extension=[_zte, _ev_ext]))

class transaction(object):

    def __init__(self, sa):
        self.sa = sa

    def __enter__(self):
        global _sa_session
        _sa_session.sa = self.sa

        return self.sa

    def __exit__(self, type, value, traceback):
        global _sa_session
        _sa_session.sa = None

        if type is None:
            try:
                self.sa.commit()
            except:
                self.sa.rollback()
                raise
        else:
            self.sa.rollback()


def sa_session():
    return transaction(_session_maker())


def get_session_maker():
    return _session_maker

def get_session():
    """Return the central SQLAlchemy contextual session.

    To customize the kinds of sessions this contextual session creates, call
    its ``configure`` method::

        composite.alchemist.get_session().configure(...)
    """
    return getattr(_sa_session, 'sa', _session) or _session

