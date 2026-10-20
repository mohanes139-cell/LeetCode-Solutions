class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        cur_line = []
        cur_len = 0  # Total length of words in cur_line (excluding spaces)

        for word in words:
            # cur_len + len(word) + len(cur_line) -> word chars + new word + at least 1 space per existing word
            if cur_len + len(word) + len(cur_line) > maxWidth:
                # Format and flush cur_line
                total_spaces = maxWidth - cur_len
                gaps = len(cur_line) - 1

                if gaps == 0:
                    # Single word in line: left-justify
                    res.append(cur_line[0] + " " * total_spaces)
                else:
                    base_space = total_spaces // gaps
                    extra = total_spaces % gaps
                    
                    line_str = []
                    for i in range(gaps):
                        line_str.append(cur_line[i])
                        # Extra space given to leftmost slots
                        spaces_to_add = base_space + (1 if i < extra else 0)
                        line_str.append(" " * spaces_to_add)
                    line_str.append(cur_line[-1])
                    
                    res.append("".join(line_str))

                cur_line = []
                cur_len = 0

            cur_line.append(word)
            cur_len += len(word)

        # Last line: left-justified with single space between words, padded on the right
        last_line = " ".join(cur_line)
        res.append(last_line.ljust(maxWidth))

        return res