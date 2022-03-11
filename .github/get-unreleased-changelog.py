

def get_unreleased_changelog(filename):
    in_section = False
    result = ''
    for line in open(filename):
        if line.startswith('## [Unreleased]'):
            in_section = True
            continue
        elif (in_section and line.startswith('## ')):
            break
        if in_section:
            result += line
    return result

if __name__ == '__main__':
    print(get_unreleased_changelog('CHANGELOG.md'))
