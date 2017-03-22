from app import app
from flask import render_template, request
import requests
@app.route('/feeds/', methods = ['POST','GET'])
def home():

	tag = None
	if request.method == 'POST':
		tag = request.form['tag']

	feeds = {}
	images = []
	res = requests.get("https://api.flickr.com/services/feeds/photos_public.gne", params={'format':'json','nojsoncallback':1})
	try:
		flickr_feeds = res.json()
	except:
		return render_template('feeds.html', feed=feeds)
	
	if tag:
		for item in flickr_feeds["items"]:
			if tag in item["tags"].lower():
				details = {}
				details["tag"] = item["tags"]
				details["image"] = item["media"]["m"]
				images.append(details)

	else:
		for item in flickr_feeds["items"]:
				details = {}
				details["tag"] = item["tags"]
				details["image"] = item["media"]["m"]
				images.append(details)	

	feeds["images"] = images
	return render_template('feeds.html', feed=feeds)