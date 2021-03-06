# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 OpenStack, LLC
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import random
import re
import urllib
from tempest import exceptions


def rand_name(name='test'):
    return name + str(random.randint(1, 999999))


def build_url(host, port, api_version=None, path=None,
              params=None, use_ssl=False):
    """Build the request URL from given host, port, path and parameters"""

    pattern = 'v\d\.\d'
    if re.match(pattern, path):
        message = 'Version should not be included in path.'
        raise exceptions.InvalidConfiguration(message=message)

    if use_ssl:
        url = "https://" + host
    else:
        url = "http://" + host

    if port is not None:
        url += ":" + port
    url += "/"

    if api_version is not None:
        url += api_version + "/"

    if path is not None:
        url += path

    if params is not None:
        url += "?"
        url += urllib.urlencode(params)

    return url


def parse_image_id(image_ref):
    """Return the image id from a given image ref"""
    temp = image_ref.rsplit('/')
    #Return the last item, which is the image id
    return temp[len(temp) - 1]


def arbitrary_string(size=4, base_text=None):
    """Return exactly size bytes worth of base_text as a string"""

    if (base_text is None) or (base_text == ''):
        base_text = 'test'

    if size <= 0:
        return ''

    extra = size % len(base_text)
    body = ''

    if extra == 0:
        body = base_text * size

    if extra == size:
        body = base_text[:size]

    if extra > 0 and extra < size:
        body = (size / len(base_text)) * base_text + base_text[:extra]

    return body
