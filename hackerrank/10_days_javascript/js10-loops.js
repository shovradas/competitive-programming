// https://www.hackerrank.com/challenges/js10-loops/problem

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

function vowelsAndConsonants(s) {
    let vowels = ['a', 'e', 'i', 'o', 'u'];

    let c = [];
    for(let i=0; i<s.length; ++i){
        if(vowels.includes(s[i]))
            console.log(s[i]);
        else
            c.push(s[i]);
    }
    console.log(c.join('\n'));
}


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}