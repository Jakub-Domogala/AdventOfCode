class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Directory:
    def __init__(self, name, parent = None, subdirectories = [], files = []):
        self.name = name
        self.parent = parent
        self.subdirectories = subdirectories
        self.files = files
    
    def add_file(self, file):
        self.files.append(file)
    
    def add_dir(self, dir):
        self.subdirectories.append(dir)

    def print(self, tabs = 0):
        if tabs > 5:
            return
        for f in self.files:
            print("---" * tabs, f.name, " ", f.size, sep="")
        for d in self.subdirectories:
            print("---" * tabs, "dir -> ", d.name, sep="")
            d.print(tabs + 1)

def find(tab, name):
    for i, x in enumerate(tab):
        if x.name == name:
            return tab[i]
    return None


SUMMARY = 0
def search_for_dir_under_100000(dir):
    global SUMMARY
    filesum = sum([x.size for x in dir.files])
    dirsum = 0
    allsum = 0
    for x in dir.subdirectories:
        dirsum += search_for_dir_under_100000(x)
    allsum = filesum + dirsum
    if allsum <= 100000:
        SUMMARY += allsum
    return allsum

root = None
jumper = None
tabs = 0
lines = None
# LOAD TREE
with open("input7.txt") as file:
    lines = file.read().splitlines()
n = len(lines)
line_id = 0
while line_id < n:
    words = lines[line_id].replace("\n", "").split(sep=" ")
    
    # if jumper is not None:
    #     print(" " * tabs, words, jumper.name)
    # else:
    #     print(" " * tabs, words, "NONAME")
    # COMMANDS
    if words[0] == "$":

        # CD
        if words[1] == "cd":
            if words[2] == "/":
                if root is None:
                    root = Directory("/")
                jumper = root
                tabs = 0
            elif words[2] == "..":
                jumper = jumper.parent
                tabs -= 1
            else:
                tmp = find(jumper.subdirectories, words[2])
                if tmp is None:
                    tmp = Directory(words[2], jumper, [], [])
                    jumper.add_dir(tmp)
                jumper = tmp
                tabs += 1
            line_id += 1
            continue
            
        # LS
        elif words[1] == "ls":
            line_id += 1
            while line_id < n and lines[line_id].split(sep=" ")[0] != "$":
                words_in = lines[line_id].replace("\n", "").split(sep=" ")
                # print(" " * tabs, words_in, jumper.name)
                if words_in[0] == "dir":
                    tmp = find(jumper.subdirectories, words_in[1])
                    if tmp is None:
                        jumper.add_dir(Directory(words_in[1], jumper, [], []))
                    
                else:
                    tmp = find(jumper.files, words_in[1])
                    if tmp is None:
                        jumper.add_file(File(words_in[1], int(words_in[0])))
                line_id += 1

# OPERATIONS ON TREE
root.print()

total_used_space = search_for_dir_under_100000(root)
print("Answer:", SUMMARY)
                    
        