__version__ = "0.0.4"
AUTHOR = 'Vanessa Sochat'
AUTHOR_EMAIL = 'vsochat@stanford.edu'
NAME = 'som'
PACKAGE_URL = "https://github.com/radinformatics/somtools"
KEYWORDS = 'medical-images, stanford, school of medicine, api, validator'
DESCRIPTION = "python tools for school of medicine"
LICENSE = "LICENSE"

INSTALL_REQUIRES = (

certifi >= 14.05.14
six == 1.8.0
python_dateutil >= 2.5.3
setuptools >= 21.0.0
urllib3 >= 1.15.1

    ('certifi',{'min_version': '14.05.14' }),
    ('flask', {'min_version': '0.12'}),
    ('flask-restful', {'min_version': None}),
    ('pandas', {'min_version': '0.19.2'}),
    ('requests', {'min_version': '2.12.4'}),
    ('retrying', {'min_version': '1.3.3'}),
    ('selenium', {'min_version': '3.0.2'}),
    ('simplejson', {'min_version': '3.10.0'}),
    ('six', {'min_version': '1.10'}),
    ('pygments', {'min_version': '2.1.3'}),
    ('python-dateutil',{'min_version': None }),
    ('urllib3',{'min_version': "1.15" }),
    ('validator.py',{'min_version': None }),
    ('google-api-python-client', {'min_version': None}),
    ('oauth2client', {'exact_version': '3.0'})

)