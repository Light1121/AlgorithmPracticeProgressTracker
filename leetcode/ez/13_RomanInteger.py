class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        sum = 0  # Variable to store the running total
        last = 0  # Variable to store the value of the previous symbol
        
        # Loop through the Roman numeral string from right to left
        for symbol in reversed(s):
            # Get the value of the current symbol
            value = roman_values[symbol]
            # If the current value is smaller than the last value, we subtract it
            if value < last:
                sum -= value
            else:
                # Otherwise, we add it to the sum
                sum += value
            
            # Update last to the current value
            last = value
        
        return sum