from src import config
from src.app import create_app
app = create_app(config.Config)
app.run(host='0.0.0.0', debug=False)