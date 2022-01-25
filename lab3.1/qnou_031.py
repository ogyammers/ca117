#!/usr/bin/env python3

import sys

def qnou(lines):
   return [line for line in lines if 'q' in line.lower().replace('qu', '')]


print(f'Words with q but no u: {qnou([line.strip() for line in sys.stdin])}')
