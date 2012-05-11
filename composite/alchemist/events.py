from sqlalchemy.orm.session import SessionExtension
from zope.interface import implements
from .interfaces import IBeforeFlush, IEngineInitialized, IDatabaseConfigured
from pyramid.threadlocal import get_current_registry

class BeforeFlush(object):
    implements(IBeforeFlush)
    def __init__(self, registry, session, flush_context, instances):
        self.registry = registry
        self.session = session
        self.flush_context = flush_context
        self.instances = instances

class EventExtension(SessionExtension):
    """Just stub now"""
    def before_flush(self, session, flush_context, instances):
        registry = get_current_registry()
        event = BeforeFlush(registry, session, flush_context, instances)
        registry.notify(event)


class EngineInitialized(object):
    implements(IEngineInitialized)
    def __init__(self, registry, engine):
        self.registry = registry
        self.engine = engine

class DatabaseConfigured(object):
    implements(IDatabaseConfigured)
    def __init__(self, registry, engine):
        self.registry = registry
        self.engine = engine

