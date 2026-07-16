# Shadowrocket

[![Update all rules](https://github.com/uxudjs/Shadowrocket/actions/workflows/update_rules.yml/badge.svg)](https://github.com/uxudjs/Shadowrocket/actions/workflows/update_rules.yml)

### 🌐 选择语言 | 選擇語言 | Choose Language

- [🇨🇳 简体中文](#-简体中文)
- [🇹🇼 繁體中文](#-繁體中文)
- [🇺🇸 English](#-english)

---

## 🇨🇳 简体中文

Shadowrocket 配置、规则集与模块合集，提供出国、回国、去广告、中国直连和全球代理等常用方案。

### 主要功能

- 🚀 **双场景配置** - 提供出国代理与回国访问两套配置，可按使用场景直接导入
- 🛡️ **去广告规则** - 聚合多个上游规则源，自动过滤、去重并排序
- 🇨🇳 **中国直连规则** - 聚合常用中国大陆服务、媒体、IP 与 ASN 规则
- 🌍 **全球代理规则** - 覆盖 GitHub、Telegram、流媒体及其他常用境外服务
- 🧩 **实用模块合集** - 提供应用去广告、功能增强与 Apple 系统追踪屏蔽模块
- 🔄 **每日自动更新** - GitHub Actions 自动更新规则文件及 README 中的规则数量
- 📱 **直接订阅使用** - 配置、规则集和模块均可通过 Raw 链接导入 Shadowrocket

### 配置文件

| 使用场景 | 说明 | 配置链接 |
|:---:|---|:---:|
| **出国规则** | 中国大陆服务直连，其余流量按规则代理 | [Across_GFW.conf](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/Across_GFW.conf) |
| **回国规则** | 中国大陆媒体服务走代理，其余流量默认直连 | [Back_CN.conf](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/Back_CN.conf) |

### 规则订阅

| 规则名称 | 当前数量 | 说明 | 订阅链接 |
|:---:|:---:|---|:---:|
| **FuckAD** | FuckAd合并规则总数：**193304** | 去广告规则集 | [订阅](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/lists/fuck_ad_sr.list) |
| **ChinaMax** | ChinaMax合并规则总数：**45894** | 中国大陆直连规则集 | [订阅](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/lists/china_max_sr.list) |
| **GlobalProxy** | GlobalProxy合并规则总数：**33739** | 全球代理规则集 | [订阅](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/lists/global_proxy_sr.list) |

### 模块下载

| 模块名称 | 说明 | 下载链接 |
|:---:|---|:---:|
| **FuckAppsAD** | 净化墨迹天气、中国联通、微信、夸克、12306、闲鱼、高德地图等应用广告 | [下载](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/modules/fuck_apps_ad_sr.sgmodule) |
| **FuckAppsVIP** | 集成 Endel、AdGuard、扫描全能王、有道词典、百度云、地震预警 ICL、波点音乐、句读等脚本 | [下载](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/modules/fuck_apps_vip_sr.sgmodule) |
| **AppleSystemBlock** | 屏蔽部分 Apple 系统追踪与安全浏览遥测域名 | [下载](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/modules/apple_block_sr.sgmodule) |

### 安装使用

#### 1. 导入配置文件

1. 复制所需配置链接
2. 打开 Shadowrocket，进入「配置」
3. 点击右上角「+」，粘贴链接并下载
4. 选中配置文件后按实际节点情况调整策略

#### 2. 添加规则订阅

1. 打开「配置」→「规则集」
2. 点击右上角「+」
3. 粘贴规则订阅链接并下载

#### 3. 添加模块

1. 打开首页「模块」
2. 点击右上角「+」
3. 粘贴模块链接并下载
4. 启用含脚本或重写功能的模块前，请确认已正确配置并信任 MITM 证书

### 自动更新

- 统一规则工作流每天 **19:00 UTC** 运行，也支持在 Actions 页面手动触发
- 工作流会依次运行三个规则脚本，拉取上游规则，过滤无效行，合并去重并排序
- 三类规则与 README 计数在同一任务中更新，并通过一次提交统一推送
- 并发锁确保同一时间只有一个更新任务运行；重复触发可安全合并等待
- README 中的计数文本与规则脚本存在固定匹配关系，请勿随意修改计数标签

> 说明：本仓库不额外提供 DNS 泄漏优化，实际 DNS 行为取决于 Shadowrocket、系统及网络环境。模块可能依赖第三方脚本，使用前请自行评估兼容性与风险。

### 规则来源鸣谢

- 去广告规则：[Cats-Team/AdRules](https://github.com/Cats-Team/AdRules) · [privacy-protection-tools/anti-AD](https://github.com/privacy-protection-tools/anti-AD)
- 中国直连规则：[whatshub.top](https://whatshub.top/) · [yfamilys.com](https://yfamilys.com/)
- 全球代理规则：[yfamilys.com](https://yfamilys.com/)

---

## 🇹🇼 繁體中文

Shadowrocket 配置、規則集與模組合集，提供出國、回國、去廣告、中國直連和全球代理等常用方案。

### 主要功能

- 🚀 **雙場景配置** - 提供出國代理與回國存取兩套配置，可按使用情境直接匯入
- 🛡️ **去廣告規則** - 聚合多個上游規則來源，自動過濾、去重並排序
- 🇨🇳 **中國直連規則** - 聚合常用中國大陸服務、媒體、IP 與 ASN 規則
- 🌍 **全球代理規則** - 涵蓋 GitHub、Telegram、串流媒體及其他常用境外服務
- 🧩 **實用模組合集** - 提供應用程式去廣告、功能增強與 Apple 系統追蹤封鎖模組
- 🔄 **每日自動更新** - GitHub Actions 自動更新規則檔案及 README 中的規則數量
- 📱 **直接訂閱使用** - 配置、規則集和模組均可透過 Raw 連結匯入 Shadowrocket

### 配置檔案

| 使用情境 | 說明 | 配置連結 |
|:---:|---|:---:|
| **出國規則** | 中國大陸服務直連，其餘流量按規則代理 | [Across_GFW.conf](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/Across_GFW.conf) |
| **回國規則** | 中國大陸媒體服務走代理，其餘流量預設直連 | [Back_CN.conf](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/Back_CN.conf) |

### 規則訂閱

| 規則名稱 | 目前數量 | 說明 | 訂閱連結 |
|:---:|:---:|---|:---:|
| **FuckAD** | FuckAd合併規則總數：**193304** | 去廣告規則集 | [訂閱](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/lists/fuck_ad_sr.list) |
| **ChinaMax** | ChinaMax合併規則總數：**45894** | 中國大陸直連規則集 | [訂閱](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/lists/china_max_sr.list) |
| **GlobalProxy** | GlobalProxy合併規則總數：**33739** | 全球代理規則集 | [訂閱](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/lists/global_proxy_sr.list) |

### 模組下載

| 模組名稱 | 說明 | 下載連結 |
|:---:|---|:---:|
| **FuckAppsAD** | 淨化墨跡天氣、中國聯通、微信、夸克、12306、閒魚、高德地圖等應用程式廣告 | [下載](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/modules/fuck_apps_ad_sr.sgmodule) |
| **FuckAppsVIP** | 整合 Endel、AdGuard、掃描全能王、有道詞典、百度雲、地震預警 ICL、波點音樂、句讀等腳本 | [下載](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/modules/fuck_apps_vip_sr.sgmodule) |
| **AppleSystemBlock** | 封鎖部分 Apple 系統追蹤與安全瀏覽遙測網域 | [下載](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/modules/apple_block_sr.sgmodule) |

### 安裝使用

#### 1. 匯入配置檔案

1. 複製所需配置連結
2. 開啟 Shadowrocket，進入「配置」
3. 點選右上角「+」，貼上連結並下載
4. 選取配置檔案後按實際節點情況調整策略

#### 2. 新增規則訂閱

1. 開啟「配置」→「規則集」
2. 點選右上角「+」
3. 貼上規則訂閱連結並下載

#### 3. 新增模組

1. 開啟首頁「模組」
2. 點選右上角「+」
3. 貼上模組連結並下載
4. 啟用含腳本或重寫功能的模組前，請確認已正確配置並信任 MITM 憑證

### 自動更新

- 統一規則工作流程每天 **19:00 UTC** 執行，也支援在 Actions 頁面手動觸發
- 工作流程會依序執行三個規則腳本，拉取上游規則，過濾無效行，合併去重並排序
- 三類規則與 README 計數會在同一任務中更新，並透過一次提交統一推送
- 並行鎖確保同一時間只有一個更新任務執行；重複觸發可安全合併等待
- README 中的計數文字與規則腳本存在固定匹配關係，請勿隨意修改計數標籤

> 說明：本倉庫不額外提供 DNS 洩漏最佳化，實際 DNS 行為取決於 Shadowrocket、系統及網路環境。模組可能依賴第三方腳本，使用前請自行評估相容性與風險。

### 規則來源鳴謝

- 去廣告規則：[Cats-Team/AdRules](https://github.com/Cats-Team/AdRules) · [privacy-protection-tools/anti-AD](https://github.com/privacy-protection-tools/anti-AD)
- 中國直連規則：[whatshub.top](https://whatshub.top/) · [yfamilys.com](https://yfamilys.com/)
- 全球代理規則：[yfamilys.com](https://yfamilys.com/)

---

## 🇺🇸 English

A collection of Shadowrocket configurations, rule sets, and modules for overseas access, return-to-China routing, ad blocking, China direct connections, and global proxy routing.

### Features

- 🚀 **Two routing scenarios** - Ready-to-import configurations for overseas and return-to-China use
- 🛡️ **Ad-blocking rules** - Aggregates multiple upstream sources, then filters, deduplicates, and sorts them
- 🇨🇳 **China direct rules** - Covers popular mainland China services, media, IP ranges, and ASNs
- 🌍 **Global proxy rules** - Covers GitHub, Telegram, streaming media, and other commonly used global services
- 🧩 **Utility modules** - Includes app ad blocking, feature-enhancement scripts, and Apple telemetry blocking
- 🔄 **Daily automatic updates** - GitHub Actions updates rule files and their counts in this README
- 📱 **Direct subscriptions** - Import configurations, rule sets, and modules into Shadowrocket through Raw links

### Configuration Files

| Scenario | Description | Configuration |
|:---:|---|:---:|
| **Overseas access** | Connects mainland China services directly and proxies other traffic by rule | [Across_GFW.conf](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/Across_GFW.conf) |
| **Return to China** | Proxies mainland China media services and connects other traffic directly | [Back_CN.conf](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/Back_CN.conf) |

### Rule Subscriptions

| Rule | Current Count | Description | Subscription |
|:---:|:---:|---|:---:|
| **FuckAD** | FuckAd merged rule count: **193304** | Ad-blocking rule set | [Subscribe](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/lists/fuck_ad_sr.list) |
| **ChinaMax** | ChinaMax merged rule count: **45894** | Mainland China direct-connect rule set | [Subscribe](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/lists/china_max_sr.list) |
| **GlobalProxy** | GlobalProxy merged rule count: **33739** | Global proxy rule set | [Subscribe](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/lists/global_proxy_sr.list) |

### Module Downloads

| Module | Description | Download |
|:---:|---|:---:|
| **FuckAppsAD** | Removes ads from Moji Weather, China Unicom, WeChat, Quark, 12306, Xianyu, Amap, and other apps | [Download](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/modules/fuck_apps_ad_sr.sgmodule) |
| **FuckAppsVIP** | Integrates scripts for Endel, AdGuard, CamScanner, Youdao Dictionary, Baidu Cloud, ICL Earthquake Warning, Bodian Music, Judou, and more | [Download](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/modules/fuck_apps_vip_sr.sgmodule) |
| **AppleSystemBlock** | Blocks selected Apple telemetry and safe-browsing domains | [Download](https://raw.githubusercontent.com/uxudjs/Shadowrocket/refs/heads/main/modules/apple_block_sr.sgmodule) |

### Installation

#### 1. Import a Configuration

1. Copy the required configuration link
2. Open Shadowrocket and go to **Config**
3. Tap the **+** button in the upper-right corner, paste the link, and download it
4. Select the configuration and adjust policies for your actual proxy nodes

#### 2. Add a Rule Subscription

1. Open **Config** → **Rule Set**
2. Tap the **+** button in the upper-right corner
3. Paste the rule subscription link and download it

#### 3. Add a Module

1. Open **Modules** on the home screen
2. Tap the **+** button in the upper-right corner
3. Paste the module link and download it
4. Before enabling modules with scripts or rewrites, make sure the MITM certificate is correctly configured and trusted

### Automatic Updates

- One unified rule workflow runs every day at **19:00 UTC** and can also be triggered manually from the Actions page
- It runs the three rule scripts sequentially to download, filter, deduplicate, and sort upstream rules
- All three rule sets and README counts are updated in one job and pushed in a single commit
- A concurrency lock allows only one update job to run at a time; duplicate triggers can safely coalesce
- README count labels are fixed matching keys used by the rule scripts; do not rename them casually

> Note: This repository does not provide additional DNS leak optimization. Actual DNS behavior depends on Shadowrocket, the operating system, and the network environment. Some modules depend on third-party scripts; review compatibility and risks before use.

### Acknowledgements

- Ad-blocking rules: [Cats-Team/AdRules](https://github.com/Cats-Team/AdRules) · [privacy-protection-tools/anti-AD](https://github.com/privacy-protection-tools/anti-AD)
- China direct rules: [whatshub.top](https://whatshub.top/) · [yfamilys.com](https://yfamilys.com/)
- Global proxy rules: [yfamilys.com](https://yfamilys.com/)

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=uxudjs/Shadowrocket&type=Date)](https://star-history.com/#uxudjs/Shadowrocket&Date)