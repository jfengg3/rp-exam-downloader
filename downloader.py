import urllib.parse, urllib.request, os, sys, requests, re
from requests_ntlm import HttpNtlmAuth
from bs4 import BeautifulSoup as bs

class downloader(object):

    def __init__(self, mode):
        self.mode = mode

    def beginDLR(self, username, password, module, folder, updateStatus):

        updateStatus('Connecting to RP Library . . .')

        # params
        site = 'intranet.rp.edu.sg'
        page = '/lib/LibraryServices/_layouts/15/start.aspx'+'#'+'/eRepository/Forms/AllItems.aspx'
        url = 'http://intranet.rp.edu.sg/lib/LibraryServices/eRepository/Examination%20Paper/C105%20Introduction%20to%20Programming'

        session = requests.Session()
        session.auth = HttpNtlmAuth(username, password)

        headers = {
            'accept' : 'application/json;odata=verbose',
            'content-type' : 'application/json;odata=verbose',
            'odata' : 'verbose',
            'X-RequestForceAuthentication' : 'true'
        }

        try:

            # Make a session request to the server
            # First, to authenticate the user's credentials if he/she is connected to RP's VPN
            r = session.get(url, headers=headers)

            # If status_code == ok or 200 means user have successfully connected to RP's VPN
            if (r.status_code == 200):

                updateStatus("Successfully connected to online library...", 'success')

                #-- Search for module
                mod_url = 'https://libopac.rp.edu.sg/client/en_GB/home/search/results?qu=' + module + '&te=ILS'

                mod_r = requests.get(mod_url)
                mod_c = mod_r.content

                mod_soup = bs(mod_c, "lxml")

                #-- We exclude everything except "intranet" as it is where the resources are located
                mod_exclude = mod_soup.findAll('a', href=re.compile("intranet"))
                #-- Count every possible mod_exclude results that will appear
                count = 0

                for mod_tag in mod_exclude:
                    count = count + 1

                #-- If "intranet" found ...
                if count > 0:
                    #-- temp_url will be the first query found
                    #-- (We do this because in exceptional cases, they will return multiple modules instead of the queried one)
                    mod_temp_url = mod_exclude[0]['href']

                    mod_new_url = mod_temp_url.replace(" ", "%20")
                    updateStatus(("Module %s found, begin download query..." % module), 'success')

                    #-- Get folder destination
                    path = folder

                    #-- Read the request(url) in bytes form, used to write files later
                    # Make a session request to the server
                    r = session.get(mod_new_url, headers=headers)
                    c = r.content
                    soup = bs(c, "lxml")

                    #-- Downloader
                    i = 0

                    for tag in soup.findAll('a', href=True):
                        tag['href'] = urllib.parse.urljoin(url, tag['href'])

                        if os.path.splitext(os.path.basename(tag['href']))[1] == '.pdf':
                            current = session.get((tag['href'])).content
                            updateStatus("Downloading: %s" %(os.path.basename(tag['href'])), 'success')

                            try:

                                f = open(path + "\\" + os.path.basename(tag['href']), "wb")
                                f.write(current)
                                f.close()
                                i+=1

                            except Exception as e:

                                updateStatus("Unable to use destination!", 'error')

                    updateStatus("Downloaded %d files" %(i), 'success')

                #-- If module is not found, return
                else:
                    updateStatus("Sorry, the module is not found in our database.", 'error')


            # If status_code returns 401 -> user's credentials failed therefore not authorized
            else:
                updateStatus("Authorization failed. Please ensure you have the right credentials.", 'error')

            return

        # If user is not connected to RP's VPN, this handler will be raised
        except requests.exceptions.ConnectionError:

            updateStatus("Unable to connect to destination. Ensure that you're connected to RP's VPN...", 'error')
            return
