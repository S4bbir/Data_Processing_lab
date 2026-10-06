word = input("Enter a word or short sentence: ")

character_count = 0
vowel_count = 0
consonant_count = 0

for word in word:
    character_count += 1

    if word.lower() in "aeiou":
        vowel_count += 1

    if word.isalpha():
        consonant_count += 1

print(f"\nTotal Characters: {character_count}")
print(f"Total Vowels: {vowel_count}")
print(f"Total Consonants: {consonant_count}")