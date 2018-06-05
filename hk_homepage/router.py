"""LICENSE
Copyright 2015 Hermann Krumrey <hermann@krumreyh.com>

This file is part of hk-homepage.

hk-homepage is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

hk-homepage is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with hk-homepage.  If not, see <http://www.gnu.org/licenses/>.
LICENSE"""

from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route('/.well-known/acme-challenge/<token_value>')
def letsencrpyt(token_value: str):
    """
    Letsencrypt endpoint for renewal of SSL certs
    :param token_value: The token requested by letsencrypt
    :return: The response for letsencrypt
    """
    with open('.well-known/acme-challenge/{}'.format(token_value)) as f:
        answer = f.readline().strip()
    return answer
