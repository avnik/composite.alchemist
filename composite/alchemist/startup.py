import sqlalchemy
from pyramid.threadlocal import get_current_registry
from .base import get_session, get_session_maker, get_base
from .events import EngineInitialized, DatabaseConfigured

def startup(ev):
    prefix = "sqlalchemy."
    session = get_session()
    cache = {}
    registry = get_current_registry()
    engine = sqlalchemy.engine_from_config(
        registry.settings, prefix,
        execution_options = {'compiled_cache': cache, 'echo': True})
    get_session().configure(bind=engine)
    get_session_maker().configure(bind=engine)
    get_base().metadata.bind = engine

    registry.notify(EngineInitialized(registry, engine))
    registry.notify(DatabaseConfigured(registry, engine))



