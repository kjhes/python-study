# dictionary(딕셔너리) : 키(key)와 값(value) 쌍으로 저장

word_dic={
    "dog":"강아지",
    "cat":"고양이",
    "tiger":"호랑이",
    "lion":"사자"
}

print(word_dic)
print(word_dic["cat"])

word_dic["dog"] = "멍멍이"
print(word_dic)
print(word_dic["dog"])

word_dic["bear"] = "곰"
print(word_dic)


ice = {"메로나":[1000,2],"폴라포":[1200,3],"빵빠레":[1800,4]}
print(ice)
# 메로나 가격 출력
print(ice["메로나"][0])
#빵빠레 재고 출력
print(ice["빵빠레"][1])







