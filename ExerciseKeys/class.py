words = ['bicycle', 'radar', 'origin', 'tie', 'level', 'poop', 'solar', 'nun']
palindromes = []
for word in words:
	rev_w = "".join(reversed(word))
	if rev_w == word:
		palindromes.append(word)
print(sorted(palindromes))
