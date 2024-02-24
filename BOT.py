from discord .ext import commands #line:1
from discord import app_commands #line:2
from typing import Literal #line:3
import discord #line:4
import random #line:5
import time #line:6
import os #line:7
required_role ="@ lcc.buyers"#line:10
class Vector2 :#line:12
  def __init__ (O0O00OOO0OO0OO0OO ,x =None ,y =None ):#line:13
      O0O00OOO0OO0OO0OO .x =x #line:14
      O0O00OOO0OO0OO0OO .y =y #line:15
  def get_x (OOOOOO00000O0000O ):#line:17
      return OOOOOO00000O0000O .x #line:18
  def get_y (OO0O0OO00000000OO ):#line:20
      return OO0O0OO00000000OO .y #line:21
def get_line (O00OOOOO00OOOO000 ):#line:23
  return Vector2 (7.015 +-0.01276 *O00OOOOO00OOOO000 ,7.1415 +-0.014512 *O00OOOOO00OOOO000 )#line:24
def random_8_char_string ():#line:26
  OO0OO0OO00O00OO0O =""#line:27
  for OOOOOO00O0O0OOOO0 in range (8 ):#line:28
      OO0OO0OO00O00OO0O +=random .choice ("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjkklzxcvbnm12345890098765432")#line:29
  return OO0OO0OO00O00OO0O #line:31
bot =commands .Bot (command_prefix ='__disabled__',intents =discord .Intents .all ())#line:34
bot .remove_command ('help')#line:35
@bot .event #line:38
async def on_ready ():#line:39
    print ("Syncing commands...")#line:40
    await bot .tree .sync ()#line:41
    print ("Synced!")#line:42
    await bot .change_presence (activity =discord .Activity (type =discord .ActivityType .watching ,name ="for /generate"))#line:43
@bot .hybrid_command (name ="generate",description ="Generate A Config From Solenoid here!")#line:49
@app_commands .describe (ping ="Your Latency/MS",blatant_percent ="1 - 100%, How Blatant You Want Your Config To Be",jump_check ="Remove your jump cooldown, this lets you jump with no cooldown or pauses",aimbot_bind_mode ="What keybind you want for the config",aimbot_part ="Where the aimbot should target",streamproof ="Whether the gui/esp would show on a recording software like OBS or Medal",v_sync ="Enable this if your PC isnt high end",show_name ="Esp via nametags",show_boxes ="Esp via boxes",show_fov ="Radius in which a player has to be for them to be locked onto",show_tracers ="Enable aiming saplines",stickyaim ="Stick to one player instead of locking onto a different player mid-fight",teamcheck ="Checks if a player is on your team therefore not allowing you to lock onto them",knockcheck ="Checks if the target has been knocked and is ready to be stomped",aimbot_fov ="The FOV of the aimbot",filled_fov ="Fill the FOV circle of the aimbot?",prediction_dot ="Esp dot via the players movement according to your x and y prediction",shake ="Shakes your camera according to the target's trajectory",shake_x ="Shake Prediction: X (Put to zero if you dont want this)",shake_y ="Shake Prediction: Y (Put to zero if you dont want this)")#line:71
async def generate (OOO0OOO0OO0OO000O ,OO000O0OOOO000OO0 :int ,OOOO0000000O00O00 :int ,OO0000OOOOO0OOO0O :bool ,O0OOO000OOO0OO0O0 :Literal ["Hold","Toggle"],OOO0O0O00OOO0OO00 :Literal ["Upper Torso","HumanoidRootPart","Lower Torso"],streamproof :bool =None ,v_sync :bool =None ,show_name :bool =None ,show_boxes :bool =None ,show_fov :bool =None ,show_tracers :bool =None ,stickyaim :bool =None ,teamcheck :bool =None ,knockcheck :bool =None ,aimbot_fov :int =None ,filled_fov :bool =None ,prediction_dot :bool =None ,shake :bool =None ,shake_x :int =None ,shake_y :int =None ):#line:94
  OO0OOOO000OO0O0O0 =discord .utils .get (OOO0OOO0OO0OO000O .guild .roles ,name =required_role )#line:97
  if OO0OOOO000OO0O0O0 not in OOO0OOO0OO0OO000O .author .roles :#line:99
      await OOO0OOO0OO0OO000O .reply (embed =discord .Embed (title =">>> No permission."),ephemeral =True )#line:100
      return #line:101
  if OO000O0OOOO000OO0 <0 or OO000O0OOOO000OO0 >300 :#line:106
    await OOO0OOO0OO0OO000O .reply (embed =discord .Embed (title =">>> Your ping is unsupported at this time."))#line:107
    return #line:108
  if OOOO0000000O00O00 <0 or OOOO0000000O00O00 >100 :#line:111
    await OOO0OOO0OO0OO000O .reply (embed =discord .Embed (title =">>> Your blatant percentage should be a percentage, between 1 and 100."))#line:112
    return #line:113
  if O0OOO000OOO0OO0O0 =="Hold":#line:118
    O0OOO000OOO0OO0O0 =1 #line:119
  else :#line:120
    O0OOO000OOO0OO0O0 =2 #line:121
  if OOO0O0O00OOO0OO00 =="Upper Torso":#line:124
    OOO0O0O00OOO0OO00 =1 #line:125
  elif OOO0O0O00OOO0OO00 =="HumanoidRootPart":#line:126
    OOO0O0O00OOO0OO00 =2 #line:127
  elif OOO0O0O00OOO0OO00 =="Lower Torso":#line:128
    OOO0O0O00OOO0OO00 =3 #line:129
  if OOO0O0O00OOO0OO00 is None :#line:132
    OOO0O0O00OOO0OO00 =2 #line:133
  if streamproof is None :#line:134
      streamproof =False #line:135
  if v_sync is None :#line:136
      v_sync =False #line:137
  if show_name is None :#line:138
      show_name =False #line:139
  if show_boxes is None :#line:140
      show_boxes =False #line:141
  if show_fov is None :#line:142
      show_fov =False #line:143
  if show_tracers is None :#line:144
      show_tracers =False #line:145
  if stickyaim is None :#line:146
      stickyaim =False #line:147
  if teamcheck is None :#line:148
      teamcheck =False #line:149
  if knockcheck is None :#line:150
      knockcheck =False #line:151
  if aimbot_fov is None :#line:152
      aimbot_fov =35 #line:153
  if filled_fov is None :#line:154
      filled_fov =False #line:155
  if prediction_dot is None :#line:156
      prediction_dot =False #line:157
  if shake is None :#line:158
      shake =False #line:159
  if shake_x is None :#line:160
      shake_x =0 #line:161
  if shake_y is None :#line:162
      shake_y =0 #line:163
  if OO0000OOOOO0OOO0O is None :#line:164
      OO0000OOOOO0OOO0O =False #line:165
  O0O0OOO0OO0000OOO =(OOOO0000000O00O00 /100 )#line:167
  OO000000OOO0OOOO0 =get_line (OO000O0OOOO000OO0 )#line:169
  O0OO000OOOOO0000O =f"""aimbot-enabled = "1";
aimbot-smoothing = "{O0O0OOO0OO0000OOO}";
camera-smoothing = "1";
aimbot-sensitivity = "1";
aimbot-bind = "67";
aimbot-bind-mode = "1";
aimbot-part = "{int(OOO0O0O00OOO0OO00)}";
streamproof = "{int(streamproof)}";
v-sync = "1";
show_name = "{int(show_name)}";
show_boxes = "{int(show_boxes)}";
show_fov = "{int(show_fov)}";
show_deadzone = "0";
show_tracers = "{int(show_tracers)}";
prediction = "1";
stickyaim = "{int(stickyaim)}";
teamcheck = "{int(teamcheck)}";
knockcheck = "{int(teamcheck)}";
aimbot-fov = "{aimbot_fov}";
filled_fov = "{int(filled_fov)}";
aimbot-deadzone = "0";
filled_deadzone = "0";
pred_x = "{OO000000OOO0OOOO0.x}";
pred_y = "{OO000000OOO0OOOO0.y}";
x_offset = "0";
y_offset = "0";
deadzone_flag = "0";
fov_flag = "0";
prediction_dot = "{int(prediction_dot)}";
pred_dot_type = "0";
tracer_type = "0";
shake = "{int(shake)}";
shake_x = "{shake_x}";
shake_y = "{shake_y}";
box_type = "0";
aimbot_type = "1";
no_jump = "{int(OO0000OOOOO0OOO0O)}";"""#line:207
  O00O00O0OO000OO0O =f"solenoid_{OO000O0OOOO000OO0}_ping.cfg"#line:209
  with open (O00O00O0OO000OO0O ,'w')as O00OO00OO0OOO00O0 :#line:212
      O00OO00OO0OOO00O0 .write (O0OO000OOOOO0000O )#line:215
  await OOO0OOO0OO0OO000O .reply (">>> Check our DMs!")#line:217
  await OOO0OOO0OO0OO000O .message .author .send (embed =discord .Embed (title =">>> Your config has been delivered!",description ="Made by discord.gg/sets"),file =discord .File (O00O00O0OO000OO0O ))#line:220
  print (f"Deleting {O00O00O0OO000OO0O}!")#line:222
  os .remove (O00O00O0OO000OO0O )#line:223
  print (f"Deleted.")#line:224
bot.run ("YOUR TOKEN HERE, MADE BY CARTI")