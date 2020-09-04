favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print(f"Sarah's favourite language is {favourite_languages['sarah'].title()}.")

for name in favourite_languages.keys():
    print(name.title())

for name in favourite_languages:
    print(name.title())

friends = ['phil', 'sarah']
for name in favourite_languages:
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favourite_languages:
    print("Erin, please take our poll!")

for name in sorted(favourite_languages):
    print(f"{name.title()}, thank you for taking  the poll.")

print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

print("The following languages have been mentioned (unique):")
for language in set(favourite_languages.values()):
    print(language.title())

# -----------------------------------------------------------------------------

favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
