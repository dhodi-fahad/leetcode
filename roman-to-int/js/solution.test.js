const romanToInt = require('./solution');

test('III to equal 3', () => {
  expect(romanToInt("III")).toBe(3);
});

test('LVIII to equal 58', () => {
    expect(romanToInt("LVIII")).toBe(58);
});

test('MCMXCIV to equal 1994', () => {
    expect(romanToInt("MCMXCIV")).toBe(1994);
});