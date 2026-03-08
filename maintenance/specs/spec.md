# 项目维护工具开发规格说明书

## 1. 项目概述

本项目旨在为 `ppanel-tutorial` 教程提供一套自动化的维护工具，用于动态更新教程中引用的第三方软件（如 Clash Meta for Android 等）的版本信息、下载链接、安装包名称及最后更新时间。工具将自动检测 GitHub 最新版本，生成官方及镜像加速下载链接，验证链接可用性，并更新对应的 Markdown 文档。

## 2. 技术架构

- **编程语言**: Python 3.x
- **配置文件**: YAML (`config.yaml`)
- **运行环境**: 本地运行 或 GitHub Actions (CI/CD)
- **依赖库**: `requests` (网络请求), `pyyaml` (配置解析), `jinja2` (可选，用于复杂的模板渲染，暂定直接字符串拼接)

## 3. 目录结构

```text
ppanel-tutorial/
├── maintenance/                # 维护工具目录
│   ├── specs/                  # 规格说明书 (本目录)
│   ├── config.yaml             # 核心配置文件
│   ├── main.py                 # 主程序入口
│   ├── requirements.txt        # Python 依赖
│   └── utils/                  # 工具模块
│       ├── github_client.py    # GitHub API 交互
│       ├── link_checker.py     # 链接可用性检测
│       └── markdown_editor.py  # Markdown 文件更新
└── ...
```

## 4. 核心功能模块

### 4.1 配置管理 (`config.yaml`)

配置文件定义需要监控的应用列表及其对应的文档位置。

```yaml
# 镜像源配置
mirrors:
  - name: "GitHub Release"
    url_template: "{url}"  # 原始链接
    check_availability: false # 官方源通常不检查或作为基准
  - name: "Mirror 1 (gh-proxy)"
    url_template: "https://gh-proxy.com/{url}"
    check_availability: true

# 应用列表
apps:
  - id: "clash-meta-android"
    name: "Clash Meta for Android"
    repo: "MetaCubeX/ClashMetaForAndroid"
    prerelease: true  # 是否允许预发布版本
    asset_filter: "universal-release.apk" # 用于筛选 Release Assets 的关键词或正则
    target_files:
      - path: "zh-CN/android/clash-meta-for-android.md"
        markers:
          version: "<!-- VERSION_START -->{}<!-- VERSION_END -->"
          filename: "<!-- FILENAME_START -->{}<!-- FILENAME_END -->"
          download_table: "<!-- DOWNLOAD_TABLE_START -->\n{}\n<!-- DOWNLOAD_TABLE_END -->"
          last_updated: "<!-- UPDATE_TIME_START -->{}<!-- UPDATE_TIME_END -->"
```

### 4.2 GitHub 版本获取 (`github_client.py`)

- 使用 GitHub API 获取指定仓库的 Latest Release 或 Latest Prerelease。
- 提取版本号 (Tag Name)。
- 提取符合 `asset_filter` 的下载链接 (Browser Download URL)。
- 提取发布时间。

### 4.3 链接生成与检测 (`link_checker.py`)

- 根据 `config.yaml` 中的 `mirrors` 模板生成所有下载链接。
- 对生成的链接发起 `HEAD` 请求。
- 记录响应状态码，判断是否可用 (HTTP 200/302)。
- 超时设置：5秒。

### 4.4 文档更新 (`markdown_editor.py`)

- 读取目标 Markdown 文件。
- 使用正则表达式查找并替换 Marker 标记的内容。
- **下载表格生成**: 动态生成 Markdown 表格，包含源名称、版本、链接（带超链接）、状态（✅/❌）。
- **版本号/文件名替换**: 更新正文中的具体文本。
- **时间戳更新**: 更新“最后更新时间”。

## 5. 文档标记规范

为了实现精准替换，需在 Markdown 文件中插入 HTML 注释作为锚点：

- **版本号**: `<!-- VERSION_START -->2.11.23<!-- VERSION_END -->`
- **文件名**: `<!-- FILENAME_START -->cmfa-2.11.23-universal-release.apk<!-- FILENAME_END -->`
- **下载表格**:
  ```markdown
  <!-- DOWNLOAD_TABLE_START -->
  | 下载源 | 版本 | 说明 | 状态 |
  |--------|------|------|------|
  | ... | ... | ... | ... |
  <!-- DOWNLOAD_TABLE_END -->
  ```
- **最后更新时间**: `<!-- UPDATE_TIME_START -->2025-07-10<!-- UPDATE_TIME_END -->`

## 6. 开发流程

1.  初始化目录和依赖。
2.  编写 `config.yaml` 示例。
3.  实现 GitHub API 获取逻辑。
4.  实现链接检测逻辑。
5.  实现 Markdown 替换逻辑。
6.  修改 `clash-meta-for-android.md` 添加标记。
7.  集成测试。
