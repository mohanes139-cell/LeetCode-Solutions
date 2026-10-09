class Solution:

  def minInsertions(self, s: str) -> int:
    insertions = 0
    open_count = 0
    i = 0
    n = len(s)

    while i < n:
      if s[i] == "(":
        open_count += 1
        i += 1
      else:
        # Check if we have consecutive '))'
        if i + 1 < n and s[i + 1] == ")":
          i += 2
        else:
          # Single ')', insert another ')' to make '))'
          insertions += 1
          i += 1

        # Match with an existing '(' or insert a new '('
        if open_count > 0:
          open_count -= 1
        else:
          insertions += 1

    # Any remaining '(' need two ')' each
    insertions += open_count * 2
    return insertions