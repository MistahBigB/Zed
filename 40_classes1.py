#40 classes1

class song(object):
    #The first method must always be self because it refers to the object, not the class.
    def __init__(self, lyrics): #double underscores
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

#cold is a variable list passed to the object
cold = ["The will to rise above",
        "Is tearing my insides out"]

iron = song(["Raise your fist beside your brothers",
             "Stand eternally proud",
             "We are the few and the brave",
             "Forever one with the Sound",
             "We are the Iron Brotherhood!"])

#The variable cold is now passed to the object
cold = song(cold)

cold.sing_me_a_song()
iron.sing_me_a_song()
