# Documentation Builder

Documentation is generated into multiple different formats:

- [x] [Apple Help Book](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProvidingUserAssitAppleHelp/authoring_help/authoring_help_book.html)
- [x] Website Documentation
- [x] GitHub Markdown

To that end, a single source of truth is needed to generate the documentation.

I have decided to use JSON as:

- [x] It's easy to read
- [x] Easy to consume
- [x] Easily host-able

I didn't want to use a database as I feel it would hide details, and possibly have a cost.

## Generation

To generate the markdown for GitHub, we use the `python` file `generate....py`

### Inclusive wording

`python DocBuilder/scripts/checkDisallowedWords.py`

This will ensure that we're using inclusive language in the docs.

### Markdown

`python DocBuilder/scripts/buildMarkdownDocumentation.py -t -src -dst`

This will generate *.md files using the template.md file and the data from the .json files

### Apple Help Book

`python DocBuilder/scriptsbuildAppleHelpBook.py -t -src -dst`

This will generate an AppleHelpBook file

### GitHub Pages HTML Pages

`python DocBuilder/scripts/buildGitHubDocs.py -t -src -dst`

This will generate a Documentation Sitemap.xml file.

## GitHub Actions

These scripts are ran as GitHub Actions, so you dont have to run them yourself.