mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\n
runOnSave = true\n\
\n\
[theme]\n\
primaryColor='#00a8e8'\n\
backgroundColor='#00171f'\n\
secondaryBackgroundColor='#003459'\n\
textColor='#ffffff'\n\
font='monospace'\n\
"

 > ~/ .streamlit/config.toml