import numpy as np

def evaluate(job_id, params):

    x = params['X']
    y = params['Y']

    #print 'Evaluating at (%f, %f)' % (x, y)

    obj1 = float(2.0+np.power(x-2.0,2.0)+np.power(y-2.0,2.0))
    obj2 = float(9.0*x-np.power(y-1.0,2.0))


    c1  = float(225.0-np.power(x,2.0)-np.power(y,2.0))/168.823484412
    c2 = float(3.0*y-x-10.0)/36.5330991522

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
