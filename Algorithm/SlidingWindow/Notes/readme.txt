So, always remember this core sliding window length formula:

🧩 window_length = end - start + 1



🪄 Visual Animation Example

Let’s say our array = [3, 8, 5, 2, 7, 4]

We are sliding the window over it.

Step 1:
start = 0, end = 0
window = [3]
window_length = end - start + 1 = 0 - 0 + 1 = 1


✅ 1 element in window

Step 2:
start = 0, end = 1
window = [3, 8]
window_length = 1 - 0 + 1 = 2


✅ 2 elements in window

Step 3:
start = 0, end = 2
window = [3, 8, 5]
window_length = 2 - 0 + 1 = 3


✅ 3 elements in window

Step 4:
Now we move start forward
start = 1, end = 3
window = [8, 5, 2]
window_length = 3 - 1 + 1 = 3


✅ Still 3 elements

So, always remember this core sliding window length formula:

🧩 window_length = end - start + 1

🧩 Why +1 is Needed

Because both start and end are inclusive indexes.
If you don’t add 1, you’ll always be off by one in the count.

Think of this as:

distance between two points = (end - start)
but you include both ends → +1