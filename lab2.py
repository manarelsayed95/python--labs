import MySQLdb
import re;


# "def of class person"

class person():
	"""docstring for ClassName"""
	def __init__(self, full_name, money):
		
		self.full_name= full_name
		self.money=money
	'''
	sleep method is used for calculate the sleepmood value
	'''
	def sleep(self,hours):
		if(hours==7):
			self.sleepmood="happy"
		elif(hours<7):
			self.sleepmood="tired"
		else:
			self.sleepmood="lazy"
		return self.sleepmood

	'''
	eat method is used for calculate the healthRate value
	'''

	def eat(self,meals):
		if (meals==3):
			self.healthRate=100
		if (meals==2):
			self.healthRate=75
		if (meals==1):
			self.healthRate=50
		return self.healthRate
	def buy(self,items):
		if (items==0):
			pass
		else:
			for value in range(1,items,1):
				self.money-=10

# def of class Employee
class Employee(person):
		def __init__(self,id,full_name, money,email,salary,is_manager):

			super().__init__(full_name, money)
			
			self.id=id
			self.email=email
			self.salary=salary
			self.is_manager=is_manager


		'''
		work method is used for calculate the workmood value
		'''
		def work(self,hours):
			if hours==8:
				self.workmood="happy"
			if hours>8:
				self.workmood="tired"
			if hours<8:
				self.workmood="lazy"
			return self.workmood

		def sendemail(self,to ,subject , body , receiver_name):
			my_file = open('email.txt', 'a')
			my_file.write(" to: ")
			my_file.write(to)
			my_file.write(" subject: ")
			my_file.write(subject)
			my_file.write(body)
			my_file.write(receiver_name)

			my_file.close()

# def of class office : "it hass all methods of sql_queries"
class office():
	def __init__(self,name):
		self.name=name

	def get_all_employees(self):
		try:
			db = MySQLdb.connect("localhost", 'root', '', 'office')
			cursor =db.cursor()
			sql_str= 'select * from employees';
			cursor.execute(sql_str)
			results = cursor.fetchall()

			for result in results:
				print ( 'id',result[0] ) #id
				print ( 'full_name',result[1] ) #fullname
				print ( 'money',result[2] ) #money
				print ( 'sleep_mood',result[3] ) #sleepmood
				print ( 'health_rate',result[4] ) #healthrate
				print ( 'email',result[5] ) #email
				print ( 'work_mood',result[6] ) #work_mood
				print ( 'salary',result[7] ) #salary
				print ( 'ismanage',result[8] ) #is_manage
				print('')
		except Exception as e:
			print("Couldnnot retrieve",e)
		finally:
			db.close()

	def get_employee(self , empId):
		self.empId=empId
		try:
			db = MySQLdb.connect("localhost", 'root', '', 'office')
			cursor =db.cursor()
			sql_str= 'select * from employees where id= %s';
			# print('sql', sql_str)
			cursor.execute(sql_str,(self.empId,))

			results = cursor.fetchone()

			
			print ( 'id',results[0] ) #id
			print ( 'full_name',results[1] ) #fullname
			print ( 'money',results[2] ) #money
			print ( 'sleep_mood',results[3] ) #sleepmood
			print ( 'health_rate',results[4] ) #healthrate
			print ( 'email',results[5] ) #email
			print ( 'work_mood',results[6] ) #work_mood
			print ( 'salary',results[7] ) #salary
			print ( 'ismanage',results[8] ) #is_manage

		except Exception as e:
			print("Couldnnot retrieve",e)
		finally:
			db.close()

	def hire(self,employee,hours,hour,meal):
			self.hours=hours
			self.hour=hour
			self.meal=meal
			self.employee=employee

			self.slmood=employee.sleep(self.hours)
			# print(self.slmood)
			self.hrate=employee.eat(self.meal)
			self.wmood=employee.work(self.hour)

			# print('hire called')
			# print(employee)

			try:
				conn = MySQLdb.connect("localhost", 'root', '', 'office')
				crsr = conn.cursor()
		
				sql = "insert into employees values({},'{}',{},'{}',{},'{}','{}',{},'{}')".format(employee.id,employee.full_name,employee.money,self.slmood,self.hrate,employee.email,self.wmood,employee.salary,employee.is_manager);
				# print('sql', sql)
				crsr.execute(sql)
				conn.commit()
			except Exception as e:
			 	print("Couldnnot insert", e)
			else:
			 	print("Inserted !")
			finally:
				conn.close()
		 	

	def fire(self ,empId):
		self.empId=empId
		try:
			db = MySQLdb.connect("localhost", 'root', '', 'office')
			cursor =db.cursor()
			sql_str= 'delete from employees where id= %s';
			cursor.execute(sql_str,(self.empId,))
			db.commit()
		except Exception as e:
			print("Couldnnot delete", e)
		finally:
			db.close()


# user_interface
def user(Number):
	if(Number.isdigit()):
		if(Number=='1'):


			db = MySQLdb.connect("localhost", 'root', '', 'office')
			cursor =db.cursor()
			sql_str= 'select max(id) from employees';
			# print('sql', sql_str)
			cursor.execute(sql_str)

			result = cursor.fetchone()
			print('please know that there is ',result,'employees in database')
			db.close()

			print('')

			print('please know that  the data in the employee table is:')
			print('1-full_name ')
			print('2- money')
			print('3-sleep_mood --> hours')
			print('4-healthrate --> meals')
			print('5-email --> name_ex@ex.ex')
			print('6-work_mood --> hour')
			print('7-salary')
			print('8-ismanage --> false or true')
			
			name=input('enter the number of your office:  ')
			first_office=office(name)

			no=int(input('enter the number of employees:  '))

			for value in range (0,no,1):
				Id=int(input('enter id:  '))
				fullname=input('enter fullname:  ')
				money=int(input('enter money:  '))
				salary=int(input('enter salary:  '))
				email=input('enter email:  ')
				is_manager=input('enter if he is manager or not: ')
				meal=int(input('enter no of meals:  '))
				hours=int(input('enter no of sleeping: '))
				hour=int(input('enter no of working:  '))


				employee=Employee(Id,fullname,money,email,salary,is_manager)
				
				first_office.hire(employee,hours,hour,meal)

		if(Number=='2'):
				name=input('enter the number of your office:  ')
				first_office=office(name)
				first_office.get_all_employees()

		if(Number=='3'):

				name=input('enter the number of your office:  ')
				first_office=office(name)

				empid=int(input('enter the no of employee you want to search for:  '))
				first_office.get_employee(empid)

		if(Number=='4'):


				db = MySQLdb.connect("localhost", 'root', '', 'office')
				cursor =db.cursor()
				sql_str= 'select max(id) from employees';
				# print('sql', sql_str)
				cursor.execute(sql_str)

				result = cursor.fetchone()
				print('please know that there is ',result,'employees in database')
				db.close()

				print('')

				print('please know that  the data in the employee table is:')
				print('1-full_name ')
				print('2- money')
				print('3-sleep_mood --> hours')
				print('4-healthrate --> meals')
				print('5-email --> name_ex@ex.ex')
				print('6-work_mood --> hour')
				print('7-salary')
				print('8-ismanage --> false or true')


				name=input('enter the number of your office:  ')
				first_office=office(name)


				Id=int(input('enter id:  '))
				fullname=input('enter fullname:  ')
				money=int(input('enter money:  '))
				salary=int(input('enter salary:  '))
				email=input('enter email:  ')
				is_manager=input('enter if he is manager or not:  ')
				meal=int(input('enter no of meals:  '))
				hours=int(input('enter no of sleeping:  '))
				hour=int(input('enter no of working:  '))

				
				# employee[value].sleep(hours)
				# employee[value].eat(hour)
				# employee[value].work(hours)
				employee=Employee(Id,fullname,money,email,salary,is_manager)
				first_office.hire(employee,hours,hour,meal)

		if(Number=='5'):
				name=input('enter the number of your office:  ')
				first_office=office(name)
				empid=int(input('enter the no of employee you want to fire:  '))
				first_office.fire(empid)

	else:
		num=int(input('please enter a valid number:  '))
		user(num)	
		

# main method has all options that  user can use from them 
def main():
	print('please enter a number from  this menu')
	print('1-fill your database')
	print('2-retrieve all data')
	print('3-retrieve one employee by id')
	print('4-hire an employee')
	print('5-fire an employee')

	print('')

	no=input('enter a number:  ')
	user(no)

x='y'	
while x=='y':
	main()
	x=input(' if you want to access anothe query please enter y if no enter n:   ')

