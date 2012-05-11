from zope.interface import Interface, Attribute

class IDeclarativeBase(Interface):
    pass

class IBeforeFlush(Interface):
    """Hook for SQLAlchemy MapperEvent.before_flush at ZCA level"""

class IEngineInitialized(Interface):
    engine = Attribute("Configured SQLAlchemy engine")

class IDatabaseConfigured(Interface):
    engine = Attribute("Configured SQLAlchemy engine")

