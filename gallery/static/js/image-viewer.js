"use strict";

/*
 * Image Viewer
 * Author: Gordienko Oleg - gordio.pp.ua
 */


function createElementWithClass(el, cl) {
	var e = document.createElement(el);
	e.className = cl;
	return e;
}

var Gallery = new function() {
	var self = this;
	// FiXME: scroll problem, recommend use `padding` > 50
	self.padding = 70;

	this.init = function(obj_id) {
		var gallery_el = document.getElementById(obj_id);
		var links = gallery_el.getElementsByTagName("a");
		for (var i = 0; i < links.length; i++) {
			// image?
			if (/.(jpg|jpeg|png|tiff|gif)$/i.test(links[i].href)) {
				links[i].addEventListener('click', function(ev) {
					if (ev.button == 0) {
						self.show(this.href, this.children[0]);
						ev.preventDefault();
					}
				});
			}
		}

	}

	this.show = function(img_src, from) {
		// if (!self.viewer) {
			// fullpage background
			self.box_bg = createElementWithClass('div', 'iw-bb');
			self.box_bg.onclick = self.hide;

			// box with image
			self.viewer = createElementWithClass('div', 'iw-vb');
			self.box_bg.appendChild(self.viewer);

			// image
			self.img = new Image();
			// important! need for activate resize
			self.img.src = "";
			self.img.onload = self.resize;
			self.img_el = new Image();
			self.viewer.appendChild(self.img_el);
		// }

		// reset position to center
		self.viewer.style.left = (from) ? from.offsetLeft - window.pageXOffset + "px" : "50%";
		self.viewer.style.top = (from) ? from.offsetTop - window.pageYOffset + "px" : "50%";
		self.viewer.style.width = (from) ? from.offsetWidth + "px" : 0;
		self.viewer.style.height = (from) ? from.offsetHeight + "px" : 0;

		self.img_el.src = self.img.src = img_src;

		document.body.appendChild(this.box_bg);
		window.addEventListener('resize', self.resize);
		document.addEventListener('keydown', self.keyevent);
	}

	this.hide = function(ev) {
		self.box_bg.parentNode.removeChild(self.box_bg);
		window.removeEventListener('resize', self.resize);
		document.removeEventListener('keydown', self.keyevent);
	}

	this.keyevent = function(ev) {
		var e = ev || window.event;

		switch(e.keyCode) {
			case 27: // ESC
			case 81: // 'q'
				self.hide();
				break;
		}
	}

	this.resize = function(ev) {
		var padd = self.padding;
		var iw = self.img.width, ih = self.img.height;
		var w = window.innerWidth - padd, h = window.innerHeight - padd;

		var border = (((iw * h) > (ih * w)) ? 0 : 1);

		var out_w = ( border ? ((iw * h) / ih) : w);
		var out_h = (!border ? ((ih * w) / iw) : h);
		var out_x = ( border ? ((w - out_w) >> 1) : 0);
		var out_y = (!border ? ((h - out_h) >> 1) : 0);

		self.viewer.style.left = Math.floor(out_x + padd/2) + "px";
		self.viewer.style.top = Math.floor(out_y + padd/2) + "px";
		self.viewer.style.width = Math.floor(out_w) + "px";
		self.viewer.style.height = Math.floor(out_h) + "px";
	}
}
