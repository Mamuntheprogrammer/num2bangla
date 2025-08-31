import unittest
from num2bangla import taka, TakaConverter

class TestTakaConverter(unittest.TestCase):
    def test_english_conversion(self):
        converter = TakaConverter(lang="en", currency="BDT", extension="Only")
        self.assertEqual(converter.convert_number(200), "Two Hundred BDT Only")
        self.assertEqual(converter.convert_number(1234), "One Thousand Two Hundred Thirty-Four BDT Only")
        
    def test_bangla_conversion(self):
        converter = TakaConverter(lang="bn", currency="টাকা", extension="মাত্র")
        self.assertEqual(converter.convert_number(200), "দুই শত টাকা মাত্র")
        self.assertEqual(converter.convert_number(1234), "এক হাজার দুই শত চৌত্রিশ টাকা মাত্র")
        
    def test_multiple_numbers(self):
        results = taka(200, 100, 300)
        self.assertEqual(len(results), 3)
        self.assertEqual(results[0], "Two Hundred BDT Only")
        self.assertEqual(results[1], "One Hundred BDT Only")
        self.assertEqual(results[2], "Three Hundred BDT Only")
        
    def test_zero(self):
        converter_en = TakaConverter(lang="en", currency="BDT", extension="Only")
        converter_bn = TakaConverter(lang="bn", currency="টাকা", extension="মাত্র")
        self.assertEqual(converter_en.convert_number(0), "Zero BDT Only")
        self.assertEqual(converter_bn.convert_number(0), "শূন্য টাকা মাত্র")

    def test_decimal_numbers(self):
        converter_en = TakaConverter(lang="en", currency="BDT", extension="Only")
        converter_bn = TakaConverter(lang="bn", currency="টাকা", extension="মাত্র")
        converter_bn_decimal = TakaConverter(lang="bn", currency="টাকা", extension="মাত্র", decimal_style="decimal")
        
    def test_bangla_numerals(self):
        # Test Bangla numerical digits
        converter = TakaConverter(numerical_digits="bn")
        self.assertEqual(converter.convert_number(42.25, return_numerical=True), "৪২.২৫")
        self.assertEqual(converter.convert_number(1234.56, return_numerical=True), "১২৩৪.৫৬")
        
        # Test with different combinations
        converter_bn = TakaConverter(lang="bn", currency="টাকা", extension="মাত্র", numerical_digits="bn")
        converter_bn_decimal = TakaConverter(lang="bn", currency="টাকা", extension="মাত্র", 
                                          decimal_style="decimal", numerical_digits="bn")
        
        # Test English decimal
        self.assertEqual(
            converter_en.convert_number(200.25),
            "Two Hundred BDT And Twenty-Five Paisa Only"
        )
        
        # Test Bangla decimal (traditional paisa style)
        self.assertEqual(
            converter_bn.convert_number(200.25),
            "দুই শত টাকা এবং পঁচিশ পয়সা মাত্র"
        )
        
        # Test Bangla decimal (দশমিক style)
        self.assertEqual(
            converter_bn_decimal.convert_number(200.25),
            "দুই শত দশমিক দুই পাঁচ টাকা মাত্র"
        )
        
        # Test rounding
        self.assertEqual(
            converter_en.convert_number(200.256),
            "Two Hundred BDT And Twenty-Six Paisa Only"
        )
        
        # Test Bangla decimal with larger number
        self.assertEqual(
            converter_bn_decimal.convert_number(42.25),
            "বিয়াল্লিশ দশমিক দুই পাঁচ টাকা মাত্র"
        )

if __name__ == '__main__':
    unittest.main()
