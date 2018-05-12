import numpy as np

def evaluate(job_id, params):

    x = params['X']
    y = params['Y']
    z = params['Z']

    print 'Evaluating at (%f, %f, %f)' % (x, y, z)

    obj1 = float(x*np.power(16.0+np.power(z,2.0),0.5)+y*np.power(1.0+np.power(z,2.0),0.5))
    obj2 = float(np.max((20.0*np.power(16.0+np.power(z,2.0)/0.5)/(x*z),80.0*np.power(1.0+np.power(z,2.0),0.5)/(y*z))))

    c1 = (float(np.power(10.0,5.0)-np.max((20.0*np.power(16.0+np.power(z,2.0)/0.5)/(x*z),80.0*np.power(1.0+np.power(z,2.0),0.5)/(y*z)))))/103324.527134

    return {
        "o1"       : obj1, 
        "o2"       : obj2, 
        "c1"	   : c1
    }

def main(job_id, params):
    try:
        return evaluate(job_id, params)
    except Exception as ex:
        print ex
        print 'An error occurred in mocotoy_con.py'
        return np.nan

if __name__ == "__main__":
	main(0, {u'X': np.array([ 5.0 ]), u'Y': np.array([ 2.8 ]), u'Z': np.array([ 1.0]) })
