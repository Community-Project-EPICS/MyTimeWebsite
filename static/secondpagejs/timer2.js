let min=59;
let sec=60;
const cd1=document.getElementById('countdown');
setInterval(updatecountdown,1000);
function updatecountdown()
{
    //  const min=Math.floor(time/60);
    //  let sec=time%60;
     
    //  if(min<=59 && sec)
    //  if(min==59 && sec==0 )
    //   cd1.innerHTML=`${min}:${sec}`;
    //   else if(min<59 && sec)
    //   else if(min<59 && sec>=10)
    //    cd1.innerHTML=`${min}:${sec}`;
    //    else if(min<59 && sec<59)
    //     cd1.innerHTML=`${min}:${sec}`;
        // if(h.value == 0 && m.value == 0 && s.value == 0){
        //     h.value = 0;
        //     m.value = 0;
        //     s.value = 0;
        // } else if(s.value != 0){
        //     s.value--;
        // } else if(m.value != 0 && s.value == 0){
        //     s.value = 59;
        //     m.value--;
        // } else if(h.value != 0 && m.value == 0){
        //     m.value = 60;
        //     h.value--;
        // }
    //  time--;
    if(sec!= 0 && sec>10){
            sec--;
            cd1.innerHTML=`${min}:${sec}`;

        } else
        if(sec!=0 && sec==10)
        {
            cd1.innerHTML=`${min}:${sec}`;
            sec--;
        } else
        if(sec!=0 && sec<10)
        {
            
            cd1.innerHTML=`${min}:0${sec}`;
            sec--;
        }
        
        // else if(sec<10)
        // {
        //     // sec--;
        //     // cd1.innerHTML=`${min}:0${sec}`;

        // }
        else if(min != 0 && sec == 0){
            sec = 59;
            min--;
            cd1.innerHTML=`${min}:${sec}`;
        // } else if( min == 0){
        //     m.value = 60;
            
        //     cd1.innerHTML=`${min}:${sec}`;

}
}