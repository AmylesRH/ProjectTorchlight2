contenttype = mycursor.execute("Select contenttype_facet from WebBehavior”)
result = mycursor.fetchall

contenttype = []
# Marks = []

for i in mycursor:
    contenttype.append(i[0])
# Marks.append(i[1])

# plt.bar(Names, Marks)
# plt.ylim(0, 5)
# plt.xlabel("Name of Students”)
# plt.ylabel("Marks of Students”)
# plt.title("Student's Information”)
# plt.show()

plt.pie(contenttype)
mylabels = ['troubleshooting', 'migration', 'installation', 'administration', 'development']  # fix this line
r = plt.pie(metadata_counts, labels=mylabels, autopct='%.0f%%')  # fix this line
plt.title('Resources by Content Type’)
plt.show()
