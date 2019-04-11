# Demo for SOLID.
from time import sleep
from random import randint

class ScreenLogger:

    def emit(self, msg):
        print(msg)

class FileLogger:

    def emit(self, msg):
        with open("moon.log", "a") as f:
            f.write(msg + "\n")


def log(msg, logger):
    logger.emit(msg)

def perform(manuever):
    # pretend we are performing it
    log(manuever)

    # simulate a hard-to-find bug:
    if randint(1,5) == 1:
        raise Exception("Crashed during " + manuever)

def land_on_moon():
    phases = ["Liftoff!", "Low-Earth Orbit Insertion", "Orbiting Earth",
              "Going to Moon Orbit", "Moon Orbit Insertion", "Oribiting Moon",
              "Descending to Surface", "Landed!"]

    try:
        for phase in phases:
            log("About to do " + phase)
            perform(phase)
            log("Completed " + phase)
            sleep(0.5)
    except Exception as e:
        print(e)

land_on_moon()


# Requirements have changed:
# * log based on severity level
# * log to file
# * log with timestamp (datetime.datetime.now())

# Ideas:
# * Parameters?
# * Polymorphism?
# * Duck typing?
# * Dependency Inversion?
