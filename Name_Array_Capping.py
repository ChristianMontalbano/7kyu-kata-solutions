def word_fixer(names):
    fixed_list = []
    for name in names:
      fix = name.lower()
      final = fix.capitalize()
      fixed_list.append(final)
    return fixed_list

def main():
    names = ["REIMU", "maRisa,", "youmu", "YUKARI"]
    fixed_list = word_fixer(names)
    print(fixed_list)

main()

