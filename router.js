/**
 * 哈基偷知识库 - 路由控制器
 * 负责页面导航、内容加载、历史记录管理
 */

class KnowledgeRouter {
  constructor(options = {}) {
    this.basePath = options.basePath || '';
    this.contentPath = options.contentPath || '/content';
    this.currentRoute = null;
    this.contentCache = new Map();
    this.loadingElement = document.getElementById('loading');
    this.mainContent = document.getElementById('main-content');
    
    this.init();
  }

  init() {
    // 监听浏览器前进/后退
    window.addEventListener('popstate', (e) => {
      this.handleRoute(window.location.pathname);
    });

    // 拦截所有带 data-router 的链接点击
    document.addEventListener('click', (e) => {
      const link = e.target.closest('a[data-router]');
      if (link) {
        e.preventDefault();
        const href = link.getAttribute('href');
        this.navigate(href);
      }
    });

    // 处理初始路由
    this.handleRoute(window.location.pathname);
  }

  /**
   * 导航到新页面
   */
  navigate(path) {
    if (path === this.currentRoute) return;
    
    history.pushState({ path }, '', path);
    this.handleRoute(path);
  }

  /**
   * 处理路由
   */
  async handleRoute(path) {
    this.currentRoute = path;
    
    // 关闭移动端菜单
    document.querySelector('.nav-links')?.classList.remove('active');
    document.querySelector('.mobile-menu-btn')?.classList.remove('active');

    // 显示加载状态
    this.showLoading();

    try {
      // 首页直接返回，不加载内容
      if (path === '/' || path === this.basePath || path === this.basePath + '/') {
        this.hideLoading();
        return;
      }

      // 尝试从缓存加载
      if (this.contentCache.has(path)) {
        this.renderContent(this.contentCache.get(path));
        return;
      }

      // 从服务器加载
      const response = await this.fetchContent(path);
      if (!response.ok) throw new Error('页面未找到');
      
      const data = await response.json();
      this.contentCache.set(path, data);
      this.renderContent(data);
      
      // 更新页面标题
      document.title = `${data.title} | 哈基偷知识库`;
      
      // 滚动到顶部
      window.scrollTo({ top: 0, behavior: 'smooth' });
      
    } catch (error) {
      console.error('路由错误:', error);
      this.showError(error.message);
    } finally {
      this.hideLoading();
    }
  }

  /**
   * 获取内容
   */
  async fetchContent(path) {
    // 模拟内容加载（实际部署时替换为真实 API）
    // const response = await fetch(`${this.contentPath}${path}.json`);
    
    // 临时模拟：根据路径返回示例内容
    return this.mockContent(path);
  }

  /**
   * 模拟内容（开发阶段使用）
   */
  async mockContent(path) {
    // 模拟网络延迟
    await new Promise(resolve => setTimeout(resolve, 300));
    
    const mockData = {
      title: this.pathToTitle(path),
      path: path,
      breadcrumb: this.generateBreadcrumb(path),
      content: `
        <div class="content-placeholder">
          <h2>${this.pathToTitle(path)}</h2>
          <p>这是哈基偷的知识库内容页面。</p>
          <p>路径：<code>${path}</code></p>
          <p class="text-muted">内容正在准备中，敬请期待喵～ 🐱</p>
        </div>
      `,
      metadata: {
        category: path.split('/')[1] || 'unknown',
        lastUpdated: new Date().toISOString().split('T')[0]
      }
    };
    
    return {
      ok: true,
      json: () => Promise.resolve(mockData)
    };
  }

  /**
   * 路径转标题
   */
  pathToTitle(path) {
    const segments = path.split('/').filter(Boolean);
    if (segments.length === 0) return '首页';
    
    const lastSegment = segments[segments.length - 1];
    return lastSegment
      .split('-')
      .map(word => word.charAt(0).toUpperCase() + word.slice(1))
      .join(' ');
  }

  /**
   * 生成面包屑
   */
  generateBreadcrumb(path) {
    const segments = path.split('/').filter(Boolean);
    const breadcrumb = [{ label: '首页', path: '/' }];
    
    let currentPath = '';
    segments.forEach((segment, i) => {
      currentPath += '/' + segment;
      breadcrumb.push({
        label: this.pathToTitle('/' + segment),
        path: currentPath
      });
    });
    
    return breadcrumb;
  }

  /**
   * 渲染内容
   */
  renderContent(data) {
    if (!this.mainContent) return;
    
    this.mainContent.innerHTML = `
      <article class="content-card" style="max-width: 900px; margin: 48px auto;">
        ${this.renderBreadcrumb(data.breadcrumb)}
        <h1 style="font-size: var(--text-3xl); margin-bottom: 24px;">${data.title}</h1>
        <div class="content-body" style="line-height: 1.8; color: var(--text-secondary);">
          ${data.content}
        </div>
        ${data.related ? this.renderRelated(data.related) : ''}
      </article>
    `;
  }

  /**
   * 渲染面包屑
   */
  renderBreadcrumb(items) {
    if (!items || items.length <= 1) return '';
    
    return `
      <nav class="breadcrumb" style="margin-bottom: 24px; font-size: var(--text-sm);">
        ${items.map((item, i) => `
          ${i < items.length - 1 ? `
            <a href="${item.path}" data-router style="color: var(--text-tertiary); text-decoration: none;">
              ${item.label}
            </a>
            <span style="color: var(--text-tertiary); margin: 0 8px;">/</span>
          ` : `
            <span style="color: var(--text-primary);">${item.label}</span>
          `}
        `).join('')}
      </nav>
    `;
  }

  /**
   * 渲染相关内容
   */
  renderRelated(items) {
    if (!items || items.length === 0) return '';
    
    return `
      <section class="related-articles" style="margin-top: 48px; padding-top: 32px; border-top: 1px solid var(--border-color);">
        <h2 style="font-size: var(--text-xl); margin-bottom: 24px;">相关内容</h2>
        <div class="card-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));">
          ${items.map(item => `
            <a href="${item.path}" class="content-card" data-router style="padding: 20px;">
              <h3 style="font-size: var(--text-lg); margin-bottom: 8px;">${item.title}</h3>
              <p style="font-size: var(--text-sm); color: var(--text-tertiary);">${item.summary || ''}</p>
            </a>
          `).join('')}
        </div>
      </section>
    `;
  }

  /**
   * 显示加载
   */
  showLoading() {
    if (this.loadingElement) {
      this.loadingElement.classList.add('active');
    }
  }

  /**
   * 隐藏加载
   */
  hideLoading() {
    if (this.loadingElement) {
      this.loadingElement.classList.remove('active');
    }
  }

  /**
   * 显示错误
   */
  showError(message) {
    if (!this.mainContent) return;
    
    this.mainContent.innerHTML = `
      <div class="error-state" style="text-align: center; padding: 80px 20px;">
        <div style="font-size: 64px; margin-bottom: 24px;">😿</div>
        <h2 style="font-size: var(--text-2xl); margin-bottom: 16px;">页面未找到</h2>
        <p style="color: var(--text-tertiary); margin-bottom: 32px;">${message}</p>
        <a href="/" data-router class="btn-primary" style="display: inline-block; padding: 12px 32px; background: var(--accent-blue); color: white; text-decoration: none; border-radius: 8px; font-weight: 500;">
          返回首页
        </a>
      </div>
    `;
  }
}

// 初始化路由
const router = new KnowledgeRouter({
  basePath: '',
  contentPath: '/content'
});
