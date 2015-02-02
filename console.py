#!/usr/bin/env python3
 
from rauth import OAuth1Session
import sys
 
from common import *
 
def main():
    rt, rts = SERVICE.get_request_token(params={'oauth_callback': 'oob'})
    auth_url = add_auth_params(SERVICE.get_authorize_url(rt), access='Full', permissions='Modify')
    print('Go to %s in a web browser.' % auth_url)
    sys.stdout.write('Enter the six-digit code: ')
    sys.stdout.flush()
    verifier = sys.stdin.readline().strip()
    at, ats = SERVICE.get_access_token(rt, rts, params={'oauth_verifier': verifier})
    session = OAuth1Session(API_KEY, API_KEY_SECRET, access_token=at, access_token_secret=ats)
    print(session.get(API_ORIGIN + '/api/v2!authuser', headers={'Accept': 'application/json'}).text)
    print('\nrequest token: ' + rt + '\nrequest secret: ' + rts + '\naccess token: ' + at + '\naccess secret: ' + ats)

    # Now we can use the session from the command line:
    again = '1'
    while (again == '1'):
        print('Enter url of private resource:')
        url = sys.stdin.readline().strip()
        print(session.get(url, headers={'Accept': 'application/json'}).text)
        print('Enter 1 for new request:')
        again = sys.stdin.readline().strip()

if __name__ == '__main__':
    main()
 
