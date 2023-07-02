import os

from app import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    from flask_script import Manager
    manager = Manager(app)
    manager.run()
