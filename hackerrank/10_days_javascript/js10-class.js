// https://www.hackerrank.com/challenges/js10-class/problem

class Polygon{
    constructor(sides){        
        this.sides = sides
    }
    perimeter() {
        let sum = 0;        
        for(let i in this.sides){
            sum += parseInt(this.sides[i]);            
        }
        return sum;
    } 
}


const rectangle = new Polygon([10, 20, 10, 20]);
const square = new Polygon([10, 10, 10, 10]);
const pentagon = new Polygon([10, 20, 30, 40, 43]);

console.log(rectangle.perimeter());
console.log(square.perimeter());
console.log(pentagon.perimeter());