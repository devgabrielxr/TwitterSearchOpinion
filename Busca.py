from leia import SentimentIntensityAnalyzer 
import tweepy
import matplotlib.pyplot as plt

key = 'yxawZNg5Ggb46fMqRHw8bbDNU'
secret = 'hkM3wNZ5n6duudDBspZHjKp7X3OZMNIsWLZr785WszTKTEN37i'
token = '2965075335-oBNw3TJ5psoWEGBIslzBGd6RbZsEvfQIwZMO0ot'
token_secret = 'C5HuoaLaEaKW7oMSw8rS6Gx7WLCBmCG1eISJWjMQfEiCd'

autenticacao = tweepy.OAuthHandler(key, secret)
autenticacao.set_access_token(token, token_secret)     
twitter = tweepy.API(autenticacao)

analise_t = [] 
tweets = []
analisador = SentimentIntensityAnalyzer()
max_id = None

count = 0
while(True):
    resultados = twitter.search(q= "desmatamento", lang="pt", locale="BR", tweet_mode="extended", count= 100, max_id = max_id)
    for tweet in resultados:
        count += 1
        #print(tweet.full_text)
        analise = analisador.polarity_scores(tweet.full_text)
        analise_t.append(analise["compound"])
        #print(analise)
        max_id = tweet.id_str
    print("Qtd de tweets importados:",count)
    
    if(count >= 100):
        break


print(analise_t)
positivos = list(filter(lambda sentimento: sentimento >= 0, analise_t))
negativos = list(filter(lambda sentimento: sentimento < 0, analise_t))

grupos = [f'positivo({len(positivos)})', f'negativo({len(negativos)})']
values = [len(positivos), len(negativos)]

plt.subplot()
plt.bar(grupos, values)
plt.show()








