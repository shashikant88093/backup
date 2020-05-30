let arr =[1,2,3,4,5,6,7]
let n = 3
for(let i =0;i<n;i++){
    n = arr.pop()
    arr.unshift(n)
}
console.log(arr)