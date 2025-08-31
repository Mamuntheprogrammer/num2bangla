from taka_number import TakaConverter

# Test various combinations of Bangla text and numerical representations

# 1. Only Bangla numerals
converter_numerals = TakaConverter(numerical_digits="bn")
number = 1234.56
print(f"\n1. Plain Bangla numerals:")
print(f"Original: {number}")
print(f"Bangla numerals: {converter_numerals.convert_number(number, return_numerical=True)}")

# 2. Traditional style with Bangla text
converter_traditional = TakaConverter(
    lang="bn",
    currency="টাকা",
    extension="মাত্র",
    numerical_digits="bn"
)
print(f"\n2. Traditional style:")
print(f"Words only: {converter_traditional.convert_number(42.25)}")
print(f"Numerals: {converter_traditional.convert_number(42.25, return_numerical=True)}")

# 3. Decimal style with Bangla text
converter_decimal = TakaConverter(
    lang="bn",
    currency="টাকা",
    extension="মাত্র",
    decimal_style="decimal",
    numerical_digits="bn"
)
print(f"\n3. Decimal style:")
print(f"Words only: {converter_decimal.convert_number(42.25)}")
print(f"Numerals: {converter_decimal.convert_number(42.25, return_numerical=True)}")

# 4. Test with various numbers
test_numbers = [0, 1.5, 10.75, 100.25, 1000.99]
print(f"\n4. Various numbers in Bangla numerals:")
for num in test_numbers:
    print(f"{num} -> {converter_numerals.convert_number(num, return_numerical=True)}")
