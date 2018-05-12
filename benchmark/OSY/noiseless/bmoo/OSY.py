import numpy as np
from spearmint.grids import sobol_grid

def evaluate(job_id, params):

    x = params['X']
    y = params['Y']
    z = params['Z']	
    a = params['A']
    b = params['B']
    c = params['C']
   

    #print 'Evaluating at (%f, %f, %f, %f, %f, %f)' % (x, y, z, a, b, c)

    obj1 = float(-(25.0*np.power(x-2.0,2.0)+np.power(y-2.0,2.0)+np.power(z-1.0,2.0)+np.power(a-4.0,2.0)+np.power(b-1.0,2.0)))
    obj2 = float(np.power(x,2.0)+np.power(y,2.0)+np.power(z,2.0)+np.power(a,2.0)+np.power(b,2.0)+np.power(c,2.0))

    c1 = (float(x+y-2.0)) / 4.24918292799
    c2 = (float(6.0-x-y)) / 4.24918292799
    c3 = (float(2.0-y+x)) / 4.24918292799
    c4 = (float(2.0-x+3.0*y)) / 9.50146187583
    c5 = (float(4.0-np.power(z-3.0,2.0)-a)) / 2.21610268515
    c6 = (float(np.power(b-3.0,2.0)+c-4.0)) / 3.26938662273

    return {
        "o1"       : obj1, 
        "o2"       : obj2, 
        "c1"	   : c1 * -1.0,
        "c2"	   : c2 * -1.0,
        "c3"	   : c3 * -1.0,
        "c4"	   : c4 * -1.0,
        "c5"	   : c5 * -1.0,
        "c6"	   : c6 * -1.0
    }

def test_grid():
    x = np.linspace( 0.0,10.0,25 )
    y = np.linspace( 0.0,10.0,25 )
    z = np.linspace( 1.0,5.0,25 )
    a = np.linspace( 0.0,6.0,25 )
    b = np.linspace( 1.0,5.0,25 )
    c = np.linspace( 0.0,10.0,25 )

    x,y,z,a,b,c = np.meshgrid( x,y,z,a,b,c )

    c1 = x+y-2.0
    c2 = 6.0-x-y
    c3 = 2.0-y+x
    c4 = 2.0-x+3.0*y
    c5 = 4.0-np.power(z-3.0,2.0)-a
    c6 = np.power(b-3.0,2.0)+c-4.0

    var1 = np.var(c1)
    var2 = np.var(c2)
    var3 = np.var(c3)
    var4 = np.var(c4)
    var5 = np.var(c5)
    var6 = np.var(c6)
    print np.sqrt(var1)
    print np.sqrt(var2)
    print np.sqrt(var3)
    print np.sqrt(var4)
    print np.sqrt(var5)
    print np.sqrt(var6)

def obj1(grid):
	return -(25.0*np.power(grid[:,0]-2.0,2.0)+np.power(grid[:,1]-2.0,2.0)+np.power(grid[:,2]-1.0,2.0)+np.power(grid[:,3]-4.0,2.0)+np.power(grid[:,4]-1.0,2.0))

def obj2(grid):
	return np.power(grid[:,0],2.0)+np.power(grid[:,1],2.0)+np.power(grid[:,2],2.0)+np.power(grid[:,3],2.0)+np.power(grid[:,4],2.0)+np.power(grid[:,5],2.0)

def c1(grid):
	return ((grid[:,0]+grid[:,1]-2.0)/4.24918292799)*-1.0

def c2(grid):
	return ((6.0-grid[:,0]-grid[:,1])/4.24918292799)*-1.0

def c3(grid):
	return ((2.0-grid[:,1]+grid[:,0])/4.24918292799)*-1.0

def c4(grid):
	return ((2.0-grid[:,0]+3.0*grid[:,1])/9.50146187583)*-1.0

def c5(grid):
	return ((4.0-np.power(grid[:,2]-3.0,2.0)-grid[:,3])/2.21610268515)*-1.0

def c6(grid):
	return ((np.power(grid[:,4]-3.0,2.0)+grid[:,5]-4.0)/3.26938662273)*-1.0

def get_functions_borders(num_vars = 6, grid_size = 1000000):

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
	print("Maximum observation of the third constraint")
        print(max_third_con)
        print("Minimum observation of the third constraint")
        print(min_third_con)
	print("Maximum observation of the fourth constraint")
        print(max_fourth_con)
        print("Minimum observation of the fourth constraint")
        print(min_fourth_con)
	print("Maximum observation of the fifth constraint")
        print(max_fifth_con)
        print("Minimum observation of the fifth constraint")
        print(min_fifth_con)
	print("Maximum observation of the sixth constraint")
        print(max_sixth_con)
        print("Minimum observation of the sixth constraint")
        print(min_sixth_con)


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
