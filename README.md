# flask-scaffold
一个简单的flask脚手架

## 安装

克隆代码

```
git clone https://github.com/van23qf/flask-scaffold.git
cd flask-scaffold
```

安装依赖

```
pip install -r requirements.txt
```

环境配置

```
cp .env.copy .env
```

## 常用命令

 - python直接启动，适合本地开发调试

```
python app.py
```

 - gunicorn启动，适合生产环境

```
gunicorn app:app -c gunicorn.py --reload
```

 - 数据库迁移

```
# 生成迁移版本
flask db migrate -m "版本备注"
# 应用版本
flask db upgrade
```

## 目录说明

```
 - core 工具类库
 - logs 日志目录
 - migrations 数据库迁移目录
 - models 模型目录
 - static 前端资源文件
 - templates 前端模版
 - views 蓝图
```
