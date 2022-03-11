import sys
import tempfile


def update_changelog(filename, version, date):
    new_content = ''
    for line in open(filename):
        if line.startswith('## [Unreleased]'):
            new_content += line
            new_content += '\n### Added\n\n### Changed\n\n### Fixed\n\n'
            new_content += '## [{version}] - {date}\n\n'
        else:
            new_content += line
    with open(filename, 'w+') as f:
        f.write(new_content)


if __name__ == '__main__':
    update_changelog('CHANGELOG.md', sys.argv[1], sys.argv[2])
