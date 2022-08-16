from os import system

system('chcp 65001')
system('cls')
system('dir /b /a-d "E:\\文件\\ACG\\piano" > file_name.txt') # change the file location of the sheet here
file_name = open("file_name.txt", encoding = 'utf-8')
name_in_array = []

def output(b):
    print("    <tr>")
    print("        <td> "+ b +" </td>")
    print("        <td> <a href='downloading_resources/"+b+".pdf'>"+b+".pdf"+"</a> </td>")
    print("    </tr>\n")

def classify(array, type):
    print(f'''<h3>{type}</h3>
<table style="width: 100%;">
    <colgroup>
       <col span="1" style="width: 300px;">
    </colgroup>
	<tbody>
		<tr>
			<th>Discription</th>
			<th>Download</th>
		</tr>''')
    h3=False
    for a in array:
        if a.find(type) != -1:
            output(a)
    print('</table>')

for a in file_name:
    a = a.replace('\n', '')
    a = a.replace('.pdf', '')
    name_in_array.append(a)

print('''<html>

<head>
  <link rel="stylesheet" href="../../main.css">
  <title>Piano Sheet</title>
  <link rel="icon" href = "../../black.png" type = "image/x-icon" style="border-radius:50%">
  <h1>Piano Sheet</h1>
</head>

<meta charset="utf-8">

<ul class="navigation">
	<li class="navigation"><a class = 'navigation' href='../../index.html'>Home</a></li>
    <li class="navigation"><a class = 'navigation' href='../../page/Program_backup/index.html'>Programming Sandbox</a></li>
	<li class="navigation"><a class = 'navigation' href='../../page/BAFS/index.html'>BAFS Lesson Resource</a></li>
	<li class="navigation"><a class = 'navigation' href='../../page/old_resources/index.html'>Old resource download</a></li>
</ul>

 <h2>HalcyonMusic  <a href="https://www.youtube.com/c/HalcyonMusic"><img src="Youtube.png" alt="youtube icon" width="50" height="50" style="margin-bottom:-12px"></a></h2> 
''')

classify(name_in_array, "OP")
    
classify(name_in_array, "ED")

print('''<h3>Other</h3>
<table style="width: 100%;">
    <colgroup>
       <col span="1" style="width: 300px;">
    </colgroup>
		<tr>
			<th>Discription</th>
			<th>Download</th>
		</tr>''')
h3=False
for a in name_in_array:
    a = a.replace('\n', '')
    a = a.replace('.pdf', '')
    if a.find("OP") == -1 and a.find("ED") == -1:
        if h3 == False:
            print(f"    <h3>Other</h3>")
            h3 = True
        output(a)
print('</table>')

input()
