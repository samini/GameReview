import json
import urllib
import urllib2

class ReviewEndpoint:
  SEARCH_URL_FORMAT = 'https://www.giantbomb.com/api/search/%s&query=%s'

  def __init__(self, api_key, verbose=False):
    self.api_key = api_key
    self.verbose = verbose

  def __make_request__(self, r):
    if self.verbose:
      print('Making request for %s' %r)
    request = urllib2.Request(r)
    content = urllib2.urlopen(request).read()
    return json.loads(content)

  def __url_suffix__(self):
    return '?api_key=%s&format=json' % self.api_key

  def __get_api_detail_url__(self, game):
    r = ReviewEndpoint.SEARCH_URL_FORMAT % (self.__url_suffix__(), urllib.quote_plus(game))
    sr = self.__make_request__(r)
    if not sr:
      return None
    if (sr['number_of_page_results'] < 1 or sr['number_of_total_results'] < 1):
      return None
    if 'results' in sr:
      results = sr['results']
    if len(results) > 0 and 'api_detail_url' in results[0]:
  	return results[0]['api_detail_url']
    return None

  def get_reviews(self, game):
    api_detail_url = self.__get_api_detail_url__(game)
    if api_detail_url:
      re = self.__make_request__("%s%s" % (api_detail_url, self.__url_suffix__()))
      if re and 'results' in re and 'reviews' in re['results']:
        return re['results']['reviews']
    return None

  def get_review(self, game):
    reviews = self.get_reviews(game)
    if (reviews):
      review = self.__make_request__(reviews[0]['api_detail_url'] + self.__url_suffix__())
      return (review['results']['score'], review['results']['site_detail_url'])
    return None

# For testing only
if __name__ == "__main__":
  import sys
  if len(sys.argv) < 2:
    print('Pass in API key')
    sys.exit(1)
  re = ReviewEndpoint(sys.argv[1], True)
  print re.get_review("Assassin's Creed Freedom Cry")
