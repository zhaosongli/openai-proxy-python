curl --location --request POST 'http://100.26.242.75:8000/v1/chat/completions' \
-H 'Content-Type: application/json' \
-d '{
"model": "text-davinci-003",
"temperature": 0.7,
"prompt": "什么是人工智能",
"messages": [{"role": "user", "prompt":"什么是人工智能"}]
}'