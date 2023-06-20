
// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out this tutorial of nested loops).
// Do this Daily Challenge by yourself, without looking at the answers on the internet.

// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *



// One Loop Solution 
function printPattern(rows){
    let pattern= '';
    for (i=1;i<=rows;i++){
        pattern += "* "
        console.log(pattern);
    }
}

printPattern(6)


// Nested Loop Solution 
function printWithNestedLoops(rows) {
for (let i = 1; i <= rows; i++) {
    let pattern = '';
    for (let j = 1; j <= i; j++) {
    pattern += '* ';
    }
    console.log(pattern);
    }
}

printWithNestedLoops(8);
