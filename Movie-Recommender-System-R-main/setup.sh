mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\n
runOnSave = true\n\
\n\
[theme]
primaryColor='#00a8e8'
backgroundColor='#00171f'
secondaryBackgroundColor='#003459'
textColor='#ffffff'
font='monospace'
" > ~/ .streamlit/config.toml