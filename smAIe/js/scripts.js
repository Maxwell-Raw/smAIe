// JavaScript for themezinho
(function($) {
$(document).ready(function() {
	"use strict";
	  
 
 		// FANCYBOX	
		$('.fancybox').fancybox({
		  helpers: {
			overlay: {
			  locked: false
			}
		  }
		});
		
		
		// STELLAR PARALLAX
		$.stellar({
			horizontalScrolling: false,
			verticalOffset: 0,
			responsive:true
		});
		
		
		// OWL CAROUSEL		
 		$(".owl-carousel").owlCarousel({
			items:4,
			loop:true,
			nav:false,
			dots:true,
			autoplay:true,
			autoplayTimeout:3000,
			autoplayHoverPause:false,
			smartSpeed:450,
			responsive:{
			375:{
				items:2
			},
			768:{
				items:3
			},
			1024:{
				items:4,
			},
			1199:{
				items:4,
			}
		   }
	  	});
		
		
		// OWL SLIDER		
 		$(".owl-slider").owlCarousel({
			items:1,
			loop:true,
			nav:true,
			dots:false,
			autoplay:true,
			autoplayTimeout:3000,
			autoplayHoverPause:false,
			smartSpeed:850,
	  	});
 
 
 
		
 		// PAGE TRANSITION
		$('.transition').on('click', function(e) {
      	$('.transition-overlay').toggleClass("show-me");
	    });
		
		
		// TRANSITION DELAY
		$('.transition').on('click', function(e) {
    	e.preventDefault();                  
    	var goTo = this.getAttribute("href"); 
		setTimeout(function(){
         window.location = goTo;
    	},1000);       
		}); 
		
		
		// ISOTOPE FILTER
		$(window).load(function(){
   			var $container = $('.grid-masonry ');
     		$container.imagesLoaded( function(){
        	$container.masonry({
           itemSelector : '.grid-masonry li'
         	});
       		});
     	});
 		
 	
		// SHOWCASE GRIDS
		var n = document.getElementById("grid");
			if (n == null) {
		} 
		else {
		
		
		new GridScrollFx( document.getElementById( 'grid' ), {
			viewportFactor : 0.4
		});
		}
		
  
  		// HAMBURGER MENU
		  (function($) {
			$.fn.clickToggle = function(func1, func2) {
				var funcs = [func1, func2];
				this.data('toggleclicked', 0);
				this.click(function() {
					var data = $(this).data();
					var tc = data.toggleclicked;
					$.proxy(funcs[tc], this)();
					data.toggleclicked = (tc + 1) % 2;
				});
				return this;
			};
		}(jQuery));

		$('.hamburger').clickToggle(function() {
			$('body').addClass('body-overflow');
			setTimeout(function() {
			$('.hamburger').addClass('open');
			}, 0);
			setTimeout(function() {
			$('.nav-menu').addClass('open');
			}, 0);
			setTimeout(function() {
			$('.nav-menu ul li a').addClass('open');
			}, 0);
			}, function() {
			$('body').removeClass('body-overflow');
			setTimeout(function() {
			$('.hamburger').removeClass('open');
			}, 300);
			setTimeout(function() {
			$('.nav-menu').removeClass('open');
			}, 400);
			setTimeout(function() {
			$('.nav-menu ul li a').removeClass('open');
			}, 0);
		});
		
		
		// SCROLL ZOOM
		$(window).scroll(function() {
			var scroll = $(window).scrollTop();
			$(".header .int-header .bg").css({
			width: (100 + scroll/10)  + "%",
			top: -(scroll/20)  + "%",
			});
		});


});

		// WOW ANIMATIONS
		wow = new WOW(
      	{
       		animateClass: 'animated',
        	offset:       50
      	}
    	);
    	wow.init();



		// COUNTER EFFECT
		var n = document.getElementById("counter");
			if (n == null) {
		} 
		else {
		
		var lastWasLower = false;
			$(document).scroll(function(){
			
			var p = $( "#counter" );
			var position = p.position();
			var position2 = position.top;
		
			if ($(document).scrollTop() > position2-300){
			if (!lastWasLower)
				$('#1').html('38');
				$('#2').html('94');
				$('#3').html('51');
				$('#4').html('27');
		
			lastWasLower = true;
				} else {
			lastWasLower = false;
			}
			});		
		};
		
		
})(jQuery);