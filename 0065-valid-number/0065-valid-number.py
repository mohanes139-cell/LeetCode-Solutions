class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_dot = False
        seen_exponent = False
        
        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True
            elif ch in ['+', '-']:
                # Sign is valid only at start or directly after 'e'/'E'
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False
            elif ch in ['e', 'E']:
                # Exponent can appear only once, and only after at least one digit
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False  # Must have digits following the exponent
            elif ch == '.':
                # Dot can appear only once, and cannot appear after an exponent
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False
                
        return seen_digit