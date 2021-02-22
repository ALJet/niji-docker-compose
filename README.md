使用docker-compose一键部署项目 （Django + MySQL + Nginx）

将整个项目（niji）上传到服务器中 （已安装了docker 和docker-compose）
切换到niji目录中
使用docker-compose  build 编译项目
docker-compose up -d 后台启动容器

每个文件夹是对应的模块（nginx NijiTest ） pci为效果图片
每个文件夹中有对应的Dockerfile 


-----------------------------------
说一下NijiTest项目下的Dockerfile 其中的----
{
	#复制operation到对应的目录下 因为python3 对应mysql报错问题
	COPY operations.py /usr/local/lib/python3.6/site-packages/django/db/backends/mysql/operations.py
	#复制boundfield.py到对应的目录下 因为要报错
	COPY boundfield.py /usr/local/lib/python3.6/site-packages/django/forms/boundfield.py
}

安装环境后项目已启动就报错！我的解决方案就是把修改好的py文件覆盖到对应的报错py文件()
-----------------------------------
关于 nginx文件中的Dockerfile想说一下
{
	#删除原有的配置文件(没有删除 nginx.conf不会生效)
	RUN rm /etc/nginx/conf.d/default.conf
}
老是忘记删除原有的文件导致无法实现反向代理 找了很久 自己开个镜像进去测试 才发现没有删除原有的default.conf文件 注意注意 
