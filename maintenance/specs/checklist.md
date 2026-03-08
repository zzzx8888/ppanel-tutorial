# 开发检查清单 (Checklist)

## 1. 基础环境
- [ ] 创建 `maintenance/` 目录。
- [ ] 创建 `maintenance/requirements.txt` (包含 `requests`, `pyyaml`)。
- [ ] 创建 `maintenance/config.yaml` 配置文件模板。

## 2. 核心模块实现
- [ ] 实现 `fetch_latest_release(repo, prerelease=True)` 函数：
  - [ ] 成功调用 GitHub API。
  - [ ] 正确提取 Tag Name (版本号)。
  - [ ] 正确提取 Asset Download URL (正则匹配)。
  - [ ] 正确提取 Published At (发布时间)。

- [ ] 实现 `generate_mirror_links(url, mirrors)` 函数：
  - [ ] 生成正确的镜像 URL。

- [ ] 实现 `check_link_status(url)` 函数：
  - [ ] 发送 HEAD 请求。
  - [ ] 返回 HTTP 状态码 (200/302/404)。
  - [ ] 处理请求异常 (Timeout/ConnectionError)。

## 3. Markdown 更新逻辑
- [ ] 实现 `update_markdown_file(filepath, release_info)` 函数：
  - [ ] 能够定位 `<!-- VERSION_START -->...<!-- VERSION_END -->`。
  - [ ] 能够定位 `<!-- FILENAME_START -->...<!-- FILENAME_END -->`。
  - [ ] 能够定位 `<!-- DOWNLOAD_TABLE_START -->...<!-- DOWNLOAD_TABLE_END -->`。
  - [ ] 能够定位 `<!-- UPDATE_TIME_START -->...<!-- UPDATE_TIME_END -->`。
  - [ ] 替换内容后保持文件其他部分不变。

## 4. 集成验证
- [ ] 修改 `zh-CN/android/clash-meta-for-android.md`：
  - [ ] 插入 HTML 注释标记。
- [ ] 运行脚本 `python maintenance/main.py`：
  - [ ] 脚本无报错退出。
  - [ ] `clash-meta-for-android.md` 内容被更新为 GitHub 最新版本。
  - [ ] 检查表格中的链接是否有效。
