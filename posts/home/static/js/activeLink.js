const activePage = window.location.pathname;
document.querySelectorAll('nav a').forEach(link => {
	if (link.pathname === activePage) {
		link.classList.add('active');
	}
});
