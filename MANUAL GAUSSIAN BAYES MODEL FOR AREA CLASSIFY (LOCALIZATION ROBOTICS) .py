import numpy


x=[[1,1],[1,1.5],[1,2],[1,2.5],[2,1],[2,2]]
y=[1,1,2,2,1,2]
pred_ar=[]
arr_x1_c1=[]
arr_x2_c1=[]
arr_x1_c2=[]
arr_x2_c2=[]

x1_c1_mean=0

x2_c1_mean=0
x1_c2_mean=0
x2_c2_mean=0

x1_c1_stdv=0
x2_c1_stdv=0
x1_c2_stdv=0
x2_c2_stdv=0

x1_c1_pdf=0
x2_c1_pdf=0
x1_c2_pdf=0
x2_c2_pdf=0

def gaussian_prob_den(mean,sd,x):

    pdf=1/numpy.sqrt(2*numpy.pi*sd)*numpy.e**-((x-mean)**2/2*sd**2)
    #
    return pdf

def probability_of_classes():
    prob_class1=y.count(1)/len(y)
    prob_class2 = y.count(2) / len(y)

    return [prob_class1,prob_class2]

def extract_x1_c1_and_x2_c1_():
    counter=0
    for data in x:
        if y[counter] == 1:
            arr_x1_c1.append(data[0])
            arr_x2_c1.append(data[1])

        counter=counter+1
    return 0


def extract_x1_c2_and_x2_c2_():
    counter=0
    for data in x:
        if y[counter] == 2:
            arr_x1_c2.append(data[0])
            arr_x2_c2.append(data[1])

        counter=counter+1
    return 0


def stdv_and_mean():
    global x1_c1_stdv,x1_c2_stdv,x2_c1_stdv,x2_c2_stdv
    global x1_c1_mean
    global x1_c2_mean
    global x2_c2_mean
    global x2_c1_mean

    x1_c1_stdv=numpy.std(arr_x1_c1)
    x1_c2_stdv=numpy.std(arr_x1_c2)
    x2_c1_stdv=numpy.std(arr_x2_c1)
    x2_c2_stdv=numpy.std(arr_x2_c2)

    x1_c1_mean=numpy.mean(arr_x1_c1)
    x1_c2_mean=numpy.mean(arr_x1_c2)
    x2_c2_mean=numpy.mean(arr_x2_c2)
    x2_c1_mean=numpy.array(arr_x2_c1)
    return 0



def pdf():
    global x1_c1_pdf
    x1_c1_pdf=gaussian_prob_den(mean=x1_c1_mean,sd=x1_c1_stdv,x=pred_ar[0][0])

    global x2_c1_pdf
    x2_c1_pdf = gaussian_prob_den(mean=x2_c1_mean, sd=x2_c1_stdv, x=pred_ar[0][1])

    global x1_c2_pdf
    x1_c2_pdf = gaussian_prob_den(mean=x1_c2_mean, sd=x1_c2_stdv, x=pred_ar[0][0])

    global x2_c2_pdf
    x2_c2_pdf = gaussian_prob_den(mean=x2_c2_mean, sd=x2_c2_stdv, x=pred_ar[0][1])

    return 0





def predict():
    class1_pred=x1_c1_pdf*x2_c1_pdf*.5
    class2_pred = x1_c2_pdf * x2_c2_pdf * .5

    return [numpy.max(class1_pred),class2_pred]





def main_func(x,y):
    pred_ar.clear()
    pred_ar.append([x,y])
    extract_x1_c1_and_x2_c1_()
    extract_x1_c2_and_x2_c2_()
    stdv_and_mean()
    pdf()
    print(choose_area_(predict()))
    return 0




def choose_area_(arr):
    if arr[0]>arr[1]:
        print("area 1")
    if arr[1] > arr[0]:
        print("area 2")
    return 0



if __name__=="__main__":
    _x=1
    _y=2
    main_func(x=_x,y=_y)

########################################
#infinity
#.
#.               Area2
#.
#2
#1.9#####################################
#1.8
#.
#.
#1.5
#.                  AREA1
#.
#1
##########################################