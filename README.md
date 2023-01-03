# Oil Price Data Process (in Python)

[Raw data](https://github.com/msnoshain/OilPrice-DataProcess/blob/master/PythonDataProcess/Tables/raw.xls) is daily oil price from 2017.10.24 to 2022.10.24 with some loss in some days. Here are steps to process the data:


![image](https://user-images.githubusercontent.com/85274323/210332838-5dd43284-4318-402b-9c8e-071860b23aa9.png)
<br>

## 1.Interpolate data with cubic
Interpolate data using scipy.interpolate package with cubic. See code [here](https://github.com/msnoshain/OilPrice-DataProcess/blob/master/PythonDataProcess/1.PriceInterPld.py). See output file [here](https://github.com/msnoshain/OilPrice-DataProcess/blob/master/PythonDataProcess/Tables/final.xls).

![image](https://user-images.githubusercontent.com/85274323/210333744-c3458a03-6365-4541-ac41-31a8efee11c7.png)
<br>

## 2.Get titles and detailed page links of all the News from 2017.10.24 to 2022.10.24
Get HTML contents from [OilPrice](https://oilprice.com/Energy/Oil-Prices/Page-2.html) by requests package and parse HTML by BeautifulSoup 4. Use pandas to export .xls files. See code [here](https://github.com/msnoshain/OilPrice-DataProcess/blob/master/PythonDataProcess/2.GetNewsLink.py). See output file [here](https://github.com/msnoshain/OilPrice-DataProcess/blob/master/PythonDataProcess/Tables/title_n_link.xls).

![image](https://user-images.githubusercontent.com/85274323/210334070-4adb9774-e085-4921-a86e-d86abe1a57c5.png)
<br>

## 3.Get contents of all the links
Get all the news contens and save each as a single file in /News, which named [index].txt. See code [here](https://github.com/msnoshain/OilPrice-DataProcess/blob/master/PythonDataProcess/3.GetNewsContent.py). See output files [here](https://github.com/msnoshain/OilPrice-DataProcess/tree/master/PythonDataProcess/News).

![image](https://user-images.githubusercontent.com/85274323/210333961-c86dbeba-5aad-4864-82b5-96a2b611652b.png)
<br>

## 4.Clean the data
Clean the text. Replace all the characters that are not lowercase letters with space. Split texts with space and trim space of each word. See code [here](https://github.com/msnoshain/OilPrice-DataProcess/blob/master/PythonDataProcess/4.Statistic.py).

## 5.Word frequecy calculation
Calculate each word's frequecy of each day. Export to .csv file. See code [here](https://github.com/msnoshain/OilPrice-DataProcess/blob/master/PythonDataProcess/4.Statistic.py). See output file [here](https://github.com/msnoshain/OilPrice-DataProcess/blob/master/PythonDataProcess/Tables/statistics_unsorted.csv).

![image](https://user-images.githubusercontent.com/85274323/210334822-1acad288-05fc-456f-a576-38e8b3da41c7.png)
<br>

## 6.Sort columns by words
Sort columns by words. See code [here](https://github.com/msnoshain/OilPrice-DataProcess/blob/master/PythonDataProcess/5.sort.py). See output file [here](https://github.com/msnoshain/OilPrice-DataProcess/blob/master/PythonDataProcess/Tables/statistics_sorted.csv).

![image](https://user-images.githubusercontent.com/85274323/210334602-3bb61f98-4a7e-4534-96c2-949bd7dc6508.png)
<br>
