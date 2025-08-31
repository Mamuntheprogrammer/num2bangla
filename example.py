from num2bangla import taka, TakaConverter

# Test in English
print(taka(200))  # Two Hundred BDT Only

# Test in Bangla
converter = TakaConverter(lang="bn", currency="টাকা", extension="মাত্র")
print(converter.convert_number(200))  # দুই শত টাকা মাত্র

# Test multiple numbers
print(taka(200, 100, 300))  # ['Two Hundred BDT Only', 'One Hundred BDT Only', 'Three Hundred BDT Only']
