// let myArray = [1, 2, 3, 4];
// //const myOtherArray = myArray.slice();
// const myOtherArray = [].concat(...myArray)
// myArray.pop();
// console.log(myOtherArray);

// myArray = [1, 2];
// console.log(myOtherArray);


// function concat(list, other) {

//     return_list = []

//     for (let i = 0; i < list.length; i += 1){
//         return_list.push(list[i])

//     }

//     if (Array.isArray(other)) {
//         let start = list.length
//         let end = start + other.length
//         let counter = 0;
//         for (let i = start; i < end; i+= 1) {
//             return_list[i] = other[counter]
//             counter += 1
//         }
//     }
//     else {

//         return_list[return_list.length] = other
        
//     }

//     return return_list
// }
// const obj = { a: 2, b: 3 };
// const arr1 = [1, 2, 3];
// const arr2 = [4, 5, obj];
// const arr3 = concat(arr1, arr2);

// console.log(arr3)

// console.log(concat([2, 3], 'four'))

// function concat(...args) {
//     const newArray = []

//     for (let argIndex = 0; argIndex < args.length; argIndex += 1) {
//         let currentArg = args[argIndex]
//         if (Array.isArray(currentArg)) {
//             let arraySize = currentArg.length
//             for (let arrayIndex = 0; arrayindex < arraySize; arrayIndex +=1) {
//                 newArray[newArray.length] = currentArg[arrayIndex]
//             }
//         }
//         else {
//             newArray[newArray.length] = currentArg
//         }
//     }

//     return newArray
// }


// function pop(list) {
    
//     if (list.length <= 0) {
//         return undefined
//     }
//     returnValue = list[list.length - 1]
//     let length = list.length - 1
//     list.length = length

//     return returnValue
// }

// function push(list, ...values) {
//     if (values.length === 0) {
//         return list.length
//     }
//     if (Array.isArray(values[0])) {
//         let length = list.length;
//         for (let i = 0; i < values[0].length; i += 1) {
//             list[list.length] = values[0][i]
//             length += 1
//         }

//         return list.length
//     }

//     for (let i = 0; i < values.length; i += 1) {
//         list[list.length] = values[i]
//     }
//     return list.length
// }

// pop
// const array1 = [1, 2, 3];
// console.log(pop(array1));                        // 3
// console.log(array1);                // [1, 2]
// pop([]);                           // undefined
// console.log(pop([1, 2, ['a', 'b', 'c']]));      // ["a", "b", "c"]

// push
// const array2 = [1, 2, 3];
// push(array2, 4, 5, 6);              // 6
// console.log(array2);                // [1, 2, 3, 4, 5, 6]
// console.log(push([1, 2], ['a', 'b']));          // 3
// push([], 1);                       // 1
// push([]);                          // 0

// function reverse(inputForReversal) {
//   // ...
    
//     let result = ""
//     if (Array.isArray(inputForReversal)) {
//         let result = []

//         for (let i = inputForReversal.length -1 ; i >= 0; i -= 1) {
//             result.push(inputForReversal[i])
//         }
//         return result
//     }

//     for (let i = inputForReversal.length -1 ; i >= 0; i -= 1) {
//             result = inputForReversal[i] + result
//         }
//         return result
// }



// reverse('Hello');           // "olleH"
// reverse('a');               // "a"
// console.log(reverse([1, 2, 3, 4]));      // [4, 3, 2, 1]
// reverse([]);                // []

// const array = [1, 2, 3];
// reverse(array);             // [3, 2, 1]
// array;                      // [1, 2, 3]


// function shift(list) {
//     if (list.length === 0) {
//         return undefined
//     }

//     let firstElement = list[0]
//     //let counter = 1
//     // for (let i = 0; i < list.length; i += 1) {
//     //     list.splice(0,1, list[counter])
//     //     counter += 1
//     // }
//     let value = list.splice(0,1)

//     return value
// }

// shift([1, 2, 3]);                // 1
// shift([]);                       // undefined
// shift([[1, 2, 3], 4, 5]);        // [1, 2, 3]
// const testArray = [1, 2, 3];
// shift(testArray);                // 1
// console.log(testArray)

// function unshift(list, ...element) {

//     let newList = []

//     for (let i = 0; i < element.length; i +=1) {
//         list.splice(i, 0, args[i])
//     }
    
//     // for (let i = 0; i < list.length; i += 1) {
//     //     newList.push(list[i])
//     // }
//     // list = newList
    
//     return list.length;
// }
// const testArray = [1, 2, 3];
// unshift(testArray, 5);           // 3
// console.log(testArray);      

function areArraysEqual(array1, array2) {
    if (array1.length !== array2.length) {
        return false
    }

    values = array1.slice()

    for (let i=0; i < array1.length; i+= 1) {
        if (values.indexOf(array2[i]) !== -1) {
            values.splice(values.indexOf(array2[i]), 1)
        } else {
         
            return false
        }
    }
    return true
}

console.log(areArraysEqual([1, 2, 3], [3, 2, 1])); 