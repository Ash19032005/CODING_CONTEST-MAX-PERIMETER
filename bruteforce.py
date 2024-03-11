def read_input_from_file(filename):
    with open(filename, 'r') as file:
        # Read the total number of elements from the first line
        n= int(file.readline().strip())
        # Initialize an empty list to store elements
        elements = []
        # Read the elements in chunks
        chunk_size = 10000  # Adjust the chunk size as needed
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break  # End of file
            elements.extend(map(int, chunk.split()))
    return n,elements
n,nums = read_input_from_file("testcase9.txt")
nums.sort()
res = 0
arr = []
for i in range(len(nums)):
    total_sum = sum(nums[:i])
    if total_sum >= nums[i]:
        arr.append(total_sum)
if sum(nums[0:len(nums)-1])<nums[-1]:
    print(max(arr))
else:
    print(max(arr)+nums[-1])

