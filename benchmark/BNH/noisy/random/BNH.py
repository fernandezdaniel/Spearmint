import numpy as np

NUM_EXP = 1

def evaluate(job_id, params):

    np.random.seed(NUM_EXP)
    x = params['X']
    y = params['Y']

    print 'Evaluating at (%f, %f)' % (x, y)

    obj1 = float(4.0*np.power(x,2.0)+4.0*np.power(y,2.0)) + np.random.normal(0,1.3)
    obj2 = float(np.power(x-5.0,2.0)+np.power(y-5.0,2.0)) + np.random.normal(0,0.45)

    c1 = ( 25.0-np.power(x-5.0,2.0)-np.power(y,2.0) + np.random.normal(0,0.05) ) / 7.92604994102
    c2 = ( np.power(x-8.0,2.0)+np.power(y+3.0,2.0)-7.7  + np.random.normal(0,0.04) ) / 17.8066390633

    return {
        "o1"       : obj1, 
        "o2"       : obj2, 
        "c1"	   : c1,
	"c2"       : c2
    }

def test_grid():
    x = np.linspace( 0.0,5.0,2000 )
    y = np.linspace( 0.0,3.0,2000 )
    x,y = np.meshgrid( x,y )

    c1 = 25.0-np.power(x-5.0,2.0)-np.power(y,2.0)
    c2 = np.power(x-8.0,2.0)+np.power(y+3.0,2.0)-7.7

    var1 = np.var(c1)
    var2 = np.var(c2)
    print np.sqrt(var1)
    print np.sqrt(var2)


def main(job_id, params):
    try:
        return evaluate(job_id, params)
    except Exception as ex:
        print ex
        print 'An error occurred in mocotoy_con.py'
        return np.nan

if __name__ == "__main__":
	main(0, {u'X': np.array([ 5.0 ]), u'Y': np.array([ 2.8 ])})
