## 安装虚拟环境

```sh
> python -m venv venv
> cd 'venv/Scripts'
> ./activate
> cd ..
> cd ..
```

## 安装依赖

```sh
(venv) > pip install -r requirements.txt
```

## 启动命令

```sh
(venv) > python main.py
```

## 打包命令

```sh
(venv) > Pyinstaller -F -w -i favicon.ico -n WorkerBee main.py
```
