from chain import MarkovChain
#second order=1
mc = MarkovChain(1)
print("training started")
mc.train("mydata.txt")
try:
    mc.train("user_input.txt")


except:
    pass
mc.to_json("markov_chain_2nd_order.json")
print("training is completed and file is saved")