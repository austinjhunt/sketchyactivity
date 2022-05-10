let CSRF_TOKEN;AOS.init({duration:800,easing:"slide",});$(document).ready(function(){(function($){"use strict";$(window).stellar({responsive:true,parallaxBackgrounds:true,parallaxElements:true,horizontalScrolling:false,hideDistantElements:false,scrollProperty:"scroll",});var fullHeight=function(){$(".js-fullheight").css("height",$(window).height());$(window).resize(function(){$(".js-fullheight").css("height",$(window).height());});};fullHeight();$(function(){$('[data-toggle="tooltip"]').tooltip();});$(".toast").toast({delay:3000,});$.Scrollax();var burgerMenu=function(){$(".js-colorlib-nav-toggle").on("click",function(event){event.preventDefault();var $this=$(this);if($("body").hasClass("offcanvas")){$this.removeClass("active");$("body").removeClass("offcanvas");}else{$this.addClass("active");$("body").addClass("offcanvas");}});};burgerMenu();var mobileMenuOutsideClick=function(){$(document).click(function(e){var container=$("#colorlib-aside, .js-colorlib-nav-toggle");if(!container.is(e.target)&&container.has(e.target).length===0){if($("body").hasClass("offcanvas")){$("body").removeClass("offcanvas");$(".js-colorlib-nav-toggle").removeClass("active");}}});$(window).scroll(function(){if($("body").hasClass("offcanvas")){$("body").removeClass("offcanvas");$(".js-colorlib-nav-toggle").removeClass("active");}});};mobileMenuOutsideClick();var contentWayPoint=function(){var i=0;$(".ftco-animate").waypoint(function(direction){if(direction==="down"&&!$(this).hasClass("ftco-animated")){i++;$(this).addClass("item-animate");setTimeout(function(){$("body .ftco-animate.item-animate").each(function(k){var el=$(this);setTimeout(function(){var effect=el.data("animate-effect");if(effect==="fadeIn"){el.addClass("fadeIn ftco-animated");}else if(effect==="fadeInLeft"){el.addClass("fadeInLeft ftco-animated");}else if(effect==="fadeInRight"){el.addClass("fadeInRight ftco-animated");}else{el.addClass("fadeInUp ftco-animated");}
el.removeClass("item-animate");},k*50,"easeInOutExpo");});},100);}},{offset:"90%"});};contentWayPoint();$(".image-popup").magnificPopup({type:"image",closeOnContentClick:true,closeBtnInside:false,fixedContentPos:true,mainClass:"mfp-no-margins mfp-with-zoom",gallery:{enabled:true,navigateByImgClick:true,preload:[0,1],},image:{verticalFit:true,},zoom:{enabled:true,duration:300,},});$(".popup-youtube, .popup-vimeo, .popup-gmaps").magnificPopup({disableOn:700,type:"iframe",mainClass:"mfp-fade",removalDelay:160,preloader:false,fixedContentPos:false,});})(jQuery);});function remove_portfolio_item(name){$.ajax({type:"POST",url:"/delete",data:{name:name,},success:function(data){location.reload();},});}
function timeStamp(){var now=new Date();var date=[now.getMonth()+1,now.getDate(),now.getFullYear()];var time=[now.getHours(),now.getMinutes(),now.getSeconds()];var suffix=time[0]<12?"AM":"PM";time[0]=time[0]<12?time[0]:time[0]-12;time[0]=time[0]||12;for(var i=1;i<3;i++){if(time[i]<10){time[i]="0"+time[i];}}
return date.join("/")+" "+time.join(":")+" "+suffix;}
function send_message_to_slack(userid){var message=$("#message").val();$.ajax({dataType:"json",type:"POST",url:"/messaging/"+userid,data:{message:message,},success:function(data){$("#message").val("");var inits=data["inits"];console.log(inits);var t=timeStamp();var newmsgcontainer=$("<div></div>").addClass("message_container").addClass("client_message_container");var newmsgtimestamp=$("<div></div>").addClass("message_timestamp").html(t);var newmsginits=$("<div></div>").addClass("inits").addClass("client_inits").html(inits);var newmsg=$("<div></div>").addClass("message").addClass("client_message").html(message);$(newmsgcontainer).append(newmsgtimestamp).append(newmsg).append(newmsginits);$("#chat-body").append(newmsgcontainer);console.log("All done...");},});}
if(window.location.href.indexOf("messaging")>-1){setInterval(function(){longpoll(user_id);},500);}
function longpoll(uid){$.ajax({url:"/messaging/"+uid,type:"GET",success:function(data){if(data["message"]!=""){var t=timeStamp();var inits="AH";var message=data["message"];var newmsgcontainer=$("<div></div>").addClass("message_container").addClass("super_message_container");var newmsgtimestamp=$("<div></div>").addClass("message_timestamp").html(t);var newmsginits=$("<div></div>").addClass("inits").addClass("super_inits").html(inits);var newmsg=$("<div></div>").addClass("message").addClass("super_message").html(message);$(newmsgcontainer).append(newmsgtimestamp).append(newmsg).append(newmsginits);$("#chat-body").append(newmsgcontainer);}},});}
if(page=="home"){console.log("Notifying...");jQuery.ajax({dataType:"json",processData:false,type:"POST",url:"/notify",});}else if(page=="login"||page=="signup"){}else if(page=="messaging"){$("html").css({height:"100%"});$("body").css({height:"100%"});}
function isScrolledIntoView(elem){var docViewTop=$(window).scrollTop();var docViewBottom=docViewTop+$(window).height();var elemTop=$(elem).offset().top;var elemBottom=elemTop+$(elem).height();return elemBottom<=docViewBottom&&elemTop>=docViewTop;}
let updateCartBadgeNumber=(newItemCount)=>{let cartBadge=document.querySelector(".cart-badge");if(newItemCount==0){cartBadge.classList.add("d-none");}else{cartBadge.textContent=newItemCount;cartBadge.classList.remove("d-none");}};let removeProductFromCheckoutTable=(productId)=>{let row=document.querySelector(`tr[data-productid='${productId}'`);removeFadeOut(row,1000);};function removeFadeOut(el,speed){var seconds=speed/1000;el.style.transition="opacity "+seconds+"s ease";el.style.opacity=0;setTimeout(function(){el.parentNode.removeChild(el);},speed);}
let removeFromCart=(btn,productId)=>{fetch("/remove-from-cart/",{method:"POST",headers:{"Content-Type":"application/json","X-CSRFToken":CSRF_TOKEN,},body:JSON.stringify({productId:productId}),}).then((response)=>response.json()).then((data)=>{console.log(data);document.querySelector(".toast-title").textContent="Item removed from cart";document.querySelector(".toast-body").textContent=data["result"];if("totalCartItems"in data){let totalCartItems=parseInt(data["totalCartItems"]);updateCartBadgeNumber(totalCartItems);}
if("cartTotalPrice"in data){let cartTotalPrice=data["cartTotalPrice"];document.querySelector("td.cart-total-price").textContent=`$${cartTotalPrice}`;}
removeProductFromCheckoutTable(productId);$("#toast").toast("show");});};let showAddToCartModal=(data)=>{let modal=document.querySelector(".commission-reference-image-modal");let form=modal.querySelector("form");form.querySelector("input#style").value=data["style"];form.querySelector("input#price").value=data["price"];form.querySelector("input#numSubjects").value=data["numSubjects"];if(data["style"]=="digital"){form.querySelector("input#size").setAttribute("disabled",true);form.querySelector("input#size").removeAttribute("required");}else{form.querySelector("input#size").removeAttribute("disabled");form.querySelector("input#size").setAttribute("required",true);form.querySelector("input#size").value=data["size"];}
form.querySelectorAll("input").forEach((el,i)=>{el.setAttribute("readonly",true);});document.querySelectorAll("#commission-reference-image-modal-form input.noch").forEach((el,i)=>{let orig=el.value;console.log(`original value = ${orig}`);el.removeEventListener("input");el.addEventListener("input",(event)=>{event.target.value=orig;});});$("#commission-reference-image-modal").modal("show");};let addToCart=(data)=>{fetch("/add-to-cart/",{method:"POST",headers:{"Content-Type":"application/json","X-CSRFToken":CSRF_TOKEN,},body:JSON.stringify(data),}).then((response)=>response.json()).then((data)=>{console.log(data);document.querySelector(".toast-title").textContent="New item added to cart";document.querySelector(".toast-body").textContent=data["result"];if("totalCartItems"in data){let totalCartItems=parseInt(data["totalCartItems"]);updateCartBadgeNumber(totalCartItems);}
$("#toast").toast("show");});};;