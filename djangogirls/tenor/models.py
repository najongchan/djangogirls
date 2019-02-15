from django.db import models
import requests, json

class Tenor(models.Model):
    # set apikey and limit
    apikey = "2I7ZV8FE37VF"
    lmt = 20

    # load the user's anonymous ID from cookies or some other disk storage
    # anon_id = <from db/cookies>

    # else - first time user, grab and store their anonymous ID
    r = requests.get("https://api.tenor.com/v1/anonid?key=%s" % apikey)

    if r.status_code == 200:
        anon_id = json.loads(r.content)["anon_id"]
        # store in db/cookies for re-use later

    else:
        anon_id = ""

    # our test search
    search_term = models.CharField(max_length=100)

    def searchGifs(self, search_term):
        # get the top 8 GIFs for the search term
        self.search_term = search_term

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&anon_id=%s"
            % (self.search_term, self.apikey, self.lmt, self.anon_id)
        )

        if r.status_code == 200:
            # load the GIFs using the urls for the smaller GIF sizes
            top_8gifs = json.loads(r.content)

            # print(top_8gifs)

        else:
            top_8gifs = None

        return top_8gifs

    def sendDoorayGifMessage(self, searchTerm, imageUrl):
        dooraydata = {
            "botName": "Gif봇",
            "botIconImage": "https://tenor.com/assets/img/tenor-logo.svg",
            "text": searchTerm,
            "attachments": [
                {
                    "imageUrl": imageUrl
                }
            ]
        }
        chatRoomUrl = "https://hook.dooray.com/services/1590498595903871702/2412863634358095097/12aY-3YvTsmiwnERVJpA1A"
        headers = {'content-type': 'application/json'}
        res = requests.post(chatRoomUrl, data=json.dumps(dooraydata), headers=headers)

        return res
