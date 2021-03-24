$("#actionc").click(function() {     //表情改变运行按钮
	var ze = 0 ;
	var ag=$("#ex6_Angry").slider().slider('getValue');
	var ea=$("#ex6_Contemptuous").slider().slider('getValue');
	var di=$("#ex6_Disgusted").slider().slider('getValue');
	var fe=$("#ex6_Fearful").slider().slider('getValue');
	var ha=$("#ex6_Happy").slider().slider('getValue');
	var sa=$("#ex6_Sad").slider().slider('getValue');
	var su=$("#ex6_Surprised").slider().slider('getValue');
	$.ajax({
		url:"/api/Test/setvalue",  
		type:"POST",
		data:JSON.stringify({                          
			"Angry":ag,          
			"Easy":ea,
			"Disgusted":di,
			"Fearful":fe,
			"Happy":ha,
			"Sad":sa,
			"Surprised":su,
			"ex13_Face":ze,              //脸的水平角度
			"ex13_Face2":ze,             //脸的竖直角度
			"Facew":ze,                  //引号里的参数和后端对应
			"Faceh":ze,
			"Beauty":ze,
			"Eyeo":ze,
			"Age":ze,
			"Sex":ze
		}),
		contentType: "application/json",
		dataType: "json", //后台处理后返回的数据格式
		success: function(data) {
			objurl=data.url
			$("#im2").attr("src", objurl+"?t="+Math.random());   
        }
	});
})

$("#actionr").click(function() {     //脸型调整运行按钮
	var ze = 0 ;
	var fa=$("#ex13_Face").slider().slider('getValue');
	var far=$("#ex13_Face2").slider().slider('getValue');
	var faw=$("#ex13_Facew").slider().slider('getValue');
	var fah=$("#ex13_Faceh").slider().slider('getValue');
	var be=$("#ex13_Facef").slider().slider('getValue');
	var ey=$("#ex13_Eyeo").slider().slider('getValue');
	var age=$("#ex13_Age").slider().slider('getValue');
	var se=$("#ex13_Sex").slider().slider('getValue');
	$.ajax({
		url:"/api/Test/setvalue",  
		type:"POST",
		data:JSON.stringify({                          
			"Angry":ze,          
			"Easy":ze,
			"Disgusted":ze,
			"Fearful":ze,
			"Happy":ze,
			"Sad":ze,
			"Surprised":ze,
			"ex13_Face":fa,              //脸的水平角度
			"ex13_Face2":far,             //脸的竖直角度
			"Facew":faw,                  //引号里的参数和后端对应
			"Faceh":fah,
			"Beauty":be,
			"Eyeo":ey,
			"Age":age,
			"Sex":se
		}),
		contentType: "application/json",
		dataType: "json", //后台处理后返回的数据格式
		success: function(data) {
			objurl=data.url
			$("#im2").attr("src", objurl+"?t="+Math.random());  
        }
	});
})
					
$("#download").click(function() {        
	let imgSrc = $("#im2").attr("src");
    download(imgSrc, "图片");
})
				   