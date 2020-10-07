import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180,
           168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]


# import list into numpy array
heights_arr = np.array(heights)

# array size / length of heights_arr
print(heights_arr.size)

# array shape / dimension of heights_arr
print(heights_arr.shape)

# sum values greater than 188 of heights_arr
print((heights_arr > 188).sum())

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47,
        55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_and_ages = heights + ages

# convert a list to a numpy array
heights_and_ages_arr = np.array(heights_and_ages)
print(heights_and_ages_arr.shape)

# reshape (2, 45)
heights_and_ages_arr = heights_and_ages_arr.reshape((2, 45))
print(heights_and_ages_arr.shape)

heights_float = [189.0, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183,
                 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

heights_float_arr = np.array(heights_float)

# data type of the array
print(heights_and_ages_arr.dtype)  # int32
print(heights_float_arr.dtype)  # float32

# access by index
print(heights_arr[2])
print(heights_and_ages_arr[1, 4])

# slice
print(heights_and_ages_arr)
# get the 3 first items from the first row
print(heights_and_ages_arr[0, 0:3])
# alternative for above
print(heights_and_ages_arr[0, :3])
# from all rows, get their 4th column
print(heights_and_ages_arr[:, 3])
