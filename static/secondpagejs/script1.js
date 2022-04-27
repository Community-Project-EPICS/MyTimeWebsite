const startingminutes=10;
let time=startingminutes*60;
const cd1=document.getElementById('countdown');
setInterval(updatecountdown,1000);
function updatecountdown()
{
     const min=Math.floor(time/60);
     let sec=time%60;
     

     if(min==10 && sec==0 )
      cd1.innerHTML=`${min}:0${sec}`;
      else if(min<10 && sec>=10)
       cd1.innerHTML=`0${min}:${sec}`;
       else if(min<10 && sec<10)
        cd1.innerHTML=`0${min}:0${sec}`;
     time--;

}
$(function(){
    var overlay = $('<div id="overlay"></div>');
    overlay.show();
    overlay.appendTo(document.body);
    
    setTimeout(function(){
        $('.popup').show();
    }, 5000);
    $('.close').click(function(){
    $('.popup').hide();
    overlay.appendTo(document.body).remove();
    
    return false;
    });
    
    $('.x').click(function(){
    $('.popup').hide();
    overlay.appendTo(document.body).remove();
    return false;
    });
    });
