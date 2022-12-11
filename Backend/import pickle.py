import pickle
info = open(r"E:/cs_project/Billing-software/Backend/login_info.dat", "rb")
a = pickle.load(info)
print(a)