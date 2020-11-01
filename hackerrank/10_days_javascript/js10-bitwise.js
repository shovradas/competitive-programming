// https://www.hackerrank.com/challenges/js10-bitwise/problem

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function getMaxLessThanK(n, k){
    // Bruteforce
    // let max = 0;
    // for(let i=1; i<n; ++i){
    //     for(let j=i+1; j<=n; ++j){
    //         let result = i&j;
    //         //console.log('i =', i, 'j =', j, 'i&j =', result)
    //         if(result<k && max<result){
    //             max = result;
    //         }
    //     }
    // }
    // return max;

    // Mathematical
    if((k | (k - 1)) > n)
        return k - 2;
    return k - 1;
}

function main() {
    const q = +(readLine());
    
    for (let i = 0; i < q; i++) {
        const [n, k] = readLine().split(' ').map(Number);
        
        console.log(getMaxLessThanK(n, k));
    }
}