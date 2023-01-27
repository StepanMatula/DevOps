# syntax=docker/dockerfile-upstream:master-labs
FROM node:16 as fe-builder
COPY ts-redux-react-realworld-example-app /app
WORKDIR /app
RUN npm clean-install
RUN npm run build

FROM nginx:latest
COPY --from=fe-builder /app/build /usr/share/nginx/html