#!/usr/bin/env python3

import logging
import logging.config
import os
import re
import sys
from configparser import ConfigParser
from itertools import chain


class NoDefaultHeaderConfigParser(ConfigParser):
    def read_file(self, f, source=None):
        with open(f) as lines:
            lines = chain(("[DEFAULT]",), lines)
            super().read_file(lines, source)

    def _write_section(self, fp, section_name, section_items, delimiter):
        """Write a single section to the specified `fp'."""
        if section_name != self.default_section:
            fp.write("[{}]\n".format(section_name))

        for key, value in section_items:
            value = self._interpolation.before_write(self, section_name, key, value)
            if value is not None or not self._allow_no_value:
                value = delimiter + str(value).replace('\n', '\n\t')
            else:
                value = ""
            fp.write("{}{}\n".format(key, value))
        fp.write("\n")


REGEX_CONFIG_VARS = re.compile(r'(?P<prefix>GOGS)__(?P<section>.+?)__(?P<option>.+)')


logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "brief": {
            "class": "logging.Formatter",
            "format": "[%(name)s] [%(levelname)s] %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "brief",
            "level": "DEBUG",
            "stream": "ext://sys.stderr"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "console"
        ]
    }
})
logger = logging.getLogger('ini-inject-secrets')

if len(sys.argv) < 2:
    raise IndexError('Expecting path to ini file as first command-line parameter; got none.')
config_file = sys.argv[1]

logger.info(f'Reading configuration from file: {config_file}')

parser = NoDefaultHeaderConfigParser()
parser.optionxform = lambda opt: opt
parser.read_file(config_file)

logger.debug(f'Read config contains sections (modulo default one): {parser.sections()}')

for k,v in os.environ.items():
    match = REGEX_CONFIG_VARS.match(k)
    if not match:
        continue

    section = match.group('section').lower()
    option = match.group('option')

    logger.info(f'Injecting option={option} into section={section} with value from envvar={k}')

    if section not in parser:
        parser[section] = {}
    parser[section][option] = v

parser.write(sys.stdout)
