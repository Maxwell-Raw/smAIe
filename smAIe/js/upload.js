$(function(){
       $("#imfile").change(function(){
           var objUrl = getObjectURL(this.files[0]) ;
           //console.log("objUrl = "+objUrl) ;
           if (objUrl) {
             $("#im").attr("src", objUrl) ;
           }
          $.ajax({
	          url:"/api/Test/path",
	          type:"POST",
	          data:JSON.stringify({"imgpath":objUrl}),
              contentType : 'application/json;charset=utf-8'
          });
        }) ;
        //建立一個可存取到該file的url
        function getObjectURL(file) {
             var url = null;
             if (window.createObjectURL != undefined) { // basic
                  url = window.createObjectURL(file);
             } else if (window.URL != undefined) { // mozilla(firefox)
                  url = window.URL.createObjectURL(file);
             } else if (window.webkitURL != undefined) { // webkit or chrome
                  url = window.webkitURL.createObjectURL(file);
             }
                  return url;
         }
	     
})

$("#delete").click(function() {        //删除按钮
	//$("#imfile").val('');  
	$("#im").parent().remove(); 
	//document.getElementById("imfile")[0].value = null;
})

//$("#download").click(function() {        
//	let imgSrc = "C:\Users\2000514\Desktop\习题.jpg";
//    download(imgSrc, "资讯图片");
//})