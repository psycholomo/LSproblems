// apples = 3
// bananas = 5

// console.log(apples == bananas)

function my_average(...nums) {
    let total = total_sum(...nums)
    //console.log(total)
    //console.log(typeof(nums.length))
    return total / nums.length
}

function total_sum(...nums) {
    let total = 0
    
    for (let i = 0; i < nums.length; i += 1) {
        total += nums[i];
        console.log(nums[i])
          }
    
    return parseInt(total)
}

console.log(my_average(1,2,3))