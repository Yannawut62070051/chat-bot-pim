import json
data = json.load(open('./data/manga.json'))

def render_manga():
    for i in data:
        return manga_function(i['imageUrl'],i['url'],i['header'],i['description'])

def manga_function(imageUrl, url, header, description):
    return {
        "fulfillmentMessages": [
            {
                "payload": {
                    "line": {
        
                        "type": "flex",
                        "altText": "This is a Flex Message",
                        # bring JSON payload here
                        "contents": {
                                "type": "bubble",
                            "size": "kilo",
                            "hero": {
                                "type": "image",
                                "url": imageUrl,
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover",
                                "action": {
                                    "type": "uri",
                                    "uri": url
                                }
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": header,
                                        "weight": "bold",
                                        "size": "xl",
                                        "wrap": True
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "margin": "lg",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": description,
                                                        "size": "sm"
                                                    }
                                                ]
                                            },
                                            # {
                                            #     "type": "box",
                                            #     "layout": "baseline",
                                            #     "spacing": "sm",
                                            #     "contents": [
                                            #         {
                                            #             "type": "text",
                                            #             "text": "ลองดู",
                                            #             "size": "sm"
                                            #         }
                                            #     ]
                                            # },
                                        ]
                                    }
                                ]
                            }
                        }
                    }
                }
            }
        ]}