@echo off
cd %~dp0

forfiles /m *.md /c "cmd /c echo @file && python printmd2html.py @file @fname.html"