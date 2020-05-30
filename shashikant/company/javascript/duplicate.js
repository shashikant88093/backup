let num = [1,1,2,5,5,4,8,7,7,9]
// for(let i=0;i<num.length;i++){
//     for(let j = i + 1;j<num.length;j++){
//         if(num[i]==num[j]){
           
//         }

        
//     }

// }
// let num2 = []
// len = num.length;
// for(let i =0;i<len;i++){
//     if(num2.indexOf(num[i])=== -1){
//         num2.push(num[i]);
//     }
// }
// console.log(num2)


//for of loop

// obj = {}
// for(let i of num){
//     obj[i] = true;

// }
// let b = Object.keys(obj);
// console.log(b)
console.log([... new Set(num)]);