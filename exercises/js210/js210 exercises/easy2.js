//1

// function crunch(string) {
//     let result = ""

//     for (let i = 0; i < string.length; i += 1)

//         if (string[i] !== string[i + 1]) {
//             result = result + string[i]
//         }
//     console.log(result)
//     return result
// }
// console.log(crunch('ddaaiillyy ddoouubbllee'));    // "daily double"
// crunch('4444abcabccba');              // "4abcabcba"
// crunch('ggggggggggggggg');            // "g"
// crunch('a');                          // "a"
// crunch('');                           // ""

//2

// function logInBox(string) {
//     let length = string.length
//     console.log(printTopBottom(length))
//     console.log(printSides(length))
//     console.log(`| ${string} |`)
//     console.log(printSides(length))
//     console.log(printTopBottom(length))
// }

// function printTopBottom(length) {
//     let result = "+"
    
//     for (let i = 0; i < length +2; i += 1) {
//         result += "-"
//     }

//     return result + "+"
// }

// function printSides(length) {
//     let result = "|"
//     for (let i = 0; i < length +2; i += 1) {
//         result += " "
//     }

//     return result + "|"

// }

// logInBox('To boldly go where no one has gone before.');
// logInBox('')

// function stringy(num) {

//     let result = ""
//     for (let i =0; i < num; i += 1) {
//         if (i % 2 === 0) {
//             result += "1"
//         } else {
//             result += "0"
//         }
//     }
//     console.log(result)
//     return result
// }

// stringy(6);    // "101010"
// stringy(9);    // "101010101"
// stringy(4);    // "1010"
// stringy(7);    // "1010101"

//4

// function triangle(num) {
//     const STAR = "*"
//     const SPACE = " "
//     let result = ""

//     for (let i =1; i <= num; i += 1) {
//         let num_spaces = num - i
//         let stars = i

//         for (let j = 0; j < num_spaces; j += 1) {
//             result += SPACE
//         }

//         for (let j =0; j < stars; j += 1) {
//             result += STAR
//         }
//         result += "\n"
//     }
//     return result
// }

// console.log(triangle(5))

//5

// const noun = prompt("Enter a noun")
// const verb = prompt("Enter a verb:");
// const adjective = prompt("enter an adjective")
// const adverb = prompt("Enter an adverb")

// const sentence1 = `Do you ${verb} your ${adjective} ${noun} ${adverb}? Thats hilarious`

// console.log(sentence1)

//6
// function twice(num) {
//     let numString = String(num)
    
//     if (numString.length % 2 === 1) {
//         return num * 2
//     }

//     let leftHalf = numString.slice(0,(numString.length) / 2 )
//     let rightHalf = numString.slice((numString.length / 2))
    
//     return leftHalf === rightHalf ? num : num * 2
    
// }

// console.log(twice(103103))

//7

// function cleanUp(string) {
//     let letters = "abcdefghijklmnopqrstuvwxyz".split("")
//     let result = ""
//     for (let indx = 0; indx < string.length; indx += 1) {
//         let char = string[indx]

//         for (let letter = 0; letter < letters.length; letter += 1) {
//             if (char === letters[letter]) {
//                 result += char
//             } else {
//                 if (char === " ") {
//                     if (string[indx + 1] === " ") {
//                         continue
//                     }
//                     else {
//                         result += " "
//                         break
//                     }
//                 }
//             }
            
//         }

//     }

//     return result
// }

// console.log(cleanUp("---what's my +*& line?"));    // " what s my line "

//8

// function century(num) {
//     let value = Math.floor((num / 100) + 1)

//     if (num % 100 === 0) {
//         value -= 1
//     }
    
//     value = String(value)
//     prefixes = {
//         "12": "th",
//         "13": "th",
//         "14": "th",
//         "15": "th",
//         "16": "th",
//         "17": "th",
//         "18": "th",
//         "19": "th",
//         "0" : "th",
//         "1" : "st",
//         "2" : "nd",
//         "3" : "rd",
//     }

//     if (value.length >= 2) {
//         let sliced = value.slice(-2, value.length)
//         value += prefixes[sliced]
//     }
//     else {
//         let sliced = value.slice(-1, value.length)
//         value += prefixes[sliced]
//     }

//     return value

// }

// console.log(century(1127))