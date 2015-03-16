from urllib import urlencode
import urllib2
import json
import time

BASE_URL = 'https://cloudapi.beddit.com'

class BedditClient(object):

  def __init__(self, u_id, token):
    if not u_id:
      raise ValueError('Missing Argument: u_id')
    if not token:
      raise ValueError('Missing Argument: token')

    self.u_id = u_id
    self.token = token

  @classmethod
  def get_auth_client(cls, email, pwd):
    url = BASE_URL + '/api/v1/auth/authorize'
    params = {
        'grant_type': 'password',
        'username': email,
        'password': pwd,
    }
    req = urllib2.Request(url, urlencode(params))
    resp = json.loads(urllib2.urlopen(req).read())
    return BedditClient(resp.get('user'), resp.get('access_token'))


  def get_sleep(self, after=None, start=None, end=None, reverse=None, limit=None):
    """Get sleep resource as a list of sleep data dictionary

    Keywords arguments:
    after -- filter sleep data after given date with format '2015-01-01'
    start -- filter sleep data between start and end date with format '2015-01-01'
    end -- use with start; won't be used if 'after' argument is given
    reverse -- 'yes' if reverse chronological order is preferred. Default: 'no'
    limit -- max number of return results (integer)
    """
    url = BASE_URL + '/api/v1/user/%s/sleep?' % self.u_id

    params = {}
    if reverse == 'yes':
      params['reverse'] = 'yes'
    if limit > 0:
      params['limit'] = limit
    if after:
      params['updated_after'] = time.mktime(time.strptime(after, '%Y-%m-%d'))
    elif start and end:
      params['start_date'] = start
      params['end_date'] = end

    url += urlencode(params)
    req = urllib2.Request(url)
    req.add_header('Authorization', 'UserToken %s' % self.token)
    return json.loads(urllib2.urlopen(req).read())

