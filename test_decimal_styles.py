from taka_number import TakaConverter

# Test both decimal styles in Bangla
traditional = TakaConverter(lang="bn", currency="টাকা", extension="মাত্র")
decimal = TakaConverter(lang="bn", currency="টাকা", extension="মাত্র", decimal_style="decimal")

test_numbers = [
    42.25,
    100.50,
    235.75,
    1042.42
]

print("Comparing decimal styles in Bangla:")
print("-" * 50)
for num in test_numbers:
    print(f"Number: {num}")
    print(f"Traditional style: {traditional.convert_number(num)}")
    print(f"Decimal style:     {decimal.convert_number(num)}")
    print("-" * 50)
