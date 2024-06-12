const mobile_block = document.getElementsByClassName('mobile-menu')[0];

const open_mobile = () => {
	document.body.style.overflow = 'hidden';
	mobile_block.classList.add('opened');
};

const close_mobile = () => {
	document.body.style.overflow = '';
	mobile_block.classList.remove('opened');
};
