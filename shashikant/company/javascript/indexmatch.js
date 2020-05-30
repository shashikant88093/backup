let arr = [7, 8, 3, 4, 8, 16];
for (let i = 0; i <= arr.length; i++) {
  for (j = i + 1; j <= arr.length; i++) {
    if (arr[i] == arr[j]) {
      if (arr[i] + arr[j] == 16) {
        console.log(i);
        
      }
    }
  }
}
