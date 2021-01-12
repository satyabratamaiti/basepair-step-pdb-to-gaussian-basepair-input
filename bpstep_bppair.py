import getopt
import sys
import os,os.path
def main(argv):
	filename=""
	try:
		opts,argvs=getopt.getopt(argv,"hf:",["help","filename"])
	except getopt.GetoptError:
		print("bpstep_bppair.py -f <input filename>")
		print("bpstep_bppair.py --filename <input filename>")
		sys.exit()
	for opt,arg in opts:
		if opt=="-h":
			print("you should type :")
			print("bpstep_bppair.py -f <input filename>")
			print("bpstep_bppair.py --filename <input filename>")
			sys.exit()
		elif opt in ("-f", "--filename"):
			filename=arg
		else:
			print("tryagain")
	
	filename_m=filename[:-4]
	filename_bp1=filename_m[2:7]
	filename_bp2=filename_m[7:12]
	fp=open(filename,'r')
#	print(filename_c)
	info_b1=[]
	info_b2=[]
	info_b3=[]
	info_b4=[]
	for line in fp:
		if (line[:4]=="ATOM") and (line[25:26]=="1"):
			info_b1.append(line)
		if (line[:4]=="ATOM") and (line[25:26]=="2"):
			line=line.replace(str(line[24:27])," 1 ")
			info_b2.append(line)
		if (line[:4]=="ATOM") and (line[25:26]=="3"):
			line=line.replace(str(line[24:27])," 2 ")
			info_b3.append(line)
		if (line[:4]=="ATOM") and (line[25:26]=="4"):
			line=line.replace(str(line[24:27])," 2 ")
			info_b4.append(line)
# writing .com file of 1-2
	fw1=open(filename_m+"-"+filename_bp1+"_bp1.pdb",'w')	
	fw2=open(filename_m+"-"+filename_bp2+"_bp2.pdb",'w')	
	for item in info_b1:
		fw1.write("%s" % (item))	
	for item in info_b4:
		fw1.write("%s" % (item))
	fw1.write("END")	
	for item in info_b2:
		fw2.write("%s" % (item))	
	for item in info_b3:
		fw2.write("%s" % (item)) 
	fw2.write("END")
	fw1.close()
	fw2.close()
	fbp1=open(filename_m+"-"+filename_bp1+"_bp1.pdb",'r')
	fbp2=open(filename_m+"-"+filename_bp2+"_bp2.pdb",'r')

	info_at1_bp1=[]
	info_cr1_bp1=[]
	info_at2_bp1=[]
	info_cr2_bp1=[]
	info_at1_bp2=[]
	info_cr1_bp2=[]
	info_at2_bp2=[]
	info_cr2_bp2=[]
	c_poise1_bp1=[]
	c_poise2_bp1=[]
	c_poise1_bp2=[]
	c_poise2_bp2=[]
	for line1 in fbp1:
		if (line1[:4]=="ATOM") and (line1[25:26]=="1"):
#                       print(resn1)
			atype1=line1[13:14]
			info_at1_bp1.append(atype1)
			coor1x=line1[30:38]
			coor1y=line1[38:46]
			coor1z=line1[46:54]
			cp1=line1[25:26]
			coor1=str(coor1x) + " " + str(coor1y) + " " + str(coor1z)
			c_poise1_bp1.append(cp1)
			info_cr1_bp1.append(coor1)
		if (line1[:4]=="ATOM") and (line1[25:26]=="2"):
			atype2=line1[13:14]
			info_at2_bp1.append(atype2)
			coor2x=line1[30:38]
			coor2y=line1[38:46]
			coor2z=line1[46:54]
			coor2=str(coor2x) + " " + str(coor2y) + " " + str(coor2z)
			cp2=line1[25:26]
			c_poise2_bp1.append(cp2)
			info_cr2_bp1.append(coor2)
	for line11 in fbp2:
		if (line11[:4]=="ATOM") and (line11[25:26]=="1"):
#                       print(resn1)
			atype11=line11[13:14]
			info_at1_bp2.append(atype11)
			coor11x=line11[30:38]
			coor11y=line11[38:46]
			coor11z=line11[46:54]
			cp11=line11[25:26]
			coor11=str(coor11x) + " " + str(coor11y) + " " + str(coor11z)
			c_poise1_bp2.append(cp11)
			info_cr1_bp2.append(coor11)
		if (line11[:4]=="ATOM") and (line11[25:26]=="2"):
			atype22=line11[13:14]
			info_at2_bp2.append(atype22)
			coor22x=line11[30:38]
			coor22y=line11[38:46]
			coor22z=line11[46:54]
			coor22=str(coor22x) + " " + str(coor22y) + " " + str(coor22z)
			cp22=line11[25:26]
			c_poise2_bp2.append(cp22)
			info_cr2_bp2.append(coor22)
	fbp1.close()
	fbp2.close()
	print(info_at1_bp1,info_cr1_bp1,c_poise1_bp1)	
	print(info_at1_bp2,info_cr1_bp2,c_poise1_bp2)	
	cm1=""
	fw_bp1_com=open(filename_m+"_bp1.com",'w')
	fw_bp2_com=open(filename_m+"_bp2.com",'w')
	fw_bp1_com.write("%nprocshared=32"+"\n" + "%mem=32GB" + "\n")
	fw_bp2_com.write("%nprocshared=32"+"\n" + "%mem=32GB" + "\n")
	fw_bp1_com.write("#p sp wb97xd/cc-pvdz scf=(maxcycles=25) counterpoise=2" + "\n")
	fw_bp2_com.write("#p sp wb97xd/cc-pvdz scf=(maxcycles=25) counterpoise=2" + "\n")
	fw_bp1_com.write("\n")
	fw_bp2_com.write("\n")
	fw_bp1_com.write("bp pair stacking" + "\n" + "\n")
	fw_bp2_com.write("bp pair stacking" + "\n" + "\n")
	f_bp1=open(filename_m+"-"+filename_bp1+"_bp1.pdb",'r')
	f_bp2=open(filename_m+"-"+filename_bp2+"_bp2.pdb",'r')
	for line2 in f_bp1:
		if ("+" not in line2):
			cm1="0 1 0 1 0 1"
		elif (line2[79:80]=="+") and (line2[25:26]=="1"):
#			if (line2[25:26]=="1"):
#				fw_bp1_com.write("1 1 1 1 0 1" + "\n")
			cm1="1 1 1 1 0 1"
			break
		elif (line2[79:80]=="+") and (line2[25:26]=="2"):
#				fw_bp1_com.write("1 1 0 1 1 1" + "\n")
			cm1="1 1 0 1 1 1"
			break
#		else:
#			cm="0 1 0 1 0 1"
#			charge_m.append(cm)
	print(cm1)
	fw_bp1_com.write(str(cm1) + "\n")
#	fw_bp1_com.write("\n")
	for val1 in zip(info_at1_bp1,info_cr1_bp1,c_poise1_bp1):
		fw_bp1_com.write('{} \t {} \t {} \n'.format(val1[0],val1[1], val1[2]))
	for val2 in zip(info_at2_bp1,info_cr2_bp1,c_poise2_bp1):
		fw_bp1_com.write('{} \t {} \t {} \n'.format(val2[0],val2[1], val2[2]))
	fw_bp1_com.write("\n")
	for line3 in f_bp2:
		if ("+" not in line3):
			cm2="0 1 0 1 0 1"
		elif (line3[79:80]=="+") and (line3[25:26]=="1"):
#                       if (line2[25:26]=="1"):
#                               fw_bp1_com.write("1 1 1 1 0 1" + "\n")
			cm2="1 1 1 1 0 1"
			break
		elif (line3[79:80]=="+") and (line3[25:26]=="2"):
#                               fw_bp1_com.write("1 1 0 1 1 1" + "\n")
			cm2="1 1 0 1 1 1"
			break
#               else:
#                       cm="0 1 0 1 0 1"
#                       charge_m.append(cm)
	print(cm2)
	fw_bp2_com.write(str(cm2) + "\n")
#	fw_bp2_com.write("\n")
	for val3 in zip(info_at1_bp2,info_cr1_bp2,c_poise1_bp2):
		fw_bp2_com.write('{} \t {} \t {} \n'.format(val3[0],val3[1], val3[2]))
	for val4 in zip(info_at2_bp2,info_cr2_bp2,c_poise2_bp2):
		fw_bp2_com.write('{} \t {} \t {} \n'.format(val4[0],val4[1], val4[2]))
	fw_bp2_com.write("\n")


if __name__ == "__main__":
	main(sys.argv[1:])

