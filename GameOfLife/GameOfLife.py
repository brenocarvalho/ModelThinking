'''
Game of Life
Written by Breno W.S.R. de Carvalho in October, 2013
Universidade Federal Fluminense - BR
Loyola University Chicago - USA
'''

def clearScreen():
    print "\n"*80

def matrixFromFile(fileName):
    '''The first line of the file must be the matrix dimensions
       separeted by an space character. The other lines must be
       the matrix, within each element is separeted by an space.'''

    input = file(fileName, 'r')
    lines, columns = map(int, input.readline().split(" "))
    matrix = []
    for _ in xrange(lines):
        line = input.readline()
        print line.split(" ")
        line = map(int, line.split(" "))
        if len(line) != columns:
            raise ValueError
        matrix.append(line)
    return matrix

def changeObjs(a,b):
    aux = a
    a = b
    b = a

class GameOfLife:

    def __init__(self, matrix):
        self.old_matrix = matrix
        self.new_matrix = []
        self.time = 0
        self.changed = False
        for line in matrix:
            self.new_matrix.append(line[:])

    @staticmethod    
    def toggle(i, j, matrix):
        matrix[i][j] = 1 - matrix[i][j]

    @staticmethod
    def isOn(i, j, matrix):
        return matrix[i][j] == 1

    @staticmethod
    def numNeighboursOn(i, j, matrix):
        counter = 0
        lines = range(max(0, i-1), 1+min(i+1, len(matrix)-1))
        columns = range(max(0, j-1), 1+min(j+1, len(matrix[0])-1))
        for line in lines:
            for column in columns:
                if GameOfLife.isOn(line, column, matrix):
                    counter += 1
        if GameOfLife.isOn(i,j,matrix):
            counter -= 1
        return counter
        
    def getMatrix(self):
        return self.new_matrix

    def hasChanged(self):
        '''Returns true if the board changed after the last clock'''
        return self.changed

    def getClock(self):
        return self.time

    @staticmethod
    def cloneMatrix(a, b):
        for i in range(len(a)):
            for j in range(len(b)):
                b[i][j] = a[i][j]

    def clock(self):
        self.changed = False
        GameOfLife.cloneMatrix(self.new_matrix, self.old_matrix)
        for i in range(len(self.old_matrix)):
            for j in range(len(self.old_matrix[0])):
                numNeighbours = GameOfLife.numNeighboursOn(i,j, self.old_matrix)
                #print "%d " %numNeighbours,
                if not GameOfLife.isOn(i,j, self.old_matrix):
                    if numNeighbours == 3:
                        GameOfLife.toggle(i,j, self.new_matrix)
                        self.changed = True
                else:
                    if GameOfLife.isOn(i,j, self.old_matrix) and (numNeighbours > 3 or numNeighbours < 2) :
                        GameOfLife.toggle(i,j, self.new_matrix)
                        self.changed = True
            #print
        changeObjs(self.old_matrix, self.new_matrix)
        self.time +=1

    def __str__(self):
        out = "Round: %d \nBoard:\n" %self.time
        for line in self.new_matrix:
            for cell in line:
                out += "%s " % ("o" if cell == 1 else " ")
            out+= "\n"
        return out
#-----------------------

def readArgv(argv):
    iterations = 5
    f_rate = 2
    try:
        if len(argv) >= 3:
            iterations = int(argv[2])
        else:
            print "Usage: python %s [input_file] [num_iterations] [frame_rate]" %argv[0]
            exit()
        if  len(argv) >= 4:
            f_rate = float(argv[3])
            if f_rate == 0:
                raise ValueError
    except ValueError:
        print "Invalid argument(s), using default"
    return argv[1], iterations, f_rate

if __name__ == "__main__":
    from sys import argv,exit
    from time import sleep
    import matplotlib.pyplot as plt

    try:
        f_name, iterations, f_rate = readArgv(argv)
        matrix = matrixFromFile(f_name)
        game = GameOfLife(matrix)
        clearScreen()
        print game
        fig = plt.figure() # make figure
        im = plt.imshow(game.getMatrix(), interpolation='nearest', cmap=plt.cm.gist_gray)
        plt.ion()
        #plt.grid(True)
        plt.show()

        for i in range(iterations):
            sleep(1./f_rate)
            game.clock()
            if not game.hasChanged():
                break
            clearScreen()
            print game
            im.set_data(game.getMatrix())
            plt.draw()
        print "Done"
        raw_input()
    except KeyboardInterrupt:
        pass
