import numpy as np

def test_list_indexing(todo_list):
    
    try:
        assert(todo_list[2] == 'REPLACED')
    except AssertionError as e:
        print("The element 'TO_REPLACE_1' is not correctly replaced!")
        raise(e)
 
    try:
        assert(todo_list[-1][-1][-1] == 'REPLACED')
    except AssertionError as e:
        print("The element 'TO_REPLACE_2' is not correctly replaced!")
        raise(e)
   
    print('Well done!')


def test_slicing_1(lst):
    
    c_answer = [2, 3, 4, 5, 6]
    try:
        assert(lst == c_answer)
    except AssertionError:
        print('The slice is incorrect!')
        raise IncorrectAnswer(lst, c_answer)
    else:
        print("Well done!")


def test_slicing_2(lst):
    
    c_answer = [5, 7, 9, 11]
    
    try:
        assert(lst == c_answer)
    except AssertionError:
        print('The slice is incorrect!')
        raise IncorrectAnswer(lst, c_answer)
    else:
        print("Well done!")

        
def test_create_array_with_zeros(arr):
    
    c_answer = np.zeros((2, 3, 5, 3, 7))
    try:
        assert(np.all(arr.shape == c_answer.shape))
    except AssertionError as e:
        print("Your array has the wrong shape, namely %r, but I expected %r" % (arr.shape, c_answer.shape,))
        raise(e)

    try:
        assert(np.all(arr == 0.0))
    except AssertionError as e:
        print("Your array does not contain zeros ... Did you use np.zeros()?")
        raise(e)

    print("Well done!")

    
def test_fill_array_with_complement(arr):
    
    c_answer = 1.0 / np.arange(1, 9)
    try:
        np.testing.assert_array_almost_equal(arr, c_answer, 4)
    except AssertionError as e:
        print("Your array (%r) does not match the correct answer (%r)!" % (arr, c_answer))
        raise(e)
    else:
        print("AWESOME!")


def test_set_odd_indices_to_zero(arr):
    
    c_answer = np.arange(3, 25)
    c_answer[1::2] = 0.0
    
    try:
        np.testing.assert_array_almost_equal(arr, c_answer, 4)
    except AssertionError as e:
        print("Your array (%r) does not match the correct answer (%r)!" % (arr, c_answer))
        raise(e)
    else:
        print("Good job!")


def test_set_lower_right_value_to_one(arr):
    
    c_answer = np.zeros((3, 3))
    c_answer[-1, -1] = 1.0
    
    try:
        np.testing.assert_array_almost_equal(arr, c_answer, 4)
    except AssertionError as e:
        print("Your array: \n\n%r\n\ndoes not match the correct answer:\n\n%r!" % (arr, c_answer))
        raise(e)
    else:
        print("Superb!")


def test_bloodpressure_index(arr):

    np.random.seed(42)
    bp_data = np.random.normal(loc=100, scale=5, size=(20, 24, 30, 2))
    c_answer = bp_data[:, :, 17, 1]

    try:
        assert(arr.shape == (20, 24))
    except AssertionError as e:
        print("The result of your indexing operation is of shape %r, "
              "while it should be %r, namely 20 subjects by 24 hours"  % (arr.shape, (20, 24)))
        raise(e)

    try:
        np.testing.assert_array_almost_equal(arr, c_answer, 4)
    except AssertionError as e:
        print("Your answer is not correct! Did you perhaps forget that Python has zero-based indexing? (First index is 0!)")
        raise(e)
    
    print("You're incredible!")


def test_boolean_indexing(arr):
    
    my_array = np.array([[0, 1, -1, -2],
                     [2, -5, 1, 4],
                     [10, -2, -4, 20]])
    c_answer = my_array[my_array ** 2 > 4]
    
    try:
        np.testing.assert_array_equal(arr, c_answer)
    except AssertionError as e:
        print("Incorrect answer! I expected %r, but I got %r" % (c_answer, arr))
        raise(e)
    
    print("EPIC!")
    

def test_tvalue_computation(arr, h0, tval_ans):
    
    c_tval = (arr.mean() - h0) / (arr.std() / np.sqrt(arr.size - 1))
    
    try:
        np.testing.assert_almost_equal(tval_ans, c_tval)
    except AssertionError as e:
        print("T-value is incorrect! Your t-value is %.3f, while it should be %.3f" % (tval_ans, c_tval))
        raise(e)
    
    print("Correct! You stats wizard!")

    
def test_array_product_and_sum(arr):
    
    arr_A = np.arange(10).reshape((5, 2))
    arr_B = np.arange(10, 20).reshape((5, 2))
    c_answer = (arr_A * arr_B) + 5

    try:
        np.testing.assert_array_equal(arr, c_answer)
    except AssertionError as e:
        print("Your answer is incorrect! I got:\n\n%r\n\nbut I expected:\n\n%r" % (arr, c_answer))
        raise(e)
    else:
        print("Great!")
        

def test_compute_range_vectorized(arr, ans):
    
    c_answer = arr.max(axis=0) - arr.min(axis=0)
    
    try:
        assert(ans.shape == c_answer.shape)
    except AssertionError as e:
        print("The shape of your answer is incorrect! I got %r, "
              "but I expected %r for input-array of shape %r" % (ans.shape, c_answer.shape, arr.shape))
        raise(e)
    
    try:
        np.testing.assert_array_almost_equal(ans, c_answer, 4)
    except AssertionError as e:
        print("Your answer is incorrect! Your answer is:\n\n%r/n/n But I expected:\n\n%r" % (ans, c_answer))
        raise(e)
    
    print("Easy peasy!")