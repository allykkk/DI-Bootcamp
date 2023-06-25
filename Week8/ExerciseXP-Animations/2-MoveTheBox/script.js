
function myMove() {
    const container = document.querySelector('#container');
    const animateBox = document.querySelector('#animate')
    let postion = 0;
    const interval = setInterval(move, 1);

    function move() {
        // maximum distance for the red box 
        if (postion === container.offsetWidth - animateBox.offsetWidth) {
            clearInterval(interval);
        }
        else {
            postion++;
            animateBox.style.left = postion + 'px';
        }
    }
}


function reset() {
    const animateBox = document.querySelector('#animate');
    animateBox.style.left = '0px';
}