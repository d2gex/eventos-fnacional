from src.db import utils as utils_db
from src.db import models
from src import config


def init_database():
    models.ModelBase.metadata.drop_all(utils_db.engine)
    models.ModelBase.metadata.create_all(utils_db.engine)


def init_tipo_torero():
    db_data = [models.ModelTipoTorero(tipo_torero=x) for x in ['Torero', 'Rejoneador']]
    with utils_db.session_scope() as dbs:
        dbs.add_all(db_data)


if __name__ == "__main__":
    print("Start setting the database ....")
    if config.Config.CREATE_DATABASE:
        print("-----------> Creating the database")
        init_database()
    print("-----------> Adding initial tipo toreros")
    init_tipo_torero()
    print("... Database set up")
