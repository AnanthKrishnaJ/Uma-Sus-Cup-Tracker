import sys

def restore_cups():
    with open('head_index.html', 'r', encoding='utf-16') as f:
        head_lines = f.readlines()
        
    with open('index.html', 'r', encoding='utf-8') as f:
        idx_lines = f.readlines()
        
    # Extract cups 1 to 22 from head_index.html
    # In head_index.html, line 1602 (index 1601) is the start of cup 1: "        {\n"
    # line 7212 (index 7211) is the end of cup 22: "        },\n"
    cups_to_restore = head_lines[1601:7212]
    
    # Check if they are correct
    if '"id": 1,' not in cups_to_restore[1]:
        print("Error: Cup 1 not found at expected position in head_index.html")
        print(cups_to_restore[:5])
        return
        
    if '"id": 22,' not in cups_to_restore[-275]: # roughly
        pass # just a check
        
    # Find insertion point in index.html
    # It should be after "  \"races\": [\n" which is around line 1842
    insert_idx = -1
    for i, line in enumerate(idx_lines):
        if '"races": [' in line:
            insert_idx = i + 1
            break
            
    if insert_idx == -1:
        print("Error: Could not find races array in index.html")
        return
        
    # Ensure we are not inserting duplicate cups
    if '"id": 1,' in idx_lines[insert_idx + 1]:
        print("Cups already exist?")
        return
        
    # Insert the cups
    idx_lines = idx_lines[:insert_idx] + cups_to_restore + idx_lines[insert_idx:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(idx_lines)
        
    print(f"Successfully inserted {len(cups_to_restore)} lines from head_index.html into index.html at line {insert_idx+1}")

if __name__ == '__main__':
    restore_cups()
