# ⚔️ Clash Verge - 现代化跨平台代理客户端

> 🌟 [Clash Verge](https://github.com/clash-verge-rev/clash-verge-rev) 是基于 Clash 内核的现代化图形界面客户端，为 macOS 用户提供了美观易用的代理解决方案。

## ✨ 产品特色

### 🎯 核心优势

- 🆓 **完全免费**：开源软件，永久免费使用
- 🎨 **界面现代**：基于现代前端技术的美观界面
- 🌍 **跨平台**：支持 Windows、Linux、macOS
- 🔧 **功能强大**：基于成熟的 Clash 内核
- 🔄 **持续更新**：活跃的社区开发和维护

### 🛠️ 功能特性

| 功能模块 | 具体功能 | 优势特点 |
|---------|----------|----------|
| 🎛️ **代理核心** | Clash Meta 内核 | 性能强劲，功能完整 |
| 📊 **流量监控** | 实时流量统计 | 详细的网络使用分析 |
| 🎯 **规则分流** | 智能分流系统 | 国内外流量自动分流 |
| 🔄 **策略组** | 多种策略模式 | 自动选择、手动选择等 |
| 🎨 **主题定制** | 多种界面主题 | 个性化视觉体验 |
| ⚙️ **配置管理** | 订阅和本地配置 | 灵活的配置方式 |

### 📋 系统要求

- **最低版本**：macOS 10.15 Catalina 或更高版本
- **推荐版本**：macOS 12.0 Monterey 及以上
- **处理器**：Intel x64 或 Apple Silicon (M1/M2)
- **内存**：4GB RAM（推荐 8GB 及以上）
- **存储空间**：200MB 可用空间

---

## 📥 下载安装

### 🔗 官方发布

> 📌 **版本说明**：选择适合您处理器架构的版本

| 处理器类型 | 下载链接 | 适用设备 |
|-----------|----------|----------|
| 🔥 Apple Silicon | [aarch64.dmg](<!-- LINK_ARM_START -->https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.2/Clash.Verge_2.5.2_aarch64.dmg<!-- LINK_ARM_END -->) | M1/M2 Mac |
| 💻 Intel x64 | [x64.dmg](<!-- LINK_INTEL_START -->https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.2/Clash.Verge_2.5.2_x64.dmg<!-- LINK_INTEL_END -->) | Intel Mac |

#### 🚀 加速下载

| 下载源 | Apple Silicon | Intel x64 |
|--------|---------------|-----------|
| 🚀 镜像1 | [aarch64](https://git.886.be/https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v1.7.7/Clash.Verge_1.7.7_aarch64.dmg) | [x64](https://git.886.be/https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v1.7.7/Clash.Verge_1.7.7_x64.dmg) |
| 🚀 镜像2 | [aarch64](https://gh.xxooo.cf/https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v1.7.7/Clash.Verge_1.7.7_aarch64.dmg) | [x64](https://gh.xxooo.cf/https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v1.7.7/Clash.Verge_1.7.7_x64.dmg) |

---

## ⚠️ macOS 安全设置

### 🛡️ 安全性问题解决

由于 macOS 安全机制，首次运行可能遇到以下问题：

#### 🚨 常见提示

- "无法验证开发者"
- "应用程序已损坏"
- "来自身份不明开发者"

#### 🔧 解决步骤

##### 步骤一：尝试打开应用

双击 DMG 文件安装后，首次打开可能出现警告：

![安全警告](Clash-Verge-01.png)

##### 步骤二：系统偏好设置

1. 打开 `系统偏好设置` → `安全性与隐私`
2. 在 `通用` 选项卡中找到相关提示
3. 点击 `仍要打开` 按钮

![系统设置](Clash-Verge-02.png)

##### 步骤三：确认打开

再次确认打开应用程序：

![确认打开](Clash-Verge-03.png)

#### 💡 替代方案

如果上述方法无效，可以使用终端命令：

```bash
# 移除隔离属性
sudo xattr -r -d com.apple.quarantine /Applications/Clash\ Verge.app

# 或者临时禁用 Gatekeeper
sudo spctl --master-disable
```

> ⚠️ **安全提醒**：完成后建议重新启用 Gatekeeper
>
> ```bash
> sudo spctl --master-enable
> ```

---

## 🚀 配置教程

### 📋 准备工作

开始配置前，请确保：

- ✅ 已成功安装 Clash Verge
- ✅ 拥有有效的订阅链接或配置文件
- ✅ 解决了 macOS 安全限制问题
- ✅ 网络连接正常

### 🛠️ 配置步骤

#### 🔗 导入配置

##### 步骤一：启动应用

打开 Clash Verge，进入主界面：

![应用主界面](Clash-Verge-04.png)

> 💡 首次启动会要求网络权限，请选择"允许"

##### 步骤二：配置管理

点击"配置"或"Profiles"标签：

![配置管理](Clash-Verge-05.png)

##### 步骤三：添加订阅

点击"新建"或"+"按钮，选择"订阅"：

![添加订阅](Clash-Verge-06.png)

##### 步骤四：输入信息

填写订阅名称和 URL 地址：

![输入订阅信息](Clash-Verge-07.png)

---

#### 🔄 更新配置

##### 定期更新

定期更新订阅，获取最新节点：

![更新配置](Clash-Verge-08.png)

> 📅 **更新建议**
>
> - 建议每天更新一次订阅
> - 可以设置自动更新
> - 支持手动强制更新

---

## 🎛️ 高级功能

### 📊 流量监控

- **实时统计**：查看当前上传/下载速度
- **历史记录**：分析长期流量使用趋势
- **连接详情**：显示活跃连接信息
- **应用统计**：按应用分类统计流量

### 🎯 策略配置

- **自动选择**：根据延迟自动选择最优节点
- **手动选择**：用户手动指定使用节点
- **负载均衡**：流量在多个节点间均衡分配
- **故障转移**：主节点失效时自动切换

### 🎨 界面定制

- **主题切换**：明亮/暗色主题
- **布局调整**：自定义界面布局
- **语言设置**：多语言界面支持
- **字体设置**：自定义字体和大小

---

## ⚙️ 系统集成

### 🌐 系统代理

- **HTTP 代理**：自动配置系统 HTTP 代理
- **SOCKS 代理**：提供 SOCKS5 代理服务
- **PAC 模式**：基于规则的自动代理配置
- **TUN 模式**：系统级全局代理（需要额外配置）

### 🔧 开机启动

- **自动启动**：开机自动启动应用
- **最小化启动**：启动后自动最小化到菜单栏
- **系统托盘**：在系统托盘显示状态图标
- **快捷键**：支持全局快捷键操作

---

## ❓ 常见问题

### 🔧 安装问题

**Q: 无法打开应用，提示已损坏？**

A: 这是 macOS 安全机制：

- 方法1：系统偏好设置 → 安全性与隐私 → 仍要打开
- 方法2：终端执行 `sudo xattr -r -d com.apple.quarantine /Applications/Clash\ Verge.app`
- 方法3：临时禁用 Gatekeeper

**Q: 下载哪个版本？**

A: 根据处理器选择：

- Apple Silicon (M1/M2)：选择 aarch64 版本
- Intel 处理器：选择 x64 版本
- 不确定：查看 Apple 菜单 → 关于本机

### 🌐 连接问题

**Q: 导入配置后无法连接？**

A: 检查步骤：

- 确认订阅链接有效
- 检查网络连接状态
- 尝试手动选择节点
- 查看应用日志信息

**Q: 连接成功但无法上网？**

A: 排查建议：

- 检查系统代理设置
- 确认防火墙没有阻止
- 尝试切换代理模式
- 重启网络服务

### 🔧 功能问题

**Q: 如何设置开机启动？**

A: 设置路径：

- 应用内：设置 → 通用 → 开机启动
- 系统：系统偏好设置 → 用户与群组 → 登录项

**Q: 怎样查看详细日志？**

A: 日志查看：

- 应用内：设置 → 日志 → 查看详细日志
- 文件位置：`~/Library/Logs/Clash Verge/`

---

## 🔗 相关资源

### 📚 官方资源

- 🏠 [项目主页](https://github.com/clash-verge-rev/clash-verge-rev)
- 📖 [使用文档](https://github.com/clash-verge-rev/clash-verge-rev/wiki)
- 🐛 [问题反馈](https://github.com/clash-verge-rev/clash-verge-rev/issues)
- 💬 [讨论社区](https://github.com/clash-verge-rev/clash-verge-rev/discussions)

### 🛠️ 技术资源

- 🔧 [Clash 内核](https://github.com/Dreamacro/clash)
- 📋 [配置文档](https://clash.gitbook.io/)
- 🎯 [规则集合](https://github.com/Loyalsoldier/clash-rules)

### 💬 社区支持

- 🔗 [Telegram 群组](https://t.me/clash_cn)
- 📢 [更新通知](https://t.me/clash_verge)
- 💭 [用户交流](https://github.com/clash-verge-rev/clash-verge-rev/discussions)

---

## 💡 最佳实践

### ⚡ 性能优化

1. **合理配置规则**：避免所有流量都经过代理
2. **选择就近节点**：选择地理位置较近的服务器
3. **定期清理日志**：防止日志文件占用过多空间
4. **关闭不必要功能**：只启用需要的功能模块

### 🛡️ 安全建议

1. **定期更新**：保持应用和配置的最新版本
2. **配置备份**：定期备份重要的配置文件
3. **源码审计**：开源软件可以审查源代码
4. **权限控制**：只授予应用必要的系统权限

---

## 🎯 总结评价

### ✅ 主要优势

- 🆓 **完全免费**：开源免费，无需付费
- 🎨 **界面美观**：现代化的用户界面设计
- 🔧 **功能全面**：基于强大的 Clash 内核
- 🌍 **跨平台**：统一的使用体验
- 🔄 **持续更新**：活跃的社区维护

### ❌ 潜在不足

- 🛡️ **安全限制**：macOS 安全机制可能造成使用障碍
- 📚 **学习成本**：某些高级功能需要学习
- 🔧 **配置复杂**：相比简单客户端配置略复杂
- 🐛 **偶发问题**：作为开源软件可能存在小bug

### 🎯 推荐指数

总体评分：⭐⭐⭐⭐⭐

- 🆕 **新手用户**：⭐⭐⭐⭐（界面友好，功能够用）
- 🔧 **进阶用户**：⭐⭐⭐⭐⭐（功能全面，自定义程度高）
- 💰 **预算考虑**：⭐⭐⭐⭐⭐（完全免费，性价比极高）
- 🎨 **界面党**：⭐⭐⭐⭐⭐（现代化设计，视觉体验佳）

---

> 📅 最后更新：<!-- UPDATE_TIME_START -->2026-08-02<!-- UPDATE_TIME_END --> | ⚔️ 适用版本：Clash Verge <!-- VERSION_START -->v2.5.2<!-- VERSION_END -->
