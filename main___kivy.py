import pandas
import itertools
import statistics
import math
import functools
#try:
text1=input()
num1=list(map(int,text1.split(' ')))
class prossedData:
        lowToHigh_=sorted(num1)
        highToLow=lowToHigh_.reverse()
        size_=len(num1)
        min_=lowToHigh_[0]
        max_=lowToHigh_[size_-1]
        minIndex_=lowToHigh_.index(min_)
        maxIndex_=lowToHigh_.index(max_)
        mean_=statistics.mean(num1)
        median_=statistics.median(num1)
        gcd_=functools.reduce(math.gcd,lowToHigh_)
        lcm_=functools.reduce(lambda a, b: a * b // math.gcd(a, b), num1)
        prefixSum_=itertools.accumulate(num1)
        def maxPlus_GAPMAKER_(size_):
                dif_min,dif_max,dif=0,0,0
                if(size_>2):
                        dif_min=abs(num1[0]-num1[1])
                gap=str(num1[0])
                for i in range(1,size_):
                        dif=abs(num1[i-1]-num1[i])
                        dif_max=max(dif,dif_max)
                        dif_min=min(dif_min,dif)
                        gap+=" "*dif+str(num1[i])
                return gap,dif_max,dif_min
        gapStringWithSpace_,maxGap_,minGap_= maxPlus_GAPMAKER_(size_)
        binary_=[bin(int(i))[2:] for i in num1]
        octa_=[oct(int(i))[2:] for i in num1]
        hex_=[hex(int(i))[2:] for i in num1]

        #smartGap_=
data=prossedData()
print("Sorted: ")
print(*data.lowToHigh_)
print("Prefix Sum: ")
print(*data.prefixSum_)
print("Maximum Gap: ")
print(data.maxGap_)
print("Minimum Gap: ")
print(data.minGap_)
print("Gap String: ")
print(data.gapStringWithSpace_)
print("Binery")
print(*data.binary_)
#except:
print("String Yet not supported")















# import kivy
# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput
# from kivy.animation import Animation
# from kivy.properties import ObjectProperty
# from kivy.uix.widget import Widget
#
# class MyGrid(Widget):
#     email=ObjectProperty(None)
#     password=ObjectProperty(None)
#     def pressed(self):
#         print(self.email.text+self.password.text)
#         if self.password.text == "admin":
#             print("logged in")
#             pass
#         else:
#             self.password.text = ""
#
#
# class BooApp(App):
#     def build(self):
#         return MyGrid()
#
# if __name__ == "__main__":
#     BooApp().run()