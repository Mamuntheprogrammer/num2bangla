# num2bangla

A Python package to convert numbers to Bengali/Bangla text and numerals, with support for currency formatting.

## Installation

```bash
pip install num2bangla
```

## Usage

```python
from num2bangla import taka, TakaConverter

# Basic usage with default settings (English)
result = taka(200)  # "Two Hundred BDT Only"

# Using Bangla (Traditional paisa style)
converter = TakaConverter(lang="bn", currency="টাকা", extension="মাত্র")
result = converter.convert_number(200.25)  # "দুই শত টাকা এবং পঁচিশ পয়সা মাত্র"

# Using Bangla (Decimal style)
converter = TakaConverter(lang="bn", currency="টাকা", extension="মাত্র", decimal_style="decimal")
result = converter.convert_number(42.25)  # "বিয়াল্লিশ দশমিক দুই পাঁচ টাকা মাত্র"

# Using Bangla numerical digits
converter = TakaConverter(numerical_digits="bn")
result = converter.convert_number(1234.56, return_numerical=True)  # "১২৩৪.৫৬"

# Combining Bangla text and numerals
converter = TakaConverter(
    lang="bn", 
    currency="টাকা", 
    extension="মাত্র", 
    decimal_style="decimal",
    numerical_digits="bn"
)
text_result = converter.convert_number(42.25)  # Text format: "বিয়াল্লিশ দশমিক দুই পাঁচ টাকা মাত্র"
numeral_result = converter.convert_number(42.25, return_numerical=True)  # Numeral format: "৪২.২৫"

# Multiple numbers at once
results = taka(200, 100, 300)  # Returns a list of converted numbers

# Customizing currency and extension
converter = TakaConverter(lang="en", currency="USD", extension="Only")
result = converter.convert_number(200)  # "Two Hundred USD Only"
```

## Features

- Convert numbers to words in Bangla or English
- Customize currency text (e.g., "Taka", "BDT", "টাকা")
- Customize extension text (e.g., "Only", "মাত্র")
- Support for multiple numbers at once
- Support for large numbers (up to crores)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
