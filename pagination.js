/**
 * 哈基偷知识库 - 分页组件
 * 支持动态加载、智能页码显示、键盘导航
 */

class PaginationController {
  constructor(options = {}) {
    this.currentPage = options.currentPage || 1;
    this.totalPages = options.totalPages || 1;
    this.itemsPerPage = options.itemsPerPage || 10;
    this.container = options.container || '#pagination';
    this.onChange = options.onChange || (() => {});
    this.visiblePages = options.visiblePages || 5;
    
    this.init();
  }

  init() {
    this.render();
  }

  /**
   * 渲染分页组件
   */
  render() {
    const container = document.querySelector(this.container);
    if (!container) return;

    container.innerHTML = `
      <nav class="pagination" aria-label="分页导航" role="navigation">
        ${this.renderFirst()}
        ${this.renderPrev()}
        ${this.renderPages()}
        ${this.renderNext()}
        ${this.renderLast()}
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

    // 键盘导航
    container.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') {
        this.prev();
      } else if (e.key === 'ArrowRight') {
        this.next();
      }
    });
  }

  /**
   * 渲染首页按钮
   */
  renderFirst() {
    if (this.currentPage <= 1) return '';
    return `
      <button 
        data-page="1" 
        class="pagination-btn pagination-first"
        aria-label="第一页"
        title="第一页"
      >
        «
      </button>
    `;
  }

  /**
   * 渲染上一页按钮
   */
  renderPrev() {
    if (this.currentPage <= 1) return '';
    return `
      <button 
        data-page="${this.currentPage - 1}" 
        class="pagination-btn pagination-prev"
        aria-label="上一页"
      >
        ‹ 上一页
      </button>
    `;
  }

  /**
   * 渲染页码
   */
  renderPages() {
    const pages = [];
    let start = Math.max(1, this.currentPage - Math.floor(this.visiblePages / 2));
    let end = Math.min(this.totalPages, start + this.visiblePages - 1);

    // 调整起始位置
    if (end - start < this.visiblePages - 1) {
      start = Math.max(1, end - this.visiblePages + 1);
    }

    // 添加第一页
    if (start > 1) {
      pages.push(this.createPageButton(1));
      if (start > 2) {
        pages.push('<span class="pagination-ellipsis" aria-label="省略">...</span>');
      }
    }

    // 添加中间页
    for (let i = start; i <= end; i++) {
      pages.push(this.createPageButton(i, i === this.currentPage));
    }

    // 添加最后一页
    if (end < this.totalPages) {
      if (end < this.totalPages - 1) {
        pages.push('<span class="pagination-ellipsis" aria-label="省略">...</span>');
      }
      pages.push(this.createPageButton(this.totalPages));
    }

    return pages.join('');
  }

  /**
   * 渲染下一页按钮
   */
  renderNext() {
    if (this.currentPage >= this.totalPages) return '';
    return `
      <button 
        data-page="${this.currentPage + 1}" 
        class="pagination-btn pagination-next"
        aria-label="下一页"
      >
        下一页 ›
      </button>
    `;
  }

  /**
   * 渲染末页按钮
   */
  renderLast() {
    if (this.currentPage >= this.totalPages) return '';
    return `
      <button 
        data-page="${this.totalPages}" 
        class="pagination-btn pagination-last"
        aria-label="最后一页"
        title="最后一页"
      >
        »
      </button>
    `;
  }

  /**
   * 创建页码按钮
   */
  createPageButton(pageNum, isActive = false) {
    const activeClass = isActive ? ' active' : '';
    return `
      <button 
        data-page="${pageNum}" 
        class="pagination-btn${activeClass}"
        ${isActive ? 'aria-current="page"' : ''}
        aria-label="第${pageNum}页"
      >
        ${pageNum}
      </button>
    `;
  }

  /**
   * 跳转到指定页
   */
  goToPage(page) {
    if (page < 1 || page > this.totalPages) return;
    
    this.currentPage = page;
    this.render();
    this.onChange(page);
    
    // 平滑滚动到顶部
    const mainContent = document.getElementById('main-content');
    if (mainContent) {
      mainContent.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  /**
   * 上一页
   */
  prev() {
    if (this.currentPage > 1) {
      this.goToPage(this.currentPage - 1);
    }
  }

  /**
   * 下一页
   */
  next() {
    if (this.currentPage < this.totalPages) {
      this.goToPage(this.currentPage + 1);
    }
  }

  /**
   * 更新总页数
   */
  setTotalPages(total) {
    this.totalPages = total;
    if (this.currentPage > total) {
      this.currentPage = total;
    }
    this.render();
  }

  /**
   * 获取当前状态
   */
  getState() {
    return {
      currentPage: this.currentPage,
      totalPages: this.totalPages,
      hasNext: this.currentPage < this.totalPages,
      hasPrev: this.currentPage > 1
    };
  }
}

/**
 * 内容加载器（配合分页使用）
 */
class ContentLoader {
  constructor(options = {}) {
    this.baseUrl = options.baseUrl || '/content';
    this.cache = new Map();
    this.loading = false;
  }

  /**
   * 加载内容
   */
  async load(path, page = 1) {
    if (this.loading) return null;
    
    const cacheKey = `${path}:${page}`;
    if (this.cache.has(cacheKey)) {
      return this.cache.get(cacheKey);
    }

    this.loading = true;
    
    try {
      const response = await fetch(`${this.baseUrl}${path}?page=${page}`);
      if (!response.ok) throw new Error('加载失败');
      
      const data = await response.json();
      this.cache.set(cacheKey, data);
      return data;
    } catch (error) {
      console.error('内容加载错误:', error);
      throw error;
    } finally {
      this.loading = false;
    }
  }

  /**
   * 预加载相邻页面
   */
  preloadAdjacent(path, currentPage) {
    if (currentPage > 1) {
      this.load(path, currentPage - 1).catch(() => {});
    }
    if (currentPage < 10) { // 假设最多 10 页
      this.load(path, currentPage + 1).catch(() => {});
    }
  }

  /**
   * 清空缓存
   */
  clearCache() {
    this.cache.clear();
  }
}

// 导出（如果使用模块系统）
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { PaginationController, ContentLoader };
}
