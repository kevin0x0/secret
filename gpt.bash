OPENAI_API_KEY=

question=
proxy=

while [[ $# != 0 ]]; do
  case $1 in
    -p)
      shift
      proxy="-x http://127.0.0.1:"$1
      ;;
    *)
      question=$1
      ;;
  esac
  shift
done

if [[ question == "" ]]; then
  echo "please provide your question"
  exit 1
fi

body='{ "model": "gpt-3.5-turbo", "messages": [ { "role": "system", "content": "You are a helpful assistant." }, { "role": "user", "content": '\"$question\"' } ] }'

curl $proxy "https://api.openai.com/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d "$body"
