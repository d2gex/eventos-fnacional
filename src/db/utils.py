from src import config as cfg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

db_path = f"sqlite:///{cfg.DB_PATH}/{cfg.Config.DB_NAME}"
engine = create_engine(db_path, echo=True)
db_session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = db_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
