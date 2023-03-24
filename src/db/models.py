from src import config as cfg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine(f'sqlite:///{cfg.DB_PATH}/{cfg.DB_NAME}')
db_session = sessionmaker(bind=engine)

ModelBase = declarative_base()


class ModelTipoFestejos (ModelBase):
    __tablename__ = 'tipo_festejos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String, nullable=False, unique=True)


class ModelTipoToreros (ModelBase):
    __tablename__ = 'tipo_toreros'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_torero = Column(String, nullable=False, unique=True)


class ModelTipoPremios (ModelBase):
    __tablename__ = 'tipo_premios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_premio = Column(String, nullable=False, unique=True)
    toreros_id = relationship('ModelToreros', backref="users")


class ModelUbicacion (ModelBase):
    __tablename__ = 'ubicacion'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ciudad = Column(String, nullable=False, unique=True)


class ModelGanaderías (ModelBase):
    __tablename__ = 'ganaderías'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_ganadería = Column(String, nullable=False, unique=True)


class ModelToreros (ModelBase):
    __tablename__ = 'torereos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column (String, nullable=True)
    apellidos = Column(String, nullable=True)
    nombre_profesional = Column(String, nullable=True, unique=True)
    user_id = Column(Integer, ForeignKey('tipo_toreros.id'))
    user = relationship(ModelTipoToreros)
