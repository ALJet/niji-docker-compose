FROM nginx
#对外暴露端口
EXPOSE 80 8000
#删除原有的配置文件(没有删除 nginx.conf不会生效)
RUN rm /etc/nginx/conf.d/default.conf
ADD nginx.conf  /etc/nginx/conf.d/
RUN mkdir -p /usr/share/nginx/html/static
RUN mkdir -p /usr/share/nginx/html/media
