# # bài 1
# product={"name":"laptop","price":200000000}
# print(product["price"])
# if "stock" in product:
#     print("có sản phẩm")   
# else:
#     print("0")  
# bài 2
candidate_A_skills=["python","java","sql","git"]
candidate_B_skills=["java","docker","go","sql"]
tat_ca_ky_nang=candidate_A_skills + candidate_B_skills
print( "tất cả" ,tat_ca_ky_nang)
ky_nang_chung=set(candidate_A_skills) & set(candidate_B_skills)
print("kỹ năng chung",ky_nang_chung)
ky_nang_rieng=set(candidate_A_skills) - set(candidate_B_skills)
print("kỹ năng riêng của A",ky_nang_rieng)