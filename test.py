import sqlite3

veritabanı=sqlite3.connect("vt.db")
imlec =veritabanı.cursor()
def connect_db():
    veritabanı=sqlite3.connect("vt.db")
    imlec =veritabanı.cursor()
    table_create="CREATE TABLE IF NOT EXISTS personel (isim TEXT, soisim TEXT, departman TEXT, maas INT)"
    imlec.execute(table_create)
    veritabanı.commit()
def insert_db():
    imlec.execute("INSERT INTO personel VALUES('SABRİ', 'elmastas', 'Bilgi Güvenligi', 30000)")
    imlec.execute("INSERT INTO personel VALUES('Mehmet', 'elmastas', 'Yazlımı', 30000)")
    veritabanı.commit()
def get_data():
    print(" Personel Listesi -----------------------------------")
    imlec.execute("SELECT*FROM personel")
    liste=imlec.fetchall()
    for i in liste:
        print(i)
def update_data():
    print(" Personel Listesi Update Etme -----------------------------------")   
    imlec.execute("UPDATE personel SET departman=? WHERE departman=?",("muhasebe", "sağlık"))
    veritabanı.commit() 
def delete_data():
    print(" Personel Listesinde Deelete -----------------------------------")   
    imlec.execute("DELETE personel SET departman=? WHERE departman=?",("muhasebe", "sağlık"))
    veritabanı.commit()
def personel_data():
    imlec.execute("SELECT isim,soisim FROM personel")
    liste=imlec.fetchall()
    for i in liste:
        print(i)
def WHERE_Clause():
    imlec.execute("SELECT*FROM personel WHERE departman ='muhasebe'")
    liste=imlec.fetchall()
    for i in liste:
        print(i)  
def LIMIT_Clause(): 
    imlec.execute("SELECT*FROM personel LIMIT 3")
    liste=imlec.fetchall()
    for i in liste:
        print(i)  
def Comparison(): 
    imlec.execute("SELECT*FROM personel WHERE maas > 30000")
    liste=imlec.fetchall()
    for i in liste:
        print(i)  
    print("-----------------------------------")
    imlec.execute("SELECT*FROM personel WHERE departman != 'sağlık'")
    liste=imlec.fetchall()
    for i in liste:
        print(i) 
def Arithmetic(): 
    imlec.execute("SELECT maas/2 AS yeni_maas FROM personel")
    liste=imlec.fetchall()
    for i in liste:
        print(i)  
def sql_logical_like():
    imlec.execute("SELECT * FROM personel WHERE soisim LIKE 'sab%'")
    liste=imlec.fetchall()
    for i in liste:
        print(i)
def sql_logical_in():
    imlec.execute("SELECT * FROM personel WHERE soisim IN ('Elmastas')")
    liste=imlec.fetchall()
    for i in liste:
        print(i)
def sql_logical_Between():
    imlec.execute("SELECT * FROM personel WHERE maas BETWEEN 10000  AND 40000")
    liste=imlec.fetchall()
    for i in liste:
        print(i) 
def sql_logical_AND():
    imlec.execute("SELECT * FROM personel WHERE maas=20000 AND maas<= 40000")
    liste=imlec.fetchall()
    for i in liste:
        print(i)  
def sql_logical_OR():
    imlec.execute("SELECT * FROM personel WHERE maas=20000 OR isim='almila'")
    liste=imlec.fetchall()
    for i in liste:
        print(i)  
def sql_logical_NOT():
    imlec.execute("SELECT * FROM personel WHERE NOT isim='nazar'")
    liste=imlec.fetchall()
    for i in liste:
        print(i) 
def sql_logical_ORDER_BY():
    imlec.execute("SELECT * FROM personel  ORDER BY  isim")
    liste=imlec.fetchall()
    for i in liste:
        print(i) 
def sql_logical_COUNT():
    imlec.execute("SELECT COUNT(*)  FROM personel maas")
    liste=imlec.fetchall()
    for i in liste:
        print(i) 
def sql_logical_SUM():
    imlec.execute("SELECT SUM(maas)  FROM personel WHERE maas")
    liste=imlec.fetchall()
    for i in liste:
        print(i) 
def sql_logical_MIN():
    imlec.execute("SELECT MIN(maas)  FROM personel WHERE maas")
    liste=imlec.fetchall()
    for i in liste:
        print(i) 
def sql_logical_MAX():
    imlec.execute("SELECT MAX(maas)  FROM personel WHERE maas")
    liste=imlec.fetchall()
    for i in liste:
        print(i) 
def sql_logical_AVG():
    imlec.execute("SELECT AVG(maas)  FROM personel WHERE maas")
    liste=imlec.fetchall()
    for i in liste:
        print(i) 
def sql_DISTINCT():
    imlec.execute("SELECT DISTINCT isim  FROM personel")
    liste=imlec.fetchall()
    for i in liste:
        print(i) 
def sql_INNER_JOIN():
    imlec.execute("SELECT * FROM personel INNER JOIN IT ON personel.isim = IT.isim")
    liste=imlec.fetchall()
    for i in liste:
        print(i)       
def sql_LEFT_JOIN():
    imlec.execute("SELECT * FROM personel LEFT JOIN IT ON personel.isim = IT.isim")
    liste=imlec.fetchall()
    for i in liste:
        print(i)              
#insert_db()
get_data()
personel_data()
WHERE_Clause()
LIMIT_Clause()
Comparison()
Arithmetic()
update_data()
sql_logical_like()
sql_logical_in()
sql_logical_Between()
sql_logical_AND()
sql_logical_OR()
sql_logical_NOT()
sql_logical_ORDER_BY()
sql_logical_COUNT()
sql_logical_SUM()
sql_logical_MIN()
sql_logical_MAX()
sql_logical_AVG()
sql_DISTINCT()
sql_INNER_JOIN()
sql_LEFT_JOIN()
veritabanı.close()
    
    
    
    
    
    
    
    
    
    

