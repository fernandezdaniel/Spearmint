import numpy as np
from spearmint.grids import sobol_grid

def evaluate(job_id, params):

    x = params['X']
    y = params['Y']
    z = params['Z']
    a = params['A']

    print 'Evaluating at (%f, %f, %f, %f)' % (x, y, z, a)

    obj1 = float(1.10471 * np.power(x,2.0) * z + 0.04811 * a * y * (14.0+z))
    obj2 = float(2.1952 / float((np.power(a,3.0)*y)))

    c1 = (float(13600.0-np.power(np.power(6000.0/(np.power(2,0.5)*x*z),2.0)+ np.power( (6000.0*(14.0+0.5*z)*np.power(0.25*(np.power(z,2.0)+np.power(x+a,2.0)),0.5)/(2*np.power(2.0,0.5)*x*z*(np.power(z,2.0)/(12.0)+0.25*np.power(x+a,2.0)))) ,2.0) + z * 6000.0/(np.power(2,0.5)*x*z) * ((6000.0*(14.0+0.5*z)*np.power(0.25*(np.power(z,2.0)+np.power(x+a,2.0)),0.5)/(2.0*np.power(2.0,0.5)*x*z*(np.power(z,2.0)/(12.0)+0.25*np.power(x+a,2.0))))) / (np.power(0.25*(np.power(z,2.0)+np.power(x+a,2.0)),0.5)),0.5)))/75842.5359709

    c2 = (30000.0-504000/(np.power(a,2.0)*y))/8526363.04783

    c3 = (y - x)/2.01692584516
    
    c4 = (64746.022 * (1.0 - 0.0282346 * a) * a *np.power(y, 3.0) - 6000.0)/11617706.4105

    return {
        "o1"       : obj1, 
        "o2"       : obj2, 
        "c1"	   : c1,
        "c2"       : c2,
        "c3"       : c3,
        "c4"       : c4
    }

def obj1(grid):
	return 1.10471 * np.power(grid[:,0],2.0) * grid[:,2] + 0.04811 * grid[:,3] * grid[:,1] * (14.0+grid[:,2])

def obj2(grid):
	return 2.1952 / ((np.power(grid[:,3],3.0)*grid[:,1]))

def c1(grid):
	return 13600.0-np.power(np.power(6000.0/(np.power(2,0.5)*grid[:,0]*grid[:,2]),2.0)+ np.power( (6000.0*(14.0+0.5*grid[:,2])*np.power(0.25*(np.power(grid[:,2],2.0)+np.power(grid[:,0]+grid[:,3],2.0)),0.5)/(2*np.power(2.0,0.5)*grid[:,0]*grid[:,2]*(np.power(grid[:,2],2.0)/(12.0)+0.25*np.power(grid[:,0]+grid[:,3],2.0)))) ,2.0) + grid[:,2] * 6000.0/(np.power(2,0.5)*grid[:,0]*grid[:,2]) * ((6000.0*(14.0+0.5*grid[:,2])*np.power(0.25*(np.power(grid[:,2],2.0)+np.power(grid[:,0]+grid[:,3],2.0)),0.5)/(2*np.power(2.0,0.5)*grid[:,0]*grid[:,2]*(np.power(grid[:,2],2.0)/(12.0)+0.25*np.power(grid[:,0]+grid[:,3],2.0))))) / (np.power(0.25*(np.power(grid[:,2],2.0)+np.power(grid[:,0]+grid[:,3],2.0)),0.5)),0.5)

def c2(grid):
	return 30000.0-504000/(np.power(grid[:,3],2.0)*grid[:,1])

def c3(grid):
	return grid[:,1] - grid[:,0]

def c4(grid):
	return 64746.022 * (1.0 - 0.0282346 * grid[:,3]) * grid[:,3] *np.power(grid[:,1], 3.0) - 6000.0

def get_functions_borders(num_vars = 4, grid_size = 1000000):

	grid = sobol_grid.generate( num_vars , grid_size )

        # Scale grid.

        grid[:,0] = grid[:,0] * ( 5.0 - 0.125 ) + 0.125
        grid[:,1] = grid[:,1] * ( 5.0 - 0.125 ) + 0.125
        grid[:,2] = grid[:,2] * ( 10.0 - 0.1 ) + 0.1
        grid[:,3] = grid[:,3] * ( 10.0 - 0.1 ) + 0.1

	print("Statistics over the objectives and constraints")
	print("==============================================")	
	first_obj_observations = obj1(grid)
	second_obj_observations = obj2(grid)
	first_con_observations = c1(grid)
	second_con_observations = c2(grid)
	third_con_observations = c3(grid)
	fourth_con_observations = c4(grid)
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

def main(job_id, params):
    try:
        return evaluate(job_id, params)
    except Exception as ex:
        print ex
        print 'An error occurred in mocotoy_con.py'
        return np.nan

if __name__ == "__main__":
	#main(0, {u'X': np.array([ 4.0 ]), u'Y': np.array([ 2.8 ]), u'Z': np.array([ 5.0 ]), u'A': np.array([ 2.8 ])})
	get_functions_borders()
