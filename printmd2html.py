import markdown
import sys
import re
import base64

input_file_name = sys.argv[1]
style_file_name = "includestyle.css" # Default stylesheet
output_file_name = sys.argv[2]

with open(style_file_name, "r", encoding="utf-8") as style_file:
    style_content = style_file.read()

with open(input_file_name, "r", encoding="utf-8") as input_file:
    input_content = input_file.read()

    # Abort if "noprint" comment is found
    found_noprint = re.findall(r'<!--\s*noprint\s*-->', input_content)
    if len(found_noprint) > 0:
        exit(0)

    # Insert base64 encoded image data
    found_macros = re.findall(r'(\$base64\([\'\"]([^\'\"]*)[\'\"]\))', input_content)
    for macro in found_macros:
        macro_pattern = macro[0]
        macro_path = macro[1]

        with open(macro_path, "rb") as macro_file:
            img_raw = macro_file.read()
            img_base64 = base64.b64encode(img_raw)
            input_content = input_content.replace(macro_pattern, img_base64.decode('ascii'))

    # Insert document confidentiality notice
    found_macros = re.findall(r'(\$docsec\([\'\"]([^\'\"]*)[\'\"]\))', input_content)
    for macro in found_macros:
        macro_pattern = macro[0]
        macro_class = macro[1].lower()

        if (macro_class == "confidential"):
            notice_color = "red"
        elif (macro_class == "internal"):
            notice_color = "blue"
        else:
            notice_color = "black"
        
        input_content = input_content.replace(macro_pattern, f"<p style=\"font-size: larger; font-weight: bold; background-color: {notice_color}; color: white; text-align: center; font-variant: small-caps;\">{macro_class}</p>")

    # Process markdown
    input_html = markdown.markdown(input_content, extensions=['tables', 'fenced_code', 'sane_lists', 'toc', 'footnotes'], output_format="html5", encoding="utf-8")

# Assemble HTML content
html = "<!DOCTYPE html> \
<html> \
    <head> \
        <style> \
" + style_content + " \
        </style> \
    </head> \
    <body> \
" + input_html + " \
    </body> \
</html>"

with open(output_file_name, "w", encoding="utf-8") as output_file:
    output_file.write(html)
