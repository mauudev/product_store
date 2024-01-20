FROM node:20-alpine3.18 as build
WORKDIR /usr/src
COPY . /usr/src
RUN npm i
RUN npm run build

FROM nginx:1.23.1-alpine
EXPOSE 80
COPY ./nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build /usr/src/dist /usr/share/nginx/html
