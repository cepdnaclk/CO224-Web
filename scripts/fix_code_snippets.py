import re

def fix_code_snippets(filepath):
    """Convert paragraph-based code snippets to proper pre/code blocks."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Check if this is a sequence of <p> lines that look like code
        # Pattern 1: Lines with dashes (bullet points in code)
        # Pattern 2: Lines that look like code statements
        if stripped.startswith('<p>-') or (
            stripped.startswith('<p>') and 
            not stripped.startswith('<p><strong>') and
            i + 1 < len(lines) and
            (lines[i+1].strip().startswith('<p>-') or
             (lines[i+1].strip().startswith('<p>') and 
              not lines[i+1].strip().startswith('<p><strong>') and
              ':' in stripped or '=' in stripped or '->' in stripped or 'If' in stripped))
        ):
            # Start collecting code block
            code_lines = []
            indent = line[:len(line) - len(line.lstrip())]
            
            # Collect all sequential <p> lines that are code-like
            while i < len(lines):
                current = lines[i].strip()
                
                # Stop if we hit a heading or wrapped strong tag
                if (current.startswith('<h') or 
                    current.startswith('<p><strong>') or
                    current.startswith('<ul>') or
                    current.startswith('<ol>') or
                    current.startswith('<div') or
                    current.startswith('<strong>') or
                    current == ''):
                    break
                
                # Extract content from <p> tags
                if current.startswith('<p>') and current.endswith('</p>'):
                    content_match = re.match(r'<p>(.*?)</p>', current)
                    if content_match:
                        text = content_match.group(1)
                        # Remove leading dash if present
                        if text.startswith('- '):
                            text = text[2:]
                        code_lines.append(text)
                        i += 1
                else:
                    break
            
            # Write the code block
            if code_lines:
                result.append(f'{indent}<pre><code>')
                for code_line in code_lines:
                    result.append(code_line)
                result.append(f'{indent}</code></pre>')
            continue
        
        result.append(line)
        i += 1
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result))
    
    print(f"Fixed code snippets in {filepath}")

if __name__ == "__main__":
    fix_code_snippets(r"d:\Academics\Projects\isuru sir\CO224-Web\Lectures\html\lecture-09.html")
    fix_code_snippets(r"d:\Academics\Projects\isuru sir\CO224-Web\Lectures\html\lecture-10.html")
    print("Done!")
