import re
import sys
import math
import os



class State:
    def __init__(self, state):
        self.state = state
        self.count = 0
        self.transition = {}
        self.emission = {}



class Node:
    def __init__(self, token, state = None, prob_word_tag = 1, p = 0, prev = None):
        self.token = token
        self.state = state
        self.p_wi_ti = prob_word_tag
        self.p = p
        self.prev = prev









class Viterbi:

    def makeNode(self, states, word, curNodes, tags):
        for s in states:
            if s.state in tags:
                curNode = Node(word,s,1/float(s.count))
                curNodes.append(curNode)

    def get_distribution(self, states, words, i, curNodes, first):
        if first:
            if re.search('\d', words[i]):
                self.makeNode(states, words[i], curNodes, ['CD'])
            elif re.match(r'\w+\-\w+', words[i]):
                self.makeNode(states,words[i],curNodes,['JJ','NNP'])
            elif words[i].isupper():
                if words[i][-1] == 'S':
                    self.makeNode(states,words[i],curNodes,['NNPS'])
                else:
                    self.makeNode(states,words[i],curNodes,['NNP'])
            elif words[i][0].isupper():
                if not i or words[i-1] == '':
                    word = words[i]
                    word = word.lower()
                    for s in states:
                        num = s.emission.get(word,0)
                        if num:
                            curNode = Node(words[i],s,num/float(s.count))
                            curNodes.append(curNode)
                if not len(curNodes):
                    if words[i][-1] == 's':
                        self.makeNode(states,words[i],curNodes,['NNPS'])
                    else:
                        self.makeNode(states,words[i],curNodes,['NNP'])
            elif len(words[i])>2 and words[-2:]=='ly':
                self.makeNode(states,words[i],curNodes,['RB'])
            else:
                for j in range(2,len(states)):
                    s = states[j]
                    if re.match(r'[A-Z\$]+',s.state):
                        curNode = Node(words[i],s,1/float(s.count))
                        curNodes.append(curNode)
        else:
            for j in range(2,len(states)):
                s = states[j]
                if re.match(r'[A-Z\$]+',s.state):
                    curNode = Node(words[i],s,1/float(s.count))
                    curNodes.append(curNode)

    def get_transition(self, prevNodes, curNodes):
        temp_nodes = []
        for curNode in curNodes:
            curState = curNode.state
            max_prob, best_prev = -sys.maxsize, None
            if len(prevNodes)>=1:
                for prevNode in prevNodes:
                    prevState = prevNode.state

                    #-----------------------#
                    #-------- TO DO --------#
                    #-------- TO DO --------#

                    #compute the trainsitional probabilities
                    

                    #-----------------------#
                    #-------- TO DO --------#
                    #-------- TO DO --------#
                    #comment out this line and assign best_prev the value with highest probablity
                    best_prev = prevNode

                curNode.prev = best_prev
                curNode.p = max_prob
            if curNode.prev:
                temp_nodes.append(curNode)
        curNodes = temp_nodes
        return curNodes

    def run(self, states, wordsFileName, responseFileName_final=None):
        responseFileName = responseFileName_final+".tmp"

        with open(wordsFileName, 'r') as wordsFile, \
                open(responseFileName, 'w') as responseFile:
            words = wordsFile.readlines()
            curNodes = []
            for i in range(len(words)):
                if not i or words[i-1]=='':
                    curNode = Node('', states[0], 1, 1)
                    curNodes = [curNode]
                prevNodes = curNodes
                curNodes = []
                words[i] = words[i].rstrip('\n')
                if words[i] == '':
                    curNode = Node('',states[1], 1)
                    curNodes.append(curNode)
                else:
                    for s in states:
                        num = s.emission.get(words[i],0)
                        if num:
                            curNode = Node(words[i],s,num/float(s.count))
                            curNodes.append(curNode)
                if not len(curNodes):
                    self.get_distribution(states, words, i, curNodes, True)
                curNodes = self.get_transition(prevNodes, curNodes)
                if not len(curNodes):
                    self.get_distribution(states, words, i, curNodes, False)
                curNodes = self.get_transition(prevNodes, curNodes)
                if words[i] == '' and len(curNodes):
                    curNode = curNodes[0]
                    sentences = []
                    while curNode:
                        curState = curNode.state
                        if curState.state not in ['START', 'END']:
                            string = curNode.token+'\t'+curState.state+'\n'
                            sentences.append(string)
                        curNode = curNode.prev
                    for string in sentences[::-1]:
                        responseFile.write(string)
                    responseFile.write('\n')

        fout = open(responseFileName_final,'w')

        for line in open(responseFileName):
            # print(line)
            
            line_values = line.split("\t")
            # print(line_values)
            if len(line_values)==2:
                if line_values[0].strip()=="":
                    continue

            fout.write(line)

        
        os.remove(responseFileName)






def score (keyFileName, responseFileName):
	  keyFile = open(keyFileName, 'r')
	  key = keyFile.readlines()
	  responseFile = open(responseFileName, 'r')
	  response = responseFile.readlines()
	  # if len(key) != len(response):
	  #       print("length mismatch between key and submitted file")
	  #       exit()
	  correct = 0
	  incorrect = 0
	  for i in range(len(key)):
	    key[i] = key[i].rstrip('\n')
	    response[i] = response[i].rstrip('\n')
	    if key[i] == "":
	      if response[i] == "":
	        continue
	      else:
	            print("sentence break expected at line " + str(i))
	            exit()
	    keyFields = key[i].split('\t')
	    if len(keyFields) != 2:
	          print("format error in key at line " + str(i) + ":" + key[i])
	          exit()
	    keyToken = keyFields[0]
	    keyPos = keyFields[1]
	    responseFields = response[i].split('\t')
	    if len(responseFields) != 2:
	          print("format error at line " + str(i))
	          exit()
	    responseToken = responseFields[0]
	    responsePos = responseFields[1]
	    if responseToken != keyToken:
	      print("token mismatch at line " + str(i))
	      exit()
	    if responsePos == keyPos:
	      correct = correct + 1
	    else:
	      incorrect = incorrect + 1
	  print(str(correct) + " out of " + str(correct + incorrect) + " tags correct")
	  accuracy = 100.0 * correct / (correct + incorrect)
	  print("accuracy: %f" % accuracy)




class HMM:
    def __init__(self):
        self.states = []

    def generate(self, datasetName):
        with open(datasetName, 'r') as dataset:
            data = dataset.readlines()
            self.states = [State("START"), State("END")]

            currentIdx = 0
            previousIdx = 0

            for i, row in enumerate(data):
                if not i or data[i-1]=='':
                    curState = self.states[0]
                    curState.count += 1

                    state = 'START'

                row = row.rstrip('\n')

                previousIdx = currentIdx

                if row == '':
                    currentIdx = 1
                    curState = self.states[currentIdx]
                    state = 'END'
                else:
                    token, state = row.split('\t')

                
                preState = self.states[previousIdx]
                preState.transition[state] = preState.transition.get(state,0) + 1
                if state == 'END':
                    continue
                
                flag = False
                length = len(self.states)
                for i in range(length):
                    curState = self.states[i]
                    if curState.state == state:
                        currentIdx = i
                        flag = True
                        curState.count += 1
                        curState.emission[token] = curState.emission.get(token,0) + 1
                if not flag:
                    curState = State(state)
                    curState.count += 1
                    currentIdx = length
                    curState.emission[token] = curState.emission.get(token,0) + 1
                    self.states.append(curState)


                    

if __name__ == "__main__":
    hmm = HMM()
    hmm.generate('data-pos/train.txt')
    V = Viterbi()
    V.run(hmm.states,'data-pos/test_words.txt', 'data-pos/test_response.txt')
    score ('data-pos/test.txt', 'data-pos/test_response.txt')


