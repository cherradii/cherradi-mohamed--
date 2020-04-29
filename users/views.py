# # users/views.py
# from django.urls import reverse_lazy, include
# from django.views.generic import CreateView
# # from .forms import CustomUserCreationForm, USPTOform
# from .forms import USPTOform
# from django.shortcuts import render
# from django.http import HttpResponse
# import json
# import numpy as np
# from pymongo import MongoClient
# import selenium.webdriver as webdriver
# from nltk.stem import PorterStemmer
# from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.cluster import KMeans
# # from wordcloud import WordCloud, STOPWORDS
import os
import zipfile
import io
import glob
from django.http import HttpResponse
# # import matplotlib.pyplot as plt
# # from sklearn.feature_extraction.text import CountVectorizer
# # import nltk
# from nltk.tokenize import word_tokenize
# import re
# import codecs
# import collections
#
#
#
#
# # class SignUpView(CreateView):
# #     form_class = CustomUserCreationForm
# #     success_url = reverse_lazy('login')
# #     template_name = 'signup.html'
#
#
# # browser = webdriver.Chrome(executable_path="C:/SeleniumDrivers/chromedriver.exe")
# browser = webdriver.PhantomJS(executable_path="C:/SeleniumDrivers/phantomjs/bin/phantomjs.exe")
# def wordCount(mystring):
#     tempcount = 0
#     count = 1
#
#     try:
#         for character in mystring:
#             if character == " ":
#                 tempcount += 1
#                 if tempcount == 1:
#                     count += 1
#
#                 else:
#                     tempcount += 1
#             elif character == ";":
#                 tempcount = 0
#
#         return count
#
#     except Exception:
#         error = "Not a string"
#         return error
# def get_results(Key):
#
#
#     url = "http://patft.uspto.gov/netahtml/PTO/search-bool.html"
#     # browser = webdriver.Chrome(executable_path="C:/SeleniumDrivers/chromedriver.exe")
#
#     browser.get(url)
#     search_box = browser.find_element_by_id("trm1")
#     search_box.send_keys(Key)
#     search_box.submit()
#     try:
#         links = browser.find_elements_by_xpath("//tbody//td//a")
#     except:
#         links = browser.find_elements_by_xpath("//td//a")
#     results = []
#     for link in links:
#         href = link.get_attribute("href")
#         # print(href)
#         results.append(href)
#
#     num = browser.find_elements_by_xpath("/html/body/i/strong[3]")
#     name = browser.find_elements_by_xpath("/html/body/b")
#
#     print(name[0].text +" is " +num[0].text)
#
#     context = {
#         'key_search': name,
#     }
#
#     # browser.close()
#     return results
#
# def stemSentence(corpus):
#     porter = PorterStemmer()
#     token_words= word_tokenize(corpus)
#     token_words
#     stem_sentence=[]
#     for word in token_words:
#         stem_sentence.append(porter.stem(word))
#         stem_sentence.append(" ")
#     return "".join(stem_sentence)
#
#
# def f_dic(x):
#     with open('static/files/dict_unification.json') as infile:
#         data = json.load(infile)
#     return data[x]
#
# def f_dic_cpc(x):
#     with open('static/files/dict_CPC.json') as infile:
#         data = json.load(infile)
#     return data[x]
#
# def access_patent(lien):
#
#     urls = get_results(lien)
#     urls = list(dict.fromkeys(urls))
#     info_items = []
#     numberInv = []
#     code_inv = []
#     item ={}
#     item_all = {}
#     item_comp = {}
#     item_cpc = {}
#     codeInv = {}
#     item_inv_comp = {}
#     item_inv_cpc = {}
#     item_comp_domaine = {}
#     item_domaine_comp = {}
#
#     countPatent = 0
#     k = []
#     kk = []
#     k_inv = []
#     lis_dic_comp = []
#     lis_doc_inv_comp = []
#     lis_doc_inv_cpc = []
#     lis_dic_domaine_comp = []
#     lis_dic_comp_domaine = []
#
#     k_countries_cities = []
#     kk_countries = []
#     lis_dic_cpc = []
#     for url in urls[5:11]:
#         browser.get(url)
#         print("Scrapping : " + url)
#         try:
#
#
#             tit = browser.find_element_by_xpath("/html/body/font")
#             title = tit.text
#             print("Title : " + title)
#
#             c = browser.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]/ b")
#             code = c.text
#             print("Code : " + code)
#
#             y = browser.find_element_by_xpath("/html/body/table[4]/tbody/tr[3]/td[3]")
#             year = y.text
#             year1 = year[-4:]
#             year_int = int(year1)
#             print(year_int)
#
#             inventors = browser.find_elements_by_xpath("/html/body/table[3]/tbody/tr[1]/td")
#             inv = inventors[0].text
#             print("inventors : " + inv)
#             num_inventors = wordCount(inv) -1
#             print(num_inventors)
#             # numberInv.append(num_inventors)
#             #####
#             inventors_without_parentheses = re.sub(r'\([^)]*\)', '', inv)
#             print("##")
#             print(inventors_without_parentheses.split(","))
#             print("##")
#             k_inv.append(inventors_without_parentheses.split(","))
#             print(k_inv)
#             ######
#             ## origin company:
#             orig_comp = browser.find_elements_by_xpath("/html/body/table[3]/tbody/tr[2]/td/table/tbody/tr[2]/td[1]")
#             orig_comp = orig_comp[0].text
#             print("Origin Company:" + orig_comp)
#             ## buys company:
#             buy_comp = browser.find_elements_by_xpath("/html/body/table[3]/tbody/tr[3]/td/b")
#             buy_comp = buy_comp[0].text
#             print("Buys Company:" + buy_comp)
#
#             ########################################## RELATIONSHIPS ###############################################
#
#             #### % script inventeur company %####
#             ## Inventors:
#             inventors = browser.find_elements_by_xpath("/html/body/table[3]/tbody/tr[1]/td")
#             inventors = inventors[0].text
#             print(inventors)
#             #####
#             inventors_without_parentheses = re.sub(r'\([^)]*\)', '', inventors)
#             inventores = inventors_without_parentheses.split(",")
#             print("Inventors: ")
#             print(inventores)
#
#             ## Companies:
#             companies = browser.find_elements_by_xpath("/html/body/table[3]/tbody/tr[2]/td/table/tbody/tr[2]/td[1]")
#             companies = companies[0].text
#             print("Companies:")
#             print(companies)
#
#             item_inv_comp = {
#                 'source': inventores,
#                 'target': companies,
#             }
#             #### % END script inventeur comapny %####
#
#             #### % script inventeur CPC %####
#             ## Inventors:
#             inventors = browser.find_elements_by_xpath("/html/body/table[3]/tbody/tr[1]/td")
#             inventors = inventors[0].text
#             print(inventors)
#             #####
#             inventors_without_parentheses = re.sub(r'\([^)]*\)', '', inventors)
#             inventores = inventors_without_parentheses.split(",")
#             print("Inventors: ")
#             print(inventores)
#
#             ## Companies:
#             # cpc:
#             cpc_class = browser.find_elements_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]")
#             cpc_class = cpc_class[0].text
#             cpc_class = cpc_class[0:1]
#             print("cpc class : " + cpc_class)
#
#             item_inv_cpc = {
#                 'source': inventores,
#                 'target': f_dic_cpc(cpc_class),
#             }
#             #### % END script inventeur CPC %####
#
#             #### % script company - domaine %####
#             ## origin company:
#             orig_comp = browser.find_elements_by_xpath("/html/body/table[3]/tbody/tr[2]/td/table/tbody/tr[2]/td[1]")
#             orig_comp = orig_comp[0].text
#             print("Origin Company:" + orig_comp)
#             ## buys company:
#             buy_comp = browser.find_elements_by_xpath("/html/body/table[3]/tbody/tr[3]/td/b")
#             buy_comp = buy_comp[0].text
#             print("Buys Company:" + buy_comp)
#
#             # cpc:
#             cpc_class = browser.find_elements_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]")
#             cpc_class = cpc_class[0].text
#             cpc_class = cpc_class[0:1]
#             cpc_class = f_dic_cpc(cpc_class)
#             print("cpc class : " + cpc_class)
#
#             print("---------------------------------------------------------------------------------------")
#             item_comp_domaine = {
#                 'source': orig_comp.lower(),
#                 'target': cpc_class
#             }
#
#             item_domaine_comp = {
#                 'source': cpc_class,
#                 'target': orig_comp.lower()
#             }
#             #### % END script company - domaine %####
#
#             print("---------------------------------------------------------------------------------------")
#             item_comp = {
#                 'source': orig_comp.upper(),
#                 'target': buy_comp.lower()
#             }
#             ######
#
#             ## cities and our countries:
#             citiesANDcountries = browser.find_elements_by_xpath("/html/body/table[3]/tbody/tr[1]/td")
#             citiesANDcountries = citiesANDcountries[0].text
#             print("Origin Company:" + citiesANDcountries)
#
#             city_country = re.findall('\((.*?)\)', citiesANDcountries)
#             country = []
#             all_city_country = list(set(city_country))
#             print("list of cities and our countries : ")
#             print(all_city_country)
#             k_countries_cities.append(all_city_country)
#
#             ## countries complet name:
#             for i in range(len(all_city_country)):
#                 tx = all_city_country[i][-2:]
#                 country.append(f_dic(tx))
#             print("countries : ")
#             print(country)
#             kk_countries.append(country)
#             # kk.append(list(set(country)))
#             ####
#
#             # cpc:
#             cpc_class = browser.find_elements_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]")
#             cpc_class = cpc_class[0].text
#             cpc_class = cpc_class[0:1]
#             print("cpc class : " + cpc_class)
#
#             print("---------------------------------------------------------------------------------------")
#             item_cpc = {
#                 'cpc_class': cpc_class,
#             }
#
#             ########
#
#             abst = browser.find_element_by_xpath("/html/body/p[1]")
#             abstract = abst.text  # Abstract
#             # print("Abstract :" + abstract)
#
#
#
#
#
#             item_all = {
#                 'title': title,
#                 'code': code,
#                 'year': year_int,
#                 'inventors': inv,
#                 'num_inventors': num_inventors,
#                 'abstract': abstract,
#             }
#
#             codeInv = {
#                 'code': code,
#                 'num_inventors': num_inventors,
#             }
#
#             numberInv.append(num_inventors)
#
#             ## cities and our countries:
#             # citiesANDcountries = browser.find_elements_by_xpath("/html/body/table[3]/tbody/tr[1]/td")
#             # citiesANDcountries = citiesANDcountries[0].text
#             # # print("Origin Company:" + citiesANDcountries)
#             #
#             # city_country = re.findall('\((.*?)\)', citiesANDcountries)
#             # country = []
#             # all_city_country = list(set(city_country))
#             # # print("list of cities and our countries : ")
#             # print(all_city_country)
#             # k.append(all_city_country)
#             #
#             # ## countries complet name:
#             # for i in range(len(all_city_country)):
#             #     tx = all_city_country[i][-2:]
#             #     # country.append(f(tx))
#             #     country.append(tx)
#             # print("countries : ")
#             # print(country)
#             #
#             # countryD = list(set(country))
#             # # kk.append(countryD)
#             # for j in range(len(countryD)):
#             #     kk.append(countryD[j])
#             # # kk.append(list(set(country)))
#             # print("---------------------------------------------------------------------------------------")
#
#         except :
#             print("Erreur")
#         info_items.append(item_all)
#         lis_dic_comp.append(item_comp)
#         lis_doc_inv_comp.append(item_inv_comp)
#         lis_doc_inv_cpc.append(item_inv_cpc)
#         lis_dic_domaine_comp.append(item_domaine_comp)
#         lis_dic_comp_domaine.append(item_comp_domaine)
#
#         lis_dic_cpc.append(item_cpc)
#         code_inv.append(codeInv)
#
#         countPatent += 1
#
#         # print(kk)
#         # totalCountry = list(set(kk))
#         # print(totalCountry)
#         # sumCountries = len(totalCountry)
#         # print(sumCountries)
#
#     print("number of patents: %d " % countPatent)
#     sum_patents = {"a": countPatent}
#     sum_inventors = {"a": sum(numberInv)}
#     # print("number of countries: %d " % sumCountries)
#     # sum_countries = {"a": sumCountries}
#
#
#
#
#     with open('TestUsptoJson.json', 'w') as outfile:
#         json.dump(info_items, outfile)
#
#     with open('static/files/codeInv.json', 'w') as outfile:
#         json.dump(code_inv, outfile)
#
#     with open('static/files/sumInv.json', 'w') as outfile:
#         json.dump(sum_inventors, outfile)
#
#     with open('static/files/sumPatent.json', 'w') as outfile:
#         json.dump(sum_patents, outfile)
#
#     # with open('static/files/sumCountries.json', 'w') as outfile:
#     #     json.dump(sum_countries, outfile)
#
#     client = MongoClient('localhost', 27017)
#     db = client['testMongoDjango']
#     collection = db['poll']
#     with open('TestUsptoJson.json') as f:
#         file_data = json.load(f)
#     collection.insert(file_data)
#
#
#     cursor = collection.find({})
#     data = []
#     for document in cursor:
#         yr = document['year']
#         data.append(yr)
#     client.close()
#     liste = data
#     print(liste)
#     # browser.close()
#     countYearsJson = []
#     compte = {}.fromkeys(set(liste), 0)
#     for valeur in liste:
#         compte[valeur] += 1
#     for key, value in compte.items():
#
#         years_item = {
#             'year': key,
#             'count': value,
#         }
#         countYearsJson.append(years_item)
#
#     with open('static/files/year.json', 'w') as outfile:
#         json.dump(countYearsJson, outfile)
#
#     ####################################################################################################################
#
#     with open('TestUsptoJson.json') as f:
#         documents = json.load(f)
#     # print(documents[1]['title'])
#     list_title = []
#     list_lem = []
#     i=0
#     while i < len(documents):
#         titAbs = documents[i]['title'] + " "+documents[i]['abstract']
#         list_title.append(titAbs)
#         # list_title.append(documents[1]['title']+" "+documents[1]['abstract'])
#         stem = stemSentence(list_title[i])
#         list_lem.append(stem)
#         i += 1
#     print("########### Normal list ###########")
#     # print(list_title)
#     print("########### stem list ###########")
#     # print(list_lem)
#     f = open("corpus.txt", "w")
#     f.write(''.join(list_lem))
#
#
#
#
#     print("########### doc term matrix ###########")
#     vectorizer = TfidfVectorizer(stop_words='english')
#     data = vectorizer.fit_transform(list_lem)
#     true_k = 5
#     clustering_model = KMeans(n_clusters=true_k,
#                               init='k-means++',
#                               max_iter=300, n_init=5)
#     clustering_model.fit(data)
#
#     print("Top terms per cluster:")
#
#     sorted_centroids = clustering_model.cluster_centers_.argsort()[:, ::-1]
#     terms = vectorizer.get_feature_names()
#
#     label = []
#     labels = []
#     for i in range(true_k):
#         print("Cluster %d:" % i, end='')
#         for ind in sorted_centroids[i, :5]:
#             print(' %s' % terms[ind], end='')
#             label.append(terms[ind])
#
#         print()
#         print()
#
#     labels.append(' '.join(label[:3]))
#     labels.append(' '.join(label[3:6]))
#     labels.append(' '.join(label[6:9]))
#     labels.append(' '.join(label[9:12]))
#     labels.append(' '.join(label[12:15]))
#     print(labels)
#
#     print()
#     print("Predictions of new documents")
#     Y = vectorizer.transform(list_lem)
#     prediction = clustering_model.predict(Y)
#
#     #######################################################################################################################
#     liste = np.array(prediction).tolist()
#     compte = {}.fromkeys(set(liste), 0)
#     for valeur in liste:
#         compte[valeur] += 1
#
#     countCkusters = []
#     for key, value in compte.items():
#         if key == 0:
#             key = labels[:1]
#         if key == 1:
#             key = labels[1:2]
#         if key == 2:
#             key = labels[2:3]
#         if key == 3:
#             key = labels[3:4]
#         if key == 4:
#             key = labels[4:5]
#         clusetrs_item = {
#             'cluster': key,
#             'count': value,
#         }
#         countCkusters.append(clusetrs_item)
#
#     with open('static/files/clustering1.json', 'w') as outfile:
#         json.dump(countCkusters, outfile)
#
#     ####################################################################################################################
#
#     file = open("static/files/corpus.txt", 'w')
#     file.write(''.join(list_lem))
#     #######
#     f = open("corpus.txt", "r")
#     text = f.read()
#     print("**************************************************Corpus***************************************************")
#     print(text)
#     ########################################################/* inventeurs treatements ############################################################
#
#     with open('all_inventors.json', 'w') as outfile:
#         json.dump(k_inv, outfile)
#
#     with codecs.open("all_inventors.json", 'r', 'utf8') as data_file:
#         data = json.load(data_file)
#     print(data)
#
#     l = data
#     k_inv = []
#     for index, value in enumerate(l):
#         longuer = len(value) - 1
#         for i, j in enumerate(value):
#             item = {
#                 'name': j,
#                 'size': longuer
#             }
#             k_inv.append(item)
#     # print(k)
#     # print("\n")
#
#     listIndex = []
#     listValues = []
#     for i in range(len(k)):
#         listValues.append(k_inv[i]['name'])
#         listIndex.append(k_inv[i]['size'])
#     # print(listValues)
#     # print(listIndex)
#
#     duplicated = [item for item, count in collections.Counter(listValues).items() if count > 1]
#     # print(duplicated)
#
#     findSize = []
#     for j in duplicated:
#         # print(j)
#         to_find = j
#         count = 0
#         for i in range(len(l)):
#             if to_find in l[i]:
#                 # print(i, len(l[i])-1)
#                 count = count + (len(l[i]) - 1)
#
#         itemSize = {
#             "name": to_find,
#             "size": count,
#         }
#         findSize.append(itemSize)
#     # print(findSize)
#
#     nVListValues = []
#     for i in range(len(findSize)):
#         nVListValues.append(findSize[i]['name'])
#     # print(nVListValues)
#
#     r = []
#     for i in k_inv:
#         # print(i['source'])
#         j = i['name']
#         k = i['size']
#         if j not in nVListValues:
#             item1 = {
#                 'name': j,
#                 'size': k
#             }
#             r.append(item1)
#     # print(r)
#
#     result = findSize + r
#     print("***Name_Size DATA:***")
#     print(result)
#     with open('static/files/name_size_inventors.json', 'w') as outfile:
#         json.dump(result, outfile)
#     print("\n")
#
#     liste = []
#     for index, value in enumerate(l):
#         # print(value)
#         A = value
#         for i in range(len(A) - 1):
#             j = i + 1
#             while (j < len(A)):
#                 item = {
#                     'source': A[i],
#                     'target': A[j]
#                 }
#                 liste.append(item)
#                 j = j + 1
#     print("***Source_Target DATA:***")
#     print(liste)
#
#     with open('static/files/source_target_inventors.json', 'w') as outfile:
#         json.dump(liste, outfile)
#     ########################################################/* END inventeurs treatements ############################################################
#
#     ########################################################/* companies treatements ############################################################
#     print(lis_dic_comp)
#     with open('static/files/source_target_companies.json', 'w') as outfile:
#         json.dump(lis_dic_comp, outfile)
#
#     with open('static/files/source_target_companies.json') as infile:
#         data = json.load(infile)
#
#     print(data)
#
#     list1 = []
#     for i in data:
#         # print(i['source'])
#         j = i['source']
#         k = i['target']
#         # print(j)
#         # print(k)
#         list1.append(j)
#         list1.append(k)
#     # print(list1)
#
#     j = 0
#     list2 = []
#     while (j < len(list1)):
#         k = j + 1
#         patent = [list1[j] + "", "" + list1[k]]
#         list2.append(patent)
#         j = j + 2
#     # print(list2)
#
#     l = list2
#
#     k_comp = []
#     for index, value in enumerate(l):
#         longuer = len(value) - 1
#         for i, j in enumerate(value):
#             item = {
#                 'name': j,
#                 'size': longuer
#             }
#             k_comp.append(item)
#     # print(k)
#     # print("\n")
#
#     listIndex = []
#     listValues = []
#     for i in range(len(k_comp)):
#         listValues.append(k_comp[i]['name'])
#         listIndex.append(k_comp[i]['size'])
#     # print(listValues)
#     # print(listIndex)
#
#     duplicated = [item for item, count in collections.Counter(listValues).items() if count > 1]
#     # print(duplicated)
#
#     findSize = []
#     for j in duplicated:
#         # print(j)
#         to_find = j
#         count = 0
#         for i in range(len(l)):
#             if to_find in l[i]:
#                 # print(i, len(l[i])-1)
#                 count = count + (len(l[i]) - 1)
#
#         itemSize = {
#             "name": to_find,
#             "size": count,
#         }
#         findSize.append(itemSize)
#     # print(findSize)
#
#     nVListValues = []
#     for i in range(len(findSize)):
#         nVListValues.append(findSize[i]['name'])
#     # print(nVListValues)
#
#     r = []
#     for i in k_comp:
#         # print(i['source'])
#         j = i['name']
#         k = i['size']
#         if j not in nVListValues:
#             item1 = {
#                 'name': j,
#                 'size': k
#             }
#             r.append(item1)
#     # print(r)
#
#     result = findSize + r
#     print("***Name_Size DATA:***")
#     print(result)
#     with open('static/files/name_size_companies.json', 'w') as outfile:
#         json.dump(result, outfile)
#     ########################################################/* END companies treatements ############################################################
#
#     ########################################################/* countries treatements ############################################################
#         with open('static/files/all_countriesANDcities.json', 'w') as outfile:
#             json.dump(k_countries_cities, outfile)
#         with open('static/files/all_countries.json', 'w') as outfile:
#             json.dump(kk_countries, outfile)
#
#         with codecs.open("static/files/all_countriesANDcities.json", 'r', 'utf8') as data_file:
#             data = json.load(data_file)
#         # with codecs.open("all_countries.json", 'r', 'utf8') as data_file:
#         #      data = json.load(data_file)
#         print(data)
#
#         l = data
#         k = []
#         for index, value in enumerate(l):
#             longuer = len(value) - 1
#             for i, j in enumerate(value):
#                 item = {
#                     'name': j,
#                     'size': longuer
#                 }
#                 k.append(item)
#         # print(k)
#         # print("\n")
#
#         listIndex = []
#         listValues = []
#         for i in range(len(k)):
#             listValues.append(k[i]['name'])
#             listIndex.append(k[i]['size'])
#         # print(listValues)
#         # print(listIndex)
#
#         duplicated = [item for item, count in collections.Counter(listValues).items() if count > 1]
#         # print(duplicated)
#
#         findSize = []
#         for j in duplicated:
#             # print(j)
#             to_find = j
#             count = 0
#             for i in range(len(l)):
#                 if to_find in l[i]:
#                     # print(i, len(l[i])-1)
#                     count = count + (len(l[i]) - 1)
#
#             itemSize = {
#                 "name": to_find,
#                 "size": count,
#             }
#             findSize.append(itemSize)
#         # print(findSize)
#
#         nVListValues = []
#         for i in range(len(findSize)):
#             nVListValues.append(findSize[i]['name'])
#         # print(nVListValues)
#
#         r = []
#         for i in k:
#             # print(i['source'])
#             j = i['name']
#             k = i['size']
#             if j not in nVListValues:
#                 item1 = {
#                     'name': j,
#                     'size': k
#                 }
#                 r.append(item1)
#         # print(r)
#
#         result = findSize + r
#         print("***Name_Size DATA:***")
#         print(result)
#         with open('static/files/name_size_countries.json', 'w') as outfile:
#             json.dump(result, outfile)
#
#         print("\n")
#
#         liste = []
#         for index, value in enumerate(l):
#             # print(value)
#             A = value
#             for i in range(len(A) - 1):
#                 j = i + 1
#                 while (j < len(A)):
#                     item = {
#                         'source': A[i],
#                         'target': A[j]
#                     }
#                     liste.append(item)
#                     j = j + 1
#         print("***Source_Target DATA:***")
#         print(liste)
#
#         with open('static/files/source_target_countries.json', 'w') as outfile:
#             json.dump(liste, outfile)
#     ########################################################/* END countries treatements ############################################################
#
#     ########################################################/* cpc treatements ############################################################
#     print(lis_dic_cpc)
#     with open('static/files/cpc_class.json', 'w') as outfile:
#         json.dump(lis_dic_cpc, outfile)
#
#     with open('static/files/cpc_class.json') as infile:
#         data = json.load(infile)
#
#     # print(data)
#
#     list1 = []
#     cpc = []
#     for i in data:
#         j = i['cpc_class']
#         list1.append(j)
#     print(list1)
#
#     for i in range(len(list1)):
#         # print(double_city_country[i][-2:])
#         tx = list1[i]
#         cpc.append(f_dic_cpc(tx))
#     print(cpc)
#     with open('static/files/cpc_class-all_name.json', 'w') as outfile:
#         json.dump(cpc, outfile)
#
#     with open('static/files/cpc_class-all_name.json') as infile:
#         liste = json.load(infile)
#
#     nv_list = list(set(liste))
#     item1 = {}
#     liste2 = []
#     i = 0
#     while (i < len(nv_list)):
#         item1 = {
#             'id': nv_list[i],
#             'Domaine': i + 4,
#             'Frequence': liste.count(nv_list[i])
#         }
#         liste2.append(item1)
#         i = i + 1
#     print(liste2)
#     with open('static/files/data_cpc.json', 'w') as outfile:
#         json.dump(liste2, outfile)
#     ########################################################/* END cpc treatements ############################################################
#
#     ########################################################/* inventeur/company treatements ##################################################
#
#         l = lis_doc_inv_comp
#         liste = []
#         for i in l:
#             for cle, value in i.items():
#                 for j in i.get('source'):
#                     item = {
#                         'source': j,
#                         'target': i.get('target')
#                     }
#                     liste.append(item)
#                 break
#
#         print(liste)
#
#         liste2 = []
#         for i in l:
#             for cle, value in i.items():
#                 for j in i.get('source'):
#                     item = {
#                         'source': i.get('target'),
#                         'target': j
#                     }
#                     liste2.append(item)
#                 break
#
#         print(liste2)
#
#
#     with open('static/files/inventors_companies.json', 'w') as outfile:
#         json.dump(liste, outfile)
#     with open('static/files/companies_inventors.json', 'w') as outfile:
#         json.dump(liste2, outfile)
#     ########################################################/* END inventeur/company treatements ##############################################
#
#     ########################################################/* inventeur/cpc treatements ##############################################
#
#         print(lis_doc_inv_cpc)
#         l = lis_doc_inv_cpc
#         liste = []
#         for i in l:
#             for cle, value in i.items():
#                 for j in i.get('source'):
#                     item = {
#                         'source': j,
#                         'target': i.get('target')
#                     }
#                     liste.append(item)
#                 break
#
#         print(liste)
#
#         liste2 = []
#         for i in l:
#             for cle, value in i.items():
#                 for j in i.get('source'):
#                     item = {
#                         'source': i.get('target'),
#                         'target': j
#                     }
#                     liste2.append(item)
#                 break
#
#         print(liste2)
#
#     with open('static/files/inventors_cpc.json', 'w') as outfile:
#         json.dump(liste, outfile)
#     with open('static/files/cpc_inventors.json', 'w') as outfile:
#         json.dump(liste2, outfile)
#     ########################################################/* END inventeur/cpc treatements ##########################################
#
#     ########################################################/* company/domaine treatements ##########################################
#
#     print(lis_dic_domaine_comp)
#     print(lis_dic_comp_domaine)
#     with open('static/files/domaine_companies.json', 'w') as outfile:
#         json.dump(lis_dic_domaine_comp, outfile)
#     with open('static/files/companies_domaine.json', 'w') as outfile:
#         json.dump(lis_dic_comp_domaine, outfile)
#
#     with open('static/files/domaine_companies.json') as infile:
#         data = json.load(infile)
#
#     print(data)
#
#     list1 = []
#     for i in data:
#         # print(i['source'])
#         j = i['source']
#         k = i['target']
#         # print(j)
#         # print(k)
#         list1.append(j)
#         list1.append(k)
#     # print(list1)
#
#     j = 0
#     list2 = []
#     while (j < len(list1)):
#         k = j + 1
#         patent = [list1[j] + "", "" + list1[k]]
#         list2.append(patent)
#         j = j + 2
#     # print(list2)
#
#     l = list2
#
#     k = []
#     for index, value in enumerate(l):
#         longuer = len(value) - 1
#         for i, j in enumerate(value):
#             item = {
#                 'name': j,
#                 'size': longuer
#             }
#             k.append(item)
#     # print(k)
#     # print("\n")
#
#     ###############################################################################################################
#
#     listIndex = []
#     listValues = []
#     for i in range(len(k)):
#         listValues.append(k[i]['name'])
#         listIndex.append(k[i]['size'])
#     # print(listValues)
#     # print(listIndex)
#
#     duplicated = [item for item, count in collections.Counter(listValues).items() if count > 1]
#     # print(duplicated)
#
#     findSize = []
#     for j in duplicated:
#         # print(j)
#         to_find = j
#         count = 0
#         for i in range(len(l)):
#             if to_find in l[i]:
#                 # print(i, len(l[i])-1)
#                 count = count + (len(l[i]) - 1)
#
#         itemSize = {
#             "name": to_find,
#             "size": count,
#         }
#         findSize.append(itemSize)
#     # print(findSize)
#
#     ###############################################################################################################
#
#     nVListValues = []
#     for i in range(len(findSize)):
#         nVListValues.append(findSize[i]['name'])
#     # print(nVListValues)
#
#     r = []
#     for i in k:
#         # print(i['source'])
#         j = i['name']
#         k = i['size']
#         if j not in nVListValues:
#             item1 = {
#                 'name': j,
#                 'size': k
#             }
#             r.append(item1)
#     # print(r)
#
#     result = findSize + r
#     print("***Name_Size DATA:***")
#     print(result)
#     with open('static/files/domaine_size_companies.json', 'w') as outfile:
#         json.dump(result, outfile)
#     ########################################################/* END company/domaine treatements ##########################################
#
#
#     browser.close()
#
def getfiles(request):
    dataset = request.GET.get('search')
    filenames = glob.glob("TestUsptoJson.json")

    zip_subdir = "results"
    zip_filename = "%s.zip" % zip_subdir

    s =io.BytesIO()

    zf = zipfile.ZipFile(s, "w")

    for file in filenames:
        fdir, fname = os.path.split(file)
        zip_path = os.path.join(zip_subdir, fname)

        zf.write(file, zip_path)
    zf.close()

    resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

    return resp
#
# def searchUspto(request):
#
#
#
#     if 'search' in request.GET:
#         search_string = request.GET['search']
#     context = {
#             "search_string": search_string
#     }
#     # redirection = get_results(search_string)
#     if not search_string:
#         return render(request, 'users/search.html', context)
#     else:
#         # get_results(search_string)
#         access_patent(search_string)
#         return render(request, 'users/search.html', context)
#
#
#
