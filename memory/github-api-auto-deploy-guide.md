# GitHub API 自动部署指南（2026 年版）🐙

**学习笔记日期：** 2026-03-30
**学习目的：** 为哈基偷的 UI/UX 知识库网页自动部署做准备
**分析师：** 哈基偷 🐱

---

## 一、核心概述

**学习目标：**
- 通过 GitHub API 自动创建仓库
- 自动推送 HTML 文件到仓库
- 配合 Cloudflare Pages 实现自动部署
- 每日自动更新网页内容

**技术栈：**
- GitHub API（REST API v3）
- Personal Access Token（PAT）认证
- Python requests 库
- Cloudflare Pages（自动构建部署）

---

## 二、GitHub Personal Access Token 配置

### 2.1 令牌类型选择

| 类型 | 细粒度（Fine-grained） | 经典（Classic） |
|------|------------------------|-----------------|
| **安全性** | ⭐⭐⭐⭐⭐（推荐） | ⭐⭐⭐ |
| **权限控制** | 可限制特定仓库 | 所有有权限的仓库 |
| **兼容性** | 较新，部分功能不支持 | 兼容所有 API |
| **推荐场景** | 自动化任务/CI/CD | 临时任务/旧工具 |

**哈基偷推荐：** 细粒度令牌（Fine-grained）— 更安全，符合最小权限原则

---

### 2.2 创建细粒度令牌步骤

**第 1 步：进入设置页面**
```
登录 GitHub → 点击右上角头像 → Settings
→ 左侧边栏 Developer settings
→ Personal access tokens → Fine-grained tokens
```

**第 2 步：填写令牌信息**

| 字段 | 推荐值 | 说明 |
|------|--------|------|
| Token name | `HajiTou-Deploy-Token` | 易识别的名称 |
| Expiration | 90 天 | 定期轮换更安全 |
| Description | `哈基偷自动部署 UI/UX 知识库` | 用途说明 |
| Resource owner | 老大的 GitHub 用户名 | 令牌所属用户 |
| Repository access | `Only select repositories` | 仅选定仓库（更安全） |

**第 3 步：配置权限（Permissions）**

| 权限类别 | 权限项 | 访问级别 | 说明 |
|----------|--------|----------|------|
| **Contents** | `contents` | Read and write | 读写仓库内容（必需） |
| **Deployments** | `deployments` | Read and write | 部署控制（可选） |
| **Pages** | `pages` | Read and write | GitHub Pages 部署（可选） |
| **Workflows** | `workflows` | Read and write | GitHub Actions（可选） |

**第 4 步：生成令牌**
- 点击 `Generate token`
- **立刻复制并保存**（离开页面后无法再次查看！）
- 存入安全位置（如密码管理器）

---

### 2.3 经典令牌（备用方案）

**如果细粒度令牌不兼容，使用经典令牌：**

**Scopes 选择：**
- ✅ `repo` — 完整控制私有仓库（必需）
- ✅ `workflow` — 管理 GitHub Actions（可选）
- ✅ `delete_repo` — 删除仓库（谨慎勾选）

**路径：**
```
Developer settings → Personal access tokens → Tokens (classic)
→ Generate new token (classic)
```

---

## 三、GitHub API 核心接口

### 3.1 创建仓库

**API 端点：**
```
POST https://api.github.com/user/repos
```

**请求头：**
```python
headers = {
    "Authorization": "Bearer YOUR_PAT_TOKEN",
    "Accept": "application/vnd.github.v3+json"
}
```

**请求体：**
```python
data = {
    "name": "haji-tou-ui-ux-knowledge-base",
    "description": "哈基偷的 UI/UX 设计知识库",
    "private": False,  # 公开仓库（GitHub Pages 免费）
    "auto_init": True,  # 自动创建 README
    "has_pages": True   # 启用 GitHub Pages（可选）
}
```

**响应示例：**
```json
{
  "id": 123456789,
  "name": "haji-tou-ui-ux-knowledge-base",
  "full_name": "username/haji-tou-ui-ux-knowledge-base",
  "html_url": "https://github.com/username/haji-tou-ui-ux-knowledge-base",
  "git_url": "git://github.com/username/haji-tou-ui-ux-knowledge-base.git",
  "ssh_url": "git@github.com:username/haji-tou-ui-ux-knowledge-base.git",
  "clone_url": "https://github.com/username/haji-tou-ui-ux-knowledge-base.git"
}
```

---

### 3.2 创建/更新文件

**API 端点：**
```
PUT https://api.github.com/repos/{owner}/{repo}/contents/{path}
```

**请求体：**
```python
data = {
    "message": "Update UI/UX knowledge base - 2026-03-30",
    "content": base64_encoded_content,  # 文件内容需 Base64 编码
    "branch": "main"  # 分支名
}
```

**Python 示例：**
```python
import requests
import base64

def upload_file(token, owner, repo, path, content, message):
    """上传/更新文件到 GitHub 仓库"""
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Base64 编码内容
    encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    
    data = {
        "message": message,
        "content": encoded_content,
        "branch": "main"
    }
    
    response = requests.put(url, headers=headers, json=data)
    
    if response.status_code in [200, 201]:
        print(f"✅ 文件上传成功：{path}")
        return True
    else:
        print(f"❌ 上传失败：{response.status_code}")
        print(response.json())
        return False
```

---

### 3.3 获取文件 SHA（用于更新）

**如果要更新已有文件，需要先获取 SHA：**

**API 端点：**
```
GET https://api.github.com/repos/{owner}/{repo}/contents/{path}
```

**响应：**
```json
{
  "type": "file",
  "encoding": "base64",
  "size": 1234,
  "name": "index.html",
  "path": "index.html",
  "sha": "abc123def456...",  # ← 需要这个 SHA
  "download_url": "https://raw.githubusercontent.com/..."
}
```

**更新文件时需要包含 SHA：**
```python
data = {
    "message": "Update index.html",
    "content": encoded_content,
    "sha": "abc123def456...",  # ← 必需
    "branch": "main"
}
```

---

## 四、完整自动化脚本

### 4.1 哈基偷的部署脚本（Python）

```python
#!/usr/bin/env python3
"""
哈基偷的 GitHub 自动部署脚本
功能：将 UI/UX 知识库 HTML 文件推送到 GitHub 仓库
"""

import requests
import base64
import os
from datetime import datetime

class GitHubDeployer:
    def __init__(self, token, owner, repo):
        self.token = token
        self.owner = owner
        self.repo = repo
        self.base_url = f"https://api.github.com/repos/{owner}/{repo}/contents"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    def get_file_sha(self, path):
        """获取文件 SHA（用于更新）"""
        url = f"{self.base_url}/{path}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json().get("sha")
        return None
    
    def upload_file(self, path, content, message):
        """上传/更新文件"""
        url = f"{self.base_url}/{path}"
        
        # Base64 编码
        encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')
        
        # 准备数据
        data = {
            "message": message,
            "content": encoded_content,
            "branch": "main"
        }
        
        # 如果是更新，需要 SHA
        sha = self.get_file_sha(path)
        if sha:
            data["sha"] = sha
        
        # 发送请求
        response = requests.put(url, headers=self.headers, json=data)
        
        if response.status_code in [200, 201]:
            print(f"✅ 上传成功：{path}")
            return True
        else:
            print(f"❌ 上传失败：{path}")
            print(response.json())
            return False
    
    def deploy_knowledge_base(self, html_files):
        """部署知识库（多个 HTML 文件）"""
        today = datetime.now().strftime("%Y-%m-%d")
        success_count = 0
        
        for file_path, content in html_files.items():
            message = f"Update {file_path} - {today} by Haji Tou 🐱"
            if self.upload_file(file_path, content, message):
                success_count += 1
        
        print(f"\n📊 部署完成：{success_count}/{len(html_files)} 文件成功")
        return success_count == len(html_files)

# 使用示例
if __name__ == "__main__":
    # 配置（从环境变量读取，更安全）
    TOKEN = os.getenv("GITHUB_PAT_TOKEN")
    OWNER = "your-github-username"
    REPO = "haji-tou-ui-ux-knowledge-base"
    
    # 初始化部署器
    deployer = GitHubDeployer(TOKEN, OWNER, REPO)
    
    # 准备文件（示例）
    html_files = {
        "index.html": """<!DOCTYPE html>
<html><head><title>哈基偷的 UI/UX 知识库</title></head>
<body><h1>哈基偷的 UI/UX 设计知识库 🐱</h1>
<p>最后更新：2026-03-30</p>
</body></html>""",
        "ui-ux-knowledge-base.html": open("ui-ux-knowledge-base.html", "r").read(),
    }
    
    # 部署
    deployer.deploy_knowledge_base(html_files)
```

---

### 4.2 环境变量配置（安全）

**不要硬编码 Token！使用环境变量：**

**macOS/Linux：**
```bash
# 添加到 ~/.zshrc 或 ~/.bashrc
export GITHUB_PAT_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxx"

# 生效
source ~/.zshrc
```

**验证：**
```bash
echo $GITHUB_PAT_TOKEN
```

**Python 读取：**
```python
import os
TOKEN = os.getenv("GITHUB_PAT_TOKEN")
```

---

## 五、Cloudflare Pages 集成

### 5.1 部署流程

```
哈基偷 Python 脚本
    ↓ (GitHub API)
GitHub 仓库（main 分支）
    ↓ (Webhook 自动触发)
Cloudflare Pages
    ↓ (自动构建)
CDN 全球分发
    ↓
用户访问 https://haji-tou.pages.dev
```

### 5.2 Cloudflare Pages 配置

**第 1 步：登录 Cloudflare**
- 访问 https://pages.cloudflare.com
- 登录账号（免费）

**第 2 步：创建项目**
- 点击 `Create a project`
- 选择 `Connect to Git`
- 授权 GitHub 账号

**第 3 步：选择仓库**
- 选择 `haji-tou-ui-ux-knowledge-base`
- 点击 `Begin setup`

**第 4 步：构建设置**

| 设置项 | 值 | 说明 |
|--------|-----|------|
| Production branch | `main` | 生产分支 |
| Build command | （留空） | 静态 HTML 无需构建 |
| Build output directory | `/` | 根目录（或 `/dist`） |

**第 5 步：部署**
- 点击 `Save and Deploy`
- 等待构建完成（约 30 秒）
- 获得临时域名：`haji-tou-ui-ux-knowledge-base.pages.dev`

### 5.3 自定义域名（可选）

**前提：**
- 域名已添加到 Cloudflare
- DNS 由 Cloudflare 管理

**步骤：**
1. Cloudflare Pages → 项目 → `Custom domains`
2. 点击 `Add a custom domain`
3. 输入域名（如 `haji-tou.com`）
4. 自动配置 DNS（CNAME 记录）
5. 等待 SSL 证书签发（约 5 分钟）

---

## 六、每日自动更新流程

### 6.1 哈基偷的自动化方案

**方案 A：哈基偷主动推送（推荐）**

```
每小时 heartbeat 检查
    ↓
哈基偷决定更新内容
    ↓
调用 Python 脚本（GitHub API）
    ↓
推送到 GitHub 仓库
    ↓
Cloudflare Pages 自动部署
    ↓
网页更新完成
```

**优点：**
- ✅ 哈基偷完全控制
- ✅ 可以智能决定更新内容
- ✅ 不需要额外服务器

**缺点：**
- ⚠️ 需要哈基偷主动触发

---

**方案 B：GitHub Actions 定时任务**

```yaml
# .github/workflows/daily-update.yml
name: Daily Update

on:
  schedule:
    - cron: '0 0 * * *'  # 每天 UTC 0:00（北京时间 8:00）
  workflow_dispatch:  # 手动触发

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Update content
        run: |
          # 在这里运行更新脚本
          python update_script.py
      
      - name: Commit and push
        run: |
          git config --global user.name "Haji Tou Bot"
          git config --global user.email "haji-tou@bot.local"
          git add .
          git commit -m "Daily update by Haji Tou Bot 🐱"
          git push
```

**优点：**
- ✅ 完全自动化
- ✅ 定时执行

**缺点：**
- ⚠️ 需要仓库中有脚本
- ⚠️ 不够灵活（固定时间更新）

---

### 6.2 哈基偷的推荐方案

**混合方案：哈基偷主动 + Actions 兜底**

1. **日常：** 哈基偷在自由行动时主动更新（灵活）
2. **兜底：** GitHub Actions 每天检查，如果哈基偷忘记则自动更新

**实现：**
```python
# 哈基偷的自由行动脚本中集成
def daily_update_check():
    """检查今日是否已更新，如未更新则推送"""
    today = datetime.now().strftime("%Y-%m-%d")
    last_update = get_last_commit_date()
    
    if last_update != today:
        print("📅 今日尚未更新，开始部署...")
        deploy_knowledge_base()
    else:
        print("✅ 今日已更新，跳过")
```

---

## 七、安全最佳实践

### 7.1 Token 安全

| ✅ 推荐 | ❌ 避免 |
|--------|--------|
| 使用细粒度令牌 | 使用经典令牌（权限过大） |
| 设置 90 天过期 | 永不过期 |
| 存入环境变量 | 硬编码在代码中 |
| 定期轮换 | 一个令牌用到底 |
| 仅授予必要权限 | 授予全部权限 |

### 7.2 仓库安全

| ✅ 推荐 | ❌ 避免 |
|--------|--------|
| 公开仓库（GitHub Pages 免费） | 私有仓库（Pages 需付费） |
| 启用 Branch Protection | 允许直接推送 main 分支 |
| 使用 .gitignore 忽略敏感文件 | 提交 Token/密码 |
| 定期审计访问日志 | 从不检查日志 |

---

## 八、哈基偷的实施计划

### 8.1 准备阶段（第 1 天）

- [ ] 老大确认有 GitHub 账号（没有则注册）
- [ ] 创建 Fine-grained PAT Token
- [ ] 创建 GitHub 仓库（公开）
- [ ] 配置 Cloudflare Pages（关联仓库）
- [ ] 测试手动部署

### 8.2 开发阶段（第 2-3 天）

- [ ] 哈基偷学习 Python GitHub API 调用
- [ ] 编写部署脚本
- [ ] 测试自动推送
- [ ] 验证 Cloudflare 自动部署

### 8.3 运行阶段（第 4 天起）

- [ ] 哈基偷每日自由行动时更新
- [ ] 可选：配置 GitHub Actions 兜底
- [ ] 监控访问统计（可选）
- [ ] 根据反馈优化内容

---

## 九、常见问题解答

### Q1: GitHub Pages 和 Cloudflare Pages 选哪个？

**A:** 推荐 Cloudflare Pages：
- 国内访问更快（CDN 节点多）
- 构建速度更快
- 免费额度更充足

### Q2: 需要备案吗？

**A:** 不需要：
- 使用 `.pages.dev` 域名无需备案
- 使用自定义域名（.com/.cn）如果服务器在海外也无需备案

### Q3: 访问统计怎么加？

**A:** 推荐无 Cookie 的统计工具：
- Umami（开源，可自托管）
- Plausible（付费，隐私友好）
- Cloudflare Web Analytics（免费，集成在 Cloudflare）

### Q4: 哈基偷没有 Python 环境怎么办？

**A:** 哈基偷可以用：
- OpenClaw 的 `exec` 工具运行 Python 脚本
- 或者直接用 `requests` 库（uv 已捆绑）

---

## 十、相关资源

**官方文档：**
- [GitHub REST API](https://docs.github.com/en/rest)
- [GitHub Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- [Cloudflare Pages](https://pages.cloudflare.com/)

**哈基偷的学习笔记：**
- `memory/ui-ux-knowledge-base.html` — UI/UX 知识库 HTML
- `memory/ui-ux-case-study-figma-2026.md` — Figma 案例分析
- `memory/ui-ux-case-study-linear-2026.md` — Linear 案例分析
- `memory/ui-ux-case-study-stripe-2026.md` — Stripe 案例分析
- `memory/ui-ux-case-study-notion-2026.md` — Notion 案例分析

---

_哈基偷的 GitHub API 学习笔记完成！现在可以为老大的 UI/UX 知识库网页做自动部署准备了喵～ 🐱💙_

**下一步：** 等老大确认 GitHub 账号和 Token 配置，哈基偷就可以开始实施部署了！
