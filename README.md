# 微服务示例项目

这是一个简单的微服务示例项目，用于演示微服务架构的开发和部署流程。

## 项目结构

- `app.py`: Flask 应用主文件
- `requirements.txt`: Python 依赖文件
- `Dockerfile`: 容器化配置文件
- `k8s/`: Kubernetes 部署文件目录
  - `deployment.yaml`: 部署配置
  - `service.yaml`: 服务配置

## 本地开发

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行应用：
```bash
python app.py
```

## 构建 Docker 镜像

```bash
docker build -t your-docker-registry/microservice:latest .
```

## Kubernetes 部署

1. 确保已配置 kubectl 并连接到正确的集群
2. 部署服务：
```bash
kubectl apply -f k8s/
```

## API 端点

- `GET /health`: 健康检查
- `GET /api/v1/hello`: 示例 API 端点 