from flask import Blueprint, render_template
from flask_socketio import emit
from . import socketio

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

# WebSocket事件处理
@socketio.on('message')
def handle_message(data):
    emit('message', data, broadcast=True)  # 广播消息给所有客户端