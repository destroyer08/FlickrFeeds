from app import app
from flask import render_template, request
import requests
@app.route('/feeds/', methods = ['POST','GET'])
def home():

	if request.method == 'POST':
		tag = request.form['tag']
		feeds = {'type':tag}
		return render_template('feeds.html', feed=feeds)

	feeds = {'type':"Default"}
	images = []
	res = requests.get("https://api.flickr.com/services/feeds/photos_public.gne", params={'format':'json','nojsoncallback':1})
	try:
		flickr_feeds = res.json()
	except:
		return render_template('feeds.html', feed=feeds)
	
	
	for item in flickr_feeds["items"]:
		details = {}
		details["image"] = item["media"]["m"]
		details["tag"] = item["tags"]
		images.append(details)

	feeds["images"] = images
	return render_template('feeds.html', feed=feeds)