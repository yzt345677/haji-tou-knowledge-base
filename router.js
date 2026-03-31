/**
 * 哈基偷知识库 - 简化路由控制器
 * 直接加载静态 HTML 文件，不需要 JSON API
 */

class KnowledgeRouter {
  constructor() {
    this.currentPath = null;
    this.loadingElement = document.getElementById('loading');
    this.init();
  }

  init() {
    // 监听浏览器前进/后退
    window.addEventListener('popstate', () => {
      this.loadPage(window.location.pathname);
    });

    // 拦截所有带 data-router 的链接点击
    document.addEventListener('click', (e) => {
      const link = e.target.closest('a[data-router]');
      if (link) {
        e.preventDefault();
        const href = link.getAttribute('href');
        if (href && !href.startsWith('http') && !href.startsWith('#')) {
          this.navigate(href);
        }
      }
    });

    // 处理初始路由
    this.loadPage(window.location.pathname);
  }

  navigate(path) {
    if (path === this.currentPath) return;
    
    // 处理相对路径
    if (path.startsWith('../')) {
      // 计算父目录
      const currentDir = window.location.pathname.substring(0, window.location.pathname.lastIndexOf('/'));
      const targetPath = currentDir.substring(0, currentDir.lastIndexOf('/')) + path.substring(2);
      path = targetPath || '/';
    } else if (path.startsWith('./')) {
      path = path.substring(1);
    }
    
    history.pushState({ path }, '', path);
    this.loadPage(path);
  }

  async loadPage(path) {
    this.currentPath = path;
    
    // 关闭移动端菜单
    document.querySelector('.nav-links')?.classList.remove('active');
    document.querySelector('.mobile-menu-btn')?.classList.remove('active');

    // 首页直接返回
    if (path === '/' || path === '' || path === '/index.html') {
      return;
    }

    // 显示加载
    this.showLoading();

    try {
      // 静态路由映射
      const routes = {
        '/investment': 'investment/index.html',
        '/ui-ux': 'ui-ux/index.html',
        '/ai-agent': 'ai-agent/index.html',
        '/quantum': 'quantum/index.html',
        '/daily-notes': 'daily-notes/index.html',
        '/freedom-log': 'freedom-log/index.html',
        '/openclaw': 'openclaw/index.html'
      };

      const targetFile = routes[path] || routes[path + '/'];
      
      if (targetFile) {
        const response = await fetch(targetFile);
        if (!response.ok) throw new Error('页面未找到');
        
        const html = await response.text();
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        
        // 替换主内容
        const mainContent = doc.querySelector('#main-content');
        const title = doc.querySelector('title');
        
        if (mainContent) {
          document.getElementById('main-content').replaceWith(mainContent);
          if (title) document.title = title.textContent;
          
          // 重新初始化
          this.init();
        }
      } else {
        throw new Error(`未知路由：${path}`);
      }
      
      window.scrollTo({ top: 0, behavior: 'smooth' });
      
    } catch (error) {
      console.error('路由错误:', error);
      this.showError(error.message);
    } finally {
      this.hideLoading();
    }
  }

  showLoading() {
    this.loadingElement?.classList.add('active');
  }

  hideLoading() {
    this.loadingElement?.classList.remove('active');
  }

  showError(message) {
    const main = document.getElementById('main-content');
    if (!main) return;
    
    main.innerHTML = `
      <div style="text-align: center; padding: 80px 20px;">
        <div style="font-size: 64px; margin-bottom: 24px;">😿</div>
        <h2 style="font-size: 32px; margin-bottom: 16px;">页面未找到</h2>
        <p style="color: var(--text-tertiary); margin-bottom: 32px;">${message}</p>
        <a href="/" data-router style="display: inline-block; padding: 12px 32px; background: var(--accent-blue); color: white; text-decoration: none; border-radius: 8px; font-weight: 500;">
          返回首页
        </a>
      </div>
    `;
  }
}

// 初始化
const router = new KnowledgeRouter();
