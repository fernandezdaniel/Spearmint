import numpy as np

NUM_EXP = 1

def evaluate(job_id, params):

    np.random.seed(NUM_EXP)

    x = params['X']
    y = params['Y']
    z = params['Z']
    a = params['A']

    #print 'Evaluating at (%f, %f, %f, %f)' % (x, y, z, a)

    obj1 = float(1.10471 * np.power(x,2.0) * z + 0.04811 * a * y * (14.0+z))
    obj2 = float(2.1952 / float((np.power(a,3.0)*y)))

    c1 = (float(13600.0-np.power(np.power(6000.0/(np.power(2,0.5)*x*z),2.0)+ np.power( (6000.0*(14.0+0.5*z)*np.power(0.25*(np.power(z,2.0)+np.power(x+a,2.0)),0.5)/(2*np.power(2.0,0.5)*x*z*(np.power(z,2.0)/(12.0)+0.25*np.power(x+a,2.0)))) ,2.0) + z * 6000.0/(np.power(2,0.5)*x*z) * ((6000.0*(14.0+0.5*z)*np.power(0.25*(np.power(z,2.0)+np.power(x+a,2.0)),0.5)/(2*np.power(2.0,0.5)*x*z*(np.power(z,2.0)/(12.0)+0.25*np.power(x+a,2.0))))) / (np.power(0.25*(np.power(z,2.0)+np.power(x+a,2.0)),0.5)),0.5)))/75842.5359709

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

def main(job_id, params):
    try:
        return evaluate(job_id, params)
    except Exception as ex:
        print ex
        print 'An error occurred in mocotoy_con.py'
        return np.nan

if __name__ == "__main__":
	main(0, {u'X': np.array([ 5.0 ]), u'Y': np.array([ 2.8 ]), u'Z': np.array([ 5.0 ]), u'A': np.array([ 2.8 ])})
