import re

def fix_code_blocks_in_file(filepath):
    """Fix malformed code blocks in lecture HTML files."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Strategy: Find all code blocks and reformat them properly
    # Pattern: ``<code> ... </code>`` with possible </code>`<code> in between
    
    # Step 1: Replace ``<code> with <pre><code>
    content = re.sub(r'``<code>', '<pre><code>', content)
    
    # Step 2: Remove continuation markers </code>`<code>
    content = re.sub(r'</code>`<code>', '', content)
    
    # Step 3: Replace </code>`` with </code></pre>
    content = re.sub(r'</code>``', '</code></pre>', content)
    
    # Step 4: Handle orphaned </code> that should have </pre>
    # Look for </code> not followed by </pre> and add it
    content = re.sub(r'</code>(\s*\n\s*<(?!pre|/code))', r'</code></pre>\1', content)
    
    # Step 5: Handle blocks that should be code but aren't
    # Convert paragraph sequences that look like code examples
    # Find patterns like: <strong>Example</strong>:\n\n<p>code line</p>
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed code blocks in {filepath}")

if __name__ == "__main__":
    fix_code_blocks_in_file(r"d:\Academics\Projects\isuru sir\CO224-Web\Lectures\html\lecture-09.html")
    fix_code_blocks_in_file(r"d:\Academics\Projects\isuru sir\CO224-Web\Lectures\html\lecture-10.html")
    print("Done!")

