"""
conn/email/outlook.py
Functionality for auto emailing persons via outlook
@author: dpgraham4401
"""

import win32com.client


def run_who(args):
    who_has_the_conn = "You have the Conn " + args.u
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(who_has_the_conn)
