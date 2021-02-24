var xAngle = 0, yAngle = 0;

document.addEventListener('keydown',function(e)
{
    switch(e.keyCode){
        case37:
        yAngle -= 45;
        break;

        case38:
        xAngle += 45;
        break;

        case39:
        yAngle += 45;
        break;

        case40:
        xAngle -= 45;
        break;
    }

    $('#cube').css("webkit-transform","rotateX("+xAngle+"deg"), rotateY(+yAngle+"deg")); 
}, false);