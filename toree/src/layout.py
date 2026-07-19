import os

def tree_xml(path, prefix=""):
    try:
        items = os.listdir(path)
    except:
        return ""
    
    items = sorted([i for i in items if not i.startswith('.')])
    result = ""
    
    for item in items:
        full_path = os.path.join(path, item)
        
        if os.path.isdir(full_path):
            sub_content = tree_xml(full_path, prefix + "  ")
            if sub_content.strip():
                result += f'{prefix}<dir name="{item}">\n'
                result += sub_content
                result += f'{prefix}</dir>\n'
            else:
                # Empty directory → self-closing
                result += f'{prefix}<dir name="{item}"/>\n'
        else:
            result += f'{prefix}<file name="{item}"/>\n'
    
    return result


def lay_3(path):
    """Print directory tree as XML"""
    print('<?xml version="1.0" encoding="UTF-8"?>')
    print(f'<tree path="{path}">')
    print(tree_xml(path, "  "), end="")
    print("</tree>")


# layout 2 tree-style
def lay_2(path, prefix=""):
    try:
        lists = os.listdir(path)
    except:
        return

    for i, list in enumerate(sorted(lists)):
        # hide .
        if list.startswith('.'): continue

        full_path = os.path.join(path, list)
        is_last = (i == len(lists) - 1)

        branch = "└── " if is_last else "├── "
        extension = "    " if is_last else "│   "

        if os.path.isdir(full_path):
            print(f"{prefix}{branch}D: {list}")
            lay_2(full_path, prefix + extension)
        else:
            print(f"{prefix}{branch}F: {list}")


# layout 1 toree-style
def lay_1(path, prefix=""):
    try:
        lists = os.listdir(path)
    except:
        return

    for i, list in enumerate(sorted(lists)):
        # hide .
        if list.startswith('.'): continue

        full_path = os.path.join(path, list)
        is_last = (i == len(lists) - 1)
        branch = "|__ " if is_last else "|-- "

        if (os.path.isdir(full_path)): # is die
            print(f"{prefix}{branch}D: {list}")
            lay_1(full_path, prefix + "    " if is_last else "|    ")
        else: # is file
            print(f"{prefix}{branch}F: {list}")
