import os
import re
import glob

def audit_numbering(lectures_dir):
    print(f"Auditing HTML files in {lectures_dir}...\n")
    
    files = sorted(glob.glob(os.path.join(lectures_dir, "lecture-*.html")))
    
    for file_path in files:
        filename = os.path.basename(file_path)
        # Extract lecture number from filename (e.g., lecture-05.html -> 5)
        try:
            lecture_num = int(re.search(r'lecture-(\d+)\.html', filename).group(1))
        except:
            print(f"Skipping {filename}: Could not parse lecture number.")
            continue
            
        print(f"--- Checking {filename} (Lecture {lecture_num}) ---")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all headings with numbers
        # Regex looks for <h[2-4]> followed by a number pattern like 5.1, 5.1.2, etc.
        # We capture the tag, the number, and the title
        headings = re.findall(r'<(h[2-4])>(\s*(\d+(?:\.\d+)*)\s+.*?)</\1>', content, re.IGNORECASE)
        
        if not headings:
            print("  No numbered headings found.")
            continue
            
        last_h2 = 0
        last_h3 = 0
        last_h4 = 0
        
        # Track the current hierarchy
        current_h2 = None
        
        for tag, full_title, number_str in headings:
            # Parse the number string into parts
            parts = [int(p) for p in number_str.split('.')]
            
            # Check if the first part matches the lecture number
            if parts[0] != lecture_num:
                print(f"  [WARNING] Wrong Prefix: '{number_str}' in {tag} (Expected starting with {lecture_num})")
                
            # Check hierarchy and sequence
            if tag.lower() == 'h2':
                if len(parts) != 2:
                     print(f"  [INFO] H2 format check: '{number_str}' (Usually X.Y)")
                
                # Check sequence
                if parts[0] == lecture_num:
                    if parts[1] != last_h2 + 1:
                        print(f"  [WARNING] Gap/Order H2: Found {number_str} after {lecture_num}.{last_h2}")
                    last_h2 = parts[1]
                    last_h3 = 0 # Reset sub-counters
                    last_h4 = 0
                    current_h2 = parts[1]
                    
            elif tag.lower() == 'h3':
                if len(parts) != 3:
                     print(f"  [INFO] H3 format check: '{number_str}' (Usually X.Y.Z)")
                
                if parts[0] == lecture_num:
                    # Check if it belongs to current H2
                    if len(parts) > 1 and parts[1] != current_h2:
                         print(f"  [WARNING] Hierarchy Mismatch: {number_str} appears under H2 {lecture_num}.{current_h2}")
                    
                    if len(parts) > 2:
                        if parts[2] != last_h3 + 1:
                            print(f"  [WARNING] Gap/Order H3: Found {number_str} after ...{last_h3}")
                        last_h3 = parts[2]
                        last_h4 = 0
                        
            elif tag.lower() == 'h4':
                if len(parts) != 4:
                     print(f"  [INFO] H4 format check: '{number_str}' (Usually X.Y.Z.W)")
                     
                if parts[0] == lecture_num:
                     if len(parts) > 3:
                        if parts[3] != last_h4 + 1:
                            print(f"  [WARNING] Gap/Order H4: Found {number_str} after ...{last_h4}")
                        last_h4 = parts[3]

if __name__ == "__main__":
    audit_numbering(r"d:\Academics\Projects\isuru sir\CO224-Web\Lectures\html")
