# 星河旅游后台服务

### 架框设计
###### python版本
3.7
###### 支撑框架
bottle
###### config
主要是配置信息，全局常量文件

### 激活本地虚拟环境
```sh
source venv/bin/activate
```

### nginx
- [Mac安装和配置](https://www.jianshu.com/p/fc1e81efc867)
- 启动
```sh
nginx
```
- 停止
```sh
nginx -s stop
```
- 重启
```sh
nginx -s reload
```
- 检查nginx配置
```sh
nginx -t
```
- 查日志
```sh
cd /usr/local/var/log/nginx
tail -f access.log
tail -f error.log
```