# Web image: Nginx as reverse proxy in front of the app service.
FROM nginx:1.27-alpine

# Replace default config with our reverse-proxy config
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/app.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]