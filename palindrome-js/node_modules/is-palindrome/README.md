Is-Palindrome
=============

[![Build Status](https://travis-ci.org/jaredcacurak/is-palindrome.png)](https://travis-ci.org/jaredcacurak/is-palindrome)

A palindrome is a word, phrase, number, or other sequence of symbols or elements, whose meaning may be interpreted the same way in either forward or reverse direction.

## Installation
```
npm install is-palindrome --save
```

## Usage
```javascript
var isPalindrome = require('is-palindrome');

isPalindrome('racecar') === true;
isPalindrome(101) === true;
isPalindrome('!@#$#@!', false) === true;
```

## Tests
```
npm test
```

## Contributing

In lieu of a formal styleguide, take care to maintain the existing coding style.
Add unit tests for any new or changed functionality. Lint and test your code.

## Release History

* 0.1.0 Initial release
* 0.1.1 Tidy up package.json and test names
* 0.1.2 Get Travis CI buid to pass
* 0.1.3 Adhere to the [Node.js Style Guide](https://github.com/felixge/node-style-guide)
* 0.1.4 Add Travis CI build status badge
* 0.2.0 Confirm global property NaN is not a palindrome
* 0.2.1 Register as a Bower package
* 0.3.0 Convert to UMD