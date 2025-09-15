import sys
import time

def printlyrics():
    lines = [
        ("I wanna da-", 0.06),
        ("I wanna dance in the lights", 0.05),
        ("I wanna ro-", 0.07),
        ("I wanna rock your body" , 0.08),
        ("I wanna go", 0.08),
        ("I wanna go for a ride", 0.068),
        ("Hop in the music and", 0.07),
        ("Rock your body", 0.08),
        ("Rock that body", 0.069),
        ("Come on, come on" , 0.035),
        ("Rock your body", 0.005),
        ("((Rock that body))", 0.03),
        ("Rock that body", 0.069),
        ("Come on, come on" , 0.035),
        ("Rock that body", 0.08),
    ]
    delays_after_line = [0.5] * len(lines)
    for i,(line, char_delay) in enumerate(lines): 
        for char in line:
            print(char, end="", flush = True)
            time.sleep(char_delay)
        print()
        time.sleep(delays_after_line[i])


if __name__ == "__main__":
    printlyrics()
