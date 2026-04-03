from pathlib import Path

path = Path('pi_digits.txt')
comment = path.read_text().rstrip()
print(comment)