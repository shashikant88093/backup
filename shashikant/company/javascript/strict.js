// 'use strict'
// console.log(a)
// var a = 10
// var bar = null;
// console.log(typeof bar === "object"); 
// console.log(typeof variable); //output undefined
// console.log(variable);// //error
function hoist() {
    a = 20;
  var  b = 100;//if there will be var before b than output will error for b
  }
   hoist();
  
 console.log(a); //output a =20

  console.log(b);  //output b = 100

// hoisted(); // Output: "This function has been hoisted."

// function hoisted() {
//   console.log('This function has been hoisted.');
// };

//for normal function hoisting can be done but for anymous function it is not applicable


//Function declarations are hoisted over variable declarations but not over variable assignments.
// var double =20;

// function double(num) {
    
//   return (num*2);
 
// }

// console.log(typeof double);

// var Frodo = new Hobbit();
// Frodo.height = 100;
// Frodo.weight = 300;
//console.log(Frodo); // Output: ReferenceError: Hobbit is not defined

// class Hobbit {
//   constructor(height, weight) {
//     this.height = height;
//     this.weight = weight;
//   }
// }
// console.log(a)
// a = 10