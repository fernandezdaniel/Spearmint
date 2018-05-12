import numpy as np

def evaluate(job_id, params):

    x = params['X']
    y = params['Y']

    print 'Evaluating at (%f, %f)' % (x, y)

    obj1 = float(x)
    obj2 = float((1.0+y)/x)

    c1 = float(y+9.0*x-6.0) / 2.74925225179
    c2 = float(-y+9.0*x-1.0) / 2.74925225179

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
