const isPalindrome = require('is-palindrome');

const capeHandler = (data) => {
    return isPalindrome(data.toString('utf8'));
};

module.exports = {
    capeHandler
};
