FROM node:16
WORKDIR /app
COPY realWorld-server /app/
RUN npm clean-install
COPY entrypoint.sh /usr/local/bin/
RUN chmod 755 /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
CMD ["node", "api/index.js"]