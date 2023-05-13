from django.shortcuts import render
import pickle
import pandas as pd
import numpy as np
# Create your views here.
bookname=pickle.load(open("book_name.pkl","rb"))
model1=pickle.load(open('model.pkl','rb'))
#finalrating=pickle.load(open('final_rating.pkl','rb'))
#bookpivot=pickle.load(open('book_pivot.pkl','rb'))

finalrating=pd.read_pickle('final_rating.pkl')
bookpivot=pd.read_pickle('book_pivot.pkl')


def book(request):
    bk=[]
    img1=[]
    book_id=np.where(bookpivot.index=='Exclusive')[0][0]
    distance,suggetion=model1.kneighbors(bookpivot.iloc[book_id,:].values.reshape(1,-1),n_neighbors=5)
    print(suggetion)
    if request.method=='POST':
        bk.clear()
        img1.clear()
        name1=request.POST.get('book')
        book_id=np.where(bookpivot.index==name1)[0][0]
        distance,suggetion=model1.kneighbors(bookpivot.iloc[book_id,:].values.reshape(1,-1),n_neighbors=5)
        print("user:",suggetion)
    
    
    for i in range(len(suggetion)):
        books=bookpivot.index[suggetion[i]]
        for j in books:
            bk.append(j)
            idm=finalrating[finalrating['title']==j]['image_url']
            img=pd.DataFrame(idm)
            url=img.iloc[0,:1][0]
            img1.append(url)
            print(url)
    context={
        'bookname':bookname,
        
        'img0':img1[0],
        'img1':img1[1],
        'img2':img1[2],
        'img3':img1[3],
        'img4':img1[4],
        'bk0':bk[0],'bk1':bk[1],'bk2':bk[2],'bk3':bk[3],'bk4':bk[4]
        }
    bk=[]
    img1=[]
    return render(request,'app/index.html',context)