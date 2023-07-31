const isPrime = (number) => {
    if (number <= 1) {
        return false;
    }
    for (let divisor = 2; divisor <= Math.sqrt(number); divisor++) {
        if (number % divisor === 0) {
            return false;
        }
    }
    return true;
}

const capeHandler = (data) => {
    const n = parseInt(data);
    const result = isPrime(n);
    let ret;
    if (result) {
        ret = `${n} is prime`
    } else {
        ret = `${n} is NOT prime`
    }
    return ret;
};

module.exports = {
    capeHandler
};
