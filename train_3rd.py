from chain import MarkovChain

mc = MarkovChain(2)
print("started training")

mc.train("mydata.txt")

try:
    mc.train("user_input.txt")

except:
    pass
mc.to_json("markov_chain_3rd_order.json")
print("training is completed and file is saved") 
