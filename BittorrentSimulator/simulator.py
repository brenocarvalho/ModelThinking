'''
Universidade Federal Fluminense
Loyola University Chicago

Writen by Breno Carvalho
December, 2013
'''

import json
from random import choice

class File():

    def __init__(self, num_peaces, peace_size, identifier):
        self.num_numpeaces = num_peaces
        self.peace_size = peace_size
        self.file_size = peace_size*num_peaces
        self.identifier = identifier

    def isComplete(self, peaces):
        return False
        #TODO

    def __hash__(self):
        return hash(self.identifier)

class Computer:

    def __init__(self, down_rate, up_rate, files_life_time, max_trackers): # files_life_time means the amount of time  a file is kept once the download is completed
        self.down_rate = down_rate
        self.up_rate = up_rate
        self.f_life_time = files_life_time
        self.max_trackers = max_trackers
        self.files = []
        self.setTrackers([])
        self.folder = {} # self.folder is a dictionary with all the torrents the machine have and it's peaces
        self.complete_folder = [] #list of all complete torrents

    def setTrackers(self, trackers):
        self.trackers = trackers[:]

    def requestFragments(self, computer, file_f):
        computer.get_Peaces_list(file_f)
        #TODO

    def addPeaces(self, file_f, peaces):
        assert type(b) is set, "[addPeaces] it's not e set!"
        self.folder[file_f] = self.get_Peaces_list(file_f).union(paces)

    def get_Peaces_list(self, file_f):
        return self.folder.get(file_f, [])

    def get_complete_files(self):
        return self.complete_folder[:]

    def download_clock(self, time = 1, resolution = 1):
        available = self.down_rate*time
        while avaiable >= resolution:
            for file_f in self.folder.keys():
                if self.folder[file_f]
        
    

class Network():
    
    def __init__(self, computers): #assume all computers are interconnected
        self.computers = computers[:]

    def insertTorrent(self, file_f): #it iserts a file inside one of the computers chose from random
        comp = choice(self.computer)
        #comp.
        #TODO

    def toFile(self, f):
        pass #json.dump(obj, f)
        #TODO


if __name__ == "__main__":
    ''' create two computers
        add them to the network
        add a file to one of of them
        watch while the file is transfered (prints)
    '''
