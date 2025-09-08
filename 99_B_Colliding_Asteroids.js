// ------------------------------------------------------------
// Problem Statement
// ------------------------------------------------------------
// You are given an array of integers called "asteroids".
// Each integer represents an asteroid in space:
//   - A positive value means the asteroid is moving to the right.
//   - A negative value means the asteroid is moving to the left.
//
// When two asteroids moving in opposite directions collide:
//   - The smaller asteroid (by absolute value) will explode (removed).
//   - If both are the same size, both will explode.
//   - If they are moving in the same direction, they will never collide.
//
// The task is to simulate all asteroid collisions and return the
// state of the asteroids after all collisions have occurred.
// ------------------------------------------------------------


function collidingAsteriods(asteroids) {
    let resultStack = [];

    // Use a plain for loop
    for (let i = 0; i < asteroids.length; i++) {
        let asteroid = asteroids[i];

        // Case 1: Moving right → just push into stack
        if (asteroid > 0) {
            resultStack.push(asteroid);
        } else {
            // Case 2: Moving left → check collisions
            let asteroidDestroyed = false;  // track if asteroid survives

            // Keep checking while collisions are possible
            while (resultStack.length > 0 && resultStack[resultStack.length - 1] > 0) {
                let top = resultStack[resultStack.length - 1]; // last asteroid in stack
                let absAsteroid = Math.abs(asteroid);

                if (top > absAsteroid) {
                    // Top asteroid is bigger → current asteroid destroyed
                    asteroidDestroyed = true;
                    break;
                } else if (top === absAsteroid) {
                    // Both same size → destroy both
                    resultStack.pop();
                    asteroidDestroyed = true;
                    break;
                } else {
                    // Current asteroid is bigger → pop top and keep checking
                    resultStack.pop();
                }
            }

            // If asteroid not destroyed, push into stack
            if (!asteroidDestroyed) {
                resultStack.push(asteroid);
            }
        }
    }

    return resultStack;
}


// ------------------------------------------------------------
// Dummy Data Testing
// ------------------------------------------------------------

// Example 1 → Output: [5, 10]
console.log(collidingAsteriods([5, 10, -5]));

// Example 2 → Output: []
console.log(collidingAsteriods([8, -8]));

// Example 3 → Output: [10]
console.log(collidingAsteriods([10, 2, -5]));
