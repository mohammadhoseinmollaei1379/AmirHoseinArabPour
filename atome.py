from vpython import *
import random

# تنظیم صحنه
scene.background = color.black
scene.title = "شبیه‌سازی اتم کربن (نسخه بهینه)"

# ایجاد پروتون‌ها و نوترون‌ها در هسته با موقعیت تصادفی
nucleus = []
for i in range(6):
    pos = vector(random.uniform(-0.2,0.2), random.uniform(-0.2,0.2), random.uniform(-0.2,0.2))
    nucleus.append(sphere(pos=pos, radius=0.1, color=color.red))
for i in range(6):
    pos = vector(random.uniform(-0.2,0.2), random.uniform(-0.2,0.2), random.uniform(-0.2,0.2))
    nucleus.append(sphere(pos=pos, radius=0.1, color=color.gray(0.5)))

# ایجاد الکترون‌ها با دنباله نرم و زاویه‌های نامتقارن
electrons = []
angles_layer1 = [0, pi/1.5]
angles_layer2 = [0, pi/3, 2*pi/3, pi]

for angle in angles_layer1:
    x = cos(angle)
    y = sin(angle)
    electrons.append(sphere(pos=vector(x, y, 0), radius=0.05, color=color.blue,
                            make_trail=True, trail_radius=0.01, retain=150))

for angle in angles_layer2:
    x = 2 * cos(angle)
    y = 2 * sin(angle)
    electrons.append(sphere(pos=vector(x, y, 0), radius=0.05, color=color.blue,
                            make_trail=True, trail_radius=0.01, retain=150))

# حرکت الکترون‌ها با سرعت مناسب و نرخ بروزرسانی بالا
angle = 0
speed = 0.01
while True:
    rate(200)
    angle += speed
    for i in range(2):
        x = cos(angle + i*pi/1.5)
        y = sin(angle + i*pi/1.5)
        electrons[i].pos = vector(x, y, 0)
    for i in range(2,6):
        x = 2 * cos(angle + (i-2)*pi/3)
        y = 2 * sin(angle + (i-2)*pi/3)
        electrons[i].pos = vector(x, y, 0)