"""
    Dragon Ocean (c) 2023

    Project name:Lenter

    File name:compress.py

    Version: 0.1.0

    Apache-2.0 license
"""
import csscompressor
css_o=open("lenter.css","r",encoding="utf-8").read()
com_css=csscompressor.compress(css_o)
open("lenter.min.css",'a').write(com_css)