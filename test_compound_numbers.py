from taka_number import TakaConverter

# Test Bangla compound numbers
converter = TakaConverter(lang="en", currency="টাকা", extension="মাত্র")

test_numbers = [
    25,    # পঁচিশ
    34,    # চৌত্রিশ
    45,    # পঁয়তাল্লিশ
    55,    # পঞ্চান্ন
    65,    # পঁয়ষট্টি
    75,    # পঁচাত্তর
    85,    # পঁচাশি
    95,    # পঁচানব্বই
]

print("Testing Bangla compound numbers:")
for num in test_numbers:
    print(f"{num}: {converter.convert_number(num)}")

# Test with decimal points
print("\nTesting decimal points:")
decimal_numbers = [250000.25, 34.50, 45.75]
for num in decimal_numbers:
    print(f"{num}: {converter.convert_number(num)}")
