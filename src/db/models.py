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


class ModelTipoFestejos(ModelBase):
    __tablename__ = 'tipo_festejos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String, nullable=False, unique=True)
    festejos = relationship('ModelFestejos', backref="festejos")


class ModelTipoToreros(ModelBase):
    __tablename__ = 'tipo_toreros'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_torero = Column(String, nullable=False, unique=True)
    toreros = relationship('ModelToreros', backref="toreros")


class ModelTipoPremios(ModelBase):
    __tablename__ = 'tipo_premios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_premio = Column(String, nullable=False, unique=True)
    torero_premios_festejos = relationship('ModelToreros',
                                           secondary='torero_premios_festejos')


class ModelPoblacion(ModelBase):
    __tablename__ = 'poblacion'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ciudad = Column(String, nullable=False, unique=True)
    provincia_id = Column(
        Integer,
        ForeignKey('provincia.id'))
    provincia = relationship('ModelProvincia')


class ModelProvincia(ModelBase):
    __tablename__ = 'provincia'

    id = Column(Integer, primary_key=True, autoincrement=True)
    provincia = Column(String, nullable=False, unique=True)
    poblacion = relationship(ModelPoblacion, backref="poblacion")
    ganaderias = relationship('ModelGanaderias', backref="ganaderias")


class ModelGanaderias(ModelBase):
    __tablename__ = 'ganaderias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_ganaderia = Column(String, nullable=False, unique=True)
    provincia_id = Column(
        Integer,
        ForeignKey('provincia.id'))
    provincia = relationship('ModelProvincia')
    ganaderias_festejos = relationship('ModelFestejos',
                                       secondary="ganaderias_festejos")


class ModelToreros(ModelBase):
    __tablename__ = 'toreros'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=True)
    apellidos = Column(String, nullable=True)
    nombre_profesional = Column(String, nullable=True, unique=True)

    tipo_toreros_id = Column(Integer, ForeignKey('tipo_toreros.id'))
    tipo_torero = relationship(ModelTipoToreros)

    torero_premios_festejos = relationship(ModelTipoPremios,
                                           secondary='torero_premios_festejos')


class ModelFestejos(ModelBase):
    __tablename__ = 'festejos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    celebracion = Column(DateTime, nullable=False)
    notas = Column(Text)

    # M: 1 relationships
    poblacion_id = Column(
        Integer,
        ForeignKey('poblacion.id'))
    poblacion = relationship(ModelPoblacion)
    tipo_festejos_id = Column(
        Integer,
        ForeignKey('tipo_festejos.id'))
    tipo_festejo = relationship(ModelTipoFestejos)

    # M:M relationships
    toreros_premios_festejos = relationship(ModelTipoPremios,
                                            backref="torero_premios_festejos")
    ganaderias_festejos = relationship(ModelGanaderias,
                                       backref="ganaderias_festejos")


class ModelTorerosPremiosFestejos(ModelBase):
    __tablename__ = 'toreros_premios_festejos'
    id = Column(Integer, primary_key=True, autoincrement=True)

    # M:M
    toreros_id = Column(
        Integer,
        ForeignKey('toreros.id'))
    festejos_id = Column(
        Integer,
        ForeignKey('festejos.id'))
    # M: 1
    tipo_premios_id = Column(
        Integer,
        ForeignKey('tipo_premios.id'))
    tipo_premios = relationship(ModelTipoPremios)


class ModelGanaderiasFestejos(ModelBase):
    __tablename__ = 'ganaderias_festejos'
    id = Column(Integer, primary_key=True, autoincrement=True)

    # M:M
    ganaderias_id = Column(
        Integer,
        ForeignKey('ganaderias.id'))
    festejos_id = Column(
        Integer,
        ForeignKey('festejos.id'))
