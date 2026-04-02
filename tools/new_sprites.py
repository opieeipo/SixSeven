"""
New sprite definitions for SixSeven Phaser migration.
Defines pixel art for: FARMER_JUMP, FARMER_CROUCH, HEART,
BOSS_CAVE_WORM, BOSS_FIRE_DRAKE, BOSS_RUIN_KNIGHT.
"""

# Reuse the existing palette
_ = None

# Farmer colors
a = "#f0c090"  # skin
A = "#d4a070"  # skin shade
b = "#c87030"  # hat
B = "#e08838"  # hat highlight
c = "#a05828"  # hat band
d = "#4888c8"  # shirt
D = "#3868a0"  # shirt shade
e = "#6050a0"  # pants
E = "#484080"  # pants shade
f = "#5c3d2e"  # boots
F = "#7a5840"  # boots highlight
g = "#302820"  # eye pupil
h = "#ffffff"  # eye white
i = "#c07050"  # mouth
j = "#8060b0"  # overall strap

# Heart colors
hr = "#ff2040"  # heart red
hd = "#c01030"  # heart dark
hp = "#ff6080"  # heart pink highlight

# Cave worm colors
cw1 = "#6a2880"  # purple body
cw2 = "#8a40a0"  # purple highlight
cw3 = "#4a1860"  # purple dark
cw4 = "#e0ff40"  # yellow eyes
cw5 = "#40c060"  # acid green

# Fire drake colors
fd1 = "#c03010"  # red scales
fd2 = "#e05020"  # orange scales
fd3 = "#ff8030"  # belly orange
fd4 = "#ffcc00"  # eye yellow
fd5 = "#801800"  # wing dark

# Ruin knight colors
rk1 = "#40808a"  # teal armor
rk2 = "#286068"  # teal dark
rk3 = "#d0a030"  # gold trim
rk4 = "#ffd860"  # gold highlight
rk5 = "#e02020"  # visor glow
rk6 = "#202830"  # dark steel

# Farmer jumping (arms up, legs tucked) 16x16
FARMER_JUMP = [
    [_,_,_,_,b,b,b,b,b,b,b,b,_,_,_,_],
    [_,_,_,b,B,B,B,B,B,B,B,b,b,_,_,_],
    [_,_,b,b,B,B,B,B,B,B,b,b,b,b,_,_],
    [_,_,b,c,c,c,c,c,c,c,c,c,b,b,_,_],
    [_,_,_,a,a,a,a,a,a,a,a,a,_,_,_,_],
    [_,_,_,a,h,g,a,a,h,g,a,a,_,_,_,_],
    [_,_,_,A,a,a,a,a,a,a,a,a,_,_,_,_],
    [_,_,_,_,a,a,i,i,a,a,a,_,_,_,_,_],
    [_,_,a,d,d,d,d,d,d,d,d,d,a,_,_,_],
    [_,a,_,d,j,D,D,D,D,j,d,_,_,a,_,_],
    [_,_,_,d,j,D,D,D,D,j,d,_,_,_,_,_],
    [_,_,_,e,e,e,e,e,e,e,e,_,_,_,_,_],
    [_,_,_,_,E,e,e,e,e,E,_,_,_,_,_,_],
    [_,_,_,f,F,f,_,_,f,F,f,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
]

# Farmer crouching (squatted, wider stance) 16x10
FARMER_CROUCH = [
    [_,_,_,_,b,b,b,b,b,b,b,b,_,_,_,_],
    [_,_,_,b,B,B,B,B,B,B,b,b,b,_,_,_],
    [_,_,b,c,c,c,c,c,c,c,c,c,b,_,_,_],
    [_,_,_,a,h,g,a,a,h,g,a,a,_,_,_,_],
    [_,_,_,A,a,a,i,i,a,a,a,_,_,_,_,_],
    [_,_,d,d,d,d,d,d,d,d,d,d,_,_,_,_],
    [_,_,d,j,D,D,D,D,D,j,d,_,_,_,_,_],
    [_,_,e,E,e,e,e,e,e,E,e,_,_,_,_,_],
    [_,f,F,f,f,_,_,_,f,f,F,f,_,_,_,_],
    [f,f,F,f,f,_,_,_,f,f,F,f,f,_,_,_],
]

# Heart pickup 8x8
HEART = [
    [_,hr,hr,_,_,hr,hr,_],
    [hr,hp,hr,hr,hr,hp,hr,hr],
    [hr,hr,hr,hr,hr,hr,hr,hr],
    [hr,hr,hr,hr,hr,hr,hr,hr],
    [_,hr,hr,hr,hr,hr,hr,_],
    [_,_,hr,hr,hr,hr,_,_],
    [_,_,_,hr,hr,_,_,_],
    [_,_,_,_,_,_,_,_],
]

# Empty heart 8x8
HEART_EMPTY = [
    [_,hd,hd,_,_,hd,hd,_],
    [hd,_,_,hd,hd,_,_,hd],
    [hd,_,_,_,_,_,_,hd],
    [hd,_,_,_,_,_,_,hd],
    [_,hd,_,_,_,_,hd,_],
    [_,_,hd,_,_,hd,_,_],
    [_,_,_,hd,hd,_,_,_],
    [_,_,_,_,_,_,_,_],
]

# Boss: Cave Worm 24x24 (purple segmented worm with glowing eyes)
BOSS_CAVE_WORM = [
    [_,_,_,_,_,_,_,_,cw1,cw2,cw2,cw1,cw1,cw2,cw2,cw1,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,cw1,cw2,cw1,cw1,cw2,cw2,cw1,cw1,cw2,cw1,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,cw3,cw1,cw2,cw1,cw1,cw1,cw1,cw1,cw1,cw2,cw1,cw3,_,_,_,_,_,_],
    [_,_,_,_,_,cw3,cw1,cw2,cw4,cw1,cw1,cw1,cw1,cw1,cw1,cw4,cw2,cw1,cw3,_,_,_,_,_],
    [_,_,_,_,cw3,cw1,cw1,cw2,cw4,cw1,cw1,cw1,cw1,cw1,cw1,cw4,cw2,cw1,cw1,cw3,_,_,_,_],
    [_,_,_,_,cw1,cw2,cw1,cw1,cw1,cw1,cw5,cw5,cw5,cw5,cw1,cw1,cw1,cw1,cw2,cw1,_,_,_,_],
    [_,_,_,cw3,cw1,cw1,cw2,cw1,cw1,cw5,cw5,cw1,cw1,cw5,cw5,cw1,cw1,cw2,cw1,cw1,cw3,_,_,_],
    [_,_,_,cw1,cw2,cw1,cw1,cw3,cw1,cw1,cw1,cw1,cw1,cw1,cw1,cw1,cw3,cw1,cw1,cw2,cw1,_,_,_],
    [_,_,cw3,cw1,cw1,cw2,cw1,cw3,cw1,cw1,cw1,cw1,cw1,cw1,cw1,cw1,cw3,cw1,cw2,cw1,cw1,cw3,_,_],
    [_,_,cw1,cw2,cw1,cw1,cw3,cw1,cw2,cw1,cw1,cw1,cw1,cw1,cw1,cw2,cw1,cw3,cw1,cw1,cw2,cw1,_,_],
    [_,_,cw1,cw1,cw2,cw1,cw1,cw3,cw1,cw2,cw1,cw1,cw1,cw1,cw2,cw1,cw3,cw1,cw1,cw2,cw1,cw1,_,_],
    [_,_,cw3,cw1,cw1,cw2,cw1,cw1,cw3,cw1,cw1,cw2,cw2,cw1,cw1,cw3,cw1,cw1,cw2,cw1,cw1,cw3,_,_],
    [_,_,_,cw1,cw2,cw1,cw1,cw2,cw1,cw3,cw1,cw1,cw1,cw1,cw3,cw1,cw2,cw1,cw1,cw2,cw1,_,_,_],
    [_,_,_,cw3,cw1,cw1,cw2,cw1,cw1,cw1,cw3,cw1,cw1,cw3,cw1,cw1,cw1,cw2,cw1,cw1,cw3,_,_,_],
    [_,_,_,_,cw1,cw2,cw1,cw1,cw2,cw1,cw1,cw3,cw3,cw1,cw1,cw2,cw1,cw1,cw2,cw1,_,_,_,_],
    [_,_,_,_,cw3,cw1,cw1,cw2,cw1,cw1,cw2,cw1,cw1,cw2,cw1,cw1,cw2,cw1,cw1,cw3,_,_,_,_],
    [_,_,_,_,_,cw1,cw2,cw1,cw1,cw2,cw1,cw3,cw3,cw1,cw2,cw1,cw1,cw2,cw1,_,_,_,_,_],
    [_,_,_,_,_,cw3,cw1,cw1,cw2,cw1,cw1,cw1,cw1,cw1,cw1,cw2,cw1,cw1,cw3,_,_,_,_,_],
    [_,_,_,_,_,_,cw1,cw2,cw1,cw1,cw1,cw2,cw2,cw1,cw1,cw1,cw2,cw1,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,cw1,cw1,cw2,cw1,cw1,cw1,cw1,cw2,cw1,cw1,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,cw3,cw1,cw2,cw1,cw1,cw2,cw1,cw3,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,cw1,cw1,cw3,cw3,cw1,cw1,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,cw3,cw1,cw1,cw3,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
]

# Boss: Fire Drake 24x24 (red/orange dragon with wings spread)
BOSS_FIRE_DRAKE = [
    [_,_,_,_,_,_,_,_,fd1,fd1,_,_,_,_,fd1,fd1,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,fd1,fd2,fd1,_,_,_,fd1,fd2,fd1,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,fd5,fd1,fd2,fd1,fd1,fd1,fd1,fd1,fd2,fd1,fd5,_,_,_,_,_,_,_],
    [_,_,fd5,fd1,fd2,fd5,fd1,fd1,fd2,fd4,fd1,fd1,fd4,fd2,fd1,fd1,fd5,fd2,fd1,fd5,_,_,_,_],
    [_,fd5,fd1,fd2,fd1,fd5,fd1,fd2,fd1,fd1,fd1,fd1,fd1,fd1,fd2,fd1,fd5,fd1,fd2,fd1,fd5,_,_,_],
    [fd5,fd1,fd2,fd1,_,_,fd5,fd1,fd2,fd1,fd1,fd1,fd1,fd2,fd1,fd5,_,_,fd1,fd2,fd1,fd5,_,_],
    [fd1,fd2,fd1,_,_,_,_,fd5,fd1,fd2,fd1,fd1,fd2,fd1,fd5,_,_,_,_,fd1,fd2,fd1,_,_],
    [fd2,fd1,_,_,_,_,_,_,fd1,fd1,fd2,fd2,fd1,fd1,_,_,_,_,_,_,fd1,fd2,_,_],
    [_,_,_,_,_,_,_,_,fd1,fd2,fd1,fd1,fd2,fd1,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,fd1,fd2,fd3,fd3,fd3,fd3,fd2,fd1,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,fd1,fd1,fd3,fd3,fd3,fd3,fd1,fd1,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,fd1,fd2,fd3,fd3,fd3,fd3,fd2,fd1,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,fd5,fd1,fd2,fd3,fd3,fd2,fd1,fd5,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,fd5,fd1,fd2,fd2,fd1,fd5,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,fd5,fd1,fd1,fd5,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,fd1,fd5,fd1,fd1,fd5,fd1,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,fd1,fd2,_,_,_,_,fd2,fd1,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,fd1,fd2,_,_,_,_,_,_,fd2,fd1,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,fd5,fd1,_,_,_,_,_,_,_,_,fd1,fd5,_,_,_,_,_,_,_],
    [_,_,_,_,_,fd5,fd2,_,_,_,_,_,_,_,_,fd2,fd5,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
]

# Boss: Ruin Knight 24x24 (armored knight with sword, teal and gold)
BOSS_RUIN_KNIGHT = [
    [_,_,_,_,_,_,_,_,rk3,rk4,rk3,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,rk3,rk4,rk3,rk4,rk3,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,rk6,rk1,rk2,rk1,rk2,rk1,rk6,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,rk1,rk2,rk5,rk1,rk5,rk2,rk1,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,rk2,rk1,rk1,rk3,rk1,rk1,rk2,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,rk1,rk2,rk1,rk2,rk1,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,rk3,rk1,rk2,rk1,rk1,rk1,rk2,rk1,rk3,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,rk3,rk4,rk1,rk1,rk2,rk2,rk2,rk1,rk1,rk4,rk3,_,_,_,_,_,_,_,_,_],
    [_,_,_,rk6,rk1,rk2,rk1,rk1,rk1,rk3,rk1,rk1,rk1,rk2,rk1,rk6,_,_,_,_,_,_,_,_],
    [_,_,rk6,rk1,rk2,rk1,rk1,rk2,rk3,rk4,rk3,rk2,rk1,rk1,rk2,rk1,rk6,_,_,_,_,_,_,_],
    [_,_,rk1,rk2,rk1,rk1,rk1,rk1,rk2,rk1,rk2,rk1,rk1,rk1,rk1,rk2,rk1,_,_,_,_,_,_,_],
    [_,_,_,rk1,rk2,rk1,rk1,rk1,rk1,rk2,rk1,rk1,rk1,rk1,rk2,rk1,_,_,_,_,_,_,_,_],
    [_,_,_,_,rk1,rk2,rk1,rk3,rk1,rk1,rk1,rk3,rk1,rk2,rk1,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,rk1,rk2,rk4,rk1,rk1,rk1,rk4,rk2,rk1,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,rk1,rk2,rk1,rk1,rk1,rk2,rk1,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,rk2,rk1,rk1,rk3,rk1,rk1,rk2,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,rk1,rk2,rk1,rk1,rk1,rk2,rk1,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,rk6,rk1,rk1,rk2,_,rk2,rk1,rk1,rk6,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,rk1,rk2,rk1,_,_,_,rk1,rk2,rk1,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,rk6,rk1,rk2,_,_,_,_,_,rk2,rk1,rk6,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,rk2,rk1,rk6,_,_,_,_,_,rk6,rk1,rk2,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,rk6,rk2,rk1,_,_,_,_,_,rk1,rk2,rk6,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,rk6,rk6,_,_,_,_,_,_,rk6,rk6,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
]

ALL_NEW_SPRITES = {
    "FARMER_JUMP": FARMER_JUMP,
    "FARMER_CROUCH": FARMER_CROUCH,
    "HEART": HEART,
    "HEART_EMPTY": HEART_EMPTY,
    "BOSS_CAVE_WORM": BOSS_CAVE_WORM,
    "BOSS_FIRE_DRAKE": BOSS_FIRE_DRAKE,
    "BOSS_RUIN_KNIGHT": BOSS_RUIN_KNIGHT,
}
