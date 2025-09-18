// function penultimate(string) {
//     value = string.split(' ')
//   return value[value.length - 2];
// }

// console.log(penultimate('last word'));                    // expected: "last"
// penultimate('Launch School is great!');      // expected: "is"


// function uniqueElements(arr) {
//     let uniqueValues = []

//     for (let i =0; i < arr.length; i += 1) {
//         if(uniqueValues.indexOf(arr[i]) === -1) {
//             uniqueValues.push(arr[i])
//         }
//     }

//     return uniqueValues
//   // …
// }

// console.log(uniqueElements([1, 2, 4, 3, 4, 1, 5, 4]));  // returns [1, 2, 4, 3, 5]


// function missing(list) {
//     result = []

//     for (let i = list[0]; i < list[list.length - 1]; i+= 1) {
//         if (list.indexOf(i) === -1) {
//             result.push(i)
//         }
//     }

//     console.log(result)
//     return result
// }


// missing([-3, -2, 1, 5]);                  // [-1, 0, 2, 3, 4]
// missing([1, 2, 3, 4]);                    // []
// missing([1, 5]);                          // [2, 3, 4]
// missing([6]);                             // []

// function countAlpha(chars) {

//     let count = 0;
//     let badChars = {
//         ".": ".",
//         ",": ",",
//         " ": " ", 
     
//         "'": "'",
//     }

//     for (let i = 0; i < chars.length; i += 1) {
//         if (!(chars[i] in badChars)) {
//             count += 1
//         }
//     }

//     return count


// }
// let value = "walk, don't run." // should return 11

// console.log(countAlpha(value))

// function stringToInteger(string) {
//     let num = 0;
//     const DIGITS = {
//   '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
//   '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
//     };
//     for (let i = 0; i < string.length; i += 1){
//         let value = DIGITS[string[i]]
//         num = num * 10 + value
//     }

//     return num
// }


// console.log(stringToInteger('4321'));      // 4321
// stringToInteger('570');       // 570

// function stringToSignedInteger(num) {
//     let first_element = num[0]

//     if (first_element === "-") {
//         num = num.split('').splice(1)
//         return stringToInteger(num) * -1
//     }
//     else if (first_element === "+"){
//         num = num.split('').splice(1)
//         return stringToInteger(num)
//     }


//     return stringToInteger(num)
// }

// console.log(stringToSignedInteger("570"))