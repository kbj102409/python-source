# # BTSのbutterの歌詞から重複していない単語を表わす
# a = """
# Smooth like butter
# Like a criminal undercover
# Gon' pop like trouble
# Breakin' into your heart like that
# Cool shade stunner
# Yeah I owe it all to my mother
# Hot like summer
# Yeah I'm makin' you sweat like that
# Break it down
# Oh when I look in the mirror
# I'll melt your heart into 2
# I got that superstar glow so 
# Do the boogie like
# Side step right left to my beat (heartbeat)
# High like the moon rock with me baby
# Know that I got that heat
# Let me show you cause talk is cheap
# Side step right left to my beat (heartbeat)
# Get it, let it roll
# Smooth like butter
# Pull you in like no other
# Don't need no Usher
# To remind me you got it bad
# Ain't no other
# That can sweep you up like a robber
# Straight up I got ya
# Makin' you fall like that
# Break it down
# Oh when I look in the mirror
# I'll melt your heart into 2
# I got that superstar glow so 
# Do the boogie like
# Side step right left to my beat (heartbeat)
# High like the moon rock with me baby
# Know that I got that heat
# Let me show you cause talk is cheap
# Side step right left to my beat (heartbeat)
# Get it, let it roll
# Get it, let it roll
# Get it, let it roll
# No ice on my wrist
# I'm that n-ice guy
# Got that right body and that right mind
# Rollin' up to party got the right vibe
# Smooth like butter
# Hate us love us
# Fresh boy pull up and we lay low
# All the playas get movin' when the bass low
# Got ARMY right behind us when we say so
# Let's go
# Side step right left to my beat (heartbeat)
# High like the moon rock with me baby
# Know that I got that heat
# Let me show you cause talk is cheap
# Side step right left to my beat (heartbeat)
# Get it, let it roll
# Smooth like (butter)
# Cool shade (stunner)
# And you know we don't stop
# Hot like (summer)
# Ain't no (bummer)
# You be like oh my god
# We gon' make you rock and you say (yeah)
# We gon' make you bounce and you say (yeah)
# Hotter?
# Sweeter! 
# Cooler?
# Butter!
# Get it, let it roll
# """
# for i in "()?!,-~\".":
#     a = a.replace(i," ")
# a = a.replace("n't"," not ")
# a = a.replace("n'","ng ")
# a = a.replace("'m", " am ")
# a = a.replace("'ve", "have")
# a = a.replace("'re", " are ")
# a = a.replace("'s", " is ")
# a = a.lower()
# word = a.split()
# for i in word :
#     if word.count(i) == 1:
#         print(i, end=" ")# # BTSのbutterの歌詞から重複していない単語を表わす
# a = """
# Smooth like butter
# Like a criminal undercover
# Gon' pop like trouble
# Breakin' into your heart like that
# Cool shade stunner
# Yeah I owe it all to my mother
# Hot like summer
# Yeah I'm makin' you sweat like that
# Break it down
# Oh when I look in the mirror
# I'll melt your heart into 2
# I got that superstar glow so 
# Do the boogie like
# Side step right left to my beat (heartbeat)
# High like the moon rock with me baby
# Know that I got that heat
# Let me show you cause talk is cheap
# Side step right left to my beat (heartbeat)
# Get it, let it roll
# Smooth like butter
# Pull you in like no other
# Don't need no Usher
# To remind me you got it bad
# Ain't no other
# That can sweep you up like a robber
# Straight up I got ya
# Makin' you fall like that
# Break it down
# Oh when I look in the mirror
# I'll melt your heart into 2
# I got that superstar glow so 
# Do the boogie like
# Side step right left to my beat (heartbeat)
# High like the moon rock with me baby
# Know that I got that heat
# Let me show you cause talk is cheap
# Side step right left to my beat (heartbeat)
# Get it, let it roll
# Get it, let it roll
# Get it, let it roll
# No ice on my wrist
# I'm that n-ice guy
# Got that right body and that right mind
# Rollin' up to party got the right vibe
# Smooth like butter
# Hate us love us
# Fresh boy pull up and we lay low
# All the playas get movin' when the bass low
# Got ARMY right behind us when we say so
# Let's go
# Side step right left to my beat (heartbeat)
# High like the moon rock with me baby
# Know that I got that heat
# Let me show you cause talk is cheap
# Side step right left to my beat (heartbeat)
# Get it, let it roll
# Smooth like (butter)
# Cool shade (stunner)
# And you know we don't stop
# Hot like (summer)
# Ain't no (bummer)
# You be like oh my god
# We gon' make you rock and you say (yeah)
# We gon' make you bounce and you say (yeah)
# Hotter?
# Sweeter! 
# Cooler?
# Butter!
# Get it, let it roll
# """
# for i in "()?!,-~\".":
#     a = a.replace(i," ")
# a = a.replace("n't"," not ")
# a = a.replace("n'","ng ")
# a = a.replace("'m", " am ")
# a = a.replace("'ve", "have")
# a = a.replace("'re", " are ")
# a = a.replace("'s", " is ")
# a = a.lower()
# word = a.split()
# for i in word :
#     if word.count(i) == 1:
#         print(i, end=" ")
