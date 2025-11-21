// function basicCallback(callback, num) {
//     setTimeout( () => {
//         callback(num)
//     }, 2000)
// }

// // Example usage:
// basicCallback((number) => {
//   console.log(number * 2);
// }, 5);
// // After 2 seconds, logs: 10

// function downloadFile(callback) {
//     console.log("Downloading file. . .")
//     setTimeout( () => {
//         callback()
//     }, 1500)
// }

// downloadFile(() => {
//     console.log("Download Complete")
// })

// // function processData(arr, callback) {

// //     arr.forEach(num => {
// //         setTimeout( () => {
// //             callback(num)
// //         },1000)
// //     })

// // }


// function waterfallOverCallbacks(arr, value) {
//     let valplaceholder = value
//     arr.forEach(element => {
//         valplaceholder = element(valplaceholder)
       
//     })
//      console.log(value)
//     return valplaceholder
// }

// // Example usage:
// const double = (x) => x * 2;
// waterfallOverCallbacks([double, double, double], 1);
// // Logs: 8


// Example usage:
function startCounter(count) {
  let counter = 0;
  const intervalId = setInterval(() => {
    counter += 1
    if (count(counter) === 5) {
        clearInterval(intervalId)
    }
  }, 1000)
  return count === 5;
};

function count (num) {
    console.log(num)
    return num
}
startCounter(count)

// Logs 1, 2, 3, 4, 5, then stops