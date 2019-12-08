from app.models import Training,Pasien
from _operator import itemgetter
# from app import db
# from app.models.diagnosa import Diagnosa

def getAtribut(kriteria):
    jk1c1 = getJumlahKriteria(kriteria,1,1)
    jk1c2 = getJumlahKriteria(kriteria,1,2)
    jk1c3 = getJumlahKriteria(kriteria,1,3)
    jk1c4 = getJumlahKriteria(kriteria,1,4)
    jk2c1 = getJumlahKriteria(kriteria,2,1)
    jk2c2 = getJumlahKriteria(kriteria,2,2)
    jk2c3 = getJumlahKriteria(kriteria,2,3)
    jk2c4 = getJumlahKriteria(kriteria,2,4)
    jk3c1 = getJumlahKriteria(kriteria,3,1)
    jk3c2 = getJumlahKriteria(kriteria,3,2)
    jk3c3 = getJumlahKriteria(kriteria,3,3)
    jk3c4 = getJumlahKriteria(kriteria,3,4)
    jk4c1 = getJumlahKriteria(kriteria,4,1)
    jk4c2 = getJumlahKriteria(kriteria,4,2)
    jk4c3 = getJumlahKriteria(kriteria,4,3)
    jk4c4 = getJumlahKriteria(kriteria,4,4)
    k1c1 = getJumlahKriteria(kriteria,1,1)/getJumlahC(1)
    k1c2 = getJumlahKriteria(kriteria,1,2)/getJumlahC(2)
    k1c3 = getJumlahKriteria(kriteria,1,3)/getJumlahC(3)
    k1c4 = getJumlahKriteria(kriteria,1,4)/getJumlahC(4)
    k2c1 = getJumlahKriteria(kriteria,2,1)/getJumlahC(1)
    k2c2 = getJumlahKriteria(kriteria,2,2)/getJumlahC(2)
    k2c3 = getJumlahKriteria(kriteria,2,3)/getJumlahC(3)
    k2c4 = getJumlahKriteria(kriteria,2,4)/getJumlahC(4)
    k3c1 = getJumlahKriteria(kriteria,3,1)/getJumlahC(1)
    k3c2 = getJumlahKriteria(kriteria,3,2)/getJumlahC(2)
    k3c3 = getJumlahKriteria(kriteria,3,3)/getJumlahC(3)
    k3c4 = getJumlahKriteria(kriteria,3,4)/getJumlahC(4)
    k4c1 = getJumlahKriteria(kriteria,4,1)/getJumlahC(1)
    k4c2 = getJumlahKriteria(kriteria,4,2)/getJumlahC(2)
    k4c3 = getJumlahKriteria(kriteria,4,3)/getJumlahC(3)
    k4c4 = getJumlahKriteria(kriteria,4,4)/getJumlahC(4)
    result = ((jk1c1,jk1c2,jk1c3,jk1c4,k1c1,k1c2,k1c3,k1c4),(jk2c1,jk2c2,jk2c3,jk2c4,k2c1,k2c2,k2c3,k2c4),(jk3c1,jk3c2,jk3c3,jk3c4,k3c1,k3c2,k3c3,k3c4),(jk4c1,jk4c2,jk4c3,jk4c4,k4c1,k4c2,k4c3,k4c4))
    return result

def getC():
    SumPCi = getJumlahC(1)+getJumlahC(2)+getJumlahC(3)+getJumlahC(4)
    jc1 = getJumlahC(1)
    jc2 = getJumlahC(2)
    jc3 = getJumlahC(3)
    jc4 = getJumlahC(4)
    c1 = getJumlahC(1)/SumPCi
    c2 = getJumlahC(2)/SumPCi
    c3 = getJumlahC(3)/SumPCi
    c4 = getJumlahC(4)/SumPCi
    result = ((jc1,c1),(jc2,c2),(jc3,c3),(jc4,c4))
    return result

def likehood(id_pasien):
    data = getDataTraining()
    pasien = Pasien.query.filter_by(id=id_pasien).first()

    # P(Ci)
    SumPCi = getJumlahC(1)+getJumlahC(2)+getJumlahC(3)+getJumlahC(4)
    PC1 = getJumlahC(1)/SumPCi
    PC2 = getJumlahC(2)/SumPCi
    PC3 = getJumlahC(3)/SumPCi
    PC4 = getJumlahC(4)/SumPCi

    # P(Merasa gelisah, cemas atau amat tegang|Ci)
    P1C1 = getJumlahKriteria('k1',pasien.k1,1)/getJumlahC(1)
    P1C2 = getJumlahKriteria('k1',pasien.k1,2)/getJumlahC(2)
    P1C3 = getJumlahKriteria('k1',pasien.k1,3)/getJumlahC(3)
    P1C4 = getJumlahKriteria('k1',pasien.k1,4)/getJumlahC(4)

    # P(Tidak mampu menghentikan atau mengendalikan rasa khawatir|Ci)
    P2C1 = getJumlahKriteria('k2',pasien.k2,1)/getJumlahC(1)
    P2C2 = getJumlahKriteria('k2',pasien.k2,2)/getJumlahC(2)
    P2C3 = getJumlahKriteria('k2',pasien.k2,3)/getJumlahC(3)
    P2C4 = getJumlahKriteria('k2',pasien.k2,4)/getJumlahC(4)

    # P(Terlalu mengkhawatirkan berbagai hal|Ci)
    P3C1 = getJumlahKriteria('k3',pasien.k3,1)/getJumlahC(1)
    P3C2 = getJumlahKriteria('k3',pasien.k3,2)/getJumlahC(2)
    P3C3 = getJumlahKriteria('k3',pasien.k3,3)/getJumlahC(3)
    P3C4 = getJumlahKriteria('k3',pasien.k3,4)/getJumlahC(4)

    # P(Sulit untuk santai |Ci)
    P4C1 = getJumlahKriteria('k4',pasien.k4,1)/getJumlahC(1)
    P4C2 = getJumlahKriteria('k4',pasien.k4,2)/getJumlahC(2)
    P4C3 = getJumlahKriteria('k4',pasien.k4,3)/getJumlahC(3)
    P4C4 = getJumlahKriteria('k4',pasien.k4,4)/getJumlahC(4)
    
    # P(Sangat gelisah sehingga sulit untuk duduk diam |Ci)
    P5C1 = getJumlahKriteria('k5',pasien.k5,1)/getJumlahC(1)
    P5C2 = getJumlahKriteria('k5',pasien.k5,2)/getJumlahC(2)
    P5C3 = getJumlahKriteria('k5',pasien.k5,3)/getJumlahC(3)
    P5C4 = getJumlahKriteria('k5',pasien.k5,4)/getJumlahC(4)

    # P(Menjadi mudah jengkel atau lekas marah |Ci)
    P6C1 = getJumlahKriteria('k6',pasien.k6,1)/getJumlahC(1)
    P6C2 = getJumlahKriteria('k6',pasien.k6,2)/getJumlahC(2)
    P6C3 = getJumlahKriteria('k6',pasien.k6,3)/getJumlahC(3)
    P6C4 = getJumlahKriteria('k6',pasien.k6,4)/getJumlahC(4)

    # P(Merasa takut seolah-olah sesuatu yang mengerikan/buruk mungkin terjadi |Ci)
    P7C1 = getJumlahKriteria('k7',pasien.k7,1)/getJumlahC(1)
    P7C2 = getJumlahKriteria('k7',pasien.k7,2)/getJumlahC(2)
    P7C3 = getJumlahKriteria('k7',pasien.k7,3)/getJumlahC(3)
    P7C4 = getJumlahKriteria('k7',pasien.k7,4)/getJumlahC(4)

    # P(X|Ci)*P(Ci)
    C1 = PC1*(P1C1*P2C1*P3C1*P4C1*P5C1*P6C1*P7C1)
    C2 = PC2*(P1C2*P2C2*P3C2*P4C2*P5C2*P6C2*P7C2)
    C3 = PC3*(P1C3*P2C3*P3C3*P4C3*P5C3*P6C3*P7C3)
    C4 = PC4*(P1C4*P2C4*P3C4*P4C4*P5C4*P6C4*P7C4)

    # Probabilitas akhir
    SumC = C1+C2+C3+C4
    PCA1 = C1/SumC
    PCA2 = C2/SumC
    PCA3 = C3/SumC
    PCA4 = C4/SumC

    result = ((P1C1,P2C1,P3C1,P4C1,P5C1,P6C1,P7C1,PC1,C1),(P1C2,P2C2,P3C2,P4C2,P5C2,P6C2,P7C2,PC2,C2),(P1C3,P2C3,P3C3,P4C3,P5C3,P6C3,P7C3,PC3,C3),(P1C4,P2C4,P3C4,P4C4,P5C4,P6C4,P7C4,PC4,C4),(PCA1,PCA2,PCA3,PCA4))
    return result


# function bayes
def bayes(id_pasien):
    pasien = Pasien.query.filter_by(id=id_pasien).first()

    # P(Ci)
    SumPCi = getJumlahC(1)+getJumlahC(2)+getJumlahC(3)+getJumlahC(4)
    PCisedikit = getJumlahC(1)/SumPCi
    PCiringan = getJumlahC(2)/SumPCi
    PCisedang = getJumlahC(3)/SumPCi
    PCiparah = getJumlahC(4)/SumPCi

    # P(Merasa gelisah, cemas atau amat tegang|Ci)
    P1C1 = getJumlahKriteria('k1',pasien.k1,1)/getJumlahC(1)
    P1C2 = getJumlahKriteria('k1',pasien.k1,2)/getJumlahC(2)
    P1C3 = getJumlahKriteria('k1',pasien.k1,3)/getJumlahC(3)
    P1C4 = getJumlahKriteria('k1',pasien.k1,4)/getJumlahC(4)

    # P(Tidak mampu menghentikan atau mengendalikan rasa khawatir|Ci)
    P2C1 = getJumlahKriteria('k2',pasien.k2,1)/getJumlahC(1)
    P2C2 = getJumlahKriteria('k2',pasien.k2,2)/getJumlahC(2)
    P2C3 = getJumlahKriteria('k2',pasien.k2,3)/getJumlahC(3)
    P2C4 = getJumlahKriteria('k2',pasien.k2,4)/getJumlahC(4)

    # P(Terlalu mengkhawatirkan berbagai hal|Ci)
    P3C1 = getJumlahKriteria('k3',pasien.k3,1)/getJumlahC(1)
    P3C2 = getJumlahKriteria('k3',pasien.k3,2)/getJumlahC(2)
    P3C3 = getJumlahKriteria('k3',pasien.k3,3)/getJumlahC(3)
    P3C4 = getJumlahKriteria('k3',pasien.k3,4)/getJumlahC(4)

    # P(Sulit untuk santai |Ci)
    P4C1 = getJumlahKriteria('k4',pasien.k4,1)/getJumlahC(1)
    P4C2 = getJumlahKriteria('k4',pasien.k4,2)/getJumlahC(2)
    P4C3 = getJumlahKriteria('k4',pasien.k4,3)/getJumlahC(3)
    P4C4 = getJumlahKriteria('k4',pasien.k4,4)/getJumlahC(4)
    
    # P(Sangat gelisah sehingga sulit untuk duduk diam |Ci)
    P5C1 = getJumlahKriteria('k5',pasien.k5,1)/getJumlahC(1)
    P5C2 = getJumlahKriteria('k5',pasien.k5,2)/getJumlahC(2)
    P5C3 = getJumlahKriteria('k5',pasien.k5,3)/getJumlahC(3)
    P5C4 = getJumlahKriteria('k5',pasien.k5,4)/getJumlahC(4)

    # P(Menjadi mudah jengkel atau lekas marah |Ci)
    P6C1 = getJumlahKriteria('k6',pasien.k6,1)/getJumlahC(1)
    P6C2 = getJumlahKriteria('k6',pasien.k6,2)/getJumlahC(2)
    P6C3 = getJumlahKriteria('k6',pasien.k6,3)/getJumlahC(3)
    P6C4 = getJumlahKriteria('k6',pasien.k6,4)/getJumlahC(4)

    # P(Merasa takut seolah-olah sesuatu yang mengerikan/buruk mungkin terjadi |Ci)
    P7C1 = getJumlahKriteria('k7',pasien.k7,1)/getJumlahC(1)
    P7C2 = getJumlahKriteria('k7',pasien.k7,2)/getJumlahC(2)
    P7C3 = getJumlahKriteria('k7',pasien.k7,3)/getJumlahC(3)
    P7C4 = getJumlahKriteria('k7',pasien.k7,4)/getJumlahC(4)

    # P(X|Ci)*P(Ci)
    C1 = PCisedikit*(P1C1*P2C1*P3C1*P4C1*P5C1*P6C1*P7C1)
    C2 = PCiringan*(P1C2*P2C2*P3C2*P4C2*P5C2*P6C2*P7C2)
    C3 = PCisedang*(P1C3*P2C3*P3C3*P4C3*P5C3*P6C3*P7C3)
    C4 = PCiparah*(P1C4*P2C4*P3C4*P4C4*P5C4*P6C4*P7C4)

    # Probabilitas akhir
    SumC = C1+C2+C3+C4
    PC1 = C1/SumC
    PC2 = C2/SumC
    PC3 = C3/SumC
    PC4 = C4/SumC

    # tuple
    tup = (("Sedikit atau tidak ada",PC1),("Ringan",PC2),("Sedang",PC3),("Parah",PC4))

    # sort
    # sorted(student_tuples, key=itemgetter(2), reverse=True)
    stup = sorted(tup, key=itemgetter(1),reverse=True)

    # tingkat kecemasan
    tk = stup[0][0]
    result = (pasien.user,tk,(tup))

    return result

def getDataTraining():
    return Training.query.all()

def getJumlahData():
    return Training.query.count()

def getJumlahKriteria(kriteria,y,z):
    if(kriteria=='k1'):
        return Training.query.filter_by(k1=y).filter_by(c=z).count()
    if(kriteria=='k2'):
        return Training.query.filter_by(k2=y).filter_by(c=z).count()
    if(kriteria=='k3'):
        return Training.query.filter_by(k3=y).filter_by(c=z).count()
    if(kriteria=='k4'):
        return Training.query.filter_by(k4=y).filter_by(c=z).count()
    if(kriteria=='k5'):
        return Training.query.filter_by(k5=y).filter_by(c=z).count()
    if(kriteria=='k6'):
        return Training.query.filter_by(k6=y).filter_by(c=z).count()
    if(kriteria=='k7'):
        return Training.query.filter_by(k7=y).filter_by(c=z).count()

def getJumlahC(z):
    return Training.query.filter_by(c=z).count()

