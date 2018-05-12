import numpy as np
from spearmint.grids import sobol_grid

def evaluate(job_id, params):

    x = params['X']
    y = params['Y']
    z = params['Z']

    #print 'Evaluating at (%f, %f, %f)' % (x, y, z)

    obj1 = float(106780.37*(y+z) + 61704.67) + np.random.normal(0,190)
    obj2 = float(3000.0*x) + np.random.normal(0,13)
    obj3 = 305700.0*2289.0*y/np.power(0.06*2289.0,0.65) + np.random.normal(0,25600)
    obj4 = 250.0*2289.0*np.exp(-39.75*y + 9.9*z + 2.74) + np.random.normal(0,158120)
    obj5 = 25.0*(1.39/(x*y)+4940.0*z-80.0) + np.random.normal(0,3400)

    c1 = (float(1.0-0.00139/(x*y)-4.94*z+0.08) + np.random.normal(0,0.21))/0.636279333822
    c2 = (float(1.0-0.000306/(x*y)-1.082*z+0.0986) + np.random.normal(0,0.21))/0.140043905079
    c3 = (float(50000.0-12.307/(x*y) - 49408.24*z - 4051.02) + np.random.normal(0,0.21))/5665.45611369
    c4 = (float(16000.0 - 2.098/(x*y) - 8046.33*z + 696.71) + np.random.normal(0,0.21))/963.611681082
    c5 = (float(10000.0 - 2.138/(x*y) - 7883.39*z + 705.04) + np.random.normal(0,0.21))/980.215853013
    c6 = (float(2000.0 - 0.417/(x*y) - 1721.26*z + 136.54 ) + np.random.normal(0,0.21))/192.247633347
    c7 = (float(550.0 - 0.164/(x*y) - 631.13*z + 54.48 ) + np.random.normal(0,0.21))/75.3374871091

    return {
        "o1"       : obj1, 
        "o2"       : obj2, 
        "o3"       : obj3,
        "o4"       : obj4,
        "o5"       : obj5,
        "c1"	   : c1,
        "c2"       : c2,
        "c3"       : c3,
        "c4"       : c4,
        "c5"       : c5,
        "c6"       : c6,
        "c7"       : c7
    }

def obj1(grid):
	return 106780.37*(grid[:,1]+grid[:,2]) + 61704.67

def obj2(grid):
	return 3000.0*grid[:,0]

def obj3(grid):
	return 305700.0*2289.0*grid[:,1]/np.power(0.06*2289.0,0.65)

def obj4(grid):
	return 250.0*2289.0*np.exp(-39.75*grid[:,1] + 9.9*grid[:,2] + 2.74)

def obj5(grid):
	return 25.0*(1.39/(grid[:,0]*grid[:,1])+4940.0*grid[:,2]-80.0)

def c1(grid):
	return 1.0-0.00139/(grid[:,0]*grid[:,1])-4.94*grid[:,2]+0.08

def c2(grid):
	return 1.0-0.000306/(grid[:,0]*grid[:,1])-1.082*grid[:,2]+0.0986

def c3(grid):
	return 50000.0-12.307/(grid[:,0]*grid[:,1]) - 49408.24*grid[:,2] - 4051.02

def c4(grid):
	return 16000.0 - 2.098/(grid[:,0]*grid[:,1]) - 8046.33*grid[:,2] + 696.71

def c5(grid):
	return 10000.0 - 2.138/(grid[:,0]*grid[:,1]) - 7883.39*grid[:,2] + 705.04

def c6(grid):
	return 2000.0 - 0.417/(grid[:,0]*grid[:,1]) - 1721.26*grid[:,2] + 136.54

def c7(grid):
	return 550.0 - 0.164/(grid[:,0]*grid[:,1]) - 631.13*grid[:,2] + 54.48

def get_functions_borders(num_vars = 3, grid_size= 1000000, noise = 0.1):

	grid = sobol_grid.generate( num_vars , grid_size )

        # Scale grid.

        grid[:,0] = grid[:,0] * ( 0.45 - 0.01 ) + 0.01
        grid[:,1] = grid[:,1] * ( 0.1 - 0.01 ) + 0.01
        grid[:,2] = grid[:,2] * ( 0.1 - 0.01 ) + 0.01

	print("Statistics over the objectives and constraints")
	print("==============================================")	
	first_obj_observations = obj1(grid)
	second_obj_observations = obj2(grid)
	third_obj_observations = obj3(grid)
	fourth_obj_observations = obj4(grid)
	fifth_obj_observations = obj5(grid)
	first_con_observations = c1(grid)
	second_con_observations = c2(grid)
	third_con_observations = c3(grid)
	fourth_con_observations = c4(grid)
	fifth_con_observations = c5(grid)
	sixth_con_observations = c6(grid)
	seventh_con_observations = c7(grid)
	max_first_obj = np.max(first_obj_observations)
	min_first_obj = np.min(first_obj_observations)
	max_second_obj = np.max(second_obj_observations)
        min_second_obj = np.min(second_obj_observations)
        max_third_obj = np.max(third_obj_observations)
        min_third_obj = np.min(third_obj_observations)
	max_fourth_obj = np.max(fourth_obj_observations)
        min_fourth_obj = np.min(fourth_obj_observations)
	max_fifth_obj = np.max(fifth_obj_observations)
        min_fifth_obj = np.min(fifth_obj_observations)
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
	max_seventh_con = np.max(seventh_con_observations)
        min_seventh_con = np.min(seventh_con_observations)
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
	print("Maximum observation of the third objective")
        print(max_third_obj)
        print("Minimum observation of the third objective")
        print(min_third_obj)
	print("Noise factor")
	print((max_third_obj-min_third_obj)*noise)
	print("Maximum observation of the fourth objective")
        print(max_fourth_obj)
        print("Minimum observation of the fourth objective")
        print(min_fourth_obj)
	print("Noise factor")
	print((max_fourth_obj-min_fourth_obj)*noise)
	print("Maximum observation of the fifth objective")
        print(max_fifth_obj)
        print("Minimum observation of the fifth objective")
        print(min_fifth_obj)
	print("Noise factor")
	print((max_fifth_obj-min_fifth_obj)*noise)
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
	print("Maximum observation of the seventh constraint")
        print(max_seventh_con)
        print("Minimum observation of the seventh constraint")
        print(min_seventh_con)
	print("Noise factor")
	print((max_seventh_con-min_seventh_con)*noise)

def main(job_id, params):
    try:
        return evaluate(job_id, params)
    except Exception as ex:
        print ex
        print 'An error occurred in mocotoy_con.py'
        return np.nan

if __name__ == "__main__":
	#main(0, {u'X': np.array([ 5.0 ]), u'Y': np.array([ 2.8 ]), u'Z': np.array([ 1.0 ]) })
	get_functions_borders()
