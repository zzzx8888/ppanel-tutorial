# 📦 sing-box - 新一代跨平台代理工具

![sing-box](sing-box.png)

> 🌟 [sing-box](https://github.com/SagerNet/sing-box) 是一款新兴的跨平台代理软件，以其出色的性能、现代化的架构和完全免费的特性受到用户青睐。

## ✨ 产品亮点

### 🎯 核心优势

- 🆓 **完全免费**：开源项目，永久免费使用
- 🌍 **跨平台支持**：Windows、macOS、Linux、Android、iOS
- 🚀 **性能卓越**：基于 Go 语言开发，高性能架构
- 🔄 **持续更新**：活跃的开发团队，定期更新维护
- 🛡️ **安全可靠**：现代化安全机制，代码开源透明

### 🌟 特色功能

| 功能特性 | 说明 | 优势 |
|---------|------|------|
| 🎭 **多重入站** | 支持多种入站协议 | 灵活配置 |
| 🔀 **智能路由** | 强大的路由规则系统 | 精准分流 |
| 📊 **实时监控** | 详细的连接和流量统计 | 便于管理 |
| 🔧 **热重载** | 支持配置热重载 | 无需重启 |
| 🎯 **DNS 优化** | 内置 DNS 服务器 | 解析加速 |

### 🔗 协议支持

| 协议类型 | 支持状态 | 特性说明 |
|---------|----------|----------|
| 🔒 Shadowsocks | ✅ | 全功能支持，包括各种加密算法 |
| 🌟 VMess | ✅ | V2Ray 协议，功能完整 |
| 🛡️ Trojan | ✅ | TLS 伪装流量，安全可靠 |
| 🚀 Hysteria 2 | ✅ | 基于 QUIC 的高速协议 |
| ⚡ VLESS | ✅ | 轻量级协议，性能优秀 |
| 🔐 WireGuard | ✅ | 现代 VPN 协议 |
| 🌊 TUIC | ✅ | 基于 QUIC 的新协议 |

### 📱 系统要求

- **最低版本**：Android 5.0 (API 21) 及以上
- **推荐版本**：Android 8.0 及以上
- **适用设备**：安卓手机 / 平板电脑
- **架构支持**：ARM64、ARM、x86_64
- **存储需求**：约 80MB 可用空间
- **内存需求**：建议 2GB RAM 以上

---

## 📥 下载安装

### 🔗 官方发布

> 📌 **版本说明**：sing-box 提供 Android 版本叫做 SFA (sing-box for Android)

<!-- DOWNLOAD_TABLE_START -->

| 下载源 | 版本 | 说明 | 状态 |
|--------|------|------|------|
| GitHub Release | v1.13.16 | [下载链接](https://github.com/SagerNet/sing-box/releases/download/v1.13.16/SFA-1.13.16-legacy-android-5-universal.apk) | ✅ |
| 镜像加速1 (gh-proxy.org) | v1.13.16 | [下载链接](https://gh-proxy.org/https://github.com/SagerNet/sing-box/releases/download/v1.13.16/SFA-1.13.16-legacy-android-5-universal.apk) | ✅ |
| 镜像加速2 (hk.gh-proxy.org) | v1.13.16 | [下载链接](https://hk.gh-proxy.org/https://github.com/SagerNet/sing-box/releases/download/v1.13.16/SFA-1.13.16-legacy-android-5-universal.apk) | ✅ |
| 镜像加速3 (cdn.gh-proxy.org) | v1.13.16 | [下载链接](https://cdn.gh-proxy.org/https://github.com/SagerNet/sing-box/releases/download/v1.13.16/SFA-1.13.16-legacy-android-5-universal.apk) | ✅ |

<!-- DOWNLOAD_TABLE_END -->

### 🛠️ 安装指南

1. **准备工作**
   - 确保设备满足系统要求
   - 允许安装未知来源应用

2. **下载安装**
   - 选择合适的下载源
   - 下载 <!-- FILENAME_START -->`SFA-1.13.16-legacy-android-5-universal.apk`<!-- FILENAME_END --> 文件到设备
   - 点击文件开始安装

3. **权限授予**
   - 授予网络访问权限
   - 允许 VPN 连接权限（首次启动时）

---

## 🚀 使用教程

### 📋 快速开始

#### 🔥 配置流程

1. **📱 启动应用** - 打开 sing-box (SFA)
2. **📂 导入配置** - 添加配置文件或订阅
3. **🌐 选择服务器** - 从可用节点中选择
4. **🚀 启动服务** - 开启代理连接
5. **✅ 验证连接** - 确认网络代理正常

### 🎯 详细操作

#### 🌟 步骤一：应用启动

打开已安装的 sing-box，进入应用首页：

![应用首页](singbox-01.png)

> 💡 **首次启动提示**：应用会要求 VPN 权限，请选择"允许"

#### ⚙️ 步骤二：配置选项

点击"配置"或"Profiles"进入配置管理：

![配置选项](singbox-02.jpg)

#### 📥 步骤三：导入配置

选择导入方式（URL订阅、本地文件或手动配置）：

![导入过程](singbox-03.jpg)

#### ✅ 步骤四：配置确认

检查导入的配置信息，确认无误：

![配置确认](singbox-04.jpg)

#### 🌐 步骤五：节点选择

从可用节点列表中选择合适的服务器：

![节点选择](singbox-05.jpg)

#### 🚀 步骤六：启动连接

返回主界面，启动代理服务：

![连接状态](singbox-06.jpg)

---

## 🎛️ 高级配置

### 📊 路由规则

- **域名规则**：基于域名的智能分流
- **IP 规则**：基于目标 IP 的精确路由
- **GeoIP 规则**：基于地理位置的自动路由
- **进程规则**：基于应用进程的分流（需 root）

### 🔄 出站配置

- **直连模式**：流量直接连接目标
- **代理模式**：通过代理服务器转发
- **阻断模式**：阻止特定流量
- **DNS 模式**：仅进行 DNS 查询

### 📈 监控统计

- **实时流量**：显示当前网络速度
- **历史统计**：查看流量使用历史
- **连接信息**：显示活跃连接详情
- **日志记录**：详细的运行日志

---

## 🎯 配置示例

### 📝 基础配置

```json
{
  "inbounds": [
    {
      "type": "tun",
      "inet4_address": "172.19.0.1/30",
      "auto_route": true
    }
  ],
  "outbounds": [
    {
      "type": "shadowsocks",
      "server": "example.com",
      "server_port": 443,
      "method": "chacha20-ietf-poly1305",
      "password": "your_password"
    }
  ]
}
```

### 🎭 高级规则

```json
{
  "route": {
    "rules": [
      {
        "domain_suffix": [".cn"],
        "outbound": "direct"
      },
      {
        "geoip": "cn",
        "outbound": "direct"
      }
    ]
  }
}
```

---

## ❓ 常见问题

### 🔧 技术问题

**Q: 配置导入失败？**

A: 请检查：

- 配置文件格式是否正确
- 网络连接是否正常
- 是否使用了支持的协议

**Q: 连接不稳定？**

A: 优化建议：

- 尝试切换不同的服务器节点
- 检查本地网络环境
- 调整 TCP/UDP 设置

**Q: 耗电量大？**

A: 节能建议：

- 合理配置路由规则，减少不必要代理
- 选择延迟较低的服务器
- 在不需要时及时关闭服务

### 📱 应用问题

**Q: 无法启动？**

A: 排查步骤：

- 检查 Android 版本兼容性
- 确认有足够的存储空间
- 重启设备后再试

---

## 🔗 学习资源

### 📚 官方资源

- 🏠 [项目主页](https://github.com/SagerNet/sing-box)
- 📖 [官方文档](https://sing-box.sagernet.org/)
- 🎯 [配置示例](https://github.com/SagerNet/sing-box/tree/main/docs/examples)
- 🐛 [问题反馈](https://github.com/SagerNet/sing-box/issues)

### 💬 社区支持

- 🔗 [Telegram 群组](https://t.me/sagernet)
- 📢 [更新频道](https://t.me/sagernet_releases)
- 💭 [讨论社区](https://github.com/SagerNet/sing-box/discussions)

### 🛠️ 开发资源

- 📋 [API 文档](https://sing-box.sagernet.org/configuration/)
- 🔧 [插件开发](https://github.com/SagerNet/sing-box)
- 🎨 [UI 组件](https://github.com/SagerNet/sing-box-for-android)

---

## 💡 最佳实践

### ⚡ 性能优化

1. **合理配置规则**：避免所有流量都走代理
2. **选择就近节点**：选择地理位置较近的服务器
3. **定期更新**：保持应用和规则的最新版本

### 🛡️ 安全建议

1. **验证配置来源**：仅使用可信的配置提供商
2. **定期备份**：备份重要的配置文件
3. **监控流量**：注意异常的流量使用情况

---

> 📅 最后更新：<!-- UPDATE_TIME_START -->2026-08-05<!-- UPDATE_TIME_END --> | 📦 适用版本：sing-box <!-- VERSION_START -->v1.13.16<!-- VERSION_END --> (SFA)
