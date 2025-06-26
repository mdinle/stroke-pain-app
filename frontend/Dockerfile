# Stage 1: build
FROM node:20-alpine as build-stage
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

# Stage 2: serve
FROM nginx:alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
