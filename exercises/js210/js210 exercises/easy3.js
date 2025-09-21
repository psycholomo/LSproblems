
// let age = Math.floor(Math.random() * (201 - 1) + 1)
// console.log(age)

//2
// let numbers = ["25","15","20","17","23"]


// function searching (nums, value) {
    

//     for (let i = 0; i < nums.length; i += 1) {
//         if (parseInt(nums[i]) === value) {
//             return true
//         }
//     }


//     return false
// }

// console.log(searching(numbers,25))

// let date = new Date()
// let year = date.getFullYear()
// let currentAge = 30
// let retirementAge = 70
// let years = retirementAge - currentAge
// let retirementDate = year + years;

// console.log(`its ${year}. You will retire in ${retirementDate}`)

//3

// function isPalindrome(string) {
//     reversedString = string.split("").reverse().join("")

//     return reversedString === string
// }

// console.log(isPalindrome("madam"));               // true

//4
// function cleanString(input) {
//     let values = "abcdefghijklmnopqrstuvwxyz1234567890".split('')
//     input = input.toLowerCase()
//     let result = ''
//     for (let i = 0; i < input.length; i += 1) {
//         for (let j = 0; j < values.length; j += 1) {
//             if (input[i] === values[j]) {
//                 result += input[i]
//                 break;
//             }
//         }

//     }

//     return result
    
// }   

// function isRealPalindrome(string) {
//     cleanedString1 = cleanString(string)
//     console.log(cleanedString1)
//    /// cleanString(string).split('').reverse().join('')
//     return cleanedString1 === cleanString(string).split('').reverse().join('')
// }
// console.log(isRealPalindrome("Madam, I'm Adam"));  

//5

// function isPalindromicNumber(num) {
    
//     return String(num) === String(num).reverse()
// }

// function runningTotal(list) {

//     if (list.length === 0) {
//         return []
//     }
//     let result = [list[0]]

//     for (let i =1; i < list.length; i += 1) {
//         result[i] = list[i] + result[i -1]
//     }
//     console.log(result)
//     return result
// }
// runningTotal([2, 5, 13]);             // [2, 7, 20]
// runningTotal([14, 11, 7, 15, 20]);    // [14, 25, 32, 47, 67]
// runningTotal([3]);                    // [3]
// runningTotal([]);                     // []

//6

// function swap(word) {
// //console.log(word.slice(-1,word.length))
// let result = ""

// let arr = word.split(' ').map(ele => {
//     let firstLetter = ele[0]
//     let lastLetter = ele[ele.length -1]

//     return lastLetter + ele.slice(1, ele.length -1) + firstLetter

// })
// return arr.join(' ')
// }


// //swap('Oh what a wonderful day it is');
// console.log(swap("wonderful we"))

//7

// function wordSizes(word) {
//     let wordArr = word.split(" ")
//     let dict = {}

//     wordArr.forEach(ele => {
//         let length = ele.length
//        dict[length] = (dict[length] || 0) + 1;
// })

// return dict
// }

// wordSizes("Four score and seven")

// function wordSizes(word) {

//     words = word.split(' ')
//     result = {}

//     words.forEach(element => {
//         element = removeNonAlpha(element)
//         let length = element.length

//         result[length] = (result[length] || 0) + 1
//     })
//     return result
// }

// function removeNonAlpha(word) {
    
//     let result = ""
//         for (let i = 0; i < word.length; i += 1) {
//             let letter = word[i].toLowerCase()
        
//             if (checkLetter(letter)) {
//                 result += word[i]
               
//             }
 
//         }
    
//     return result
    
// }

// function checkLetter(letter) {
//     return letter >= "a" && letter <= "z"
// }


// console.log(wordSizes('Four score and seven.'));                       // { "3": 1, "4": 1, "5": 2 }
// wordSizes('Hey diddle diddle, the cat and the fiddle!');  // { "3": 5, "6": 3 }
// wordSizes("What's up doc?");                              // { "5": 1, "2": 1, "3": 1 }
// wordSizes('');                                            // {}