#define PY_SSIZE_T_CLEAN
#include <Python.h>
void print_python_bytes(PyObject *p)
{
	Py_ssize_t l, i;
	char *str;

	if (PyBytes_Check(p))
	{
		l = PyBytes_Size(p);
		str = PyBytes_AsString(p);
		printf("%s", "[.] bytes object info\n  size: ");
		printf("%d%s", (int)l, "\n  ");
		printf("%s%s", "trying string: ", str);
		printf("%s", "\n  first ");
		if (l > 10)
			l = 10;
		if (l != 10) 
			printf("%d%s", (int)l + 1, " bytes: ");
		else
			printf("%d%s", (int)l, " bytes: ");
		for (i = 0; i <= l; i++)
		{
			printf("%02x", str[i]);
			if (i != l)
				printf("%s", " ");
		}
		printf("\n");
	}
	else
		printf("[ERROR] Invalid Bytes Object\n");
}
char *return_type(PyObject *p)
{
	char *res;

	if (PyList_Check(p))
		res = "list";
	if (PyTuple_Check(p))
		res = "tuple";
	if (PyFloat_Check(p))
		res = "float";
	if (PyLong_Check(p))
		res = "int";
	if (PyBytes_Check(p))
		res = "bytes";
	if (PyUnicode_Check(p))
		res = "str";
	return (res);
}
void print_python_list(PyObject *p)
{
	Py_ssize_t i, n;
	PyObject *item;

	n = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", (int)n);
	printf("[*] Allocated = %d\n", (int)n);
	if (n > 0)
	{
		for (i = 0; i <= n - 1; i++)
		{
			printf("Element %d: ", (int)i);
			item = PyList_GetItem(p, i);
			printf("%s\n", return_type(item));
			if (PyBytes_Check(item) || PyUnicode_Check(item))
				print_python_bytes(item);
		}
	}
}
