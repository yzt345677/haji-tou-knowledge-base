# UI/UX 设计原则完全指南（第三部分）🎨

_哈基偷的学习笔记 - 2026-03-28 16:55 整理喵～_

**学习来源：** UI/UX Pro Max Skill (Claude Code)
**原始项目：** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

---

## 🌈 161 种配色方案详解

### 一、色彩理论基础

#### 色轮关系

```
        红 (Red)
      /   \
    橙     紫
   /         \
  黄 ——— 绿 ——— 蓝
```

**配色关系：**
- **互补色** — 色轮对面（红 + 绿），高对比度
- **类似色** — 色轮相邻（蓝 + 紫），和谐统一
- **三色搭配** — 等边三角形（红 + 黄 + 蓝），丰富活泼
- **分裂互补** — 主色 + 对面两侧颜色，平衡对比

---

### 二、按行业分类的配色方案（精选）

#### 1. Tech & SaaS（科技与企业软件）

| # | 方案名 | 主色 | 辅色 | 强调色 | 适用场景 |
|---|--------|------|------|--------|---------|
| 001 | **Startup Blue** | #3B82F6 | #1E40AF | #10B981 | SaaS 初创 |
| 002 | **Enterprise Gray** | #4B5563 | #1F2937 | #3B82F6 | 企业软件 |
| 003 | **Developer Dark** | #1F2937 | #374151 | #10B981 | 开发者工具 |
| 004 | **AI Purple** | #7C3AED | #4C1D95 | #2DD4BF | AI 平台 |
| 005 | **Cyber Security** | #1E3A5F | #374151 | #EF4444 | 安全产品 |
| 006 | **Cloud White** | #FFFFFF | #F3F4F6 | #3B82F6 | 云服务 |
| 007 | **Data Analytics** | #1E40AF | #374151 | #F59E0B | 数据分析 |
| 008 | **API First** | #059669 | #047857 | #3B82F6 | API 产品 |

**Startup Blue 示例：**
```css
:root {
  --primary: #3B82F6;      /* 信任、专业 */
  --primary-dark: #1E40AF; /* 深度、稳定 */
  --accent: #10B981;       /* 成功、增长 */
  --background: #F9FAFB;   /* 干净、现代 */
  --text: #1F2937;         /* 清晰、可读 */
}
```

---

#### 2. Finance（金融）

| # | 方案名 | 主色 | 辅色 | 强调色 | 适用场景 |
|---|--------|------|------|--------|---------|
| 009 | **Banking Trust** | #1E3A8A | #374151 | #F59E0B | 银行 |
| 010 | **Crypto Modern** | #F7931A | #1F2937 | #10B981 | 加密货币 |
| 011 | **Investment Gold** | #1E3A5F | #D4AF37 | #FFFFFF | 投资平台 |
| 012 | **Insurance Safe** | #059669 | #374151 | #EF4444 | 保险 |
| 013 | **Personal Finance** | #8B5CF6 | #4C1D95 | #10B981 | 理财应用 |
| 014 | **Payment Green** | #10B981 | #047857 | #1F2937 | 支付平台 |
| 015 | **Wealth Black** | #000000 | #D4AF37 | #FFFFFF | 财富管理 |
| 016 | **Fintech Blue** | #0EA5E9 | #0369A1 | #F59E0B | 金融科技 |

**Banking Trust 示例：**
```css
:root {
  --primary: #1E3A8A;      /* 深蓝 = 信任、稳定 */
  --secondary: #374151;    /* 炭灰 = 专业 */
  --accent: #F59E0B;       /* 金色 = 财富、价值 */
  --background: #F9FAFB;   /* 浅灰 = 干净 */
  --text: #111827;         /* 深灰 = 清晰 */
}
```

**避坑：** ❌ 避免 AI 紫色/粉色渐变（不适合金融行业）

---

#### 3. Healthcare（医疗健康）

| # | 方案名 | 主色 | 辅色 | 强调色 | 适用场景 |
|---|--------|------|------|--------|---------|
| 017 | **Medical Blue** | #0EA7CC | #0891B2 | #EF4444 | 医院 |
| 018 | **Pharmacy Green** | #059669 | #047857 | #FFFFFF | 药店 |
| 019 | **Dental Clean** | #06B6D4 | #FFFFFF | #0891B2 | 牙科 |
| 020 | **Mental Health** | #8B5CF6 | #A78BFA | #10B981 | 心理健康 |
| 021 | **Veterinary Warm** | #F59E0B | #78350F | #10B981 | 兽医 |
| 022 | **Wellness Spa** | #E8B4B8 | #A8D5BA | #D4AF37 | 健康 SPA |
| 023 | **Emergency Red** | #EF4444 | #DC2626 | #FFFFFF | 急救服务 |
| 024 | **Health Tracker** | #10B981 | #059669 | #3B82F6 | 健康追踪 |

**Medical Blue 示例：**
```css
:root {
  --primary: #0EA7CC;      /* 医疗蓝 = 专业、信任 */
  --secondary: #0891B2;    /* 青蓝 = 清洁 */
  --accent: #EF4444;       /* 红色 = 紧急、重要 */
  --background: #F0F9FF;   /* 浅蓝 = 清爽 */
  --text: #1E3A5F;         /* 深蓝灰 = 专业 */
}
```

---

#### 4. E-commerce（电商）

| # | 方案名 | 主色 | 辅色 | 强调色 | 适用场景 |
|---|--------|------|------|--------|---------|
| 025 | **Luxury Black** | #000000 | #FFFFFF | #D4AF37 | 奢侈品电商 |
| 026 | **Marketplace Blue** | #3B82F6 | #1E40AF | #10B981 | 综合电商 |
| 027 | **Fashion Pink** | #EC4899 | #BE185D | #FDF2F8 | 时尚电商 |
| 028 | **Tech Store** | #1F2937 | #3B82F6 | #10B981 | 电子产品 |
| 029 | **Organic Green** | #059669 | #78350F | #FCD34D | 有机产品 |
| 030 | **Food Delivery** | #DC2626 | #F59E0B | #10B981 | 外卖平台 |
| 031 | **Beauty Soft** | #F9A8D4 | #EC4899 | #FFFFFF | 美妆电商 |
| 032 | **Sports Dynamic** | #DC2626 | #1F2937 | #10B981 | 运动用品 |

**Luxury Black 示例：**
```css
:root {
  --primary: #000000;      /* 纯黑 = 高端、神秘 */
  --secondary: #FFFFFF;    /* 纯白 = 纯净、简洁 */
  --accent: #D4AF37;       /* 金色 = 奢华、独家 */
  --background: #FFFEFA;   /* 米白 = 温暖、高级 */
  --text: #1F2937;         /* 深灰 = 清晰 */
}
```

---

#### 5. Education（教育）

| # | 方案名 | 主色 | 辅色 | 强调色 | 适用场景 |
|---|--------|------|------|--------|---------|
| 033 | **Kids Fun** | #EC4899 | #8B5CF6 | #10B981 | 儿童教育 |
| 034 | **University Blue** | #1E40AF | #3B82F6 | #F59E0B | 高等教育 |
| 035 | **Online Course** | #7C3AED | #6D28D9 | #10B981 | 在线课程 |
| 036 | **Language Learning** | #10B981 | #059669 | #F59E0B | 语言学习 |
| 037 | **STEM Education** | #3B82F6 | #1F2937 | #EF4444 | 科学教育 |
| 038 | **Art School** | #EC4899 | #F59E0B | #8B5CF6 | 艺术学校 |
| 039 | **Professional Training** | #1F2937 | #4B5563 | #3B82F6 | 职业培训 |
| 040 | **Early Learning** | #FCD34D | #F59E0B | #EC4899 | 早教 |

---

#### 6. Creative & Media（创意媒体）

| # | 方案名 | 主色 | 辅色 | 强调色 | 适用场景 |
|---|--------|------|------|--------|---------|
| 041 | **Portfolio Minimal** | #000000 | #FFFFFF | #6B7280 | 作品集 |
| 042 | **Agency Vibrant** | #EC4899 | #8B5CF6 | #F59E0B | 创意机构 |
| 043 | **Photography Dark** | #1F2937 | #374151 | #FFFFFF | 摄影作品 |
| 044 | **Music Streaming** | #1DB954 | #191414 | #FFFFFF | 音乐平台 |
| 045 | **Video Platform** | #FF0000 | #1F2937 | #FFFFFF | 视频平台 |
| 046 | **Gaming Neon** | #8B5CF6 | #EC4899 | #10B981 | 游戏平台 |
| 047 | **Design Studio** | #F59E0B | #1F2937 | #FFFFFF | 设计工作室 |
| 048 | **Podcast Warm** | #78350F | #FCD34D | #1F2937 | 播客 |

---

#### 7. Lifestyle & Wellness（生活方式）

| # | 方案名 | 主色 | 辅色 | 强调色 | 适用场景 |
|---|--------|------|------|--------|---------|
| 049 | **Meditation Calm** | #A78BFA | #C4B5FD | #10B981 | 冥想应用 |
| 050 | **Fitness Energy** | #DC2626 | #1F2937 | #10B981 | 健身应用 |
| 051 | **Recipe Warm** | #F59E0B | #78350F | #10B981 | 食谱应用 |
| 052 | **Travel Adventure** | #0EA5E9 | #10B981 | #F59E0B | 旅游应用 |
| 053 | **Weather Fresh** | #0EA5E9 | #60A5FA | #FCD34D | 天气应用 |
| 054 | **Habit Green** | #10B981 | #059669 | #F59E0B | 习惯追踪 |
| 055 | **Mood Soft** | #A78BFA | #F9A8D4 | #10B981 | 情绪追踪 |
| 056 | **Sleep Dark** | #1F2937 | #374151 | #8B5CF6 | 睡眠应用 |

---

#### 8. Food & Beverage（餐饮）

| # | 方案名 | 主色 | 辅色 | 强调色 | 适用场景 |
|---|--------|------|------|--------|---------|
| 057 | **Restaurant Classic** | #DC2626 | #1F2937 | #F59E0B | 餐厅 |
| 058 | **Cafe Warm** | #78350F | #FCD34D | #FFFFFF | 咖啡馆 |
| 059 | **Bar Night** | #1F2937 | #7C3AED | #F59E0B | 酒吧 |
| 060 | **Bakery Soft** | #FCD34D | #F59E0B | #78350F | 面包店 |
| 061 | **Healthy Salad** | #10B981 | #059669 | #FCD34D | 健康餐 |
| 062 | **BBQ Bold** | #DC2626 | #78350F | #F59E0B | 烧烤店 |
| 063 | **Seafood Fresh** | #0EA5E9 | #FFFFFF | #F59E0B | 海鲜餐厅 |
| 064 | **Vegan Green** | #059669 | #10B981 | #FCD34D | 素食餐厅 |

---

#### 9. Travel & Hospitality（旅游酒店）

| # | 方案名 | 主色 | 辅色 | 强调色 | 适用场景 |
|---|--------|------|------|--------|---------|
| 065 | **Hotel Luxury** | #1F2937 | #D4AF37 | #FFFFFF | 豪华酒店 |
| 066 | **Resort Tropical** | #0EA5E9 | #10B981 | #FCD34D | 度假村 |
| 067 | **Airline Blue** | #0EA5E9 | #1E3A5F | #FFFFFF | 航空公司 |
| 068 | **Cruise Ocean** | #0891B2 | #0EA5E9 | #F59E0B | 邮轮 |
| 069 | **Adventure Orange** | #F59E0B | #78350F | #10B981 | 探险旅游 |
| 070 | **City Guide** | #374151 | #F59E0B | #FFFFFF | 城市指南 |
| 071 | **Booking Easy** | #3B82F6 | #1E40AF | #10B981 | 预订平台 |
| 072 | **Tour Guide** | #10B981 | #059669 | #F59E0B | 导游服务 |

---

### 三、配色设计原则

#### 60-30-10 法则

```
60% 主色（背景、大面积）
30% 辅色（卡片、次要元素）
10% 强调色（按钮、CTA、重要信息）
```

**示例应用：**
```css
/* 背景和大面积 */
body { background: #F9FAFB; }  /* 60% */

/* 卡片和次要元素 */
.card { background: #FFFFFF; }  /* 30% */

/* 按钮和 CTA */
.button { background: #3B82F6; }  /* 10% */
```

---

#### 无障碍对比度要求

| 等级 | 普通文本 | 大文本（18px+） | 图标/图形 |
|------|---------|---------------|---------|
| **WCAG A** | 4.5:1 | 3:1 | 3:1 |
| **WCAG AA** | 4.5:1 | 3:1 | 3:1 |
| **WCAG AAA** | 7:1 | 4.5:1 | 3:1 |

**快速检查：**
- ✅ #1F2937 on #FFFFFF = 14.7:1 ✅ AAA
- ✅ #3B82F6 on #FFFFFF = 4.5:1 ✅ AA
- ❌ #A78BFA on #FFFFFF = 2.8:1 ❌ 不达标

---

## 🔤 57 种字体组合详解

### 一、字体分类基础

#### 衬线体（Serif）

**特点：** 字母末端有装饰性笔画
**情感：** 传统、优雅、权威、可信
**适用：** 标题、长文阅读、传统品牌

**经典衬线体：**
- Georgia
- Times New Roman
- Playfair Display
- Cormorant Garamond
- Merriweather
- Lora

---

#### 无衬线体（Sans-Serif）

**特点：** 字母末端无装饰，简洁
**情感：** 现代、干净、友好、科技
**适用：** 正文、UI 界面、现代品牌

**经典无衬线体：**
- Helvetica
- Inter
- Roboto
- Open Sans
- Montserrat
- Poppins

---

#### 等宽字体（Monospace）

**特点：** 每个字符宽度相同
**情感：** 技术、代码、精确
**适用：** 代码显示、数据表格、技术产品

**经典等宽字体：**
- Courier New
- Fira Code
- JetBrains Mono
- Space Mono
- Roboto Mono

---

### 二、经典字体组合（57 种精选）

#### 组合 1-10：现代专业

| # | 标题字体 | 正文字体 | 适用场景 | Google Fonts 链接 |
|---|---------|---------|---------|-----------------|
| 01 | **Inter** | **Inter** | SaaS/科技/通用 | [链接](https://fonts.google.com/share?selection.family=Inter) |
| 02 | **Playfair Display** | **Source Sans Pro** | 时尚/杂志/博客 | [链接](https://fonts.google.com/share?selection.family=Playfair+Display:Source+Sans+Pro) |
| 03 | **Cormorant Garamond** | **Montserrat** | 奢侈品/美容 | [链接](https://fonts.google.com/share?selection.family=Cormorant+Garamond:Montserrat) |
| 04 | **Poppins** | **Open Sans** | 初创/创意机构 | [链接](https://fonts.google.com/share?selection.family=Poppins:Open+Sans) |
| 05 | **Roboto** | **Roboto** | Android/科技/通用 | [链接](https://fonts.google.com/share?selection.family=Roboto) |
| 06 | **Lato** | **Lato** | 企业/博客/通用 | [链接](https://fonts.google.com/share?selection.family=Lato) |
| 07 | **Oswald** | **Lora** | 新闻/杂志 | [链接](https://fonts.google.com/share?selection.family=Oswald:Lora) |
| 08 | **Raleway** | **Merriweather** | 作品集/博客 | [链接](https://fonts.google.com/share?selection.family=Raleway:Merriweather) |
| 09 | **Nunito** | **Nunito** | 教育/儿童/友好 | [链接](https://fonts.google.com/share?selection.family=Nunito) |
| 10 | **Space Grotesk** | **Space Mono** | 科技/开发者工具 | [链接](https://fonts.google.com/share?selection.family=Space+Grotesk:Space+Mono) |

---

#### 组合 11-20：优雅高端

| # | 标题字体 | 正文字体 | 适用场景 |
|---|---------|---------|---------|
| 11 | **Cinzel** | **Lato** | 奢侈品/酒店 |
| 12 | **Bodoni Moda** | **Inter** | 时尚杂志 |
| 13 | **Italiana** | **Raleway** | 高端品牌 |
| 14 | **Tenor Sans** | **Crimson Text** | 艺术画廊 |
| 15 | **Abril Fatface** | **Lato** | 高端博客 |
| 16 | **Prata** | **Open Sans** | 珠宝腕表 |
| 17 | **Bellefair** | **Raleway** | 高端 SPA |
| 18 | **Kaisei Decol** | **Noto Sans JP** | 日式美学 |
| 19 | **Shippori Mincho** | **Noto Sans** | 和风品牌 |
| 20 | **Cormorant** | **Work Sans** | 高端餐厅 |

---

#### 组合 21-30：创意活力

| # | 标题字体 | 正文字体 | 适用场景 |
|---|---------|---------|---------|
| 21 | **Fredoka One** | **Nunito** | 儿童产品 |
| 22 | **Pacifico** | **Open Sans** | 咖啡馆/休闲 |
| 23 | **Righteous** | **Roboto** | 科技初创 |
| 24 | **Bangers** | **Comic Neue** | 漫画/游戏 |
| 25 | **Creepster** | **Open Sans** | 万圣节/恐怖 |
| 26 | **Lobster** | **Raleway** | 餐饮/休闲 |
| 27 | **Permanent Marker** | **Roboto** | 街头风格 |
| 28 | **Kalam** | **Hind** | 手写风格 |
| 29 | **Dancing Script** | **Lato** | 婚礼/邀请 |
| 30 | **Satisfy** | **Open Sans** | 女性品牌 |

---

#### 组合 31-40：科技未来

| # | 标题字体 | 正文字体 | 适用场景 |
|---|---------|---------|---------|
| 31 | **Orbitron** | **Rajdhani** | 科幻/游戏 |
| 32 | **Exo 2** | **Roboto** | 科技产品 |
| 33 | **Audiowide** | **Open Sans** | 电子音乐 |
| 34 | **Russo One** | **Roboto** | 体育/竞技 |
| 35 | **Teko** | **Rajdhani** | 数据展示 |
| 36 | **Syncopate** | **Rajdhani** | 高端科技 |
| 37 | **Orbitron** | **Exo 2** | 太空主题 |
| 38 | **Michroma** | **Roboto** | 汽车/机械 |
| 39 | **Quantico** | **Open Sans** | 数据分析 |
| 40 | **Share Tech Mono** | **Share Tech** | 终端/代码 |

---

#### 组合 41-50：传统权威

| # | 标题字体 | 正文字体 | 适用场景 |
|---|---------|---------|---------|
| 41 | **Playfair Display** | **Lato** | 律师事务所 |
| 42 | **Crimson Text** | **Source Sans Pro** | 学术出版 |
| 43 | **EB Garamond** | **Inter** | 传统媒体 |
| 44 | **Libre Baskerville** | **Open Sans** | 金融机构 |
| 45 | **Vollkorn** | **Roboto** | 政府网站 |
| 46 | **Merriweather** | **Open Sans** | 新闻媒体 |
| 47 | **PT Serif** | **PT Sans** | 多语言网站 |
| 48 | **Lora** | **Open Sans** | 文学博客 |
| 49 | **Gentium Plus** | **Noto Sans** | 学术研究 |
| 50 | **Old Standard TT** | **Open Sans** | 历史档案 |

---

#### 组合 51-57：特殊场景

| # | 标题字体 | 正文字体 | 适用场景 |
|---|---------|---------|---------|
| 51 | **Noto Sans SC** | **Noto Sans SC** | 中文网站 |
| 52 | **Noto Serif SC** | **Noto Sans SC** | 中文传统 |
| 53 | **ZCOOL XiaoWei** | **ZCOOL QingKe HuangYou** | 中文创意 |
| 54 | **Ma Shan Zheng** | **Noto Sans SC** | 中文书法 |
| 55 | **Long Cang** | **Noto Sans SC** | 中文手写 |
| 56 | **Press Start 2P** | **Press Start 2P** | 像素游戏 |
| 57 | **VT323** | **VT323** | 复古终端 |

---

### 三、字体配对原则

#### 对比原则

**有效对比：**
- ✅ 衬线标题 + 无衬线正文（传统 + 现代）
- ✅ 粗标题 + 细正文（字重对比）
- ✅ 装饰标题 + 简洁正文（复杂度对比）

**避免：**
- ❌ 两种相似的衬线体
- ❌ 两种相似的无衬线体
- ❌ 超过 3 种字体家族

---

#### 字重搭配

```
标题：700 (Bold) 或 600 (SemiBold)
副标题：500 (Medium)
正文：400 (Regular)
辅助文字：300 (Light)
```

**示例：**
```css
h1 { font-weight: 700; font-size: 2.5rem; }
h2 { font-weight: 600; font-size: 2rem; }
h3 { font-weight: 600; font-size: 1.5rem; }
p  { font-weight: 400; font-size: 1rem; }
.small { font-weight: 300; font-size: 0.875rem; }
```

---

#### 字号层级

**桌面端推荐：**
```
H1: 48-64px  (3-4rem)
H2: 36-48px  (2.25-3rem)
H3: 24-36px  (1.5-2.25rem)
H4: 20-24px  (1.25-1.5rem)
正文：16-18px (1-1.125rem)
辅助：14-16px (0.875-1rem)
```

**移动端推荐：**
```
H1: 32-40px  (2-2.5rem)
H2: 24-32px  (1.5-2rem)
H3: 20-24px  (1.25-1.5rem)
H4: 18-20px  (1.125-1.25rem)
正文：16px   (1rem)
辅助：14px   (0.875rem)
```

---

## 💡 哈基偷的学习心得

### 核心收获

1. **配色不是随意的** — 有行业规则和情感联想
2. **60-30-10 法则** — 经典配色比例，保证视觉平衡
3. **无障碍优先** — 对比度至少 4.5:1（WCAG AA）
4. **字体配对有原则** — 对比但不冲突，最多 3 种字体

### 哈基偷能帮老大什么

**现在可以：**
- ✅ 根据项目推荐配色方案
- ✅ 提供 CSS 变量代码
- ✅ 检查配色对比度是否达标
- ✅ 推荐字体组合
- ✅ 提供字号层级建议

---

_哈基偷的 UI/UX 设计原则学习笔记（第三部分）完成喵～ 161 种配色 +57 种字体！_ 🐱💙

**下一步：** 第四部分 - 设计模式/检查清单详解
