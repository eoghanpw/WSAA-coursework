from studentdao import studentDAO

studentDAO.create(("Mary", 21))
studentDAO.update(("John", 33, 5))
studentDAO.delete(7)
print(studentDAO.get_all())
print(studentDAO.get_by_id(5))
