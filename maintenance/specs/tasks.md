# 开发任务清单 (Tasks)

## 阶段 1: 基础设施搭建
- [ ] **创建项目结构**:
  - 创建 `maintenance` 目录。
  - 创建 `requirements.txt` (包含 `requests`, `pyyaml`)。
  - 创建 `README.md` (说明如何使用)。

## 阶段 2: 核心功能实现
- [ ] **实现配置读取**:
  - 创建 `config.yaml` 模板。
  - 编写配置加载函数。
- [ ] **实现 GitHub API 获取**:
  - 编写 `fetch_release.py`。
  - 获取 Release Tag、发布时间、特定 Asset 的下载链接。
- [ ] **实现镜像链接生成与检测**:
  - 编写 `check_links.py`。
  - 根据模板生成所有下载链接。
  - 验证每个链接的可用性 (HEAD request)。

## 阶段 3: Markdown 更新模块
- [ ] **实现文件替换逻辑**:
  - 编写 `update_markdown.py`。
  - 使用正则替换 HTML 注释标记之间的内容。
- [ ] **实现下载表格生成**:
  - 动态生成 Markdown 格式的表格。
  - 包含状态指示符 (✅/❌)。

## 阶段 4: 集成与测试
- [ ] **迁移现有文档**:
  - 修改 `zh-CN/android/clash-meta-for-android.md`，添加 HTML 注释标记。
- [ ] **运行完整流程**:
  - 运行脚本，确认所有标记被正确更新。
  - 确认生成的链接有效。
- [ ] **验证**:
  - 检查生成的 Markdown 文件格式是否正确。
  - 检查版本号、文件名是否一致。

## 阶段 5: CI/CD 配置 (可选/后续)
- [ ] **创建 GitHub Action Workflow**:
  - 配置定时任务 (Cron)。
  - 配置自动提交变更。
