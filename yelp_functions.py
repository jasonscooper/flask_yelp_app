# Provided by Yelp

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def print_businesses(term, location):

	auth = Oauth1Authenticator(
		consumer_key=os.environ['CONSUMER_KEY'],
		consumer_secret=os.environ['CONSUMER_SECRET'],
		token=os.environ['TOKEN'],
		token_secret=os.environ['TOKEN_SECRET']
	)

	client = Client(auth)

	params = {
		'term': term,
		'lang': 'en',
		'limit': 3
	}
	response = client.search(location, **params)
	
	businesses = []

	for business in response.businesses:
		# print(business.name)
		businesses.append({"name": business.name, 
			"rating": business.rating, 
			"phone": business.display_phone,
			"address": business.location.display_address
		})

	return businesses

# term = "food"
# location = 92116
# businesses = print_businesses(term, location)

# print(businesses)