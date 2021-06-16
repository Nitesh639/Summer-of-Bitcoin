mempool=open ("mempool.csv")
row_no=0
weight_total=0
useful_tx_id_details=list()
tx_id_list=list()
valid_block=list()

#my idea for this problem
def algorithm():
    fee_per_weight=int(row[1])/int(row[2])
    id_details=(fee_per_weight,row[0],row[2],row[1])
    useful_tx_id_details.append(id_details)

    
for line in mempool:
    if(row_no>0):
        row=line.split(",")
        tx_id_list.append(row[0])
        parent = row[3].strip("\n")
        
        if parent in tx_id_list: 
            algorithm()
            
        elif parent=='':
            algorithm()
                        
        else:
            pass
    row_no +=1

    
useful_tx_id_details.sort(reverse=True)

#we append here only those blocks who return max fee         
for id_details in useful_tx_id_details:
    weight_total=weight_total+int(id_details[2])
    if(weight_total< 4000000):
        valid_block.append(id_details[1])

#Now, Transactions appear in order by this code
for tx_id in tx_id_list:
    if tx_id in valid_block:
        print(tx_id)