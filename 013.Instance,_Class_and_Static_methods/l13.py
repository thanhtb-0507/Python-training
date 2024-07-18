# Instance,_Class_and_Static_methods

"""
Instance method:
	self: tu truy cap chinh no
	Instance point to the object
Class method:
	cls: truy cap vo class 
	Class method point to the class
Static method:
	special, not using obj or class
	just an ordinary function

When to use?
	instance: khi muon tham chieu va thay doi trang thai
	class-m: truy cap vo class hien tai (hay su dung)
		tra lai nhu 1 ham constructer
	static: namespace - gom nhom cac method lien quan ()
"""

class MyClass:
	def instance_method(self):
		return "Instance method called.", self, self.__class__

	@classmethod # decorator
	def class_method(cls): # cls = class
		return "Class method.", cls

	@staticmethod
	# if no def appear then:
	# 		IndentationError: unexpected unindent
	def static_method():
		return "Static method."

a = MyClass()
print(a.instance_method())
# ('Instance method called.', <__main__.MyClass object at 0x7f97cd04bd30>, <class '__main__.MyClass'>)

print(MyClass.class_method())
# ('Class method.', <class '__main__.MyClass'>)

print(MyClass.static_method())
print(a.static_method())

