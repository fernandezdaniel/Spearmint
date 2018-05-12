import numpy as np
from spearmint.grids import sobol_grid

def evaluate(job_id, params):

    x = params['X']
    y = params['Y']

    print 'Evaluating at (%f, %f)' % (x, y)

    obj1 = float(4.0*np.power(x,2.0)+4.0*np.power(y,2.0)) + np.random.normal(0,1.3)
    obj2 = float(np.power(x-5.0,2.0)+np.power(y-5.0,2.0)) + np.random.normal(0,0.45)

    c1 = ( 25.0-np.power(x-5.0,2.0)-np.power(y,2.0) + np.random.normal(0,0.05) ) / 7.92604994102
    c2 = ( np.power(x-8.0,2.0)+np.power(y+3.0,2.0)-7.7  + np.random.normal(0,0.04) ) / 17.8066390633


    return {
        "o1"       : obj1, 
        "o2"       : obj2, 
        "c1"	   : c1 * -1.0,
	"c2"       : c2 * -1.0
    }

def test_grid():
    x = np.linspace( 0.0,5.0,2000 )
    y = np.linspace( 0.0,3.0,2000 )
    x,y = np.meshgrid( x,y )

    c1 = (25.0-np.power(x-5.0,2.0)-np.power(y,2.0) + np.random.normal(0,0.05))*-1.0
    c2 = (np.power(x-8.0,2.0)+np.power(y+3.0,2.0)-7.7 + np.random.normal(0,0.04))*-1.0

    var1 = np.var(c1)
    var2 = np.var(c2)
    print np.sqrt(var1)
    print np.sqrt(var2)

def obj1(grid):
        return 4.0*np.power(grid[:,0],2.0)+4.0*np.power(grid[:,1],2.0) + np.random.normal(0,1.3)

def obj2(grid):
        return np.power(grid[:,0]-5.0,2.0)+np.power(grid[:,1]-5.0,2.0) + np.random.normal(0,0.45)

def c1(grid):
        return ((25.0-np.power(grid[:,0]-5.0,2.0)-np.power(grid[:,1],2.0) + np.random.normal(0,0.3))/7.92604994102 )*-1.0

def c2(grid):
        return ((np.power(grid[:,0]-8.0,2.0)+np.power(grid[:,1]+3.0,2.0)-7.7  + np.random.normal(0,0.8))/17.8066390633 )*-1.0

def get_functions_borders(num_vars = 2, grid_size = 10000):

        grid = sobol_grid.generate( num_vars , grid_size )

        # Scale grid.

        grid[:,0] = grid[:,0] * ( 5.0 - 0.0 ) + 0.0
        grid[:,1] = grid[:,1] * ( 3.0 - 0.0 ) + 0.0

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
        print("Maximum observation of the second objective")
        print(max_second_obj)
        print("Minimum observation of the second objective")
        print(min_second_obj)
        print("Maximum observation of the first constraint")
        print(max_first_con)
        print("Minimum observation of the first constraint")
        print(min_first_con)
        print("Maximum observation of the second constraint")
        print(max_second_con)
        print("Minimum observation of the second constraint")
        print(min_second_con)

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
