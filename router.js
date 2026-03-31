/**
 * 哈基偷知识库 - 简单路由
 * 直接使用浏览器默认行为，不拦截内部链接
 */

// 页面加载时处理
document.addEventListener('DOMContentLoaded', function() {
  // 移除所有 data-router 属性，让链接正常工作
  document.querySelectorAll('a[data-router]').forEach(link => {
    link.removeAttribute('data-router');
  });
  
  // 关闭加载动画
  const loading = document.getElementById('loading');
  if (loading) {
    loading.style.display = 'none';
  }
});

// 处理浏览器后退/前进
window.addEventListener('popstate', function() {
  location.reload();
});
