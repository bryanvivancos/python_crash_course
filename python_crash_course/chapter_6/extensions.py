favorite_languages = {
    'jen':['python', 'rust'],
    'sarah':['c'],
    'edward':['rust','go'],
    'phil':['python','haskell'],
    'bryan':['python'],
    'alex':['ruby','c++']    
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is: {languages[0].title()}")