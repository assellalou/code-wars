const countBits = (n) => {
  return (n >>> 0)
    .toString(2)
    .split("")
    .map(Number)
    .reduce(function (a, b) {
      return a + b;
    }, 0);
};
