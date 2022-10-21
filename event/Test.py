# {% extends 'main.html' %}
#
# {% block title %}Create new event{% endblock %}
#
# {% block content %}
#
#   <form method="post" action="" enctype="multipart/form-data"> <!-- TODO new_event -->
#   <table>
#     {% csrf_token %}
#     <tr>
#       <td><label for="name">Name:</label> </td>
#       <td><input class ="cei" type="text" name="name" id="name"></td>
#     </tr>
#     <label for = "category">Category:</label>
#     <select class ="cei" id="category" name="category">
#     {% for category in categories %}
#       <option value="{{ category.id }}">{{ category.name }}</option>
#     {% endfor %}
#     </select><br>
#     <label for="typeonline">Type online:</label>
#     <input class ="cei" type="Checkbox" name="typeonline" id="typeonline"> <br>
#     <label for="typefysical">Type fysical:</label>
#     <input class ="cei" type="Checkbox" name="typefysical" id="typefysical"> <br>
#     <label for="location">Location:</label>
#     <input class ="cei" type="text" name="location" id="location"> <br>
#     <label for="startdatetime">Date from:</label>
#     <input class ="cei" type="datetime-local" name="startdatetime" id="startdatetime"> <br>
#     <label for="enddatetime">Date till:</label>
#     <input class ="cei" type="datetime-local" name="enddatetime" id="enddatetime"> <br>
#     <label for="name">Organizer:</label>
#     <input class ="cei" type="organizer" name="organizer" id="organizer"> <br>
#     <label for="name">Photo:</label>
#     <input class ="cei" type="file" name="upload" accept="*">
#     <label for="descr">Description:</label>
#     <input class ="cei" type="text" name="descr" id="descr"> <br>
#     <button type="submit">Create</button>
#   </table>
#   </form>
#
# {% endblock %}