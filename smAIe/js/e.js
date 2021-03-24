$("#ex6_Angry").slider();
$("#ex6_Angry").on("slide", function(slideEvt) {
	$("#ex6SliderVal1").text(slideEvt.value);
});

$("#ex6_Contemptuous").slider();
$("#ex6_Contemptuous").on("slide", function(slideEvt) {
	$("#ex6SliderVal2").text(slideEvt.value);
});

$("#ex6_Disgusted").slider();
$("#ex6_Disgusted").on("slide", function(slideEvt) {
	$("#ex6SliderVal3").text(slideEvt.value);
});

$("#ex6_Fearful").slider();
$("#ex6_Fearful").on("slide", function(slideEvt) {
	$("#ex6SliderVal4").text(slideEvt.value);
});

$("#ex6_Happy").slider();
$("#ex6_Happy").on("slide", function(slideEvt) {
	$("#ex6SliderVal5").text(slideEvt.value);
});

$("#ex6_Sad").slider();
$("#ex6_Sad").on("slide", function(slideEvt) {
	$("#ex6SliderVal6").text(slideEvt.value);
});

$("#ex6_Surprised").slider();
$("#ex6_Surprised").on("slide", function(slideEvt) {
	$("#ex6SliderVal7").text(slideEvt.value);
});

$("#ex13_Face").slider({
    ticks: [-4,0,4],
    ticks_labels: ['向左', '', '向右'],
});

$("#ex13_Face2").slider({
    ticks: [-4,0,4],
    ticks_labels: ['向下', '', '向上'],
});

$("#ex13_Facew").slider({
    ticks: [-4,0,4],
    ticks_labels: ['窄', '', '宽'],
});

$("#ex13_Faceh").slider({
    ticks: [-4,0,4],
    ticks_labels: ['短', '', '长'],
});

$("#ex13_Facef").slider({
    ticks: [-4,0,4],
    ticks_labels: ['粗短', '', '精致'],
});

$("#ex13_Eyeo").slider({
    ticks: [-4,0,4],
    ticks_labels: ['合', '', '开'],
});

$("#ex13_Age").slider({
    ticks: [-4,0,4],
    ticks_labels: ['年幼化', '', '老年化'],
});

$("#ex13_Sex").slider({
    ticks: [-4,0,4],
    ticks_labels: ['男性化', '', '女性化'],
});

/*$('#ex1_Eye').slider({
	formatter: function(value) {
		return value;
	}
});*/




