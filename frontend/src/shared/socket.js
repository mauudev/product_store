import io from "socket.io-client";

const createWebSocketConnection = () => {
  const socket = io("http://localhost:8000");

  return new Promise((resolve, reject) => {
    socket.on("connect", () => {
      console.log("Connected to the socket server ..");
      resolve(socket);
    });

    socket.on("connect_error", (error) => {
      console.error("Error when connecting to the socket server:", error);
      reject(error);
    });
  });
};

const createSocketChannel = (socket) => {
  return eventChannel((emit) => {
    const stockResponseHandler = (event) => {
      emit(event.payload);
    };

    const errorHandler = (errorEvent) => {
      emit(new Error(errorEvent.reason));
    };

    socket.on("stockReply", stockResponseHandler);
    socket.on("error", errorHandler);

    const unsubscribe = () => {
      socket.off("stockReply", stockResponseHandler);
    };

    return unsubscribe;
  });
};

export { createWebSocketConnection, createSocketChannel };
