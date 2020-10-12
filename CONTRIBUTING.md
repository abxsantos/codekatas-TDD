# Contributon guidelines

## How Can I Contribute?

#### Suggest improvements!
Suggest improvements for the readme and this guideline! To do that just open an issue.

You can also open an issue to suggest improvements in the kata problems.

You can also open issues to discuss a given kata problem. Just check if one isn't open already before opening one yourself.

#### Add you own kata problem!
To do that create a new folder with the kata name in **snake_case** and add the given rules for the kata in a file written in markdown.

The markdown file itself must contain:

- A h1 with the name of the kata
- A h4 right below it giving credits to the author of the kata (if there is a link you can also hyperlink the name of the author)
- A main goal brief description
- A list or paragraph describing a set of rules for the kata. These rules can be optional, or a must for your kata.

#### Add the method you used for solving a kata problem!

All languages are welcome!

To add your kata method, add it inside the language specific folder inside the kata.

**If there is no folder for your language, just create a new one in lowercase.**

Inside the language specific folder, add a directory containing your method. This directory must have the kata name and your username separated by a dash.

Ex.: `supermarket-absantos`

Inside this folder you must add a src folder and a tests folder.

### Folder structure
The folder structure is as follows

```
codekatas-TDD
└── business_rules                          # Kata name in snake_case
    └── business_rules.md                   # Kata problem guidelines
    ├── javascript                          # Language specific folder
    │       └── business_rules-abxsantos    # Kata name - username
    │               └── src                 # Source folder containing code
    │                    └── ...            # Use whatever structure floats your boat here
    │               └── tests               # Tests folder
    │                    └── ...            # Use whatever structure floats your boat here
    │               └── checklist.md        # Cheklist with the rules you're using to solve the kata
    └── python                              # Language specific folder
    │       └── business_rules-abxsantos    
    │               └── src                 
    │                    └── ...            
    │               └── tests              
    │                    └── ... 
    │               └── checklist.md              
```                 