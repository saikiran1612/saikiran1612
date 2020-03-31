import sys
import pandas as pd



def main():
        file_1=sys.argv[1]
        file_2=sys.argv[2]
        f1=file_1+".csv"
        f2=file_2+".csv"
        def luk(k):
            k +=1
            return mydict.get(k)

        def luk2(k):
            k +=1
            return mydict2.get(k)

        df1=pd.read_csv(f1)
        df1.sort_values(by=['article_id'], inplace=True)

        article_id1=df1["article_id"].tolist()
        cluster_id1=df1["cluster_id"].tolist()

        df2=pd.read_csv(f2)
        df2.sort_values(by=['article_id'], inplace=True)

        article_id2=df2["article_id"].tolist()
        cluster_id2=df2["cluster_id"].tolist()

        group1=df1.groupby('cluster_id')
        group2=df2.groupby('cluster_id')

        first_group1=group1.first()
        first_group2=group2.first()


        first_element_of_cluster=first_group1["article_id"].tolist()
        first_element_of_cluster2=first_group2["article_id"].tolist()

        def dft(df):
            return df.groupby('cluster_id', group_keys=False).apply(lambda x: x[1:])
        df1_1=dft(df1)
        mydict=df1_1.groupby('cluster_id')['article_id'].apply(list).to_dict()
        df2_2=dft(df2)
        mydict2=df2_2.groupby('cluster_id')['article_id'].apply(list).to_dict()


                                    #for ground_truth data
        org_dict={}
        i=0
        while (i<len(first_element_of_cluster)):
            x=luk(i)
            h={first_element_of_cluster[i]:x}
            org_dict.update(h)
            i +=1


                                             #for algo O/p data
        org_dict2={}
        i=0
        while (i<len(first_element_of_cluster2)):
            x=luk2(i)
            h={first_element_of_cluster2[i]:x}
            org_dict2.update(h)
            i +=1



                                                    #counting
        total_articleids=len(article_id1)
        count1=0 #non_duplicates as non_duplicates
        count2=0 #non_duplicates as duplicates
        count3=0  #duplicates as originals
        count4=0  #duplicates as duplicates

        for key in org_dict:
            if key in org_dict2:
                count1 +=1
            else:count2 +=1

        for key in org_dict2:
            if key not in org_dict:
                count3 += 1

        count4=total_articleids-count1-count2-count3

        print("non_duplicates as non_duplicates:", count1)
        print("non_duplicates as duplicates:", count2)
        print("duplicates as non_duplicates:", count3)
        print("duplicates as duplicates:", count4)

if __name__=="__main__":
    main()






