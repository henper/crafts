'''
Created on Nov 10, 2019

@author: eponhik
'''
import unittest
import requests
import base64
import json
from time import time, ctime, sleep

class Authentication:
  def __init__(self, key, secret, device_id='0'):
    # store combination of key and secret in base64 as api expects it, strip the trailing newline
    self.client_credentials = base64.encodebytes(key + b':' + secret).rstrip() # key and secret must be byte-arrays
    self.device_id = device_id
    self.expiration = 0.0 # indicate that the current token expired at midnight on jan 1, 1970

  def fetchToken(self):
    timestamp = time()
    response = requests.post('https://api.vasttrafik.se/token',
                             headers = {'Authorization' : 'Basic ' + str(self.client_credentials,'utf-8')},
                             data = 'grant_type=client_credentials&scope=' + self.device_id)
    if(response.status_code == 200):
      self.token = response.json().get('access_token')
      self.expiration = response.json().get('expires_in') + timestamp

    return response.status_code

  def getValidToken(self):
    if(self.expiration <= time()):
      self.fetchToken()
    return self.token


class Test(unittest.TestCase):

  def setUp(self):
    # The test expects a JSON file with client credentials to exist in the same directory, example contents:
    # { 
    #   "key": <nyckel>,
    #   "secret": <hemlighet>,
    #   "client_credentials": <your key:secret in base64>
    # }
    # All values should be fetched for a registered application from https://developer.vasttrafik.se/portal/#/applications
    fh = open('client_credentials.json','r')
    cc = json.loads(fh.read())
    fh.close()
    self.key = cc.get('key').encode('utf-8')
    self.secret = cc.get('secret').encode('utf-8')
    self.client_credentials = cc.get('client_credentials').encode('utf-8')

  def testClientCredentials(self):
    auth = Authentication(key=self.key, secret=self.secret)
    assert(auth.client_credentials == self.client_credentials)

  def testFetchToken(self):
    auth = Authentication(key=self.key, secret=self.secret)
    assert(auth.fetchToken() == 200)

  def testGetValidToken(self):
    auth = Authentication(key=self.key, secret=self.secret)

    # Initial fetch of the token
    print('\nInitial fetch at: %s' % ctime())
    initialToken = auth.getValidToken()
    print('token: ' + initialToken)

    # Subsequent gets should return the same token
    subsequentToken = auth.getValidToken()
    assert(initialToken == subsequentToken)
    print('token: ' + subsequentToken)

    # taking a nap past expiration should result in new token
    nap = auth.expiration - time()
    print('Sleeping for %f seconds' % nap)
    sleep(nap)

    print('Subsequent fetch at: %s' % ctime())
    subsequentToken = auth.getValidToken()
    assert(initialToken != subsequentToken)
    print('token: ' + subsequentToken)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()