# Download progress example.
# Violates open-closed principle.
# Example adapted from https://code.tutsplus.com/tutorials/solid-part-2-the-openclosed-principle--net-36600

import unittest
class RemoteFile:

    def __init__(self):
        self.length = 0
        self.sent = 0

class MusicFile(RemoteFile):
    pass

class Progress:

    def __init__(self, f):
        self.file = f

    def getAsPercent(self):
        return self.file.sent * 100 / self.file.length



class ProgressTest(unittest.TestCase):

    def test_progress_as_percent(self):
        mp3_file = MusicFile()
        mp3_file.length = 200
        mp3_file.sent = 100

        progress = Progress(mp3_file)

        self.assertEqual(50, progress.getAsPercent())

    def test_progress_as_percent(self):
        mp3_file = RemoteFile()
        mp3_file.length = 200
        mp3_file.sent = 100

        progress = Progress(mp3_file)

        self.assertEqual(50, progress.getAsPercent())

unittest.main()
