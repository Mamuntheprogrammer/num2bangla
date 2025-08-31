from taka_number import taka, TakaConverter

# Test 1: Basic English conversion
print("\nTest 1: Basic English conversion")
print(taka(200))  # Default English

# Test 2: Basic Bangla conversion
print("\nTest 2: Basic Bangla conversion")
converter_bn = TakaConverter(lang="bn", currency="টাকা", extension="মাত্র")
print(converter_bn.convert_number(200))

# Test 3: Decimal points in English
print("\nTest 3: Decimal points in English")
converter_en = TakaConverter(lang="en", currency="BDT", extension="Only")
print(converter_en.convert_number(200.25))  # With 25 paisa
print(converter_en.convert_number(200.5))   # With 50 paisa
print(converter_en.convert_number(200.75))  # With 75 paisa

# Test 4: Decimal points in Bangla
print("\nTest 4: Decimal points in Bangla")
converter_bn = TakaConverter(lang="bn", currency="টাকা", extension="মাত্র")
print(converter_bn.convert_number(200.25))  # With 25 paisa
print(converter_bn.convert_number(200.5))   # With 50 paisa
print(converter_bn.convert_number(200.75))  # With 75 paisa

# Test 5: Multiple numbers at once
print("\nTest 5: Multiple numbers at once")
print(taka(200.25, 100.50, 300.75))

# Test 6: Custom currency and extension
print("\nTest 6: Custom currency and extension")
converter_custom = TakaConverter(lang="en", currency="USD", extension="Only")
print(converter_custom.convert_number(200.25))

# Test 7: Large numbers with decimals
print("\nTest 7: Large numbers with decimals")
large_number = 1234567.89
print("English:", TakaConverter(lang="en").convert_number(large_number))
print("Bangla:", TakaConverter(lang="bn", currency="টাকা", extension="মাত্র").convert_number(large_number))
