# queue_example.py
# FIFO


#10
#20
#30

# Create an empty queue
queue = []

# ENQUEUE operations (insert at rear)
queue.append(10)   
queue.append(20)
queue.append(30)

print("Queue after enqueues:", queue)    #[10,20,30]

# PEEK (front element)
if queue:
    print("Front element:", queue[0])   # 10

# DEQUEUE operation (remove from front)
removed_item = queue.pop(0)         
print("Removed item:", removed_item)  # 10

print("Queue after dequeue:", queue)   # [20,30]

# Check if queue is empty
if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")   # print

# Remove all elements
while queue:
    print("Removing:", queue.pop(0))    #20      # 30

print("Final queue:", queue)    # []




text = "apple banana apple"

split_word = text.split()  #[apple ,banana, apple]
print(split_word)
count = {}

for a in split_word:
   print("word" , count.get(a))
   print("next" ,count.get(a,0))
   print(count.get(a, 0) + 1)
   count[a] = count.get(a, 0) + 1

print(count)
