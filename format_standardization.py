```python
# Import necessary libraries
import re

def standardize(script):
    """
    Standardize the script to industry standards.
    """
    # Split the script into lines
    lines = script.split('\n')

    # Standardize each line
    standardized_lines = []
    for line in lines:
        # Standardize scene headings
        if line.upper() == line and line.endswith('.'):
            standardized_line = standardize_scene_heading(line)
        # Standardize action descriptions
        elif line.upper() != line and not line.startswith(' '):
            standardized_line = standardize_action_description(line)
        # Standardize character dialogues
        elif line.startswith(' '):
            standardized_line = standardize_character_dialogue(line)
        # Standardize parentheticals
        elif line.startswith('(') and line.endswith(')'):
            standardized_line = standardize_parenthetical(line)
        # Leave other lines as is
        else:
            standardized_line = line

        standardized_lines.append(standardized_line)

    # Join the standardized lines back into a script
    standardized_script = '\n'.join(standardized_lines)

    return standardized_script

def standardize_scene_heading(line):
    """
    Standardize a scene heading.
    """
    # Scene headings should be in all caps and end with a period
    standardized_line = line.upper()
    if not standardized_line.endswith('.'):
        standardized_line += '.'

    return standardized_line

def standardize_action_description(line):
    """
    Standardize an action description.
    """
    # Action descriptions should start with a capital letter
    standardized_line = line[0].upper() + line[1:]

    return standardized_line

def standardize_character_dialogue(line):
    """
    Standardize a character dialogue.
    """
    # Character names should be in all caps and dialogues should start with a capital letter
    character_name, dialogue = re.split(r'(?<=\w)\s', line, 1)
    standardized_line = character_name.upper() + ' ' + dialogue[0].upper() + dialogue[1:]

    return standardized_line

def standardize_parenthetical(line):
    """
    Standardize a parenthetical.
    """
    # Parentheticals should be in lowercase and enclosed in parentheses
    standardized_line = '(' + line[1:-1].lower() + ')'

    return standardized_line
```
