


function big(){
    function sub1(){
        var x=7;
        console.log(`sub1: `,x)
        sub2();
    }
    function sub2(){
        var y=x;
        console.log("sub2:", y)
    }

    var x=8;
    sub1();
}

big()