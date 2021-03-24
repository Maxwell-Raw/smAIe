var tpj=jQuery;
var revapi647;
tpj(document).ready(function() {
	if(tpj("#rev_slider_647_1").revolution == undefined){
		revslider_showDoubleJqueryError("#rev_slider_647_1");
	}else{
		revapi647 = tpj("#rev_slider_647_1").show().revolution({
			sliderType:"standard",
			jsFileLocation:"js/",
			sliderLayout:"fullscreen",
			dottedOverlay:"none",
			delay:9000,
			navigation: {
							keyboardNavigation:"off",
							keyboard_direction: "horizontal",
							mouseScrollNavigation:"off",
 							mouseScrollReverse:"default",
							onHoverStop:"off",
							touch:{
								touchenabled:"on",
								swipe_threshold: 75,
								swipe_min_touches: 1,
								swipe_direction: "horizontal",
								drag_block_vertical: false
							}
							,
							arrows: {
								enable:true,
								hide_onmobile:false,
								hide_onleave:false,
								tmp:'',
								left: {
									h_align:"left",
									v_align:"center",
									h_offset:0,
									v_offset:0
								},
								right: {
									h_align:"right",
									v_align:"center",
									h_offset:0,
									v_offset:0
								}
							}
							,
							bullets: {
								enable:true,
								hide_onmobile:true,
								hide_under:768,
								style:"hermes",
								hide_onleave:false,
								direction:"horizontal",
								h_align:"center",
								v_align:"bottom",
								h_offset:0,
								v_offset:80,
								space:5,
								tmp:''
							}
						},
						responsiveLevels:[1240,1024,778,480],
						visibilityLevels:[1240,1024,778,480],
						gridwidth:[1240,1024,778,480],
						gridheight:[650,600,550,450],
						lazyType:"smart",
						parallax: {
							type:"scroll",
							origo:"enterpoint",
							speed:400,
							levels:[5,10,15,20,25,30,35,40,45,46,47,48,49,50,51,55],
							type:"scroll",
							disable_onmobile:"on"
						},
						shadow:0,
						spinner:"off",
						stopLoop:"on",
						stopAfterLoops:0,
						stopAtSlide:1,
						shuffle:"on",
						autoHeight:"off",
						disableProgressBar:"on",
						hideThumbsOnMobile:"off",
						hideSliderAtLimit:0,
						hideCaptionAtLimit:0,
						hideAllCaptionAtLilmit:0,
						debugMode:false,
						fallbacks: {
							simplifyAll:"off",
							nextSlideOnWindowFocus:"off",
							disableFocusListener:false,
						}
		 });
		}
	});	