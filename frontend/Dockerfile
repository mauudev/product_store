FROM node:14

WORKDIR /app
COPY . .

RUN npm install
RUN npm run build
EXPOSE 5173
CMD ["npm", "start"]
