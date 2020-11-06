def rgb(r, g, b):
    if(r > 255):
        r = 255
    if(g > 255):
        g = 255
    if(b > 255):
        b = 255
    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0
    hr = hex(abs(r)).split('x')[1].upper()
    hg = hex(abs(g)).split('x')[1].upper()
    hb = hex(abs(b)).split('x')[1].upper()
    if len(hr) < 2:
        hr = "0%s" % (hr)
        print(hr)
    if len(hg) < 2:
        hg = "0%s" % (hg)
    if len(hb) < 2:
        hb = "0%s" % (hb)

    return "%s%s%s" % (hr, hg, hb)
