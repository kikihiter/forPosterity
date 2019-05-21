#主程序
import os
import shutil
import re
import subprocess
import math
import time
#from openpyxl import Workbook
global power


start=time.clock()
" 找到时间卡"
r_path = "c:\\Users\\Administrator\\Desktop\\relap-mcnp\\couple\\"
m_path = "e:\\MCNP5\\"
r_out_path =r_path+ "m-rout\\"
m_out_path = m_path+"r-mout\\"
e_path='c:\\Users\\Administrator\\Desktop\\'

def run_relap_new(filename='',dir1=''):
    name='0.bat'
    dir=dir1+name
    cmd ='del wxl.o' +'\n'+ 'del wxl.r' +'\n'+'relap5.exe -i '+filename+'.i -o '+filename+'.o -r '+filename+'.r'
    f = open(dir, 'w')
    f.write(cmd)
    f.close()
    cmd = '0.bat'
    subprocess.call(cmd, shell=False, cwd=dir1)
    #print('new')

def run_relap_restart(filename='', dir1=''):
    name = '1.bat'
    dir = dir1 + name
    cmd =  'relap5.exe -i ' + filename + '.i -o ' +  'wxl.o -r '  + 'wxl.r'
    #f = open(dir, 'w')
    #f.write(cmd)
    #f.close()
    #cmd = '1.bat'
    os.system(cmd)
    #print('restart')
def area_average(temp=[],rad=1):
    location=[a*rad/(len(temp)-1)for a in range(0,len(temp))]
    location_m=[(location[a]+location[a+1])/2for a in range(0,len(temp)-1)]
    location=location+location_m
    #print(location)
    location=sorted(location, reverse = False)
    #print(len(location))
    area = [ location [ 1 ] ** 2 -location [ 0 ] ** 2]
    area_m=[(location[a]**2-location[a-2]**2) for a in range(3,2*len(temp)-1,2)]
    area=area+area_m
    area.append(location[2*len(temp)-2]**2-location[2*len(temp)-3]**2)
    mul = [a * b for a, b in zip(temp, area)]
    area_average_value=sum(mul)/sum(area)
    return  area_average_value
run_relap_restart('restart', r_path)

cmd='chdir'+'\n'+'pause'
#f = open(dir, 'w')
#f.write(cmd)                              
#f.close()
#cmd = '1.bat'
os.system(cmd)

#Inlet_temperature=560
#Inlet_mass_flow_rate=82.12
#Inlet_density=0.752
#Outlet_pressure=15.5
#Power=18.47
#Total_length=365.76
#Assembly_size=21.42
#num_of_length=24
#num_of_edge = 17
#Fuel_rod_inner_radius=0.3951
#Fuel_rod_outer_radius=0.4583
#Guide_tube_inner_radius=0.5624
#Guide_tube_outer_radius=0.6032
#U235_enrichment=0.0425
#U238_enrichment=1-U235_enrichment
#Fuel_density=10.24
#Cladding_density=6.504
#mun_of_fuel=264
#num_of_tube=25
##几何数据
#
##RELAP初始卡
#
#ratio_initial = []
#IMAX = []
#x = 0
#while x <= num_of_length-1:
#    ratio_initial.append(0.041666666)
#    IMAX.append(0.01)
#    x = x+1
#xou=[]
#qou=[]
#wou=[]
#you=[]
#zou=[]
#k=1
#while (max(IMAX) > 0.0001 )& (k<19):
#    wb = Workbook()
#    sheet = wb.active
#    print('第', k, '次')
#    print("IMAX="+str(max(IMAX)))
#    qou.append(max(IMAX))
#    print(qou)
#    if os.path.exists(m_path+'1717.o'):
#        temp_2 = m_out_path+'out'+str(k-1)+'.txt'
#        shutil.move(m_path+'1717.o', temp_2)
#    if os.path.exists(m_path+'runtpe'):
#        os.remove(m_path+'runtpe')
#    if os.path.exists(m_path+'srctp'):
#        os.remove(m_path+'srctp') #mcnp: remove srctp,move and rename out.txt runtpe new.txt
#
#
#    if os.path.exists(r_path+'wxl.o'):
#        temp_2=r_out_path+'out'+str(k-1)+'.txt'
#        shutil.move(r_path+'wxl.o',temp_2) #RELAP:remove out.txt
#
#    print ("RELAP is running...........")
#    if k==1:
#        if os.path.exists(r_path + 'wxl.r'):
#            os.remove(r_path + 'wxl.r')
#        run_relap_new('wxl', r_path)
#    else:
#        run_relap_restart('restart', r_path)
#    print("RELAP done")
#
##    RTM 部分
#    f = open(r_path+'wxl.o', 'r')
#    Thermal_list = []
#    g = []
#    for line in f:
#        Thermal = line.strip()
#        Thermal_list.append(Thermal)
#        g.append(Thermal)
#    f.close()
#
#    ROWS_2 = '0MAJOR EDIT !!!time=    '+"%3.3f" %(50+50*k)+'     sec'
#    ROWSNO_2 =g.index(ROWS_2)
#    ROWS_3 = '0   At time=     '+"%3.3f" %(50+50*k)+'     sec       str.no.   mesh point temperatures     (K)'
#    ROWSNO_3 = g.index(ROWS_3)
#    #print(ROWSNO_2)
#    #print(ROWSNO_3)
#    num_node=11
#
##   燃料温度
#    Metal_fuel_list = []
#    Metal_clad_list = []
#    for c in range(0, 2*num_of_length,2):
#        Metal = g[ROWSNO_3+c+1].split()+g[ROWSNO_3+c+2].split()
#        Metal_fuel = Metal[1:(num_node+1)]
#        #print('Metal=', Metal)
#        Metal_clad = Metal[num_node:(num_node + 4)]
#        #print('Metal_clad=', Metal_clad)
#        Metal_fuel = list(map(float, Metal_fuel))
#        Metal_clad = list(map(float, Metal_clad))
#        print('Metal_fuel=',Metal_fuel)
#        print('Metal_clad=', Metal_clad)
#        Metal_fuel_list.append(area_average(Metal_fuel))   # extract every line to create list without empty
#        Metal_clad_list.append(area_average(Metal_clad))
#    print('Metal_fuel_list=',Metal_fuel_list)
#    Temperature_1=Metal_fuel_list
#    wou.append(Metal_clad_list)
##   水温度密度
#    Thermal_Density = []  # " 获得密度，去掉空格和引号"
#    Thermal_Temperature = []  # " 获得冷却剂温度，去掉空格和引号"
#    x = 0
#    while x <= num_of_length - 1:
#        if x<=18:
#            Density_vol=Thermal_list[ROWSNO_2 + 40 + x].split()
#            print(Density_vol)
#            Density_vol[0]=1
#            Density_vol=list(map(float, Density_vol))
#        else:
#            Density_vol=Thermal_list[ROWSNO_2 + 42 + x].split()
#            print(Density_vol)
#            Density_vol[0]=1
#            Density_vol=list(map(float, Density_vol))
#        Thermal_Density.append(Density_vol[1])  # find needed words's index and add
#        Temperature_vol=Thermal_list[ROWSNO_2 + 11 + x].split()
#        Temperature_vol[0]=1
#        Temperature_vol=list(map(float, Temperature_vol))
#        Thermal_Temperature.append(Temperature_vol[5])
#        x = x + 1
#    print('Thermal_Density=', Thermal_Density)
#    Density=Thermal_Density
#    print('Thermal_Temperature=', Thermal_Temperature)
#    Temperature=Thermal_Temperature
#    you.append(Temperature)
#    zou.append(Temperature_1)
#    "编写MCNP m卡"
#
#    text = []
#    narrative_line_1 = ('c  17*17*14')
#    text.append(narrative_line_1)
#    # cell
#    narrative_line_3 = ('c cell card')
#    text.append(narrative_line_3)
#
#    region = 3
#    d_u = Fuel_density
#    d_zr = Cladding_density
#    d_h2o = []
#    for i in range(0, num_of_length):
#        d_h2o.append(Density[i] / 1000)
#
#    for i in range(1, num_of_length * region * 2 + 1):
#        floor = math.ceil(i / (region * 2)) - 1
#        ceil = math.ceil(i / region)
#        if i % (region * 2) == 1:
#            data_line_20 = str(i) + ' ' + str(i) + ' -' + str(d_u) + ' -1 5 -6 u=' + str(ceil) + ' imp:n=1'
#            text.append(data_line_20)
#        elif i % (region * 2) == 2:
#            data_line_21 = str(i) + ' ' + str(i) + ' -' + str(d_zr) + ' 1 -2 5 -6 u=' + str(ceil) + ' imp:n=1'
#            text.append(data_line_21)
#        elif i % (region * 2) == 3:
#            data_line_22 = str(i) + ' ' + str(i) + ' -' + '%.5f' % d_h2o[floor] + ' 2 5 -6 u=' + str(ceil) + ' imp:n=1'
#            text.append(data_line_22)
#        elif i % (region * 2) == 4:
#            data_line_23 = str(i) + ' ' + str(i) + ' -' + '%.5f' % d_h2o[floor] + ' -3 5 -6 u=' + str(ceil) + ' imp:n=1'
#            text.append(data_line_23)
#        elif i % (region * 2) == 5:
#            data_line_24 = str(i) + ' ' + str(i) + ' -' + str(d_zr) + ' 3 -4 5 -6 u=' + str(ceil) + ' imp:n=1'
#            text.append(data_line_24)
#        elif i % (region * 2) == 0:
#            data_line_25 = str(i) + ' ' + str(i) + ' -' + '%.5f' % d_h2o[floor] + ' 4 5 -6 u=' + str(ceil) + ' imp:n=1'
#            text.append(data_line_25)
#    for i in range(1, num_of_length + 1):
#        data_line = str(num_of_length * region * 2 + 2 * i - 1) + '    0     7 -8 9 -10 5 -6 u=' + str(
#            100 + i) + ' lat=1 imp:n=1 fill=-' + str(int((num_of_edge - 1) / 2)) + ':' + str(
#            int((num_of_edge - 1) / 2)) + ' -' + str(int((num_of_edge - 1) / 2)) + ':' + str(
#            int((num_of_edge - 1) / 2)) + ' 0:0'
#        text.append(data_line)
#        data_line = ('        ' + 17 * (str(2 * i - 1) + ' ') + '\n' +
#                     '        ' + 17 * (str(2 * i - 1) + ' ') + '\n' +
#                     '        ' + 5 * (str(2 * i - 1) + ' ') + str(2 * i) + ' ' + 2 * (str(2 * i - 1) + ' ') + str(
#                2 * i) + ' ' + 2 * (str(2 * i - 1) + ' ') + str(2 * i) + ' ' + 5 * (str(2 * i - 1) + ' ') + '\n' +
#                     '        ' + 3 * (str(2 * i - 1) + ' ') + str(2 * i) + ' ' + 9 * (str(2 * i - 1) + ' ') + str(
#                2 * i) + ' ' + 3 * (str(2 * i - 1) + ' ') + '\n' +
#                     '        ' + 17 * (str(2 * i - 1) + ' ') + '\n' +
#                     '        ' + 2 * (str(2 * i - 1) + ' ') + str(2 * i) + ' ' + 2 * (str(2 * i - 1) + ' ') + str(
#                2 * i) + ' ' + 2 * (str(2 * i - 1) + ' ') + str(2 * i) + ' ' + 2 * (str(2 * i - 1) + ' ') + str(
#                2 * i) + ' ' + 2 * (str(2 * i - 1) + ' ') + str(2 * i) + ' ' + 2 * (str(2 * i - 1) + ' ') + '\n' +
#                     '        ' + 17 * (str(2 * i - 1) + ' ') + '\n' +
#                     '        ' + 17 * (str(2 * i - 1) + ' ') + '\n' +
#                     '        ' + 2 * (str(2 * i - 1) + ' ') + str(2 * i) + ' ' + 2 * (str(2 * i - 1) + ' ') + str(
#                2 * i) + ' ' + 2 * (str(2 * i - 1) + ' ') + str(2 * i) + ' ' + 2 * (str(2 * i - 1) + ' ') + str(
#                2 * i) + ' ' + 2 * (str(2 * i - 1) + ' ') + str(2 * i) + ' ' + 2 * (str(2 * i - 1) + ' ') + '\n' +
#                     '        ' + 17 * (str(2 * i - 1) + ' ') + '\n' +
#                     '        ' + 17 * (str(2 * i - 1) + ' ') + '\n' +
#                     '        ' + 2 * (str(2 * i - 1) + ' ') + str(2 * i) + ' ' + 2 * (str(2 * i - 1) + ' ') + str(
#                2 * i) + ' ' + 2 * (str(2 * i - 1) + ' ') + str(2 * i) + ' ' + 2 * (str(2 * i - 1) + ' ') + str(
#                2 * i) + ' ' + 2 * (str(2 * i - 1) + ' ') + str(2 * i) + ' ' + 2 * (str(2 * i - 1) + ' ') + '\n' +
#                     '        ' + 17 * (str(2 * i - 1) + ' ') + '\n' +
#                     '        ' + 3 * (str(2 * i - 1) + ' ') + str(2 * i) + ' ' + 9 * (str(2 * i - 1) + ' ') + str(
#                2 * i) + ' ' + 3 * (str(2 * i - 1) + ' ') + '\n' +
#                     '        ' + 5 * (str(2 * i - 1) + ' ') + str(2 * i) + ' ' + 2 * (str(2 * i - 1) + ' ') + str(
#                2 * i) + ' ' + 2 * (str(2 * i - 1) + ' ') + str(2 * i) + ' ' + 5 * (str(2 * i - 1) + ' ') + '\n' +
#                     '        ' + 17 * (str(2 * i - 1) + ' ') + '\n' +
#                     '        ' + 17 * (str(2 * i - 1) + ' '))
#        text.append(data_line)
#        data_line = str(num_of_length * region * 2 + 2 * i) + ' 0 11 -12 13 -14 5 -6 u=' + str(
#            200 + i) + ' fill=' + str(100 + i) + ' lat=1 imp:n=1'
#        text.append(data_line)
#        # reflector
#
#    # data_line = str(num_of_length*region*2  + 1) + '    ' + str(num_of_length*region*2  + 1) + ' -1.7  16 -17 18 -19 5 -6 u=' + str(ceil + 1) + ' imp:n=1'
#    # text.append(data_line)
#    # data_line = str(num_of_length*region*2  + 2) + '    0     7 -8 9 -10 20 -21 u=' + str(ceil + 2) + ' lat=1 imp:n=1 fill=-' + str(int((num_of_edge - 1) / 2)) + ':' + str(
#    #    int((num_of_edge - 1) / 2)) + ' -' + str(int((num_of_edge - 1) / 2)) + ':' + str(
#    #    int((num_of_edge - 1) / 2)) + ' 0:0'
#    # text.append(data_line)
#    # data_line = '        ' + str(num_of_cell + 1) + ' ' + str(num_of_edge ** 2 - 1) + 'r'
#    # text.append(data_line)
#
#    data_line = str(num_of_length * region * 2 + 2 * num_of_length + 1) + '    0   11 -12 13 -14 -6 5 u=' + str(
#        200 + num_of_length + 1) + ' lat=1 imp:n=1 fill=0:0 0:0 0:' + str(num_of_length - 1)
#    text.append(data_line)
#    data_line = '        201 22i 224'
#    text.append(data_line)
#    data_line = str(
#        num_of_length * region * 2 + 2 * num_of_length + 2) + ' 0   11 -12 13 -14 -15 5    imp:n=1 fill=' + str(
#        200 + num_of_length + 1)
#    text.append(data_line)
#    data_line = str(num_of_length * region * 2 + 2 * num_of_length + 3) + ' ' + str(
#        num_of_length * region * 2 + 1) + ' -1.7   18 -19 20 -21 16 -17 #' + str(
#        num_of_length * region * 2 + 2 * num_of_length + 2) + '   imp:n=1'
#    text.append(data_line)
#    data_line = str(num_of_length * region * 2 + 2 * num_of_length + 4) + ' 0   -18:19:-20:21:-16:17   imp:n=0' + '\n'
#    text.append(data_line)
#
#    narrative_line_2 = ('c surface')
#    text.append(narrative_line_2)
#    data_line_surface = ('1    CZ 0.3951' + '\n' + '2    CZ 0.4583' + '\n' + '3    CZ 0.5624  ' + '\n' +
#                         '4    CZ 0.6032' + '\n' + '5    PZ -7.62' + '\n' + '6    PZ 7.62     ' + '\n' +
#                         '7    PX -0.63 ' + '\n' + '8    PX 0.63  ' + '\n' + '9    PY -0.63   ' + '\n' +
#                         '10   PY 0.63  ' + '\n' + '*11  PX -10.71' + '\n' + '*12   PX 10.71   ' + '\n' +
#                         '*13   PY -10.71' + '\n' + '*14   PY 10.71' + '\n' + '15   PZ 358.14  ' + '\n' +
#                         '16   PZ -37.62' + '\n' + '17   PZ 388.14' + '\n' + '18   PX -10.71001' + '\n' +
#                         '19   PX 10.71001' + '\n' + '20   PY -10.71001' + '\n' + '21   PY 10.71001' + '\n')  #
#    text.append(data_line_surface)
#
#    #   data card
#
#    narrative_line_4 = ('c data')
#    text.append(narrative_line_4)
#    for i in range(1, num_of_length + 1):
#        data_line = '     ' + '(' + str(num_of_length * region * 2 + 2 * i) + '<' + str(
#            num_of_length * region * 2 + 2 * num_of_length + 1) + '[0 0 ' + str(i - 1) + ']' + ')'
#        if i == 1:
#            data_line = 'f7:n' + data_line
#        text.append(data_line)
#    a = ' 1'
#    data_line = 'sd7'
#    for i in range(2, num_of_length + 2):
#        data_line = data_line + a
#    text.append(data_line)
#    data_line = ('kcode 5000 1.0 500 550' + '\n' + 'ksrc  1.26 1.26 0.0 1.26 1.26 15.24 1.26 1.26 30.48' + '\n'
#                 + '     1.26 1.26 121.92 -1.26 -1.26 152.4 1.26 1.26 60.96 1.26 1.26 180.88' + '\n'
#                 + '     1.26 1.26 213.36 -1.26 -1.26 243.84 1.26 1.26 274.32 1.26 1.26 304.8' + '\n'
#                 + '     1.26 1.26 335.28 -1.26 -1.26 365.76 ')
#    text.append(data_line)
#
#    temprature_gap_1 = range(550, 950, 50)
#    temprature_gap_2 = range(550, 720, 20)
#    temprature_gap_3 = range(1000, 1500, 50)
#    if min(Temperature) < temprature_gap_2[0]:
#        print('this is a error,moderater temperature is too low')
#        print(x)
#    elif min(Temperature_1) < temprature_gap_1[0]:
#        print('this is a error,fuel temperature is too low')
#        print(x)
#    elif max(Temperature) > temprature_gap_2[-1]:
#        print('this is a error,moderater temperature is too high')
#        print(x)
#    elif max(Temperature_1) > temprature_gap_3[-1]:
#        print('this is a error,fuel temperature is too high')
#        print(x)
#
#    for i in range(1, num_of_length * region * 2 + 1):
#        floor = math.ceil(i / (region * 2)) - 1
#        if i % (region * 2) == 1:
#            if Temperature_1[floor] < 950:
#                for a in temprature_gap_1:
#                    if (Temperature_1[floor] >= a) and (Temperature_1[floor] < (a + 50)):
#                        low = ((a + 50) ** 0.5 - Temperature_1[floor] ** 0.5) / ((a + 50) ** 0.5 - a ** 0.5)
#                        high = 1 - low
#                        data_line = ('m' + str(i) + '   92235.' + str(int(a / 10)) + 'c ' + "%.7f" % (
#                                0.0425 * low) + ' 92235.' + str(int(a / 10) + 5) + 'c ' + "%.7f" % (0.0425 * high) + '\n'
#                                     + '     92238.' + str(int(a / 10)) + 'c ' + "%.7f" % (0.9675 * low) + ' 92238.' + str(
#                                int(a / 10) + 5) + 'c ' + "%.7f" % (0.9675 * high) + '\n'
#                                     + '     8016.' + str(int(a / 10)) + 'c ' + "%.7f" % (2 * low) + ' 8016.' + str(
#                                int(a / 10) + 5) + 'c ' + "%.7f" % (2 * high))
#
#                        text.append(data_line)
#            elif Temperature_1[floor] < 1000:
#                low = ((1000) ** 0.5 - Temperature_1[floor] ** 0.5) / ((1000) ** 0.5 - 950 ** 0.5)
#                high = 1 - low
#                data_line = ('m' + str(i) + '   92235.95c ' + "%.7f" % (0.0425 * low) + ' 92235.00c ' + "%.7f" % (0.0425 * high) + '\n'
#                             + '     92238.95c ' + "%.7f" % (0.9675 * low) + ' 92238.00c ' + "%.7f" % (0.9675 * high) + '\n'
#                             + '     8016.95c ' + "%.7f" % (2 * low) + ' 8016.00c ' + "%.7f" % (2 * high))
#                text.append(data_line)
#            else:
#                for a in temprature_gap_3:
#                    if (Temperature_1[floor] >= a) and (Temperature_1[floor] < (a + 50)):
#                        low = ((a + 50) ** 0.5 - Temperature_1[floor] ** 0.5) / ((a + 50) ** 0.5 - a ** 0.5)
#                        high = 1 - low
#                        data_line = ('m' + str(i) + '   92235.' + "%02d"%(int((a-1000) / 10)) + 'c ' + "%.7f" % (
#                            0.0425 * low) + ' 92235.' + "%02d"%(int((a-1000) / 10) + 5) + 'c ' + "%.7f" % (0.0425 * high) + '\n'
#                                     + '     92238.' + "%02d"%(int((a-1000) / 10)) + 'c ' + "%.7f" % (
#                                             0.9675 * low) + ' 92238.' + "%02d"%(
#                                int((a-1000) / 10) + 5) + 'c ' + "%.7f" % (0.9675 * high) + '\n'
#                                     + '     8016.' + "%02d"%(int((a-1000) / 10)) + 'c ' + "%.7f" % (2 * low) + ' 8016.' + "%02d"%(
#                                int((a-1000) / 10) + 5) + 'c ' + "%.7f" % (2 * high))
#
#                        text.append(data_line)
#        elif i % (region * 2) == 2:
#            data_line = 'm' + str(i) + '   ' + '50000  0.015 26056 0.0012  24052 0.001  40000 0.9823  7014  0.0005'
#            text.append(data_line)
#        elif i % (region * 2) == 3:
#            for a in temprature_gap_2:
#                if (Temperature[floor] >= a) and (Temperature[floor] < (a + 20)):
#                    low = ((a + 20) ** 0.5 - Temperature[floor] ** 0.5) / ((a + 20) ** 0.5 - a ** 0.5)
#                    high = 1 - low
#                    data_line = ('m' + str(i) + '   ' + '1001.' + str(int(a / 10)) + 'c ' + str(
#                        "%.7f" % (2 * low)) + ' 1001.' + str(int(a / 10) + 2) + 'c ' + str("%.7f" % (2 * high)) + '\n'
#                                 + '     ' + '8016.' + str(int(a / 10)) + 'c ' + str("%.7f" % low) + ' 8016.' + str(
#                            int(a / 10) + 2) + 'c ' + str("%.7f" % high) + '\n'
#                                 + '     ' + '5011.' + str(int(a / 10)) + 'c ' + str(
#                            "%.7f" % (0.001336767 * low)) + ' 5011.' + str(int(a / 10) + 2) + 'c ' + str(
#                            "%.7f" % (0.001336767 * high)) + '\n'
#                                 + '     ' + '5010.' + str(int(a / 10)) + 'c ' + str(
#                            "%.7f" % (0.0003300248 * low)) + ' 5010.' + str(int(a / 10) + 2) + 'c ' + str(
#                            "%.7f" % (0.0003300248 * high)))
#                    text.append(data_line)
#        elif i % (region * 2) == 4:
#            for a in temprature_gap_2:
#                if (Temperature[floor] >= a) and (Temperature[floor] < (a + 20)):
#                    low = ((a + 20) ** 0.5 - Temperature[floor] ** 0.5) / ((a + 20) ** 0.5 - a ** 0.5)
#                    high = 1 - low
#                    data_line = ('m' + str(i) + '   ' + '1001.' + str(int(a / 10)) + 'c ' + str(
#                        "%.7f" % (2 * low)) + ' 1001.' + str(int(a / 10) + 2) + 'c ' + str("%.7f" % (2 * high)) + '\n'
#                                 + '     ' + '8016.' + str(int(a / 10)) + 'c ' + str("%.7f" % low) + ' 8016.' + str(
#                            int(a / 10) + 2) + 'c ' + str("%.7f" % high) + '\n'
#                                 + '     ' + '5011.' + str(int(a / 10)) + 'c ' + str(
#                            "%.7f" % (0.001336767 * low)) + ' 5011.' + str(int(a / 10) + 2) + 'c ' + str(
#                            "%.7f" % (0.001336767 * high)) + '\n'
#                                 + '     ' + '5010.' + str(int(a / 10)) + 'c ' + str(
#                            "%.7f" % (0.0003300248 * low)) + ' 5010.' + str(int(a / 10) + 2) + 'c ' + str(
#                            "%.7f" % (0.0003300248 * high)))
#                    text.append(data_line)
#        elif i % (region * 2) == 5:
#            data_line = 'm' + str(i) + '   ' + '50000  0.015 26056 0.0012  24052 0.001  40000 0.9823  7014  0.0005'
#            text.append(data_line)
#        elif i % (region * 2) == 0:
#            for a in temprature_gap_2:
#                if (Temperature[floor] >= a) and (Temperature[floor] < (a + 20)):
#                    low = ((a + 20) ** 0.5 - Temperature[floor] ** 0.5) / ((a + 20) ** 0.5 - a ** 0.5)
#                    high = 1 - low
#                    data_line = ('m' + str(i) + '   ' + '1001.' + str(int(a / 10)) + 'c ' + str(
#                        "%.7f" % (2 * low)) + ' 1001.' + str(int(a / 10) + 2) + 'c ' + str("%.7f" % (2 * high)) + '\n'
#                                 + '     ' + '8016.' + str(int(a / 10)) + 'c ' + str("%.7f" % low) + ' 8016.' + str(
#                            int(a / 10) + 2) + 'c ' + str("%.7f" % high) + '\n'
#                                 + '     ' + '5011.' + str(int(a / 10)) + 'c ' + str(
#                            "%.7f" % (0.001336767 * low)) + ' 5011.' + str(int(a / 10) + 2) + 'c ' + str(
#                            "%.7f" % (0.001336767 * high)) + '\n'
#                                 + '     ' + '5010.' + str(int(a / 10)) + 'c ' + str(
#                            "%.7f" % (0.0003300248 * low)) + ' 5010.' + str(int(a / 10) + 2) + 'c ' + str(
#                            "%.7f" % (0.0003300248 * high)))
#                    text.append(data_line)
#    data_line = ('m' + str(num_of_length * region * 2 + 1) + '   ' + '6012 1')
#    text.append(data_line)
#
#    word = '\n'.join(text)
#    f = open(m_path + '1717.i', 'w')
#    f.write(word)
#    f.close()
#    #      RTM  END
#
#    print("MCNP is running.........")
#    if os.path.exists(m_path + '1717.i'):
#        cmd = 'mpirun -localonly 7 mcnp5d6mpi.exe i=1717.i o=1717.o'
#        subprocess.call(cmd, shell=True, cwd=m_path)
#    print("MCNP done")
#
#    #   MTR部分
#    f = open(m_path + '1717.o', 'r')
#    temp_list = []
#    for line in f:
#        temp = line.strip()
#        temp_list.append(temp)  # extract every line to create list without empty
#    f.close()
#    #    "从数组中获得能量MeV"
#    flux = []
#    var_1 = 'cell (' + str(num_of_length * region * 2 + 2) + '<' + str(
#        num_of_length * region * 2 + 2 * num_of_length + 1) + '[0 0 0])'
#
#    print(var_1)
#    b = 0
#    while b <= num_of_length - 1:
#        flux.append(temp_list[temp_list.index(var_1) + 1 + b * 3])
#        b = b + 1
#    #   "去掉误差和引号"
#    p = re.compile(r' ')  # 空格识别
#    fuel_flux = []
#    for a in flux:
#        w = p.split(a)
#        fuel_flux.append(float(w[0]))  # split by empty and extract needed words
#    #    print (fuel_flux)
#
#    #   "各个组件功率所占份额"
#    ratio = []
#    b = 0
#    while b <= num_of_length - 1:
#        ratio.append(fuel_flux[b] / sum(fuel_flux))
#        print(ratio[b],type(ratio[b]))
#        b = b + 1
#
#    f = open(r_path + 'restart.i', 'r')
#    number_list = []
#    for line in f:
#        number = line.strip()  # 查找比率卡所在的行数
#        number_list.append(number)
#    f.close()
#
#    # 改时间
#    number_list[1] = '103     ' + "%3d" %(50+50*k)+ '000'
#    number_list[2] = '201     ' + "%3.1f" %(100+50*k) + '  1.0e-6  0.001   3  50000  5000  50000'
#    number_list[23] ='13000701   10  '+"%.8f"%(ratio[0])  +'  0.0  0.0  ' +'1'
#    number_list[24] ='13000702   10  '+"%.8f"%(ratio[1])  +'  0.0  0.0  ' +'2'
#    number_list[25] ='13000703   10  '+"%.8f"%(ratio[2])  +'  0.0  0.0  ' +'3'
#    number_list[26] ='13000704   10  '+"%.8f"%(ratio[3])  +'  0.0  0.0  ' +'4'
#    number_list[27] ='13000705   10  '+"%.8f"%(ratio[4])  +'  0.0  0.0  ' +'5'
#    number_list[28] ='13000706   10  '+"%.8f"%(ratio[5])  +'  0.0  0.0  ' +'6'
#    number_list[29] ='13000707   10  '+"%.8f"%(ratio[6])  +'  0.0  0.0  ' +'7'
#    number_list[30] ='13000708   10  '+"%.8f"%(ratio[7])  +'  0.0  0.0  ' +'8'
#    number_list[31] ='13000709   10  '+"%.8f"%(ratio[8])  +'  0.0  0.0  ' +'9'
#    number_list[32] ='13000710   10  '+"%.8f"%(ratio[9])  +'  0.0  0.0  ' +'10'
#    number_list[33] ='13000711   10  '+"%.8f"%(ratio[10]) +'  0.0  0.0  ' +'11'
#    number_list[34] ='13000712   10  '+"%.8f"%(ratio[11]) +'  0.0  0.0  ' +'12'
#    number_list[35] ='13000713   10  '+"%.8f"%(ratio[12]) +'  0.0  0.0  ' +'13'
#    number_list[36] ='13000714   10  '+"%.8f"%(ratio[13]) +'  0.0  0.0  ' +'14'
#    number_list[37] ='13000715   10  '+"%.8f"%(ratio[14]) +'  0.0  0.0  ' +'15'
#    number_list[38] ='13000716   10  '+"%.8f"%(ratio[15]) +'  0.0  0.0  ' +'16'
#    number_list[39] ='13000717   10  '+"%.8f"%(ratio[16]) +'  0.0  0.0  ' +'17'
#    number_list[40] ='13000718   10  '+"%.8f"%(ratio[17]) +'  0.0  0.0  ' +'18'
#    number_list[41] ='13000719   10  '+"%.8f"%(ratio[18]) +'  0.0  0.0  ' +'19'
#    number_list[42] ='13000720   10  '+"%.8f"%(ratio[19]) +'  0.0  0.0  ' +'20'
#    number_list[43] ='13000721   10  '+"%.8f"%(ratio[20]) +'  0.0  0.0  ' +'21'
#    number_list[44] ='13000722   10  '+"%.8f"%(ratio[21]) +'  0.0  0.0  ' +'22'
#    number_list[45] ='13000723   10  '+"%.8f"%(ratio[22]) +'  0.0  0.0  ' +'23'
#    number_list[46] ='13000724   10  '+"%.8f"%(ratio[23]) +'  0.0  0.0  ' +'24'
#
#    input = '\n'.join(number_list)
#    f = open(r_path + 'restart.i', 'w')
#    f.write(input)
#    f.close()
#    #
#    #   MTR end
#    r = []
#    for a in ratio:
#        r.append(float(a))
#    xou.append(r)
#    r_i = []
#    for a in ratio_initial:
#        r_i.append(float(a))
#    IMEX = []
#    u = 0
#    while u <= num_of_length - 1:
#        IMEX.append(float(r[u]) * (abs(float((r[u] - r_i[u]) / r[u]))))
#        IMAX[u] = IMEX[u]
#        print("IMEX=" + str(IMEX[u]))
#        u = u + 1
#    y = 0
#    while y <= num_of_length - 1:
#        ratio_initial[y] = ratio[y]
#        y = y + 1
#
#    sheet['A1'] = 'power'
#    sheet.cell(row=k + 2, column=1).value = 'temp_of_coolant'
#    sheet.cell(row=2 * k + 3, column=1).value = 'temp_of_fuel'
#    sheet.cell(row=3 * k + 4, column=1).value = 'temp_of_clad'
#    for c in range(0, num_of_length):
#        for d in range(0, k):
#            sheet.cell(row=1, column=c + 2).value = c + 1
#            sheet.cell(row=d + 2, column=c + 2).value = xou[d][c]
#            sheet.cell(row=d + 2, column=1).value = d + 1
#
#            sheet.cell(row=k + (d + 1) + 2, column=c + 2).value = you[d][c]
#            sheet.cell(row=k + (d + 1) + 2, column=1).value = d + 1
#
#            sheet.cell(row=2 * k + (d + 1) + 3, column=c + 2).value = zou[d][c]
#            sheet.cell(row=2 * k + (d + 1) + 3, column=1).value = d + 1
#
#            sheet.cell(row=3 * k + (d + 1) + 4, column=c + 2).value = wou[d][c]
#            sheet.cell(row=3 * k + (d + 1) + 4, column=1).value = d + 1
#    wb.save('c:\\Users\\Administrator\\Desktop\\2.xlsx')
#
#    k = k + 1
#print("victory")
#end = time.clock()
#print("time:" + str(end - start) + 's')