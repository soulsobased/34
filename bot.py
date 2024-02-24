import discord #line:1
from discord .ext import commands #line:2
from discord import app_commands #line:3
from typing import Literal #line:6
import json #line:9
import os #line:10
import requests #line:13
cookie =""#line:17
x_tok =""#line:18
embed_color =discord .Color .blue ()#line:21
admin_role ="@ ++"#line:24
permissionsMissing =discord .Embed (title ="Missing permissions",description =">>> No permission.",color =0xa61c1c )#line:28
invalid_username =discord .Embed (title ="Invalid Username",description =">>> I couldn't find the username you provided",color =0xa61c1c )#line:29
privateInventory =discord .Embed (title ="Private Inventory",description =">>> Your inventory is private, make sure it is public before running any commands.",color =0xa61c1c )#line:30
doesntOwnGamepass =discord .Embed (title ="Gamepass",description =">>> You don't have the gamepass.",color =0xa61c1c )#line:31
purchaseMsg =discord .Embed (title ="Purchase",description =">>> Thanks for your purchase, access will be granted.",color =0xa61c1c )#line:32
blacklistMsg =discord .Embed (title ="Blacklisted",description =">>> You are blacklisted.",color =0xa61c1c )#line:33
alreadyRedeemedMsg =discord .Embed (title ="Redeemed",description =">>> Username already claimed.",color =0xa61c1c )#line:34
addedProduct =discord .Embed (title ="Added",description =">>> Product added, bot restart is required.",color =0xa61c1c )#line:35
placeholderMessage =discord .Embed (title ="Placeholder",description =">>> You cannot redeem this product, this is a placeholder product.",color =0xa61c1c )#line:36
errorMessage =discord .Embed (title ="Error",description =">>> Try again later.",color =0xa61c1c )#line:37
idError =discord .Embed (title ="Error",description =">>> Try again later.",color =0xa61c1c )#line:38
userStructure ={}#line:42
productsStructure ={}#line:43
class WebView :#line:48
    def __init__ (OOOOO0O00OO0OOOOO ):#line:50
        pass #line:51
    @staticmethod #line:53
    def roblox_profile_metadata (OOO0O00OO000000OO ):#line:54
        OO000O00O000000OO =requests .get (url =f"https://www.roblox.com/search/users/results?keyword={OOO0O00OO000000OO}&maxRows=12&startIndex=0",headers ={"Cookie":cookie ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","X-Bound-Auth-Token":x_tok },json ={"keyword":OOO0O00OO000000OO ,"maxRows":12 ,"startIndex":0 })#line:67
        O0OO00OO0000O0O0O =json .loads (OO000O00O000000OO .text )#line:69
        if (OO000O00O000000OO .status_code ==200 ):#line:71
            if O0OO00OO0000O0O0O ['UserSearchResults']==None :#line:72
                return "USER_NOT_FOUND"#line:73
            for OO0O0OO0OOOO00O0O ,O0OO00000OOO0O00O in O0OO00OO0000O0O0O .items ():#line:74
                if (OO0O0OO0OOOO00O0O =="UserSearchResults"):#line:75
                    for O0000O00OOO0OOO00 in O0OO00000OOO0O00O :#line:76
                        if O0000O00OOO0OOO00 ['Name'].lower ()==OOO0O00OO000000OO .lower ():#line:77
                            return O0000O00OOO0OOO00 #line:78
                    return "USER_NOT_FOUND"#line:80
        else :#line:81
            return OO000O00O000000OO .status_code #line:82
    @staticmethod #line:84
    def get_owned_gamepasses (OO00OOOO00OO0O0O0 ,OO000O0OO0O0OOO00 ):#line:85
        O0O000O0OOO0OO0OO =requests .get (url =f"https://www.roblox.com/users/inventory/list-json?assetTypeId=34&cursor=&itemsPerPage=100&pageNumber=1&userId={OO00OOOO00OO0O0O0}",headers ={"Cookie":cookie ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36","X-Bound-Auth-Token":"47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=|1707413002|K1wh/ZlzPdm559e/WPkyThMhZauR0AKXTvHGAdkru6XIhKkjbRio7wQ6fNRK38ydCA2luFZDRwKfxDNgr4t+Uw=="},json ={"assetTypeId":34 ,"cursor":"","itemsPerPage":100 ,"pageNumber":1 ,"userId":OO00OOOO00OO0O0O0 })#line:100
        OOOOO0OOO0OOOO0O0 =json .loads (O0O000O0OOO0OO0OO .text )#line:102
        if OOOOO0OOO0OOOO0O0 ["IsValid"]==False :#line:104
            return "Unknown"#line:105
        if len (OOOOO0OOO0OOOO0O0 ["Data"]["Items"])==0 :#line:107
            return "Private Inventory"#line:108
        for OOO0O000O00O000O0 in OOOOO0OOO0OOOO0O0 ["Data"]["Items"]:#line:110
            if OOO0O000O00O000O0 ["Item"]["AssetId"]==OO000O0OO0O0OOO00 :#line:111
                print (f'Returning true, gid: {OO000O0OO0O0OOO00} == {OOO0O000O00O000O0["Item"]["AssetId"]} ({OOOOO0OOO0OOOO0O0})')#line:112
                return True #line:113
        return False #line:115
class Utility :#line:118
    def __init__ (OOO00000000O00OOO ):#line:119
        pass #line:120
    @staticmethod #line:122
    def dump ():#line:123
        try :#line:124
            with open ("database.json","w")as O0OO0O00OO0O0O0O0 :#line:125
                json .dump (userStructure ,O0OO0O00OO0O0O0O0 ,indent =4 )#line:126
        except Exception as O0000O0O0OO000O0O :#line:128
            print (f"[Debug] FAILED TO LOG - {O0000O0O0OO000O0O}")#line:129
    @staticmethod #line:131
    def read ():#line:132
        try :#line:133
            with open ("database.json","r")as O0OO000OO0O0OOOOO :#line:134
                return json .loads (O0OO000OO0O0OOOOO )#line:135
        except Exception as O000O00O00O00000O :#line:137
            print (f"[Debug] FAILED TO LOG - {O000O00O00O00000O}")#line:138
    @staticmethod #line:140
    def dump_products ():#line:141
        try :#line:142
            with open ("products.json","w")as O0000OOO00OOO00OO :#line:143
                json .dump (productsStructure ,O0000OOO00OOO00OO ,indent =4 )#line:144
        except Exception as OOO00O0OOOOO000OO :#line:146
            print (f"[Debug] FAILED TO LOG - {OOO00O0OOOOO000OO}")#line:147
    @staticmethod #line:149
    def exists (OOO0O000O000O0OOO ):#line:150
        OO0000000O0O00000 =False #line:151
        for OOOO000O0O00O000O in userStructure :#line:152
            if (OOOO000O0O00O000O .discord_id ==OOO0O000O000O0OOO ):#line:153
                OO0000000O0O00000 =True #line:154
        return OO0000000O0O00000 #line:156
    @staticmethod #line:158
    def get_embed (OO0OOOOOO00OOO0OO ,description =None ,footer =None ):#line:159
        OOOOO00O00O000OOO =discord .Embed (title =OO0OOOOOO00OOO0OO ,description =description ,color =embed_color )#line:164
        if footer is not None :#line:166
            OOOOO00O00O000OOO .set_footer (text =footer )#line:167
        return OOOOO00O00O000OOO #line:169
    @staticmethod #line:171
    def get_proucts ():#line:172
        OOOOO0O00OOO00000 =[]#line:173
        for O000O000O00OOO0OO ,O00000OO00OOOOOO0 in productsStructure :#line:175
            OOOOO0O00OOO00000 .append (f"{O000O000O00OOO0OO} (ID: {O00000OO00OOOOOO0})")#line:176
        return OOOOO0O00OOO00000 #line:178
class UserCache :#line:181
    def __init__ (OO0O0OOO00OOOO0OO ,OO0OO0OOO0OO0OO0O ,O0OOO0000O00OOO0O ,OOOO0O0O0OOOO000O ):#line:182
        OO0O0OOO00OOOO0OO .discord_id =OO0OO0OOO0OO0OO0O #line:183
        OO0O0OOO00OOOO0OO .metadata =OOOO0O0O0OOOO000O #line:184
        OO0O0OOO00OOOO0OO .roblox_id =O0OOO0000O00OOO0O #line:185
        OO0O0OOO00OOOO0OO .blacklisted =False #line:187
        OO0O0OOO00OOOO0OO .redeemed =[]#line:188
    def toString (O000OOO0000OO00O0 ):#line:191
        OO0OOO0OOO0O000O0 ={O000OOO0000OO00O0 .discord_id :{"discord_id":int (O000OOO0000OO00O0 .discord_id ),"roblox_metadata":O000OOO0000OO00O0 .metadata ,"roblox_id":O000OOO0000OO00O0 .roblox_id ,"blacklisted":O000OOO0000OO00O0 .blacklisted ,"redeemed":list (O000OOO0000OO00O0 .redeemed )}}#line:200
        return OO0OOO0OOO0O000O0 #line:202
class ProductCache :#line:205
    def __init__ (O0000OO00O0O0000O ,O0OOOO0O0O0OO0O0O ,OO0OOOO00O0000OO0 ,O0OO00OO00000OOOO ):#line:206
        O0000OO00O0O0000O .product_id =O0OOOO0O0O0OO0O0O #line:207
        O0000OO00O0O0000O .alias =OO0OOOO00O0000OO0 #line:208
        O0000OO00O0O0000O .role =O0OO00OO00000OOOO #line:209
    def toString (OO00OOOO00OOO00O0 ):#line:211
        OO0OO0OOOO00000OO ={OO00OOOO00OOO00O0 .alias :{"product_id":OO00OOOO00OOO00O0 .product_id ,"given_role":OO00OOOO00OOO00O0 .role }}#line:217
        return OO0OO0OOOO00000OO #line:219
if (os .path .exists ("database.json")):#line:224
    with open ("database.json","r")as keys :#line:225
        userStructure .update (json .load (keys ))#line:226
    print ("[Debug] Read key array.")#line:227
else :#line:228
    print ("[Debug] [Warning] database.json does not create, creating it now...")#line:229
    data ={}#line:231
    with open ("database.json",'w')as file :#line:232
        json .dump (data ,file )#line:233
        print ("[Debug] Successfully created file database.json, please re-run the script.")#line:235
        exit (0 )#line:236
if (os .path .exists ("products.json")):#line:238
    with open ("products.json","r")as keys :#line:239
        productsStructure .update (json .load (keys ))#line:240
    print ("[Debug] Read key array.")#line:241
else :#line:242
    print ("[Debug] [Warning] products.json does not create, creating it now...")#line:243
    data ={}#line:245
    with open ("products.json",'w')as file :#line:246
        json .dump (data ,file )#line:247
        print ("[Debug] Successfully created file products.json, please re-run the script.")#line:249
        exit (0 )#line:250
bot =commands .Bot (command_prefix ='?',intents =discord .Intents .all ())#line:252
product_names =["Choose a product! (not this one retard)"]#line:254
ps =0 #line:256
for name ,data in productsStructure .items ():#line:258
    product_names .append (name )#line:259
    ps +=1 #line:260
avaliableProducts =Literal [tuple (product_names )]#line:262
@bot .event #line:265
async def on_ready ():#line:266
    print ("[Debug] Syncing commands... While this is syncing you won't be able to use new commands or products.")#line:267
    try :#line:268
        await bot .tree .sync ()#line:269
        print ("[Debug] Synced commands.")#line:270
    except Exception as OOOOOO0000O0O0OOO :#line:271
        print (f"[Debug] [ErrorLog] Failed to sync: {OOOOOO0000O0O0OOO}")#line:272
@bot .hybrid_command (name ="addproduct",description ="Add a product for your users to purchase!")#line:278
@app_commands .describe (link ="The link to your gamepass.",name ="What do you want this product to be called?",role ="The role you want customers to get when they redeem this gamepass")#line:283
async def addproduct (OOO0O0O0O0OOOO0O0 ,OO00O000OOO0O0O0O ,OOO00O0OO00O00OOO ,OOOO0O0OO000OO0OO :discord .Role ):#line:284
    OOO0000OO0OO0O0O0 =discord .utils .get (OOO0O0O0O0OOOO0O0 .guild .roles ,name =admin_role )#line:285
    if OOO0000OO0OO0O0O0 not in OOO0O0O0O0OOOO0O0 .author .roles :#line:287
        await OOO0O0O0O0OOOO0O0 .reply (embed =permissionsMissing )#line:288
        return #line:289
    O0O00OO0OOO0OO0O0 =OOO00O0OO00O00OOO .split ('/')#line:291
    for O000O0O0000O0OOOO in O0O00OO0OOO0OO0O0 :#line:293
        if O000O0O0000O0OOOO .isdigit ():#line:294
            OO0O0OO0OO00OOOO0 =int (O000O0O0000O0OOOO )#line:295
            break #line:296
    else :#line:297
        OO0O0OO0OO00OOOO0 =None #line:298
    if (OO0O0OO0OO00OOOO0 is None ):#line:300
        await OOO0O0O0O0OOOO0O0 .reply (">>> Invalid link.")#line:301
        return #line:302
    O0000O00OOOOOO000 =ProductCache (OO0O0OO0OO00OOOO0 ,OO00O000OOO0O0O0O ,OOOO0O0OO000OO0OO .name )#line:304
    productsStructure .update (O0000O00OOOOOO000 .toString ())#line:305
    Utility .dump_products ()#line:307
    await OOO0O0O0O0OOOO0O0 .reply (embed =addedProduct )#line:309
@bot .hybrid_command (name ="claim",description ="Claim your purchase")#line:315
@app_commands .describe (roblox_username ="Enter your Roblox USERNAME not DISPLAY name",product ="Which did you purchase?")#line:319
async def claim (O0O0O000O0OOOO000 ,OOOOOOO00OOO0O0OO ,O00O0OOOOOO0OO000 :avaliableProducts ):#line:320
    if O00O0OOOOOO0OO000 =="Choose a product! (not this one retard)":#line:321
        await O0O0O000O0OOOO000 .reply (embed =placeholderMessage )#line:322
        return #line:323
    O0OOOOOO0OO0O0O00 =productsStructure [O00O0OOOOOO0OO000 ]#line:325
    if O0OOOOOO0OO0O0O00 is None :#line:327
        await O0O0O000O0OOOO000 .reply (embed =errorMessage )#line:328
        return #line:329
    OOO0O000000OO000O =False #line:331
    OOO0OOOO00O00OOO0 =None #line:332
    for O000000OO000OO0OO ,O000OOOOO0O00O000 in userStructure .items ():#line:334
        if str (O000000OO000OO0OO )==str (O0O0O000O0OOOO000 .message .author .id ):#line:335
            OOO0OOOO00O00OOO0 =UserCache (O0O0O000O0OOOO000 .message .author .id ,O000OOOOO0O00O000 ["roblox_id"],O000OOOOO0O00O000 ["roblox_metadata"])#line:336
            OOO0OOOO00O00OOO0 .redeemed =O000OOOOO0O00O000 ["redeemed"]#line:337
            OOO0O000000OO000O =True #line:338
    if OOO0O000000OO000O is False :#line:340
        print ("Making a new user object")#line:341
        OOO0OOOO00O00OOO0 =UserCache (O0O0O000O0OOOO000 .message .author .id ,None ,None )#line:342
        userStructure .update (dict (OOO0OOOO00O00OOO0 .toString ()))#line:345
        Utility .dump ()#line:346
    O0000OOOOO00O0O0O =WebView .roblox_profile_metadata (OOOOOOO00OOO0O0OO )#line:349
    if O0000OOOOO00O0O0O =="USER_NOT_FOUND":#line:351
        await O0O0O000O0OOOO000 .reply (embed =invalid_username )#line:352
        return #line:353
    OOO0OOOO00O00OOO0 .roblox_id =O0000OOOOO00O0O0O ["UserId"]#line:355
    O0O00000O0O00OO0O =[]#line:357
    for O0OO0O0O0000OO00O ,O00O0000O000OOOO0 in userStructure .items ():#line:358
        if O0OO0O0O0000OO00O ==O0O0O000O0OOOO000 .message .author .id :#line:359
            O0O00000O0O00OO0O .append (O0OO0O0O0000OO00O )#line:360
    for O0OO0O0O0000OO00O in O0O00000O0O00OO0O :#line:362
        del userStructure [O0OO0O0O0000OO00O ]#line:363
    userStructure .update (OOO0OOOO00O00OOO0 .toString ())#line:365
    Utility .dump ()#line:367
    if O0OOOOOO0OO0O0O00 ["product_id"]in OOO0OOOO00O00OOO0 .redeemed :#line:369
        await O0O0O000O0OOOO000 .reply (embed =alreadyRedeemedMsg )#line:370
        return #line:371
    if (O0000OOOOO00O0O0O =="USER_NOT_FOUND"):#line:373
        await O0O0O000O0OOOO000 .reply (embed =idError )#line:374
        return #line:375
    if userStructure [O0O0O000O0OOOO000 .message .author .id ]["blacklisted"]==True :#line:378
        await O0O0O000O0OOOO000 .reply (embed =blacklistMsg )#line:379
        return #line:380
    O0OO00000OOOO00OO =WebView .get_owned_gamepasses (userStructure [O0O0O000O0OOOO000 .message .author .id ]["roblox_id"],O0OOOOOO0OO0O0O00 ["product_id"])#line:383
    if (O0OO00000OOOO00OO =="Private Inventory"):#line:385
        await O0O0O000O0OOOO000 .reply (embed =privateInventory )#line:386
        return #line:387
    if (O0OO00000OOOO00OO =="Unknown"):#line:389
        await O0O0O000O0OOOO000 .reply (embed =invalid_username )#line:392
        return #line:393
    if (O0OO00000OOOO00OO ==False ):#line:395
        await O0O0O000O0OOOO000 .reply (embed =doesntOwnGamepass )#line:396
        return #line:397
    OOOO0OOO00OOOOOO0 =O0OOOOOO0OO0O0O00 ["given_role"]#line:401
    await O0O0O000O0OOOO000 .author .add_roles (discord .utils .get (O0O0O000O0OOOO000 .guild .roles ,name =OOOO0OOO00OOOOOO0 ))#line:402
    OOO0OOOO00O00OOO0 .redeemed .append (O0OOOOOO0OO0O0O00 ["product_id"])#line:404
    O0O00000O0O00OO0O =[]#line:407
    for O0OO0O0O0000OO00O ,O00O0000O000OOOO0 in userStructure .items ():#line:408
        if O0OO0O0O0000OO00O ==O0O0O000O0OOOO000 .message .author .id :#line:409
            O0O00000O0O00OO0O .append (O0OO0O0O0000OO00O )#line:410
    for O0OO0O0O0000OO00O in O0O00000O0O00OO0O :#line:412
        del userStructure [O0OO0O0O0000OO00O ]#line:413
    userStructure .update (OOO0OOOO00O00OOO0 .toString ())#line:415
    Utility .dump ()#line:417
    await O0O0O000O0OOOO000 .reply (embed =purchaseMsg )#line:419
bot.run ("YOUR TOKEN HERE, MADE BY CARTI")