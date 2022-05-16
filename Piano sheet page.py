file_name = open("file_name.txt", encoding='UTF-8')
lines = file_name.readline()

for a in file_name:
    a = a.replace('\n', '')
    a = a.replace('.pdf', '')
    print("    <tr>")
    print("        <td> "+ a +" </td>")
    print("        <td> <a href='downloading_resources/"+a+".pdf'>"+a+".pdf"+"</a> </td>")
    print("    </tr>\n")

input("\n\n\n\npress Enter to continue")
