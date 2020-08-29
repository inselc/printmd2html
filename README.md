<!-- noprint -->

# printmd2html

Generate standalone HTML files from Markdown for easy distribution.

## Installation

1. Clone or download this repository
2. Install the required packages using `pip install -r requirements.txt`

## Usage

Run the "`make`" Batch script to export all Markdown files found in the current directory.

```
.\make
```

If you only want to process a single file, use the following syntax:

```
python printmd2html.py <input_md> <output_html>
```

The processed file names will be printed to `stdout`.

### Including image files

In order to produce a standalone HTML file, use the `$base64('<file>')` macro. The Python script will replace all these macros before processing the Markdown.

```
<img id="logo" src="data:image/png;base64, $base64('logo.png')"/>
```

### Confidentiality notice

The `$docsec('<class>')` macro will insert a prominent confidentiality notice into the document. Special formatting will be applied to select classes:

* "`confidential`" will use a red background color
* "`internal`" will use a blue background color

```
$docsec('confidential')
```

### Customization

The default stylesheet is located in `includestyle.css`. It will be included verbatim into the generated HTML file.

### VS Code Task

A *Visual Studio Code* Task configuration is included in the `.vscode` folder, for quick building.

### Excluding a file

If you want to prevent a file from being exported, insert the following comment anywhere in the file:

```
<!-- noprint -->
```