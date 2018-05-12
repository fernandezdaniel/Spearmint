import numpy as np
from spearmint.grids import sobol_grid

def evaluate(job_id, params):

    x = params['X']
    y = params['Y']
    z = params['Z']

    #print 'Evaluating at (%f, %f, %f)' % (x, y, z)

    obj1 = float(x*np.power(16.0+np.power(z,2.0),0.5)+y*np.power(1.0+np.power(z,2.0),0.5)) + np.random.normal(0,0.00008)
    obj2 = float(np.max((20.0*np.power(16.0+np.power(z,2.0)/0.5)/(x*z),80.0*np.power(1.0+np.power(z,2.0),0.5)/(y*z)))) + np.random.normal(0,1120)

    c1 = (float(np.power(10.0,5.0)-np.max((20.0*np.power(16.0+np.power(z,2.0)/0.5)/(x*z),80.0*np.power(1.0+np.power(z,2.0),0.5)/(y*z)))) + np.random.normal(0,0.1)) / 103324.527134

    return {
        "o1"       : obj1, 
        "o2"       : obj2, 
        "c1"	   : c1 * -1.0
    }

def test_grid():
    x = np.linspace( 0.0001,0.01,200 )
    y = np.linspace( 0.0001,0.01,200 )
    z = np.linspace( 1,3,200 )
    x,y,z = np.meshgrid( x,y,z )

    c1a = 20.0*np.power(16.0+np.power(z,2.0),0.5)/(x*z)
    c1b = 80.0*np.power(1.0+np.power(z,2.0),0.5)/(y*z)
    c1 = np.power(10.0,5.0)-np.maximum(c1a,c1b)

    var1 = np.var(c1)
    print np.sqrt(var1)

def obj1(grid):
	return grid[:,0]*np.power(16.0+np.power(grid[:,2],2.0),0.5)+grid[:,1]*np.power(1.0+np.power(grid[:,2],2.0),0.5)

def obj2(grid):
	return np.maximum(20.0*np.power(16.0+np.power(grid[:,2],2.0),0.5)/(grid[:,0]*grid[:,2]),80.0*np.power(1.0+np.power(grid[:,2],2.0),0.5)/(grid[:,1]*grid[:,2]))

def c1(grid):
	return (((np.power(10.0,5.0)-np.maximum(20.0*np.power(16.0+np.power(grid[:,2],2.0),0.5)/(grid[:,0]*grid[:,2]),80.0*np.power(1.0+np.power(grid[:,2],2.0),0.5)/(grid[:,1]*grid[:,2])))+np.random.normal(0,0.1)) / 103324.527134)*-1.0

def get_functions_borders(num_vars = 3, grid_size = 1000000, noise = 0.1):

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

def main(job_id, params):
    try:
        return evaluate(job_id, params)
    except Exception as ex:
        print ex
        print 'An error occurred in mocotoy_con.py'
        return np.nan

if __name__ == "__main__":
	#main(0, {u'X': np.array([ 5.0 ]), u'Y': np.array([ 2.8 ]), u'Z': np.array([ 1.0]) })
	get_functions_borders()
