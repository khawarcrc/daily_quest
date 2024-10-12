/**
 * Context: 
 * The company is trying to determine the most common customer rating. 
 * The majorityRating function identifies the rating that appears more than half the time.
 * 
 * Purpose: 
 * The company wants to understand customer sentiment by finding the rating that appears most frequently in customer reviews.
 * 
 * Output: 
 * The function outputs the majority rating, allowing the company to make data-driven decisions 
 * regarding customer feedback and product quality.
 */



function majorityRating(ratings) {
    // Initialize count to 0 and answer to null
    let count = 0;
    let answer = null;

    // Loop through each rating in the array
    for (let rating of ratings) {
        // If count is 0, set the current rating as the potential majority rating
        if (count === 0) {
            answer = rating;
        }

        // If the current rating is the same as the potential majority rating, increase count
        if (rating === answer) {
            count += 1;
        } else {
            // Otherwise, decrease count as this rating is different
            count -= 1;
        }
    }

    // Return the majority rating (appears more than n//2 times in the array)
    return answer;
}

// Real-world scenario: Finding the majority rating in product reviews
// Test case 1: Majority rating is 5, as it appears 3 times in the array of 5 ratings
let ratings1 = [5, 5, 3, 1, 5];
console.log("Majority Rating:", majorityRating(ratings1));  // Output: 5

// Test case 2: Majority rating is 4, as it appears 4 times in the array of 6 ratings
let ratings2 = [4, 4, 4, 1, 4, 1];
console.log("Majority Rating:", majorityRating(ratings2));  // Output: 4

// Test case 3: Majority rating is 2, as it appears 5 times in the array of 9 ratings
let ratings3 = [2, 2, 1, 1, 2, 2, 1, 2, 2];
console.log("Majority Rating:", majorityRating(ratings3));  // Output: 2
