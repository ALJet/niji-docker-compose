FROM python:3.6.8

RUN mkdir /niji
#设置工作目录
WORKDIR /niji
#将当前目录加入到工作目录中
ADD . /niji
RUN pip install -r requeriments.txt -i https://pypi.douban.com/simple
RUN pip install cryptography
#对外暴露端口
EXPOSE 80 8080
#设置环境变量
ENV SPIDER=/niji
#复制operation到对应的目录下 因为python3 对应mysql报错问题
COPY operations.py /usr/local/lib/python3.6/site-packages/django/db/backends/mysql/operations.py
#复制boundfield.py到对应的目录下 因为要报错
COPY boundfield.py /usr/local/lib/python3.6/site-packages/django/forms/boundfield.py
