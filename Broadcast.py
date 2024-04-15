def broadcast_function(source_node, data3, nodes):
    print("Broadcasting Data")
    for node in nodes:
        if node != source_node :
            broadcast_message(source_node, node,data3)

def broadcast_message(sender, receiver,data3):
    message="Data Recieved:",data3
    print(f"Message from node {sender} to node {receiver}: {message}")
