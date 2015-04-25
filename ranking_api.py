import requests
import json as simplejson


def call_ranking_api(cards):
    data = {"cards": simplejson.dumps(cards)}
    r = requests.post('http://rainman.leanpoker.org/rank', data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    return simplejson.loads(r.content)


def main():
    ranking = call_ranking_api([{"rank":"5","suit":"diamonds"},
                               {"rank":"6","suit":"diamonds"},
                               {"rank":"7","suit":"diamonds"},
                               {"rank":"7","suit":"spades"},
                               {"rank":"8","suit":"diamonds"},
                               {"rank":"9","suit":"diamonds"}])

    print ranking

if __name__ == "__main__":
    main()
