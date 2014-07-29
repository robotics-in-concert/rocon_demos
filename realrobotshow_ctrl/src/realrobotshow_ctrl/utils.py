#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import subprocess

def check_button_event(prev, curr):

    green = False
    red = False
    if prev.values[0] is False and curr.values[0] is True:
        green = True

    if prev.values[1] is False and curr.values[1] is True: 
        red = True

    return green, red

def play_sound(resource_path, sound):
    chirp_path = subprocess.check_output(['rospack','find','rocon_apps']).replace('\n','')
    chirp = chirp_path + '/scripts/chirp.bash' 
    sound_path = resource_path + '/' + sound
    subprocess.call([chirp, sound_path])
