let brack = function(str){
 let stack = []
 let match = {
   '(':')',
   '{':'}',
   '[':']'
 }
 for(let i =0;i<str.length;i++){
   if(str[i]==='(' || str[i]==='{' || str[i] === '['){
    stack.push(str[i])
   }else{
     let last = stack.pop()
     if(str[i] !== match[last]){
       return false
     }
   }
 }
 if(stack.length !== 0){
   return false
 }
 return true
}
console.log(brack("[]{"))