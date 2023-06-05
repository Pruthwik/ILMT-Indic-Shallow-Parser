"""Run Sampark shallow parser."""
# Language codes for passing onto the API, 3 lettered language identifier.
# Kannada - kan, Punjabi - pan, Urdu - urd, Telugu - tel, Hindi - hin
# Malayalam - mal, Tamil - tam
# if requests package is not there, do pip install requests
import requests
import json
from sys import argv


url = "https://ssmt.iiit.ac.in/indic_shallow_parser_v1"


def run_sampark_parser_with_arguments(text, lang):
    """Run Sampark shallow parser with arguments."""
    # for multiple sentences, just join them by \n
    out =  {"language":lang, "text": text}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(out), headers=headers)
    json_output = r.json()
    ssf_sent = json_output['data']
    return ssf_sent


def main():
    """Pass arguments and call functions here."""
    text = argv[1]
    # for hindi, lang is hin
    lang = argv[2]
    ssf_sent = run_sampark_parser_with_arguments(text, lang)
    print(ssf_sent)


if __name__ == '__main__':
    main()
