import socketio

sio = socketio.AsyncServer(cors_allowed_origins="*", async_mode="asgi")
get_sio_instance = lambda: sio
