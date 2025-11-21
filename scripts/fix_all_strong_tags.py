import re

def fix_strong_tags(filepath):
    """Wrap standalone <strong> tags in <p> tags."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    result = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Check if line contains <strong> but is NOT already wrapped
        if stripped.startswith('<strong>') and stripped.endswith('</strong>'):
            # Get the indentation
            indent = line[:len(line) - len(line.lstrip())]
            # Extract the content
            content_match = re.match(r'<strong>(.*?)</strong>', stripped)
            if content_match:
                result.append(f'{indent}<p><strong>{content_match.group(1)}</strong></p>\n')
            else:
                result.append(line)
        elif stripped.startswith('<strong>') and '</strong>' in stripped and not stripped.startswith('<li><strong>'):
            # Handle inline strong tags like: <strong>Text</strong>: More text
            indent = line[:len(line) - len(line.lstrip())]
            result.append(f'{indent}<p>{stripped}</p>\n')
        else:
            result.append(line)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(result)
    
    print(f"Fixed strong tags in {filepath}")

if __name__ == "__main__":
    fix_strong_tags(r"d:\Academics\Projects\isuru sir\CO224-Web\Lectures\html\lecture-09.html")
    fix_strong_tags(r"d:\Academics\Projects\isuru sir\CO224-Web\Lectures\html\lecture-10.html")
    print("Done!")
