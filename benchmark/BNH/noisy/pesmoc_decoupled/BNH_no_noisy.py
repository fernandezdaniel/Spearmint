import numpy as np

def evaluate(job_id, params):

    x = params['X']
    y = params['Y']

    #print 'Evaluating at (%f, %f)' % (x, y)

    obj1 = float(4.0*np.power(x,2.0)+4.0*np.power(y,2.0))
    obj2 = float(np.power(x-5.0,2.0)+np.power(y-5.0,2.0))

    c1 = ( 25.0-np.power(x-5.0,2.0)-np.power(y,2.0) ) / 7.92604994102
    c2 = ( np.power(x-8.0,2.0)+np.power(y+3.0,2.0)-7.7 ) / 17.8066390633

    return {
        "o1"       : obj1, 
        "o2"       : obj2, 
        "c1"	   : c1,
	"c2"       : c2
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
