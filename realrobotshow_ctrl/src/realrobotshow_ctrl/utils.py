#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

def check_button_event(prev, curr):

    green = False
    red = False
    if prev.value[0] is True and curr.value[0] is False:
        green = True

    if prev.value[1] is True and curr.value[1] is False: 
        red = True

    return green, red

def play_sound(resource_path, sound):
    chirp_path = subprocess.check_output(['rospack','find','rocon_apps']).replace('\n','')
    chirp = chirp_path + '/scripts/play_sound.bash' 

    sound = resource_path + '/' + sound
    subprocess.call([chirp_path, sound])
