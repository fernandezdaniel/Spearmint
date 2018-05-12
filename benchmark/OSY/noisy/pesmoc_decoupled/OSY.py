import numpy as np
from spearmint.grids import sobol_grid

NUM_EXP = 1

def evaluate(job_id, params):

    np.random.seed(NUM_EXP)

    x = params['X']
    y = params['Y']
    z = params['Z']	
    a = params['A']
    b = params['B']
    c = params['C']
   

    #print 'Evaluating at (%f, %f, %f, %f, %f, %f)' % (x, y, z, a, b, c)

    obj1 = float(-(25.0*np.power(x-2.0,2.0)+np.power(y-2.0,2.0)+np.power(z-1.0,2.0)+np.power(a-4.0,2.0)+np.power(b-1.0,2.0))) + np.random.normal(0,1.6)
    obj2 = float(np.power(x,2.0)+np.power(y,2.0)+np.power(z,2.0)+np.power(a,2.0)+np.power(b,2.0)+np.power(c,2.0)) + np.random.normal(0,0.35)

    c1 = (float(x+y-2.0) + np.random.normal(0,0.05)) / 4.24918292799
    c2 = (float(6.0-x-y) + np.random.normal(0,0.05)) / 4.24918292799
    c3 = (float(2.0-y+x) + np.random.normal(0,0.05)) / 4.24918292799
    c4 = (float(2.0-x+3.0*y) + np.random.normal(0,0.04)) / 9.50146187583
    c5 = (float(4.0-np.power(z-3.0,2.0)-a) + np.random.normal(0,0.04)) / 2.21610268515
    c6 = (float(np.power(b-3.0,2.0)+c-4.0) + np.random.normal(0,0.04)) / 3.26938662273

    return {
        "o1"       : obj1, 
        "o2"       : obj2, 
        "c1"	   : c1,
        "c2"	   : c2,
        "c3"	   : c3,
        "c4"	   : c4,
        "c5"	   : c5,
        "c6"	   : c6
    }

def obj1(grid):
	return -(25.0*np.power(grid[:,0]-2.0,2.0)+np.power(grid[:,1]-2.0,2.0)+np.power(grid[:,2]-1.0,2.0)+np.power(grid[:,3]-4.0,2.0)+np.power(grid[:,4]-1.0,2.0))

def obj2(grid):
	return np.power(grid[:,0],2.0)+np.power(grid[:,1],2.0)+np.power(grid[:,2],2.0)+np.power(grid[:,3],2.0)+np.power(grid[:,4],2.0)+np.power(grid[:,5],2.0)

def c1(grid):
	return grid[:,0]+grid[:,1]-2.0

def c2(grid):
	return 6.0-grid[:,0]-grid[:,1]

def c3(grid):
	return 2.0-grid[:,1]+grid[:,0]

def c4(grid):
	return 2.0-grid[:,0]+3.0*grid[:,1]

def c5(grid):
	return 4.0-np.power(grid[:,2]-3.0,2.0)-grid[:,3]

def c6(grid):
	return np.power(grid[:,4]-3.0,2.0)+grid[:,5]-4.0

def get_functions_borders(num_vars = 6, grid_size = 1000000, noise=0.1):

	grid = sobol_grid.generate( num_vars , grid_size )

        # Scale grid.

        grid[:,0] = grid[:,0] * ( 10.0 - 0.0 ) + 0.0
        grid[:,1] = grid[:,1] * ( 10.0 - 0.0 ) + 0.0
        grid[:,2] = grid[:,2] * ( 5.0 - 1.0 ) + 1.0
        grid[:,3] = grid[:,3] * ( 6.0 - 0.0 ) + 0.0
        grid[:,4] = grid[:,4] * ( 5.0 - 1.0 ) + 1.0
        grid[:,5] = grid[:,5] * ( 10.0 - 0.0 ) + 0.0

	print("Statistics over the objectives and constraints")
	print("==============================================")	
	first_obj_observations = obj1(grid)
	second_obj_observations = obj2(grid)
	first_con_observations = c1(grid)
	second_con_observations = c2(grid)
	third_con_observations = c3(grid)
	fourth_con_observations = c4(grid)
	fifth_con_observations = c5(grid)
	sixth_con_observations = c6(grid)
	max_first_obj = np.max(first_obj_observations)
	min_first_obj = np.min(first_obj_observations)
	max_second_obj = np.max(second_obj_observations)
        min_second_obj = np.min(second_obj_observations)
	max_first_con = np.max(first_con_observations)
        min_first_con = np.min(first_con_observations)
	max_second_con = np.max(second_con_observations)
        min_second_con = np.min(second_con_observations)
	max_third_con = np.max(third_con_observations)
        min_third_con = np.min(third_con_observations)
	max_fourth_con = np.max(fourth_con_observations)
        min_fourth_con = np.min(fourth_con_observations)
	max_fifth_con = np.max(fifth_con_observations)
        min_fifth_con = np.min(fifth_con_observations)
	max_sixth_con = np.max(sixth_con_observations)
        min_sixth_con = np.min(sixth_con_observations)
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
	print("Maximum observation of the third constraint")
        print(max_third_con)
        print("Minimum observation of the third constraint")
        print(min_third_con)
	print("Noise factor")
	print((max_third_con-min_third_con)*noise)
	print("Maximum observation of the fourth constraint")
        print(max_fourth_con)
        print("Minimum observation of the fourth constraint")
        print(min_fourth_con)
	print("Noise factor")
	print((max_fourth_con-min_fourth_con)*noise)
	print("Maximum observation of the fifth constraint")
        print(max_fifth_con)
        print("Minimum observation of the fifth constraint")
        print(min_fifth_con)
	print("Noise factor")
	print((max_fifth_con-min_fifth_con)*noise)
	print("Maximum observation of the sixth constraint")
        print(max_sixth_con)
        print("Minimum observation of the sixth constraint")
        print(min_sixth_con)
	print("Noise factor")
	print((max_sixth_con-min_sixth_con)*noise)

def main(job_id, params):
    try:
        return evaluate(job_id, params)
    except Exception as ex:
        print ex
        print 'An error occurred in mocotoy_con.py'
        return np.nan

if __name__ == "__main__":
	#main(0, {u'X': np.array([ 5.0 ]), u'Y': np.array([ 2.8 ]), u'Z': np.array([ 2.8 ]), u'A': np.array([ 2.8 ]), u'B': np.array([ 2.8 ]), u'C': np.array([ 2.8 ])})
	get_functions_borders()
