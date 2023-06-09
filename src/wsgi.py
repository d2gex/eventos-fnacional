from src.app import create_app
from src.config import Config
app = create_app(config_class=Config)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
