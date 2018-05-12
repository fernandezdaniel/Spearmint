import numpy as np
from spearmint.grids import sobol_grid

def evaluate(job_id, params):

    x = params['X']
    y = params['Y']
    z = params['Z']

    print 'Evaluating at (%f, %f, %f)' % (x, y, z)

    obj1 = float(x*np.power(16.0+np.power(z,2.0),0.5)+y*np.power(1.0+np.power(z,2.0),0.5))
    obj2 = float(np.max((20.0*np.power(16.0+np.power(z,2.0),0.5)/(x*z),80.0*np.power(1.0+np.power(z,2.0),0.5)/(y*z))))

    c1 = float(np.power(10.0,5.0)-np.max((20.0*np.power(16.0+np.power(z,2.0),0.5)/(x*z),80.0*np.power(1.0+np.power(z,2.0),0.5)/(y*z)))) / 103324.527134

    return {
        "o1"       : obj1, 
        "o2"       : obj2, 
        "c1"	   : c1
    }

def obj1(grid):
	return grid[:,0]*np.power(16.0+np.power(grid[:,2],2.0),0.5)+grid[:,1]*np.power(1.0+np.power(grid[:,2],2.0),0.5)

def obj2(grid):
	return np.maximum(20.0*np.power(16.0+np.power(grid[:,2],2.0),0.5)/(grid[:,0]*grid[:,2]),80.0*np.power(1.0+np.power(grid[:,2],2.0),0.5)/(grid[:,1]*grid[:,2]))

def c1(grid):
	return np.power(10.0,5.0)-np.maximum(20.0*np.power(16.0+np.power(grid[:,2],2.0),0.5)/(grid[:,0]*grid[:,2]),80.0*np.power(1.0+np.power(grid[:,2],2.0),0.5)/(grid[:,1]*grid[:,2]))

def get_functions_borders(num_vars = 3, grid_size = 1000000):

	grid = sobol_grid.generate( num_vars , grid_size )

        # Scale grid.

        grid[:,0] = grid[:,0] * ( 0.01 - 0.0001 ) + 0.0001
        grid[:,1] = grid[:,1] * ( 0.01 - 0.0001 ) + 0.0001
        grid[:,2] = grid[:,2] * ( 3.0 - 1.0 ) + 1.0

	print("Statistics over the objectives and constraints")
	print("==============================================")	
	first_obj_observations = obj1(grid)
	second_obj_observations = obj2(grid)
	first_con_observations = c1(grid)
	max_first_obj = np.max(first_obj_observations)
	min_first_obj = np.min(first_obj_observations)
	max_second_obj = np.max(second_obj_observations)
        min_second_obj = np.min(second_obj_observations)
	max_first_con = np.max(first_con_observations)
        min_first_con = np.min(first_con_observations)
	print("Maximum observation of the first objective")
	print(max_first_obj)
	print("Minimum observation of the first objective")
        print(min_first_obj)
	print("Maximum observation of the second objective")
        print(max_second_obj)
	print("Minimum observation of the second objective")
        print(min_second_obj)
	print("Maximum observation of the first constraint")
        print(max_first_con)
	print("Minimum observation of the first constraint")
        print(min_first_con)

def main(job_id, params):
    try:
        return evaluate(job_id, params)
    except Exception as ex:
        print ex
        print 'An error occurred in mocotoy_con.py'
        return np.nan

if __name__ == "__main__":
	main(0, {u'X': np.array([ 0.005 ]), u'Y': np.array([ 0.002 ]), u'Z': np.array([ 2.0]) })
	#get_functions_borders()
