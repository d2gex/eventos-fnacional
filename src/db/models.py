from src import config as cfg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship

db_path = f'sqlite:///{cfg.DB_PATH}/{cfg.DB_NAME}'
engine = create_engine(db_path)
db_session = sessionmaker(bind=engine, echo=True)

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


class ModelUbicacion (ModelBase):
    __tablename__ = 'ubicacion'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ciudad = Column(String, nullable=False, unique=True)


class ModelGanaderías (ModelBase):
    __tablename__ = 'ganaderías'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_ganadería = Column(String, nullable=False, unique=True)


class ModelToreros (ModelBase):
    __tablename__ = 'toreros'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=True)
    apellidos = Column(String, nullable=True)
    nombre_profesional = Column(String, nullable=True, unique=True)

    # Foreign keys
    tipo_toreros_id = Column(Integer, ForeignKey('tipo_toreros.id'))

    # relationships
    tipo_torero = relationship(ModelTipoToreros)
    torero_premios_festejo = relationship(ModelTipoPremios,
                                          secondary='torero_premios_festejos')


class ModelFestejos(ModelBase):
    __tablename__ = 'festejos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    celebracion = Column(DateTime, nullable=False)
    notas = Column(Text)

    toreros_premios_festejos = relationship('ModelTorerosPremiosFestejos',
                                            backref="torero_premios_festejos'")


class ModelTorerosPremiosFestejos (ModelBase):
    __tablename__ = 'torero_premios_festejos'
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Many to Many with TipoPremios and Toreros
    toreros_id = Column(
        Integer,
        ForeignKey('toreros.id'))
    festejos_id = Column(
        Integer,
        ForeignKey('festejos.id'))

    # M:1 with TipoPremios
    tipo_premios_id = Column(
        Integer,
        ForeignKey('tipo_premios.id'))
    tipo_premios = relationship(ModelTipoPremios)


