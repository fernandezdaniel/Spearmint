import numpy as np

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

    c1 = float(x+y-2.0)/4.24918292799
    c2 = float(6.0-x-y)/4.24918292799
    c3 = float(2.0-y+x)/4.24918292799
    c4 = float(2.0-x+3.0*y)/9.50146187583
    c5 = float(4.0-np.power(z-3.0,2.0)-a)/2.21610268515
    c6 = float(np.power(b-3.0,2.0)+c-4.0)/3.26938662273

    return {
        "o1"       : obj1, 
        "o2"       : obj2, 
        "c1"	   : c1,
        "c2"	   : c2,
        "c3"	   : c3,
        "c4"	   : c4,
        "c5"	   : c5,
        "c6"	   : c6
    }

def main(job_id, params):
    try:
        return evaluate(job_id, params)
    except Exception as ex:
        print ex
        print 'An error occurred in mocotoy_con.py'
        return np.nan

if __name__ == "__main__":
	main(0, {u'X': np.array([ 5.0 ]), u'Y': np.array([ 2.8 ]), u'Z': np.array([ 2.8 ]), u'A': np.array([ 2.8 ]), u'B': np.array([ 2.8 ]), u'C': np.array([ 2.8 ])})
