from facebook import Facebook

api_key = 'Your App API Key'
secret  = 'Your App Secret Key'

session_key = 'your infinite Session key of user'

fb = Facebook(api_key, secret)
fb.session_key = session_key