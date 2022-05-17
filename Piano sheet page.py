from os import system

system('echo off\nchcp 65001\ndir /b /a-d E:\\文件\\ACG\\piano > file_name.txt') # change the file location of the sheet here
file_name = open("file_name.txt", encoding = 'utf-8')
name_in_array = []

def output(b):
    print("    <tr>")
    print("        <td> "+ b +" </td>")
    print("        <td> <a href='downloading_resources/"+b+".pdf'>"+b+".pdf"+"</a> </td>")
    print("    </tr>\n")

def classify(array, type):
    print('''<table style="width: 100%;">
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
            if h3 == False:
                print(f"    <h3>{type}</h3>")
                h3 = True
            output(a)
    print('</table>')

for a in file_name:
    a = a.replace('\n', '')
    a = a.replace('.pdf', '')
    name_in_array.append(a)


classify(name_in_array, "OP")
    
classify(name_in_array, "ED")

print('''<table style="width: 100%;">
    <colgroup>
       <col span="1" style="width: 300px;">
    </colgroup>
	<tbody>
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
