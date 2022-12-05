from matplotlib.widgets import Cursor
import numpy as np
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt
import array as array


# variable arange

mem_height = np.arange(0, 1001, 1)
mem_velocity = np.arange(-30, 31, 1)
mem_cforce = np.arange(-30, 31, 1)

# membership oluşturma
'''
height_zero = mf.trimf(mem_height, [-500, 0, 500]) # -500, 0, 500 orj
height_small = mf.trimf(mem_height, [-200, 300, 800]) #-200, 300, 800
height_medium = mf.trimf(mem_height, [300, 800, 1300]) # 300, 800, 1300
height_large = mf.trimf(mem_height, [500, 1000, 1500]) # 500, 1000, 1500 orj
'''

height_zero = mf.trimf(mem_height, [-500, 0, 500]) # -500, 0, 500 orj
height_small = mf.trimf(mem_height, [-300, 200, 700]) #-200, 300, 800
height_medium = mf.trimf(mem_height, [0, 500, 1000]) # 300, 800, 1300
height_large = mf.trimf(mem_height, [500, 1000, 1500]) # 500, 1000, 1500 orj



velocity_downlarge = mf.trapmf(mem_velocity, [-30,-30, -20, -10])
velocity_downsmall = mf.trimf(mem_velocity, [-20, -10, 0])
velocity_zero = mf.trimf(mem_velocity, [-10, 0, 10])
velocity_upsmall = mf.trimf(mem_velocity, [0, 10, 20])
velocity_uplarge = mf.trapmf(mem_velocity, [10, 20, 30, 30])

#'''
force_downlarge = mf.trapmf(mem_cforce, [-30,-30, -20, -10])
force_downsmall = mf.trimf(mem_cforce, [-20, -10, 0])
force_zero = mf.trimf(mem_cforce, [-10, 0, 10])
force_upsmall = mf.trimf(mem_cforce, [0, 10, 20])
force_uplarge = mf.trapmf(mem_cforce, [10, 20, 30, 30])
'''

force_down5 = mf.trimf(mem_cforce, [-30, -30, -24])
force_down4 = mf.trimf(mem_cforce, [-30, -24, -18])
force_down3 = mf.trimf(mem_cforce, [-24, -18, -12])
force_down2 = mf.trimf(mem_cforce, [-18, -12, -6])
force_down1 = mf.trimf(mem_cforce, [-12, -6, 0])
force_zero = mf.trimf(mem_cforce, [-6, 0, 6])
force_up1 = mf.trimf(mem_cforce, [0, 6, 12])
force_up2 = mf.trimf(mem_cforce, [6, 12, 18])
force_up3 = mf.trimf(mem_cforce, [12, 18, 24])
force_up4 = mf.trimf(mem_cforce, [18, 24, 30])
force_up5 = mf.trimf(mem_cforce, [24, 30, 30])
'''
# membership çizdirme matplotlib ile
#'''
fig, (ax0, ax1, ax2) = plt.subplots(nrows = 3, figsize =(6, 10))

ax0.plot(mem_height, height_zero, 'r', linewidth = 2, label = 'zero')
ax0.plot(mem_height, height_small, 'g', linewidth = 2, label = 'small')
ax0.plot(mem_height, height_medium, 'b', linewidth = 2, label = 'med')
ax0.plot(mem_height, height_large, 'y', linewidth = 2, label = 'large')
ax0.set_title('Height')
ax0.legend()

ax1.plot(mem_velocity, velocity_downlarge, 'r', linewidth = 2, label = 'downlarge')
ax1.plot(mem_velocity, velocity_downsmall, 'g', linewidth = 2, label = 'downsmall')
ax1.plot(mem_velocity, velocity_zero, 'b', linewidth = 2, label = 'zero')
ax1.plot(mem_velocity, velocity_upsmall, 'y', linewidth = 2, label = 'upsmall')
ax1.plot(mem_velocity, velocity_uplarge, 'r', linewidth = 2, label = 'uplarge')
ax1.set_title('Velocity')
ax1.legend()

ax2.plot(mem_cforce, force_downlarge, 'r', linewidth = 2, label = 'downlarge')
ax2.plot(mem_cforce, force_downsmall, 'g', linewidth = 2, label = 'downsmall')
ax2.plot(mem_cforce, force_zero, 'b', linewidth = 2, label = 'zero')
ax2.plot(mem_cforce, force_upsmall, 'y', linewidth = 2, label = 'upsmall')
ax2.plot(mem_cforce, force_uplarge, 'r', linewidth = 2, label = 'uplarge')
ax2.set_title('Control Force')
ax2.legend()

plt.tight_layout()
#'''
# ilk datamız değişkenlerimiz

input_height=1000
input_velocity=-20


#ucak visualization icin define
i=0
x=[0]
y=[1000]
z=0
v=[-20]

while True:

#### ucak visualization icin arraya ekleme yapılıyor her seferinde
    x.append(i)
    y.append(input_height)
    v.append(input_velocity)
    i=i+1

### membership derece hesaplama
    height_fit_zero = fuzz.interp_membership(mem_height, height_zero, input_height) #(arange,membership,input değeri)
    height_fit_small = fuzz.interp_membership(mem_height, height_small, input_height)
    height_fit_medium = fuzz.interp_membership(mem_height, height_medium, input_height)
    height_fit_large = fuzz.interp_membership(mem_height, height_large, input_height)


    print("hz",height_fit_zero)
    print("hs",height_fit_small)
    print("hm",height_fit_medium)
    print("hl",height_fit_large)


    velocity_fit_downlarge = fuzz.interp_membership(mem_velocity, velocity_downlarge, input_velocity)
    velocity_fit_downsmall = fuzz.interp_membership(mem_velocity, velocity_downsmall, input_velocity)
    velocity_fit_zero = fuzz.interp_membership(mem_velocity, velocity_zero, input_velocity)
    velocity_fit_upsmall = fuzz.interp_membership(mem_velocity, velocity_upsmall, input_velocity)
    velocity_fit_uplarge = fuzz.interp_membership(mem_velocity, velocity_uplarge, input_velocity)

    print("vdl",velocity_fit_downlarge)
    print("vds",velocity_fit_downsmall)
    print("vz",velocity_fit_zero)
    print("vus",velocity_fit_upsmall)
    print("vup",velocity_fit_uplarge)

    # KURAL MATRİSİ TABLOSU

    '''
    rule_matrix = np.array([
    [force_zero,force_downsmall,force_downlarge,force_downlarge,force_downlarge],
    [force_upsmall,force_zero,force_downsmall,force_downlarge,force_downlarge],
    [force_uplarge,force_upsmall,force_zero,force_downsmall,force_downlarge],
    [force_uplarge,force_uplarge,force_zero,force_downsmall,force_downsmall]])
    '''
    #'''
    rule_matrix = np.array([
    [force_zero,force_downsmall,force_downlarge,force_downlarge,force_downlarge],
    [force_upsmall,force_zero,force_downsmall,force_downlarge,force_downlarge],
    [force_upsmall,force_upsmall,force_zero,force_downsmall,force_downlarge],
    [force_uplarge,force_upsmall,force_zero,force_downsmall,force_downsmall]])
    #'''
    '''
    rule_matrix = np.array([
    [force_zero,force_down1,force_down3,force_down4,force_down5],
    [force_up2,force_zero,force_down3,force_down3,force_down4],
    [force_up3,force_up2,force_zero,force_down1,force_down4],
    [force_up4,force_up3,force_zero,force_down1,force_down3]])
    '''
    #KURAL TABLOSU AŞAĞIDAKİ GİBİDİR

    #           0    1   2   3    4
    #        V.DL V.DS  V.Z  V.US  V.UL
    #0 H.L
    #1 H.M
    #2 H.S
    #3 H.Z

    #force matrisinden doğru kuralı belirlemek, için için yanarım
    height_a=-1
    height_b=-1
    height_j=-1
    velo_c=-1
    velo_d=-1
    velo_k=-1

    
    my_tuple = (-2.0, -2.0,-2.0 ,-2.0,-2.0,-2.0) #boş define edemediğim için -2.0 verdim özel bir neden yok
    a,b,c,d,j,k=my_tuple

    #height_a ve benzerleri matristen kuralı çekmemiz için sütun ve satır numaralarını alıyorlar

    #abcdjk değişkenleri,  height_a ve benzerleri aynı if koşulunun içine girip daha sonra üstüne yazılmasın diye  ve daha sonra üyelik derecelerini yazdırmak için kaydediliyor
    
    if height_fit_zero>0.0 and height_a==-1:
        height_a=3
        a=height_fit_zero
    elif height_fit_small>0.0  and height_a==-1:
        height_a=2
        a=height_fit_small
    elif height_fit_medium>0.0  and height_a==-1:
        height_a=1
        a=height_fit_medium
    elif height_fit_large>0.0  and height_a==-1:
        height_a=0
        a=height_fit_large

    if height_fit_zero>0.0 and height_a!=-1 and a!=height_fit_zero:
        height_b=3
        b=height_fit_zero
    elif height_fit_small>0.0  and height_a!=-1 and a!=height_fit_small:
        height_b=2
        b=height_fit_small
    elif height_fit_medium>0.0  and height_a!=-1 and a!=height_fit_medium:
        height_b=1
        b=height_fit_medium
    elif height_fit_large>0.0  and height_a!=-1 and a!=height_fit_large:
        height_b=0
        b=height_fit_large
    else:
        b=a
        height_b=height_a

    if height_fit_zero>0.0 and height_a!=-1 and a!=height_fit_zero and height_b!=-1 and b!=height_fit_zero:
        height_j=3
        j=height_fit_zero
    elif height_fit_small>0.0  and height_a!=-1 and a!=height_fit_small and height_b!=-1 and b!=height_fit_small:
        height_j=2
        j=height_fit_small
    elif height_fit_medium>0.0  and height_a!=-1 and a!=height_fit_medium and height_b!=-1 and b!=height_fit_medium:
        height_j=1
        j=height_fit_medium
    elif height_fit_large>0.0  and height_a!=-1 and a!=height_fit_large and height_b!=-1 and b!=height_fit_large:
        height_j=0
        j=height_fit_large
    else:
        j=a
        height_j=height_b
        
    #########################

    if velocity_fit_downlarge>0.0 and velo_c==-1:
        velo_c=0
        c=velocity_fit_downlarge
    elif velocity_fit_downsmall>0.0 and velo_c==-1:
        velo_c=1
        c=velocity_fit_downsmall
    elif velocity_fit_zero>0.0 and velo_c==-1:
        velo_c=2
        c=velocity_fit_zero
    elif velocity_fit_upsmall>0.0 and velo_c==-1:
        velo_c=3
        c=velocity_fit_upsmall
    elif velocity_fit_uplarge>0.0 and velo_c==-1:
        velo_c=4
        c=velocity_fit_uplarge

    if velocity_fit_downlarge>0.0 and velo_c!=-1 and c!=velocity_fit_downlarge:
        velo_d=0
        d=velocity_fit_downlarge
    elif velocity_fit_downsmall>0.0 and velo_c!=-1 and c!=velocity_fit_downsmall:
        velo_d=1
        d=velocity_fit_downsmall
    elif velocity_fit_zero>0.0 and velo_c!=-1 and c!=velocity_fit_zero:
        velo_d=2
        d=velocity_fit_zero
    elif velocity_fit_upsmall>0.0 and velo_c!=-1 and c!=velocity_fit_upsmall:
        velo_d=3
        d=velocity_fit_upsmall
    elif velocity_fit_uplarge>0 and velo_c!=-1 and c!=velocity_fit_uplarge:
        velo_d=4
        d=velocity_fit_uplarge
    else:
        velo_d=velo_c
        d=c

    if velocity_fit_downlarge>0.0 and velo_c!=-1 and c!=velocity_fit_downlarge and velo_k!=-1 and k!=velocity_fit_downlarge:
        velo_k=0
        k=velocity_fit_downlarge
    elif velocity_fit_downsmall>0.0 and velo_c!=-1 and c!=velocity_fit_downsmall and velo_k!=-1 and k!=velocity_fit_downsmall:
        print('Girdu')
        velo_k=1
        k=velocity_fit_downsmall
    elif velocity_fit_zero>0.0 and velo_c!=-1 and c!=velocity_fit_zero and velo_k!=-1 and k!=velocity_fit_zero:
        velo_k=2
        k=velocity_fit_zero
    elif velocity_fit_upsmall>0.0 and velo_c!=-1 and c!=velocity_fit_upsmall and velo_k!=-1 and k!=velocity_fit_upsmall:
        velo_k=3
        k=velocity_fit_upsmall
    elif velocity_fit_uplarge>0 and velo_c!=-1 and c!=velocity_fit_uplarge and velo_k!=-1 and k!=velocity_fit_uplarge:
        velo_k=4
        k=velocity_fit_uplarge
    else:
        print('else girdu')
        velo_k=velo_c
        k=c
        #pass    


    #kurallar
    print("a: ",a)
    print("b: ",b)
    print("j" ,j)
    print("c:",c)
    print("d" ,d)
    print("k" ,k)
    print("height a satırı: " ,height_a)
    print("height b satırı: " ,height_b)
    print("height j satırı: " ,height_j)
    print("valo c sütunu: " ,velo_c)
    print("velo d sütunu: " ,velo_d)
    print("velo k sütunu: " ,velo_k)

    #abj cdk üyelik değerlerini almışlardı
    #height_a ve benzerleri de matristen kural çekmek için satır ve sutun sayısı almışlardı burada kullanıyoruz

    rule1=np.fmin(np.fmin(a,c),rule_matrix[height_a][velo_c])
    rule2=np.fmin(np.fmin(a,d),rule_matrix[height_a][velo_d])
    rule3=np.fmin(np.fmin(a,k),rule_matrix[height_a][velo_k])
    rule4=np.fmin(np.fmin(b,c),rule_matrix[height_b][velo_c])
    rule5=np.fmin(np.fmin(b,d),rule_matrix[height_b][velo_d])
    rule6=np.fmin(np.fmin(b,k),rule_matrix[height_b][velo_k])
    rule7=np.fmin(np.fmin(j,c),rule_matrix[height_j][velo_c])
    #print('j-d min:', np.fmin(j,d))
    rule8=np.fmin(np.fmin(j,d),rule_matrix[height_j][velo_d])
    rule9=np.fmin(np.fmin(j,k),rule_matrix[height_j][velo_k])





    #kural görselleştirme

    # cforce1 = np.zeros_like(mem_cforce)

    # fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows = 4, figsize =(6, 10))
    # ax1.fill_between(mem_cforce, cforce1, rule1, facecolor = 'r', alpha = 0.7)
    # ax1.plot(mem_cforce, rule1, 'r', linestyle = '--')
    # ax2.fill_between(mem_cforce, cforce1, rule2, facecolor = 'g', alpha = 0.7)
    # ax2.plot(mem_cforce, rule2, 'g', linestyle = '--')
    # ax3.fill_between(mem_cforce, cforce1, rule3, facecolor = 'y', alpha = 0.7)
    # ax4.plot(mem_cforce, rule3, 'y', linestyle = '--')
    # ax4.fill_between(mem_cforce, cforce1, rule4, facecolor = 'b', alpha = 0.7)
    # ax4.plot(mem_cforce, rule4, 'b', linestyle = '--')
    # ax1.set_title('rule1')
    # ax2.set_title('rule2')
    # ax3.set_title('rule3')
    # ax4.set_title('rule4')
    #plt.tight_layout()

    #birleşm kümesi
    '''
    out_0=np.fmax(rule1,rule2,rule3)
    out_1=np.fmax(rule4,rule5,rule6)
    out_2=np.fmax(rule7,rule8,rule9)

    out_fmax = np.fmax(out_1, out_0, out_2)
    '''

    out_0=np.fmax(rule1,rule2)
    out_1=np.fmax(rule4,rule5)
    out_2=np.fmax(rule7,rule8)

    out_fmax = np.fmax(np.fmax(out_0, out_1), out_2)
    #'''
    # Durulaştırma


    defuzzified  = fuzz.defuzz(mem_cforce, out_fmax, 'centroid')
    #defuzzified= fuzz.defuzzify.dcentroid(mem_cforce, out_fmax, -30)
    #print("aaaa:",defuzzyfiy)
    result = fuzz.interp_membership(mem_cforce, out_fmax, defuzzified)

    # Sonuç

    
    
#    if input_velocity<0:
#         input_height=input_height+input_velocity
#     if input_velocity>0:
#         input_height=input_height-input_velocity

    print("----old height",input_height)
    print("----old velo",input_velocity)

    print("Control force Çıkış Değeri deff:", defuzzified)
    print("Control force Çıkış Değeri result:", result)

    #yükseklik ve hız değişimi hesaplama
    input_height=input_height+input_velocity
    input_velocity=input_velocity+defuzzified

    print("----new height",input_height)
    print("----new velo",input_velocity)

    #450 dalgalanmanın başladığı yükseklik
    #300 velocitynin sıfıra indiği yükseklik
    '''
    if x[-1]>=66:

        fig, ax = plt.subplots(figsize=(8, 6))
        j=0
        while j<z:
            j=j+1
            ax.plot(x[j], y[j], 'o')
        ax.set_xlim(0, 500)
        ax.set_ylim(0, 1000)

        cforce0 = np.zeros_like(mem_cforce)

        fig, ax0 = plt.subplots(figsize = (7, 4))
        ax0.fill_between(mem_cforce, cforce0, out_fmax, facecolor = 'r', alpha = 0.7)
        #ax0.fill_between(mem_cforce, cforce0, rule8, facecolor = 'r', alpha = 0.7)
        ax0.plot(mem_cforce, out_fmax, 'r', linestyle = '--')
        ax0.set_title('output')

        plt.tight_layout()

        plt.show()
        #input()
    '''
    #input()

    z=z+1
    if z>500 or input_height<10:
        break

# birleşim kümesi görselleştirme

fig, ax = plt.subplots(figsize=(8, 6))
j=0
while j<z:
    j=j+1
    ax.plot(x[j], y[j], 'o')
ax.set_xlim(0, 250)
ax.set_ylim(0, 1000)

fig, ax1 = plt.subplots(figsize=(8, 6))
j=0
while j<z:
    j=j+1
    ax1.plot(y[j], v[j], 'o')
ax1.set_xlim(0, 1000)
ax1.set_ylim(5, -20)
ax1.set_xlabel('Height')
ax1.set_ylabel('Velocity')
##############

cforce0 = np.zeros_like(mem_cforce)

fig, ax0 = plt.subplots(figsize = (7, 4))
ax0.fill_between(mem_cforce, cforce0, out_fmax, facecolor = 'r', alpha = 0.7)
ax0.plot(mem_cforce, out_fmax, 'r', linestyle = '--')
ax0.set_title('output')

plt.tight_layout()

plt.show()