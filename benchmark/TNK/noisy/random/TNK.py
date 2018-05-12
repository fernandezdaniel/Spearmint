import numpy as np

NUM_EXP = 1

def evaluate(job_id, params):

    np.random.seed(NUM_EXP)

    x = params['X']
    y = params['Y']

    print 'Evaluating at (%f, %f)' % (x, y)

    obj1 = float(x) + np.random.normal(0,0.0003)
    obj2 = float(y) + np.random.normal(0,0.0003)

    c1 = (float(np.power(x,2.0)+np.power(y,2.0)-1.0-0.1*np.cos(16.0*np.arctan(x/float(y)))) + np.random.normal(0,0.048)) / 4.17
    c2 = (float(0.5-np.power(x-0.5,2.0)-np.power(y-0.5,2.0)) + np.random.normal(0,0.048)) / 2.94

    return {
        "o1"       : obj1, 
        "o2"       : obj2, 
        "c1"	   : c1,
        "c2"	   : c2
    }

def main(job_id, params):
    try:
        return evaluate(job_id, params)
    except Exception as ex:
        print ex
        print 'An error occurred in mocotoy_con.py'
        return np.nan

if __name__ == "__main__":
	main(0, {u'X': np.array([ 5.0 ]), u'Y': np.array([ 2.8 ])})
