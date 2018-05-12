import numpy as np
from spearmint.grids import sobol_grid

NUM_EXP = 1

def evaluate(job_id, params):

    np.random.seed(NUM_EXP)

    x = params['X']
    y = params['Y']

    #print 'Evaluating at (%f, %f)' % (x, y)

    obj1 = float(2.0+np.power(x-2.0,2.0)+np.power(y-2.0,2.0)) + np.random.normal(0,0.95)
    obj2 = float(9.0*x-np.power(y-1.0,2.0)) + np.random.normal(0,0.8)

    c1 = (float(225.0-np.power(x,2.0)-np.power(y,2.0)) + np.random.normal(0,0.04))/168.823484412
    c2 = (float(3.0*y-x-10.0) + np.random.normal(0,0.04))/36.5330991522

    return {
        "o1"       : obj1, 
        "o2"       : obj2, 
        "c1"	   : c1,
	"c2"       : c2
    }

def obj1(grid):
	return 2.0+np.power(grid[:,0]-2.0,2.0)+np.power(grid[:,1]-2.0,2.0)

def obj2(grid):
	return 9.0*grid[:,0]-np.power(grid[:,1]-1.0,2.0)

def c1(grid):
	return 225.0-np.power(grid[:,0],2.0)-np.power(grid[:,1],2.0)

def c2(grid):
	return 3.0*grid[:,1]-grid[:,0]-10.0

def get_functions_borders(num_vars = 2, grid_size = 1000000, noise = 0.1):

	grid = sobol_grid.generate( num_vars , grid_size )

        # Scale grid.

        grid[:,0] = grid[:,0] * ( 20.0 + 20.0 ) - 20.0
        grid[:,1] = grid[:,1] * ( 20.0 + 20.0 ) - 20.0

	print("Statistics over the objectives and constraints")
	print("==============================================")	
	first_obj_observations = obj1(grid)
	second_obj_observations = obj2(grid)
	first_con_observations = c1(grid)
	second_con_observations = c2(grid)
	max_first_obj = np.max(first_obj_observations)
	min_first_obj = np.min(first_obj_observations)
	max_second_obj = np.max(second_obj_observations)
        min_second_obj = np.min(second_obj_observations)
	max_first_con = np.max(first_con_observations)
        min_first_con = np.min(first_con_observations)
	max_second_con = np.max(second_con_observations)
        min_second_con = np.min(second_con_observations)
	print("Maximum observation of the first objective")
	print(max_first_obj)
	print("Minimum observation of the first objective")
        print(min_first_obj)
	print("Noise factor")
	print((max_first_obj-min_first_obj)*noise)
	print("Maximum observation of the second objective")
        print(max_second_obj)
	print("Minimum observation of the second objective")
        print(min_second_obj)
	print("Noise factor")
	print((max_second_obj-min_second_obj)*noise)
	print("Maximum observation of the first constraint")
        print(max_first_con)
	print("Minimum observation of the first constraint")
        print(min_first_con)
	print("Noise factor")
	print((max_first_con-min_first_con)*noise)
	print("Maximum observation of the second constraint")
        print(max_second_con)
	print("Minimum observation of the second constraint")
        print(min_second_con)
	print("Noise factor")
	print((max_second_con-min_second_con)*noise)

def main(job_id, params):
    try:
        return evaluate(job_id, params)
    except Exception as ex:
        print ex
        print 'An error occurred in mocotoy_con.py'
        return np.nan

if __name__ == "__main__":
	#main(0, {u'X': np.array([ 5.0 ]), u'Y': np.array([ 2.8 ])})
	get_functions_borders()
