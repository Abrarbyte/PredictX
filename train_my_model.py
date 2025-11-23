from chain import MarkovChain

# 1st order Markov Chain (simple and enough)
mc = MarkovChain(0)

print("Training started...")

# Train using your file
mc.train("mydata.txt")
mc.train("user_input.txt")    # your user’s new sentences

# Save trained modelpython train_my_model.py

mc.to_json("markov_chain_1st_order.json")

print("Training complete! Model saved as markov_chain_1st_order.json")
