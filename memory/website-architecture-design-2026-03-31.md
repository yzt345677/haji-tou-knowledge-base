# 哈基偷知识库网站 - 信息架构设计 🐱

_创建时间：2026-03-31 11:05_
_设计风格：Figma + Apple（黑色科技感）_

---

## 🗺️ 一、网站结构总览

### 一级导航（主页面）

```
🏠 首页 (index.html)
│
├── 📈 投资知识库 (/investment)
├── 🎨 UI/UX 知识库 (/ui-ux)
├── 🤖 AI Agent 知识库 (/ai-agent)
├── ⚛️ 量子计算知识库 (/quantum)
├── 📰 每日笔记 (/daily-notes)
├── 📔 自由行动日记 (/freedom-log)
└── 🛠️ OpenClaw 工具 (/openclaw)
```

---

## 📈 二、投资知识库详细结构

### 二级导航

```
📈 投资知识库 (/investment)
│
├── 📚 投资基础 (/investment/basics)
├── 🌍 宏观经济 (/investment/macro)
├── 🏢 行业分析 (/investment/industry)
├── 📊 个股分析 (/investment/stocks)
├── 📉 技术分析 (/investment/technical)
├── 🧮 量化投资 (/investment/quantitative)
├── 🛠️ 实战工具 (/investment/tools)
└── ✅ 检查清单 (/investment/checklist)
```

### 三级导航（个股分析 - 分页加载）

```
📊 个股分析 (/investment/stocks)
│
├── 批次 1 (/investment/stocks/batch-1) — NVDA/TSM/ASML/AVGO
├── 批次 2 (/investment/stocks/batch-2) — 药明康德/恒瑞医药
├── 批次 3 (/investment/stocks/batch-3) — ...
├── 批次 4 (/investment/stocks/batch-4) — ...
├── 批次 5 (/investment/stocks/batch-5) — ...
└── 批次 6 (/investment/stocks/batch-6) — ...
```

---

## 🎨 三、UI/UX 知识库详细结构

```
🎨 UI/UX 知识库 (/ui-ux)
│
├── 📐 设计原则 (/ui-ux/principles)
│   ├── 第一部分：核心框架 (/ui-ux/principles/part-1)
│   ├── 第二部分：67 种 UI 风格 (/ui-ux/principles/part-2)
│   ├── 第三部分：配色与字体 (/ui-ux/principles/part-3)
│   └── 第四部分：设计模式与检查清单 (/ui-ux/principles/part-4)
│
├── 🔍 案例分析 (/ui-ux/case-studies)
│   ├── Linear.app (/ui-ux/case-studies/linear)
│   ├── Stripe.com (/ui-ux/case-studies/stripe)
│   ├── Notion.so (/ui-ux/case-studies/notion)
│   ├── Figma.com (/ui-ux/case-studies/figma)
│   ├── Airbnb.com (/ui-ux/case-studies/airbnb)
│   ├── Apple.com (/ui-ux/case-studies/apple)
│   └── Dribbble.com (/ui-ux/case-studies/dribbble)
│
└── 📋 对比总结 (/ui-ux/summary)
```

---

## 🤖 四、AI Agent 知识库详细结构

```
🤖 AI Agent 知识库 (/ai-agent)
│
├── 📚 核心学习 (/ai-agent/core)
│   ├── 完整学习笔记 (/ai-agent/core/learning)
│   ├── 框架对比 (/ai-agent/core/frameworks)
│   └── 完整指南索引 (/ai-agent/core/index)
│
├── 🛡️ 安全最佳实践 (/ai-agent/security)
│   ├── 安全最佳实践 (/ai-agent/security/best-practices)
│   └── 生产环境安全 (/ai-agent/security/production)
│
├── 🔧 高级主题 (/ai-agent/advanced)
│   ├── 上下文管理 (/ai-agent/advanced/context)
│   ├── 提示词工程 (/ai-agent/advanced/prompt)
│   ├── 成本优化 (/ai-agent/advanced/cost)
│   └── 开发与部署 (/ai-agent/advanced/deployment)
│
├── 💼 应用案例 (/ai-agent/applications)
│   ├── 应用案例 (/ai-agent/applications/cases)
│   └── 金融投资应用 (/ai-agent/applications/finance)
│
└── 🚀 未来趋势 (/ai-agent/future)
    ├── 2026 年 3 月更新 (/ai-agent/future/2026-march)
    └── 2026-2030 趋势 (/ai-agent/future/2026-2030)
```

---

## ⚛️ 五、量子计算知识库详细结构

```
⚛️ 量子计算知识库 (/quantum)
│
├── 📖 基础原理 (/quantum/basics)
├── 📈 2026 年最新进展 (/quantum/2026-update)
├── 🧮 核心算法 (/quantum/algorithms)
├── 🤖 量子机器学习 (/quantum/ml)
└── 📋 学习总索引 (/quantum/index)
```

---

## 📰 六、每日笔记结构

```
📰 每日笔记 (/daily-notes)
│
├── 2026-03 (/daily-notes/2026-03)
│   ├── 2026-03-11 (/daily-notes/2026-03-11)
│   ├── 2026-03-18 (/daily-notes/2026-03-18)
│   ├── 2026-03-19 (/daily-notes/2026-03-19)
│   ├── 2026-03-20 (/daily-notes/2026-03-20)
│   ├── 2026-03-21 (/daily-notes/2026-03-21)
│   ├── 2026-03-22 (/daily-notes/2026-03-22)
│   ├── 2026-03-26 (/daily-notes/2026-03-26)
│   └── 2026-03-27 (/daily-notes/2026-03-27)
│
└── 成长日记 (/daily-notes/growth)
    └── 2026-03-27 (/daily-notes/growth/2026-03-27)
```

---

## 🛠️ 七、OpenClaw 工具结构

```
🛠️ OpenClaw 工具 (/openclaw)
│
├── 🔌 技能安装 (/openclaw/skills/install)
├── 📋 技能推荐 (/openclaw/skills/recommendations)
├── 🧠 记忆管理最佳实践 (/openclaw/memory)
├── ⚡ 自动化工作流 (/openclaw/workflows)
└── 📖 快速参考 (/openclaw/quick-reference)
```

---

## 🔗 八、URL 路由设计

### 路由规则

```javascript
const routes = {
  // 首页
  '/': 'index.html',
  
  // 一级知识库
  '/investment': 'investment/index.html',
  '/ui-ux': 'ui-ux/index.html',
  '/ai-agent': 'ai-agent/index.html',
  '/quantum': 'quantum/index.html',
  '/daily-notes': 'daily-notes/index.html',
  '/freedom-log': 'freedom-log/index.html',
  '/openclaw': 'openclaw/index.html',
  
  // 二级分类（投资示例）
  '/investment/basics': 'investment/basics.html',
  '/investment/macro': 'investment/macro.html',
  '/investment/industry': 'investment/industry.html',
  '/investment/stocks': 'investment/stocks.html',
  '/investment/technical': 'investment/technical.html',
  '/investment/quantitative': 'investment/quantitative.html',
  '/investment/tools': 'investment/tools.html',
  '/investment/checklist': 'investment/checklist.html',
  
  // 三级详情（个股分析示例）
  '/investment/stocks/batch-1': 'investment/stocks/batch-1.html',
  '/investment/stocks/batch-2': 'investment/stocks/batch-2.html',
  // ...
  
  // UI/UX 案例分析
  '/ui-ux/case-studies/linear': 'ui-ux/case-studies/linear.html',
  '/ui-ux/case-studies/stripe': 'ui-ux/case-studies/stripe.html',
  // ...
};
```

---

## ⚙️ 九、JavaScript 动态加载逻辑

### 核心路由控制器

```javascript
// router.js
class KnowledgeRouter {
  constructor() {
    this.currentRoute = null;
    this.contentCache = new Map();
    this.init();
  }

  init() {
    // 监听浏览器前进/后退
    window.addEventListener('popstate', (e) => {
      this.handleRoute(window.location.pathname);
    });

    // 拦截所有内部链接点击
    document.addEventListener('click', (e) => {
      if (e.target.matches('a[data-router]')) {
        e.preventDefault();
        const href = e.target.getAttribute('href');
        this.navigate(href);
      }
    });

    // 处理初始路由
    this.handleRoute(window.location.pathname);
  }

  navigate(path) {
    history.pushState({ path }, '', path);
    this.handleRoute(path);
  }

  async handleRoute(path) {
    this.currentRoute = path;
    
    // 显示加载状态
    this.showLoading();

    try {
      // 尝试从缓存加载
      if (this.contentCache.has(path)) {
        this.renderContent(this.contentCache.get(path));
        return;
      }

      // 从服务器加载
      const response = await fetch(`/content${path}.json`);
      if (!response.ok) throw new Error('Not found');
      
      const data = await response.json();
      this.contentCache.set(path, data);
      this.renderContent(data);
      
      // 更新页面标题
      document.title = `${data.title} | 哈基偷知识库`;
      
    } catch (error) {
      this.showError(error.message);
    } finally {
      this.hideLoading();
    }
  }

  showLoading() {
    document.getElementById('loading').style.display = 'block';
  }

  hideLoading() {
    document.getElementById('loading').style.display = 'none';
  }

  renderContent(data) {
    const main = document.getElementById('main-content');
    main.innerHTML = `
      <article class="content-card">
        <h1>${data.title}</h1>
        ${data.breadcrumb ? this.renderBreadcrumb(data.breadcrumb) : ''}
        <div class="content-body">${data.content}</div>
        ${data.related ? this.renderRelated(data.related) : ''}
      </article>
    `;
  }

  renderBreadcrumb(items) {
    return `
      <nav class="breadcrumb">
        ${items.map((item, i) => `
          <a href="${item.path}" data-router>${item.label}</a>
          ${i < items.length - 1 ? '<span class="separator">/</span>' : ''}
        `).join('')}
      </nav>
    `;
  }

  renderRelated(items) {
    return `
      <section class="related-articles">
        <h2>相关内容</h2>
        <div class="card-grid">
          ${items.map(item => `
            <a href="${item.path}" class="content-card" data-router>
              <h3>${item.title}</h3>
              <p>${item.summary}</p>
            </a>
          `).join('')}
        </div>
      </section>
    `;
  }

  showError(message) {
    document.getElementById('main-content').innerHTML = `
      <div class="error-state">
        <h2>页面未找到</h2>
        <p>${message}</p>
        <a href="/" data-router>返回首页</a>
      </div>
    `;
  }
}

// 初始化路由
const router = new KnowledgeRouter();
```

---

## 📄 十、分页组件设计

### 分页控制器

```javascript
// pagination.js
class PaginationController {
  constructor(options = {}) {
    this.currentPage = options.currentPage || 1;
    this.totalPages = options.totalPages || 1;
    this.itemsPerPage = options.itemsPerPage || 10;
    this.container = options.container || '#pagination';
    this.onChange = options.onChange || (() => {});
  }

  render() {
    const container = document.querySelector(this.container);
    if (!container) return;

    container.innerHTML = `
      <nav class="pagination" aria-label="分页导航">
        ${this.renderPrev()}
        ${this.renderPages()}
        ${this.renderNext()}
      </nav>
    `;

    // 绑定事件
    container.querySelectorAll('[data-page]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const page = parseInt(btn.dataset.page);
        this.goToPage(page);
      });
    });
  }

  renderPrev() {
    if (this.currentPage === 1) return '';
    return `
      <button data-page="${this.currentPage - 1}" class="pagination-btn prev">
        ← 上一页
      </button>
    `;
  }

  renderNext() {
    if (this.currentPage === this.totalPages) return '';
    return `
      <button data-page="${this.currentPage + 1}" class="pagination-btn next">
        下一页 →
      </button>
    `;
  }

  renderPages() {
    const pages = [];
    const maxVisible = 5;
    let start = Math.max(1, this.currentPage - Math.floor(maxVisible / 2));
    let end = Math.min(this.totalPages, start + maxVisible - 1);

    // 调整起始位置
    if (end - start < maxVisible - 1) {
      start = Math.max(1, end - maxVisible + 1);
    }

    // 添加第一页
    if (start > 1) {
      pages.push(this.createPageButton(1));
      if (start > 2) {
        pages.push('<span class="pagination-ellipsis">...</span>');
      }
    }

    // 添加中间页
    for (let i = start; i <= end; i++) {
      pages.push(this.createPageButton(i, i === this.currentPage));
    }

    // 添加最后一页
    if (end < this.totalPages) {
      if (end < this.totalPages - 1) {
        pages.push('<span class="pagination-ellipsis">...</span>');
      }
      pages.push(this.createPageButton(this.totalPages));
    }

    return pages.join('');
  }

  createPageButton(pageNum, isActive = false) {
    const activeClass = isActive ? ' active' : '';
    return `
      <button 
        data-page="${pageNum}" 
        class="pagination-btn${activeClass}"
        ${isActive ? 'aria-current="page"' : ''}
      >
        ${pageNum}
      </button>
    `;
  }

  goToPage(page) {
    if (page < 1 || page > this.totalPages) return;
    this.currentPage = page;
    this.render();
    this.onChange(page);
    
    // 滚动到顶部
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}

// 使用示例
const pagination = new PaginationController({
  currentPage: 1,
  totalPages: 6, // 6 批次个股分析
  container: '#stock-pagination',
  onChange: (page) => {
    // 动态加载对应批次内容
    loadStockBatch(page);
  }
});

pagination.render();
```

---

## 🎨 十一、视觉设计规范（Figma + Apple 黑色科技感）

### 配色方案

```css
:root {
  /* 底色 */
  --bg-primary: #0D0D0D;      /* 深空黑 - 主背景 */
  --bg-secondary: #1A1A1A;    /* 卡片背景 */
  --bg-tertiary: #252525;     /* 悬停/强调 */
  
  /* 文字 */
  --text-primary: #FFFFFF;    /* 主标题 */
  --text-secondary: #E5E5E5;  /* 正文 */
  --text-tertiary: #A1A1A1;   /* 辅助文字 */
  
  /* 强调色 */
  --accent-blue: #2997FF;     /* Apple 蓝 */
  --accent-figma: #0D99FF;    /* Figma 蓝 */
  --accent-success: #30D158;  /* 成功绿 */
  --accent-warning: #FF9F0A;  /* 警告橙 */
  --accent-error: #FF453A;    /* 错误红 */
  
  /* 边框/分割线 */
  --border-color: #333333;
  
  /* 阴影 */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.5);
}
```

### 字体系统

```css
:root {
  /* 字体家族 */
  --font-sans: 'Inter', 'Noto Sans SC', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'SF Mono', 'Fira Code', 'JetBrains Mono', monospace;
  
  /* 字号层级 */
  --text-xs: 12px;    /* 辅助文字 */
  --text-sm: 14px;    /* 小字 */
  --text-base: 16px;  /* 正文 */
  --text-lg: 18px;    /* 大正文 */
  --text-xl: 24px;    /* 小标题 */
  --text-2xl: 32px;   /* 中标题 */
  --text-3xl: 40px;   /* 大标题 */
  --text-4xl: 48px;   /* 超大标题 */
  
  /* 字重 */
  --font-normal: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;
  
  /* 行高 */
  --leading-tight: 1.25;
  --leading-normal: 1.5;
  --leading-relaxed: 1.75;
}
```

### 组件样式（卡片/按钮/导航）

```css
/* 内容卡片 */
.content-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 24px;
  transition: all 0.2s ease;
}

.content-card:hover {
  background: var(--bg-tertiary);
  border-color: var(--accent-blue);
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

/* 主按钮 */
.btn-primary {
  background: var(--accent-blue);
  color: white;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: var(--font-medium);
  transition: all 0.2s ease;
}

.btn-primary:hover {
  background: var(--accent-figma);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(41, 151, 255, 0.3);
}

/* 导航栏 */
.navbar {
  background: rgba(13, 13, 13, 0.95);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border-color);
  padding: 16px 24px;
  position: sticky;
  top: 0;
  z-index: 1000;
}

.nav-link {
  color: var(--text-secondary);
  text-decoration: none;
  padding: 8px 16px;
  border-radius: 8px;
  transition: all 0.2s ease;
}

.nav-link:hover,
.nav-link.active {
  color: var(--text-primary);
  background: var(--bg-tertiary);
}

/* 分页组件 */
.pagination {
  display: flex;
  gap: 8px;
  justify-content: center;
  padding: 24px 0;
}

.pagination-btn {
  min-width: 40px;
  height: 40px;
  padding: 0 12px;
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.2s ease;
}

.pagination-btn:hover {
  background: var(--bg-tertiary);
  border-color: var(--accent-blue);
  color: var(--text-primary);
}

.pagination-btn.active {
  background: var(--accent-blue);
  border-color: var(--accent-blue);
  color: white;
}

/* 面包屑导航 */
.breadcrumb {
  display: flex;
  gap: 8px;
  align-items: center;
  margin-bottom: 24px;
  font-size: var(--text-sm);
}

.breadcrumb a {
  color: var(--text-tertiary);
  text-decoration: none;
  transition: color 0.2s ease;
}

.breadcrumb a:hover {
  color: var(--accent-blue);
}

.breadcrumb .separator {
  color: var(--text-tertiary);
}
```

### 响应式断点

```css
/* 移动优先 */
@media (min-width: 640px) {
  /* 手机大 */
  .container { max-width: 640px; }
}

@media (min-width: 768px) {
  /* 平板 */
  .container { max-width: 768px; }
  .card-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 1024px) {
  /* 桌面小 */
  .container { max-width: 1024px; }
  .card-grid { grid-template-columns: repeat(3, 1fr); }
}

@media (min-width: 1440px) {
  /* 桌面大 */
  .container { max-width: 1440px; }
  .card-grid { grid-template-columns: repeat(4, 1fr); }
}
```

---

## 📊 十二、内容数据结构

### JSON 内容格式

```json
{
  "title": "个股分析 - 批次 1",
  "path": "/investment/stocks/batch-1",
  "breadcrumb": [
    { "label": "首页", "path": "/" },
    { "label": "投资知识库", "path": "/investment" },
    { "label": "个股分析", "path": "/investment/stocks" },
    { "label": "批次 1", "path": "/investment/stocks/batch-1" }
  ],
  "content": "<h2>NVDA - 英伟达</h2>...",
  "metadata": {
    "category": "investment",
    "subcategory": "stocks",
    "batch": 1,
    "stocks": ["NVDA", "TSM", "ASML", "AVGO"],
    "lastUpdated": "2026-03-24"
  },
  "related": [
    {
      "title": "批次 2 - 药明康德/恒瑞医药",
      "path": "/investment/stocks/batch-2",
      "summary": "医药行业龙头股深度分析"
    },
    {
      "title": "技术分析基础",
      "path": "/investment/technical",
      "summary": "K 线/均线/成交量/指标入门"
    }
  ],
  "pagination": {
    "current": 1,
    "total": 6,
    "type": "batch"
  }
}
```

---

## 🚀 十三、性能优化建议

### 1. 内容预加载

```javascript
// 预加载相邻页面内容
function preloadAdjacent(currentPath) {
  const adjacent = getAdjacentPaths(currentPath);
  adjacent.forEach(path => {
    fetch(`/content${path}.json`)
      .then(res => res.json())
      .then(data => router.contentCache.set(path, data));
  });
}
```

### 2. 懒加载图片

```html
<img src="placeholder.jpg" data-src="actual-image.jpg" loading="lazy" alt="...">
```

### 3. 虚拟滚动（长列表）

```javascript
// 当内容超过 100 项时使用虚拟滚动
class VirtualScroller {
  constructor(options) {
    this.itemHeight = options.itemHeight || 60;
    this.containerHeight = options.containerHeight || 600;
    this.visibleItems = Math.ceil(this.containerHeight / this.itemHeight);
  }
  
  render(items, startIndex) {
    // 只渲染可见区域的内容
    const visible = items.slice(startIndex, startIndex + this.visibleItems);
    // ...
  }
}
```

---

## ✅ 十四、交付清单

### 行动 #42 产出（11:05-12:05）

- [x] 完整导航树（三级结构）
- [x] URL 路由设计
- [x] JavaScript 动态加载逻辑（router.js）
- [x] 分页组件设计（pagination.js）
- [x] 黑色科技感视觉规范（CSS 变量）
- [x] 内容数据结构定义（JSON 格式）
- [x] 性能优化建议

---

_这是哈基偷知识库网站的完整信息架构设计喵～ 下一步开始创建实际页面代码！_ 🐱💙
