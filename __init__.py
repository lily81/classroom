from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

db = SQLAlchemy()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # 从config.py加载配置

    # 初始化扩展
    db.init_app(app)
    socketio.init_app(app)

    # 注册蓝图（如果有）
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app